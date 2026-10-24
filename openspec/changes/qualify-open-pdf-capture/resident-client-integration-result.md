# Resident client integration checkpoint

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

The fixtures model publication error boundaries; they do not establish actual
power-loss behavior. Linux synchronization uses existing Store file/parent-directory
primitives. Windows fixtures do not prove Linux durability. Container Git metadata
warnings limit the local Linux output to development host evidence.

Native activation, reusable mutation qualification, current/adjacent recognition,
fresh target selection, Supervisor recovery, capture/write/persistence and the full
PDF/notebook/blank-start/Writer matrix remain open. The legacy installed Reader path
and historical capture SDK source pin remain unchanged. No tablet action occurred.
The coordinated changes remain active and draft; no archival follows this checkpoint.

Source basis: current implementation/specification files, directly observed local
test output and independent source review. Native findings remain in the original
handoff and are not reproduced as new results here.
