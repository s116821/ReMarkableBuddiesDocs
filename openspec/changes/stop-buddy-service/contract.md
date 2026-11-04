# Candidate service-stop consumer boundary

Status: concrete source-backed proposal for independent review. Unit-scoped intent
is accepted. The closed supported-shape/admission table and exact private DTO are
in profile-admission.md and private-property-keys.json. No production profile is
enabled before its explicit owner qualification gate; there is no new runtime
readiness flag. This is not implemented behavior or tablet execution authority.

## Public API and matrix

Exactly one argument to `serviceStop`:

- `{action:"begin",connection_id,boot_id}`
- `{action:"confirm"|"refresh",connection_id,boot_id,reference,invocation}`
- `{action:"cancel",reference,invocation}` (null only for an undispatched review)
- `{action:"retained"}`

Identity/reference are canonical64hex; boot/invocation canonical nonnil UUID.
Public requests at most512bytes. No unit/PID/path/command/environment/configuration,
raw proof, expected runtime version or native lease is caller-controlled.

Candidate result extends the existing validated observation envelope with exactly
`service_stop:{state,reference,invocation,current,reason,retained}`. Public cap8KiB.
States: none|ready|invalidated|expired|busy|unavailable|unsupported|capacity|
request-accepted|unknown. Closed reasons: null|busy|unsupported|unavailable|
invalid-response|cancelled|expired|session-changed|capacity|lifecycle-unqualified.
Current is null or exactly `{state:"inactive"|"active"|"transitioning"|"failed"}`.
Unknown OS spellings refuse; missing unit is unsupported, never inactive success.

Rows are exactly `{reference,connection_id,boot_id,outcome,reason}` with outcome
request-accepted|unknown, unique references, at most8, no eviction. Row reasons
remain original historical diagnostics, separate from a later current-read reason.

| Action | Allowed historical selection | Current | Selected row identity |
| --- | --- | --- | --- |
| Begin | Existing unknown only; otherwise ready/refusal | Null | Connection-only; older boot allowed |
| Confirm | Original request-accepted/unknown | Only with request-accepted | Original connection AND boot |
| Refresh | Either historical outcome | Current read only | Original connection AND boot |
| Cancel | Either original historical echo | Null | No caller target identity |
| Retained | State none, null selected reference/invocation | Null | Closed history only |

Ready is Begin-only, with no current service-readiness claim. None is Retained-only.
Confirm/Refresh/Cancel echo the exact bounded reference/invocation, including on a
refusal; an echo grants no original/current authority. Current must match the
request's observed connection/boot. An unknown/current reply is Refresh-only.
Malformed or contradictory replies refuse completely; a possibly submitted local
attempt stays unknown. No-current history does not waive selected identity checks.

## Private operation, profiles and DTO

Only fixed service observation and one fixed nonblocking request may be sent:
`/bin/systemctl --system --no-pager --no-ask-password --no-block --job-mode=fail
stop -- reader-buddy.service`. It is unit-scoped, not original-PID CAS. Observed
connection/boot/profile drift refuses; no custom lock, job cancellation, recovery,
start/restart, force-kill fallback or service/unit/package editing follows.

profile-admission.md defines exact ordinary-manual/resident-installed predicates,
fixed paths/source policies, mode evidence explicitly unavailable from this
interface, the existing ownership checks and their non-transferable limits,
all unsupported cases, and qualification required before enabling each profile.
It also specifies every private request/result member and nested field. The
machine-readable private-property-keys.json contains exactly11STATE/20POLICY
source properties plus12Stop-specific ones; all snapshots are closed.

Private input4KiB, raw show32KiB per service, original existing profile/lease32KiB
each, full child envelope256KiB (including base64), discarded stderr8KiB; public
result8KiB. These revised private bounds accommodate the actual existing source
record limits. Validate framing/UTF8/BOM/duplicates/selector/identity/closed shape
before reducing. No environment contents, arbitrary argv or native grant reaches
renderer/logs. Do not persist or log private evidence. Drop references on
completion/invalidation and clear owned mutable byte buffers where available;
immutable strings and runtime copies have no secure-erasure guarantee.

## Deadlines, effects and custody

Reuse at most2s channel/8s collection/12s child/13s host/14s UI software ceilings,
with remaining budgets including observation quiescence. These limit local waits;
they do not shorten the unit's stop policy or establish that a remote systemd job
has ended. A delayed/lost submission acknowledgment becomes unknown; the accepted job may
continue beyond the local wait, including its admitted escalation behavior.
An accepted acknowledgment is not a bounded shutdown completion promise. No host timeout triggers a replacement stop or
force kill. Longer native recovery is independent; the Manager does not wait for or claim its
completion. Profile qualification must preserve that truthful distinction.

Mark possible submission before the stop transport call. A live admitted zero-exit acknowledgment of the
original fixed nonblocking command may be historical request-accepted, without a claim
of native restoration, good flush, causal authorship of later inactive state or a
quiescence grant. Current readback is separate. All lost/nonzero/malformed/late/
incomplete/cancelled post-submission outcomes remain unknown. No automatic retry.
A later inactive read cannot settle it or grant another stop for the connection.

Ready lasts120s; at most32invocation/fence entries per original, including early
cancel tombstones. Cancel targets only the captured original local wait. Stale
cancel/timer/finally cannot revoke another owner; no delayed global cancel. Remote
job cancellation/rollback/restart is not performed. Retained reads do no I/O or
invalidation. Host restart loses custody and never proves no stop occurred.

## Required qualification

acceptance.md and acceptance-cases.json define concrete fixture variations and
ordinary/resident enablement evidence; the vectors are not executed product tests.

Use synthetic closed-protocol and actual local SSH/process/systemctl fixtures for
unit drift, all action/current/identity states, unsupported lifecycle profiles,
unknown outcomes, no stdin, bounded output/deadline, queued Stop/expiry and19peer
ownership in both actual factories. Derive final peer count from admitted source.
Qualify browser/Electron, Linux/Windows and retained packages without confusing
fixtures with a real service/native stop. Supported ordinary/native lifecycle and
package/unit compatibility must have their own current-source and actual-target
owner evidence. This assessment does not authorize those executions.
