# Consumer design before implementation

## Protected entry and shared ownership
Use optional ManagerHost.modelSettings(request), authenticated fixed POST
/manager-model-settings and exact-arity authorized main-frame IPC
manager:modelSettings. A separate strict private/public parser and coordinator
consume the immutable model producer; do not weaken or parametrize basic shapes.
The same existing MaintenanceIO spans basic/model Begin, whole Save, remote status
and forget prepare/confirm/receipt. Busy acquisition performs no hook/cancel/I/O.
Cross-invalidate ready grants before owned remote I/O while preserving all unknown
originals. Keep original observer receiver; conditional release and lane/reference/
token cancellation prevent old callbacks from killing another coordinator's work.

## Origin-only read, deliberate replacements
Begin pauses polling once before its inspect and grants120s monotonic authority.
Model and endpoint each offer Keep unchanged, Replace, Remove override. Current
origin/presence is visible; saved strings are never fetched/populated. A replacement
is explicit exact user input, not a URL/href/provider selector. Remove clears even
present null; unchanged fields stay absent. No attempt to compare replacement text
to undisclosed old strings: producer no-change is valid and preserves original bytes.
One Save prepares and at most once applies without pausing again or confirming twice.
Saved-file readback says restart required/runtime unverified; no restart/provider UI.

## Private input lifecycle
Transient renderer drafts are separate from safe published state/diagnostics, with
no app persistence, telemetry, copy-to-report or auto-retry cache. Clear on submission
before await, local refresh/navigation/disconnect/other maintenance, Stop, replacement
of editor,120s local draft expiry and destroy. A failed/busy/no-change Save never
restores text. Preserve raw pasted scalar text in the controller; the textarea's
normalized display is not the submitted source of truth. contract.md specifies
CRLF index mapping and exact edit/refusal behavior. This adds no clipboard read API.

The host validates and snapshots the original patch only for the bounded Save,
binds its canonical digest to the prepare response, and supplies it once in apply.
After prepare refusal/no-change or any terminal/cancelled/expired Save, drop all raw
patch/serialized-apply/base64 references and clear mutable owned buffers. After a
possible apply retain only original hash-only prepare/intent/status packet and
safe before/after presence. Status never needs raw changes. JavaScript strings,
framework/IPC copies and OS buffers are not promised cryptographic zeroization.

## Remaining-time and stale-response rules
Reuse existing2/8/12/13/14s bounds. Save has one13s budget, original ready expiry is
rechecked after prepare and before possible apply, private budget_ms carries only
remaining time to supervisor/Python, and post-await/parsing/final settlement checks
cannot accept a late verified result before a delayed timer callback. Before apply
expiry is not-dispatched; after possible dispatch it is unknown with hash-only
original evidence, never a stored retry patch. Every controller stop mutation checks
captured generation/reference/original; ready final projections check host epoch.

## Risks and alternatives
Reusing the entire basic coordinator would incorrectly assume current string values
and unresolved status fields exist. Reuse custody/deadline patterns through explicit
model contracts; producer unresolved status has null data/current. Never return raw
patch in prepare/retained for convenience or introduce a second I/O lane. Increasing
all bridge caps is unnecessary: only the new model request path needs16384bytes to
accommodate worst-case escaped256/2048-byte replacements; existing request caps stay.

## Verification and completion
Reuse all32original reports/60hashes including their actual after-verified status;
label synthetic apply loss/faults separately. Both actual HTTP/main-frame IPC hosts
and both ordinary OS source/retained jobs cover exact opaque paste, lifecycle clearing,
private record absence, cross-lane ownership, late timers/stop, capacity and old-wire
compatibility. Inspect390/1280 source captures with synthetic text cleared. Own
canonical sync/archive occurs only after implementation/current checks/review.
