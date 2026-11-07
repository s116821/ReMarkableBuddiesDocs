# Shared resident package-transition wiring amendment

## Status and exact gap

Review before implementation. Baselines are Manager PR57
`0efb7c64bd4beeb7b27ad007bbdced6f01e00fef` (Stop parent baf0265e) and
Docs PR134 `f8b67d68ff6233c032093034736c06a754b9ad2d`.

The current proposal explicitly excludes package installer wires, enable/disable
and removal from serviceStop; its public protocol accepts only
retained/begin/confirm/refresh/cancel for fixed service Stop. Manager's nine private
recovery/transition files have no public factory action, renderer adapter or shared
package panel. Treating those existing Stop requirements as approval of a package
transaction would be a scope error. This amendment adds that missing finite
boundary in the existing active change; the original Stop contract remains intact.

## Reuse and finite operations

Expose a separate optional `residentPackage` host capability through the existing
browser helper, Electron IPC/preload, common renderer adapter and one shared panel.
There is no new installer, Vellum implementation, download/staging/trust engine,
RPC server on Buddy or generic workflow framework.

| User intent | Existing private behavior to reuse |
| --- | --- |
| Disable startup | transition.review/prepare then disable.execute; disable.observe for original-intent checking |
| Remove Buddy package, preserving data | removal.review/execute/observe; reuse its existing prepare -> disable -> uninstall coordinator and sole-package solver/ownership checks |
| Replace/update or explicitly approved rollback | replacement.preview/execute/observe, composed with existing transition.prepare and disable.execute under one original deadline; no new transaction implementation |

The fixed Python helpers remain authoritative for durable intent creation,
possible-submission handling, signature/solver/lock/ownership checks, stock
recovery and terminal verification. The public host must not send a separate
serviceStop.confirm before calling a preparation helper that already submits its
one fixed stop. Reuse the current fixed commands; never copy them into the UI or
create another stop/transaction engine. Retain each helper's RecoveryPending and
read-only reconciliation semantics. No automatic retry or continuation after an
uncertain phase is added. Explicit continuation after proven reconciliation is
defined below; the coordinator must not re-enter prepare for a retained Stop.

## Closed public and private authority

Add `host/resident-package-protocol.mjs` and matching types. Public requests are
bounded512-byte JSON with exactly one of these shapes:

- `{action:"begin",operation:"disable"|"remove"|"replace",connection_id,boot_id}`.
- `{action:"confirm"|"refresh"|"resume",reference,invocation,connection_id,boot_id}`;
  resume is a read-only continuation review, never submission.
- `{action:"cancel",reference,invocation}`; invocation may be null before dispatch.
- `{action:"retained"}` for host-owned retained references only.

Digests/UUIDs use the existing strict validators. Unknown keys, actions, operation
values, wrong references or context, duplicate/invalid framing and oversized input
refuse before configuration, transport, peer invalidation or mutation. Public
requests never contain a package version, APK/index/profile digest, activation,
private path, candidate directory/nonce, command, signing key or trust policy.

The host derives approved installed version/profile and, for replacement, the
already verified eligible candidate from immutable host qualification/release
policy. The current ZIP download path is not a signed APK admission substitute.
No eligible host candidate means unavailable; do not create/download/stage one in
this change. All production package qualification bindings default empty and both
existing Stop registries stay empty. No settings/device JSON/environment toggle
or renderer value may enroll them. Synthetic test-only host bindings are explicit
constructor/fixture inputs and cannot be reached through product routes.

The host retains private original activation, ownership/solver plan, candidate
pins and helper phase behind a random opaque reference. Ready expires after120s.
Review facts returned to the UI are bounded display data, never authority supplied
back by the renderer. Use the existing8KiB public envelope and observation validator
with one closed `resident_package` object: state, operation, reference, invocation,
reason, current and at most8 retained rows. Public state is one of
none/ready/busy/unavailable/unsupported/expired/invalidated/unknown/continuable/completed;
operation is null only for a retained request with no selected reference. Reference
and invocation are null or the existing digest/UUID shapes; invocation is null at
begin. Reason is null or exactly busy/unsupported/unavailable/invalid-response/
cancelled/expired/session-changed/capacity/lifecycle-unqualified/candidate-unavailable/
recovery-pending/continuation-required. Current is null or exactly
`{phase,outcome,installed_version,candidate_version,data_preserved}`:
phase is review/stop/recovery/disable/package; outcome is ready/pending/prepared/
disabled/removed/replaced; data_preserved is true. Version fields are null or
host-derived package-version display strings accepted by the existing private
require_package_version validator, with the same64-byte public cap. Candidate version is
null except replacement. These display strings are never accepted back as policy.
Each retained row is exactly `{reference,operation,connection_id,boot_id,state,reason}`,
with state unknown/continuable/completed, an operation enum, and the same strict identities/
reason catalog. Completed has null reason; unknown has a nonnull reason;
continuable has continuation-required and a proven prepared/disabled current outcome. No raw
private record or proof is public. Host-private completion states require the
existing helper's phase-specific terminal proof, not merely process exit0 or an
inactive service.

Add only a fixed `resident-package` Python action/adapter with an allowlist of
review/execute/observe/review-continuation/continue selectors and the three fixed
operation enums. The last two are the narrow existing-coordinator extension below. It receives
host-resolved private inputs and delegates to the existing helpers. Keep the
existing4KiB private request,256KiB private response and8KiB public response limits;
unknown selector/input refuses before opening SSH. No arbitrary Python module,
remote command or unit/file path can be selected. The helper remains host-private.

## Shared ownership, delivery and original-operation recovery

Use the current MaintenanceIO instance in both actual factories. Acquire ownership
before peer invalidation or I/O; Busy has no invalidation/cancel side effects.
Quiesce ordinary observation while active. Include serviceStop and every current
maintenance peer in reciprocal host exclusion, App review invalidation and Busy
checks. Review/confirm revalidate the original verified connection, boot, package
ownership, activation/profile, solver/candidate and ready lifetime. USB drift never
switches targets silently. Do not clear unresolved history by opening another panel.

Keep a shared host-private unresolved-submission fence between package preparation
and standalone Stop: possible submission in either lane prevents a second stop or
new package execution for that connection. This is an interlock around the existing
engines, not a second Stop state machine. At most8 retained operations and32
invocation/fence entries per original; capacity refuses without eviction/renewal.
Use the current child/host/HTTP absolute12/13/14-second ceilings. One confirmed
package operation passes a single deadline through all existing fixed phases;
renewing a per-phase timer is forbidden. A recovery that outlives a call becomes
unknown and needs an explicit read-only check of the original intent, not a retry.

Before possible submission, cancellation can invalidate a review. After it,
cancel/timeout/lost child/route/window/process output remains unknown. Cancel
stops local waiting only; it sends no cancel/start/rollback service job or package
command. Only the recorded original host reference/invocation may be checked.
Use the existing protected durable intent files to reconstruct uncertainty after
host process loss; admission of retained records must be finite, host-private,
source-schema validated and tied to approved policy/original connection. Do not
expose an arbitrary intent file picker or invent a second persisted journal.
Retained discovery is restricted to the existing protected host configuration
parent and fixed resident-stop/disable/remove/replace filename forms, with at most
32 candidate entries and8 admitted operations. Excess/unknown/malformed or
unsupported-schema records refuse; do not truncate/evict or rewrite old records.
Delegate validation to the existing private load/observe helpers using the
host-approved original policy. Discovery cannot authorize replay or enroll a
profile; default empty policy performs no record or device admission.
Invalidated late completion/finally cannot release another lane's owner or advance
another operation. Repeated confirm, including after a process restart, must never
redispatch a possibly submitted private phase. Current state and historical
submission/recovery evidence remain distinct; OS inactivity is not completion.

## Explicit continuation after an intermediate phase

This section resolves the reviewed intermediate-phase gap. A successful Stop or
disable proof is progress, not completion of removal/replacement. Refresh is always
read-only. A failed observation is not evidence that a command was never submitted.

**Durable original goal.** Before any possible initial Stop submission, extend the
existing stop-intent writer/loader with a closed version4 record, in the same fixed
file and exclusive/fsync publication path. Its exact fields are version,
connection_id, activation, ownership, removal_plan (null except remove), and goal.
Goal is exactly `{operation,operation_id,installed_version,replacement}`: operation
is the three fixed enums; operation_id is the original host-issued invocation UUID;
installed_version matches approved ownership; replacement is null except replace,
where it is exactly `{candidate,profile_sha256,plan}` using the existing
ApprovedReplacement fields and approved replacement plan/profile. No new journal,
filename, trust source or editable user setting is introduced. Enforce the existing
4096-byte cap for the original and every downstream record before any command;
preflight their bounded serialization including embedded goal/stock/plan fields.
Oversized/invalid goals refuse; no record cap is increased. Existing
load/observe/disable/uninstall/replacement helpers must accept this validated schema
by its goal (not raw version-number substitution), preserving all current checks.
Downstream records embed the exact same stop record, as they already do. Their
connection/boot/activation/goal and replacement pins must agree byte-for-byte in
canonical parsed fields. Legacy1/2/3 remain readable under their existing rules;
no inferred goal, migration or replay authority is granted. In particular a bare
legacy v2 stop cannot distinguish disable from replace after restart and cannot
become a resumable public operation. New public operations use v4, including when
the initial command never returned. Candidate policy must still independently admit
the retained pins; disk records alone never enroll a candidate or production tuple.

**One existing coordinator.** Narrowly extend resident_package_removal.py's finite
coordination boundary with review_continuation and continue_transition for the
three closed goals; keep its existing removal entrypoints compatible. Initial
host-private execute delegates the same fixed phase sequence there. Node/UI never
implements a phase machine or calls helpers directly. Continuation loads the
original goal and all relevant phase records, performs read-only proof, and selects
exactly one next phase; it never calls transition.prepare for a retained Stop.
Reuse transition.observe, disable.observe/observe_disabled, uninstall.observe and
replacement.observe; no new Stop/transaction command or lifecycle proof is added.
A missing record means not-submitted only under the original protected parent,
exclusive writer, surviving original Stop record, proven predecessor and no active
original invocation. Hold MaintenanceIO and the original shared fence; require the
prior child/process invocation positively settled before admission. Use a native
process-lifetime exclusive lock on the existing original intent, acquired by the
initial exclusive writer before command submission and held through coordinator
exit; continuation obtains it nonblocking and retains it through its bounded call.
Keep record bytes immutable and readable by the existing same-process helpers;
validate the corresponding Linux/Windows lock behavior. If this lock or equivalent
exact prior-process proof is unavailable, continuation refuses. A live or
unaccounted-for prior writer, deleted/tampered parent/record, contradictory chain,
unknown path/schema or context drift refuses continuation. No record deletion or
rewrite is used to obtain absence. At confirmation re-read the exact chain and
recheck next-phase absence before the existing exclusive intent publication.
Existing possibly-submitted phase records are never overwritten or resubmitted,
even if a read-only check appears to show the old device state.

| Original goal and retained evidence | Required read-only proof | Sole next mutation after new review/confirm |
| --- | --- | --- |
| Any goal: stop exists; disable and both package records absent | transition.observe proves original archived activation/lease, stock recovery and exact owned package; removal additionally matches its original sole-package plan; replacement preview revalidates original candidate/plan | disable.execute only; never prepare/Stop |
| Remove/replace: disable exists; both package records absent | disable.observe proves original stock identities, disabled Buddy/static helper, absent startup link and unchanged ownership/removal plan; replacement also revalidates its original candidate/plan | uninstall.execute for remove or replacement.execute for replace only |
| Disable: disable exists | disable.observe's full disabled/recovery/ownership proof | none; completed disable |
| Remove: removal exists | uninstall.observe proves original recovery, released owned paths/startup/active lease absent, expected database change, package absence and exact stock/sync identities | none; completed removal |
| Replace: replacement exists | replacement.observe proves original recovery, exact candidate ownership/profile/files/world constraints, disabled/inactive service and exact stock/sync identities | none; completed replacement |
| Any retained phase fails its exact proof, or goal/record chain conflicts | no settled predecessor or whole-goal proof | none; unknown/refusal, Check only; never reinterpret failed proof as absence |

If startup was already disabled and disable.execute returned a complete disabled
proof without creating its optional record, continuation may use that same existing
observe_disabled proof with stock from the original recovery observation; package
submission still requires both package intents absent. It must not invent a disable
record or run disable again to manufacture one. For goal disable that full proof is
terminal. A read-only phase result without the goal-specific final proof remains
continuable, including after a continuation's one allowed phase succeeds.

**Explicit bounded user path and shared fences.** Refresh returns continuable with
continuation-required only after the settled proof above, retaining the original
operation reference/goal and shared fence. It does not return ready or run the next
phase. The panel offers Review remaining step. Its resume request selects only the
retained reference/current invocation/context; host review_continuation rechecks
current proof/policy and issues a fresh opaque invocation/review token, ready for
120s. The UI shows the remaining consequence (including the original replacement/
downgrade), then requires a new confirm. Confirm uses continue_transition and a new
12/13/14s bounded child/host/HTTP invocation for that one proven unsubmitted phase.
This is a separately reviewed mutation, not extension/renewal of the original
in-flight deadline. Each token is single-use; repeated/stale confirms never dispatch.
After possible submission, lost output/cancel/timeout again means unknown and Check
only until exact read-only proof. Another remaining phase requires another explicit
review and confirmation; no automatic chain resumes after uncertainty.

Settled intermediate proof removes only the uncertainty marker for that specific
invocation. The connection's logical reservation remains with the original goal:
standalone Stop, a new package goal and other mutations cannot supersede it. During
read-only Check/review and continuation the existing MaintenanceIO grants only the
original owner's bounded call, never an overlapping call. Cancel of a continuation
review invalidates its token but keeps durable history/reservation. Release the
shared operation fence only on the goal-specific terminal proof above; the retained
completed history remains non-replayable. Unresolved/contradictory records retain
the fence. Do not label all peers Busy after terminal proof merely because immutable
historical files remain; coordinator admission reconciles them read-only and cannot
reuse the same activation for a fresh Stop/goal.

After host restart, bounded protected discovery reconstructs the v4 goal and exact
phase chain behind a new opaque public reference, initially unknown/fenced. It may
become continuable/completed only by the same explicit Check/proofs and a proven
settled prior invocation. Re-deriving a goal from the currently installed version,
renderer choice or a new candidate is forbidden. Lost process-identity evidence
cannot authorize a continuation; retain uncertainty until the prior writer can be
positively excluded. Tablet reboot/context drift is not host restart and refuses.

**Focused scenario mapping.** Verify with existing small synthetic records and real
coordinator/host routes: Stop times out then proves recovered -> Check -> review ->
confirm disable exactly once; disable lost output then proves disabled -> goal
disable completes, remove/replace still needs review of its package step; package
lost output then exact observe proves removed/replaced -> completion without
resubmission; package record exists but final proof fails -> Check only. Repeat at
each boundary with host restart, stale/duplicate confirm, active prior writer,
changed goal/candidate/plan/context, missing/tampered predecessor and already-disabled
without a disable record. Assert the phase command counts, fresh bounded deadlines,
no renewed in-flight deadline, preserved fence until goal completion and reciprocal
Stop exclusion. A failed phase proof never yields completed or submission authority.

## User flow and verification

The shared panel presents the selected operation's reviewed consequence and an
explicit confirm. Disable affects startup; removal preserves owned user data;
replacement reports its host-selected versions and any downgrade impact before
confirmation. Unavailable/unqualified policy stays visibly disabled. Show retained
unknown and an original-operation Check action; a proven intermediate outcome
offers Review remaining step followed by a separate explicit confirm. No automatic switch, retry,
downgrade, trust repair, personal account/cloud setup or firmware update is added.
Do not show paths, tuple digests, solver output or protocol details to ordinary users.

Implementation file scope is the new closed protocol/shared host/private action/
shared panel/controller plus the existing observer, browser/Electron routes,
preload/common host types and App peer boundaries. Extend existing package/Stop
fixtures and actual host-route checks; only the specified narrow existing-coordinator/
intent-schema continuation extension changes helpers. Do not change transaction/Stop
engines or production profile tables to make a test pass. Both real factories and shared UI
must exercise unavailable gates before any I/O, fixture-only approved flow, context/
source/candidate drift, stale/foreign/cancelled reference, queue/peer ownership,
pre/post submission disconnect and timeout, retained intent after process loss,
wrong phase/replay refusal, late results and same-connection cross-lane fencing.
Run the normal source/build/browser/Electron checks appropriate to the final diff.
These use small synthetic transport/record fixtures; the retired v0.65.0 APK bytes
are not needed. Actual lifecycle/platform/package qualification and independently
reviewed production enrollment remain separate; no tablet operation is selected
by this wiring amendment. Keep this change open through coordinated review/delivery.
