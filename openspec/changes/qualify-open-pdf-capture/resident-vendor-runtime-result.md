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

## Remaining integration

Versioned installed profile/lease and native candidate admission must retain the
original sync service/process/group and fixed policy/artifact identities, prove
both original services stopped before replacement, and independently verify both
restored services before Buddy/completion. Existing callers intentionally remain
unchanged until that path is implemented and reviewed. Host shutdown is not a
guardian recovery result. Native capture, automatic creation/reuse for Reader,
Writer and blank-start, broader simulator acceptance and coordinated delivery all
remain required.

Source basis: current runtime/request source and independent review; host-process
fixtures with synthetic broker evidence. The native profile constants come from
the earlier read-only vendor observations, not a successful owned companion run.
