## Context

Authority: current REM-46/REM-30 descriptions and their four/two returned comments,
the September 26 release clarification and October 1 SDK/target/ownership updates.
Preserve REM-30 tag identity and REM-21 independent component releases. The October 1
resume supersedes historical pauses and usage stops. Current accepted bases are
Docs 8008389f, Rust ff8ad75b and Manager 555421ce. September research began on
Docs e7fbdc44 / Rust 3df3b1e6; saved checkpoint refs preserve that unmerged work.
Owned REM-46 branches are now rebased on accepted main, preserving REM-9/36.

## Goals / Non-Goals

### October 1 authority and qualification amendment

Fresh REM-46 and REM-30 descriptions and all returned comments were audited
(four and two respectively, no further pages or returned inline/reply anchors).
October 1 user resume supersedes historical 90%-used stopping text; ordinary
allowance may be exhausted, without reset redemption or overage credits.
Non-SDK work and independent reviews use GPT-6.1 Sol. Accepted dependency bases
are Docs `8008389fa676d395401e6f28e049b47baa7b10ef` and Rust
`ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`; preserve their storage delivery.

Canonical repository names are ReMarkableBuddiesDocs, ReMarkableBuddiesManager,
ReMarkableBuddies and ReMarkableOpenSDK. SDK API, native compatibility, canonical
OpenSpec and SDK releases belong to its independent repository, outside REM-46.
Buddy/Manager product integration and release workflow contracts remain here.
One Buddy semantic tag may produce RM2 ARMv7 and Paper Pro AArch64 artifacts from
one source tree, built against their appropriate SDK target. Manager retains its
independent version/cadence and installs the compatible Buddy artifact without a
separately installed SDK runtime. Building AArch64 does not prove Paper Pro native
qualification; REM-29 remains its hardware validation gate.

Proposed publisher amendment, pending independent plan acceptance and actual
distribution qualification: official `octokit/graphql-action` v3.0.2
(`ddde8ebb2493e79f390e6449c725c21663a67505`) performs a fixed declarative
`repository.release(tagName)` lookup. Validate repository and returned release
identity/state before build; null release alone means absent. Upstream GraphQL
errors must fail even with HTTP 200. A published result skips all app build and
release writes. An existing draft reuses its database ID regardless of its age
or release-list position; no list pagination or duplicate create request occurs.
Only an absent release invokes official request-action's fixed draft-create route.
Validate its ID/tag/draft result and carry that same ID through the DAG.

Primary upstream support for draft visibility: GitHub CLI's
[draft-release lookup](https://github.com/cli/cli/blob/fbda842467a0140d9e1f29b85b44db16493c7bd6/pkg/cmd/release/shared/fetch.go#L219)
uses the same direct GraphQL tag query to obtain a draft database ID before its
REST lookup by ID. The October 1 live schema/read-only published-release check
confirms query fields; actual pinned Action fixtures additionally verify draft,
absence and HTTP-200 error handling. No production draft was created for research.

`AButler/upload-release-assets` v4.0.0
(`34491005a5d7ec239a784e460807ce844fde7962`) accepts the explicit release ID and
uploads build-verified packages. Its asset discovery only reads one page: this
candidate must therefore qualify and enforce a bounded draft asset inventory
before any upload, refusing unsupported counts rather than silently overlooking
an existing asset. No custom pagination client is permitted. Revalidate draft
identity/state before uploads and publication using fixed upstream API requests.
Publish by fixed request-action PATCH to the same ID only after all uploads pass.
Partial failures retain the draft; unexpected observations stop before app build
or writes. Native concurrency serializes supported workflow attempts; this does
not claim atomic protection against an external actor editing a release.

Build-only verification must record selected SDK/sysroot identity and qualify ELF
architecture/interpreter and required runtime symbol versions against the supported
target baseline. Fresh coordinator read-only evidence reports supported RM2 firmware
3.28.0.172 uses glibc 2.39; an older emulator's refusal is not device incompatibility
evidence. Do not impose an inferred older ABI ceiling or modify historical assets.
Cross/emulated checks and native qualification remain explicitly distinguished.

Goals: upstream release logic; exact tag/source/binary agreement; no docs-only
compile or tag; deterministic feature/fix/breaking versions; visible bounded failure
and safe retries. No generated version commits, alternate app-version authority,
new hosted service, custom release engine, production experiment tags or settings
changes. App functionality and deployment to the tablet are outside this change.

## Decisions

### Current qualification checkpoint: unfinished

The ncipollo checkpoint was rejected by actual old-draft recovery fixtures and
preserved for history. The October 1 official GraphQL/request and explicit-ID
upload composition now passes actual-distribution/workflow-expression fixtures in
both components, including old draft reuse, partial uploads, published skips and
malformed observations. Build-only ELF/sysroot verification is implemented; actual
tagged package verification, hosted CI and final independent review remain gates.
No production release was changed. Do not sync/archive this unfinished delivery.

### 1. Use maintained Actions with explicit responsibilities

Candidate composition, pinned to inspected immutable revisions before delivery:

| Responsibility | Upstream mechanism |
| --- | --- |
| Changed-file selection | dorny/paths-filter v4.0.3 (`ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d`) with explicit documentation exclusions and conservative unknown-path handling |
| Semantic PR title | Existing amannn/action-semantic-pull-request, with application titles excluding docs and public scopes allowed |
| Version selection | GitTools/actions v4.7.0 (`7417b1089e2c7de93510f1901d656ddf60bb024f`), GitVersion 6.8.2, TaggedCommit/Mainline strategies and conventional-message configuration |
| Immutable tag creation | Pinned upstream tag-only Action on Linux, with force disabled and exact commit supplied; candidate rickstaa/action-create-tag v1.7.2 (`a1c7777fcb2fee4f19b0f283ba888afa11678b72`) |
| Exact release observation | Proposed official octokit/graphql-action v3.0.2 direct tag query, validated identity/state and fail-closed results |
| Draft/assets/publication | Proposed official octokit/request-action v3.0.0 (`b91aabaa861c777dcdb14e2387e30eddf04619ae`) fixed create/PATCH routes and AButler explicit-ID upload, pending strengthened qualification |
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

After successful tag creation, the proposed official Octokit GraphQL Action observes
the exact release by tag, including its draft state, database ID and asset count.
Network/authentication/GraphQL errors or malformed repository/release observations
stop the run. A validated published result skips all draft/build/publication steps;
a validated draft reuses its ID and only explicit null release permits creation.
An REST release-by-tag 404 alone does not prove draft absence. The query/routes and
checks are declarative Action inputs/expressions, not an embedded API client or
custom query loop. Build jobs run only for an unfinished draft,
checkout the exact remote tag, and produce the two Rust packages or the existing
browser/Windows/Linux Manager packages with matching embedded version and provenance.

Upload all validated artifacts while the release remains draft. Only a final
upstream action step changes `draft` to false after all uploads succeed. A failed
build/upload leaves a recoverable draft; completed published assets are untouched.
Use upstream semantic/latest-release behavior rather than a custom latest pointer.

The initial ncipollo v1.21.0 candidate reads only the first releases page for draft
discovery. Current softprops v3.0.3 bounds discovery to two pages, so it only shifts
that recovery failure. The proposed softprops v2.5.1 pin was rejected by independent
review: its async iterator exists but is unused; the actual lookup returns no
release on a direct 404. The earlier inference that absence of a scan bound implied
complete pagination was incorrect. A strengthened actual-bundle fixture rejects a
duplicate create for an existing page-three draft and fails on that pin, confirming
the source review. A production-dependency audit additionally reports advisories;
do not downgrade as a workaround without resolving compatibility/security findings.

Qualify the October 1 upstream composition with an actual-distribution fixture
that checks the same draft ID despite release-list placement beyond page two and
no duplicate POST. Direct upstream tag lookup may avoid listing entirely; the
requirement is complete recovery, not a mandated pagination algorithm. Fail all
unexpected observations. No private query loop or coordinator is allowed.

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


### October 1 implementation blocker: equal commit timestamps

The actual checksum-verified GitVersion 6.8.2 Windows and Linux distributions
fail two deterministic cases in `release/test_versioning_equal_dates.py` in both
component branches. Three linear commits at the same timestamp (baseline
`v0.1.17`, `feat(REM-46)`, `fix(REM-46)`) yield `0.2.0` for the fix instead of
`0.2.1`. Tagging the later fix `v0.2.1` and checking out the earlier feature yields
`0.2.2` using the descendant tag instead of `0.2.0`. The reported source SHA still
matches HEAD, so the existing SHA guard does not detect the wrong version.
Hosted Linux fixtures surfaced the defect; ordinary slower local fixtures pass.
Do not stagger dates or weaken assertions to claim this is qualified.

Source inspection shows that [current-branch selection uses commit time](https://github.com/GitTools/GitVersion/blob/6.8.2/src/GitVersion.Core/GitVersionContext.cs#L23),
and [its prior-commit filter skips by date](https://github.com/GitTools/GitVersion/blob/6.8.2/src/GitVersion.LibGit2Sharp/Git/CommitCollection.cs#L22).
Those lines are relevant evidence, not proof that a private workaround is safe.
No maintained-upstream configuration remedy has been qualified. The selected
version action is therefore provisional; publication remains blocked and the
change stays active. A replacement composition or changed upstream pin requires
an explicit design delta and independent acceptance before implementation.

### October 8 downstream package contract and targeted upstream follow-up

The later REM-41/42/35 descriptions supersede the earlier two-installer proposal:
Vellum/apk owns one tablet-side Buddy package from the first Manager release.
Official signed local APKs originate from verified Git-tagged GitHub assets;
public catalog acceptance is not a release prerequisite. REM-41 owns packaging,
installation and source handoff. REM-55 owns delayed post-1.0 public listing.
This is a downstream artifact contract, not a replacement release engine or a
reason to bypass the unfinished REM-46 gates. Package `pkgver` derives from the
exact Buddy tag, and `pkgrel` is packaging-only metadata. Official and eventual
community sources must preserve the same package identity/ownership database.
Equal version strings alone do not establish signed package equivalence.

Fresh upstream inspection found GitVersion commit
[`17cc645b`](https://github.com/GitTools/GitVersion/commit/17cc645b19c60dbad8a2fa3cc080cc51ba52dc7f)
introducing branch-environment overrides as checkout context. Its contextual
branch uses history reachable from the checked-out tip without moving a physical
branch ref; `GitVersionContext` bypasses the timestamp filter for that context.
This is a concrete candidate for the held detached/equal-date regression, not a
verified fix. On October 8 the latest published upstream release remains 6.8.2.
The next bounded investigation is the unchanged equal-date regression against
an exact upstream source build with its documented branch context, checking both
expected versions, exact SHA and unchanged refs. No private upstream patch,
production pin change, tag mutation or acceptance weakening follows from this
finding. A usable maintained distribution and independent qualification remain
required before selecting a replacement composition.
