# Selected isolated backup download

This continues the existing [reader](manager-isolated-backup-reader.md) and V1
package contract. Reuse the publisher's content addresses, Buddy's complete
package validator, protected Drive authority, and existing restore/preferences
import. Do not add a second backup format, login store or restore engine.

## Original selection and bounded reconstruction

The private coordinator receives the original host operation/selection, a
callback that revalidates that exact selection, its original invalidation signal,
and the same captured protected read binding. It must not obtain a replacement
grant or advance to a newer marker. Selection expiry, rescan, cancellation,
authority change and disposal invalidate pending reads and staged results. The
first increment finishes within the remaining two-minute selection lifetime;
it creates no extended child lease, retry or automatic resume.

The trusted binding adds only fixed object lookup, exact object metadata and
bounded object streaming. Lookup projects the existing `buddy_isolated`, `kind`,
`root`, `backup` and `sha256` properties in appData. Complete bounded pagination,
reject repeated tokens and ambiguous/missing candidates, and recheck the one
exact candidate's ID, original properties, size, MIME type and non-trashed state
before streaming. No caller-supplied endpoint, path, token or arbitrary request
option enters this interface. Check original authority around every asynchronous
read and while consuming streams, not just when the factory is captured.

Protected record checks must leave cancellation responsive and fit the same
remaining lifetime. Do not launch a synchronous credential-helper process for
each stream chunk. Reuse one bounded read-only guard for the original protected
record digests, with asynchronous checks around reads and accepted chunks,
including admission before stage creation and completion. In-memory generation,
expiry and exact-selection predicates must not repeatedly copy marker bytes.
A file watcher alone does not replace authoritative protected-record checks.
Guard failure invalidates the original capture; it cannot silently restart.

Read and hash `data/backup.json` first. Its inventory extractor is only a bounded
way to discover the ordinary V1 producer's exact content-addressed closure; it
is not another semantic backup validator. Refuse selected/feedback formats,
unexpected fields, configuration snapshots, duplicate object digests, invalid
lengths and oversized collections before admitting object reads. Preserve the
existing 8 MiB data-manifest, 128 KiB preferences, 16 KiB marker, 4,096 manifest/
object-count and 256 MiB per-object limits; ordinary content objects may be empty.

One desktop attempt additionally allows at most 512 MiB of total staged bytes,
64 MiB of metadata responses, and 16,384 binding calls. Count before admission;
one deadline is never renewed by pagination or progress. These are desktop
operational limits, not a new package format. Refuse an oversized inventory
before its content downloads. Check free space before creating staging and
against the known remaining closure before further files, retaining at least
256 MiB free. Missing disk/authority information refuses safely. The stream is
bounded before buffering/writing, hashes the original bytes through EOF, and
refuses short, overlong, substituted or interrupted content.

## Selected download action

Extend the existing closed V1 protocol with
`{version: 1, action: 'download', operation, reference}`. Both opaque values
must match the current selected operation and selection reference. Reserve one
download phase synchronously under that same owner before I/O; reuse its
original capture and the existing status/cancel requests. Reject repeated or
stale starts without obtaining another grant, rereading the marker or replacing
the selection. A missing configured coordinator reports unavailable before
object reads. Scan/select request and response shapes remain unchanged.

Download responses are the separate closed branch
`{version, operation, status, inspection, cleanupPending}`. Only a verified
response carries the existing reduced inspection: original marker digest,
bounded manifest/object/setting counts and `completeMedia`. Other outcomes have
no inspection; terminal results preserve the coordinator's cleanup warning.
The controller compares the reported digest with the original selected revision.
An interruption is incomplete without a verified summary; a valid package that
intentionally omits media is verified with `completeMedia: false`.

Show one explicit "Download and verify" action beside the selected revision,
preserving that selection during progress and showing the specific terminal
result. Reuse the existing controller, polling, original selection deadline and
caller/document checks. Download start does not renew the two-minute lifetime.
Cancel can name the selected operation before start acknowledgement; invalidate
it immediately, await the exact original release and show any uncertain cleanup
result only in that operation's still-current view. Late results and old cancels
cannot replace or affect a successor. Legacy inspection cancellation remains
immediate.

The browser's existing transport deadline can expire before joined retirement
finishes. A lost, rejected or invalid cancellation reply leaves cleanup
unconfirmed in that same current view; it must not imply successful removal.
Preserve caller/document checks after awaiting the result in both hosts.

Keep verified staging private under the original selection until the existing
one-shot trusted handoff, expiry or invalidation retires it. Polls revalidate
ownership without copying marker bytes. Navigation, rescan, authority change,
cancel and disposal release only the exact operation/reference pair. The UI
receives no filesystem path or handoff/restore authority. This source increment
does not register production factories or add an Apply action.

## Host-owned restore preview handoff

Reuse the coordinator's one-shot handoff for the exact verified operation and
reference. A private composition method may pass the original source to the
existing ordinary restore owner and a trusted destination stager. Production
registration remains absent in this source slice; synthetic staging callbacks
exercise the integration without a tablet transfer or a new public request.

Carry the bounded original file inventory and data/preferences commitments from
the successful checked writes. Do not reopen Drive, replace the selection or
introduce another archive parser. The original source deadline and abort signal
cover transfer and Prepare. Capture the intended wired connection and boot;
changed target identity or incomplete destination custody refuses Prepare.

Expose bounded source reading through the existing staging broker and its
original sealed file records. The trusted handoff supplies `readFile(name, write)`
instead of a local staging path and may read only members of its
frozen verified inventory, with exact byte length and SHA-256 checked through
EOF. Use bounded chunks and the original signal/deadline; do not reopen raw
paths outside the broker or introduce another inventory/parser. Refuse a
replaced, linked, changed or additional member, concurrent file access, or use
after handoff retirement. Reader completion or cancellation must join the
actual file access before the existing owner releases staging. This local
source capability does not select a tablet runtime or register a destination
transport. Ending the handoff revokes that reader, joins any admitted read and
refuses success if the recipient left a read in flight. Retained callbacks
cannot read after retirement. The writer callback must honor its abort signal;
a timeout notification alone does not join a callback still using the bytes.

A local SSH child exit or connection loss alone cannot establish remote
Prepare completion. The eventual destination binding must join its actual
reader or retain cleanup uncertainty without deleting the stage. Do not assume
an installed target Python broker or treat an injected peer as wired evidence.

The existing private V1 restore owner must enforce this deletion condition for
both Prepare and Apply before a destination transport is registered. Mark the
exact stage as possibly being read immediately before the original command is
submitted. Clear only that command's reader guard after the existing authenticated
transport returns `reported` and the strict original selector/request parser
accepts its terminal report, before interpreting archive correspondence or the
write outcome. Raw `unavailable` or `unsupported` frames, local child exit,
timeout, cancellation, stale reply suppression, changed identity and malformed
reports do not settle the reader. A command channel can close without a remote
exit-status message even when the SSH connection remains open.

Checked destination release is allowed only if no reader was submitted or all
submitted readers of that stage have this original terminal evidence. Otherwise
withhold release and carry cleanup uncertainty through the existing private
handoff and disposal results. A valid terminal Apply report may still say the
write outcome is unknown; retain its original Status packet independently of
checked stage retirement. A later Status, including desired-generation-observed,
cannot settle an earlier uncertain reader or authorize delayed deletion. Reuse
the existing joined maintenance option through local command and retirement
settlement so external observer cancellation cannot admit a competing owner.
This source gate supplies neither remote cancellation nor residue reclamation;
the future wired adapter still needs its own qualified staging ownership.

The gate is implemented and independently source-reviewed at
[Manager `6e19e5b`](https://github.com/s116821/ReMarkableBuddiesManager/commit/6e19e5b70da08743ff5f363a589904ae3c74c076).
Scoped JavaScript lint, Python parsing and whitespace checks pass. The existing
composition, actual supervisor and authenticated loopback transport fixtures
contain the new cases. The original [hosted run](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43652329222)
failed all five supervisor Apply setups because their copied source preview
excluded configuration while the target and intent still included it. The
two-line fixture-only correction at
[Manager `e71518c`](https://github.com/s116821/ReMarkableBuddiesManager/commit/e71518c8d137352e52aa3124dc7dc350f3dc1d02)
aligns those fields without changing production admission, assertions or timeouts.
Corrected [full hosted CI](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43652739440)
passes Checks, Build and both Windows/Linux Integration jobs. Checks includes all
ten supervisor cases and the authenticated missing-exit-status control; both
Integration jobs pass the retained packaged host modes and native archive
controls. The original failure remains separate. These host and peer results do
not establish wired staging, real remote cancellation or residue recovery.

Transfer and Prepare share one existing maintenance admission. Preserve the
ordinary command's current bounded payload and execution budget. On cancellation
or timeout, join the actual transfer/Prepare work before releasing either stage;
the existing timeout race alone must not grant completion or free inputs that
the trusted callback may still use. Legacy manual behavior remains unchanged.

The trusted destination remains private. Compare the returned Prepare intent's
archive digest with the original data manifest digest before accepting preview.
Publish that preview only after the complete source handoff has passed its final
authority checks; otherwise retire the candidate with any cleanup uncertainty
preserved. A successful ready intent adopts destination custody under its
existing bounded preview lifetime. Explicit Confirm rechecks that exact custody
and target. Cancel, expiry, invalidation and terminal completion retire only that
destination, while uncertain Apply keeps the existing original reconciliation
packet. Status must not reopen the archive or silently dispatch Apply.

The trusted destination callback returns a private canonical root,
`assertOwned` for the captured target and original file inventory, and one
checked `release`. Only a `true` release confirms removal; refusal or failure
retains cleanup uncertainty. Private restore disposal joins outstanding work
and reports unconfirmed release of returned destination handles. The private
handoff result carries source-stage and failed-transfer cleanup uncertainty.
The existing public restore response shape remains unchanged. The lifecycle
bridge's existing helper close and desktop quit paths
share their respective memoized drain and await both ordinary restore owners,
backup composition and active download quarantine. Close admission first and
join all owners even if one fails. Preserve reduced cleanup uncertainty in the
trusted close result and existing shutdown error reporting, without a modal
prompt or a change to the manual restore response. A repeated close/quit does
not start another retirement. The public cloud-to-restore consumer remains
unregistered until its own target and transport acceptance. Source fixtures
hold original restore, backup and active quarantine cleanup across repeated
close, including synchronous and asynchronous failure. The retained packaged
host fixture holds both restore owners across repeated quit; actual execution
and installed qualification remain separate acceptance work.

Preference preview remains a separate explicit action through the existing
portable-configuration owner. Do not start it alongside data preview: their
shared maintenance lane invalidates competing owners. This increment neither
adds a public Apply action nor implements provider registration, tablet transfer
or clean/replacement-target bootstrap.

## Buddy destination staging command

The selected source increment extends the normal Buddy archive command with
`receive-isolated-stage`, `check-isolated-stage` and
`release-isolated-stage`. It uses the existing Rust binary and package validator;
it adds no target Python, daemon, extra executable, persistent operation registry
or second restore engine. Production Manager registration remains a later
qualified adapter step.

Derive the fixed parent
`Config.paths.data.parent()/.remarkable-buddies-restore-stage-v1`
from the existing trusted saved configuration. Its existing data parent must
exist. Accept no input-path or environment override for this stage root. Refuse
overlap in either direction with configured data, cache, credentials, saved
configuration directory and protected/native document roots. Pin each ancestor
with no-follow directory descriptors and recheck its named identity. Create only
the fixed private parent, owned by the effective user with mode 0700 and an
exclusive regular single-link mode-0600 V1 owner marker. A preexisting parent
requires the exact marker and safe ownership/permissions; never adopt an unmarked
or partly initialized directory. Open no Store, credentials, provider or runtime.

Manager allocates one random V4 stage ID before dispatch and records it with the
original consumed operation, reference, wired connection/boot and archive
commitments. Receive exclusively creates `restore-v1-<stage_id>`; it never resumes
an existing leaf. The literal stdin stream begins with one strict JSON control
line, at most 4 KiB including LF, containing only version, stage_id, boot_id,
marker_sha256, inventory_sha256, object_count, payload_bytes and budget_ms.
Reject duplicate fields and noninteger numeric tokens.

Transmit `data/backup.json`, zero to 4,096 objects sorted by raw SHA-256,
`portable-configuration.json`, then `isolated-backup.json`. Each record is an
unsigned big-endian 64-bit length and 32 raw digest bytes followed by exactly
that many payload bytes. Object filenames derive only from the digest; other
names are fixed. The inventory SHA-256 commits a versioned domain, big-endian
32-bit object count and these ordered 40-byte descriptors. Require distinct
objects, exact count/order, original marker digest and EOF after the final byte.
Bounds remain the existing download limits: 8 MiB manifest, 128 KiB preferences,
16 KiB marker, 256 MiB per object and 512 MiB aggregate payload. Metadata members
are nonempty; objects may be empty. All additions are checked for overflow.
Require a 256 MiB reserve plus remaining declared bytes on the pinned filesystem
before allocation and during bounded 64 KiB writes.

One monotonic receive deadline covers header, payload, validation and settlement.
Its budget is 1 to 12,000 ms and cannot exceed the original host remainder.
The real Linux stdin path uses deadline-aware polling; a plain blocking generic
Read implementation is not evidence of deadline enforcement. Check the same
deadline around disk and validator operations. Kernel I/O can outlive a userspace
deadline; local process termination never proves remote completion. Other archive
operations retain their 16 KiB input/output limits. Check/release inputs and all
reports remain within those limits.

Sync and verify the complete closed package with the existing isolated V1 oracle,
then return a small receipt containing the original stage ID, boot, marker and
inventory commitments, canonical root and custody SHA-256. The custody domain
binds length-prefixed names, fixed-width stat values, parent/stage/child-directory
device/inode and owner/mode, and every exact member's device/inode, size,
owner/mode, link count, mtime and ctime. Reopen and verify the original fixed
parent and entire closed tree before check or release; retain descriptor custody
and recheck identities during deletion. Do not replace this with path-recursive
removal. A matched stage ID alone never grants deletion.

An ordinary receive failure before handing off a receipt must attempt bounded
cleanup of only the directories/files created and still owned by that attempt,
using retained descriptors and exact membership. Refuse deletion on replacement,
unexpected membership, expired cleanup bound or uncertain ownership, and retain
cleanup uncertainty. Do not deliberately retain reproducible partial uploads
after a cleanly observed failure. Lost acknowledgement or abrupt process death
may leave the exact original ID unresolved; the host preserves that bounded
operation-specific warning, without scanning, adoption, reconnect or auto-retry.
A future Manager adapter must propagate even pre-receipt failure into sticky
shutdown cleanup reporting. Checked destination release after receipt adoption
remains subject to the existing Prepare/Apply terminal-reader guard.

First implementation scope is the archive dispatcher, a private Linux staging
module and focused tests, with only the real stdin dispatch adjustment needed for
deadline enforcement. Unsupported hosts refuse without filesystem mutation.
Hosted tests use actual isolated-producer packages for receive, check and release,
framing/integrity/refusal cases, parent and member replacement, links/extra
membership, reserve, deadlines and partial cleanup. Real CLI coverage verifies
literal stdin, EOF and silent/stalled pipes. Fixtures remain modeled filesystem
and process evidence; installed selector availability, actual tablet parent/mount
layout, free space and wired throughput must be qualified before registration.

### Manager streaming adapter

The next source increment connects the existing private `stageDestination`
injection to these three commands. Keep it unregistered in production until
installed qualification. Add `host/isolated-stage-transport.mjs` and the fixed
`host/isolated_stage_transport.py` helper; use the existing observer child slot,
ordinary restore owner, sealed download reader and staging broker. Packaging
already copies the host tree and its sibling imports. No renderer command,
general command runner, dependency, workflow or new test lane is needed.

Before dispatch, validate and freeze the complete selected inventory, source
operation/reference, target connection/boot and one random V4 stage ID. Compute
the existing V1 inventory digest from metadata, order the fixed manifest, sorted
objects, preferences and marker, and stream their descriptors and bodies through
the sealed `readFile` callback. Keep one at-most-64-KiB write outstanding and await
pipe backpressure; do not buffer the package or expose a source path. Retain the
existing small JSON/Base64 protocol for other maintenance commands.

The stage operation uses `WiredObserver`'s original active child and generation.
Cancellation fences and kills only that captured child. Its slot stays occupied
until both child close and the writer settle. A generic successor may cancel the
stage but must join it and recheck its generation before spawning; a stale caller
cannot cancel or replace a newer child. The ordinary joined `MaintenanceIO` token
owns receive, check and Prepare. Supply optional trusted read bounds to the
sealed reader and broker: intersect original source and restore signals and
remaining deadlines for authority, open, read and close. An unconfirmed bounded
close stops and joins that original broker and retains cleanup uncertainty.
Neither close nor failure cleanup replenishes the original attempt's budget.

Use one fixed `READY\n` prefix and a bounded 24,576-byte control line on the local
pipe. The helper anchors its monotonic clock before emitting readiness; Node
then samples its remaining allowance, and the helper clamps it against that
earlier anchor. A startup watchdog also bounds a missing control line. Recompute
Buddy's at-most-12,000-ms budget immediately before forwarding its header. Node
still rejects replies outside its own original cutoff. Check and release carry
only the original bounded receipt, encoded canonically in the control line.

Reuse existing Linux/Windows wired observation and host-key authentication. The
helper admits only the three literal archive selectors with the existing fixed
Buddy executable and configuration. Mark possible dispatch before SSH command
submission; a lost child reply is conservatively possibly dispatched. Pump stdin
and drain SSH stdout/stderr concurrently, checking declared lengths, EOF and
deadlines. Require exact remote exit zero, complete terminal stream draining,
one strict UTF-8 JSON line within 16 KiB and unchanged original final observation.
Bound and discard diagnostics at 8 KiB. The local terminal envelope is limited
to 24,576 bytes in addition to readiness; never forward raw errors or package
bytes as diagnostics. An authenticated early refusal may stop the upload writer;
successful receive additionally requires the complete joined writer and EOF.

Reduce only the published version, selector, status/incomplete pair and
settlement. Receive `sealed` may adopt the matching original receipt;
`no-output` or `cleaned` may settle that failed receive without cleanup pending.
Ambiguous or `unconfirmed` receive preserves a sticky warning and one bounded
private record of the original stage ID, source and target commitments, with no
payload retention. Only `verified` confirms a check and only `released` confirms
release, each matching the saved receipt exactly. A later refusal cannot clear
an already adopted receipt or earlier uncertainty. No rescan, reconnect, stage
lookup, inferred adoption or retry follows ambiguity.

The host-only stage handle exposes its canonical returned root to Ordinary
Restore for `root/data`, together with bounded `assertOwned` and one-shot cached
`release`; none of these reach the renderer. Preserve the existing
Prepare/Apply reader-completion guard. Cleanup inside an active joined attempt
uses its live token and remaining cutoff. Expiry, drop or disposal outside it
may take one new bounded nonwaiting joined lease for that original receipt only
when the owner slot is idle and the target remains current. A competing owner,
unresolved reader or exhausted active attempt retains uncertainty; cleanup must
not cancel somebody else's child or renew an expired attempt.

Extend the existing composition, supervised-child and authenticated SSH peer
tests with retained producer bytes. Cover complete receive/check/Prepare and
explicit Confirm/release, true early refusal, partial/stalled writes, missing or
malformed replies, deadlines, cancellation, child/writer joining, target drift,
competing ownership and sticky pre-receipt warnings. Existing Node/Python CI
discovers these tests. Peer evidence, actual Buddy CLI evidence and physical
tablet qualification remain separate.

### Buddy source checkpoint

Buddy `dfd5d09ad6cdc3d9b3e2b0a3d868cd6841bdd23e` implements the
three fixed archive selectors and has passed independent source review. Receive
cleanup keeps the original deadline; an expired or changed stage remains
unconfirmed. The normal CLI tests include a complete receive/check/release path
using 1,659 bytes of retained synthetic output from the existing isolated-package
producer, with raw-byte Git attributes and exact file hash assertions. Scoped
formatting and whitespace checks passed. Original
[hosted Checks](https://github.com/s116821/ReMarkableBuddies/actions/runs/43655946337/job/132634406000)
passes with 1,317 library tests and 15 literal-stdin CLI cases, including all five
new stage-engine groups, the producer round trip and bounded silent/stalled pipe
controls. The same [full run](https://github.com/s116821/ReMarkableBuddies/actions/runs/43655946337)
also passes Build and Integration using the unchanged retained packages for
armv7 and aarch64 under emulation. This is not native/tablet qualification. The
Manager adapter, installed selectors and target qualification retain their
separate gates.

### Pre-receipt cleanup warning checkpoint

Manager `1f925377598f0e084f071c2a51db5ed9e1f216cd` retains an
exactly-true destination transfer cleanup warning in the ordinary owner's
existing sticky disposal result, even when no stage handle was returned. The
immediate handoff warning and joined source retirement remain unchanged.
Independent source review accepts the narrow correction and composed cases for
true/false/nonboolean flags and disposal joining a held failing transfer.
Node syntax, scoped lint and whitespace passed.
[Hosted Checks](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43654958927/job/132631379222)
passed with 1,310 Node passes, zero failures or cancellations and five skips,
including the new warning cases and retained remote-reader controls. The
authenticated SSH channel-close test and separate 14 archive checks also passed.
Build and native Integration remain pending. No actual tablet upload or cleanup
is established by these synthetic-peer and host-owner results.

### Manager adapter source checkpoint

Manager `7ce12a03595d435f485d9a32fb5b4726f57cf12d` implements
the private adapter described above and passes independent source review, scoped
JavaScript syntax/lint, Python parsing and whitespace checks. Authored coverage
includes retained producer bytes through the real supervised child pipe and
Prepare/Confirm/release, held writers and successors, bounded source-reader
cancellation, and authenticated SSH terminal and failure controls. The local
fixture child models the Python helper; the SSH cases separately exercise its
actual execute boundary. The original [hosted Checks](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43659100364/job/132644256568)
records 1,327 Node passes and five skips; the authenticated selector positives
pass. The missing-EOF fixture refuses before dispatch under its one-second
allowance. Reviewed fixture-only `f0fdbc3bdf65e8fcedf17830ed70f9fc62d5a084`
uses the existing eight-second test allowance and additionally requires complete
input EOF, sent terminal status and an actual timeout while output EOF remains
withheld. Production code and its deadline are unchanged. Corrected hosted
validation is pending in [the successor run](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43659688652);
the original failure remains separate. The adapter remains unregistered; these
results do not establish installed selectors, real provider composition or
physical target throughput and cleanup.

## Private preview of verified backup preferences

This source increment connects one deliberate preferences-only action to the
portable member of an already verified isolated V1 backup. The accepted
ordinary data handoff and its destination stager stay separate. Choose one
consumer for the exact verified operation and reference. The same one-shot
handoff cannot issue both previews. A later choice needs its own fresh verified
selection; a retained callback, path or result cannot reopen the old stage.

### Existing owners and admission

Add a host-only `preparePreferences(operation, reference, {portable, target})`
to `host/isolated-backup-composition.mjs`. Reuse the same exact-pair preflight
and one-shot consumer used by `prepareRestore`. Check closing, coordinator
availability and portable owner support first. Call the existing portable
owner through a private `prepareHandoff(target, handoff)` method. Reserve that owner's existing
`MaintenanceIO` token before calling `takeVerifiedHandoff`. Even when the
preflight passes, recheck and consume the exact verified pair only inside
that admitted call. A Busy, absent/unsupported owner or changed target before
consumption leaves the verified selection available. The chosen preferences
action may start only after the competing data action has settled or been
declined. Keep the existing peer invalidation of stale previews and protect
against an active data restore with the same shared token. Capture the exact
wired connection/boot from `observer.lastObservation` and bind it to the
original portable owner, live observer and epoch throughout the operation.

Keep the selected operation and reference in the composition closure.
Hand only the existing verified source reader to the private portable entry.
Use `files` and `components.preferences` to require one member named
`portable-configuration.json`, with exactly the original byte count and
SHA-256. Check a positive declared length up to 128 KiB before allocating
one private buffer of that size. Read only that member with the existing
`readFile(name, write)` callback. Refuse excess before copying a chunk and
require exact total length and raw SHA-256 at EOF. The broker continues to
validate the full original inventory, sealed-file identity and source
authority. Parse only the completed buffer using `portableArtifactBytes`.
The raw member digest proves byte identity and the existing canonical
artifact digest binds the portable Prepare result. Keep both comparisons.
Do not send a staging path, source bytes or provider identity to a renderer.

In `host/portable-configuration.mjs`, factor the current
`#read` Inspect and Prepare portion into an internal function that returns
a private candidate. Keep construction of the reduced result and adoption
into `#editor` separate. Manual import decodes its existing input and adopts
the candidate as it does today. The new entry supplies its own validated
artifact and uses the existing `#raw` selectors, `parsePortableReport`,
bounded JSON inputs, original intent and Apply-packet hashes, and
`parsePortableResult` with the same Prepare result context. Do not call
public `request` or acquire a second token from inside the handoff. A typed
Inspect or Prepare refusal stays a normal reduced refusal. A verified
no-change has no editable reference, Apply packet or retained operation. Only a valid prepared candidate can become the existing ready editor.
Its normal preview lifetime starts at final adoption. Confirm and Status
remain the existing explicit operations with their own current target checks
and original uncertainty handling. The handoff never calls Apply.

### Cancellation and publication

Use the joined branch of `OrdinaryRestoreHost.#owned` as the ownership
pattern. Keep one active private Prepare invocation on the portable owner
with its exact token, epoch, abort controller, completion promise and
original deadline. Capture its deadline at initial lane admission. Shorten
it once from the source handoff's remaining timeout. Since the coordinator
rounds that value up, use at most `timeoutMs - 1` milliseconds from callback
entry and refuse an exhausted remainder. Use the earlier cutoff for reading, Inspect,
Prepare and final adoption, including after cleanup. Preserve the existing
portable command and request size/time caps. Check the exact active
invocation, token, epoch, signal, target and deadline before and after
awaited work and before each command. A late Inspect must never start
Prepare. A late Prepare must never install an editor.

Current `PortableConfigurationHost.invalidate` releases `#active.token`.
Give the joined private invocation an abort-only invalidation branch that
advances the epoch and keeps its active token and buffers until the
original work settles. Cancel the original observer child if that
invocation is currently inside `observer.run`. Await its actual promise,
which the existing observer settles on child close or launch failure. Use
the original source and invocation signals for member reads and command
dispatch, with an already-aborted check and an abort listener scoped only
to the currently running child. To interrupt a held broker read, bind the
invocation's abort to cancellation of the exact consumed source through
the existing coordinator `release(operation, reference)`. Trigger it
without awaiting it from inside the handoff callback because release
joins that callback. Join the source handoff and any triggered release
from the outer owner. An abort before consumption cannot release an
unconsumed selection. A timeout, cancel or disposal requests the same
abort. None releases the token, returns early via a timeout race,
zeroes buffers still in use, or lets another owner start on that token.
This join establishes completion of host-owned work. Remote data-archive
reader completion remains a distinct wired restore requirement.

The current common observer wrapper must also respect the joined token.
Both hosts route external observation, cancellation and several legacy
commands through `MemoryForgetHost.wrap()`. It invalidates peers and then
calls `MaintenanceIO.revoke()` before running the wrapped command. Today that
would clear even an active private preview's token and permit another
owner to use the shared observer. Add a joined acquisition option to
`MaintenanceIO` for private Prepare. Keep its exact owner until the
invocation's final release, and make `revoke()` return false while such a
token is held and true on normal revocation. Only the joined private
preferences Prepare requests this option. The existing ordinary restore and
all ordinary tokens retain their current behavior.
After the existing peer invalidation requests abort, the wrapper must
honor revocation refusal and avoid calling the raw observer for external
commands while the joined token is held. Return the existing canceled
result for wrapped `cancel`; it acknowledges the cancellation request,
while the original private invocation and its disposal promise still join
the actual drain. Refuse other methods immediately with a
bounded host error. The existing Electron IPC path can reject that call.
Add a catch to the browser helper's generic observation route and return
a fixed 409 refusal. Its other observer routes already catch errors.
Do not queue a refused external command for later dispatch. The private
portable owner uses the raw observer, and its abort listener cancels
only during the original call while its token still owns the lane.

Hold the private candidate until the handoff has completed final source
validation, joined the reader and returned from its checked stage
retirement. The coordinator aborts its source signal as part of normal
retirement. After the callback finishes, use the handoff's final
`handed-off` status for source disposition, together with the portable
invocation's still-current epoch, token, target and deadline. Never
interpret the normal retirement signal as an independent cancellation or
treat callback success alone as admission. If stage cleanup is uncertain,
return `cleanupPending` in the private result and withhold the preview.
Keep the original cleanup result on the existing backup owner. Refusal,
source loss, timeout or late output withholds the preview and discards the
candidate without retry or replacement selection. Wipe owned raw artifact,
command, report and abandoned candidate buffers at their last use. After
ready adoption, retain only the existing bounded original report and Apply
packet needed by Confirm/Status. Clear parsed artifact references once used.
No new operation ledger or private artifact cache is needed.

Make portable `dispose()` close admission, invalidate the active operation,
and return one memoized drain promise. The drain awaits the joined private
invocation and its source release, then clears retained buffers. The
invocation's finalizer releases its exact token once after all joins and
buffer disposal are complete. The manual cancellation and request shapes
stay unchanged. The private cancel path uses the same joined drain.
Current browser-helper close and Electron quit already await returned
`portable.dispose()` and backup composition disposal in their memoized
shutdown. The backup owner already reports source cleanup uncertainty
there. Reuse those shutdown lists and existing transports. The browser
helper change is limited to handling observation refusal while the joined
owner drains.

### Scope and hosted fixture

Use `host/isolated-backup-composition.mjs` and
`host/portable-configuration.mjs` for the private join. Also scope the
ownership and refusal changes to `host/maintenance-io.mjs`,
`host/memory-forget.mjs` and the generic observation catch in
`host/browser-helper.mjs`. Extend `tests/isolated-backup-composition.test.mjs`
through the current staged
selection fixture with the actual portable owner on its shared maintenance
lane and a scripted wired observer. Verify exact member/hash/count and
existing V1 Inspect/Prepare input and reduced output. Check a mismatched
target and Busy before consumption, missing/corrupt member and unsupported
selector, verified no-change with no Confirm reference, and ready with
zero Apply before explicit Confirm. Confirm must use only the original
prepared packet. Keep the existing manual import/export and original-only
Status coverage.

Hold a broker read or an original Inspect/Prepare promise through cancel,
deadline or repeated disposal. Assert another owner stays Busy until the
original work and stage retirement finish, retirement runs once and the
late response cannot publish a preview or start a successor command. Hold
stage retirement after successful Prepare to check that neither ready nor
no-change is published early. Check target/source invalidation and a
failed release with preserved cleanup uncertainty and no ready result.
Exercise the real wrapped observer while the joined token is held.
Its external cancellation must abort the original invocation without
releasing the lane, and another wrapped command must refuse without
invoking the raw observer. After the original drain, a fresh action can
acquire the lane. Retain the existing ordinary-token revocation control.
Use the existing hosted composition suite with synthetic provider and
wired responses. Product registration, live namespace and installed/wired
restore qualification remain under their existing tasks.

### Source checkpoint

The six-file Manager implementation at
`26877e8808861046b7378038aa304b8c636495fb` has passed independent source review
and scoped syntax/whitespace checks. The existing composition suite has 14
authored subcases in three groups, including short, excess and wrong member
readback, original Confirm, held reads/commands and uncertain retirement.
Full hosted run `43634084071` passed: Checks includes all 14 authored subcases
within 1,274 Node passes, zero failures and five skips; Build and both native
Integration jobs also passed. The existing source/package browser and Electron
flows use synthetic provider and target responses. Retained native commands
passed their archive and actual-producer package checks; this does not qualify
the later UI consumer, real Drive or installed/wired behavior.
Cleanup uncertainty is returned privately
and remains retrievable through the backup owner's original cancellation
result; this does not claim automatic refresh of the ordinary status view.

## Manager preferences preview from a verified backup

The browser and Electron use the same explicit **Review backup preferences**
action after the selected download reports verified and the destination is
admitted for portable preferences. The action hands the
original staged portable member to the existing portable editor. The existing
Confirm button owns Apply and the existing retained Status owns reconciliation.
The one-shot handoff precludes using the same stage for data preview. A separate
data operation needs a fresh verified selection.

### Closed bridge and target admission

Add a separate V1 branch to the existing isolated-backup bridge, with the
following exact keys.

```text
{version: 1, action: 'preview-preferences', operation, reference, connection_id, boot_id}
{version: 1, operation, reference, status, retryable, preview, cleanupPending}
```

Use the existing 512-byte request cap and strict parsing. Validate both backup
IDs and the portable connection ID as the existing lowercase 64-hex handles,
and the boot ID with the existing portable UUID predicate. Keep the bridge
parser and result branch separate from the ordinary scan/select/download/status/
cancel contracts consumed by `IsolatedBackupHost.request`. Cap the nested
portable response at its existing 8 KiB and the full preview frame at 9 KiB.
Require the reply to echo both original backup IDs. Allow `ready`, `no-change`,
`busy`, `invalidated`, `capacity`, `unsupported`, `not-dispatched` and
`unavailable`. Only `ready` and `no-change` carry a preview. Parse it with
`parsePortableResult` using `{action: 'prepare', connection_id, boot_id}` and the
existing observation validator, and require the inner state to match the outer
state. Ready carries the portable editor reference and reduced summary.
No-change carries no editor reference. Failures carry null preview. Cleanup
uncertainty also requires a failure status, null preview and `retryable: false`. `retryable` is true only for Busy with the same source still
available for handoff, checked after the refusal. A portable command can report
Busy after consumption, which yields Busy with `retryable: false`. No request
carries an artifact, path, source-device substitution, grant or Apply intent.

Dispatch through the same `POST /manager-isolated-backup` guard and Electron
`manager:isolated-backup` channel with the existing sandboxed preload's
single-argument allowlist. Preserve the browser's loopback Host, exact Origin,
session cookie, content type, body limit and document checks before and after
the await. Electron rechecks the trusted window, main frame, exact UI URL,
arity and original document after the await. Capture the connection and boot
from the raw wired observer's current valid sample at admission and require
them to match the requested values. Apply the same observed-model, firmware
and architecture admission criteria as the saved-configuration probe. The
request is a comparison to that sample. The archived device and the wired
destination can differ. Use the same portable owner that handles the existing
route or IPC. It checks the original target during Prepare and Confirm.

### One original attempt and joined cancellation

Create one small host attempt owner per companion instance in
`host/isolated-backup-preferences.mjs`. The adapters pass their captured
document, target reader and lifecycle predicate into this owner. The slot
holds the original document and pair, captured target, abort controller,
completion and issued Ready object. Reserve it synchronously. A second
request while it is occupied returns Busy with `retryable: false`. Keep caller/document currentness distinct from whether an individual
response is still writable. It uses `canHandoff` only
before consumption and when classifying a Busy refusal. Add a host-only
`selectionSignal(operation, reference)` to `IsolatedBackupHost` backed by the
reader's original selection controller. Return only the signal for a current
exact pair, without copying marker bytes. Selection expiry, cancellation,
reselection and authority invalidation already abort that controller. Read
its signal through a host-only reader accessor that uses the existing
selection currentness check. Watch that signal until attempt retirement.
Check the exact selection again at final delivery and before Confirm using
`isSelectionCurrent`. The attempt holds no handles into the retired stage.

Pass the host-only `{signal, current, releaseAttempt}` options through
composition `preparePreferences` to `portable.prepareHandoff` alongside its
existing inputs. Refuse an already-aborted signal before taking the lane.
Attach a one-shot listener to abort only that joined invocation. Check it
through final adoption, including while source retirement settles. Remove the listener when the
invocation drains. Continue to join the exact consumed source release and
original observer child before releasing the maintenance token. The normal
coordinator retirement also aborts its broker signal, so only the original
attempt and selection signals stay authoritative for cancellation at final
adoption. For an exact backup Cancel, capture the slot, abort its controller
synchronously, and join its completion and the existing backup cancellation
from outside the private handoff. Repeated cancellation joins the same drain.
Return the existing bounded cancellation result with the original cleanup
warning preserved. Unmatched cancels keep their current backup behavior.

Keep the original issued Ready object host-side through publication. Check
caller, target, selection and `portable.assertCurrent` in a shared final
publication method immediately before returning the IPC reply or ending the
HTTP response. If validation or delivery fails, cancel that exact attempt.
Add `discardHandoffPreview(issued)` as a host-only method on the portable
owner. It uses the existing issued-result WeakMap and a handoff flag on the
editor context. In one synchronous check require the exact issued Ready,
current epoch, same editor object, still-ready state, no possible Apply and
no active command for that editor. Clear only that editor and its timer,
wipe its buffers, mark it invalidated and call its `releaseAttempt` hook.
Return false for a successor, a manual editor, an expired or replaced
result, or an editor with possible Apply. Use this scoped method for backup
discard because public portable Cancel can interrupt active Apply. The guard uses the actual issued object,
never just the string reference or a renderer-supplied result.

Store `current` and `releaseAttempt` only on the backup editor context. Existing
Confirm checks `current()` at admission and immediately before it marks the
reference possibly dispatched. The predicate checks the exact attempt,
original document, selection and target. A failed check refuses dispatch and
retires only that still-unapplied editor. Recheck the editor identity when
the predicate itself invalidates the selection. After recording the
possible-Apply receipt and before starting the raw command, call
`releaseAttempt`. It synchronously detaches the source listener and clears
only the captured attempt slot, without cancelling or performing I/O. Use
the same hook when expiry, peer invalidation or editor replacement drops an
adopted backup editor. Once Confirm records possible Apply, source
cancellation leaves the existing Apply and original Status ownership in place. The backup attempt owner
stores no reconciliation packet. Once dispatch can have occurred, the UI's
backup Stop/clear only releases the backup selection and leaves the portable
controller's original-reference retention intact.

Route ordinary backup actions through the existing backup owner. Accepted
scan or selection replacement invalidates the old exact pair. Release the
attempt slot and remove its listener on terminal refusal, no-change, discard,
expiry or possible Apply. A callback from a prior attempt can release only
what it captured. Old backup Cancel can discard only the matching attempt
for its admitted document and operation.
Use the existing navigation and shutdown hooks to invalidate the matching
attempt, and Electron's renderer-loss event to do the same. The existing
wrapped observation cancellation also invalidates the portable owner. When
that peer teardown drops a backup editor, release only the matching attempt
through `releaseAttempt`. Drive authority replacement aborts the original
selection. On HTTP response close before finish, cancel the attempt captured
by that response. Remove that transport listener on normal finish. On a rejected, timed-out or invalid browser response or IPC promise
the controller cancels the original operation and retires its view. If a
cancellation reply is lost, report cleanup unconfirmed for that view.
Delivered responses remain subject to Ready expiry and invalidation. Close
admission before shutdown and join any pending attempt alongside the existing
portable and backup drains. Preserve the existing cleanup reporting.

### Shared UI and hosted evidence

The backup controller captures its private operation, selected reference,
verified download result, deadline and view generation before yielding.
Associate the portable controller's pending or Ready view with that attempt. Use
the existing local-only `ConnectionController.pauseObservation()` to drain
queued observations, then recheck that same selection, target and both
controller generations. Keep wrapped observer Cancel for deliberate
disconnect and teardown. Keep the original selection deadline and block
parallel or automatic starts. Surface a Busy retry only when the matching
reply explicitly permits it. A new click remains subject to the original
selection and portable guards. After consumption or ambiguous delivery, another
preview requires a fresh verified selection.

Adopt the closed result through the existing portable controller's common
validated result and expiry handling. Show the selected backup as the source
and direct the operator to the existing preferences panel.
Expire the view at the earlier of the existing selection deadline and the
normal portable Ready timer. The host checks its own deadlines.
Expose Confirm only for the same still-current target and Ready reference.
Both Stop buttons use the same backup operation while this preview is pending
or still ready. Clear, Stop, rescan, reselection, Drive changes, target
changes, visibility or navigation, expiry and disposal fence both views and
cancel the exact preview
while it is pending or still ready. Fence cancellation and cleanup warnings by
the initiating generation. Once Confirm can have dispatched, releasing the
backup view preserves the existing portable original and Status UI. Retain
manual file import/export and the shared preference editor as existing flows.

Implementation scope is `host/isolated-backup-protocol.mjs` and `.d.mts`,
`host/isolated-backup-preferences.mjs`, `host/isolated-backup-host.mjs`,
`host/isolated-backup-reader.mjs`, `host/isolated-backup-composition.mjs`,
`host/portable-configuration.mjs`, `host/browser-helper.mjs`,
`electron/main.cjs`, `src/host.ts`, `src/isolated-backup.ts`,
`src/portable-configuration.ts`, `src/app.ts` and `src/app.html`.
The preload capability and the observation controller's pause API already exist.

Extend `tests/isolated-backup-composition.test.mjs` for cancellation while stage
release is held, exact Ready discard and possible Apply/Status preservation.
Extend `tests/isolated-backup-helper.test.mjs` for closed frames, original
origin/document/target, lost response, checked cleanup and stale successor
controls. Extend `tests/isolated-backup-controller.test.mjs` and
`tests/portable-configuration-controller.test.mjs` for verified-only action,
local pause, both generation fences, Busy before and after consumption,
ready/no-change, one explicit Confirm, original Status and late failure
recovery. Include a late Ready discarded after a manual or backup successor,
and one discarded after dispatch where Status still settles the original.

Extend `tests/isolated-backup-hosts.mjs` in the existing hosted Integration jobs.
Use the existing helper injection for a positive browser case. Extract the
current Electron backup and portable IPC registrations into
`registerIsolatedBackupHandler` and `registerPortableConfigurationHandler`
in the shared host module, used from production main and a test-only main at
`tests/fixtures/isolated-backup-preferences-electron.cjs`. Launch the source
fixture with its real `ipcMain`, sandboxed preload, built Angular UI and the
same exported main-frame/URL guard used by production. Register the real
navigation and renderer-loss invalidation hook in this fixture. Provide a
process-local composition created with the real factory and synthetic store,
binding, stage/verifier and wired peer, using shared test inputs in
`tests/fixtures/isolated-backup-preferences.mjs`. The fixture supplies
dependencies to the actual registrations, and the renderer drives the
existing preload and both real IPC handlers. Browser uses the same fixture
composition with its real loopback transport. Check changed and no-change,
zero Apply before Confirm, and exact original reference once Confirm runs.
Verify default refusal separately using the existing packaged Electron and
packaged browser-helper launches. Assert the unavailable preview and zero
portable commands. The existing packaged Drive stub can exercise browsing and
still leaves the coordinator absent. Keep the existing manual control in
`tests/portable-configuration-hosts.mjs`. The tests establish source consumer
behavior with synthetic peers. Shipped startup still supplies neither a
production namespace factory nor a staging parent, and actual provider and
installed/wired qualification remain open.

### Consumer source checkpoint

Manager `c8694e56b8fe9979c37a28dabf7163b9ddab3729` implements this consumer and
has passed independent source review, scoped syntax/lint and whitespace checks.
Both host adapters use the same attempt owner. A terminal non-retryable refusal
after admission or an abandoned HTTP preview response triggers joined retirement
of the original selection, with unconfirmed cleanup preserved. Still-ready
discard is scoped to its issued editor. Confirm releases backup cancellation
after recording possible
Apply, preserving the original Status record. The synchronous HTTP write-error
cleanup branch is source-reviewed.

The first hosted Node run passed 1,284 cases, failed one new controller
expectation about post-Confirm cancellation, and skipped five; Build and
Integration did not run. The original failure remains in run `43638535370`.
The fixture-only correction at `c6ad0ce8ee4092bcaeec6b7c26705d2a21e146dd`
requires no extra backup cancellation after possible Apply and explicitly
preserves the unknown result, original Status and one Apply. Its hosted
Checks in run `43638985009` passed 1,285 Node cases with zero failures and
five skips, including the controller, composed owner and loopback cases.
The separate 14 archive checks passed as well.

That run compiled the native commands, then failed production UI generation:
the initial bundle measured 722.77 kB against the existing 720 kB error budget.
Build failed and native Integration was skipped. The authored source
browser/Electron positive fixture and packaged default refusal did not run
in that revision. The original bundle-budget failure remains separate from
the earlier controller expectation failure. The test-owned provider, staging, verifier
and wired peer do not establish real Drive or installed qualification.

Manager `deae2f150dee56b51053c416003082eba4f2e1a6` factors repeated App
controller-reset sequences into three private synchronous helpers, preserving
the original calls and order. Independent source review confirms the expanded
TypeScript syntax tree matches the preceding revision. Its original hosted
Build passed, measuring 718.95 kB against the unchanged 720 kB error budget.
The existing 400 kB warning and test coverage are unchanged. Checks passed
1,285 Node cases with zero failures and five skips, plus all 14 separate archive
checks. [Full hosted CI](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43643656430)
passed both native Integration jobs. The actual loopback browser and source
Electron fixtures verify the preview, explicit one-Apply and no-change paths
with test-owned provider, staging, verifier and wired peers. Both packaged
host modes retain unavailable-preview refusal without a portable command.
The retained native archive and actual-producer package checks also passed,
with original command, harness, provenance and ZIP bytes preserved.
Production factories remain absent. The preceding private-handoff run belongs
to `26877e8808861046b7378038aa304b8c636495fb`, not this consumer revision.

## Owned private staging

Use one exclusively created private directory under the host's designated
canonical staging parent, outside credential, Store, checkout and user-document
roots. Reuse existing protected filesystem and stream/identity utilities where
appropriate; Windows privacy requires the existing protected ACL checks, not
POSIX mode bits alone. A trusted constructor may inject a qualified staging
factory for fixtures; absent/unqualified staging or verifier support reports
unavailable before provider download, with no renderer-controlled filesystem.

Create only `data/backup.json`, `data/objects/<sha256>`,
`portable-configuration.json` and the exact retained `isolated-backup.json`.
Use exclusive file creation, safe canonical membership and original file/directory
identity checks. Write the outer marker last. No unknown file may appear in the
completed package. A valid hash inventory alone is not a verified package.

Cancellation stops and joins reads and the verifier before teardown. Delete only
this attempt's identity-verified owned files/directories. If identity changed or
cleanup failed, preserve the unknown residue and report that condition; never
scavenge other attempts or follow replacement paths. Successful staging has one
explicit owner and remains usable only while the original selection is current.
It is released after its handoff, expiry, cancellation or disposal, not retained
as an indefinite cache. Public output has no credentials, provider IDs, staging
paths, raw settings or personal content.

If a staging child fails after creation but before returning custody, report
uncertain cleanup even though the coordinator has no stage object. A joined
process exit alone is not proof of rollback; retain the warning unless explicit
owned cleanup succeeded. Do not retry deletion or adopt a new process's residue.

## Reuse the complete Buddy oracle

Expose `Store::inspect_isolated_package(root, Some(original_marker_sha256))`
through the existing bounded offline archive command family as
`--archive-operation inspect-isolated --archive-input -`. Its closed input is
`{"path":"<absolute package directory>","marker_sha256":"<original sha256>"}`.
Reuse the existing input/output byte caps, strict JSON and redacted failures.
No Store creation, mode switch, credentials, provider call, tablet API, restore
or runtime activation is permitted. Existing archive command inputs and output
shapes remain unchanged. The new operation's successful data contains only
`isolated_package`, the existing redacted `PackageInspection`; errors expose no
raw paths or settings. A failed check cannot issue a success receipt.

The Manager's trusted verifier seam consumes that original package root/digest,
honors cancellation/deadline and checks exact bounded output and verifier
provenance. No available trusted verifier means unavailable, not verified. A
fixture-injected verifier must be labeled synthetic until exercised against a
retained real producer package and this actual Buddy command. This increment
does not claim that existing Windows/Linux Manager distributions already ship
a compatible host Buddy executable; host packaging/runner qualification remains
an explicit delivery task, or verification occurs in a separately qualified
target path before restore. Do not add an unreviewed download/execute helper.

A successful run of the full existing oracle for the original marker can yield
a private verified stage handoff. Declared media omissions retain the oracle's
`complete_media=false` and `incomplete=true`; verified package structure never
means all media is present or that a restore has been applied. The later wired
transfer must preserve and recheck that same
closure/digest before feeding its `data/` child to existing ordinary Prepare.
Portable preferences use the existing explicit import and separate confirmation.
Clean/replacement target admission and actual provider namespace visibility
remain their existing separate obligations. No reconstruction result applies
data or grants native authority.

## Implementation and verification

### Host oracle delivery decision

Use the existing normal `reader-buddy` command as a pinned, offline host
dependency of Manager. Its Windows x64 and Linux x64 builds belong inside
Manager's existing private host resources, not Buddy's tablet release asset
inventory. Do not add another binary target, parser, backup format, release
channel or runtime download-and-execute path.

The dependency source is reviewed Buddy commit
`95b75443629ea455f9b92af7ce48dc0902a42994`, tree
`16e5a83296ceb70d0a3867098a149e04af03eae9`, with Cargo.lock SHA-256
`dd6ddeeb756da0a93c8e3d7020d2f7e92ba68026a1492d2312da1ad94b2472d1`
over the exact Git blob bytes, independent of checkout line-ending conversion.
This is a development dependency pin, not a published Buddy release or a new
application version. Use Buddy's existing Git-derived identity without Manager
version substitution. A later pin change requires review and fresh applicable
qualification; it must not silently follow a branch or a latest release.

This pin includes the reviewed test-only retained-command selector. Copy the
ordinary executable before compiling tests, bind its exact canonical path, size
and SHA-256 through the all-or-none `READER_BUDDY_ARCHIVE_TEST_COMMAND`,
`READER_BUDDY_ARCHIVE_TEST_BYTES` and `READER_BUDDY_ARCHIVE_TEST_SHA256` variables,
and recheck those same retained bytes after the tests. This avoids accidentally
qualifying a replacement binary compiled with test-only dependency features.
The Windows path uses Rust's canonical verbatim form. The selector's local
Cargo-built test proves the harness only; native retained-release results remain
required. Production code, Cargo.lock and the SDK revision are unchanged by this
test-only successor. Its negative dot-path fixture constructs the spelling as raw
OS text: Windows verbatim path joining would otherwise normalize away the very
component the fixture is intended to reject.

The initial, temporary qualification path builds the dependency within the two
existing platform Integration jobs on PRs. It does not rebuild retained Manager
ZIPs or enable a release path. The final shipping path below replaces that
temporary compilation; qualification artifacts alone are not installed dependencies.

Keep the pin in one Manager host-owned source record. CI checks out that exact
Buddy source separately, builds `--locked --release --bin reader-buddy` with
default features and no native experiment flags for each supported host, and tests
the normal archive command on the native platform. Reuse maintained checkout/toolchain/artifact
actions and put orchestration in the existing workflow. Record source/tree,
lockfile, resolved SDK revision, target, toolchain, feature/profile settings,
Git-derived identity, executable size/hash and matching notices with the
retained artifact. Source and native platform claims remain distinct.

Only the matching qualified executable and bounded provenance enter
`host/buddy-oracle/` in Manager's private resources. Preserve its Linux execute
bit through ZIP assembly. Verify the embedded source/target/hash and original
Manager package digests without executing downloaded ZIP contents. Keep the
existing three Manager ZIP names and size limits; measure before proposing any
limit change. Source-tree helper mode and browser use must resolve the same
qualified installed host dependency through the existing local helper contract.
A static browser ZIP alone does not supply a native verifier.

### Shipping build and native qualification

The final shipping path compiles both dependencies in Manager's existing Build
job. Use Ubuntu 22.04 as the initial tested Linux baseline, Rust 1.98.1 and the
normal default-feature release command. Cross-compile Windows x64 with maintained
cargo-xwin 0.23.1, LLVM/clang-cl 22.1.8, signed Jammy NASM 2.15.05-1, desktop SDK
10.0.26100 and CRT selector 14.44.17.14. Record the actual resolved SDK/CRT inputs
and compiler versions. These selectors and the initial runner are qualification
inputs, not a claim of immutable upstream catalogs or universal Linux support.
The maintained resolver prefers a separately published Universal CRT package
when present. Guard its actual package/version and notice basis independently;
the SDK selector and installed directory do not identify that UCRT input.
The current source candidate records UniversalCRT package 10.0.26624.1, which
Microsoft identifies with the legacy Windows SDK 10.0.10240 family. Retain that
family's original SDK EULA and third-party notice RTFs separately from the newer
SDK files. The publisher archive's original setup layout contains EULA MSI
10.0.26624; its read-only File/Media tables identify the two notice members in
the matching cabinet. Record that association and the publisher's separate
static-library redistribution reference in the origin index. Passing a build
alone does not establish runtime compatibility or notice completeness.

Prime a fresh cargo-xwin cache with maintained xwin 0.10.0: list using VS17,
then download using that same cached channel and identical architecture,
variant, SDK and CRT selectors. Retain the actual channel/package files,
downloaded payload hashes and matching publisher package identities outside
the managed cache before cargo-xwin's normal first splat. Set its outer setup
retry count to zero so failure cannot discard that snapshot and fetch a new
one. Do not fabricate a DONE marker or implement a second package resolver.
The original metadata and inventory stay in the existing CI-only receipt;
SDK archives and a duplicate ordinary executable do not ship in that receipt.

Keep Windows CRT linkage static and AWS-LC bundled-source/static with assembly
enabled and prebuilt NASM fallback disabled. Remove global Rust flag overrides
before applying target-specific flags. Preserve the locked dependency graph,
original source identity and normal features. Use pinned maintained setup actions
and workflow orchestration; do not add a custom SDK downloader, new release asset
or executable target. Record native PE imports, ELF dependencies/symbol versions
and matching license/third-party notices. A working compiler alone does not
establish runtime compatibility or notice completeness.

Copy the reviewed Microsoft SDK and historical UCRT SDK RTF files, BuildTools third-party text and
matching VS2022 terms document byte-for-byte with a compact origin index.
Use standard archive extraction, bounded downloads and exact input/member
hashes. Recheck those notice inputs when the resolved SDK/CRT packages change.
Do not concatenate binary RTF/DOCX into a text notice or substitute installed
Community-edition files for the verified BuildTools payload.

Copy and hash each normal executable before compiling `archive_cli --no-run`.
Use Cargo's root-artifact and build-script JSON records for the original
`READER_BUDDY_VERSION`; do not run Windows code on Linux, substitute Manager's
version or duplicate Buddy's version algorithm. Retain the test executables and
build receipts as CI-only inputs outside the three release ZIPs. Both native
Integration jobs execute those tests against the same oracle bytes extracted
from their retained Manager package, using the existing all-or-none selector.
The pinned Linux test also reads two scenario files beneath its compile-time
`CARGO_MANIFEST_DIR`. Retain their original source bytes and digests, verify that
the recorded path is the exact assigned checkout path, and restore only those
two fixtures there before testing. Refuse a changed path or fixture; do not omit
the test or silently substitute a different source tree.

Compare actual native `--version`, original provenance and command hashes, then
recheck the command and ZIPs after testing. Do not rebuild or repack in Integration.

Preserve the five existing PR jobs, required status contexts and common-check
placement. The Linux Integration runner uses the initial Build baseline even if
its status-context label is retained for repository compatibility. Keep generated
targets on disposable hosted runners, check free space before compiling, and
retain only the bounded original inputs needed for qualification and delivery.

Generate target/default-feature third-party notice JSON with maintained
cargo-about, locked dependencies and failure on unresolved licenses. Keep its
root-package handling explicit: the pinned generator includes Buddy even though
its manifest lacks license metadata. Bind a root-only `LicenseRef-Buddy-Repository`
clarification to the original LICENSE checksum without choosing a GPL version
qualifier. Carry the exact root LICENSE and THIRD_PARTY_NOTICES separately as
the authoritative Buddy notice artifacts; the generator's dependency JSON does
not replace them. Include
the locked foreign SDK and its notices, all runtime transitive dependencies and
matching Rust standard-library and native-library notices. Do not blanket-ignore
unpublished foreign dependencies. Cargo's graph does not account for statically
linked Microsoft CRT/UCRT objects; retain their resolved input and notice basis
separately before distribution.

When original Build inputs are supplied, compare the exact notice inventory and
bytes in each native ZIP with those inputs through the existing bounded ZIP
reader. An updated outer package digest does not excuse a missing, changed or
additional notice. Preserve the generated dependency report and vendor texts
without rewriting them into a custom license format.

### Package readback and compatibility

Extend the existing bounded Manager ZIP observer for embedded dependency checks;
do not extract or execute an archive, add an asset, or introduce a second ZIP
parser. Native ZIPs that carry an oracle contain exactly its platform executable
and provenance in `resources/host/buddy-oracle/`, plus the adjacent host-owned
source record. Require that record and provenance to agree, validate the existing
runtime schema and platform, and stream the declared executable to verify its
exact size, CRC and SHA-256. Preserve current archive, metadata and time limits.
Require regular 0755 for the Linux command and regular 0644 for the Windows
command and JSON. Refuse partial pairs, extra members and target-platform aliases
or collisions into these fixed resources. The static browser ZIP has no oracle.

Runtime download verification checks the downloaded release's own internally
consistent pin, not the currently installed Manager's older pin. Both native
ZIPs must agree on their source record. Existing annotated-tag, completion-record
and asset-digest checks bind the candidate bytes; embedded metadata alone is not
independent build provenance or update authorization. Keep the existing fixed
quarantine response and its lack of installation eligibility.

The runtime compatibility boundary is Manager **1.0.0**: earlier versions may
omit both native oracles, but any present oracle must be complete and both native
ZIPs must carry it. At and after 1.0.0, both are required. The adjacent source
record is not a rollout marker because pre-oracle packages already contain it.
This feature boundary does not create a tag, change version authority, or remove
the existing premature-1.0 release hold.

Shipping CI is stricter at every candidate version: before upload it requires
both native oracles, compares their source to the exact candidate checkout pin,
and checks each against the original retained executable/provenance supplied by
Build. Reuse the bounded observation core for candidate readback and publication.
Runtime verification of a future release must still accept a different valid
embedded pin. Neither a trusted CI expectation nor an executable path may come
from the renderer or downloaded package.

### Installed host verifier

Provide an explicit value-free `--browser-helper` mode in the existing packaged
Manager executable. It starts the existing fixed-loopback helper with browser UI
assets from `app.getAppPath()/dist/manager/browser`, before creating a desktop
window or registering desktop IPC. Host modules and native resources still come
from the same installed external resources used by normal Electron mode; only
static UI reads use ASAR. Do not add an executable, release asset, chosen port or
path, or runtime code download. Source-only browser helper mode does not acquire
installed-dependency authority from a lookalike directory.

Normal explicit launches open only the helper's own returned loopback preview
URL in the user's browser and expose that URL for attached terminals. A trusted
host test seam may suppress external-browser launch without granting any path,
credential or verifier choice. Startup failures produce no success URL and must
not fall through to desktop startup. Normal desktop behavior remains intact.
Windowless Linux use still needs the supported Electron desktop environment;
it does not imply display-server-free operation.

Use one idempotent awaited shutdown on signals and explicit quit. Stop admitting
HTTP requests, invalidate pending owners, close the helper and finish owned
cleanup before ordinary process exit. When the download coordinator is later
composed, shutdown must await its existing child join and checked stage disposal.
Browser page-close signaling is best effort and does not replace host expiry or
authority checks. Forced process termination cannot prove cleanup or authorize
scavenging. Extend the existing packaged host tests to launch this actual mode
and verify its ASAR UI, loopback/session checks, lack of desktop windows, ordinary
shutdown and truthful unconfigured/unqualified results. The launch mode alone
does not activate backup download, restore or the installed oracle factory.

Both entry points use one shared host-private composition with one protected
Drive store, one auth owner, one inspection/selection owner and at most one
download coordinator. Reuse the store's trusted interpreter and exclude its
protected root from the explicit staging parent. Resolve only the fixed
`hostRoot/buddy-oracle` resource and its adjacent installed source pin. Keep
source-helper and injected-auth fixture behavior without creating a second auth
owner. The composition's host-only `downloadSelection` obtains the original
capture from `captureDownload(operation, reference)` itself; callers cannot
supply a replacement binding, grant, marker or staging path.

Memoize one disposal promise and close admission synchronously. Abort the
existing owners before awaiting their original work, including cancelled
inspection predecessors, pending protected guard opens/closes, active provider
streams and verifier execution. Release owned staging only after those users
have joined, retaining the existing cleanup-uncertainty result. HTTP close stops
admission before draining; desktop window close and explicit quit use that same
drain. Fixtures prove these lifecycle properties without registering a real
read factory or adding a public download action. Production source continues to
omit read-factory/staging registration until the installed-host and namespace
qualification above is accepted.

The verifier adapter is disabled by default. Its trusted host constructor may
select the resource directory and expected dependency pin; a renderer, user
setting, provider object or staged package may not select an executable. Before
and after each invocation, validate the original canonical regular executable,
its expected size/hash/target/source and bounded metadata. Refuse missing,
changed, unqualified or mismatched inputs. Never search PATH, install, recapture,
refresh, or fall back to a tablet binary.

On Windows, acquire a narrow resource lock helper before the first Node resource
capture, including availability checks. Use the existing trusted host Python and
pywin32 boundary. The helper accepts only the trusted canonical local resource
root and derives the two fixed file names; it never receives a command, arguments
or backup input. Reuse the existing handle checks through a small shared primitive
without changing staging or Drive behavior. Reject every reparse component,
alternate stream, alias, nonlocal path and nonsingle-link leaf. Hold a
share-accounted handle on each ancestor without delete sharing, and hold each
leaf with generic read access and read sharing only. Compare held and path file
identities before readiness and final confirmation. Directory share modes alone
do not protect arbitrary children.

Node retains the original fixed launch and all provenance, membership and hash
checks. Monitor the helper throughout the same bounded operation. Stop and join
the Buddy child before releasing helper handles on failure, cancellation or
timeout; after success, finish the original checks while handles remain held,
then release and join the helper before accepting output. Missing or lost guard
custody refuses success. A helper crash immediately invalidates the attempt and
aborts/joins Buddy; it does not provide handle retention across that crash.

This requires a trusted interpreter, helper/imports, OS loader, stable local
volume mapping and installed directory, including ancestor delete-child, ACL,
metadata and reparse mutation rights. Only trusted host/installer principals may
alter them. It is not a sandbox against a same-principal attacker or an untrusted
writable installation. Qualify actual Windows loader/read compatibility, denied
leaf write/replacement and ancestor rename, leaf/ancestor reparse refusal, guard
loss, and handle release after success/cancel/timeout before enabling the factory.

Run only `--archive-operation inspect-isolated --archive-input -`, with the
original root/digest on bounded stdin, shell disabled, hidden Windows console,
a private working directory and a minimal environment without credentials,
configuration or loader overrides. Bound stdout to the existing 16 KiB report,
refuse stderr and nonzero/ambiguous exit, honor the original remaining deadline
and cancellation, and join the child before settling or releasing staging.
Process fixtures may test these mechanics but are not Rust-oracle evidence.
The coordinator continues to validate exact report semantics and original
selection authority; the runner must not become another package parser.

Before wiring download, independently verify native Windows compilation and
normal command behavior, the supported Linux runtime baseline, actual retained
package bytes/modes and both browser-helper and Electron paths. Exercise the
runner against an actual isolated-producer package as well as malformed output,
wrong dependency, cancellation and timeout controls. Keep platform and provider
qualification incomplete until their own evidence exists.

Retain small synthetic complete and media-omitted packages emitted by the actual
crate-private isolated exporter for the cross-repository runner controls. Record
the producer source, exact file inventory/digests, expected redacted report and
reproduction command with those fixtures. A test-only opt-in emission path may
reuse the existing producer fixture; do not expose a production export API or
manually recreate its outer marker. Treat these as synthetic producer evidence,
separate from live provider publication and native restore. Tests using a retained
oracle must keep its original executable bytes and source attribution explicit.

Native owns the private Manager coordinator, staging/read-guard adapters and
their focused offline fixtures. Root owns protected-host integration, UI,
independent staging/verifier qualification, Docs, CI and delivery. SCRAPPY owns
the narrow Buddy oracle command and actual-producer
command tests, using the existing relevant source branch/cache. Review this
contract before coding; report contradictions without widening other scopes.

Test complete healthy closure, zero-byte objects, incomplete/duplicate lookup,
wrong size/hash/EOF, changed authority/selection during a read, original expiry,
disk/aggregate/call exhaustion, unavailable or failed verifier, exact redacted
success, and cleanup refusal after identity replacement. Exercise the real
Buddy oracle with an actual exported ordinary isolated package, corruption,
extra membership and wrong-marker refusal. No local app build or new Cargo
cache is required; keep platform/runtime/source evidence distinct.
