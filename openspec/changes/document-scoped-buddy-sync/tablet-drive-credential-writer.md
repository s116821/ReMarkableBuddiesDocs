# Conditional tablet Drive credential writer

This is the pre-implementation design for the local USB step in
[Manager tablet authorization](manager-tablet-drive-authorization.md). The
writer installs one already-authorized Buddy V1 grant or removes that exact
grant. It never contacts Google, changes mode, allocates a backup root, starts
a publisher, or installs an application. Existing credential formats and
provider qualification remain in force.

## One fixed command and one existing owner

Add the Linux-only selector `--sync-mode-operation drive-credential
--sync-mode-input -` to the existing mode-maintenance entry. All three request
actions use bounded stdin. Preserve the existing argument conflicts and
reject a missing `-`, redirected input paths, alternate selectors, trailing
JSON, duplicate keys, unknown fields and unsupported versions. The Manager
transport invokes only that fixed command using the same clean environment
and declared config entry as the existing wired mode/model-credential
transports. The wired product entry sets
`REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json`.
Buddy requires that declared configuration to exist. Use the saved validated
`Config.paths.credentials.join("drive.json")` as the only writable leaf. The
default leaf is `/home/root/.config/remarkable-buddies/credentials/drive.json`.
The request has no config path, destination, credential name, executable path,
environment override, or provider permit.

Reuse `Store::open_existing_for_mode`, the credential-root owner marker and
the Store's `store.lock` lifetime. Require the existing ordinary isolated
family and `config.sync.enabled == false`, with no selected Reader or memory
configuration. Refuse unsupported or incomplete storage and a missing config,
Store, or credential root. The writer never initializes them. Require the
current persisted mode snapshot and token inside custody and hold the
appropriate ordinary or explicit mode lease through response delivery. Also
hold the Store inner mutation boundary through final compare, publication,
directory sync, and disk readback. Mode validation in that section must use
the existing locked load/snapshot logic rather than recursively taking the
mutex via `sync_mode_snapshot()`. Recheck the saved config and root identities
before publication. Read-only inspection and reconciliation take custody too
and perform no writes or recovery publication.

The existing runtime and sync Workers retain the same Store lock through
their live ownership. Maintenance returns `busy` while that owner exists.
The connected workflow uses only an already-qualified Manager lifecycle to
quiesce the exact owner where requested, with verified release of the lock.
If such a lifecycle is unavailable, report busy. Do not add an automatic
Stop/Start, force release, or a credential-specific publisher lock. The legacy
GoogleDrive refresh path can rewrite `drive.json`. An isolated qualified
transport instead pins the exact on-disk revision and refreshes in memory.
The writer runs no refresh and cannot race either production path while the
Store is exclusively held. Any future caller that refreshes outside this
Store lifetime must be brought under the same ownership before it is eligible
for the installed workflow. Durable isolated refresh-token rotation and
restart after provider rotation still require their own verified behavior.

## Private request and result

The version-1 request is a closed, action-tagged JSON object. The mode token
is the existing `{actor, sha256}` shape. An original observation binds the
config SHA-256, credential path fingerprint, private parent identity
fingerprint, current Store actor, device and epoch, and exact mode token.
The apply and readback requests carry the exact `original` object returned
by inspect, with fields `config_sha256`, `credential_path_sha256`,
`parent_identity_sha256`, `device`, `epoch`, `mode`,
`mode_token`, and `slot`. The mode uses the existing tagged mode
shape. The actor is carried in the mode token and must agree with both Store
and credential-root ownership. Slot state is either `{"kind":"absent"}` or
`{"kind":"present","sha256":"…","metadata_sha256":"…","binding_sha256":"…","collection":"…"}`.
The revision is SHA-256 over the exact checked file bytes. The metadata
fingerprint uses the existing model-credential fields, including file
identity, owner, permissions, link count, and length. A location fingerprint
or mode token is a compare value and grants no authority.

| Action | Required fields besides `control_version: 1` and `action` |
| --- | --- |
| `inspect` | `expected_mode` (mode token) |
| `apply` | `operation` (nonzero UUID), `original` (observation and slot state), `change` |
| `readback` | `operation`, `original`, `desired` (no secret) |

`change` is one of `{kind:"create", collection, binding_sha256, credential_b64}`,
`{kind:"replace", collection, binding_sha256, credential_b64}`, or
`{kind:"remove", collection, binding_sha256}`. The original slot state is
the expected file precondition, so create requires true absence and replace or
remove requires the exact present revision, metadata and binding. The desired
readback state is `{kind:"present",sha256,collection,binding_sha256}` for
create/replace and `{kind:"absent"}` for remove. An absent status requires an
existing, verified private parent and a missing leaf. Invalid, unowned or
unreadable bytes are never absence and cannot be overwritten by this writer.

Serialize Buddy V1 once in the trusted Manager host, then send its exact UTF-8
bytes as canonical padded base64 inside the private stdin envelope. Buddy
checks the bounded bytes and writes those exact bytes, so Manager can retain the
intended digest without duplicating Rust JSON serialization. Cap decoded
credential bytes at 48 KiB, Buddy stdin at 68 KiB, and Buddy JSON stdout at
16 KiB. Enforce corresponding bounded framing limits before decode and before
SSH forwarding, including the outer observer's base64 expansion. These are
specific to this action and leave existing action limits intact. Require a
single completed request with EOF and strict JSON at both layers. Reuse
`storage::drive::Credentials` and its account/client/collection binding
digest. For writes additionally require V1, a nonempty bounded refresh token,
an unexpired UNIX-seconds access expiry within its admitted range, exact
singleton appdata scope, and a canonical nonzero collection matching the
request. Verify the computed binding against the request and the applicable
current mode or current credential binding. The existing digest covers the
serialized tuple of client ID, Drive permission ID, and collection UUID.
Derive it through the existing Buddy implementation, with a shared test
vector if Manager must compute it before the initial dispatch. These are local shape and custody
checks. They do not replace Manager's independently verified account and
audience or the installed provider checks. Keep the input private to the host
and tablet command. Never include it in argv, renderer/IPC responses, output,
logs, an operation journal, or an upload/staging file outside the guarded
credential directory. Reuse the current application registration and V1
schema. Keep logical binding distinct from the credential revision.

Return a single closed sanitized report with fields `report_version`, `action`,
`operation`, `outcome`, `current`, and `disk_readback_verified`. Report version is 1.
Action is `inspect`, `apply`, `readback`, or `null` when the input cannot be decoded.
Operation is the parsed UUID for `apply` or `readback` and `null` otherwise.
Current is the `observed` object in the same shape as `original`, or `null` when
there is no `verified` `current` result. Inspect returns `observed`. A `verified`
`apply` returns the intended new slot metadata in `current` and the `original`
`operation` UUID. The Boolean `disk_readback_verified` is true only for `observed`,
`verified`, `desired-state-observed`, and `original-state-observed`. Mode and
location custody must still match. For explicit pre-dispatch failures
use fixed codes for `invalid-input`, `unsupported`, `busy`,
`conflict` or `unavailable`. Apply reports `verified` only with a
verified post-publication result, or `outcome-unknown` after a possibly
committed mutation with incomplete proof. Readback reports
`desired-state-observed`, `original-state-observed`, or `unresolved`
against the retained original intent. Never emit tokens, account permission IDs,
raw paths, or filesystem/provider errors. The Manager host checks the
closed schemas, exit, EOF, SSH identity and original result before mapping a
report to public state. Renderer surfaces see only status, account label, and
opaque confirmation/reference values.

## Mode and target sequencing

1. Use the current Write/Apply USB target proof in Manager to bind its private
   confirmation to connection, boot, Store actor/device, mode token/epoch,
   chosen collection, and the inspected slot. Check the approved executable
   and supported service state on the current cable. Target loss, host grant
   drift, app disposal, cancellation before dispatch, expiry or changed
   selection invalidates the pending commitment. The short-lived tablet grant
   is taken exactly once after the confirmation and target checks. The
   protected transport checks identity again immediately before dispatch
   and brackets the reply. Buddy independently compares the saved config,
   Store and slot inside exclusive custody. A user-provided proof value
   cannot enable this composition.
2. Initial setup uses an existing Store with explicit `local-only` selected.
   If setup is new or the supported Store has no explicit mode yet, complete
   the existing first-configuration and LocalOnly controls separately. First
   create requires absence and uses this LocalOnly token. Manager chooses one
   collection UUID for the confirmed account and target, retains it in the
   original intent, and passes it to the private grant take. Verify the
   proposed binding from the V1 bytes. No existing isolated binding is
   required for this first write, and installing the file leaves LocalOnly
   unchanged.
3. Once the file is verified, an explicit choice can use the actual binding
   digest with the existing isolated-mode chooser, then obtain the resulting
   mode token/epoch and use the existing gated root provisioner as its own
   confirmed operation. A verified credential alone is not permission to
   select the mode or create a root. The existing isolated `backup` ID
   allocated by Buddy's mode ledger is distinct from the V1 grant
   `collection`. Preserve the existing root/reservation semantics rather
   than substituting one identifier for the other.
4. In LocalOnly, replace/remove an existing valid grant only under its
   inspected current binding and exact revision. In IsolatedBackup, require
   the exact current epoch and mode binding too. Reconnect replaces under the
   same client/account/collection binding. If a prior verified disconnect left
   an absent slot, reconnect may create into that absent slot only under its
   existing IsolatedBackup binding and the retained original collection,
   verified by recomputing the saved binding. Local disconnect removes the
   exact file under custody. It leaves the saved mode/root intact and presents
   authorization required until reconnected. A later confirmed revoke is a
   separate Google action and may affect other app grants.
5. Refuse implicit account/client/collection switches, a missing original
   collection on same-binding reconnect, or SharedGroup for this ordinary
   slice. A changed binding needs its own explicit mode workflow and
   qualification. Never silently pick a new collection to make reconnect pass.
   Loss of a prior host's collection reference is a recovery case. The product
   may obtain it from existing owned backup evidence when separately
   qualified. It must not guess it from the isolated backup ID.

## Publish and reconcile the original

Use the existing Linux model-credential staged publication pattern. Extract or
reuse its private stage/seal and Linux checked-leaf primitives rather than
calling its model-name/config mutation path or duplicating the engine.
Require a real private owned parent, safe non-symlink ancestors and a single-link
owned private regular leaf. Bind the parent and exact file metadata/bytes
between observation and the last prepublication check. Prepare one exclusive
0600 private sibling, write and sync it, recheck its identity, then publish
via no-overwrite hard-link publication for create (or an equivalent existing
no-clobber primitive), atomic rename for replacement, or exact unlink for
removal. Never truncate in place and never use the unconditional atomic JSON
replacement path for absence-only create. Clean up only the still-owned
temporary and fsync the directory. Read back the actual leaf under the same
custody and compare intended bytes, new private metadata and binding (or
absence for removal). Failures before the destination syscall leave the original slot intact.
An incomplete publication acknowledgment, parent sync or readback after
possible commit is uncertain. The final compare is a concurrency guarantee for the
shared Store owner. It does not defend against an arbitrary local privileged
writer acting outside that owner.

Before possible dispatch, the protected Manager host retains one original
operation reference with its device proof, original observation, selector,
operation UUID, and intended digest/absence, following the existing protected
model-credential readback pattern. Retain only metadata and bounded target
identity for uncertainty, never the grant bytes. Keep dispatch one-use.
Persist enough original metadata in the existing protected Manager storage
using its bounded atomic record pattern to survive restart if the connected
workflow presents restart reconciliation. Keep the same target and slot blocked from another mutation while the
original outcome is unknown. No new tablet
credential ledger is required for this conditional leaf write. There is no
result replay capability in Buddy's writer.

For lost acknowledgment, timeout, partial/trailing frame or connection loss
after possible dispatch, run only `readback` on the original physical target
with the original intent and same boot/actor/device/mode/config/parent proofs.
If confirmation no longer matches, report unresolved rather than rebase. A
verified desired state resolves the current file result. Without the original
receipted commit it does not prove execution causality. Exact original state
is also a current observation, not permission to send the old grant again.
Changed bytes, missing custody or insufficient proof remain unresolved. A new
explicit operation can only follow resolution of the old target outcome, a
fresh inspection, and where needed fresh private consent. Never mint
success from a previous response, teardown, a working SSH session, or a failed
command's exit alone.

## Code and verification plan

- Buddy `src/main.rs` and `src/mode_maintenance.rs` dispatch the fixed
  selector. A scoped `src/mode_maintenance/drive_credential.rs` owns the closed
  wire types, admission and sanitized report. Extend the existing Store
  maintenance and mode helpers in `src/storage/maintenance.rs`,
  `src/storage/recovery.rs` and `src/storage/sync/mode.rs` only where the
  existing private lock and snapshot interfaces need shared access. Give
  local V1 validation and credential-file operations a narrow seam under
  `src/storage/drive.rs` or `src/storage/drive/credential_file.rs`. Reuse
  `src/config/model_credential/linux.rs` and `src/storage/files.rs` for
  checked publication primitives. The isolated provider path in
  `src/storage/sync/isolated/provision.rs` keeps its installed gate and separate
  publisher ownership.
- Manager extends the existing wired observer/private maintenance dispatch
  following `host/local_mode_choice_transport.py` and
  `host/model_credential_transport.py`. The shared privileged operation
  uses `host/drive-auth.mjs`'s private take and the existing original
  operation/USB ownership pattern in `host/model-credential.mjs`. Wire
  `host/browser-helper.mjs`, `electron/main.cjs`, the narrow preload
  bridge and the existing `src/drive-auth.ts` / Backup & sync surface to the
  same host operation. Show the existing connection, selected mode and backup
  state with distinct authorization, verified installation, unresolved
  installation and verified backup outcomes. No extra panel or editable
  config path.
- Rust fixtures exercise absent create, competing create, same-binding
  replace/remove and stale bytes/metadata including a change just before
  publication. Cover malformed or oversize V1, incompatible binding, changed
  mode/epoch/config/actor/parent, symlink/hardlink or unsafe permissions,
  already-held Store by a runtime-style owner, and durable visibility/readback
  on failure before and after publication, parent sync and output loss.
  Assert zero state changes for inspect/readback/error paths and no credentials
  in any result. Take the actual fixed CLI path in subprocess fixtures.
- Manager synthetic checks cover exact fixed stdin, limits, complete EOF,
  same target pre/post, one-use pending take, generation/lease drift and
  lost-ack status using the original metadata after restart. Check both
  packaged surfaces route through the same restricted host behavior. Use no
  real grants for these checks. Installed Linux custody/permissions, verified
  quiescence and restore of ordinary service, approved app registration,
  distinct real grants/cross-account isolation, isolated provisioning and
  backup after Manager exits remain separate hardware/provider acceptance.
  Verify refresh rotation across restart before claiming unattended
  continuity.

## Pinned source basis

- Buddy `c1dd74b23a1b9877aa46fccdde33a804b91ad28e`.
  [Mode dispatch and output custody](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/mode_maintenance.rs#L284),
  [Store exclusivity and root ownership](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/storage/maintenance.rs#L100),
  [Linux credential publication](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/config/model_credential/linux.rs#L587),
  [Drive V1 binding](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/storage/drive.rs#L28),
  [runtime refresh](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/storage/drive.rs#L391),
  [mode ledger](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/storage/sync/mode.rs#L601),
  and [closed installed provisioner](https://github.com/s116821/ReMarkableBuddies/blob/c1dd74b23a1b9877aa46fccdde33a804b91ad28e/src/storage/sync/isolated/provision.rs#L205).
- Manager `49eddc07cd3ce9c0dc4f38bb45682515b6e3a1bf`.
  [Fixed credential transport](https://github.com/s116821/ReMarkableBuddiesManager/blob/49eddc07cd3ce9c0dc4f38bb45682515b6e3a1bf/host/model_credential_transport.py#L156)
  and [original-operation readback](https://github.com/s116821/ReMarkableBuddiesManager/blob/49eddc07cd3ce9c0dc4f38bb45682515b6e3a1bf/host/model-credential.mjs#L100).
