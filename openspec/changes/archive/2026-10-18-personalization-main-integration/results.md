# Integration evidence

This is the independent-main successor of configuration PR39 and Docs PR28.
Pre-code design was committed as `cb74fbf` before implementation. Source
`daa4ea5` records both prior owned source `214db007` and current main `f1d697ce`
as parents; previous source history and other feature branches remain intact.

The source diff against current main contains seven paths: configuration,
personalization, CLI dispatch, the shared Store lease, its existing Linux lease
regression's field access, the new maintenance constructor and focused tests.
No SDK dependency, Cargo lockfile, pipeline or Reader/provider implementation is
imported from the old stacked branch.

On Windows with Rust 1.98.1, the final focused run passed 14 tests: four CLI unit
controls, eight filesystem/actual-process personalization controls and two
adjacent configuration controls. Compilation took 11.59 seconds on the second
run; test groups took 0.01, 1.93 and 0.01 seconds respectively. The initial run
had seven of eight personalization tests pass; its new fixture snapshot tried to
read the exclusively locked zero-byte lock file on Windows. The fixture now
checks that known empty file's metadata while retaining byte-for-byte comparison
of every other file. Production code was unchanged by that test correction.

The new controls cover missing identity/lock/current/owner/format/directories,
foreign ownership, unsupported generation format, nil generation and corrupt
commits; refusal leaves the directory tree and configuration unchanged. A later
actual child command succeeds after rejection, demonstrating lease release.
An already held owner refuses a child command as busy. Successful maintenance
retains exact Unicode, line endings, immutable prior snapshots and existing data.

Formatter and strict all-target/all-feature Clippy passed on the final source.
The final source preserves all 297 unrelated current-main entries, including
their Git mode, type and blob. The integrated Docs tree preserves all 279
unrelated main entries and all six files of the prior accepted archive unchanged.
Local Docs tests passed 12 controls; guidance verified 22 current files and 126
preserved source blobs. Strict OpenSpec passed 31 items after canonical sync.

Independent source review found no actionable issues at
`daa4ea533321bed5643c91124b107fe05e3aa8b3` in
[Buddy review 5560689712](https://github.com/s116821/ReMarkableBuddies/pull/39#pullrequestreview-5560689712).
The paired spec review accepted `4c99aec94cea2c4c5249398b38d61d2199749ddf` in
[Docs review 5560689753](https://github.com/s116821/ReMarkableBuddiesDocs/pull/28#pullrequestreview-5560689753).
The reviewer independently checked scope preservation, lease ownership,
read-only recovery, failure cleanup, pre-code chronology and exact spec sync.
It did not repeat the owner's tests or perform tablet operations.

[Docs CI 39080399564](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/39080399564)
passed OpenSpec and portable Ubuntu/Windows jobs at that spec revision.
[Buddy CI 39080395596](https://github.com/s116821/ReMarkableBuddies/actions/runs/39080395596)
passed all four required PR jobs: PR Title, Checks, Build and Integration.
Publication was correctly skipped on the PR. The hosted Linux run passed all
reported Rust test groups, including 159 library tests, and 13 release-tool tests.
The build used the actual temporary PR merge
`c993463f7b3d59044002f218c22918aa334696c7`, with candidate version `0.5.0`.
Downloaded artifact `12119121017` is 16,100,652 bytes; its ZIP SHA256 is
`b797dc5e50d23f42895e00fda1db0641e2c7ac06913929cdffff317e4cb7c9a5`.
Both package digests match its provenance manifest. Integration consumed the
retained ARMv7/AArch64 packages under the pinned cross-image emulators without
an application rebuild. This PR candidate is not a published release.

Only this new integration change is archived after the explicit canonical sync.
Its final archive delta must receive narrow independent review and green Docs
checks before the coordinated merges below; source and canonical contracts are
unchanged by that lifecycle step.

Final local lifecycle validation passed 30 strict OpenSpec items; guidance
validation again verified 22 current files and 126 preserved source blobs.
The archive command used its date `2026-10-18`. Its non-blocking proposal-header
warning was corrected by adding the standard Why/What Changes headings around
the unchanged pre-code prose; design and both delta specs are unchanged.

These are host filesystem/CLI results, not tablet, live-provider, running-runtime
activation, Writer or whole-personalization qualification.

## Coordinated delivery and verification

After source CI and final lifecycle review pass, normally squash-merge Docs PR28
then Buddy PR39, matching the reviewed branch heads. Do not bypass required
checks or change repository settings. After both merges, verify the actual main
commits, the Docs checks, and all four application jobs (Checks, Build,
Integration, Release). Verify the published annotated tag resolves to the exact
Buddy merge, and that downloaded release assets match the completed build's
manifest and source identity. Record those post-merge observations in the PR
discussion and canonical issue; a prepared handoff is not proof of publication.
The broader personalization issue remains open for its runtime and product work.
