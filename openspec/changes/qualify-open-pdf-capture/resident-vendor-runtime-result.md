# Owned companion runtime source checkpoint

This implements the runtime portion of the [companion lifecycle](resident-vendor-companion.md).
The fixed measured RM2 selection is explicit in `Launch`; all existing installed
activation and disposable-bootstrap callers still pass no companion. They cannot
silently adopt a new service contract. No new native activation occurred.

## Implemented source

The runtime pins the original executable, binds exec to its retained inode, keeps
the original argv0 and owns the Child handle throughout the session. It applies the
fixed environment, working directory, nice level and umask without inheriting
injection or service notification variables. Metadata, process incarnation,
executable link/inode and exact command line are checked during progress. A retained
descriptor does not make root-writable executable bytes an atomic snapshot.

Reader starts before companion; both exist before SDK handshake. Broker readiness
is required after the handshake so the reader's main-loop startup cannot be blocked
by a circular wait. Startup and admission share the original deadline. The broker
must identify the owned companion, with its unique owner and broker ID retained
across later request admission/delivery and reconnect.

Witnessed process or broker integrity failure permanently retires the companion
session; restored historical broker evidence does not enable reconnect. Typed
caller cancellation/deadline remains ordinary request retirement, while integrity
and an unreaped helper retain precedence. Pending SDK effect uncertainty stays in
the existing journal. Direct unguarded connection access refuses a two-process
session; requests use progress and delivery admission.

Shutdown dispatches companion termination before reader termination, then waits
under one original deadline. It retains separate child results and reports overall
reaping only when both are reaped. Failure to reap still requires independent group
recovery. A partial companion spawn failure cleans up the already-owned reader.
The initial `0e414236` increment retained forced KILL cleanup. Fresh read-only
loaded-unit inspection confirmed the vendor's TERM-then-KILL policy; the ordered
shutdown follow-up below implements that bounded source path. Separate reaping
evidence still does not establish graceful vendor persistence.

## Source validation

The host fixture uses real owned Linux processes and an explicitly synthetic broker
file. It covers handshake-dependent companion readiness, launch environment,
same-session reconnect, missing/dead companion startup, foreign broker ownership,
sticky refusal after original evidence returns, ordinary cancellation/deadline,
partial spawn cleanup and uncertain dispatched insertion after companion death.
It does not prove actual D-Bus behavior, vendor functionality, native mutation or
installed two-service restoration.

Independent review found and resolved cancellation misclassification and a missing
sticky integrity state. The first host run compiled and passed 29 tests, but three
new tests failed because their reader fixture omitted required arguments; the
fixture arguments were corrected. The revised full runtime suite passed 34 tests;
its spawn-failure fixture instead produced a child whose executable identity was
rejected, with both children reaped. The fixture now uses a missing interpreter to
exercise an actual spawn error without relying on ENOEXEC behavior. All seven
companion tests and strict all-target/all-feature Clippy then passed on Buddy
`0e414236437ac1f405f7376e4ef723310aaa2c77`; production code is unchanged from
that 34-test run. Formatting/whitespace checks passed. The fixed profile digest was
independently compared to the measured vendor digest and matches. The preserved
host logs retain missing Git metadata warnings; they do not identify an ARM build.
Docs guidance and all 88 strict OpenSpec items passed before publication.

A later test refinement requires handshake evidence and a typed startup deadline
for the absent-broker case. It exposed two fixture limits: a two-second bound could
end before companion launch, and the reader's three-second socket timeout could
end the reader before the expanded startup deadline. The companion test now uses
a five-second startup bound and a dedicated ten-second reader-fixture idle bound;
other reader fixture modes retain their original timeout. A test-only witness at
the successful missing-owner return additionally proves startup reached broker
observation, rather than merely creating the handshake marker. Independent review
accepted this coverage refinement. All seven companion tests and strict
all-target/all-feature Clippy passed on final test revision
`08576dbec7cdd375dd97468b1570f62a98f6965d`; formatting and whitespace checks passed.
Production behavior remains that of `0e414236437ac1f405f7376e4ef723310aaa2c77`.

## Ordered shutdown follow-up

Buddy `ba143d81e39fb544d5b369686329444a56049dba` implements the fixed phase
boundaries in the lifecycle contract without extending the original two-second
cleanup cap or caller deadline. The explicit two-process path requests companion
TERM, observes its completion or allocated timeout, then terminates the reader.
KILL escalation and final reaping have reserved intervals. An exhausted deadline
still reaches forced dispatch for both retained children. One-process callers keep
the earlier forced-cleanup policy.

Each child retains ordered signal attempts/errors and actual exit code/signal;
the overall report includes both child receipts and succeeds only when both were
reaped without an error. Signal dispatch alone does not imply termination. The
emergency companion destructor remains bounded forced cleanup.

Independent source review accepted this implementation. All 39 runtime tests,
including explicit root-only fixtures, passed, as did strict all-target/all-feature
Clippy and formatting/whitespace checks. Cooperative handlers are installed before
readiness and prove the companion is reaped before the reader's TERM handler runs.
Other cases require KILL when both children ignore TERM, preserve a modeled signal
failure while still stopping the reader, and verify forced dispatch after deadline
exhaustion. That last fixture retains its actual Child handles for separate cleanup;
it never signals a saved PID from a report. These tests use real owned host processes
with synthetic broker/fault evidence and do not reproduce the vendor's ninety-second
stop allowance or establish native data preservation.

## Versioned disposable service admission

Buddy `6d9224b3d4e26c928380c59c19dde40666e6d77d` adds the shared fixed-profile
vendor admission module and connects it to the disposable controller/observer.
Candidate version 3 explicitly carries the original sync baseline; ownership
version 2 binds those exact bytes to the candidate digest. Older candidates and
fixture candidates cannot opt in. A separate strict loaded-policy parser preserves
the existing baseline serialization and its watchdog-reset handling.

Admission pins the original sync executable, unit and drop-in, firmware/kernel,
loaded dependencies, launch and termination settings. It observes original sync
process/argv, group and broker ownership before stock stop. The controller's stock
stop waits for both original services and groups, and includes sync in subsequent
terminal checks. The observer selects its companion profile only from the pinned
candidate and checks original sync termination at admission and delivery.

Recovery never starts sync separately. A new stock start waits for the original
sync group to drain, including after controller interruption, and rechecks before
dispatch. Already-active stock is independently observed. Recovery retains the
exact stock baseline written to its restoration record; it does not recapture a
possibly replaced process. It waits for dependency-driven sync activation and bus
name readiness, retaining the first captured incarnation. Missing name is pending;
replacement or integrity loss refuses. Both restored incarnations remain retained
through source checks, Buddy restoration and final verification.

Independent review identified and verified fixes for the asynchronous name race,
stock recapture and missing sync-drain admission in interrupted recovery. On final
source, all 118 Linux host supervisor tests and strict all-target/all-feature Clippy
passed; formatting and whitespace checks passed. New tests cover policy/schema
changes, duplicate and reordered dependencies, absent-name-to-ready, replacement
during waiting, canceled/lost delivery, candidate/ownership version boundaries and
retained-pair orchestration. The first draft's 115-test/lint result is preserved
separately and is not evidence for the corrected source.

These are source and host-model checks. The existing PID1 fixture models stock and
Buddy; it does not model native vendor-pair transitions or broker ownership. No ARM
artifact, new native candidate, vendor-pair execution, capture or recovery result is
claimed here. A separate new staging script has only been syntax-checked and remains
unexecuted and unqualified. Existing spent candidate inputs remain unchanged.

## Remaining integration

Versioned installed profile/lease must consume the original sync service/process/
group and fixed policy/artifact admission, prove both original services stopped,
and verify both restored services before completion. The installed caller still
selects no companion. Disposable admission above still needs exact-artifact PID1
fixture checks and a fresh bounded native run. Host shutdown is not a guardian
recovery result. Native capture, automatic creation/reuse for Reader,
Writer and blank-start, broader simulator acceptance and coordinated delivery all
remain required.

Source basis: current runtime/request source and independent review; host-process
fixtures with synthetic broker evidence. The native profile constants come from
the earlier read-only vendor observations, not a successful owned companion run.
