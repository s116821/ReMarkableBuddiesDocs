# Shared basic-settings consumer contract (proposed; implementation pending)

This completes the existing active companion design, preserving its original two
requirements/four scenarios. Producer wire remains the immutable accepted
[contract82717f](https://github.com/s116821/ReMarkableBuddiesDocs/blob/82717f481005bfd403ec35c149dfbbf28805d156/openspec/changes/edit-saved-basic-settings/contract.md).
Actual producer c50eb6b3 is published as v0.20.0; its completed execution/publication
is not replayed here. Managerf43627ba/Docs5f2e7175 delivered saved-configuration
inspection and are this consumer's actual baselines. This is concrete precode,
not an implemented API or successful mutation claim.

## Public boundary
One optional ManagerHost.basicSettings(request), authenticated same-origin POST
/manager-basic-settings, exact-arity authorized main-frame IPC manager:basicSettings.
Use existing identity validators and fixed lowercase64hex opaque references.
Strict request object <=1024UTF8bytes; no recursive duplicates/extras/invalidUTF8,
arbitrary CLI selector, config path, hash, operation UUID or private report.

- begin: {action:'begin',connection_id,boot_id} creates one fresh editor context.
- save: {action:'save',connection_id,boot_id,reference,changes} claims that context.
- status: {action:'status',connection_id,boot_id,reference} reads original intent.
- cancel: {action:'cancel',reference} stops local work without claiming rollback.
- retained: {action:'retained'} reads only bounded host memory, never tablet I/O.

The retained action is a concrete proposed consumer decision: it lets reload recover opaque
unknown references without a new producer inspection or automatic status operation.
It returns at most8 original safe target/boot identities and opaque references;
private packet/hashes/UUID are never exposed. It is not an apply/status capability
on another target, and current verified target binding is required before remote I/O.
No localStorage/file persistence; restarting the helper loses recovery guarantees.

Exact outer {contract_version:1,status:OBSERVATION_STATUS,observation:SAMPLE|null,
basic_settings:VIEW}. VIEW is strict with state/reference/current/report/retained.
State enumerates none/ready/invalidated/unsupported/unavailable/
busy/capacity/not-dispatched/no-change/verified/unknown/unresolved/
desired-file-observed. current is exact BASIC_FIELDS or null, never raw Config.
report is null or reduced {operation,status,outcome,disk_readback_verified,
runtime_activation}; deny all private data/hash fields. retained is an array<=8 of
{reference,connection_id,boot_id,state} for unresolved originals only. Current host
view/ref and original diagnostic refs cannot be silently confused or reassigned.
The retained array has0..8 exact records, each state unknown|unresolved only,
unique references and original validated identities. All other states are never
listed as unresolved. Host-local retained returns state none/reference/current/
report null, observation null and outer unconfigured without tablet I/O.

Ready requires its reference and exact3current fields plus inspect/ok/read-only
report. No-change requires exact3current and prepare/ok/no-change, no private intent.
Verified requires exact3current and apply/ok/verified, true readback/restart-required.
Desired-file-observed requires exact3current and status/ok/desired-file-observed,
false readback/unverified. Unresolved may show exact3currently observed fields with
status/ok/unresolved; it never makes its spent original reference editable. Unknown
has original reference, null current and no false verified/readback. Invalidated,
capacity and unavailable have no ready authority. Progress is local controller state,
not a remotely reported inspecting/saving result. Original nonready references in
terminal responses do not grant another Save. A status result for an older reference
cannot replace a later editor context or settle its pending call.

Only current identity-verified wire results carry outer observed/sample; host-local
retained/cancel or refusal may use existing unconfigured/null observation form.
The reduced parser validates each state/report/current/reference combination;
no permissive arbitrary report forwarding. All public output <=8192UTF8bytes, bounded before parsing; hashes discarded except
in private contexts. Only verified apply may expose true readback/restart-required.
Desired-file observation remains false/unverified, not historical/runtime success.

## Fields and UI patch
BASIC_FIELDS is exactly trigger_corner/log_level/debug_dump, each exact
{origin:default|declared|declared-null,value}. Declared trigger is UR|UL|LR|LL;
declared log is off|error|warn|info|debug|trace; declared debug is boolean. Default/
declared-null values are null, never guessed effective defaults. CHANGES contains
one..three exact supported keys: {action:'set',value:NONNULL_TYPED_VALUE} or
{action:'clear'} only, no extras; absent keys unchanged, empty object refused.

Three controls only trigger_corner/log_level/debug_dump. Current exact values and
origins are always displayed. Each control offers No saved override and supported
explicit values; keep a dirty-field set. Begin populates controls without dirtiness.
An explicit Remove saved override control handles declared-null even when its
select already shows No saved override. Save sends only dirty fields: set(nonnull typed value) or clear. Omitted/null current
both select No saved override while preserving their different origin labels until
an explicit edit. No-op user gesture with zero dirty fields disables Save; producer
no-change still preserves original bytes. No freeform JSON/model/path/credential.

Begin pauses polling through existing queued ConnectionController.pause BEFORE
creating the editor reference. Save does not pause again and invalidate its own
reference; polling stays paused. Explicit later tablet read/refresh invalidates ready
context even with unchanged IDs. One Save means internal prepare plus at most one
apply, not two confirmations. Pending text never claims premature success; Cancel
has phase-correct not-dispatched/unknown meanings. After verified save show saved
state with restart-required, without restart/service/provider buttons. Uncertain
originals get explicit Check desired file; no auto check/retry or rollback claim.

## Private custody and atomic claim
Host keeps raw original inspection base/path hashes and exact3fields privately.
General configuration view cannot authorize edits. Begin invalidates previous ready
context before I/O; late inspection completion cannot recreate it. Save checks same
original reference, target/boot, generation and monotonic120000ms ready lifetime before an atomic
same-host claim; double/concurrent Save cannot reenter or reuse a spent reference.

Generate original operation UUID privately and send exact original inspected hashes
and dirty patch to prepare. Validate complete prepare response against requested
operation/hash/patch and original before/after fields; target hash must be valid
and differ from original base. Producer owns full-file deterministic serialization;
the host cannot recompute that hash from a three-field projection. Apply/status
reports must link to the exact retained target hash. Retain
original exact private report and serialized {intent}, plus integrity digests,
BEFORE possible apply dispatch. Apply uses those bytes only, at most once. Expiry,
cancel, capacity or target change before dispatch is not-dispatched; after dispatch
may have occurred retain original unknown packet, never update conditions/reprepare.
Check generation/target after every await and again in the final HTTP/IPC projection.
A ready reference expires at120000ms from successful inspection using monotonic
host time; validate before claim and before public release. A status read never
extends that lifetime or upgrades an old/spent reference. Cancellation while Begin
has no published reference uses the existing global queued cancel/invalidation;
a late inspection cannot recreate ready authority.

One Save has one global existing13s coordinator budget for prepare+apply, preserving
existing2/8/12/13/14s hierarchy; not13s twice. Pass remaining bounded budget to each
lower phase. No apply begins after budget expiry; after possible dispatch expiry is
unknown. Prepare alone remains no-write and cannot be represented as a saved result.

At most one active editor/preparing/apply slot; at most8 unresolved originals across
targets. Reserve capacity before a new potentially mutating Save. Do not evict an
unresolved packet to admit a new Save. A fresh explicit Begin may inspect current
state while preserving old diagnostics; if all8slots occupied refuse Save before
prepare/dispatch and explain capacity. Capacity refusal retires that ready grant without remote I/O;
a later explicit Begin is required, never an automatic reattempt. Keep per-invocation results separate from
older original states. A later refused status invocation leaves original unknown;
matching exact target yields desired-file-observed only, other valid bytes unresolved.
Terminal verified/no-change/not-dispatched records may retire; unresolved cannot.
No automatic replay/retry or guarantees across helper/process restart. A cancel
for an old/nonactive reference must not cancel a newer active operation; return
its retained unknown state without invoking observer.cancel for unrelated work.

## Bidirectional invalidation and unchanged observer receiver
Construct editor and existing MemoryForgetHost around the SAME original observer.
Public maintenance wrapper invalidates ready editor + ready forget before external
I/O, preserving both possible-dispatch originals. Extend direct forget prepare,
confirm/receipt and OWNED cancel entrypoints too; nonowning retained-reference
cancel is host-local and bypasses the external-I/O hook. merely adding editor methods to forget's
external-method set is insufficient in the reverse direction. Host-only status/
retained snapshots do not perform external maintenance or invalidate a new editor.

Editor Begin/Save/status before-I/O invalidate ready forget but never settle unknown
forget. Editor's own internal raw prepare/apply cancellation must not be mistaken
for a second external invalidation: raw observer receiver stays original. Wrapped
observe/inspect/runtime/personalization/query/config/mode/run/navigation/cancel
external paths clear ready editor and generation before I/O. Explicit raw run paths
used by direct forget also invoke the shared external hook before their own claim.
Main-document reload/navigation invalidates ready/pending reads; resources/iframes/
same-document paths do not. Cancel queues serialize before later reads. Generation
changes after possible apply retain original packet even if the UI drops late result.

## Validation and attributed evidence
Strict private parser must validate all producer operations/status/outcome/readback/
activation/data combinations and hash linkage; pure reduced parser denies private
report, duplicate/unknown keys and shape/type/origin inconsistencies. Fixed trusted
wired Python transport supports inspect(no stdin), prepare/apply/status(bounded stdin)
only. Fixed remote command prefix is /usr/bin/env -i HOME=/home/root
PATH=/opt/bin:/usr/bin:/bin REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json
/opt/bin/reader-buddy --basic-settings-operation OP. OP is chosen internally:
inspect for Begin, prepare then optional apply for Save, status for explicit original
status. Inspect has no remote stdin/input flag; the other operations append exact
--basic-settings-input - and receive only the bounded private JSON packet through
stdin. No renderer-selected argv/path/environment, fallback or stdout-as-error log.
Caps: config1048576, input/report16384, stderr8192, child envelope24576,
public8192/request1024. Exact original connection/boot before/after every phase.
Old selector/binary unsupported before apply is not-dispatched; after possible apply
any invalid/truncated/nonzero/late output preserves unknown. No file/service fallback.

Use retained original45reports from Buddy61685ea, capture87bc8d4/executableed2f34f,
artifact101745bytes SHA8adbd87c292d886a9aceed52e701cb1941ca8abc8c1671ac187446d32b375b10.
Validate all original bytes/hashes with typed parser/controller and before/after
linkage; label separate before-shape observation honestly, no producer replay.
Add synthetic fault/race/capacity/malformed/late tests separately. Actual protected
HTTP and main-frame IPC paths must cover same-ID refresh, before-I/O direct forget
invalidation, unknown forget preservation, duplicate Save, old versus new refs,
original status refusal, all8slots and response loss. Ordinary dev/retained browser/
Electron on both OSes with390/1280 captures, same fixed trusted guards and deadlines.
No tablet/provider/signing/package-trust/native/runtime or broad project completion.

## Exact private consistency checks
Inspect current is exactly3keys. Each field has origin default|declared|declared-null;
default/declared-null mean null, declared means the supported nonnull typed value.
Prepare before must equal original inspected fields, intent operation/base/path/
changes must equal the private original request, and target must differ from base.
After is derived from original fields plus requested changes: set yields declared
value; clear yields default/null. Unchanged keys and origins stay exact. No-change
returns original fields/base exactly and never creates an intent. The host does not
recompute a full-file target digest from the projection.

Apply verified target/current must equal retained target/after. Status matching
outcome requires observed hash==target and current==prepared after; unresolved
requires a different observed hash and valid current fields. Every failure's null
data/false readback/unverified activation and exact phase outcome must satisfy the
accepted producer table. A refusal from a later status call is invocation evidence
only: original possible publication remains unknown/unresolved. An explicit desired
file match may retire that diagnostic, without claiming historic publisher/runtime.

## Shared I/O ownership and old diagnostic status
The active editor grant and active remote-I/O slot are separate concepts. One
host-private synchronous ownership record identifies the current remote invocation
with a unique token, coordinator lane, original reference and operation. Begin,
whole Save (prepare through apply), editor status, and direct forget prepare/
confirm/receipt participate in this same single I/O slot. Acquisition before any
await either installs that unique token or returns a sanitized busy invocation
without remote I/O, cancellation or changes to the owner/original evidence. No
implicit queue/retry, condition refresh or second slot is introduced. Release in
finally is conditional on the SAME token still owning the slot; an old completion
cannot release a newer owner's work. Existing explicit global refresh/cancel paths
revoke/invalidate owner generations under the current cancellation contract; they
are distinct from cancelling a retained reference that no longer owns I/O.

Editor action=status is remote I/O, unlike editor retained and MemoryForgetHost
status (host-memory snapshots). For an older diagnostic it first validates original
reference/current identity, then acquires the shared I/O slot. If newer Save/Begin/
forget/status owns it, return busy for this invocation, preserving that newer work
and the older unknown record; do not call observer.run/cancel or the cross-operation
invalidation hook. If acquisition succeeds while another editor grant is merely
ready, invalidate that ready grant BEFORE status dispatch, preserving old uncertain
packets. Status uses the original diagnostic packet, never the ready editor's base.
Its response cannot recreate the invalidated grant or replace a newer context.

## Ownership-aware targeted cancellation across both coordinators
Extend MemoryForgetHost.request(cancel), including the existing unconditional raw
observer.cancel path, as well as the new editor cancel. A retained-reference cancel
may call raw observer.cancel only when its coordinator lane AND exact reference
AND active invocation token own the current shared I/O slot. Then invalidate only
that owned operation with correct pre/post-possible-dispatch meaning and retain any
original unknown packet. A cancel for an old/nonowning forget OR basic reference
returns only that record's local invalidated/unknown state; it must neither call
raw observer.cancel nor run the external-I/O invalidation hook against newer work.
Ready cancellation with no owned I/O simply retires that ready grant locally.
Unknown original evidence is not settled or evicted by a nonowning cancel. Merely
adding a shared before-I/O invalidation hook does not satisfy this ownership rule.

Required actual guarded race controls run in BOTH browser HTTP and Electron main-
frame IPC fixtures. First retain an unknown forget, then start a distinct basic Save
and hold its apply transport pending. Send cancel for the OLD forget reference;
assert no observer cancel or newer generation change, release the one new apply and
require its verified result. Unknown forget stays retained; its later explicit
receipt uses byte-identical original input, not the settings packet. This proves
cross-coordinator stale cancellation cannot kill the new owner. Keep actual guards;
only the lower synthetic transport/report is controlled, no tablet execution.

Also exercise old editor status against a newer in-flight Save (busy, no cancel/
replacement, original unknown unchanged), and against an idle ready editor grant
(status acquires the single slot and invalidates ready before I/O, so that old
ready reference cannot Save). Both hosts must preserve original diagnostics,
conditional token release and final generation checks through these races.
