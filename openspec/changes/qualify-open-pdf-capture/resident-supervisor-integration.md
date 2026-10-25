# Resident stock-service ownership and recovery

This is the next integration design, not an installed capability. The runtime
owner exists; stock-service takeover, independent recovery and Reader wiring do
not yet exist in the normal application. Keep those tasks open until verified.

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

OnSuccess and OnFailure request a separate `reader-buddy-stock-recovery.service`.
That service conflicts with and is ordered after Buddy, so PID1 completes Buddy
shutdown before recovery starts. Do not synchronously start the ordered stock
service from Buddy's ExecStopPost: it participates in stop ordering and can wait
on the very shutdown that is waiting for it. The recovery service retains normal
shutdown dependencies and must not resurrect services during system shutdown.

The recovery helper requires its own approved service context, the original
lease and an inactive/failed Buddy service with no remaining native process group.
Validate the retained cgroup directory/mount identity and recursive population;
a bare MainPID=0 or successful stop command is insufficient. Preserve uncertainty
if emptiness cannot be established. Once safe, start the unchanged stock unit,
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

First exercise the selected PID1 ordering/recovery behavior with uniquely named
owned fake-stock, actor and recovery units. Test clean exit, abrupt actor failure,
watchdog expiry and explicit stop while a child remains in the actor group. Prove
that recovery starts only after that recursive group is empty, restores the fake
stock exactly once and never touches either real stock or installed Buddy. Use
fresh bounded units and archive/clean only their exact files and groups. This is
a platform fixture, not native activation or document-preservation evidence.

Independent review accepted only that isolated fixture phase. The existing
retained-directory requirement is not yet implemented: an after-exit recovery
process cannot inherit Buddy-local descriptors. Record PID1 removing the stopped
service group explicitly; absence or reopening a pathname does not establish
retained identity. Resolve the actual proof handoff before product acceptance.
Also test recovery-helper failure/restart: a spent native-activation latch must
still allow idempotent stock restoration. Test shutdown-job cancellation without
shutting down the development tablet; a modeled isolated target is preliminary
evidence, not proof of real system shutdown behavior. These remain open gates.

Then implement/review the actual lease, helper, heartbeat and installed handoff.
Qualify bootstrap/resource relocation with an observation-only resident candidate
and independent recovery before enabling effects. Subsequent native acceptance
must still cover reusable capacity, actual Reader state, write/reopen/persistence,
current/adjacent reuse, middle/end insertion, cancellation and preservation.

Source basis: current application/runtime source and the directly captured live
platform inventory. The lifecycle above is a proposed integration design.
Systemd 255 documents [success/failure activation and ordering](https://www.freedesktop.org/software/systemd/man/255/systemd.unit.html)
and [watchdog and stop-command behavior](https://www.freedesktop.org/software/systemd/man/255/systemd.service.html).
Those contracts guide the design; they do not replace execution of its acceptance
checks on the target platform.
