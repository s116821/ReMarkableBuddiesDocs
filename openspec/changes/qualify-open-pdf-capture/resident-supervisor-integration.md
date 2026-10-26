# Resident stock-service ownership and recovery

This is the integration design, not an installed capability. The runtime owner,
lease/context support, service sampler, fixed-profile restoration helper,
isolated CLI dispatch and service health exist. Installed activation composition
is being verified; the normal Reader path, installed independent recovery and
approved payload/profile remain open. Keep those tasks open until verified.

## Refreshed platform evidence

Bounded read-only SSH inventory on October 25 at 21:36–21:37 UTC confirmed the
authorized RM2 runs firmware 3.28.0.172, kernel 5.4.70-v1.6.3-rm11x and systemd
255.21. Stock xochitl was active/running with no pending job. Its executable,
vendor unit and vendor drop-in retain these respective SHA256 values:

- `071d85beef3ef2d4cc0e11002140b27b82a2cc04a2ed740a5669f591069b77df`
- `adb0a2654ce9ec884f67c0627c22d539d6475dd0af80816819ee80bf13c0e6d6`
- `b15560e1dca2f4451b59537c490015aa2f5ea691437bd7ddddc7a65411aaad6e`

Stock ExecStart is `/usr/bin/xochitl --system`; policy includes
KillMode=control-group, Restart=on-failure, RestartMode=direct, a 60-second watchdog,
90-second stop timeout and OnFailure=remarkable-fail.service. Preserve the vendor
files and policy. Never convert a stock restoration into an injected restart.

The device uses a hybrid hierarchy: cgroup2 mounts at `/sys/fs/cgroup/unified`,
and the named systemd v1 hierarchy mounts at `/sys/fs/cgroup/systemd`. Its root
`/sys/fs/cgroup` filesystem is tmpfs, so assuming that root is cgroup2 is wrong.
Both running service groups have readable cgroup2 `cgroup.events` files with
`populated 1`. Determine and validate the actual mount and service path; do not
hardcode a fully unified host layout into recovery.

Installed Buddy is active/running, has KillMode=control-group and Delegate=no,
but has no watchdog or success/failure recovery handler. Its installed binary
hash is `caa5dd3e51e5443d665c727c4ff5730af475ec6d4d7175ef5eb3f78fab57f03b`.
That installation is not the new resident implementation. No files, services,
input, UI state or account settings were changed by these reads.

## Intended product lifecycle

The executable exposes one exclusive `--resident-stock-recovery` command. Dispatch
it immediately after argument validation, before dotenv, configuration, Store,
provider, sync or device startup. Reject combinations with ordinary/maintenance
arguments. It accepts no path, unit, environment or deadline override. On other
platforms it refuses without starting the ordinary application.

Cold-boot recovery has a distinct `NoRecordedActivation` outcome. Only ENOENT for
the exact final `activation.json` component below the existing protected fixed
directory permits that outcome, with the directory identity and absence checked
again before return. Missing/untrusted parents, symlinks, malformed/partial/stale
records and read failures remain errors. This outcome makes no service/process
call and claims neither stock readiness nor proof that activation never occurred.
An existing record always enters full recovery admission. Neither path removes,
repairs or recreates the latch. The installed common activation guard and package
lifecycle must still enforce retention; this command alone does not establish them.

Ordinary Linux startup checks the same fixed latch before dotenv/configuration,
Store, provider, sync or device initialization, independently of any optional
resident mode. Any occupied activation record refuses ordinary startup, including
an unreadable or invalid record. Explicit non-device Writer and maintenance
commands remain separate; Writer may use a provider but neither command class
gains native activation permission. An absent boot directory permits the
existing non-resident application path; it never authorizes native activation.
The future first-gesture activation must require that protected directory and
exclusive publication again immediately before stock takeover. An initial empty
check is not a reservation or a replacement for that atomic publication.

Keep the resident owner in the normal Buddy process for the session. Use PID1's
service watchdog and a separate stock-recovery service as the UI-independent
recovery path, packaged with the same application. No network/admin endpoint,
second effect journal, per-conversation UI restart or general process-name killer
is introduced. Cold boot starts stock normally. Only the first supported gesture
may request the compatibility-gated lease and native activation.

Before stopping stock, require a supported live firmware/artifact/service profile,
the installed recovery definitions, actual Buddy service MainPID/incarnation and
invocation, the expected nondelegated control group and an idle admitted source.
Publish and synchronize an exclusively owned boot/session lease under `/run`,
including a fresh activation identity and original stock baseline. It is service
ownership metadata; native effects remain in the existing Store journal. Reject
an old, malformed, unresolved or already consumed lease instead of resetting it.

Request stock stop through PID1 and observe the same job/service/group under the
original activation deadline. Do not launch the resident child while the stock
service or its recursive group remains populated. If stop or native startup
fails, close/reap the owned native child where possible and exit the Buddy
service so independent recovery owns the remainder. Protocol Ready does not
establish a valid Reader or writing permission.

The proposed installed Buddy service uses Restart=no to avoid automatic native
crash loops, explicit control-group cleanup, bounded stop, and watchdog support.
The watchdog must track actual main-loop/operation progress, including the
existing 90-second model deadline and at-most-60-second activation; an unrelated
thread that pings indefinitely is not sufficient. Final heartbeat placement and
the service timeout values require implementation review before installation.
The resident child must not inherit Buddy's notification socket.

Implement health notifications on the calling main thread, without a keep-alive
thread. Read systemd's notification/watchdog environment before dotenv and ordinary
initialization; require the supported 120-second watchdog and an absent or matching
WATCHDOG_PID. Incomplete or malformed notification settings refuse. Existing
non-notify operation keeps its current behavior. Send READY only after ordinary
initialization completes, then send WATCHDOG at most every 30 seconds when actual
idle-input polling or request-progress callbacks succeed. Both supported native
history input and the ordinary touch fallback must call the same progress hook.
Keep the existing bounded input-observation timeout semantics unchanged.

Use a nonblocking Unix datagram socket with no retry/wait on a full or failed
notification endpoint. A failed send, wrong process/thread, clock regression or
at least 120 seconds since the last successful READY/WATCHDOG send permanently
fails that health instance. A callback that does not send cannot renew that deadline;
later callbacks cannot revive it. Propagate failure out of the ordinary main loop
so independent service recovery can run. READY/WATCHDOG establish service progress
only, never SDK/page readiness, current source identity or mutation permission.
The 120-second service window covers the existing at-most-95-second model request
and at-most-60-second activation, but does not extend either operation deadline.
No notification environment or socket may be inherited by the resident child.

The notification wire contract follows upstream
[sd_notify](https://www.freedesktop.org/software/systemd/man/255/sd_notify.html)
and [sd_watchdog_enabled](https://www.freedesktop.org/software/systemd/man/255/sd_watchdog_enabled.html).
Their standard semantics are distinct from target PID1/unit/native qualification.

OnSuccess and OnFailure request a separate `reader-buddy-stock-recovery.service`.
That service conflicts with and is ordered after Buddy, so PID1 completes Buddy
shutdown before recovery starts. Do not synchronously start the ordered stock
service from Buddy's ExecStopPost: it participates in stop ordering and can wait
on the very shutdown that is waiting for it. The recovery service retains normal
shutdown dependencies and must not resurrect services during system shutdown.

The recovery helper requires its own approved service context, the original
lease and an inactive/failed Buddy service with no remaining native process group.
Validate the original cgroup identity against the same mount and namespace and
establish recursive emptiness under the concrete contract below; a bare MainPID=0
or successful stop command is insufficient. Preserve uncertainty if emptiness
cannot be established. Once safe, start the unchanged stock unit,
then observe its actual process, executable, policy, group and absence of pending
jobs under one bounded recovery deadline. Service-level recovery is distinct
from visual UI readiness and document persistence, which need native acceptance.

Keep a boot-scoped failure/consumption latch and all unresolved effect evidence.
Do not automatically launch another native session after failure. Manager
disable/update/uninstall must stop Buddy and wait for confirmed stock recovery
before replacing/removing the helper or payload. Reboot clears runtime activation
and returns to untouched stock startup. Incomplete recovery remains visible and
does not authorize repeating a native effect.

After any activation restart, discard device/input/Reader handles and reacquire
source and cancellation from fresh evidence. Library/unknown/different-source
state must refuse the pending operation. Do not manufacture synthetic
PageObservation or visit/revision/write authority from resident ReaderFacts.
Installed acquisition, binding and capture/write composition remain required.

## Concrete verification before stock takeover

### Installed caller composition

The installed handoff reuses recovery's protected-file/profile/policy checks;
it does not accept arbitrary unit names, executable paths, environment or command
overrides. Fixed native payload siblings are `resident-profile.json` and
`libremarkable-resident.so` beside the application and `resident-recovery.json`.
Their independently qualified hashes come from the recovery profile. No approved
profile is added by this source implementation.

Under one at-most-60-second absolute activation deadline, admit the unchanged
installation, the current main Buddy process in its original service invocation,
an inactive recovery helper with no queued job, and actual unmodified running
stock. Require the fixed protected boot directory and an unoccupied latch. The
ordinary main-thread health owner must be active; source/input cancellation checks
remain the product caller's responsibility and run at every handoff boundary.
A callback's success alone does not establish current page identity.

Arm a sticky exit-on-drop guard tied to the actual ready main-thread health owner
before attempting publication: exclusive creation/write/sync can fail after
leaving a partial occupied record without returning a `Lease`. Every such error
must exit the ordinary runtime; do not wait for successful publication to arm it.
Publish the immutable lease exclusively, then repeat installation, Buddy/helper
and original stock checks before issuing one fixed nonblocking stock stop with
`--job-mode=fail`. No stop retry or conflicting-job replacement is permitted.
Repeat input/health and the original deadline immediately before that command,
after all service observations. After runtime artifact copying and synchronized
admission preparation, but before spawning the child, recheck the installed
lease/artifacts/Buddy/helper, absence of competing stock, cancellation, health
and original deadline. Recheck the copied files after that callback. A refusal
at either boundary performs no corresponding stop or spawn; post-handshake
validation cannot substitute for this pre-spawn check.
Continue the same installed checks during endpoint and handshake waits; the
callback never renews activation's deadline. Successful replies remain historical
facts and do not establish post-restart source continuity.
Observe stock termination and its original recursive group under the original
deadline; require stable loaded policy and no job/main/control process. A newly
running or changed stock incarnation refuses. Only the original empty group or
its qualified deletion can permit launch; a missing unrelated path cannot.

The session owns the lease, pinned installation and `ResidentRuntime` together.
Its fresh child directory is derived from that lease's activation UUID below the
fixed boot directory; the SDK admission retains its independently fresh protocol
nonce. These identities serve different purposes and must not be silently
substituted. Before child launch and when exposing the live connection, recheck
the lease, installation, Buddy context and absence of competing stock. The child
must belong to the admitted Buddy group. Activation failure after lease publication,
or verified installed/runtime/health integrity failure, is fatal to the ordinary
runtime so independent recovery owns stock restoration;
the latch and diagnostics remain. The successful session retains the exit guard;
session shutdown/drop permanently fails that same health owner, causing the
existing main-loop fatal predicate to exit. Merely stopping the child while the
ordinary loop remains healthy would strand stock and is forbidden. Dropping the
session only closes/stops its owned child and never starts stock itself.

Established-session request cancellation, timeout or ordinary connection/idle
retirement must not be classified as whole-session failure or restart xochitl.
The installed `Session::request` and `Session::reconnect` operations replace the
unscoped connection accessor. Their typed input callback distinguishes ordinary
cancellation from observer failure, and progress retains health, installed lease,
service incarnation, stock exclusion, group and original child checks. A reconnect needs
fresh connection/handshake/server nonces and must preserve original uncertain
effects without replay. It does not replace the child or consumed activation.
See [the installed request result](resident-installed-request-result.md) for exact
source and validation status. This component does not supply the first-gesture
Reader/Writer caller or qualify an installed native profile.

This service handoff cannot manufacture a native page observation or a supported
SDK mutation capability. The first-gesture product route must also discard old
input/Reader handles, reacquire source and cancellation, and refuse an unknown or
different source before continuing Reader/Writer. Installed payload/bootstrap,
source continuity and reusable native capacity still need their actual acceptance.

First exercise the selected PID1 ordering/recovery behavior with uniquely named
owned fake-stock, actor and recovery units. Test clean exit, abrupt actor failure,
watchdog expiry and explicit stop while a child remains in the actor group. Prove
that recovery starts only after that recursive group is empty, restores the fake
stock exactly once and never touches either real stock or installed Buddy. Use
fresh bounded units and archive/clean only their exact files and groups. This is
a platform fixture, not native activation or document-preservation evidence.

Initial independent review identified that an after-exit recovery process cannot
inherit Buddy-local descriptors. The observed group removal motivates the explicit
deletion contract below, replacing that descriptor-handoff premise. The fake
helper failure/restart test now passes; the production consumed-activation lease
must still permit idempotent stock restoration. Shutdown-job cancellation remains
open. Test it without shutting down the development tablet; a modeled isolated
target is preliminary evidence, not proof of real system shutdown behavior.

### Deleted-cgroup recovery contract to implement and qualify

The five live fake-unit cases in
[resident-supervisor-fixture-result.md](resident-supervisor-fixture-result.md)
all found the actor group removed before recovery. Keep the after-exit helper;
do not introduce a persistent monitor merely to wait for a final event read.

The lease records the actual populated service cgroup device/inode,
validated cgroup2 mount identity and path, mount/cgroup namespaces, boot, Buddy
invocation and process incarnation, and actual Buddy parent membership. Child
membership, when available, is additional corroboration rather than a recovery
prerequisite: stock may already be stopped when Buddy fails before native spawn
or before recording the new child. Qualified fork inheritance and no migration
must cover that entire spawn/record crash window through the original parent
group. Do not require a post-spawn receipt to restore stock or introduce another
native effect journal. Missing parent membership still refuses activation.
Recovery must bracket its lookup with the admitted terminal Buddy state, MainPID=0,
no pending activation/job and the incarnation checks below. A consumed activation lease stays
consumed while repeated stock restoration can finish idempotently. The helper's
Conflicts/After relation prevents overlapping ordinary Buddy startup during its
restoration; startup also checks the same lease/latch before any native launch.

PID1 retained the actor's invocation/process metadata for the first live helper
call, then cleared it before a subsequent call (see the fixture result). Requiring
the cached original invocation on every retry would strand otherwise safe stock
recovery. Distinguish two explicit branches; never interpret missing fields as zero:

- Retained metadata must match the original lease's Buddy invocation and process
  incarnation under the admitted inactive/failed terminal state.
- Fully cleared metadata requires an approved **loaded** unit with the expected
  policy, inactive/dead, MainPID=0, no job, an explicitly empty InvocationID,
  ExecMainPID=0 and ExecMainStartTimestampMonotonic=0. It additionally requires the
  unchanged original private boot lease and qualified `OriginalAbsent`; merely
  `EmptyOriginal` is insufficient. Every installed native-entry path must enforce
  the same boot-scoped non-resettable activation latch, without alternate-directory
  bypass. This branch proves prior group deletion and prevention of another native
  launch; it does not claim PID1 still remembers the original invocation.

Bracket group observation with both service samples. Refuse partial clearing,
missing/error fields, not-found/masked/unapproved policy, or any changed nonempty
invocation. Preserve a regression where the helper fails before writing any
terminal proof marker and PID1 has fully cleared metadata by the next attempt.
No persistent monitor or second native-effect journal is needed for this retry.

Allow two separately typed outcomes only: the unchanged original group reports
recursive `populated 0`, or lookup of its exact validated location returns ENOENT
under the qualified kernel-deletion contract. Changed mount/namespace/boot,
replacement inode, a symlink, permission/I/O errors, missing parent membership
or uncertain service incarnation refuse. Never map arbitrary read errors to an
empty group. Successful restoration still requires the actual stock service,
process/executable, policy and job checks in the original recovery deadline.

This relies on trusted PID1 and no task migration out of the owned group, no
external privileged cgroup renames or hierarchy replacement. `Delegate=no` does
not itself restrict privileged application code; qualify the supported payload's
group membership and make these assumptions explicit in the platform profile.
Do not claim robustness against another privileged actor moving native processes.

Upstream [Linux 5.4 cgroup destruction](https://raw.githubusercontent.com/torvalds/linux/v5.4/kernel/cgroup/cgroup.c)
rejects populated groups and live child groups before removal, then prevents
migration into the dying group. That motivates the deletion outcome; the vendor
kernel contract and implementation remain to be qualified. Upstream
[kernfs reads and polling](https://raw.githubusercontent.com/torvalds/linux/v5.4/fs/kernfs/file.c)
can report ENODEV after deactivation, and ordinary changes can also signal poll
error/priority. Neither event alone proves emptiness. A retained descriptor may
aid measurement but is not a substitute for the full recovery predicate.

The support implementation and real-filesystem refusal tests are recorded in
[resident-supervisor-integration-result.md](resident-supervisor-integration-result.md).
The fresh isolated fake-group check below demonstrates direct populated-group
removal refusal and subsequent PID1 deletion; it does not qualify child-only nested
groups or privileged migration. Shutdown cancellation remains a separate open
requirement; none of these checks permits a real stock takeover by itself.

The isolated `populated-delete` fixture captures the fake actor and its
sleeping child's actual unified membership, requires both to belong to the exact
nonce-owned actor group, and observes that group's identity and `populated 1`.
From the fake actor it attempts to remove only that exact group, requires failure
with the C-locale busy diagnostic, then rechecks unchanged identity and population.
It then exits normally and uses the existing ordered recovery/cleanup assertions
to observe PID1's later removal. All original independent unit bounds remain.
This is a narrow vendor-kernel behavior check; it does not establish safety under
privileged task migration or qualify native startup/stock takeover by itself.

### Initial implementation boundary

Linux `resident_supervisor` supplies support for the forthcoming installed
helper. It captures the actual caller process incarnation and cgroup membership,
boot and namespace identities, exact cgroup2 mount record, mount/system.slice
identities and original service-group identity. All group path components are
opened relative to directory descriptors with no symlink following. Bound proc
and events reads, reject duplicate/malformed fields, and bracket observations
with unchanged context. Group observations are typed as populated, unchanged
empty, or original location absent. Absence is not itself execution authority;
the qualified platform and actual service-state checks remain mandatory at the
helper integration boundary.

Publish a versioned immutable service-ownership record in an existing private
boot-scoped directory using exclusive creation, file synchronization and directory
synchronization. Record the source profile/artifact hashes and the original stock
service baseline alongside the group baseline and activation identity. The
module never overwrites or clears malformed, partial, stale or consumed state at
the supplied lease path. Installed startup must enforce one fixed common path
whose occupied record prevents another automatic activation. Recovery can reopen the
same record repeatedly, without consuming a one-shot right to restore stock.
No generic state journal or fabricated native child receipt is introduced.

The record retains Buddy's exact nonzero systemd
`ExecMainStartTimestampMonotonic` in microseconds separately from the parent's
`/proc` start ticks. Admission must verify it in the same service bracket as
MainPID and InvocationID; recovery compares the saved systemd value without
converting between representations. Publication rechecks current caller
incarnation, exact unified group membership and group population before and
after synchronization. A late mismatch returns failure and leaves the occupied
lease untouched; it cannot authorize stock stop. These checks detect stale
capture and do not remove the qualified no-migration assumption after return.

The ownership module does not activate the resident child or install service
units; the service submodule below adds bounded systemctl observations and the
recovery submodule's fixed stock-start command.
Its tests use actual Linux files and malformed/replaced
path cases; fake filesystem fixtures cannot qualify kernel cgroups. The next
recovery implementation supplies bounded stock commands and profile-bound stock
verification. The actual first-gesture caller, installation and qualified profile
remain required before native activation.

Then implement/review the fixed installed lease/latch caller, helper, heartbeat and handoff.
Qualify bootstrap/resource relocation with an observation-only resident candidate
and independent recovery before enabling effects. Subsequent native acceptance
must still cover reusable capacity, actual Reader state, write/reopen/persistence,
current/adjacent reuse, middle/end insertion, cancellation and preservation.

### Service observation implementation

The implemented observation boundary samples PID1 through a fixed absolute `systemctl`
executable and explicit properties for one validated unit. Clear inherited
environment, select the system manager and C locale, disable pager/password
interaction, and pass arguments directly without a shell, with `--` before the
unit so its name cannot become a command option. Keep stdout/stderr
nonblocking and individually bounded to 16 KiB. Clamp each observation to the
remaining operation deadline and at most three seconds; failed/expired commands
must kill and attempt to reap only their owned child under a separate two-second
cleanup bound. Never wait on a pipe-reader thread after the deadline. Nonzero
exit, stderr, malformed UTF-8, missing/duplicate/unknown fields and overflow refuse.
Success requires zero exit and both pipe EOFs before the original deadline;
every error after spawn enters the same bounded cleanup path. An unreaped child
is explicitly reported. Keep this runner separate from the older maintenance
observer, whose unconditional wait/join cannot satisfy this bound.

Parse explicit unit identity/load/state, main/control/last-main process IDs,
InvocationID, exact start timestamp, pending Job and ControlGroup. Preserve the
explicit selected service-policy properties for comparison with the supported
installed profile. Both service samples surrounding group observation must be
independently valid for the original lease and unchanged policy; a transition
between retained and cleared identity inside that bracket refuses that attempt.
Return the exact bracketed group outcome alongside the terminal identity and
policy snapshot, so the helper can distinguish unchanged-empty from qualified
deletion without performing an unbracketed replacement read. Recheck the operation
deadline after the final lease read and bracket validation before returning success.
The retained branch allows only inactive/dead or failed/failed with no main or
control PID and no job. The cleared branch is stricter as specified above.

These observations alone must not expose a stock-start operation or assert that
the installed profile, common activation latch or vendor deletion contract is
qualified. The actual helper must combine those independently established facts,
its own service context and the original current lease before a bounded stock
start, then verify the resulting actual stock process and policy. Regression
fixtures must exercise real owned command children, timeout/output/error cleanup,
both terminal branches, partial clearing, changed invocation/policy and state
changes across the bracket. This is service-integration coverage; no synthetic
Reader or native-write authority follows from it.

A fresh read-only target sample at 22:39:36 UTC confirmed all 26 selected
properties are emitted using this exact option/operand ordering. Both existing
real service PIDs/invocations and the boot identity remained as recorded above.
The installed Buddy still has Restart=on-failure, no recovery handlers and
WatchdogUSec=0, so it does not satisfy the proposed recovery policy. Stock reports
DefaultDependencies=no and explicit Conflicts=shutdown.target; preserve its
vendor policy. The new helper must retain its own normal shutdown dependencies.
This read verifies the property contract, not installation or recovery behavior.
The exact script, stdout/stderr and receipt are retained in the local evidence
directory `supervisor-properties-ca50e981172d4cd6a9c1169ab354934e`.

### Installed recovery helper implementation contract

Use one fixed `/run/reader-buddy-resident` activation directory and a separately
installed, root-owned `resident-recovery.json` beside the application payload.
The installed entrypoint takes no path, unit, environment or command overrides.
The recovery profile is a release/Manager artifact approved after platform and
payload qualification; do not generate approval by copying a live service sample.
No approved production profile ships until those gates pass. The fixed helper API
and exclusive CLI dispatch are implemented, but no production service invokes them yet. Bind its exact bytes
in a distinct version-2 lease field, preserving the native profile digest separately.
Version-1 records remain occupied and cannot silently upgrade or authorize takeover.

The helper verifies root-owned immutable artifact bytes and all selected loaded
policies, including its own ordered oneshot service, against that profile. It
requires its actual process incarnation and membership to match PID1's running
ExecStart process. Unit files, executable and drop-ins must match the installed
profile and the original lease's stock baseline. Recheck the profile and lease
through the operation; changing installation during recovery is an error.

Once the original Buddy terminal/group bracket is admitted, request only
`systemctl --system --no-pager --no-ask-password --no-block --job-mode=fail start -- xochitl.service`.
Issue this at most once per helper invocation, only for inactive/dead or
failed/failed stock with no job or process. Already active stock is verified
without a command; an existing start transition is observed without another
request. Never replace another PID1 job, reset a failed unit, stop/restart stock,
or kill a stock process. Explicit job-mode=fail closes the conflicting-job race
between sampling PID1 and submitting the request. A failed or timed-out start command may already have
queued a job; retain the lease and report uncertainty instead of retrying it.

Recovery may begin while the original stock shutdown is still running. Distinguish
an explicit deactivating stop/final substate from startup or an unknown queued job;
the numeric Job property alone never identifies its operation. Waiting through
shutdown requires the lease's original stock invocation and ExecMainPID, an
original-or-zero MainPID, expected group, and a nonzero stable systemd start
timestamp. A control process may remain during that wait. Preserve the first
shutdown identity across observations. A later terminal sample must retain that
identity or be completely cleared and inactive/dead; no main/control process or
job and an empty stock group are still required before the helper's first start.
Observing startup or any unknown pending job permanently forbids a subsequent
start request in that helper invocation. Never clear that restriction merely
because a later sample is deactivating. An attempted start also remains one-shot.

Use one 120-second monotonic helper deadline, retaining the three-second command
and separate two-second cleanup bounds. Sample TimeoutStartUSec with the other
approved loaded policy: the supported helper profile uses exactly `2min 10s`,
Buddy WatchdogUSec exactly `2min`, and stock TimeoutStopUSec `1min 30s`. Those fixed
values make the budget assumptions reviewable; they do not prove that every
shutdown/startup completes within the budget. Qualification must account for
systemd's per-phase stop timeouts and actual vendor commands before approving
the installation. Expiry during shutdown issues no start or retry. Upstream
[systemd 255.21 service states](https://github.com/systemd/systemd-stable/blob/v255.21/src/core/service.c)
define the deactivating stop/final substates used for this distinction; target
behavior still requires the installed acceptance checks.

Success requires stable loaded active/running stock with no pending job/control
process, the exact executable and argv, unchanged process start ticks, populated
expected cgroup and actual membership, and matching policy. Observe those facts
between service snapshots under the same monotonic recovery deadline. Verify
Buddy remains terminal and the helper still owns its approved context before
returning. This is service restoration only; visual readiness, document effects
and persistence need their separate native checks. Fixture seams stay private
and cannot select arbitrary commands or disable checks in the installed entrypoint.

Source basis: current application/runtime source and the directly captured live
platform inventory. The lifecycle above is a proposed integration design.
Systemd 255 documents [success/failure activation and ordering](https://www.freedesktop.org/software/systemd/man/255/systemd.unit.html)
and [watchdog and stop-command behavior](https://www.freedesktop.org/software/systemd/man/255/systemd.service.html).
Those contracts guide the design; they do not replace execution of its acceptance
checks on the target platform.
