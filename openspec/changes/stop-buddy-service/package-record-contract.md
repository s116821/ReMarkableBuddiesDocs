# Delivered package reconciliation proposal

Status: accepted source delta from precode3f059509 against Manager c013eb2.
The paired successor implements this private contract; exact source/control
evidence is recorded in results.md. Both production qualification registries
remain empty. Earlier results retain their original source/schema scope.
No target observation, execution or qualification follows from this document.

## Source and scope

The source baseline is Buddy merge
`91dcc601154507790254946f8f0f811204a0fd43`, tree-equivalent to tablet-tested
`75f8017fe491da99353cac7b308ad6e96c620c7e`. Relevant files are
`src/workflow/resident_supervisor.rs`, `recovery.rs`,
`recovery/activation.rs`, `service.rs`, `service/baseline.rs` and
`service/vendor.rs`, plus `cicd/deploy/rm2-resident/`. SDK merge
`a0c6480be6785480c2e0da76a3c06697a18efae4` retains the distinction between
logical request cancellation and physical native owner retirement.

There remain two Stop candidate profiles: ordinary-manual and resident-installed.
The latter now proposes only the delivered PACKAGE/Profile6/Lease3 combination.
Do not accept a range of versions or choose paths from observed JSON.
Buddy recovery source also understands LEGACY profiles, including Profile1 with
Lease2, but no production Stop tuple qualifies that installation. Keep it
unsupported in Stop; do not translate records or add a fallback to it. The old
bare `/usr/bin/reader-buddy` APK is also unsupported. Source support, development
qualification and production Stop qualification remain distinct.

Profile6 is accepted by delivered Buddy only with its explicit installed-output
build features and pinned native pair. The ordinary v0.62.0 release provenance
declares no OpenSDK consumption. A common source commit does not make that
tarball interchangeable with the installed-output development binary.

## Fixed package paths and artifacts

| Slot | Fixed path |
| --- | --- |
| buddy_executable | /home/root/.local/lib/remarkable-buddies/reader-buddy |
| recovery_profile | /home/root/.local/lib/remarkable-buddies/resident-recovery.json |
| native_profile | /home/root/.local/lib/remarkable-buddies/resident-profile.json |
| adapter | /home/root/.local/lib/remarkable-buddies/libremarkable-resident.so |
| buddy_unit | /usr/lib/systemd/system/reader-buddy.service |
| helper_unit | /usr/lib/systemd/system/reader-buddy-stock-recovery.service |
| stock_executable | /usr/bin/xochitl |
| stock_unit | /usr/lib/systemd/system/xochitl.service |
| stock_dropin | /usr/lib/systemd/system/xochitl.service.d/xochitl-service-override.conf |
| companion_executable | /usr/bin/rm-sync |
| companion_unit | /usr/lib/systemd/system/rm-sync.service |
| companion_dropin | /usr/lib/systemd/system/rm-sync.service.d/rm-sync-service-override.conf |

All twelve slots use the existing protected regular-file FileEvidence schema and
ancestor/before-after checks. Executables and adapter retain the128MiB limit;
unit/drop-in/profile files retain32KiB. Executable and argv are exactly the
package app path, with no additional argument. Both loaded Buddy/helper fragments
must be the package paths with no drop-ins or shadowing `/etc` Buddy/helper unit.
Check that the fixed LEGACY recovery profile is absent, matching delivered
recovery::profile_path conflict rejection. Allow either the legacy directory's
final component to be absent below verified `/home/root/.local/lib`, or the
recovery file's final component to be absent below a verified protected legacy
directory. Bracket the existing ancestors and exact missing component; permission
errors, symlinks or a different missing ancestor refuse. Do not create the legacy
directory just to establish absence. Do not
copy, link, repair, remove or silently prefer either installation.

Ordinary-manual retains `/opt/bin/reader-buddy`, its exact `/etc` manual unit and
all original restrictions. Its artifacts object also has twelve keys, with only
buddy_unit/buddy_executable nonnull; the three new private fields below are null.
An observed absent activation latch removes a veto and does not prove native
inactivity, effective mode, or an accepted source/build binding.

## Closed Profile6 and Lease3

Profile6 is exactly the existing eight digest arrays
`native_profile_sha256,adapter_sha256,app_sha256,buddy_unit_sha256,
helper_unit_sha256,stock_executable_sha256,stock_unit_sha256,stock_dropin_sha256`,
plus `version,companion,source_mode,firmware,kernel,buddy_policy,helper_policy,
stock_policy`. Version is integer6; companion is `rm2-3.28.0.172-v1`;
source_mode is `resident-installed-output-v1`; firmware/kernel remain exactly
`3.28.0.172`/`5.4.70-v1.6.3-rm11x`. development_output is absent, not null.
Each digest is exactly32 unsigned8bit integers and nonzero; each policy has
exactly the existing20POLICY keys with bounded ASCII values. Each digest and
policy matches protected artifacts and the independently accepted immutable
tuple. The pinned native pair is profile
`f49f297717cc09cf21fad47e52d47a4faad0c84f4fed4f98ca69ddb41b96b146`
and adapter `8fc60498eb404f5a833d4b4ec4c99b76080f146012c76eb1ea7cb55d44b2b62c`.
These source constants do not qualify any observed binary or production release.

Lease3 is exactly the previous Lease2 fields plus required `companion`:
`version,activation,group,buddy_invocation,buddy_start_micros,stock,
profile_sha256,adapter_sha256,recovery_profile_sha256,companion`.
Version is integer3. Preserve every existing boot/group/process/invocation/hash
relationship. Require the Buddy group parent to be the current MainPID/start
ticks, with matching PID1 invocation/start micros. Its current group remains
the original populated group in the same sampled cgroup2 context.

companion is a UTF8 JSON STRING containing ServiceBaseline version1, not an
object, optional hint, path or readiness flag. Decode it independently with
duplicate/unknown-key/type/numeric/UTF8/framing checks. Its exact members are
`version,snapshot,group`; version is integer1. The nested source record limit
is64KiB, additionally constrained by the enclosing32KiB original lease limit.
snapshot is the source newline-framed `key=value` STRING containing exactly
11STATE plus20POLICY unique keys; it is bounded16KiB. Parse the actual source
format; do not treat it as an arbitrary shell/systemd command or generic object.

Original AND current rm-sync WatchdogUSec must equal `0`, independently of any
tuple. This is vendor::OriginalCompanion::load's explicit source invariant;
nonzero values refuse even if an arbitrary proposed tuple agrees with them.
The original snapshot must identify loaded/active/running rm-sync.service,
ControlPID0, empty Job, MainPID=ExecMainPID>1, nonzero start micros and canonical
nonnil InvocationID, with ControlGroup=/system.slice/rm-sync.service. Its group
has exactly `mount_path,unit,context,group,parent`, using the existing closed
GroupBaseline/Identity/ProcessIdentity schemas. The original companion's parent
matches its historical MainPID/start ticks. Its unit is rm-sync.service, mount
path is `/sys/fs/cgroup/unified`, context equals the Buddy lease context and group
identity differs from Buddy's. Preserve all existing device/inode/type/mode,
namespace/mount-record/slice/group and canonical integer restrictions. Do not
require the historical rm-sync PID to be live after takeover.

## Vendor artifacts, policies and sampled terminal evidence

The companion baseline contains no new artifact hashes. Independently pin the
fixed vendor source hashes, also included in the accepted tuple:

- executable `1caf6493cce2132af89a9377679c19005bef1c5b0e658f704f95b4fdbd07138c`
- unit `076675399604b9fdbee7f267900bd4490de88d32ab1cc49a32d8d45a75bcac8f`
- drop-in `4d4345a6299448ade99878ddeeb894dd9a1a90de230bc3371a5e44237da7a795`

Compare the full fixed vendor::policy projections for BOTH xochitl.service and
rm-sync.service, not just the20POLICY subset in Profile/ServiceBaseline. The
separate vendor-policy-keys.json enumerates exactly27 keys and the source values.
These include rm-sync's RestartForceExitStatus=`HUP INT PIPE TERM`,
BusName=`no.remarkable.sync`, Nice=`19`, and BindsTo/PartOf=`xochitl.service`.
Only Requires/Wants/BindsTo/PartOf/Before/After/RestartForceExitStatus use the
source duplicate-free token-set comparison. Other values match exactly. Never
normalize original record/raw bytes used in the digest.

Read-only sampler validation must bracket the original companion cgroup identity
and current rm-sync snapshot using the source baseline::stopped_snapshot rules.
Both service snapshots must agree semantically and have unchanged source policy.
The original InvocationID/ExecMainPID/start micros are either all retained or all
cleared. A different incarnation refuses. MainPID/ControlPID are0 and Job empty;
allowed terminal state is inactive/dead, or retained failed/failed. A populated
group is not terminal. Empty ControlGroup with an extant original group remains
pending even if empty. Cleared identity requires original group absence; a
same-name replacement group or changed context/ancestors refuses. Retained
identity may use EmptyOriginal or OriginalAbsent subject to those source rules.
ENOENT means OriginalAbsent only for the independently bracketed exact final
component below protected original parents, never for an unreadable/replaced
ancestor. Sampled comparisons do not transfer the native owner's open FDs or
grant recovery authority. A pending/unsupported sample refuses this Stop review.

No stock/companion service stop/start, D-Bus request or recovery is sent by Stop.
The vendor artifact/policy/current-companion checks are observational. Stock
readiness and causal restoration remain independent post-experiment evidence.

## Private DTO and tuple delta

Add exactly three nullable private raw fields:

- companion: the existing `{state,policy,stop_extra}` snapshot shape, with its
  fixed Id rm-sync.service. Each section retains its exact catalog. It is a
  current PID1 observation, distinct from the original nested snapshot.
- companion_group: null or one source observation enum
  `populated|empty-original|original-absent`, accepted only after the fixed
  sampler has performed the source identity/context/parent brackets. This is
  sampled state, not a native ownership or safe-to-stop flag.
- vendor_policy: null or exactly `{stock,companion}`, each a closed27-key string
  map from vendor-policy-keys.json, sampled only at the fixed two unit names.

All three are required/nonnull for resident collection and null for ordinary,
inspect and factless refusal. Include all three in the existing canonical sample
digest, retaining original recovery_profile_base64/lease_base64 strings, all
twelve artifact facts and existing evidence/connection/boot/profile fields.
The private request and public DTO/selectors/reasons are unchanged. No renderer
layout, version, path, command, tuple, proof or readiness input is introduced.

The immutable tuple gains exactly companion_policy and vendor_policy, beside
the existing profile/model/platform/artifacts/buddy_policy/buddy_extra/
helper_policy/stock_policy. companion_policy is the full20POLICY original/current
companion projection accepted from source/release evidence; vendor_policy has
the two fixed27-key maps. Both are null for ordinary. artifacts has two trusted
digests for ordinary or all twelve for resident. A tuple is independently
reviewed source/release policy, never constructed from current observations.
No runtime tuple ingestion or registry entry is part of this proposal.

Keep raw show32KiB, private input4KiB, original profile/lease32KiB each,
stderr8KiB, child envelope256KiB and public8KiB limits. Bound each serialized
private service snapshot and each vendor policy map to16KiB so four snapshots,
two vendor maps and base64 records fit the existing envelope with bounded
process/platform/twelve-file metadata. Still enforce the complete256KiB cap;
do not increase it or skip a field on timeout. The nested source snapshot has its
own16KiB limit. All new reads/hash/parse/brackets share the existing remaining
2/8/12/13/14-second ceilings. Unsupported utility/property spelling or deadline
refuses. Raw private records/argv/policies never reach logs or renderer.

## Evidence and next implementation boundary

Preserved R128/R129/R135 receipts support reproducible native inputs,
development-signed package identity and no-request SIGKILL/helper-success
recovery. They do not qualify this fixed Stop/SIGTERM, active modes, a tagged
signed package, or helper-failure/watchdog recovery. The saved timer rollback
depends on vendor readiness/lease retirement; independent helper-failure
recovery remains a separately prepared operator unit. Ordinary released-unit
sampling is also separate and does not block this source reconciliation.

proposed-manager-changes.md maps the bounded files and acceptance controls for
independent review. Manager c013eb2 remains the implementation baseline, with
both qualification registries empty. Do not sync/archive this unfinished change
or relabel earlier fixtures as coverage of this schema.
