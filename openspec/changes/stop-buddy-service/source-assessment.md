# Verified source assessment and remaining qualification

Historical source packet below: b008027 and the pending bare APK are retained
with their original evidence. Current proposed consumer reconciliation uses
delivered91dcc601 and is defined in package-record-contract.md. The old resident
paths/Profile1/Lease2 are not current Stop admission; production gates remain empty.

Source packet: 108119bytes SHA256
`5e2aa83671499566ffab2bfeb457e91006c237eb5811c663150734a5620de34c`.
All18payload lengths/SHA256 values and17tracked Git blob identities independently
verified. This is committed-source evidence, not deployed tablet observation.

## Fixed service and package compatibility

At [main b008027](https://github.com/s116821/ReMarkableBuddies/tree/b008027b378f8f06422c17d5e58ed7bb041e402b),
[cicd/deploy/reader-buddy.service](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/cicd/deploy/reader-buddy.service)
is Git blob337d2eb153b2778f37e2f893ced9f259e693cf55, SHA256
434d00dc6b62096b782dc85d417338a8283269f913f954af897a85cbc8ba64a6.
It runs /opt/bin/reader-buddy from /home/root, Type=simple,
Restart=on-failure/RestartSec=5, with the protected environment file. It contains
no explicit ExecStop, TimeoutStopSec, KillMode or SendSIGKILL. Effective PID1
properties and drop-ins must therefore be observed; defaults are not a profile.
README manual service examples are not stronger installed-state evidence.

The separately pending [APK source3f0a10a](https://github.com/s116821/ReMarkableBuddies/blob/3f0a10a3e62f364f14225200d5eed5281103d3dc/cicd/release/apk_generate.py)
packages exactly usr/bin/reader-buddy, LICENSE and build.json. Its parser rejects
scripts/triggers/extra members. There is no unit installation or stop/recovery
hook. Thus an APK build does not establish a /opt binary, service ownership,
loaded unit agreement or independent stock recovery. Do not repair/copy/symlink
between those layouts as part of Stop. Actual build/signing remains separate.

## Ordinary and resident shutdown

The ordinary [main.rs559–664](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/main.rs#L559)
checks the occupied activation latch before ordinary startup, captures health
notification context, loads configuration/roles/mode, retains Store/lifetime and
sync worker, and enters the ordinary orchestrator. The supplied ordinary entry
and [run_loop760](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/orchestrator.rs#L760)
do not demonstrate a SIGTERM-to-cooperative-finalization route. This is a scoped
call-path finding, not an assertion about every omitted backend/dependency.
Existing progress/health/error returns do not prove termination signals unwind
Rust objects or settle active effects.

[ResidentRuntime stop/Drop348–420](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_runtime.rs#L348)
retires its connection, kills/reaps only its owned child under a2second cleanup
bound and writes process diagnostics. That is not stock Reader restoration.
[Session/Pending](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/recovery/activation.rs#L27)
retains this runtime and ExitOnDrop. [ExitOnDrop170–200](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/health.rs#L170)
poisons health; it sends no stock-service command. Mere presence of Drop does not
prove those paths run on systemd signal termination.

[Recovery profile validation](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/recovery.rs#L426)
requires verified binary/unit/helper/stock artifacts and a specific firmware/kernel,
Buddy Type=notify, Restart=no, OnSuccess/OnFailure recovery helper and fixed policy.
This differs from the committed manual simple/restart-on-failure unit. The
[activation latch94](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/recovery.rs#L94)
is persistent occupied evidence created per boot; service stop must never remove
it. Failed publication is not permission to stop stock. Manager must not mutate,
replace, retire or reinterpret that latch as a safe-to-stop grant.

[run_installed recovery750](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/recovery.rs#L750)
is a separate explicit installed operation. NoRecordedActivation is a no-op,
not proof of stock readiness. Restored requires original Buddy terminal/group
admission, profile verification, stock state/identity checks and at most one
stock start. A plain inactive Buddy unit does not supply those facts. Stop must
not invoke this recovery command itself, start stock, or claim its receipt.

## Concrete command choice and authorization limits

Reuse the existing native source's fixed [nonblocking fail-on-conflict command
pattern](https://github.com/s116821/ReMarkableBuddies/blob/b008027b378f8f06422c17d5e58ed7bb041e402b/src/workflow/resident_supervisor/service.rs#L376),
substituting only the product's fixed Buddy unit in reviewed source. It enqueues
one stop without replacing a pending job. Zero exit means request accepted, not
stopped process or recovery completed. Local SSH cancellation cannot undo PID1.

The accepted authorization is UNIT-SCOPED: request that this verified fixed unit
stop. Recheck observed invocation/policy drift before submission; no atomic
conditional stop of a historical PID is promised. No bespoke lifecycle lock or
original-process compare-and-stop protocol is part of this change. The exact
closed profile/DTO and existing-versus-unavailable evidence are recorded in
profile-admission.md. It is qualification of supported unit behavior, not a new
remote readiness grant, that governs profile enablement.

## Can useful work proceed?

Yes: after full precode review, strict action/current/history types, unavailable
profile refusal, fixed observation/submission fixtures, real local SSH/channel
limits, maintenance/cancellation/lifetime tests and both host/UI packages can be
implemented independently of live provider or new native experiments. No new
sync/status engine or selected-outbox paths are needed.

No current profile has been qualified for Manager mutation by this assessment.
The two closed candidate layouts and exact private facts are specified. Their
binary/unit/policy/platform tuples still require actual owner qualification; no
currently deployed profile is declared enabled by a source shape match.
Coordinator update at12:57UTC identifies newer unmerged Buddy26f39565/SDKb3a66e3b
with RM2 combined-head notebook-reuse smoke. Repeat packaged automatic creation,
remaining acceptance, simulator and linked delivery remain open. That is attributed
owner status, not a newly verified source packet or ordinary/resident Stop-profile
qualification. The b008027 source baseline here is unchanged; no RM1 safety follows.
Unsupported profiles refuse before submission. This is a real enablement and
actual-target qualification dependency, not a reason to stop protocol/fixture
work under the independently accepted concrete design. No target execution or
production profile enablement is authorized by source assessment alone.
