## 1. Plan and ownership
- [x] 1.4 Independently accept October 1 amendment: direct upstream tag-to-draft lookup/ID upload/publication, fail-closed asset bound, SDK ownership and target/sysroot verification. Sol review accepted exact `34860298f7d2bbe80d90e375c341c879265b0719` and additive deltas `cba1d609db40ff0099eaeca7011e625f586dabb8`; implementation qualification remains separate.
- [x] 1.1 Read current requirements, full REM-30 comments and central release/Manager contracts; reserve release-only paths with the coordinator.
- [x] 1.2 Inspect upstream implementations and run disposable ancestry/semantic version research without production tags.
- [x] 1.3 Complete proposal/design/deltas, strict validation and independent plan acceptance before implementation. Coordinator independently accepted `d7ea8ed5371018eb9e452ac550b1be5427f6bdda`, including the explicit REST file-count guard.

## 2. Action-based workflows
- [x] 2.1 Create isolated Rust/Manager branches from accepted main; read their AGENTS guidance and preserve other lanes. `work/rust-rem46` starts at `3df3b1e`; `work/manager-rem46` at `555421c`, both isolated `ci/rem-46-upstream-releases` branches.
- [x] 2.2 Configure upstream path/title/history filters and GitVersion with conservative exclusions and matching semantic rules. Real tool fixtures include executable files under documentation image/license directories.
- [x] 2.3 Replace coordinators with merged-PR admission, exact-source tag creation, ordered build/upload/publication and existing-tag recovery. October 1 composition uses direct GraphQL lookup, same-ID upstream upload and fixed official create/PATCH routes; old coordinator remains removed.
- [x] 2.4 Restrict custom helpers to actual build/package/version-integrity work; remove obsolete policy/orchestration/tool setup.
- [x] 2.5 Preserve required check names, docs-only completion/no compile, independent versions and REM-35 major guard.

## 3. Verification
- [x] 3.5 Strengthened actual-distribution fixtures reuse a draft beyond release-list page two with its same ID and zero duplicate POST; exercise GraphQL errors/malformed results, published pre-build skip, asset-count refusal, partial uploads and ID-based retry. Both four-test publisher suites pass at Rust `bb49e4f` / Manager `da240b8`; they do not establish semantic-version correctness. Actual downloaded 0.2.0 ARM ELF symbol/version requirements match the selected vendor SDK; all four provider hashes match coordinator-collected native hashes. Actual new-package/native behavior and hosted CI remain separately gated.
- [ ] 3.1 Exercise actual upstream distributions in isolated fixtures: semantic types/body/footer, docs/mixed/unknown/renamed paths, reverted history and missing history. Ordinary GitVersion6.8.2 history, actual dorny distribution and real Rust build.rs metadata fixtures passed locally, but the actual Windows and Linux GitVersion distributions fail the added same-second ancestry regression. Semantic-version qualification remains open.
- [ ] 3.2 Verify tag-before-build, wrong-SHA conflict, main advancement, reverse queue order, existing tag/draft retry, published skip and partial upload using mocked/local boundaries.
- [ ] 3.3 Validate workflow syntax/action inputs and run appropriate Rust/Manager build, package and metadata checks; no production test tags.
- [ ] 3.4 Obtain independent exact-code/spec review and required CI; inspect bot comments, reporting unavailable bot coverage honestly.

## 4. Coordinated delivery
- [x] 4.1 Publish linked Docs/Rust/Manager draft PRs with Summary-only bodies and detailed evidence in comments: Docs #5, Rust #29, Manager #2. Same-second GitVersion blocker is disclosed in all three comments; delivery remains unfinished.
- [ ] 4.2 Sync both canonical capabilities, archive only this completed change, validate and review the exact final revision set.
- [ ] 4.3 Coordinator squash-merges in reviewed order, verifies actual release/tag/runtime versions and docs-only skips, and updates REM-46/REM-35 handoff.
