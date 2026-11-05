# Resident admission progress: next source increment

Status: proposed implementation contract. Review and implement after the current
installed-source integration is frozen and validated; do not edit its moving
source or credit its tests/artifacts to this increment. This work removes a
source-visible admission bottleneck. It does not complete REM-25 or authorize
another diagnostic-only native run, approved package, native capture or output.

## Evidence and attribution

Spent native05301e used frozen Buddy87b63ad through CI merge951b69df,
tree3b3a9a56. Its bound diagnostics show setup-progress entered at0ms and returned
at46851ms; actor-ended wait entered at46983ms. There is no capture, reconnect,
capture-api or image-publication entry. The actor reported a service-observation
deadline failure; independent recovery and separately verified cleanup succeeded.
These observations establish slow pre-capture admission, not Qt capture latency,
request dispatch or the duration of any individual systemctl/busctl command.

The following counts are source-derived lower bounds, not measured subprocess
counts. With a present companion owner, one broker sample performs six busctl
queries. Each query invokes its progress callback at least five times: owner_with
before/after, run_with_progress before spawn, its first pipe poll and completion.
Companion::observe adds two checks: at least32 caller callbacks per sample.
VisualTransport::progress invokes with_connection with two broker samples plus
three checked/action callbacks: at least67 inactive_services invocations.
Each inactive_services invokes four systemctl observations plus vendor.stopped,
whose policy and stopped bracket add four more: at least536 systemctl and12
busctl processes for one nominal visual progress operation. Additional pipe polls
increase the count. Installed Pending::session_current similarly expands to16
systemctl observations per authority callback, before nested broker polling.
The46.851-second observation is consistent with this amplification; exact causal
cost attribution requires no invented per-command measurements.

## Two explicit responsibilities

Introduce a narrow read-only admission interface with two methods sharing the
same original Instant. A trait/object can own the necessary mutable input/health
borrows; do not construct recursively calling closures.

- pulse(deadline): original deadline; sticky input cancellation/integrity; actual
  ServiceHealth; lease/root/candidate/unit-file pins; known child PID/start/exe
  and process/group/context identities; stopped original-group absence. It must
  perform no systemctl, busctl, nested broker observation or service transition.
- boundary(deadline): fresh full PID1 policy/state/incarnation/job observations,
  matching pinned profiles and original baselines, with unchanged before/after
  group/pin checks. It is not a cached pulse result or a reusable authority token.

Keep all existing comparisons and error classifications. A direct group, child,
lease, file, input or health change refuses during polling; a loaded service or
broker change refuses at the next full boundary before dispatch/acknowledgment or
delivery. No reply, marker, historical image or prior successful sample skips
that boundary. No TTL, elapsed-time cache or periodically refreshed permission is
introduced. Synchronous work still consumes the original bound; check after it
returns, and never claim forced preemption of filesystem work.

Use a CLOSED read-only request enum and internal dispatcher containing only
Observe, CaptureSource(expected facts) and development CaptureVisual. The new
seam must not expose a generic action closure or mutable ResidentConnection:
otherwise a caller could dispatch Insert/Select under cheaper guards. Keep
Insert/Select, Reconcile and their existing admission paths unchanged. Retired
lost-request state and unresolved mutation-journal gating remain intact; historical
capture and reconnection cannot settle a mutation reservation.
Stock stop/start, activation publication, recovery commands and cleanup retain
full fresh admission immediately before their existing effects and their original
ordering/deadlines. This performance change cannot become effect authority.

## Runtime, Session and observer call sites

Add the closed read-only request dispatcher and read-only reconnect admission
seam alongside existing APIs. ResidentRuntime::sample_companion and
Companion::observe use pulse for all
service::companion::owner_with queries and run_with_progress pipe polls. Full
caller service admission brackets the complete broker sample once, not each
internal poll. Preserve GetId/GetNameOwner/unique-name PID/GetNameOwner/GetId
correlation, broker-loss refusal, known companion ownership and sticky integrity.

For an actual read-only request, perform a full boundary and fresh broker sample,
then a full boundary immediately before the SDK API call. Native transport progress
uses pulse plus the existing known-child/artifact/group checks. After the reply,
perform a fresh broker sample and full boundary before returning it. A final
current boundary also gates acknowledged image/provider delivery where that is a
distinct operation. Define and test the exact fixed boundary count; no full
service/broker sampling is permitted from internal pipe-poll callbacks.
Existing service-child3s, busctl2s, setup120s, capture10s, installed acquisition90s,
activation60s and reconnect30s caps remain intersected with their original caller
bounds. No retry, readiness sleep, deadline renewal or new runtime follows failure.

Split Pending::current/session_current into cheap pin/lease/known-process/group
checks and full service validators. Session read-only requests/reconnect use the
new interface; ServiceHealth and RequestInput remain owned by the same caller.
SourceOwner reconnect must select the new read-only reconnect seam; existing
general/effectful/Reconcile APIs are unchanged. Add a narrow SourceSession delivery
admission method, implemented by the real Session, that executes the fresh full
service/broker boundary after actual stored-image readback, recipe validation,
encoding and model-payload construction, immediately before the first provider
admission and BEFORE SourceOwner clears the original90-second deadline. Health
and input alone do not establish this final full boundary.

SourceOwner::progress must also invoke the real Session cheap pulse whenever a
Session is retained, including provider progress and the actual idle Reader-poll
callback. Validate owned Reader/companion child liveness and PID/start/exe/group,
lease and pinned identities there; health/input-only polling must not keep a
watchdog healthy after native ownership is lost. Loss poisons the actual health
owner, refuses subsequent provider delivery/request, and exits to existing
independent recovery. Before activation there is no retained child to validate.
Idle pulses create no request or new budget; active acquisition/provider checks
retain their existing original bounds. No PID1/broker subprocess enters this cheap
path. Session finish retains the child and unresolved effect state while retiring
only the connection. Existing effectful Session dispatch stays on its existing
guard. In examples/resident_bootstrap_observer.rs, VisualTransport::progress becomes a
cheap read-only runtime pulse, rather than opening with_connection and sampling
the broker twice merely to wait for a mailbox file. Actual visual/source APIs
still use the full request boundaries.

## Coherent bounded PID1 batches

Add service::observe_many for a fixed small approved unit set and the union of
existing required property fields. One subprocess reads the before set; perform
the existing pin/caller/terminal-group checks; a second reads the after set.
Validate exact requested unit membership, one complete block per unit, unique
fields, no unexpected/duplicate units, all required values and bounded output.
Retain the existing output limit; refuse a set that cannot fit rather than raising
limits. Reuse Snapshot/PolicySnapshot and existing incarnation, cleared-state,
watchdog and stopped-bracket validators; do not reimplement weaker string tests.

Factor vendor policy/stopped validation so it consumes these fresh batch snapshots
and the original pinned files/group evidence instead of launching its own duplicate
queries. Inactive_services can then use two batches instead of eight commands;
installed session_current can use two coherent batches instead of sixteen.
Do not treat batch ordering as an atomic PID1 snapshot: before/after comparisons
and the interleaved identity/group checks remain necessary. Installation/package
approval, vendor pairing and independent recovery ownership remain unchanged.

## Actor and mailbox waiting

Split bootstrap Context::current into cheap pulse and full service admission while
preserving the public full check for effect/recovery callers. Actor setup loops
poll input, child/binding/root/pins and stopped original groups cheaply. Mailbox
wait first pulses and attempts to receive/pin the requested marker. An absent
marker only pulses and paces; it does not query PID1 or the broker. A present marker
must pass exact binding/pin checks plus one full boundary before it is accepted,
acknowledged or used to publish readiness/admission. Revalidate after any slow
retention before onward action. Both actor and observer keep their original input
end/reacquire boundary and single-consumption markers. No ready marker or image
is manufactured to avoid this wait, and no previously spent candidate is reused.

## Required validation before another native artifact

Use the real production admission/command/mailbox seams with owned peers and
instrumented command invocations, not a helper-only or elapsed-time benchmark.

- For one read-only connection request, changing broker pipe polls from1 to1000
  adds pulse checks and zero full PID1/broker samples. Freeze an explicit ceiling:
  at most four full two-batch brackets and two six-query broker observations
  (at most8 PID1 and12 busctl subprocesses), excluding separately selected
  reconnect/activation/delivery operations with their own fixed counts.
- With1000 absent mailbox polls, assert zero PID1/broker commands; a newly received
  marker requires a fresh full bracket before acknowledgment or SDK action.
- Inject cancellation, original expiry, health loss, changed lease/file/root,
  known-child PID/start/group and competing original-group changes at internal
  polls and before/after each boundary. Refuse further query, dispatch, marker,
  provider delivery or replay as appropriate; reap only owned command children.
- Change broker ID/unique owner/PID across correlation queries and request/reply;
  change service policy/job/incarnation/group across the batch bracket or while a
  marker is pending. Stale successful samples never authorize subsequent work.
- Refuse missing, duplicated, unknown-unit, truncated, malformed or oversized batch
  output. Prove old single-unit Snapshot meanings and cleared/watchdog rules stay
  intact, including the no-job and original stopped-group conditions.
- Exercise the CLOSED dispatcher: no Insert/Select/Reconcile variant or generic
  mutable-connection/action escape exists; original effectful and lost/unresolved
  journal guards remain unchanged. Verify SourceOwner uses read-only reconnect.
- Delay actual stored readback/encoding/model-payload assembly, then change a full
  service/broker identity or exhaust the original acquisition budget. Real
  SourceSession delivery admission must refuse the first provider call before
  discharging the original deadline; health/input-only success is insufficient.
- Kill/replace the owned Reader or companion during provider work and during the
  actual idle Reader wait. The real cheap Session pulse detects loss, poisons the
  health owner and prevents later provider delivery/new request/healthy watchdog
  continuation, without PID1/broker polling, restart or replay.
- Exercise actual selected Workflow/Session and visual actor/observer flows with
  delayed service/broker responses: fixed command counts, no deadline expansion,
  input cancellation, exact source correlation, no hidden dismissal or fallback,
  unchanged effectful guards/unresolved journal bytes and stock-first recovery.

Coordinate runtime/companion, service/baseline/vendor, bootstrap/setup, observer
example and the narrow Session read-only adapter with the current source owner
before editing. Run exact-source tests/lint and independent review first. A later
native artifact/candidate requires its own identity, fixture, preparation and
separate admission. Full automatic creation/reuse, Reader/Writer/blank-start,
source preservation and qualified rendering remain mandatory unfinished work.

Source basis: current local native-05301e-outcome-r1.json and saved terminal
receipts; frozen Buddy87b63ad runtime/companion, PID1/vendor, activation and
bootstrap/setup source; accepted installed source-handoff precode. The pulse,
batch and boundary APIs above are proposed design, not current implementation or
hardware qualification. No saved memory or cross-project context was used.
