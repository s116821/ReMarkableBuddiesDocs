# Closed profile admission and private observation

Current source delta: package-record-contract.md supersedes the earlier resident
LEGACY/Profile1/Lease2 shape implemented at Manager c013eb2. The paired successor
implements the accepted private package/companion contract; results.md attributes
its source controls separately from native qualification. Both production
registries stay empty. Ordinary-manual retains its original predicates with the
closed private DTO additions below.

## Meaning and release gate

The action is unit-scoped: request Stop for reader-buddy.service on this verified
connection/boot. Fresh checks reject observed drift; no original-PID CAS, new
lifecycle lock, stock-write authority or native-restoration grant is promised.

There are exactly two candidate profiles below. No profile is production-enabled
by this precode. Enabling either requires independent owner acceptance of the
exact binary/unit/effective-policy/platform tuple and actual shutdown tests across
all running configuration modes that tuple admits. This is a code/release gate,
not a new tablet file, readiness bit, host credential or renderer parameter.
The implementation may build/test the closed sampler, refusal paths, transport,
queue and UI before that gate; it must not publish an unfinished planning-only
feature or advertise qualified Stop while the gate remains open.

A self-reported version, a root-owned file alone, fresh metadata copied into an
expected record, or absent native metadata cannot satisfy binary/profile trust.
No automatic trust enrollment or package repair is introduced. The manual profile
still requires an independently accepted extracted binary binding. Buddy v0.62.0
supplies a released ordinary tarball/source input, not native shutdown
qualification or a signed installed-output package. Development fixtures do not
satisfy production trust or all-mode shutdown qualification.

## Exact common predicate

For either profile, all of the following must hold before submission:

1. Current connection/boot equals the original review. All fixed reads finish
   within the remaining budget and match a second service/process/file bracket.
2. Id and Names identify only reader-buddy.service; LoadState=loaded,
   ActiveState=active, SubState=running, MainPID=ExecMainPID>1, ControlPID=0,
   Job empty, nonempty canonical InvocationID, nonzero canonical start timestamp,
   ControlGroup=/system.slice/reader-buddy.service. Other states may be inspected
   as current OS state, but do not create a stop-ready review in this slice.
3. RefuseManualStop=no, CanStop=yes, NeedDaemonReload=no, User/Group empty or root
   with actual process/file uid=gid=0. No drop-in, wrapper, extra argv, service alias,
   deleted/replaced executable, unsafe ancestor, unexpected hook or pending job.
4. Unit and executable are protected root-owned regular files with no group/world
   write; fixed ancestors are safe, and process executable/argv/start ticks agree
   with the pinned artifact and MainPID. Checks detect sampled drift, not hostile
   root races. Unit bytes and effective policy agree with the selected profile.
5. Exact tuple has passed the release gate above. Every missing/unavailable/
   mismatched condition refuses before host admission. Confirm rechecks the
   original private sample; it never adopts a newly observed profile or process.
   A drift after the final bracket is still within unit-scoped intent, not a
   promise of targeting one historical PID.

## Supported-shape table

| Evidence | ordinary-manual | resident-installed |
| --- | --- | --- |
| Source | Delivered91dcc601 manual unit, unchanged from b008027 | Delivered91dcc601 PACKAGE/Profile6/Lease3 and installed-output activation |
| Unit file | /etc/systemd/system/reader-buddy.service; exact SHA256434d00dc6b62096b782dc85d417338a8283269f913f954af897a85cbc8ba64a6 | /usr/lib/systemd/system/reader-buddy.service; digest matches protected Profile6 and accepted tuple; no shadowing /etc unit |
| Effective base | Type=simple; Restart=on-failure; RestartUSec=5s; WorkingDirectory=/home/root | Type=notify; Restart=no; existing complete20-property buddy_policy must match source-approved protected recovery profile |
| Effective hooks | ExecStop/ExecStopPost/OnSuccess/OnFailure empty; RestartForceExitStatus empty | OnSuccess=OnFailure=reader-buddy-stock-recovery.service; both job modes fail; ExecStop/ExecStopPost empty in this candidate (unknown hooks unsupported) |
| Termination | KillMode=control-group; Delegate=no; KillSignal=15; FinalKillSignal=9; SendSIGKILL=yes; DefaultDependencies=yes; WatchdogUSec=0 | Source requires control-group/no delegation/SendSIGKILL=yes and fixed watchdog2min. Same signal restrictions; other20-policy fields equal the verified recovery profile |
| Timeouts | Finite observed TimeoutStopUSec/TimeoutStartUSec, exact qualified tuple required; no universal default is assumed | Exact existing profile values. Helper TimeoutStartUSec=2min10s; stock TimeoutStopUSec=1min30s. Do not shorten these to the Manager wait |
| Executable and argv | /opt/bin/reader-buddy, regular file (no alias); argv exactly [/opt/bin/reader-buddy]; digest requires independently accepted source/build binding | /home/root/.local/lib/remarkable-buddies/reader-buddy; argv exactly that PACKAGE path; digest equals Profile6 app_sha256 and accepted installed-output tuple |
| Environment declaration | Exactly the committed EnvironmentFiles path /home/root/.config/reader-buddy/environment with ignore-errors=no; no raw values read/exported | Declared environment/working directory/argv must match the pinned unit and qualified tuple; no secret values read/exported |
| Native ownership observations | Any occupied/partial/refused resident latch is a veto. A well-observed missing final component only removes that veto; it does not establish no native activity or grant Stop | Closed Lease3 binds current Buddy identity/context/hashes and original rm-sync ServiceBaseline1; package-record-contract.md defines current companion terminal/group and vendor checks; no absent/partial/foreign fallback |
| Recovery artifacts | Not asserted from the manual unit; no automatic stock recovery claim | Fixed PACKAGE artifacts and all three rm-sync artifacts; helper idle; Profile6 policies, original/current companion policy and both27-key vendor projections match immutable tuple |
| Platform | Exact model/firmware/kernel in qualified ordinary tuple; no RM1/RM2 equivalence inferred | Profile6 firmware3.28.0.172/kernel5.4.70-v1.6.3-rm11x and companion rm2-3.28.0.172-v1 only; model independently qualified |
| Current enablement | Unsupported until trusted binary binding and ordinary interruption/native-safety qualification cover every admitted runtime mode | Unsupported until exact installed-profile/native active cancellation/recovery and source delivery qualification are accepted |

The manual termination values are deliberate candidate restrictions supported by
systemd's property model, not assertions that the unit explicitly sets them or
that a particular tablet uses the defaults. Unknown/unsupported property spellings
refuse. resident-installed is not the development bootstrap. The legacy /opt argv
exception is development-only. Other source-supported LEGACY versions have no
qualified Stop tuple and are excluded from this candidate. The old /usr/bin APK
matches neither row. No translation, alias, copy or version widening is attempted.

## Configuration and mode evidence

Source main559–664 loads Config, checks Reader enablement/selection/startup,
retains ordinary mode lifetime and starts optional sync before the loop. Saved
configuration or Store mode may change after startup. effective-config.json
contains effective source labels, not a complete current runtime-mode receipt.
The recovery profile/LeaseRecord has no effective configuration-mode field;
source_mode selects the native contract, not the running sync/provider mode. PID1 properties and
self-reported binary version do not supply one either.

Stop is therefore explicitly MODE-AGNOSTIC. It reads no credential/environment
contents, opens no Store, and invokes no configuration/mode producer. The exact
private DTO states that effective mode is unverified; it cannot silently infer
ordinary/local-only from absent selection/lease or copy a saved mode into runtime
state. Profile qualification must cover every active configuration/mode the
verified binary/unit can reach, including sync/provider work and pending native
operations. A qualification restricted to local-only cannot enable this action
unless the existing verified startup contract independently excludes other modes;
current saved-file presence is insufficient. Existing saved/mode inspectors remain
separate actions that revoke a ready Stop preview through shared ownership.

## Existing ownership checks: what is and is not transferred

Existing source supplies root-owned/no-follow artifact Pinned checks,
ProcessIdentity PID/start ticks and exact executable/argv hashing, closed service
Snapshot policy comparisons, boot/group-bound immutable LeaseRecord, and native
GroupBaseline namespace/cgroup checks. These are owner mechanisms, not an API
Manager may fabricate or replace. Read-only sampled values in this DTO support
profile matching/drift rejection only. They do not transfer FD-backed native
ownership, prove group emptiness/restoration, or authorize stock commands.

Manager never calls activation, recovery, stock start/stop, development bootstrap,
or a function with side effects to obtain admission. It never removes, rewrites
or acknowledges the occupied boot latch. Missing/unreadable/partial/changed fields
refuse; there is no optimistic absent-native profile. Native owners retain their
existing guards. No new compare-and-stop protocol or custom lock is required by
the accepted unit-scoped action.

## Exact private DTO

All objects are closed. package-record-contract.md defines exact Profile6,
Lease3/nested ServiceBaseline1 and three new private fields. Public caller fields
cannot supply any of these facts.
A private child request is exactly
`{connection_id,boot_id,selector,budget_ms,expected}`: selector review|stop|inspect,
budget integer1..12000; expected null for review/inspect and otherwise exactly
`{profile,sample_sha256}`, where profile ordinary-manual|resident-installed and
the digest binds the host's canonical original private sample. Input cap4KiB.
The child recomputes the fixed observations before Stop; a digest is a drift
fence, not a new readiness credential or authority over an arbitrary unit.
The digest is SHA256 of UTF8 JSON with recursively sorted ASCII object keys,
no whitespace, ordinary JSON escaping, and unchanged array order/string bytes.
Its closed input is `{connection_id,boot_id,profile,buddy,helper,stock,process,
platform,artifacts,recovery_profile_base64,lease_base64,lease_observation,
configuration,companion,companion_group,vendor_policy}` from the accepted review.
No timestamp/status/selector/command/
reason is included. The child re-samples the same facts and compares this digest
before the command. Root/native qualification is independently required; matching
a digest does not enable an unsupported tuple.

The child result is exactly the existing validated
`{contract_version,status,observation,service_stop_raw}` envelope, with
`service_stop_raw` exactly:

```
{
  "selector": "review|stop|inspect",
  "command": "not-submitted|request-accepted|unknown",
  "reason": null,
  "buddy": null,
  "helper": null,
  "stock": null,
  "process": null,
  "platform": null,
  "artifacts": null,
  "recovery_profile_base64": null,
  "lease_base64": null,
  "lease_observation": "not-read|absent-final-component|occupied|refused",
  "configuration": {"read":"not-read","effective_mode":"unverified"},
  "companion": null,
  "companion_group": null,
  "vendor_policy": null
}
```

Strings separated by | denote finite enums, not literal wire values. reason is
null or the public contract's closed reason set. Refusal has command=not-submitted
and unavailable facts null. For Stop, only a complete zero-exit fixed-command
acknowledgment may report request-accepted; every possibly submitted failure is
unknown. review/inspect must be not-submitted. There is no safe_to_stop, admitted,
restored, mode-derived grant, arbitrary diagnostic or claimed native owner field.

Each nonnull buddy/helper/stock/companion is exactly `{state,policy,stop_extra,hooks}`.
private-property-keys.json lists11STATE,20POLICY and10textual Stop extras plus the
two typed hooks defined in contract.md. Textual keys remain required without
aliases/unknowns; each textual value is bounded ASCII without controls/newline,
at most4096bytes. Each raw
fixed show response at most32KiB. Integers retain canonical decimal strings:
PID32bit, timestamp64bit; InvocationID empty only with cleared runtime, otherwise
32lowerhex. Empty Job is required for review/stop. The four unit IDs are fixed;
Only fixed read-only show and typed hook queries may inspect helper/stock/companion. No caller unit or helper mutation.
The configured ExecStart declaration is pinned by exact unit bytes and no drop-ins;
the executing command is checked through exact /proc PID executable and NUL-framed
argv. No new parser guesses systemd's diagnostic ExecStart rendering or treats a
self-reported version as provenance. Effective file/loaded-state/property brackets
remain sampled checks, not a promise against privileged concurrent replacement.

Finite duration syntax must match the reviewed systemd spelling/qualified tuple;
unknown/infinity values refuse except the existing helper's cleared-runtime
watchdog sentinel under the source's exact predicate and pinned zero-watchdog
policy. That exception grants no native authority.

platform is null or exactly `{firmware,kernel}`: bounded ASCII strings (firmware
max128bytes, kernel max256bytes), read only from fixed /etc/os-release and
/proc/sys/kernel/osrelease. Firmware extraction uses the existing source parser
and rejects duplicate/missing/malformed IMG_VERSION. Original bounded file
reads are16KiB/256bytes. Tablet model comes only from the original validated
observation; no model is inferred from these strings. The release tuple must
match that model plus these exact values. Unavailable model/platform refuses.

process is null or exactly `{pid,start_ticks,uid,gid,executable,argv,sha256}`:
canonical decimal strings (PID32bit, others64bit), fixed candidate executable,
exact one-element argv described above,64lowerhex digest. Unexpected argv is
refused before serialization, avoiding secret-bearing arbitrary process args.

artifacts is null or a closed object with exactly these fixed slots:
`buddy_unit,buddy_executable,recovery_profile,native_profile,adapter,helper_unit,
stock_executable,stock_unit,stock_dropin,companion_executable,companion_unit,
companion_dropin`. Each slot is null or exactly
`{device,inode,uid,gid,mode,length,mtime_ns,ctime_ns,sha256}`, numeric facts encoded
as canonical unsigned64decimal strings (mode/uid/gid32bit), nonzero device/inode,
64lowerhex hash. Slot paths are fixed by source/constants, never read from a JSON
field and followed. Canonical executable/adapter bytes are bounded128MiB and all
reads share remaining time; hashing timeout refuses rather than skipping identity.
Profile/lease and unit files are bounded32KiB. Environment declaration is
compared as the exact qualified systemd serialization, never interpreted as shell
syntax; unexpected representation refuses. Environment-file bytes are not read. Parent safety and before/after
identity are validated before emitting any FileEvidence; the object is still
sampled evidence, not a promise against hostile root writers.

recovery_profile_base64/lease_base64 are null or canonical original UTF8 JSON bytes,
max32KiB decoded each. Strict duplicate/unknown field/type/version/identity checks
use exactly the delivered Profile6/Lease3/nested ServiceBaseline1 schemas in
package-record-contract.md, including companion fields. Original outer record
bytes remain unchanged. Only resident observation uses them. Lease absence never
becomes an owner grant. Do not persist or log the
original bytes or private evidence. Release references at invalidation/completion
and clear owned mutable byte buffers where available; immutable strings and
runtime copies have no secure-erasure guarantee.

Raw service responses max32KiB each, discarded stderr8KiB; complete child envelope
cap256KiB remains unchanged. Each serialized private service snapshot and vendor
policy map is bounded16KiB; the two original32KiB records retain base64 overhead,
with the complete envelope cap enforced independently. vendor-policy-keys.json
is separate from the existing11/20/10 textual catalog and two typed hooks.
UTF8/BOM/duplicate/framing/selector/closed-shape/bounds validation
precedes any reduction; refused facts and secrets are never echoed. Public cap
remains8KiB. Ready/stop admission is computed independently by the host from the
facts/table and accepted profile release gate, never from a child readiness flag.


## Typed hook candidate predicate

The authoritative private shape and collection contract is
[contract.md, Typed hook evidence](contract.md#typed-hook-evidence). Every required
service slot must have both positively typed empty hook observations. A well-formed
nonempty or unknown observation is not eligible, including helper/stock/companion.
Both production registries remain empty and actual shutdown/recovery qualification
is unchanged. No formatted-text omission or earlier diagnostic creates a grant.

## Ordinary alias candidate extension

Keep ordinary-manual as the existing profile. A candidate alias layout accepts
only the exact compiled future installation target
/home/root/.local/lib/reader-buddy/ordinary/reader-buddy. This source-only path
does not assert installation or qualify a production tuple. The reviewed
compiled tuple includes ordinary_alias_target with that exact literal.
Development, trial, arbitrary and nested link paths remain ineligible.

The fixed sampler may lstat /opt/bin/reader-buddy under protected parents.
A link requires root uid/gid, mode 0120777, one link, exact literal and byte
length. A single READLINK result is exact ASCII plus LF, capped at 256 bytes.
Bracket the link and its parents around the read and the regular target
artifact. Both chains require real root-owned directories without group or
other write. Compare the same link, target and parent stamps again after
the service/process samples and across the two complete observations.
The target is a root-owned executable regular file admitted by the existing
128 MiB artifact bound. The expected digest is in the candidate tuple.
The process retains the existing exact PID, ticks, invocation and group
checks. argv is exactly [/opt/bin/reader-buddy], while the /proc executable
literal, file metadata, device/inode and hash equal the protected target.

Only the alias variant adds private ordinary_alias evidence with exact keys
device, inode, uid, gid, mode, length, mtime_ns, ctime_ns, links, literal,
link_parents_sha256 and target_parents_sha256. Numeric strings retain the
artifact bounds, links is exactly "1", and each parent digest hashes sorted
compact UTF-8 JSON of the existing ordered path/metadata/link-count bracket.
The private sample digest adds ordinary_alias only if present. Direct and
resident samples preserve their exact shapes and canonical digests. The
parser classifies the alias as ordinary through its explicit validated
evidence. It cannot satisfy resident requirements or admit companion/vendor
evidence. Public DTOs and fixed Stop dispatch do not change.

Keep both production registries empty. Reject wrong literal, wrong argv0,
wrong target or process inode/hash, bad ownership/mode, nested link, changing
link/target/parent metadata, malformed/extra evidence and stale brackets.
Keep the existing direct and resident compatibility vectors and both
actual factory refusal controls. The successful diagnostic trial remains
candidate-specific and does not qualify this persistent alias layout.
