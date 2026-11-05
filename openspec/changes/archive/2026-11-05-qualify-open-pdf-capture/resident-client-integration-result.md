# Resident client integration checkpoint

The latest compatibility candidate is Buddy
`5fcfad9bd3a315dabde996f005038dda95956474`, which pins SDK
`9880766f5bb0bdb91445716132703b02587d372e`. Historical requests now expose immutable
original bytes/revision/digest together. Journal loading checks original-byte
hashes and same-revision replies while preserving scope, sequence, operation and
exact insertion-result validation. Old records are never re-encoded for storage
or response correlation. Existing consumed operations and unresolved/observed
reservations survive the upgrade.

Independent source review accepted the consumer and its frozen original v1
fixtures. Ten Windows journal tests passed before the final Linux-only fixture
addition; final-source Windows strict all-target/all-feature Clippy passes after
correcting a conditional import. The Linux additions check original-fact read-only
reconciliation over strict v2 with an unchanged journal, replacement refusal and
malformed history refusing before a socket connection.

On October 25, the retained Linux run was confirmed complete: **546 passed,
3 ignored**, including all **15 resident journal/socket tests**. Its container
could not embed Git provenance, so it remains local development evidence.
The exact source commit separately passed all required hosted checks, application
build and integration in [Buddy CI 40144048485](https://github.com/s116821/ReMarkableBuddies/actions/runs/40144048485).
The pinned SDK passed [CI 40143522893](https://github.com/s116821/ReMarkableOpenSDK/actions/runs/40143522893),
and Docs `a89d53d5db3490aa1f385ba239f3080ffc32564b` passed
[CI 40144063933](https://github.com/s116821/RemarkableBuddiesDocs/actions/runs/40144063933).
Release jobs are intentionally skipped for these draft PRs. The compatibility
checkpoint is verified; earlier results below retain their original scope.

No installed Reader selection, journal reset, runtime activation or native
qualification is included. Historical capture `SDK_SOURCE` remains
`2d473f0954120889f8a04c6294151241576ff8c3`.

October 24, 2026. Buddy source `b06db07c5ff4558d4c269510ad4308985c635949`
pins SDK `095f6c73777195b2bee56321a81857346a76ebde`. This implements
[the consumer contract](resident-client-integration.md), not installed Reader
acquisition or native qualification.

The Store-owned local journal retains canonical insertion frames and original
operation/digest/source/target before SDK pending admission and socket write.
It survives Store generation restoration. Unresolved and observed attempts block
replacement insertion for their conversation; original operation identities
remain consumed even after a durably known predispatch/refusal outcome. The Linux
wrapper authenticates through the SDK Client and only reconciles the original
target. It creates no Ledger binding or rendering permission.

Independent source review found no blocker. The initial Windows eight journal
tests and strict Clippy passed. Linux eleven journal/socket tests passed, including
actual Store restart/generation restoration, lost reply and read-only original-target
reconciliation. Test-only publication faults cover refusal before reservation,
failure before reply retention, and reported error after successful retention.
Those runs used SDK transport revision `061fbf2`; the later SDK pin corrects its
package allowlist and component status documentation. The final consumer revision
also strengthens the original-digest assertion. Exact-final-source broader checks
are recorded separately when complete; earlier results are not relabeled.

A simultaneous broader Windows/Linux build exhausted host paging capacity
(Windows error1455). Its failure is retained. The owned Linux build was stopped
and the Windows check restarted with one Cargo job. This is a resource failure,
not a passing broader regression run.

Buddy's hosted checks were unavailable because newer main changes conflicted with
the preserved topic. The single-job pre-merge run was stopped before changing its
inputs; a normal preserving merge brings in the newer Reader/Ledger/sync behavior.
Independent review identified one required adaptation: historical binding lookup
must retain main's durable request-evidence validation without rereading current
heads. The merged implementation selects evidence/receipt pairs from its original
snapshot and reads only pinned immutable records/original transactions afterward.
The contract is amended accordingly; valid, orphan and replaced-receipt regressions
are required. The first merged build was stopped before this repair; final merged
verification remains pending.

The fixtures model publication error boundaries; they do not establish actual
power-loss behavior. Linux synchronization uses existing Store file/parent-directory
primitives. Windows fixtures do not prove Linux durability. Container Git metadata
warnings limit the local Linux output to development host evidence.

Native activation, reusable mutation qualification, current/adjacent recognition,
fresh target selection, Supervisor recovery, capture/write/persistence and the full
PDF/notebook/blank-start/Writer matrix remain open. This journal increment does not wire the installed Reader to native insertion or
selection. The preserving main merge includes newer Reader/Ledger behavior; the
historical capture SDK source pin remains unchanged. No tablet action occurred.
The coordinated changes remain active and draft; no archival follows this checkpoint.

Source basis: current implementation/specification files, directly observed local
test output and independent source review. Native findings remain in the original
handoff and are not reproduced as new results here.

## Merged consumer verification

The preserving merge and evidence adaptation are committed at Buddy
`6d23c7d3ef362c99f9d1bce4877b38f2ca247fa2`, with SDK still pinned to
`095f6c73777195b2bee56321a81857346a76ebde`. Independent review accepted the
snapshot-aware evidence check and regressions. The valid historical association
uses its original operation-head snapshot; orphan facts and replaced receipts
refuse after basic snapshot parsing, without a second current-head read.

The final merged Windows library suite passed **504 tests**, with 3 intentionally
ignored and no failures (`cargo test --locked --all-features --lib -j 1 --
--test-threads=2`). Compilation began before committing the reviewed sources,
so its embedded development Git metadata is not a clean-commit attestation.

The hosted Linux Checks job associated with that pushed head passed formatting,
strict all-target/all-feature Clippy, the full all-feature test suite, release
Python checks, npm audit and release workflow gates:
[CI 40140251341, Checks](https://github.com/s116821/ReMarkableBuddies/actions/runs/40140251341/job/121010337363).
The application artifact build was still running at this checkpoint; successful
Checks is not a claim that the entire workflow completed.

SDK `095f6c7` separately passed its full hosted workflow
[40138801562](https://github.com/s116821/ReMarkableOpenSDK/actions/runs/40138801562).
The earlier `061fbf2` workflow failed because its exact package allowlist omitted
the new transport source; `926526f` corrected that omission. That failure remains
historical evidence and is not relabeled.

The SDK's subsequent revision 2 selection protocol remains a separate unconsumed
increment. The consumer pin is intentionally unchanged: an upgrade must preserve
old canonical attempt bytes and original digests. No new native or power-loss
qualification follows from any of these source, owned-socket or hosted results.


The complete Buddy workflow 40140251341 subsequently finished successfully at
`6d23c7d3ef362c99f9d1bce4877b38f2ca247fa2`: PR title, Linux Checks, application
Build and Integration all passed; release was intentionally skipped for the PR.
Docs `b6e1e878a28bca2181e86b48e3c707c61c5b9c5d` passed
[40141239212](https://github.com/s116821/RemarkableBuddiesDocs/actions/runs/40141239212).
The coordinated PRs remain draft pending native/product gates.
