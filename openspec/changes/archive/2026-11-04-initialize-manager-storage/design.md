# Explicit configured storage preparation consumer

## Existing evidence

The canonical host-sync-mode and archived operate-host-sync-mode define the
already-delivered no-input Initialize selector. The exact4eeaabef source/reference
module calls Config::load, refuses enabled legacy sync, then Store::open and
finish(Initialize). Store::open permits normal creation/recovery; it is distinct
from inspect/choose's existing-only opener. Output holds Store/current-mode leases
through write_all of one consuming report. This is not an independent flush or remote-effect settlement guarantee. No original operation receipt is created.

Manager's current saved-mode parser accepts operation inspect only. Local-only
choice accepts inspect/choose and requires an original conditional token. Their
wires/parsers remain unchanged. The new capability is separate, shares existing
pure nested snapshot validation, and never widens an existing operation enum.

The reference also shows failure can happen after Store::open, including snapshot
or output-lease acquisition. Therefore report absence or a non-ok result after
possible dispatch cannot establish that setup changed nothing. Even Busy is not
used as a historical no-write proof. A later successful inspect is a current
observation, not the missing initialize receipt.

## Review, confirmation and uncertainty

A policy-only review captures only current verified connection/boot and a new
opaque host reference. It does not dispatch initialize/inspect, assert a missing
Store, capture a token, freeze configuration or promise specific repairs. The
review explains creation/recovery/owned staging cleanup, current configured roots,
kept existing data under producer rules, and no mode/runtime/provider activation.
It expires120s after issue; a peer operation/session change revokes it.

Confirmation consumes the reference once. The host records possible dispatch
before calling the observer. A fresh valid full initialize-ok report admits
`prepared` (current storage available after this command), never `new-store-created`,
`repair-completed`, `Local-only saved` or `ready to run`. Every post-dispatch
malformed, incomplete, non-ok, nonzero, timeout, cancelled or lost response retains
`unknown`, with a sanitized reason only. Pre-dispatch stale/Busy/invalid/capacity
refusals do not create an unknown original or cancel someone else's owner.

Keep at most8possible-dispatch records per host lifetime, without eviction. A
same-connection unknown blocks another preparation/initialize in this capability;
other existing management actions are not automatically blocked and retained
uncertainty is never erased by them. This conservative boundary is an explicit
accepted review decision, not a claimed producer replay protocol. There is no receipt
lookup or init replay route. Host restart/record expiry is not reconciliation.
No persistence or physical-erasure claim follows from in-memory custody.

A separate **Check current storage** for a retained reference uses only the fixed
inspect selector and same original connection/boot. It may report a current saved
mode kind without changing the original unknown outcome or granting another
initialize. At most32admitted invocation/fence records per original, including early
cancellation tombstones; overflow refuses with no evictions.

## Host/transport boundaries

Use new StorageInitializationHost/protocol/private-parser/controller files rather
than extending LocalModeChoiceHost or SavedMode. Both real factories share the
existing MaintenanceIO. Enumerate the actual18predecessor coordinators from the
admitted fresh source (including owned-data-v3); derive final counts from source.
Acquire ownership before beforeIO or dispatch. Busy has no invalidation/cancel/I/O.
All peers and external observe/cancel/runtime/saved/legacy paths revoke ready
policy/current views, preserving both this and Local-only unknown histories.

Host-issued epochs and renderer generations reject late/wrong-session results.
Each confirm/refresh carries a new renderer invocation UUID used only as a host transport/cancellation fence, never a producer operation or retry ID. Cancel names the exact reference+invocation (null only for an undispatched preview). Early cancel fences that invocation before it can dispatch. A stale timer/cancel/finally can affect only its original token/invocation. A
retained read or stale cancel cannot release another owner. Confirm/check use
remaining13s host/12s child budgets; UI14s includes queued-observation quiescence.
Stop/pagehide/hidden/dispose detaches pre-reference waits locally; with a captured
reference it cancels only the original currently owned invocation. Never schedule
a delayed global cancel that can kill newer work. Post-dispatch outcomes stay
unknown unless the original complete success was validated and delivered current.

Reuse the identity-verified Linux/Windows Python callback, fixed normal nonsecret
configuration prefix and no remote stdin. Child input is host-only identity,
selector and integer remaining budget, at most512bytes. Remote commands are only
fixed initialize or inspect variants. Stdout16KiB incl one LF, discarded stderr8KiB,
private base64 envelope24KiB, public result8KiB. Existing2s channel/8s collection/
12s child/13s host/14s UI ceilings apply; no automatic retry or fallback.

## Admission and privacy

New raw decoder checks fatal UTF8/BOM, duplicate/closed keys, one JSON frame/LF,
original canonical report-version numeric spelling, exact six top-level fields
and operation initialize|inspect matching the host-selected branch. Require
activation_performed=false and the producer status/incomplete/data relationships.
Initialize-ok requires incomplete=false, data.current_snapshot and null
receipt/receipt_status. Validate the complete nested snapshot/token/bindings
privately using the same pure snapshot admission pattern already used by Local-only;
The reuse may construct a typed nested-snapshot validation envelope after the new branch checks its original selector/status/receipt, as the existing Local-only snapshot helper does. Never pass or normalize the incoming Initialize report into the old inspect route.

Only the saved mode kind is reduced publicly. No token, actor/device/epoch/group/
backup IDs, binding/root, private report, path, config value, payload or diagnostic
text reaches renderer/bridge output. Independent public validators enforce closed
state/identity/reference/retained limits on both bridges and the shared UI.

## Product behavior and qualification

Panel labels: **Prepare Buddy storage**, **Review storage setup**, **Prepare
storage**, **Stop setup wait**, **Check current storage**. Policy review explains
normal creation/recovery and prerequisites. Successful copy: **Buddy storage
prepared. Saved mode: Not set/Local only/Isolated backup/Shared group. Running Buddy
and cloud readiness have not been checked.** Unknown: **Storage setup not
confirmed. Check current storage; this does not confirm the earlier setup.**
No implementation/receipt/epoch/store-lease jargon in the primary flow.

Use source-derived report specimens where available and label synthetic mutations
as synthetic. Verify known-mode preservation, complete success vs unknown,
non-ok-after-open, report prefix/nonzero/late/oversized/duplicate/BOM/UTF8 cases;
strict public privacy; one dispatch, repeated confirmation,120s expiry,8record/
32invocation caps, both unknown histories and peer/currentness/cancel controls.
Meaningful actual browser/Electron and retained Linux/Windows package views cover
initial no-Store policy, explicit confirmation, saved mode distinct from setup,
uncertainty/current-only check and responsive keyboard/plain copy. Mock transport
and local SSH peer are not tablet/provider/native qualification. Preserve all old
read-only and Local-only behavior. Independent review confirmed current mode-module equivalence and accepted this consumer contract before implementation. Normal source review, hosted checks and coordinated delivery remain required; no behavior beyond the actual producer contract is inferred.

## Review decisions made explicit

A valid original report captured and validated by the still-current host invocation
can settle its in-memory original as prepared even if the later public delivery is
lost. A later retained read may show that historical host result without a current
mode observation; it is not a new initialization or a producer receipt lookup.
If the host never admitted that valid original result before cancellation/session
invalidation, the terminal original stays unknown. Later inspect cannot settle it.
No report/record survives a host restart as proven execution, and none is a flush,
power-loss durability, running-service or remote-effect settlement guarantee.

## Exact unknown target key

The same-target block is exactly equality of the verified opaque connection_id
string: records.some(r => r.outcome === 'unknown' &&
r.sample.connection_id === request.connection_id). It deliberately ignores
boot_id for this lookup; a reboot cannot settle unknown initialization. That key
is host connection identity, not a newly invented hardware-serial identity.
Refresh/confirm execution still requires both original connection_id AND boot_id
to equal the current verified observation, plus the live reference/invocation/
epoch owner. A foreign/new boot may leave history visible and block another
initialize by connection_id, while refusing a current read on its old boot.
