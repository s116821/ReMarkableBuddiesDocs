# Ordinary isolated Drive root provisioning

Proposed against published Buddy `6ef88ca878e712660d37f2ac6e8e0a486ac5ce1e`
and Docs `c62a7d68ae176d6e74b97bff887a94fbdc43e132`. The
[isolated publisher](isolated-backup-publication.md) already has a fixed
package format, durable original upload state, an ordinary format-1 route
and a production gate. This proposal supplies the explicit control that
establishes one provider root for that publisher.

## Public control

Use the existing one-shot host mode binary and existing Store opener. First
`choose` saves the isolated mode and assigns its device, backup and epoch.
That command and `inspect` perform local work only. A separate explicit
operator action provisions the chosen root.

```text
reader-buddy --sync-mode-operation provision-isolated-backup --sync-mode-input -
```

Use the same explicit saved Config selection, existing-only Store admission,
process lock and consuming report as mode maintenance. Require ordinary
format 1, legacy sync disabled, absent Reader/memory selections, complete
local custody and the original matching isolated-mode token for a first
operation. Root provisioning may run on an empty Store. The root is control
metadata. The Worker still publishes no package for empty history.

Input is one UTF-8 JSON object with exactly the fields shown here, using actual
UUIDs and the unmodified token returned by the private host inspect command.
It is limited to 16 KiB inclusive and rejects duplicate keys, trailing JSON,
unknown fields, nil UUIDs, an unsupported version and unsafe input transport.
The caller owns EOF, cancellation, and an outer deadline.

```json
{
  "control_version": 1,
  "operation": "<new operation UUID or the exact original UUID on retry>",
  "expected": { "actor": "<actor UUID>", "sha256": "<lowercase SHA-256>" }
}
```

The command derives device, backup, epoch and grant from the admitted Store
and chosen mode. There is no input for credentials, a provider ID, account,
application, generation, config path, namespace selection or an alternate
endpoint. A request with unknown operation and stale expected token is a
conflict. A known operation requires the original expected token and exact
validated input. Exact retry is an explicit call by the owner, including
after output is lost. The command never rebases to a fresh token or turns
missing output into a new request.

The **provision command only** adds `data.isolated_root` to the existing
bounded report-v1 envelope when there is valid local result custody. All
other command report shapes stay as delivered. The outer `status` retains
the existing enum, `activation_performed` is always false, and the
existing mode `receipt` and `receipt_status` are null for provisioning.
The new value has exactly these fields:

| Field | Value |
| --- | --- |
| `operation` | Original provisioning UUID |
| `device`, `backup`, `epoch` | Original device, backup and operation epoch UUIDs |
| `outcome` | `root-verified`, `outcome-unknown`, `authorization-required`, `retry-later`, `recovery-required` or `provider-binding-unqualified` |
| `currency` | `current` if original epoch and binding still match the current snapshot, otherwise `historical` |

`ok` with `incomplete:false` and `root-verified` means exact provider
readback completed. A historical result carries historical evidence only.
Use `unavailable` with `incomplete:true` for unknown, auth or retry,
`failed` with `incomplete:true` for recovery, and `unsupported` for the
unqualified gate. Use existing invalid-input, busy and conflict handling
with no fabricated result. In a safe early refusal the whole `data` may
be null. When `data` is present without valid result custody, the
`isolated_root` key is omitted. It is never emitted as JSON null.
For an unqualified production application with an admitted original
intent, the bounded report includes `data.isolated_root` with
`provider-binding-unqualified` and its original identities. Provider IDs,
root properties, grant identifiers and digests,
resumable URLs, paths and content stay out of the new result. The envelope's
existing `current_snapshot` remains host-only and can contain mode tokens
and binding details. One report is emitted while the Store and the applicable
current mode output lifetime are held. A prefix-write failure triggers no
additional write or provider operation.

Manager's existing inspect route stays read-only. A future provisioning
consumer lives in the separately owned privileged wired host service, using
an identity-verified connection and exact fixed command. That host validates
the full report, correlates the operation and current connection/boot,
retains retry input privately and returns only redacted state to the renderer.
It may consume the existing redacted Worker health separately. Root verification
does not prove a committed backup or current runtime health. This proposal
does not add Manager IPC, UI, OAuth or service stopping. A separately
connected desktop OAuth grant provides neither the tablet's protected
credential nor proof that its app-data namespace is visible to Manager.
Future Manager download must independently qualify its provider visibility.

The minimum future wired handoff has two distinct inputs. A privileged
credential-install action would place a separately authorized, qualified
tablet grant in the existing protected Buddy Drive credential location.
Its private payload is the existing credential-v1 schema, including client
registration, account permission ID, refresh material, app-data scope and
the credential collection used in the existing grant digest. The tablet
grant must be produced by a supported authorization flow and installed
atomically in its owned credential area. The wired host uses only the
resulting protected grant binding digest for `choose`, then the exact
saved mode token for provisioning. This producer accepts neither secret
JSON on stdin nor arbitrary credential location. Manager source
`457d2278` keeps host registration/grant inside `host/drive-auth.mjs`;
`drive-protocol.mjs` exposes an opaque `authorizationId` and
`backupReady:false`. That contract supplies neither handoff input.
Credential installer, account/namespace interoperability and UI stay with
the existing Manager/auth owners.

## Root identity and persisted custody

Reuse Drive generated IDs and the existing immutable app-data metadata and
readback model. Create one zero-byte binary root with a fixed name and
`parents:["appDataFolder"]`. Its exact app properties match the existing
publisher's `Binding::root_properties()` contract.

| Private property | Value |
| --- | --- |
| `buddy_isolated` | `1` |
| `kind` | `root` |
| `root` | Exact provider-generated root ID |
| `backup` | Locally minted backup UUID |
| `device` | Persisted Buddy device UUID |
| `grant` | Existing digest of client ID, account permission ID and credential collection |

Verify the exact returned ID, untrashed state, app-data space, binary root
metadata and exact private property map by ID. Use the existing private
property bounds before staging. The credential collection participates only
in grant correspondence. Actor, chosen epoch and conditional token are
private local custody. The immutable root does not encode an admission
epoch that could change while the same backup identity remains chosen.

Persist the original and package progress in one owned private checkpoint
per backup UUID, under `data/sync/isolated/<backup>/publisher.json`. Keep
sessions bound to the exact binding and attempt under the protected
credentials area and package staging under the publisher's disjoint private
path. Extend the checkpoint with a versioned provisioning record and retain
the publisher's existing latest/attempt/settled fields. The root record pins
the operation UUID and original conditional token, actor, device, backup,
epoch, grant digest, and optional generated root ID. Its states are
`prepared` (ID absent), `candidate` (ID retained), and `verified` (same ID
read back). Root properties and the request derive deterministically from
the ID and typed record. OAuth tokens, raw account values, and provider
responses are unnecessary. An exact readback of the protected checkpoint
is required after a write with an uncertain local acknowledgment.

A small private reservation in the existing mode ledger distinguishes
never started from missing publisher custody for a used backup. Persist the
prepared checkpoint first, then atomically reserve its backup, operation
and original epoch in the existing mode file under the Store mutex.
Verify the reservation and prepared record before any allocation. The
reservation is additive, bounded by the existing mode history limits, and
retained through all mode transitions. It links to a real historical isolated
receipt. Index initial and later admission operations by UUID in this same
private ledger, with one accepted operation per backup and epoch. Use the
index to resolve historical requests to their exact checkpoint without a
directory scan or caller-supplied backup ID. Register a later admission
operation before its remote observation. An indexed admission operation
without a completed receipt is resumable with its original input.
Validate original tokens against the corresponding mode history prefix.
Preserve current and historical conditional tokens by serializing the exact
legacy projection of `format`, `actor`, `device` and `transitions` in their
original order and retaining the existing outer actor tuple. Private
reservations cannot change public receipts. Mode selection uses its existing
input.
A prepared checkpoint without a matching reservation can complete that
initial handshake only while its exact original is current and before an ID
is assigned. A reservation whose checkpoint is missing, malformed or
inconsistent always requires recovery, even if listing finds nothing.
A pre-provisioning Store with neither durable record has no root allocated
by this protocol. Existing localhost publisher checkpoints are fixture
inputs and cannot act as production genesis. Keep the reservation and
checkpoint outside portable backup and restore. Restored data on a
replacement actor goes through that actor's own mode transition and root
provisioning.

### Interrupted local writes

Both files are written under the existing process Store lease using the
owned atomic writer. Release the Store index mutex before any provider
request. After an uncertain local write, reread both files under custody and
validate their exact operation, backup and epoch correspondence. The
observable states determine which action is available.

| Durable evidence | Next action |
| --- | --- |
| Neither record is present for the current backup | A new current request may reserve a local original. |
| Prepared checkpoint only, with no allocated ID | Only its exact current operation may finish reservation. A stale request cannot complete it and makes no provider request. |
| Reservation and matching prepared checkpoint | Only its exact current operation may allocate. A lost allocation response with no durable ID can consume an unused ID, but cannot create a root. |
| Reservation and matching candidate | Observe the recorded ID first. An authorized current retry may create only at that ID. |
| Reservation and verified checkpoint | Observe the same root. A missing formerly verified root requires recovery. |
| Reservation with missing/foreign/corrupt checkpoint, or an allocated checkpoint with no matching reservation | Require recovery before any new allocation or create. |

Root verification and the initial empty publisher progress are one
checkpoint write. Uncertainty on that write leaves either the candidate
to observe again or the verified original with its current progress.
Historical observation may update the original's verification evidence
without authorizing the current epoch or modifying another backup.

Use a private redacted historical result only when the indexed original
can be validated. The provisional checkpoint that never acquired a
reservation is discoverable from the current backup only, so a replay
after departure returns conflict without an unrelated path lookup.

## Provider identity, dispatch and recovery

The provision control and Worker first require a separately qualified
installed provider application policy and compatible local mode. Grant
installation stays in the existing protected credential responsibility.
Use the fixed Google endpoints and read the existing owner-only
`credentials/drive.json` through protected-file validation. Check that
the installed application is allowed, the grant digest agrees with the
original, Google accepts the protected refresh grant with that client,
the grant provides `drive.appdata`, and Drive `about.user.permissionId`
matches the protected account. A cached bearer and a matching permission
ID alone do not establish client provenance. Reuse the existing refresh and
`about` transport with an explicit fixed-client refresh proof for initial
qualification or credential replacement. Scope evidence comes from the
supported grant installation and the refreshed scope when returned. A refresh
with reduced scope invalidates admission. Isolated refresh keeps the
replacement bearer and expiry in memory and leaves the protected file under
the installer owner's custody. Before every create, recheck
the original protected grant identity, current Store/mode lease, exact
checkpoint candidate and persisted token. No Store index mutex spans HTTP.
Missing, revoked or different authorized credentials leave the original for
recovery and preserve the previous backup.

The legacy Drive refresh helper writes back `drive.json`. The isolated
adapter keeps refresh results in process and compares the exact original
protected file revision before and after refresh and before dispatch. A
replacement ends this invocation's authority even when it projects the
same grant digest. Supported tablet grants must continue to refresh across
process restart from the installed material. Any provider refresh-token
rotation that requires installing a new durable grant belongs to the
protected installer boundary and must be covered in qualification.

1. Validate or resume the prepared original under exclusive Store ownership.
   Take the exact current mode lease for mutation. After verifying the
   protected grant, request a single generated app-data ID. Validate the ID
   and private metadata bounds. Persist it atomically before a root create.
   If allocation returned no durable ID there has been no create. Reread
   the checkpoint before requesting another allocation.
2. Observe the recorded ID first on restart, and before any repeat send.
   A matching readback advances to verified. Contradictory metadata, a
   malformed identity or unexpected occupancy requires recovery. A
   first-create or retry at an absent candidate is allowed only under
   current original authority. Prepare the deterministic metadata request
   before the final checks. Send at most one metadata-only create at that ID
   per command attempt. A fresh qualified token and exact account proof must
   still match the command when the request is dispatched.
3. An HTTP success, 409, timeout, empty or lost response all go through
   exact-ID observation. Missing/unavailable observation after possible
   dispatch keeps the original unresolved. A still-current operator retry
   may repeat a same-ID create after renewed checks. A stale original may
   only observe its exact ID under the original qualified grant. A root
   previously verified and now absent requires recovery. Never use listing,
   a root name, collection or a supplied ID to adopt a root or prove genesis.
4. Record `verified` with the same ID before any Worker can start. With a
   verified first root, empty package progress in the same checkpoint is
   the original genesis. If that checkpoint is later missing, no code
   creates another genesis or root for that backup. No processing step
   overwrites or deletes a provider object.

One bounded command fits the existing request deadline and cancellation
model. 429/5xx and authorization are distinguished from invalid custody.
A command/worker restart can use local receipts without treating them as
a substitute for current exact remote root verification.

## Epoch changes and Worker admission

Leaving for LocalOnly, selecting a group or changing the protected binding
retires current authority without freeing its root identity or deleting its
checkpoint. Re-entering isolated mode after departure or changing the
binding uses the new locally minted backup UUID and requires its own
reservation and generated root. Existing package and root outcomes stay
with their original backup.

A new `choose` for the same consecutive grant currently retains the backup
UUID and advances the epoch. Preserve this behavior and the original root
record. A command retry naming the old operation can only observe after
epoch change. For a verified root and no unsettled publisher attempt, a
new explicit provisioning operation for the current epoch may read back
that same root and persist current admission separately from the immutable
original. Require continuous validated history for this actor, device,
backup and grant. Keep one successful admission receipt per mode epoch,
bounded by the already limited mode history, with operation UUID, original
token and epoch. A replay requires the corresponding original request, and
a distinct operation cannot replace a retained receipt or allocate another
root for the same backup. Publish the current admission and replacement of
the idle publisher binding's epoch in the same atomic checkpoint write.
Carry `latest` unchanged. If an old root candidate is
still unresolved or a package attempt holds the old epoch, return recovery
required for current admission, retaining all original IDs and previous
verified status. The old root operation can still resolve by observation.
The first increment does not rebind an unsettled package to a new epoch.
A deliberate departure and re-entry can use a different backup while
retaining the previous backup and its pending records for recovery. A local
restore or target promotion that changes the supported Store family also
ends format-1 Worker eligibility.

`Worker::isolated(store, policy, saved_config)` resolves the existing mode
snapshot and, behind the installed qualification gate, reads the matching
reservation and publisher checkpoint. Its local constructor loads a verified
root receipt for the exact current admission epoch and takes the existing
mode and single-publisher lifetimes. It constructs the existing isolated
`Engine` from that checkpoint and calls `Worker::launch`. The existing
Worker step establishes an in-memory verified root before provider upload:
check saved Config association, protected application/account proof and exact
remote root readback. This keeps bounded network calls off ordinary startup.
The startup gate does not create roots or a fresh checkpoint. Unsupported or
unqualified application branches refuse before
credentials. Missing credentials, unavailable provider and unresolved
provisioning leave Reader/Writer local; use the versioned redacted health
with device/backup and the last verified marker for that binding when valid
local custody is available. Corrupt local mode remains a local refusal.
The legacy and selected Worker admissions keep their existing routes.

## Source ownership and verification

| Source surface | Proposed change |
| --- | --- |
| `src/main.rs`, existing sync-mode flags/dispatch | Select the new enum value and enforce exact-dash input. No startup architecture change. |
| `src/mode_maintenance.rs`, `docs/host-sync-mode.md` | Strict request/report handling, existing Config/Store acquisition, lease-through-output and public examples. Keep existing inspect reports unchanged. |
| `src/storage/sync/mode.rs` | Private reservation load/validation and original/current snapshot correspondence under the existing Store guard. Keep receipts and conditional tokens stable. |
| `src/storage/sync/isolated.rs`, new `src/storage/sync/isolated/provision.rs` | One backup-keyed checkpoint, exact original progress, root control, separate current admission and typed constructor for the existing engine. |
| `src/storage/sync.rs` | Declare the private control boundary and connect qualified ordinary admission to the same Worker. |
| `src/storage/drive.rs`, `src/storage/drive/slot.rs` if factoring the wire helper | Reuse fixed-ID metadata-only create and exact ID readback, generated IDs, protected grant and bounded request logic. Preserve selected/legacy request and verification behavior. |
| `src/storage/drive/shared_fixture.rs`, `src/mode_maintenance/tests.rs`, `src/storage/sync/isolated/tests.rs` | Exercise real command/control, durable reopen, adapter and scheduler behavior using localhost only. |
| `src/storage/inspection.rs`, `src/storage/inspection_v3/scan.rs` | Coordinate with the inspection owner before adding the expected private isolated checkpoint layout. Admission of the exact owned path must preserve bounded no-follow enumeration and expose no checkpoint contents or provider IDs. |

Verify exact same-ID create/request counts for before-allocation, after
durable pin, uncertain response or commit acknowledgment, 409, corrupt
or foreign root and stale observation. Cover wrong client/account/namespace,
binding replacement during send preparation, credential loss, missing/corrupt
checkpoint with its reservation intact, report interruption, Store Busy,
old/new epoch behavior with and without an outstanding package, away/back
with new identities, empty history, and the actual runtime Worker admission
against that rooted checkpoint. Assert zero provider I/O on prequalification
or rejection and no Store mutex during provider waits. Verify unchanged
legacy/selected/inspect shapes and redaction of command/health output. Both
offline storage scanners currently enumerate known `sync` children. Verify
that the new private checkpoint layout yields neither a warning for normal
provisioned custody nor acceptance of foreign entries.
Hosted Linux and live provider evidence stay separate.

Drive documentation establishes generated IDs, retry of a pre-generated
ID, per-app visibility and app-data space. These are inputs to the proposed
wire behavior. Installed application qualification and live behavior require
independent evidence, including fixed-ID metadata-only create/readback,
actual grant provenance and any separate Manager app-data visibility.

[Generated IDs](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/generateIds) ·
[Same-ID retry](https://developers.google.com/workspace/drive/api/guides/manage-uploads#use_a_pre-generated_id_to_upload_files) ·
[Application data](https://developers.google.com/workspace/drive/api/guides/appdata) ·
[Private properties](https://developers.google.com/workspace/drive/api/guides/properties) ·
[OAuth clients and grants](https://developers.google.com/identity/protocols/oauth2)
