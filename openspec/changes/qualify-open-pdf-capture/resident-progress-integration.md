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
events must retain the resident child. The existing `Session::connection` helper
does not yet make that distinction; do not use it as the product request route.
Implement separately reviewed reconnect to the same verified runtime with fresh
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
Session still needs typed health/input classification and lease/group checks in
its product request route before these runtime primitives may be composed there.
