# Caller progress through the resident consumer

Pin the SDK's reviewed progress-aware transport. Buddy's ResidentConnection
shall offer progress-aware handshake, observation, insertion, selection and
reconciliation methods, retaining the existing no-op conveniences. The caller
callback is synchronous, bounded, and read-only with respect to native effects.
It must service actual input cancellation and main-thread health; a historical
ReaderFacts reply cannot substitute for those checks.

The Store journal still reserves the original request before dispatch. If SDK
progress fails before admission, record known-not-dispatched only from the SDK's
explicit NoPendingMutation result. Failure after admission preserves the original
reservation and operation/digest. Reply-retention failure remains sticky. A
progress callback never marks uncertain work safe to retry or clears old history.

ResidentRuntime's installed admission callback shall continue through socket
appearance and handshake, using the same original startup deadline. Callback
failure after spawn stops/reaps only the owned child and retains startup evidence.
Preparation and cleanup remain bounded independently; callback failure must not
disable cleanup. Installed Session keeps its existing protected installation,
lease, stock-exclusion and fatal-health ownership throughout these checks.

Verify real Store/socket cancellation before dispatch and during a pending effect,
including restart inspection and blocked replay; verify owned child cancellation
before socket readiness and during handshake plus normal launch. First-gesture
source reacquisition, capture/output admission, actual installed services and
native qualification remain separate required work. Do not connect a stale legacy
process/page guard across activation or advertise a native capability from this
transport increment.

The endpoint's 30-second idle timeout retires its connection, not the resident
process. Product integration must distinguish ordinary request cancellation,
timeout and EOF from health or installed/runtime identity failure. Those ordinary
events must retain the resident child. The installed `Session::request` route
replaces the former unscoped connection accessor with typed request outcomes.
Explicit reconnect uses the same verified runtime with fresh
connection/handshake/server nonces, retained uncertain effects and no replay.

The consumer must retain typed SDK failure causes and original lost-request
identity, including callback errors, rather than parse diagnostic strings.
Explicit runtime reconnection retires only the prior socket, validates the
original child incarnation and copied files plus consumed admission, and uses
the existing Store. It must not rerun activation, rewrite the original process
identity, or consume another admission. Failed reconnection leaves that child
owned by the session and retains all uncertainty for later reconciliation or
shutdown. An unresolved effect from a retired connection makes subsequent
connections read-only for effects, including requests from other conversations;
observation and explicit original-target reconciliation remain available.

Exercise same-process repeated handshakes with fresh identities, idle EOF,
caller refusal during reconnect, tampered admission/artifact refusal before new
handshake, and reply-retention loss across reconnect and shutdown. The installed
Session composes typed health/input classification and lease/group checks in
its request route. Source implementation and validation are tracked separately in
[the installed request result](resident-installed-request-result.md); the
first-gesture Reader/Writer caller and native acceptance remain open.

## Installed request route

Replace the unscoped installed connection accessor with explicit request and
reconnect operations. Requests carry fresh operation IDs and use the same
ResidentConnection journal/dispatch methods. Caller input progress returns a
typed quiet/canceled observation; an input-observer error is an integrity failure,
not ordinary cancellation. Health ownership, installed pins, fixed lease,
Buddy/helper invocation, stock exclusion and resident group membership are
revalidated during progress. Runtime-owned child and consumed admission checks
must continue through the transport wait as well.

Distinguish cancellation, original request deadline expiry, ordinary socket
retirement, unresolved prior work and request refusal from integrity failure.
Request retirement closes only the connection and preserves the original lost
operation/digest. Actual health, input-observer or installed/runtime integrity
failure poisons the service health owner; whole-session drop remains fatal.
Unknown or malformed peer responses are integrity failures. Explicit reconnect
uses the same admission checks and never automatically retries an effect.

Deadline errors must be typed at their origin, including bounded PID1 reads;
do not infer timeout from error text or an expired clock after an unrelated
failure. A service-command cleanup that cannot reap its owned child is fatal
even if the initiating request deadline expired. Internal service-read timeout
is distinct from the caller's request deadline. Startup failure retains the
existing fatal activation/cleanup rules.

Exercise the common installed-request dispatcher against owned sockets/children
and injected admission outcomes: cancellation/deadline/EOF retains process and
healthy session, input/health/identity/protocol failure marks fatal, uncertain
effects survive retirement/reconnect and fresh requests, and no action happens
after refused admission. Actual installed service and native-device acceptance
remain separate; this does not fabricate current-page/capture/write authority.

Sample input again after potentially slow authority checks before dispatch.
Check admission again after successful journal outcome publication before
delivering the reply. Cancellation, deadline or integrity failure at that point
must refuse delivery while retaining the actual historical outcome; do not
rewrite a recorded observation into uncertainty or known-not-dispatched evidence.

## Native input producer

The installed Session API shall require an owned Linux request-input guard built
from the existing InputObserver, rather than an arbitrary production callback.
Any interaction or nonquiescent contact cancels this request permanently; later
quiet polls cannot revive it. Polls must continue to detect observer loss even
after cancellation, and an observer error is fatal rather than ordinary cancel.
No input grab or injected event is needed for these read-only observations.

After activation, reacquire input descriptors while the old observer still
covers the transition: poll old, construct new, poll old again, then poll new
before replacing old. Cancellation from either remains sticky, and any failure
invalidates the guard rather than permitting renewal retries. Activation refuses
to publish a session unless this handoff and final installed checks succeed.
This is input continuity only. It cannot preserve or create a page/process guard;
source reacquisition remains separately required before Reader/Writer continuation.

Verify actual InputObserver poll/quiescence semantics with scripted OS input and
owned runtime fixtures: quiet handoff, activity during replacement, initial or
unfinished contact without a completed gesture, error after cancellation, and
failures from old/new observer or replacement construction. No native qualification
follows from these host checks.
