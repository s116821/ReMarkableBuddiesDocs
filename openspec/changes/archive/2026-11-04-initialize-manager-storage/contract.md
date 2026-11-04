# Proposed closed consumer contract (not implemented)

Public method `storageInitialization(request)`, exactly1argument. Browser
POST /manager-storage-initialization uses existing origin/cookie/content-type/
body guards; Electron manager:storageInitialization uses authorized main frame
and exact arity. Renderer input is at most512UTF8 bytes:

- `{action:"begin",connection_id,boot_id}`
- `{action:"confirm",connection_id,boot_id,reference,invocation}`
- `{action:"refresh",connection_id,boot_id,reference,invocation}`
- `{action:"cancel",reference,invocation}`
- `{action:"retained"}`

connection_id/reference: exactly64lowercase hexadecimal; boot_id: canonical
nonnil UUID. invocation is a new canonical nonnil UUID for each confirm/refresh,
and the exact same UUID in its cancel (null only to invalidate an undispatched
preview). It is a host cancellation fence, never a producer operation/retry ID.
No arbitrary strings/paths/selector/mode/token/version/producer-operation ID.
No reference is derived from producer authority or configuration.

Result is exactly `{contract_version:1,status,observation,storage_initialization}`.
Use existing ObservationResult validation; a current mode observation requires
observed status and the original current connection/boot. No current observation
means unconfigured/null observation. storage_initialization is exactly
`{state,reference,invocation,current,reason,retained}`. state is none|ready|invalidated|expired|busy|
unavailable|unsupported|capacity|prepared|unknown. current is null or exactly
`{kind:"unconfigured"|"local-only"|"isolated-backup"|"shared-group"}`.

ready requires a host-issued live reference, matching observed context, null
current and no same-target unknown. It means policy review only. prepared/unknown
require a retained original reference; current can be nonnull only from a fully
validated original success or separate current inspect in the same session.
retained is at most8unique rows exactly
`{reference,connection_id,boot_id,outcome:"prepared"|"unknown",reason}`.
reason is null or one of busy|unsupported|unavailable|invalid-response|cancelled|
expired|session-changed|capacity. Ready/none and a newly successful prepared result use null; a failed current
refresh may carry a closed reason while retaining the original prepared outcome.
Unknown retains a
closed reason without turning it into a no-write claim. No arbitrary error text. A refresh updates
current only and never changes the original outcome; absent/failed refresh cannot
become a prepared result. Retained action performs no I/O/invalidation and returns
none/null reference/current/unconfigured observation. Public serialized cap8KiB.

ready/none/retained results have null invocation; confirm/refresh/cancel replies
match the request invocation. Each of at most32private per-original ledger entries
is keyed by invocation. A cancellation arriving first reserves a nonexecuting
fence so its later queued request cannot dispatch. A stale cancellation can
neither affect another invocation of that same reference nor another owner.

Policy expiry120s and invocation limits are host-private monotonic state, not
renderer-supplied timestamps. Record check/cancel limits never renew or evict
originals. Same-target unknown retains the reference and blocks another begin.
No automatic initialize from a check, source capability probe or observation.

Private child input exactly `{connection_id,boot_id,selector,budget_ms}`, at most
512bytes; selector initialize|inspect is host-chosen, budget integer1..12000.
Private output reuses bounded ObservationResult plus exactly
`storage_initialization_raw:{status:"reported"|"unsupported"|"unavailable",stdout_base64}`.
Nonreported output has null base64. Reported output still needs matching identity
and independent raw admission. Cap24KiB, raw16KiB including LF. Full raw init-v1:
exact report_version/operation/status/incomplete/activation_performed/data, with
producer-owned nested current_snapshot/receipt/receipt_status. The source report
has SIX top-level fields; nested snapshot has device/epoch/mode/token. Existing
source error shape relationships remain unchanged; no new producer DTO is minted.

Important phase rule: unsupported/unavailable/busy after possible initialize
submission describes a reason, not a verified no-write historical outcome. Public
original remains unknown. All actual report fields are validated before any
reduced current.kind is admitted. Existing inspectSavedMode/Local-only/report3
wires and fixed commands remain unchanged.

## State/identity interpretation

Public admission binds results to the requested action: ready is permitted only
for begin; begin cannot return prepared or any current kind. A nonnull current
kind is permitted only for confirm/refresh. A begin/unknown response must match
the reference and connection of an unknown retained row, while deliberately
allowing its older boot identity. Genuine confirm replay/cancel responses can
return retained prepared/unknown with null current; history is not a fresh read.

A prepared/unknown reply to confirm or refresh must match the request's original
connection AND boot even when current is null. Confirm may carry current only
with prepared; unknown plus current is refresh-only. Cancel's no-current
historical echo has no target request identity and grants no current authority.
A refused unavailable reply may retain the host's closed history list, including
the differently bound reference that caused refusal; it cannot claim a historical
outcome or current observation for that request.

| Action | Prepared/unknown outcome | Current kind | Matching original identity |
| --- | --- | --- | --- |
| Begin | Unknown only | Never | Same connection; older boot allowed |
| Confirm | Either | Prepared only | Original connection and boot |
| Refresh | Either | Either outcome | Original connection and boot |
| Cancel | Either historical echo | Never | No caller target identity |
| Retained | State is none; rows remain history | Never | No selected original |

- begin may return ready with a new reference/null invocation, or the existing
  same-target unknown reference/null invocation. Ready uses the current verified
  observation as target context, not a new storage observation. Pre-dispatch
  Busy/unavailable/capacity has null current and does not create a retained row.
- confirm/refresh/cancel replies echo only their bounded supplied reference and
  invocation, even on a not-found/refused request; that echo grants no authority.
  The null invocation cancel may invalidate only an undispatched ready preview.
- prepared/unknown require a matching retained row. A possible-dispatch row is provisional while its exact invocation still owns
  the active context; only a matching fully validated original initialize-ok
  result can settle it as prepared. The terminal original outcome freezes after
  completion or invalidation/unknown settlement. Its reason stays the original
  reason (prepared row reason null), separate from a later failed refresh reason.
- a current.kind value always has matching current observed context. A stopped,
  expired or wrong-session result cannot carry it. A later current value never
  changes the original retained outcome. No mode/device identity is inferred from
  a bare policy-ready response.
- none/retained is null reference/invocation/current with unconfigured observation;
  retained rows remain bounded safe history. Any ready reference is revoked on
  expiry/peer/session/lifecycle invalidation without releasing another owner.
