# Resident runtime ownership

The resident client accepts runtime identity and an activation-directory
descriptor. The Linux runtime integration component owns an explicitly launched
child, its one-use SDK
admission and authenticated connection. This is a required part of the eventual
lazy Supervisor, not a replacement for stock-service handoff, native qualification,
installed Reader acquisition or recovery to stock.

## Launch inputs and identity

An explicit caller supplies the independently approved profile, executable and
adapter file paths and exact SHA-256 digests, an absolute fresh activation path,
an explicit argument vector and one absolute startup deadline. Hashes are expectations, not caller-created
native qualification. The production caller must separately establish supported
firmware, an idle device, stock-service ownership and independent recovery before
launch. No ordinary Reader constructor or service unit invokes this component
until those obligations are integrated and qualified.

Open the three regular files without following final symlinks, bound their reads,
and copy their actual bytes into exclusively created files in the fresh owned
activation directory while hashing. Verify exact hashes and stable source metadata,
synchronize the copies, set executable mode0500 and profile/adapter mode0400,
and retain their descriptors and identities through startup. Launch from those
private copies, not the original replaceable paths. This is compatible with the
bootstrap's no-follow dladdr filename check; procfd preload paths are not.
Refuse writable-by-other-user artifacts, wrong ownership, changed files,
nonregular files or digest mismatch. Directory owners are trusted; this does not
isolate hostile same-UID code. The native bootstrap independently verifies its
loaded executable/profile/adapter as already specified by OpenSDK.

Create exactly one new mode0700 activation directory and a new mode0600
admission.bin. Use the current kernel boot UUID, actual parent PID/start ticks
and UID, a fresh activation UUID and CLOCK_BOOTTIME expiry clipped to the original
startup deadline and SDK's 60-second bound. Encode through ActivationAdmission,
synchronize the file and directory before spawning. Preserve the directory and
admission on every failure; never erase a consumed marker or reuse an old path.
Reject activation paths containing loader list separators or dollar-sign tokens,
and trailing slashes, before creation. Startup is capped at 60 seconds; cleanup
is clipped to at most two seconds. Fixed polling is a paced readiness observation,
never evidence of successful completion or a deadline renewal.

## Child and connection lifecycle

Spawn the private verified executable copy directly with the private adapter copy in
LD_PRELOAD, LD_BIND_NOW=1 and RSDK_ACTIVATION_DIRECTORY. No shell, detached helper,
ambient preload chain, process-name lookup, systemd mutation or reboot is used.
Forward the caller-approved arguments in their original order and exact string
boundaries through Command::args, with no shell expansion, joining or tokenization.
Before creating an activation directory, refuse NUL bytes, more than 16 arguments
or more than 16 KiB of total argument bytes. Empty arguments remain distinct.
The retained October 20 RM2 stock unit (SHA256
`adb0a2654ce9ec884f67c0627c22d539d6475dd0af80816819ee80bf13c0e6d6`)
starts `/usr/bin/xochitl --system`; a qualified caller must preserve this mode
after refreshing the live supported profile. That historical unit is source
evidence for the missing argument seam, not current device-state admission.
Argument forwarding does not qualify relocation, argv[0] or resource lookup.
The child starts in the explicit root working directory, not an inherited checkout.
Clear the entire inherited environment. Accept only explicit approved HOME, USER,
LOGNAME, PATH, LANG, LC_ALL, TZ, XDG_RUNTIME_DIR and QT_QPA_PLATFORM values;
QT_QPA_PLATFORM must be a simple platform identifier, not a plugin path/options.
No inherited LD_AUDIT, LD_LIBRARY_PATH, Qt/QML plugin paths or unrelated variables
reach the child. Supply the three loader/admission variables internally afterward.
The caller owns approval of the supplied ordinary environment values; host checks
do not qualify the actual tablet's environment or relocated executable resources.
The launching process remains the child's direct parent and sole SDK peer.
Standard output/error go to exclusively created owner-only files inside the
activation directory, keeping diagnostics out of inherited application output.

Observe the owned Child handle, its actual /proc executable inode and process
start ticks. Wait only for endpoint creation under the original absolute startup
deadline, then attempt one authenticated ResidentConnection handshake with a
fresh connection nonce and operation. No connection retry or effect replay is
permitted. Handshake correspondence is protocol readiness only; it does not
establish an open Reader, native mutation support, page ownership or capture/write
authority. The admission's consumed hard link must match the original file before
returning the runtime. Verify file/directory/process identity again after Ready.

The installed admission callback continues during endpoint creation and through
the SDK's progress-aware handshake, on the original caller thread and unchanged
deadline. After each callback, recheck copied artifacts and the child before
accepting readiness. Callback failure after spawn uses the same owned cleanup;
it cannot skip cleanup or erase the preserved evidence. See
[caller progress](resident-progress-integration.md) for the request-side contract.

Retain the Child, connection and activation-directory descriptor together. The
caller uses the existing ResidentConnection methods and Store-owned effect journal;
no second request journal or binding registry is introduced. Startup failure,
explicit shutdown or dropping this owned runtime closes the connection and stops
only its direct child. Use bounded try_wait/kill/reap, never an unbounded wait.
Preserve the original LostRequest when closing; killing a process does not settle
native effects. A consumer reply-retention failure must retain its original
indeterminate operation/digest across later calls and repeated close, even when
the SDK already correlated the response and retired its own pending request.
This does not change the journal reload policy: a future fresh connection still
uses the actual stored outcome and never replays a consumed operation.
Record inability to reap as recovery-needed, rather than claiming
cleanup. Diagnostic files and admission evidence remain available to the caller.
Write shutdown diagnostics through the retained directory descriptor, even if
the original path was renamed or replaced. Never follow a replacement root when
recording cleanup. Report diagnostic publication failure in the shutdown result.

The owner must not be dropped per conversation. The eventual Supervisor retains
one runtime across requests. Its separate stock-service lease will own one lazy
transition after the first supported gesture and restoration after shutdown,
failure, disable/update/uninstall. A process restart invalidates Reader/input
handles and demands fresh acquisition. Cold boot must remain stock, and failure
must disable further activation for the boot/session rather than create a loop.
Those policies and UI-independent stock recovery remain required integration.

## Verification and limits

Exercise the actual Linux filesystem, child process and authenticated SDK socket
with an owned test executable: admission bytes and modes, parent/process identity,
one handshake, successful observation, child exit, missing/late endpoint, wrong
artifact hash, changed or consumed admission, and shutdown/reaping. Test children
do not load the proprietary adapter; explicitly distinguish that fixture launch
from the production preload environment. No tablet or system service is touched.
Use one absolute deadline throughout and preserve evidence after each fault.
Exercise directory replacement after Ready: subsequent access refuses, the owned
child is reaped, and cleanup evidence stays in the original directory inode.
Exercise the actual argument path with the owned child, including spaces, empty
values and shell metacharacters as literal data; reject invalid vectors before
directory creation. Test-only launch customization only removes native preload.

Native constructor ordering, actual preload behavior and copied-executable resource
resolution, UI readiness, stock-service
handoff/recovery, reusable native capacity, first-gesture wiring, heartbeat and
crash-loop handling still need their full acceptance before production activation.
This component must not report those as implemented by its host tests.

Source basis: current Buddy Workflow/service/client/runtime source and the SDK
bootstrap, ActivationAdmission, Linux Client and activation.h contracts. The
owned launch component implements this bounded contract; native behavior remains
unqualified. Verification is recorded separately from the required product gates.
