## Context

Authority: REM-46 and the September 26 user clarification, preserving REM-30's
tag-centric requirements and REM-21's independent component releases. Full REM-30
description and two timestamped comments were read; the historical pause was
superseded by the explicit roadmap resume. Current public baseline is Docs e7fbdc44,
Rust 3df3b1e6 and Manager 555421ce. REM-9 and other active lanes are preserved.

## Goals / Non-Goals

Goals: upstream release logic; exact tag/source/binary agreement; no docs-only
compile or tag; deterministic feature/fix/breaking versions; visible bounded failure
and safe retries. No generated version commits, alternate app-version authority,
new hosted service, custom release engine, production experiment tags or settings
changes. App functionality and deployment to the tablet are outside this change.

## Decisions

### 1. Use maintained Actions with explicit responsibilities

Candidate composition, pinned to inspected immutable revisions before delivery:

| Responsibility | Upstream mechanism |
| --- | --- |
| Changed-file selection | dorny/paths-filter v4.0.3 (`ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d`) with explicit documentation exclusions and conservative unknown-path handling |
| Semantic PR title | Existing amannn/action-semantic-pull-request, with application titles excluding docs and public scopes allowed |
| Version selection | GitTools/actions v4.7.0 (`7417b1089e2c7de93510f1901d656ddf60bb024f`), GitVersion 6.8.2, TaggedCommit/Mainline strategies and conventional-message configuration |
| Immutable tag creation | Pinned upstream tag-only Action on Linux, with force disabled and exact commit supplied; candidate rickstaa/action-create-tag v1.7.2 (`a1c7777fcb2fee4f19b0f283ba888afa11678b72`) |
| Published-release observation | octokit/request-action v3.0.0 (`b91aabaa861c777dcdb14e2387e30eddf04619ae`), one fixed GET route and declarative status guards |
| Draft/assets/publication | softprops/action-gh-release v2.5.1 (`71d29a04ae7c63895f38299d7a5e05d238f7f445`), deliberately retained complete draft pagination |
| Handoff between build jobs | actions/upload-artifact and download-artifact with exact run-local artifact names and missing-artifact failures |
| Scheduling | Native Actions dependencies, bounded timeouts and concurrency `queue: max`, without canceling active releases |

These are inputs/configuration and ordinary DAG conditions, not an embedded API
script or custom policy/version loop. Verify the selected tag Action's exact
distribution and retry behavior before adoption. If an unavoidable upstream gap
requires more custom scope, report the concrete gap before implementing it.

GitVersion research ran its checksum-verified 6.8.2 executable against disposable
local repositories: scoped feat/minor, fix/patch, queued feature then fix, older SHA
after a descendant tag, tagged retry, docs-path exclusions (even with a feat title),
body example versus real subject, zero-major breaking header, breaking footer and
edit/revert history all produced expected versions. This is version-selection
evidence only, not end-to-end hosted workflow proof. The experiment tagged only its
temporary local fixture. No production release files were changed for research.

Alternatives inspected: mathieudutour/github-tag-action v7 has useful path filtering
but chooses the globally highest tag rather than target ancestry and refuses tag
writes in PR events; it alone cannot meet out-of-order per-merge recovery. The
PaulHatch semantic-version Action has per-commit ancestry support, but its shared
subject/body pattern handling is less direct for the strict conventional contract.
Release-PR version-bump commits are excluded by the user's source-of-truth rule.

### 2. Admit one merged PR, then build its immutable source

Release admission uses `pull_request_target: closed` targeting main, guarded by
`merged == true`, selecting the actual squash `merge_commit_sha`. This uses the
trusted base workflow and supports merged contributions from public forks, unlike
the read-only fork token on `pull_request`. Never checkout or execute an unmerged
PR head, fork ref or mutable branch; assert that the selected commit is reachable
from fetched main. Grant write permission only to tag/publication jobs and keep
build jobs read-only. Unmerged closures and docs-only changes do not
invoke the publication workflow. This preserves one independently recoverable run
per merged PR, avoiding a custom scan/replay loop when multiple main merges queue.
Main-push CI remains non-compiling; PR CI still builds development artifacts when
application files change. Direct commits outside the required PR/squash workflow
are not silently treated as completed releases; document the explicit recovery path.

Use a complete checkout at the selected SHA. GitVersion derives each version from
that SHA's tagged ancestry and relevant conventional history, so a later queued
merge running first cannot allocate its version to an older SHA. Do not derive the
application source from current main after waiting. Fail if version output's source
identity differs from the admitted SHA or history is shallow/unavailable.

Only the upstream tag step creates tags. It may reuse an existing identical tag,
never move it. Re-check the fetched remote tag against the admitted SHA before any
application compilation. Default GITHUB_TOKEN is sufficient for the ordered job
chain; do not depend on its tag push triggering another workflow.

### 3. Documentation filtering and conventional classification

Everything except an explicit small list of documentation paths is app-relevant.
Keep scripts/fixtures under docs, dependencies, build definitions, unknown paths,
renames and mixed docs/code relevant. Use upstream filtering for PR and release
admission; no local classifier script. Reject an application PR's docs or unsupported
title before merge/tagging. Required checks finish on docs-only PRs without a build.

GitVersion `ignore.paths` also excludes documentation-only commits from history:
the whole commit is ignored only when every changed path is documentation. Scoped
feat increments minor, fix/maintenance patch, `!` or BREAKING CHANGE major even at
0.x. Anchored patterns distinguish the subject from examples in a commit body. Keep
the current REM-35 guard blocking premature major publication; test calculation
separately from publication authorization. No `next-version` or authoritative
Cargo/package version is introduced.

Filters in different upstream configuration syntaxes must agree. Hermetic tests
exercise their actual distributions against the same path and history cases,
including renamed/deleted executable fixtures and a change followed by its revert.
API truncation or incomplete history must fail rather than silently classify docs.
The pinned paths-filter paginates but does not detect GitHub's 3,000-file REST
ceiling. A declarative job admission assertion therefore requires the merged PR's
reported `changed_files` to be present, greater than zero and less than 3,000 before
classification. Missing/zero/at-cap/over-cap counts fail visibly before tagging or
compiling; split oversized PRs rather than treating incomplete observations as docs.
Use this same conservative bound for required PR classification. Do not override
the event context or pretend the Action enforces this check. Fixtures exercise the
actual pinned Action's multipage/rename behavior and the workflow boundary at
2,999/3,000/3,001/missing counts. This is a small input-completeness assertion, not
a custom path classifier or API pagination implementation.

### 4. Recoverable publication without a coordinator

Use a driver and reusable publication workflow. Only admitted application merges
enter the publication queue; `queue: max` avoids default pending-run replacement.
GitHub does not promise commit-order execution, so correctness relies on per-SHA
version calculation, immutable identity checks and separate artifact namespaces,
not assumed FIFO. Queue limits/cancellation remain visible failed or cancelled runs
which can be rerun; do not label them released or silently substitute a later SHA.

After successful tag creation, the official Octokit request Action observes the
release-by-tag endpoint. Only 200 and 404 are accepted: missing status, network,
authentication and other API failures stop the run. A published 200 response skips
all draft/build/publication steps; a draft response or 404 allows draft discovery.
The route and status checks are declarative Action inputs/expressions, not an API
client, custom query loop or release engine. Build jobs run only for an unfinished draft,
checkout the exact remote tag, and produce the two Rust packages or the existing
browser/Windows/Linux Manager packages with matching embedded version and provenance.

Upload all validated artifacts while the release remains draft. Only a final
upstream action step changes `draft` to false after all uploads succeed. A failed
build/upload leaves a recoverable draft; completed published assets are untouched.
Use upstream semantic/latest-release behavior rather than a custom latest pointer.

The initial ncipollo candidate was rejected after implementation research found
that its draft search reads only the first releases page. Current softprops v3.0.3
also bounds draft discovery to two pages, so it only shifts that recovery failure.
Pin softprops v2.5.1, the latest inspected version with complete async pagination;
v2.5.2 introduced the limit. Its declared Node20 runtime is run with GitHub's
Node24 compatibility override and the actual distribution is tested on Node24.
Before any future Action upgrade, retain the fixture with an existing draft on
page three and verify that it is reused without another release creation. This
deliberate compatible pin avoids shipping a private pagination implementation.

Recovery is an Actions rerun of the original merge or manual dispatch naming an
existing stable tag. Manual recovery does not invent a version, move a tag or tag
current main. Historical failure is not automatically replayed by a docs push;
each unfinished release remains visible and recoverable independently. This replaces
the old coordinator's automatic backlog replay; it preserves the required explicit
manual recovery and prevents missing tags caused by pending-run replacement.
Test completed-release skip, draft retry, later main advancement, wrong-SHA tag,
multiple queued merges and partial publication before claiming equivalence.
Keep workflow/tooling at its reviewed revision when recovering an older tag, while
the app source is separately checked out at that exact tag. A historical app tag
must not need to contain the new release workflow or build wrapper to be recoverable.

### 5. Keep application-specific build code only

Keep Rust vergen/git metadata and the manifest placeholder; retain or simplify its
exact-tag/version/provenance verification. Manager similarly embeds Git-derived
metadata without a manually incremented package version. Local/PR builds retain
clear dev labels. Build/package helpers may invoke compilers, create archives,
verify binary metadata and produce checksums/provenance, but may not choose versions,
filter commits, create GitHub refs/releases or orchestrate retries.

Delete obsolete coordinator/policy files, release-it/git-cliff tool downloads and
tests which solely mirror those removed implementations. Retain meaningful fixture
coverage by exercising the actual upstream tools and workflow boundary, plus normal
Rust/Angular/Electron checks. No tablet or paid model test is needed for CI-only code.

## Delivery / risks

One central change and linked Rust/Manager PRs, reviewed as an exact revision set.
Publish evidence in comments, preserve Summary-only bodies, inspect available bot
feedback and disclose the existing cap. Only completed work is synced/archived.
Coordinator alone squash-merges after final review; verify first actual component
releases and docs-only main skips. Never rewrite historical tags/assets. Docs itself
has validation only. REM-46 blocks REM-35; foundation completion remains distinct
from full MVP/1.0. Public local tests/manual procedures require no private Linear.

Primary references: [GitVersion configuration](https://gitversion.net/docs/reference/configuration),
[GitTools Actions](https://github.com/GitTools/actions/tree/v4.7.0),
[paths-filter](https://github.com/dorny/paths-filter/tree/v4.0.3),
[tag Action](https://github.com/rickstaa/action-create-tag/tree/v1.7.2),
[release Action](https://github.com/softprops/action-gh-release/tree/v2.5.1),
[request Action](https://github.com/octokit/request-action/tree/v3.0.0),
[merged PR events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#running-your-pull_request_target-workflow-when-a-pull-request-merges),
[GitHub concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
