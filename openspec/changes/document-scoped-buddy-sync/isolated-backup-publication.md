# Ordinary isolated backup publication

Proposed for review against Buddy `efeb55c` and Docs `597756d2`. The current
isolated branch of `Worker::google` stops before opening Drive. The local V1
package already verifies format-1 history and media plus portable preferences.
Use that package unchanged.

## Smallest connected increment

Launch an upload-only isolated engine through the existing `Worker::launch`
thread, wake, cancel, retry and health writer. Use the existing Drive create,
resumable transfer, generated IDs, private metadata, exact-ID read and streamed
verification. Factor the upload verification and request metadata seam narrowly
from `drive.rs`. The legacy `SyncEngine` receives/imports before publishing and
stores checkpoints and resumable sessions under a different binding policy.
Retain its existing behavior and keep isolated state in the isolated engine.
Selected group slots, catalog, import and activation stay on their existing
paths. The isolated publisher does not receive data or run a restore.

Use the existing `appDataFolder` scope. The device-backup root is an immutable
provider object with verified private metadata for the selected backup UUID,
device identity and grant binding. Its ID is selected explicitly from private
local custody. The ordinary isolated attempt pins a typed verified root along
with Store actor, device, backup UUID, epoch and binding digest. The credentials'
existing collection is part of the account/application grant fingerprint. The
Store allocates the isolated backup UUID separately when entering a mode. Never
use the legacy collection or shared group UUID as the backup namespace. Never
treat a matching account permission ID, display name, mode metadata alone, or
an arbitrary declared remote ID as proof of a root.

Proposed Drive representation within the existing immutable object/manifest
pattern:

- Put objects and markers in app-data and partition them logically by one
  verified root ID and backup UUID. Use private properties with an isolated
  discriminator distinct from the legacy `buddy_protocol`, plus fixed kind
  and content digest. Existing legacy discovery ignores isolated objects.
- Upload immutable archive objects and both package children, keyed by content
  digest under that root. The data archive already supplies the exact bounded
  object inventory. The existing local package marker points to the two
  component hashes/lengths. Reuse those bytes as the final published marker;
  no package bundle, tar format, shared catalog, or new descriptor is needed.
- Private metadata on the final marker includes the immutable predecessor
  marker ID, or its root ID for genesis. Validate property bounds before
  staging, including the provider's combined key/value limit. Match exact
  root, backup, kind, identity, expected properties and content. To locate
  dependencies after download, filter app-data by root/backup, object kind,
  and digest, then verify immutable ID and bytes against the package. An
  ambiguous or inconsistent discovery result reports recovery required.
  Parent relationships are causal. Listings can discover candidates, but
  cannot turn names, enumeration order, or wall time into currentness proof.

The first implementation should accept a private verified-binding value from
the local HTTP fixture, whose exact root record and app/account check exercise
the real adapter. Keep production unavailable before opening credentials until
an equivalent supported root provisioning and binding constructor exists.
Provisioning must associate the locally minted backup UUID with its own
preallocated root after choosing isolated mode, under a current mode lease.
Persist the root candidate before its first create, and verify the exact
root ID, scoped properties, app and account on readback. A restart or switch
cannot adopt another backup's root. A new backup UUID after leave/re-entry
needs a new root. This proposal separates the fixture and future provisioning
so offline implementation does not depend on a live credential or tablet.

## One original attempt

Keep one in-flight attempt per original binding in the existing Store's
private sync area. Persist the frozen local package reference and marker hash,
the Store generation, exact saved Config path fingerprint and raw digest,
original mode token/epoch/root, intended predecessor, and stable allocated
IDs with per-object progress. Keep resumable session URLs with credentials
under the exact original binding, attempt and provider object ID. Neither
checkpoint nor session goes into the package, ordinary restore, or file status.
Use atomic local writes and current Store custody. Do not hold the Store mutex
over provider calls. Retain the one verified staging package until its
original marker is verified, or original failure/recovery is settled.

Select a candidate from one current Store generation and the explicit saved
Config using the existing package collector. Reuse its same-Store lease,
raw sparse projection and final saved digest recheck. Return no work for
empty history. Ordinary writes after staging can remain pending for a later
snapshot without rewriting the frozen history. Before marker dispatch, verify
the same current mode/binding, Store generation and saved Config; refuse new
publication if any changed. A stale in-flight attempt can be observed by its
original ID under the original qualified binding. Changed mode, Config or
binding cannot authorize a new create for it. A changed account or application
leaves its original outcome unresolved until that original binding can be
verified.

Resolve an object by its exact root, kind and digest before allocating a new
ID. Reuse a unique verified existing object, including one uploaded by a
previous attempt. A stale listing cannot prove the object absent after a
possible creation. Keep the allocated ID and original object reference in
the checkpoint until it is settled, including when a snapshot becomes
stale. If the bounded checkpoint cannot retain this unresolved mapping,
stop for recovery instead of starting another attempt. Before the first
send for any object or marker, persist its allocated ID and exact reference.
Reuse the same ID on retry, including after an expired resumable session.
Treat reported success and conflict as reasons to verify existing metadata
and bytes. After a possible final dispatch, first observe
that exact ID; absent/timeout/read failure stays pending until the original
is reconciled. A still-current attempt may repeat the same fixed-ID create
after verifying the original binding, staged bytes and predecessor. A stale
attempt may only observe. Invalid occupied identity, foreign content and
contradictory ancestry require recovery. There is no allocation of an
alternate final ID or successor while the original marker is uncertain.
A missing local checkpoint for a previously used namespace requires
original recovery. It is not proof that the root never had a committed child.

Before publishing the final marker, verify all promised remote children
and objects for the exact candidate. Only after the marker itself is read
back under the same binding should the worker advance its last verified
checkpoint. A reopened sender observing the original marker also verifies
the full referenced closure before advancing. A verified equal package under
the same current committed predecessor can be skipped; a stale or incomplete
remote listing cannot prove equality. If discovery yields competing verified
children of one predecessor, refuse to select a winner. This first isolated
increment has one local producer using the existing Store ownership and mode
lease. It makes no shared-writer exclusivity claim.

Keep existing per-step request, object and media limits and the package
inspector's inventory/metadata bounds. Bound scoped discovery and transfer
work across steps using the same existing worker budget and cancel handling.
No automatic pruning policy is selected. This increment retains committed
remote revisions and writes no remote delete, trash, or mutable head. On
capacity/quota refusal, keep the last verified revision and expose the
remaining work or recovery condition. Retention/cleanup requires its own
policy and ownership checks. Do not evict a reachable original or add an
arbitrary generation count. Ordinary format 1 is the only source family
this package can publish. Other generations remain explicitly unsupported.

## Reachability and status

The ordinary startup calls `reader_runtime::ordinary_store`, which currently
refuses isolated mode. `mode_maintenance::admit_ordinary` and
`admit_local_dispatch` hold absent/LocalOnly lifetimes, and `main.rs` only
calls `Worker::google` on the old ExistingReader route. Therefore the first
Worker fixture can run against a real Store without crossing startup, but
product integration must address all three edges. Add a runtime-only
ordinary isolated admission for format 1 with legacy sync disabled and no
shared selection. Hold its checked mode lease through the ordinary runtime
and launch publisher admission from that same Store and explicit saved
Config. Existing ordinary Reader/Writer behavior stays usable when the
publisher is disabled or offline. Keep normal maintenance, LocalOnly, legacy
sync and selected startup admissions unchanged. Coordinate startup/dispatch
file ownership before that source step.

Extend the existing versioned file/OS health contract with isolated mode,
device and backup identities, `latest_verified` marker identity if present,
pending/unknown/auth/recovery state, and the verified revision's media
coverage. A previously verified backup stays identifiable when a new one is
pending or the provider becomes unavailable. Use wall-clock time only as
diagnostic last success. An isolated publisher does not report an applied
generation. It claims a recoverable package only after complete verification
of its promised contents. An intentionally omitted sample is a verified
partial-media backup. Missing or corrupt promised bytes make the affected
revision unavailable. No URLs, paths, private provider IDs used solely for
resumption, raw Config digests or preference text enter health. Manager's
existing separate offline inspect and explicit wired data restore and
preference import remain separate operations.

## Ownership and acceptance

The source preparation owner can implement the isolated engine beside
`src/storage/sync.rs`, its narrow upload metadata/readback seam in
`src/storage/drive.rs`, and streaming member enumeration from the verified
`src/storage/isolated_backup.rs` package. Keep the existing Store, provider
transport and Worker. Coordinate `main.rs`, `reader_runtime.rs` and
`mode_maintenance.rs` with their owners before product startup edits.
Manager, production root provisioning and live qualification have separate
owners and evidence.

Test the real Worker and current Drive adapter against the existing local
HTTP fixture. Cover object/marker order, uncertain responses with persisted
original IDs, resumable expiration, restart with the same package, no alternate
ID, same-device resume versus different mode/account/root, Config change,
empty Store, partial/missing media, conflicting dependency/head, bounded
capacity, and unchanged last verified status during pending work. Rebuild
the downloaded test package and verify it through the existing strict local
inspector. Startup needs its own actual ordinary entry-point cases, including
offline local behavior. Keep live Google Drive, Manager/tablet and full
feature acceptance open.

Provider behavior used as a design input is documented by Google. Generated
IDs support app-data creation and retry of the same ID. The app-data scope
and private properties have application visibility limits. Those documents
do not establish this project's live binding or recovery guarantees.

[Generated IDs](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/generateIds) ·
[Upload and retry](https://developers.google.com/workspace/drive/api/guides/manage-uploads) ·
[App data](https://developers.google.com/workspace/drive/api/guides/appdata) ·
[Private properties](https://developers.google.com/workspace/drive/api/guides/properties)
