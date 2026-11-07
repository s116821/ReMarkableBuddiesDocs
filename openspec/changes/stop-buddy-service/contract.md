# Candidate service-stop consumer boundary

Status: active source contract for independent successor review. Unit-scoped intent
is accepted. package-record-contract.md specifies the proposed delivered
PACKAGE/Profile6/Lease3/rm-sync delta implemented after Manager c013eb2 in the
paired successor, with both original/current companion watchdog values pinned0.
The closed admission table and private DTO are in profile-admission.md,
private-property-keys.json and the separate vendor-policy-keys.json. No production profile is
enabled before its explicit owner qualification gate; there is no new runtime
readiness flag. Source/control results are not native qualification or execution authority.

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
machine-readable private-property-keys.json retains11STATE/20POLICY plus10textual Stop
properties and two typed hook observations; vendor-policy-keys.json separately pins both27-key vendor projections.
All snapshots are closed. Three new nullable private fields (companion,
companion_group,vendor_policy), twelve artifact slots and the nested record rules
are specified in package-record-contract.md and included in the canonical digest.

Private input4KiB, raw show32KiB per service, original existing profile/lease32KiB
each, full child envelope256KiB (including base64), discarded stderr8KiB; public
result8KiB. Proposed serialized service snapshots and vendor policy maps are
individually bounded16KiB, with the complete envelope cap independently enforced.
The nested ServiceBaseline has its source64KiB bound and remains constrained by
the original outer32KiB lease; its snapshot is separately16KiB. Validate
framing/UTF8/BOM/duplicates/selector/identity/closed shape
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

SSH exit-status availability and temporarily empty receive buffers do not prove
complete output. The collector drains stdout and stderr fairly with bounded
nonblocking reads until BOTH streams return actual EOF and exit status is
available, under the unchanged remaining deadline and per-stream caps. Missing
EOF or late excess bytes refuses; a possibly submitted Stop remains unknown.
Every exit closes the owned channel and clears mutable drain buffers. This is
completion evidence, not proof of remote job termination or native restoration.

Ready lasts120s; at most32invocation/fence entries per original, including early
cancel tombstones. Cancel targets only the captured original local wait. Stale
cancel/timer/finally cannot revoke another owner; no delayed global cancel. Remote
job cancellation/rollback/restart is not performed. Retained reads do no I/O or
invalidation. Host restart loses custody and never proves no stop occurred.

## Metadata producer compatibility

Use the common GNU/BusyBox `stat -c` interface for the existing fixed-path
metadata reads. Pass actual newline characters between the numeric, mtime and
ctime fields, with no final newline in the format argument: `-c` supplies that
one final newline. The result remains exactly three lines, including nine
fractional timestamp digits and an explicit numeric UTC offset. Filesystem type
uses `stat -f -c %t`, with the existing exact cgroup2 magic check. Do not fall
back to epoch seconds, pad missing precision, repair framing or choose another
command after refusal.

For an explicitly optional final component under already-bracketed parents,
absence requires exit1, empty stdout and exactly one of the qualified C-locale
GNU `cannot statx` or BusyBox `can't stat` messages for that exact operand and
`No such file or directory`. Permission errors, other exit codes, partial output
and extra diagnostics refuse. Keep existing no-follow, parent identity, mode,
ownership, size, EOF, shared deadline and output bounds. Source/local utility
tests do not establish target qualification or enable a production Stop profile.

Each existing ordered parent-directory chain may use one fixed shell command.
Keep an immediate no-symlink test before each parent's unchanged `stat -c`
command, joined with `&&`; any failed test/stat aborts the chain. Require exactly
one three-line metadata record per requested parent, in order, and the final LF.
Any nonzero status, stderr, partial/extra record or invalid metadata refuses the
whole chain. Retain the 4096-byte stdout cap and original absolute deadline.

The host validates all returned parent identities, ownership, directory types
and write permissions before a caller can stat, read or hash the leaf. This
permits collecting deeper ancestor metadata before rejecting an earlier unsafe
owner/type/mode; it does not permit leaf access after such rejection. Preserve
each independent before/after chain and comparison without caching or reusing a
prior sample. Neither batching nor these sampled checks provides atomic ancestry
or protection against hostile root replacement.

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

## Typed hook evidence

Each private service snapshot has exactly state, policy, stop_extra and hooks.
The first three contain the strict textual catalog; ExecStop and ExecStopPost are
removed from stop_extra and never inferred from missing text. hooks has exactly
ExecStop and ExecStopPost. Each observation has exactly property, observation,
type_verified and reason, with property equal to its map key. Only
observed-empty/true/typed-empty for both hooks satisfies the candidate predicate
for EVERY required service slot. Valid full nonempty arrays are
observed-nonempty/true/typed-nonempty and refuse; unknown/false with a closed decoder
reason also refuses. Old text-only, mixed, missing and extra forms refuse.

Use fixed installed busctl Properties.Get calls, cleared normal system-bus
environment, replies, no destination auto-start, no interactive authorization and
2s method timeout. Possible OS socket activation and ephemeral clients are
explicitly permitted effects. There is no installed-source-attestation or zero
infrastructure-effects prerequisite. Only the four existing fixed units and their
constant encoded loaded objects are allowed; no LoadUnit or alternate route.

One typed group belongs to one original sampler bracket. It verifies current
client identity, bus, systemd unique owner/reported PID1 before and after, and
loaded unit objects before their first and after their last hook read. Every
service observation reads both hooks afresh, including repeated captures. Reset
the group on all exits. Typed-query uncertainty terminates the complete candidate
loop, not a retry against another profile. Keep the remaining original deadline,
stream/frame limits and repeated sample checks. Additional exec ceilings are18
ordinary/40resident and at most58 for a two-candidate review; a count is no timing
qualification. Inspect adds none. No raw hook content, private context identifiers
or response hashes enter retained facts. The canonical Python/JS digest includes
reduced hooks, never raw replies. Matched samples are time-point evidence, not
atomic invocation/configuration custody.

Decoder bounds remain32768stdout/8192stderr,32commands,256argv entries per command,
4096UTF8 bytes per string and exact integer ranges. Validate every array member
before classification. Both production registries remain empty. This contract
does not qualify actual Stop, native effects or independent recovery.
