# Proposed mechanism and integration boundaries

## Existing behavior and reuse

At Rust `ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`, `src/storage/types.rs` defines opaque domain envelopes and causal parents; `sync.rs` imports immutable manifests and retains concurrent record heads. `drive.rs` already allocates IDs with `files.generateIds`, creates ordinary files, and verifies metadata and content after a 409. Its generic upload treats different content at the same ID as an integrity error. Shared-sync contention needs a separate explicit winner-read result, not a relaxation of object hash verification.

The existing whole-store recovery path and branch-preserving index remain valid for local storage and isolated backup. Shared mode needs a selected aggregate view; importing the winner into the existing all-history index alone cannot replace a stale branch. No blind whole-store restore, deletion of another document, or timestamp-based branch resolution is acceptable.

## Identities, modes and bootstrap

Device identity, local actor identity, backup identity and group identity are separate values. A replacement installation creates a new actor/device identity while preserving historical record IDs. Credentials are account/client bindings, not shared data. Portable configuration is an allowlisted projection; it cannot serialize device paths, connections, credentials, group membership, cache or runtime state.

Local-only never publishes. Isolated backup publishes recoverable snapshots beneath its own device-backup root and never imports another device automatically. Shared mode requires explicit selection of a verified group root by immutable provider ID, account permission identity, app identity and protocol. Switching modes disables the old publisher before activating a new binding; pending work keeps its old binding and cannot leak into the new namespace. Leaving does not delete the group or any device backup. Empty local state never overwrites an existing remote collection.

New-group creation allocates and durably records one root ID, group UUID and first catalog slot before a bounded immutable root create. Roots and catalog entries use the same descriptor-pointer publication discipline as document slots below. Lost acknowledgement retries that same root ID and verifies the returned content. A label is display-only: two independent creators can create two distinct groups with the same label, which must be presented for explicit selection rather than silently joined. A join uses the selected root and pulls before publication. Drive app-data groups require a supported provider account/application binding matrix. Browser, Electron and tablet OAuth registrations are qualified explicitly: the same user/account alone does not establish appDataFolder or private appProperties visibility across registrations. Verify the actual supported bindings and refuse incompatible clients before shared-mode activation; no application combination is currently qualified. Cross-account sharing is not promised by `drive.appdata`.

## Candidate conditional commit: one slot per accepted base

The root names a catalog genesis slot. Catalog commits map stable aggregate keys to document genesis slots and link to the next catalog slot. Registration is append-only: an existing key's genesis slot is never replaced, even after a document tombstone. Catalog contention serializes registration only, not every document edit. A losing registration reads the winning catalog: if its key exists, it adopts that slot; if absent, it may register its still-unregistered key against the new catalog base. It may never replace an existing key or lose another entry. Bounded incremental catalog entries and replay checkpoints avoid a growing full-catalog snapshot in each commit.

For each document or independent global record, the accepted revision provides a pre-generated `next_slot_id`. A pending attempt pins group, aggregate key, exact accepted base revision/hash, slot ID, local generation, operation ID and immutable candidate digest. It stages and verifies its manifest, envelopes and selected media before creating a metadata-only commit pointer at that exact slot. The separately staged immutable descriptor contains protocol/schema, group/key, base identity, operation/actor identity, manifest hash and provider object reference, media coverage, and the next pre-generated slot ID. Proposed maximum descriptor size is 64 KiB, below the adapter's existing 256 KiB non-resumable threshold; referenced manifests retain existing bounds. Store the descriptor itself with the existing content-addressed upload path before adjudication. The actual slot creation is a normal JSON `files.create` request with an ordinary empty-file MIME type, fixed ID, `appDataFolder` parent and six private properties: protocol, kind, group, descriptor provider ID, descriptor SHA-256 and scope-key SHA-256. Read these properties by exact ID and verify the referenced descriptor and manifest. Bound the request to 8 KiB, each UTF-8 key-plus-value to 124 bytes and the property count below 30. Provider IDs exceeding the limit are refused before publication, not truncated. No resumable or multipart commit upload, metadata reservation followed by a later write, or `files.update` is used for adjudication.

The adapter exposes `create-or-read-slot`, distinct from generic object upload: bounded metadata-only create with the chosen ID; on 409 or uncertain acknowledgement, read that same ID with an explicit private-property field mask and verify descriptor identity and referenced immutable content. Identical operation and digest acknowledges the original attempt. A different valid descriptor with the same group/key/base is the winning revision: replace the losing selected local view and retire its outbox attempt. Never allocate a different slot to evade contention, retry stale payload at the winner's successor, or auto-rebase it. A new edit is allowed only after the winning generation is applied and the domain operation starts from that accepted base.

Ownership and commit are one provider creation event, not a reserved lock followed by a mutable update. There is no lease, expiry or clock comparison to renew. An old process retry is confined to its old slot and cannot publish at the successor. This candidate must demonstrate provider exclusivity and complete readable metadata-pointer publication before shared mode is qualified; idempotent retry documentation alone is insufficient live concurrency evidence.

If a slot is occupied by invalid, incomplete, wrong-group or wrong-base data, stop that aggregate with recovery-required status. Never delete/recreate the slot, claim another slot, or treat timeout/404 as proof of freedom after an uncertain write. No automatic lease-expiry workaround exists. Provider removal and unavailability are not domain tombstones. Clients only create/read protocol files; external mutation or deletion is an integrity/recovery event, not a supported history rewrite. Persist observed commit digests and reject changed bytes on replay.

## Source-document aggregate and domain ownership

Aggregate key is `(group, source-document identity)` and is stable across conversation/page/operation IDs. Native UUIDs are historical correlation inputs; title and page position never establish identity. REM-37 `SourceObservation.document`, bindings and receipts remain its authoritative domain schema. A domain-owned projector reads one consistent selected store snapshot and returns the existing opaque envelope references, media descriptors/coverage and unambiguous `SourceObservation.document` key. Its reference closure enumerates all Buddy records belonging to that source document, including conversations, turns, captures, source uses, binding receipts, operation receipts and export associations. Storage handles typed scope references and opaque envelopes; it does not invent a second conversation schema. Records lacking a stable source document remain backed up and visibly deferred from shared document publication. Ambiguous/multi-document ownership is refused until the domain owner defines it; it must not silently choose a conversation ID as a document key.

Subject memory, handwriting and portable configuration use their existing domain-owned stable record keys and independent commit chains. A shared reference cannot give a record conflicting aggregate owners. Preserve unrelated keys when applying one winner. Optional domains may be absent; absence is not deletion. A tombstone is an explicit accepted aggregate/record revision with causal parentage, never an inference from remote listing or native page lag.

Imported capture/binding/export history remains historical and unbound for the current tablet. Local verification of exact native identity and current state is a distinct operation. Shared sync cannot authorize page recreation, erase, native export, undo replay, learning from a canceled turn, or mutation of missing native pages.

## Atomic local selection and operation fencing

Maintain an immutable selected aggregate snapshot plus durable selection metadata under the existing owned storage root. Verify all referenced objects/domain schema/media coverage before staging a new selection. Activate it at one local atomic transaction boundary under the existing OS store lease. Keep immutable loser/history objects as non-selected recovery evidence; they are not active heads and must not be re-enqueued automatically. Local readers use the selection consistently; a crash before activation leaves the old view, after activation leaves the complete new view. Rebuild/replay must respect selection, not resurrect every stored historical branch.

Every Reader/Writer operation captures the aggregate generation and accepted base. A domain-owned admission guard serializes generation/base validation AND actual native handoff with selected-revision activation; checking then dispatching outside that guard is forbidden. Durable writes atomically revalidate both pins with commit/selection under the same local ordering. The OS process lease does not provide this within-process ordering. Applying a winner invalidates not-yet-admitted operations, but cannot retroactively cancel an already-admitted external effect. Keep its existing native evidence/reconciliation guards, settle it as verified or uncertain without attaching stale completion to the new selected view, and block conflicting admissions while settlement remains unresolved. A late completion cannot append active history or manufacture success. Exercise activation between check and attempted dispatch and a late durable completion. The integration lock order is domain admission guard, then store selection/commit lock, consistently for admission and activation. Persist the existing domain operation intent with its pinned base/generation before handing off the external effect; hold the admission guard through actual handoff, then release it for completion observation. Selection activation preserves unresolved local operation intents and their required evidence/media outside replacement of the active shared history. An already-admitted operation remains in its existing reconciliation state until the domain adapter verifies settlement against its original native request; record that settlement as historical/reconciliation evidence, not an append to the newly selected generation or a stale payload rebase. Do not clear the unresolved latch from a sync receipt, elapsed time, imported binding or uncertain callback. The exact existing journal/guard seam and ownership remain for REM-37/Main review; no new operation schema or generic admission framework is selected here. The synchronization worker never holds a store mutex across network I/O. Offline work is allowed against the pinned last accepted base and remains visibly pending; if that base loses remotely, its active view is replaced without republishing the stale payload. Domain integration and the actual native admission fence require owner review and tests; generic DTOs do not qualify the native path.

## Media, restore and status

Reuse content-addressed media descriptors, lineage validation and explicit coverage. Required local screenshots/confirmed samples remain locally retained even when remote size policy omits them. A valid logical revision may declare intentional remote media omission; status and restore must expose it. Missing media promised as included is incomplete, so it cannot silently become an acknowledged complete snapshot. Interrupted, corrupt or unknown-schema imports never activate partially.

A disconnected Manager may authorize and inspect cloud backups through its host adapter. Selected restore is a separate explicit hardwired maintenance transaction using validated staging and atomic activation, with a new actor identity, rollback and protected source data. Restore cannot turn historical binding into live authority or reuse another tablet's credentials. Shared-group join is distinct from restoring an isolated backup.

Versioned files/OS commands report mode, device/backup/group identities, selected root, latest verified committed revision, applied revision/generation, last successful sync, pending/offline/auth/contention/replacement/recovery state and media completeness. Wall-clock times are diagnostic only. No service API is introduced. REM-42 owns equivalent browser/Electron UI behavior; this lane supplies the contract and fixtures.

## Qualification and review gates

Host transport fixtures cover overlapping creates, response loss, replay, corrupt/incomplete slots, group registration, bounded discovery and stale operation fencing. Live Drive tests in a disposable explicitly authorized app-data namespace must separately verify same-ID concurrent create exclusivity, cross-client private-property visibility, interruption before/after metadata-only create, 409 reads, property-limit refusal and deletion/rewrite failure handling. No live account test has occurred. Until that evidence and independent contract review exist, this remains a candidate; shared publication must not be advertised as qualified.

No native operation or personal account access is required to write the proposal, implement generic fixtures after review, or validate isolated recovery. Native integration remains separately gated by its actual source identity/admission capabilities.

## Independent contract review boundary

Main reviewed exact `ebf8c72cc286de988d0307c98bf34d48dce8f4da` and accepted generic fixed-ID metadata create-or-read and host transport fixtures. That permits the generic adapter seam only, not live-provider or domain/native integration. Main subsequently accepted the clarified admission/settlement, consistent opaque projector closure and application-binding matrix contract at `7e06d9f96f7fb037698b4b44a71ed2518e44ff06` in [the independent review](https://github.com/s116821/ReMarkableBuddiesDocs/pull/7#pullrequestreview-5439778838). The next [concrete seam proposal](integration-seams.md) maps the inspected REM-37 journal, store and actual backend handoffs; Main's ownership/interface review remains required before those shared-path edits. Generic transport observations verify pointer/object bytes only and cannot declare a domain-valid winning base or authorize native effects. No worker/config enables shared publication in this generic slice.

## Bounded outbox inventory seam
Store::selected_attempt_inventory() returns the complete strict local journal as original SelectedAttempt values in deterministic UUID order under one Store lock. Reuse existing actor/fingerprint/filename/item/metadata limits, with whole-read refusal on any corrupt or foreign entry. Do not verify current selection/object availability, fetch provider state, mint live tokens or modify journals; stale and withdrawn intents remain discoverable historical custody. Callers must perform current checks and mode/domain admission separately before any future send/apply.

The remaining live-provider resource and execution boundary is proposed in [provider qualification contract](provider-qualification-contract.md); no live resource or worker activation follows from that proposal.


## Current product worker integration precode

[Shared-worker integration](shared-worker-integration.md) maps actual72ddbe55
interfaces, original-operation handoff/recovery, exact root/catalog/base/slot,
mode/account/application qualification, complete domain/media winner validation,
serialized activation/retention and truthful file status. It proposes the required
notebook format5 compatibility/producer stage rather than pretending format4 is
already selected-ready. It also preserves local memory genesis validation through
a receiving-local registration bridge; a foreign local transaction hash is not a
portable genesis identity. These choices need independent review before code.
The delivered storage/slot mechanisms are reused; accepted inspection/import/archive
increments and unrelated domain/native drafts are not reopened.


## Shared-worker successor r2 review corrections

The [integration design](shared-worker-integration.md) now specifies read-only
agreed-slot observation without a candidate; explicit CreateGroup allocation under
ordinary mode followed by exact conditional shared-mode selection; current-original
same-ID retry versus stale observe-only recovery; and passive first-join/pull
receiving custody with receipt-first crash reconciliation. No outbound attempt is
fabricated. It also makes staged mixed-scope readiness depend on exact local
registration across all product paths, separates active/retained causal projections
and imported history from verified local uncertainty, chooses committed-not-applied
for unresolved selected-receipt overlap, and requires notebook live/reopen validation
parity and original-only capability reconciliation. These are proposed corrections
after protocol/domain review, not implementation or runtime evidence.

Later provider qualification may use a suitable existing explicitly authorized
OAuth/account binding with isolated disposable app-data resources and exact cleanup;
a new account/project is not mandatory. No live credential/resource action or
production eligibility is selected. Original precode remains preserved; corrected
precode acceptance still precedes implementation and the eventual paired lifecycle.


## Reviewed optional-domain integration

The active delta now records portable configuration as one independently selected
group-global record, consumed through the reviewed strict Artifact and admitted
LocalConfigSnapshot raw merge. Effective values are request-scoped; current saved
Manager/import editing remains its delivered local contract. Selection/absence
pins join the same ordered gate set at actual handoff and result commit. Strict
decoding starts from the original envelope bytes before a Value can collapse
duplicate nested members.

Confirmed handwriting uses existing Handwriting1 semantics and one typed scope
per correction, not a whole-profile snapshot or document-derived key. Its raw
adapter is independently owned; core Store/catalog/Worker/format5/selectors and
actual consumers stay in this delivery. Local original operation reuse checking
and publication must be atomic across applicable producers under the existing
Store mutex and bounded accepted local transaction evidence, with no shadow
operation database. Imported envelope operations are not local receipts.

The compatible recognition receiving interfaces from
[Buddy105](https://github.com/s116821/ReMarkableBuddies/pull/105) remain a real
separate source dependency. Exact correction transfer does not complete Reader
analysis/verification, Writer image normalization/ingress, null-original admission
or fidelity/native qualification. Stored samples remain historical data and their
selected coverage controls usability independently of unrelated cache contents.


### Accepted correction adapter interface split

The disjoint `handwriting::selected` component supplies `Owner::new(profile,
correction)` and `Owner::scope(group, binding_sha256)` using the existing record
UUID and approved independent scope key. Core matches the typed catalog owner,
actual group/binding, actor and format5; this value is not current admission.

`Projection::read(owner, manifest, bounded_original_object_loader)` validates
exact original record/sample references, duplicate-free JSON, existing Handwriting1
lineage/immutable genesis, one connected head and exact original-sample coverage.
It exposes the current head, confirmed value or tombstone and verified bytes only
for an Included current sample. Read each retained closure separately as evidence.
Storage-valid PNG custody does not establish the stricter static recognition rule.

`Mutation::prepare(owner, actor, ValidatedInput)` produces an envelope/sample and
fingerprint without Store effects. Original receipt lookup precedes
`Mutation::check_predecessor(current_projection_or_qualified_absence)` and fresh
CAS. First Confirm requires separately established catalog/genesis absence; None
is not an absence permit. Core performs original-operation identity checking and
selection publication together under the actual Store mutex across applicable
producers. The component grants no admission, maintains no journal/index and
exposes no enabled selected dispatch or recognition hook. Native owns its raw
handwriting files; core/catalog/Store/format5/admission/CLI/real callers and Docs
remain coordinated here. No additional review of these accepted seams is required
before that disjoint component implementation.

### Correction catalog discovery and local transaction custody

The correction command publishes its explicit original through the existing
selection transaction. Catalog discovery enumerates bounded published
selection heads, filters for Handwriting in the current binding, and verifies
the reachable local genesis and exact typed closure under the ordered gates.
An imported genesis has a receive receipt and cannot register a local
correction. Staged heads and arbitrary record history grant no discovery.
The Store's existing format5 operation claim and publication mutex arbitrate
operation UUID reuse against accepted selection history. No additional journal
or index is needed.

### Shared-preference Manager and one-shot command boundary

The coordinated Manager implementation follows the
[accepted shared-preference management contract](shared-preferences-manager.md).
That leaf is owned by the Manager lane; this design, the requirement delta and
tasks remain core-owned. Saved-file import/export keep their delivered local
meaning. The separate shared control uses a successful selected Inspect before
Edit and a strict sparse V1 patch that contains only deliberate declarations.

The core one-shot Inspect/Edit/Status command must bind original mode epoch,
group/binding, Store/selection identity, accepted head or established absence,
and the exact raw local configuration snapshot used for the reviewed effective
projection. Status retains only the original operation, guard and patch digest;
the original local transaction and exact result must prove correspondence without
retaining private patch text, creating a second operation index or retrying Edit.
An unchanged resulting portable declaration artifact under the existing
structural/declaration semantics is a no-change outcome without a fabricated
receipt. Equal effective values alone do not establish no-change: omitted,
supported null and explicit-default declarations remain distinct, and adding a
shared declaration may change future fallback despite today's equal value.

The browser and Electron paths use the same guarded private host transport and
opaque bounded references. A saved shared-group mode only offers the control;
unsupported older Buddy, busy exclusive Store custody, stale inspection and
post-dispatch uncertainty remain explicit. No automatic Stop, replay, saved-file
fallback or provider request is introduced by the Manager transports. A verified inspection describes the
next admitted request's overlay; running activation is unverified. Source-only
UI/protocol fixtures do not close the real backend/host parity gate, and the
combined unfinished feature is not independently enabled or merged to main.

Only the real Buddy first-absence path may reuse its already-qualified fixed-slot
adapter for a bounded GET-only refresh of Drive data. Qualification and current
mode/binding admission precede credentials. Under existing Store/mode/domain
custody and one original deadline/read budget, revalidate exact root identity,
complete accepted catalog, expected global key/owner, Store generation, epoch and
raw local Config pin. A saved absent Inspect guard establishes correspondence
only: first Edit must establish current absence again before local conditional
publication. A competing registration after that read remains subject to the
existing catalog/fixed-slot arbitration; the GET supplies no reservation or
upstream-success claim.

An exact-ID 404 alone proves neither absent key nor free slot. Missing bootstrap,
partial/invalid/unavailable observations, stale pins and a known mapping whose
content is not received remain Joining/unavailable, without an editable guard or
empty seed. This path allocates no IDs and creates, updates or deletes no Drive
data; it introduces no OAuth flow, grant/resource creation, mode transition,
ordinary fallback, Config rewrite or service action. Existing separately qualified
credential refresh retains its original bounded authorization contract. Explicit
local Edit supplies the original selected transaction; the existing Worker alone
owns catalog/content publication and adoption.

Established selected Inspect/Edit remain local-first/offline with their exact
current domain/configuration pins. Original Status checks local original receipt
and result correspondence without a network prerequisite. Neither acquires an
unconditional provider-read dependency from the first-absence exception.

### One-shot preference report profile

The implemented command keeps the accepted fixed stdin selector and request
fields in the Manager contract. Its version1 response carries `report_version`,
`operation` (inspect/edit/status), `status`, `disposition` and
`runtime_activation: unverified`. Inspect includes `guard` and `view` only after
current admission. Edit/Status preserve the valid original `guard`,
`original_operation` and compact `patch_sha256` for correspondence; Status never
includes a view or private patch text. No response claims running activation or
remote application.

`ok/read-only` is an admitted inspection. `ok/no-change` describes exact raw
declaration equality without a fabricated receipt. `ok/local-committed` verifies
a local original selected transaction, with upstream application still unverified.
Joining/not-admitted has no editable inspection guard. Changed admission conditions
produce conflict/not-dispatched; unavailable unknown remains uncertain after a
possible edit. Busy, unsupported and invalid-input refusals retain their ordinary
meanings. No client may infer a receipt from matching effective values.

Original Status traverses the bounded accepted local chain, requires an explicit
Initialize or Commit (never a received Activate), checks the exact predecessor
selection/revision for Commit and the original Store generation, then verifies
the local actor, operation and unchanged guard/patch/result-bound revision recipe
against original raw records. This needs no current mode permit, configuration
hash equality or provider access and creates no second operation index.

Established selected Inspect/Edit construct no provider adapter. First absence
alone lazily constructs the qualified adapter under current mode/domain custody
and refreshes only root/catalog observations, with one original sixty-second
deadline and conservative read allowance. Each observation is charged before
I/O for its account-identity response, two metadata responses and bounded 64KiB
descriptor; exhaustion cannot prove absence. Existing qualified token refresh
retains its separate bounded authorization contract. Local Config/checkpoint and
selected-original reads share the same allowance. The domain gate remains held
while Store mutexes are released for GETs; no command allocates/uploads provider
data. Raw Config is rechecked at conditional publication and output handoff.

The production qualification factory remains sealed. Actual executable evidence
therefore covers supported parsing/refusal and original Status; the private test
HTTP adapter covers positive Inspect/Edit admission, crash and correspondence.
These evidence categories do not establish live provider qualification or complete
the Manager's real editable-command parity gate.

### Effective selected Writer consumer implementation

The bounded consumer increment connects the actual selected Writer command,
not a renderer setting or a saved guard, to the same qualified preference
admission used above. Capture the exact raw Config and a selected preference token
or privately established absence, and derive the allowed effective Config from
those bytes. Historical original recovery stays read-only before new-work policy
and model credentials. Other runtime settings remain local. No Config rewrite,
new provider sender, serialized permit or operation index follows.

A private request-scoped preference snapshot joins Writer and any selected memory
catalog/aggregate admission in the existing ordered gate set. Recheck all current
pins immediately around the synchronous model handoff and the actual result
transaction. Existing OpenAI owned-request submission remains the only transport.
An internal guarded-handoff seam wraps the owned request submission, then releases
domain gates before waiting for its response. Progress and result checks may
cancel/refuse stale inputs; they must not reacquire a gate recursively from an
already locked callback. Unsupported model adapters refuse the guarded path.

One original monotonic lifetime covers the 60-second admission window, the
existing supported model wait of at most 90 seconds and a bounded 60-second
completion window. The model handoff is single-use and must occur inside the
original admission window; waiting for a healthy response does not renew it.
Reserve the finite preference read allowances once from a single charged parent:
full admission, handoff and completion validation each keep their own allowance,
while periodic cancellation checks use a separate finite raw-Config/current-header
allowance sized for the complete 210-second cadence. Dropping an allowance or
calling progress cannot replenish it. Cheap progress checks issue no token and
never replace complete object/history verification at the real handoff or result.
Generated text without an actual guarded owned submission cannot be published.

The result route uses the existing joined selected Writer publication, adding the
same preference admission and locked verification alongside selected memory pins.
An equal display value or a newer snapshot cannot authorize completion for an
older request. Mode/group/binding, raw Config, Store generation and the captured
selection/absence must still match. Provider qualification remains sealed in
production and the current executable/Manager evidence retains its previous
limits. Reader and remaining memory/research consumers remain separate unfinished
work. Reader has multiple model submissions and needs its own coherent request
lifetime and custody; the single-submission Writer snapshot is not a ready Reader
implementation.

### Installed resident Reader input

The [selected Reader input contract](selected-reader-resident-input.md) defines the
installed source-only constructor, registered document admission, one atomic
Prepared publication and the effective preference lifetime through Generated.
