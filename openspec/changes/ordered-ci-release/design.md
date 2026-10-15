# Ordered checks, immutable artifacts and final publication

## Authority and ownership

REM-56 and the October 15 Things to Fix version111 instruction supersede the
older tag-before-build ordering. This change owns Buddy/Manager and central Docs.
SDK tooling source and its own contracts remain SCRAPPY-owned. Implementation
starts from Buddy ff8ad75, Manager 7ff5167 and Docs 7686a67, avoiding a cumulative
import of unfinished REM-46 candidates. Old branches, equal-date regressions and
upstream failures remain available; no previously failed case is reclassified.

## Workflow DAG

Each component has checks -> build -> artifact integration -> release. Checks
include maintained path filtering, scoped semantic-title validation, formatting,
lint, unit tests and release-tool qualification. Build cannot start on failed,
skipped or canceled required checks. Integration downloads and exercises exactly
the build outputs, with no substitute compilation in that phase. Only the final
dedicated release job has contents-write permission. It requires every required
predecessor to have succeeded and an eligible canonical-repository main push.
PRs/forks never tag or publish. Documentation-only changes finish noncompiling
checks and skip application build/integration/publication.

Docs keeps portable checks and strict OpenSpec validation with explicit ordering,
read-only permission and no application/release job. Standalone semantic-title
checks may remain required PR checks; there is no separate policy release path.

## Maintained version and publication tools

Use maintained upstream path filters and semantic parsing, not a new release
coordinator in Python, JavaScript or shell. Python Semantic Release10.7.0 is an
already qualified SDK candidate: its read-only version --print-tag supplies a
candidate, with empty source-version declarations and no changelog/version commit.
Buddy/Manager retain their own tested policy, including feat/minor, maintenance/
patch and explicit breaking/major behavior at0.x. A computed1.0 candidate remains
blocked pending REM-35. The known GitVersion6.8.2 equal-timestamp defect and failed
upstream-source candidate remain recorded; changing test timestamps is forbidden.

Final tagging uses maintained tag-only capabilities after gates, without running
another app build. Maintained publisher Actions handle lookup, draft/upload and
finalization. Prefer already qualified exact-ID recovery/upstream source-built
publisher primitives; unsupported pagination/retry behavior must fail a focused
fixture rather than produce a private publication engine. Dependencies, source,
license and emitted publisher bytes remain pinned and audited. The original SDK
candidate security failures are not removed or waived by this change.

## Candidate identity and artifact handoff

Candidate calculation is read-only and freezes source SHA, candidate tag/version
and build profile. Build helpers validate clean exact source, reject conflicting
metadata and inject generated version metadata without a source version field or
early official tag. These files are unpublished candidates until final remote-tag
and release proof; a candidate name or embedded value alone is not release trust.

Build outputs include exact inventory/checksum/source/candidate provenance.
Integration verifies identity and executes supported built-artifact paths:
Buddy target version/ELF/package controls and Manager browser/desktop packages.
It must not call a build command that silently substitutes another binary.
The release job downloads the same outputs, verifies their inventory/digests and
rechecks candidate/source before creating an immutable remote tag. A missing,
conflicting or stale candidate refuses. No version substitution or rebuild is
allowed between integration and publication. Normal dev builds remain distinct.

## Queue, failure and retry

Use native upstream workflow concurrency to serialize main release runs; do not
depend on a GITHUB_TOKEN tag push waking a second workflow. Each run stays bound
to its admitted main SHA even after main advances. Failed predecessors leave no
new official tag or draft/release. A later successful commit cannot retroactively
publish a failed predecessor; upstream semantic history determines its candidate
from existing immutable tags. This replaces the bespoke unreleased-history loop.

A final-job retry reuses verified build artifacts and exact tag/source identity.
Existing published bytes are verified, never overwritten or retagged. Recover a
partial draft only after retained assets match independently expected digests;
upload missing bytes and finalize only after the complete set verifies. Expired
artifacts require a new checks/build/integration run for the same source and must
not be called the original verified bytes. Conflicting remote tags/assets refuse.

## Verification and remaining gates

Focused fixtures exercise real maintained tools in disposable Git/loopback
services: semantic and equal-date histories; docs/mixed/unknown paths; failed,
skipped and canceled predecessors; no early tag/API mutation; build-to-integration
byte ownership; wrong SHA/candidate; concurrent main advancement; existing draft,
partial upload and retry. Validate workflow syntax and actual hosted builds and
artifact integration. No production tags/releases/settings experiment is allowed.
Source/package qualification is separate from native compatibility, real-provider
behavior, remote platform immutability, SDK first release and REM-35 readiness.

Source basis: current human note/REM-56, REM-46/50 chronology and preserved source,
current main/candidate workflows, SDK maintained-tool qualifications, and upstream
Python Semantic Release command documentation. This document precedes code.

## Resolved integration details

Canonical events are push:main, with PR events for premerge checks; no new
pull_request_target dependency is introduced. The metadata job requires one
first-parent main commit in push.before..github.sha; zero/unknown, non-forward or
ambiguous batch history refuses before compilation/tagging. This keeps dorny's
supported base/ref filtering without a private touched-history classifier.
The final associatedPullRequests proof accepts the exact merged SHA, including
squash merges; a direct push cannot publish. The reusable caller permission
ceiling permits the final job's contents:write, while every actual preceding job
remains contents:read; final metadata proof also has pull-requests:read.

The selected uploader is unmodified Svenstaro2.11.5 source29e53e9, source-built
with the full audited minimal build/runtime lock40d12ef7. The source's empty Jest
placeholder and unused ts-jest/lint graph are omitted transparently. Original
full/range/Jest30 scans remain41/34/20 advisories; selected closure is0 at the
recorded scan, not a proof of security or a waiver of SDK's original gates.
Exact lookup/request Actions supply an ID; only verified missing names are sent
with overwrite:false/check_duplicates:true/draft:true/promote:false. ID404 may
create a replacement draft upstream, and outside publication may be reverted to
draft upstream; final same-ID/complete-byte proof prevents our finalization of a
replacement. There is no atomic external-writer claim. This avoids both the old
uploader's same-name DELETE and softprops' two-page draft scan without a fork.

The existing Manager build-info four-field wire format remains unchanged.
Its official:true denotes the controlled release-build recipe; absent remote tag
and verified complete release it is an unpublished CI candidate, not trusted
publication, installation or provenance by itself. Parent reconciliation of
unmerged Manager consumers that hash-import old release/coordinator.py is
explicitly required; this main-based change does not silently claim compatibility.
