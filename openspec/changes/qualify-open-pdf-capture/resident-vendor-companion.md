# Owned vendor companion lifecycle

This increment addresses the measured service dependency omission in
[the spent 1a94 attempt](resident-error-screen-result.md). It does not assert that
the omission caused that screen. Preserve the direct-parent SDK admission,
existing effect journals and single owned activation group. Extend the installed
resident runtime to own the reader and its required vendor companion together.
Do not start the original `rm-sync.service` while stock xochitl is inactive: its
`BindsTo` relationship can request stock again.

## Exact native profile

The measured RM2 firmware profile runs `/usr/bin/rm-sync` without arguments, as
root, from `/`, with nice level 19 and umask 0022. Its approved ordinary environment
is `HOME=/home/root`, `USER=root`, `LANG=en_US.UTF-8`, and
`PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin`. Exclude ambient variables,
adapter injection, activation-directory credentials, original invocation/journal
descriptors, watchdog and notification authority. Do not copy or retarget the
vendor service unit. Its original executable path and bytes remain authoritative.

The measured executable is a root-owned mode-0755 regular file, 3,409,308 bytes,
SHA-256 `1caf6493cce2132af89a9377679c19005bef1c5b0e658f704f95b4fdbd07138c`.
The original unit SHA-256 is
`076675399604b9fdbee7f267900bd4490de88d32ab1cc49a32d8d45a75bcac8f`;
its sole HOME drop-in SHA-256 is
`4d4345a6299448ade99878ddeeb894dd9a1a90de230bc3371a5e44237da7a795`.
Before native selection, pin these original unit and ordered drop-in bytes as well
as this executable. The original unit is Type=simple, has no watchdog, and owns
the system-bus name `no.remarkable.sync`; process spawn alone is not readiness.
The HOME drop-in and measured dependency graph are part of the admitted profile.
Fresh loaded-unit observation additionally confirms `KillSignal=15`,
`FinalKillSignal=9`, `RestartForceExitStatus=HUP INT PIPE TERM`, and the expected
nice level, bus name, original paths and no pending reload. Pin these loaded
settings as well as the unit bytes; ordering-only lists require duplicate-free
set comparison, not substring matching.
No pairing, account change, firmware change or new provider operation is added.

## Ownership and ordering

Before stopping stock, retain both original service incarnations, process/group
baselines, executable identities and policies. After stock stop, require both
original services terminal and both original groups empty/absent before any
replacement launch. Preserve each durable stop/start intent and original recovery
ownership; an uncertain attempt is never automatically repeated.

Prepare the companion executable with a retained file handle, bounded digest,
canonical path and metadata checks. Execute the admitted retained inode with the
original executable path as argv0, without injection. A post-spawn inode check
alone SHALL NOT substitute for binding the executable before dispatch. Verify
the running executable inode and canonical /proc executable link against the retained handle, its
PID/start/boot identity and original command line. Retain the Child handle for the
entire session. Both children belong to the existing owned activation group.

Start the reader first, then the companion, before waiting for the reader's SDK
handshake to complete. Startup of both uses the same original activation deadline
and admission callback. A partial launch failure must shut down every child that
was actually created. No helper process or second runtime may be left unowned.

Companion readiness requires the system-bus broker to identify the owned companion
PID as the current owner of `no.remarkable.sync`, bracketed by process/executable
checks. Also retain and bracket the unique connection owner and broker ID, so a
replacement owner or restarted broker cannot reuse an unqualified name sample.
Each bounded read-only broker query shares the caller's remaining deadline and
bounded subprocess cleanup; it must not activate a missing service. This explicit
admission check does not change the vendor's Type=simple semantics or prove
uninterrupted ownership between samples. Retain the observed identity and recheck at operation admission and delivery;
process liveness alone is insufficient after name loss or replacement. Readiness
never grants Reader identity, native page authority or permission to mutate.

## Requests and shutdown

Every resident request continues to check the same reader and companion process
incarnations and executable pins. Unexpected companion exit, replacement or
ownership loss is session integrity failure. Retire the connection, retain pending
effect uncertainty and require independent recovery; do not silently restart the
companion or replay a request. Reconnection retains this same two-process session.

Normal shutdown requests companion termination before reader termination, matching
the vendor stop ordering. The two-process path SHALL request TERM before bounded
forced KILL escalation, with a finite grace interval and reserved final cleanup
time inside one original deadline. An already exhausted budget SHALL still
dispatch necessary forced termination to both owned children. The historical
single-process forced-cleanup path is not evidence of this vendor shutdown policy.
Retain separate termination/reaping/error evidence for each child. A timeout or
failed termination cannot be reported as complete shutdown. Exhausting the wait
budget on one child SHALL NOT skip termination dispatch for the other. The existing independent
guardian must prove the entire owned group drained before restoring stock. A
partial failure must still attempt cleanup of the other owned child. Never signal
a process merely because a saved PID now exists.

Restoring original `xochitl.service` restores its original dependency graph. Verify
both restored service incarnations, original unit/drop-in bytes, executable/argv
and required running states before restoring Buddy or reporting completion. Do not
assume companion restoration from xochitl's state alone. Manager disable/update/
uninstall and cold boot retain their stock-first lifecycle obligations.

## Verification and remaining native gate

Use actual owned host child processes for normal startup, companion spawn failure,
early exit, identity replacement/refusal, partial startup cleanup, and termination
failure/timeout accounting. Exercise the real request/reconnect path with companion
loss, ensuring unresolved effects stay retained. Broker fixtures must cover missing
name, wrong PID, replacement during a query, malformed output and deadline/cancel.
Keep the source, simulator/process model, service fixture and actual native evidence
distinct. The modeled runtime must represent a missing/dead companion rather than
treating a spawned reader as a usable session.

The installed profile and disposable native candidate must explicitly include the
companion contract; an old one-process profile cannot silently opt in. Preserve old
spent candidates unchanged. Freeze and review new binaries and original service
admission before one new native selection. Only its actual source identity/capture,
preservation and independently verified two-service recovery can qualify that
native step. Automatic Reader/Writer/blank-start creation/reuse remains the required
product end state.

Source basis: measured vendor unit/drop-in, process environment and dependency
journal; current runtime/SDK ownership source. The owned-companion design is an
integration decision, not a proven explanation for the historical error screen.
