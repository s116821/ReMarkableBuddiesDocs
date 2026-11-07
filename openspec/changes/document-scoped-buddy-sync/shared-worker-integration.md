# Selected publication, recovery and adoption integration precode

Status: successor r2, proposed source integration, awaiting acceptance before code.
This successor preserves the original ef149155 candidate and resolves protocol
review db02c677 and domain review 2e03d6af on REM-52. The choices below are concrete
implementation contracts, not implemented APIs or executed provider evidence.
Source basis is Buddy `72ddbe5557222947f6a85167a7cb58c3601cb0e5` and central
Docs `a1f446b8c4857e4f17726a0cb40ed62b8048b71a`. This amendment advances the
active shared-sync feature; it is not a planning-only prerequisite delivery,
inspection utility, new synchronization engine or live-provider qualification.

## Current interfaces and concrete conflicts

1. `storage/sync.rs::Worker::{google,start}` constructs the legacy `SyncEngine`,
   which acquires `LegacyPublisherLease` and publishes ordinary manifests.
   `main.rs` calls it only on ExistingReader. No selected sender/adopter consumes
   selected-outbox journals. Reusing that loop unchanged cannot implement group
   selection and must not send an explicit LocalOnly store merely because legacy
   Config.sync.enabled is true. Route modes before opening a credential file.
2. Existing `Store::{prepare_selected_attempt,current_selected_attempt,
   selected_attempt_inventory,inspect_selected_attempt,withdraw_selected_attempt}`
   preserve original selection, request, actor and mode epoch. They do not prove
   an agreed remote base/slot or authorize network handoff. `Pending` is not proof
   of never-submitted; a crash can happen after request submission.
3. `GoogleDrive::{prepare_slot,create_or_read_slot,observe_prepared_slot}` already
   checks the original application/account/group and immutable descriptor.
   `SlotObservation` proves pointer/hash bytes, not domain validity or parentage.
   The descriptor has no implemented schema and there is no agreed root/catalog
   bootstrap. An allocated ID by itself is not an agreed commit slot. In addition,
   observe_prepared_slot requires a remotely staged candidate; a passive receiver
   has none. Add the narrow read-only agreed-binding seam below, rather than
   manufacture an upload or weaken PreparedSlot.
4. `SelectedAdmission::{with_current,initialize,activate}` shares a domain gate
   for one Store/group/key even across replacement bindings. It is the correct
   admission order, but `activate` accepts a raw SelectionChange and does not
   derive or validate unresolved local intent retention. Add the real receiving
   adapter, not a caller-supplied boolean saying the winner is safe.
5. Subject-memory `Registration.genesis_sha256` is the hash of a LOCAL
   SelectionTransaction; `Aggregate::project` compares it to local accepted
   lineage. SelectionTransaction contains store/aggregate generation IDs. It
   cannot be copied unchanged as a portable remote genesis and match a second
   Store. Keep this local invariant. The proposed bridge below maps validated
   portable genesis to a new receiver-local registration rather than weakening
   that comparison or minting a remote live token.
6. Current mixed conversation/memory projection has a real document key:
   `memory::catalog::document_key(document)`. Global memory uses
   `Owner::GlobalFact { key }` and its existing record UUID. Do not replace these
   with per-turn IDs or a new generic key recipe. Handwriting is currently guarded
   by OrdinaryModeLease/LocalDomainLease. Portable preferences are raw Config
   projections, with no configuration Namespace in storage. Their selected
   producers/adopters are genuinely absent, not already covered by these APIs.
7. `selection::prepare_generation` explicitly refuses notebook format4; notebook
   readiness/capabilities and its ordinary producer reject nonlocal publication.
   Leaving this unchanged would omit current product data. The compatibility stage
   below is REQUIRED in the same feature before claiming a usable notebook sync
   route; the deferred inspection-only format4 observer remains closed.

## One connected product path

Use the existing Worker wake/cancel/backoff owner with mutually exclusive legacy
and selected engines; do not launch a second loop for the same Store. A selected
step is consumed by the real runtime route, not only another test. A qualified
host test supplies an explicit test transport context to that same step; no test
context is loadable through product configuration or renderer input.

Mode routing precedes credential access: absent mode preserves existing legacy
compatibility, explicit LocalOnly launches no publisher, SharedGroup uses the
selected route only after binding/root/domain admission, and an unimplemented
IsolatedBackup binding reports unavailable rather than reusing the legacy
collection or another device's namespace. Unprepared store families report their
actual refusal; notebook preparation below makes the supported selected notebook
route concrete. Do not broaden native runtime eligibility to reach this worker.

The first complete implementation path must connect existing selected Writer
publication and selected memory mutation to the Store wake, original-attempt
preparation, actual fixed-slot adapter and receiving domain adapter. It must also
accept a second Store's validated document/global-memory winner through the same
path. Low-level helper tests alone are insufficient. Handwriting and preference
adapters remain explicit tasks in the parent; their absence cannot be called
whole-feature completion or silently omitted from backup completeness.

## Agreed identity and bounded wire contract

Reuse fixed-ID metadata pointers and existing immutable object upload/download,
serde validation, file atomics, original outbox and content-addressed media. No
new database, distributed lease, mutable shared-head update, expiry protocol,
third-party sync service or dependency is proposed.

Proposed closed immutable root body: schema1, group UUID, protocol identifier,
provider/account/application binding digest, selected profile identity, and the
first catalog slot ID. The explicit provider root ID plus body digest is group
identity; display labels and listing order are not. Root publication is itself
one fixed metadata pointer at root_id, referring to the exact staged root body.
Use a protocol-defined root scope digest derived from group and the root role;
the catalog and domain roles have distinct validated bindings. The root body
includes its first catalog slot but not a self-referential digest. Its exact bytes'
digest is the portable root-body identity carried by later descriptors. Root
creation uses prepare_slot/create_or_read_slot after the control ordering below;
joining uses the agreed-slot read without a candidate. Retry only the original
root ID/body. A SharedGroup mode receipt records local intent, not remote existence
or publication readiness. Report Joining until the exact root/catalog/content and
receiving readiness are verified. A new empty Store never replaces remote data.

### Explicit first-root control and allocation ordering

Extend the existing hardwired mode maintenance dispatch with a separate
`--sync-mode-operation create-group --sync-mode-input -` operation. Keep current
Choose/Inspect behavior local and credential-free. CreateGroup takes a strict
bounded request containing original operation UUID, expected actor/mode token,
explicit group, binding digest and profile; no caller-supplied credential text,
root ID or live token. It runs only under existing Store/process custody with the
service/legacy publisher stopped, Config.sync.enabled false, a prepared supported
family, and absent/LocalOnly mode. Unsupported or unqualified context refuses
before credentials. A qualified binding is supplied by the maintained protected
provider context, not this JSON or a test fixture. Existing Drive authorize checks
must agree with its configured collection/group, account and application; do not
rewrite credential collection or widen authorization to make allocation succeed.

Reuse `sync/state.json` and its atomic save/load owner for this selected branch.
Extend the currently strict State with an optional versioned selected checkpoint
(default absent, omitted for unchanged legacy serialization); preserve legacy
fields and refuse conflicting/corrupt selected provenance rather than reset it.
The single Worker/maintenance Store owner serializes checkpoint publication. Keep
control, receive and staging entries in that bounded branch, not new general-purpose
journal files; original outbound custody still belongs solely to the outbox.

Persist the original control request/fingerprint and actor/source-generation pins
in a bounded versioned control entry in this existing private worker checkpoint.
Acquire OrdinaryModeLease with the original current token, recheck the exact
qualified binding, call existing authorize/allocate for nonpublishing generated
IDs, and durably append each returned ID under that same original control. This
lease admits ID allocation only for the explicit control; it grants no group or
content publication. No domain or Store mutex spans these HTTP requests. An ID
returned just before a crash but never persisted is unused; no remote object has
been created, so it can be abandoned. Restart resumes the same control and keeps
all persisted IDs. Before any upload/create, persist the complete root_id,
root-descriptor ID, first catalog slot and exact root body/fingerprint.

Release OrdinaryModeLease, revalidate the original actor/source-generation pins,
request fingerprint and mode token, then call
set_sync_mode(expected, original control operation, exact SharedGroup choice).
Other leases produce Busy; a raced choice produces Conflict. Do not refresh the
expected token automatically. Mode replay returns history, so re-read the current
mode and require the exact receipt epoch/group/root/binding before obtaining
SyncModeLease. A historical receipt grants no network continuation. Only then
stage the root descriptor and create/read root_id under this shared lease and
original control custody. The current mode/binding is rechecked at the actual
create boundary; group bootstrap does not borrow a document admission token.

Crashes after IDs but before mode leave a resumable local control and unused IDs;
after mode but before root leave Joining and resume the exact selected receipt;
after uncertain root create verify/retry only the original pointer/body under the
still-current shared epoch. A changed mode/binding stops creation and retains the
original record for diagnosis. No background LocalOnly or legacy worker creates
a group, and neither allocation nor local mode selection proves remote readiness.

After verifying its original root pointer, the creating control stages/persists one
original empty-catalog descriptor and successor at the root's first catalog slot,
then uses the same current shared-lease/fixed-ID create-or-read discipline. Persist
its exact IDs/body before send; uncertain retry never changes that initial catalog.
If a valid catalog is already present, validate/adopt it rather than overwrite it.
This explicit bootstrap control is the only initial empty-catalog producer. A
pull-only joiner with an absent catalog remains Joining and never synthesizes a
catalog upload. Root creation alone therefore cannot be misreported as complete
group bootstrap, and an existing nonempty catalog cannot be replaced by emptiness.

The catalog is a chain through the same fixed-slot primitive, mapping stable
scope keys to typed domain owner and ONE portable genesis slot. Its descriptor
contains its accepted predecessor digest and next pre-generated catalog slot.
Same-key races adopt the accepted mapping. A different-key registration may build
an additive new catalog candidate from the applied catalog, preserving every
existing mapping; this is catalog-set extension, never rebase of losing user
content. Bound its inventory using existing domain/MAX_ITEMS limits and reject
conflicting owner or genesis mappings. Group bootstrap state is not inferred from
the local SubjectMemory catalog.

Proposed closed commit descriptor (at most existing64KiB): schema1, group/root
body digest, typed scope/key, accepted remote base digest, original slot ID,
operation UUID, actor UUID, immutable manifest provider ID plus ObjectRef, and
next pre-generated slot ID. The original slot is obtained ONLY from the accepted
root/catalog/genesis or predecessor descriptor. A candidate chooses a successor
ID before adjudication; only the winning descriptor's successor becomes agreed.
Do not put local SelectionToken, store generation, credentials or live permits in
portable descriptors. Remote manifest uses existing Manifest and exact original
record ObjectRefs; do not reserialize envelopes to generate substitute hashes.

Manifest/object discovery may reuse existing bounded tagged-object inventory to
locate immutable content. A tag/listing is only a locator: verify account/group,
size/hash and complete referenced closure. Root/catalog/commit choice always uses
its exact agreed ID, never the first listed filename. Object/manifest metadata
and record/media checks share one receiving budget (existing4096 items/8MiB
metadata ceilings, existing media policy/caps). Missing promised media or budget
exhaustion prevents complete activation; explicit policy omissions remain typed
and visibly incomplete-media, preserving local source evidence.

## Read-only agreed-slot observation

Add `GoogleDrive::observe_agreed_slot(&SlotBinding)` for an already agreed root,
catalog or domain slot, called only under current qualified mode/binding custody.
Reuse SlotBinding validation, authorize(group), exact-ID metadata,
SlotPointer::from_metadata and slot_descriptor (including the existing 64KiB
descriptor bound, exact appProperties, object tag and digest checks). Factor their
common read path; do not duplicate or loosen these validators. Return a typed
AgreedSlotObservation with Absent, Invalid(reason) or Present(pointer, verified
descriptor bytes); transport/auth/unavailable remain typed errors. Absent denotes
the exact ID's not-visible/404 result under that context, not proof that no commit
exists, no hidden permission issue, or that a replacement slot is permitted.
Trashed/wrong-binding/malformed metadata and corrupt/missing referenced descriptor
are Invalid rather than absence. Classify HTTP/auth via structured TransportFailure
status and explicit validation variants, never error-message substring matching.
No candidate-match field exists in this result.

Keep existing PreparedSlot and SlotObservation candidate semantics. Its
observe_prepared_slot and create_or_read_slot share the new internal read path,
but calculate Same/Different only against their actual prepared pointer and
original descriptor reference. A joiner needs no local descriptor, upload session,
outbound attempt or synthetic candidate. Following the root/catalog/accepted
descriptor's exact next slot is a real Worker pull step. An absent next slot leaves
the last validated applied head unchanged; an absent initial root/genesis keeps
Joining, and invalid occupied slots keep recovery-required. Neither branch creates
content just to observe. GET-only tests record no allocate/upload/create/update/
delete request for passive join/recovery, including absent and invalid paths.

## Durable publication and recovery

1. Under current mode and domain admission, capture a real Store-minted selected
   snapshot and a domain-validated complete scope. Check existing pending attempts
   before preparing another. A stale or uncertain original cannot be bypassed by
   allocating a new operation, descriptor, slot or mode epoch.
2. Stage/hash immutable objects and descriptor with existing upload/session
   primitives. Persist provider object IDs before their first possible upload;
   reuse the existing worker checkpoint for staging progress, not another intent
   journal. Hold the original mode/binding lease for staging requests, but do network staging
   outside Store mutex and domain gate. Changed mode
   or selected token may leave retained unreferenced staging, never a commit.
3. Persist SelectedAttemptRequest with the original descriptor ObjectRef and
   already-agreed slot. After preparation, every ambiguous crash is potentially
   submitted. Reconstruction enumerates that exact original journal, not a fresh
   snapshot relabeled as the old operation.
4. Acquire the existing SyncModeLease. Require its group/root/binding and original
   epoch, recheck current application/account qualification and original prepared
   descriptor, then enter SelectedAdmission::with_current. Inside the gate call
   current_selected_attempt at the actual send boundary and execute the single
   synchronous create_or_read_slot. No Store mutex spans HTTP. Hold the domain
   gate through the entire synchronous call because the current API exposes no
   earlier reliable submission boundary. Keep existing per-request timeouts and
   cancellation; clamp requests to one proposed60s monotonic step deadline, never
   renew that deadline during retries or response observation. Long object staging
   is not performed under this gate. Mode changes wait for the actual lease.
5. Recovery first reconstructs the original outbox, immutable staging and exact
   prepared request; never relabel a fresh snapshot as the original. There are
   two distinct branches:
   - If original selection, Store generation, mode epoch, root and provider binding
     remain current, restore prepare_slot from original staged IDs/bytes and retry
     create_or_read_slot at the SAME fixed ID under the actual mode/domain handoff
     in step4. This is the permitted idempotent retry both after uncertain send and
     after a crash before the first create. A preliminary missing observation is
     not required and is not the authority: current original request plus current
     admission is. The exact operation, descriptor bytes/IDs and successor remain
     unchanged. If staged descriptor is temporarily unavailable, restore only its
     exact original staging when currently admitted; do not invent a descriptor.
   - If local selection/generation is stale, NO create is admitted. Observe the
     original agreed SlotBinding through the read-only seam, even if the original
     candidate descriptor cannot be prepared, and compare to the journal only if
     a validated candidate exists. Preserve/reconcile unknown outcome. A changed
     mode epoch/account/application/root stops even that old-namespace network
     work; historical custody is not authority to contact the old namespace.
   Both branches refuse alternate-slot/operation/rebase bypass. A local edit
   after durable preparation and before send must force the stale observe-only
   branch. Missing/404/unavailable/invalid evidence remains pending or recovery-
   required; it never independently proves freedom. Repeat steps use fresh bounded
   deadlines/backoff but never reset an in-progress step's monotonic deadline.
6. A verified different pointer is only a candidate winner. Validate descriptor
   schema, root/group/key, exact accepted base/original slot, chain, complete
   manifest/typed ownership and media before classifying it as authoritative.
   Wrong-base, foreign scope, malformed or incomplete data refuses adoption.
7. Fetch/validate into bounded staging without Store mutex or admission. Reacquire
   current mode/domain gates, revalidate all current pins and local intent state,
   and activate once as below. Network never runs while the Store mutex is held.
8. Use the receiving original-operation custody below for BOTH outbound-winner
   recovery and passive pull/first join. Its exact local activation/Initialize
   receipt binds the request fingerprint and applied remote accepted_base. Only
   after receiving readiness and receipt verification retire any associated
   original outbound attempt using existing withdrawal semantics; passive receive
   has no outbound attempt to retire. Withdrawal alone is not remote proof. Crash
   after activation is reconciled from the exact local receipt, without create or
   reapply. A stale original never mints a successor or rebases its content. Only a
   genuinely new domain edit after an applied ready winner may produce a candidate.

### Passive pull and first-join receiving custody

Use one bounded versioned receiving entry in the existing private worker checkpoint,
not a fabricated SelectedAttemptRequest or a second general journal. Before local
Initialize/Activate, atomically persist a ReceiveRequest with a fresh original local
operation UUID, local actor/Store generation, current mode epoch/group/root/binding,
typed scope/key, remote predecessor/slot/pointer/descriptor digest and complete
closure/media fingerprint, and historical expected local selection pins (Store and
aggregate generation, selection digest, accepted-base digest and binding) or an
explicit absent scope. These saved conditional pins are not a deserialized live
SelectionToken: obtain the current token from Store and compare every saved pin
again inside actual admission. Include origin Passive or
OutboundAttempt(original UUID); outbound identity
is an optional correlation, never a prerequisite for receiving. Replays with the
same operation must match the full fingerprint. Bound entries/bytes with the
existing checkpoint/Store ceilings and refuse overflow without dropping custody.
The activation operation is this persisted receiver-local UUID; it does not derive
from a nonexistent outgoing attempt and never imports the remote operation UUID
as local admission. The exact local receipt supplies the resulting local ancestry.

Fetch/validate immutable bytes outside locks. Reacquire SyncModeLease and one
ordered set of domain/catalog gates, then revalidate mode/binding, expected local
pins, remote chain and local intent before Initialize for absent scope or Activate
for an existing scope. The domain adapter checks absence while holding the same
gate; it cannot overwrite a raced local genesis. For mixed genesis, receiving
readiness below also applies. A remote descriptor digest alone is never authority.

After a crash, resolve the persisted receive operation using existing selected_receipt
before allocating another local operation. If its exact Initialize/Activate receipt
already exists, verify scope/accepted_base/requested membership and saved closure
fingerprint, recover that receipt and finish the original registration/checkpoint/
status publication. Do not activate again, resend a candidate or create an outbound
intent. A stale mode may expose historical diagnostic evidence, but may not claim
current readiness or mutate a new namespace. If no receipt exists, resume only when
the saved pins remain current; otherwise keep that receive visibly superseded/
recovery-required and make no silent refresh of its precondition. Subsequent pulls
start from the verified applied remote base, not an uncommitted status file.

Tests must drive the existing Worker with two real Stores for empty first join,
passive update with no local edit/outbox, and abrupt exit after receipt but before
checkpoint/health publication. Verify exact operation replay, one local activation,
new local identity, no outgoing intent and zero remote create/allocation requests.

## Domain adoption and actual handoff ordering

Add one domain-owned `adopt_shared_winner` receiving seam adjacent to
SelectedAdmission, consuming a non-constructible validated winner value minted
only by the actual worker's complete verification. Its data is historical, not
native permission. Under the same gate, recheck expected token, run strict
conversation/mixed-memory ownership and source-reference closure, and derive
retention from the actual current snapshot/original intents. Retain the complete
losing selected manifest plus prior retained closure where necessary, including
unresolved admitted receipts, source/evidence and required local media. Apply
winner and retention in ONE existing activate_selected transaction. Refuse if
combined bounds cannot preserve evidence. Imported receipts cannot release local
uncertainty or implement SourceAdmission/SettlementVerification.

The chosen fail-closed overlap rule applies to EITHER own or competing winner:
if its selected membership contains an exact still-unresolved locally admitted
receipt, preserve the original durable evidence and report committed-not-applied.
Do not activate merely to advance status, create a successor, or claim that
settle_retained resolves an active-plus-retained receipt. That API requires
exclusive retention. Resume only after genuine local proof settles the original;
an active-intent transition would require a separately reviewed seam and is not
promised here. When the unresolved original is exclusively retained and the winner
does not contain it, activation can preserve the original full closure and keep
the conflicting local-admission fence until genuine settlement.

Update reader_uncertainty.rs rather than merge winner and losing heads into one
strict causal graph. Validate the active winner and EACH exact retained original
manifest independently with its original pinned references. Same-record sibling
revisions across those closures are valid historical alternatives, not two active
heads. Build the local uncertainty fence from verified LOCAL original Commit/
predecessor lineage using recover_original and its exact generation/base/receipt
checks. A validated imported receipt/pending pair with foreign lineage is historical
data and grants no effect, release or resume authority; it is not a fabricated
local pending operation. Foreign classification requires validated receiving
provenance, not simply failure to find a local receipt. Missing/ambiguous purported
local lineage, malformed pairs and uncertain ownership remain blocked. Apply the
same rule to Reader, selected Writer and receiving send/admission checks; no union
projection or remote receipt may bypass a genuine local unresolved fence.

Real-Store tests include same-record active/retained sibling revisions together
with a valid foreign pending pair, a missing/ambiguous local lineage refusal,
own AND competing exact-local-receipt overlap (committed-not-applied), and exclusive
retention with genuine local settlement. Neither a remote pair nor activation
alone clears local uncertainty.

Use existing SelectedAdmission gate ordering for document and global memory;
where receiving genesis also registers local memory membership, use the existing
ordered with_gates mechanism. Do not reacquire participating gates recursively.
Model/request completion and backend handoffs keep their existing current-token
validation; an earlier check outside the gate is not a permit. A recording backend
can prove stale dispatch is refused; no production native adapter is minted.

For subject-memory genesis, preserve the remote manifest/fact bytes. After remote
catalog/owner/genesis validation, initialize the receiver's local selected scope
and mint its OWN Registration using the resulting local genesis operation/hash.
Then publish the exact receiver-local catalog mapping. The local catalog is a
receiving index, not remote agreed bootstrap; never send its replacement local
genesis hash as remote group identity. Existing Aggregate::project checks stay strict.

Before publishing a mixed document's local Initialize, persist its pending ReceiveRequest
as a staged mixed scope, including the original local genesis operation and exact
input fingerprint. The current local catalog Registration is the readiness witness:
it must match that scope's exact receiver-local Initialize operation/hash and owner.
Every affected current product path (SelectedAdmission::with_current_store, selected
Writer, Worker capture/send/pull and SelectedMemory) must require this mapping for
a staged mixed scope before treating it as ready/current. Merely hiding it through
SelectedMemory is insufficient: raw selected reads already expose initialized data.
Low-level storage snapshots remain historical bytes, not product readiness. Ordinary
memory-only catalog semantics remain unchanged; remote ancestry remains separate.

Under mode lease -> one ordered same-Store/group/binding catalog+document gate set
-> Store operation, validate both captured pins and the original staged receipt.
Factor a narrow locked registration publication from register_selection; do NOT
call its public read_extra/pins.guard path while already holding those gates.
Discovery may occur outside this set, followed by re-read/revalidation inside it.
After initialization a crash may leave a staged unregistered scope, but all product
paths refuse readiness until that exact registration exists. On restart recover
the saved Initialize receipt/hash (including a crash before checkpoint update),
validate the exact staged input, and resume the same locked registration. After
registration but before status update the mapping itself proves readiness when
verified against the original receipt; no reinitialization or fresh foreign token.
Tests must attempt actual SelectedAdmission, Writer and Worker access between each
boundary, not only SelectedMemory reads. Do not rewrite imported fact records.

Independent global memory scopes use their existing Owner key and domain decoder.
Handwriting needs a selected adapter over its existing profile/correction record
identity and confirmed-sample media; its ordinary lease must not simply be removed.
Portable preferences need an explicitly approved stable selected-record schema
and namespace over the existing allowlisted raw portable artifact. No such
Namespace exists now. Do not store Config text in SubjectMemory/Source, copy whole
Config, auto-apply imported preferences to runtime, or silently mark these domains
synchronized. These are concrete domain interface/coverage decisions for the
coordinating owner, not a request to reopen delivered export/import maintenance.

## Required notebook compatibility and production stage

This is a staged compatibility change inside this SAME worker feature, not a
new observer increment or a declaration that existing format4 already supports
sync. Proposed Store format5 composes notebook and live selected-generation
features. Review that exact format choice before implementation. Preserve old
format4 readers, archive/import/restore and their explicit refusals unchanged.
An old reader must reject format5, rather than silently ignore a new marker.

- Prepare format5 under existing unique Store/maintenance custody, with no active
  Writer/export/model/domain or publisher lease. Reuse current generation staging,
  verified object copying, recovery and final CURRENT publication. Validate source
  identity, contract and every record/media reference before publication. Keep the
  original actor for an existing installation and create a fresh LOCAL generation;
  receiving into a replacement installation keeps that installation's fresh actor.
  Never adopt another Store's owner/generation/lock files. Capture an explicit
  original preparation operation, bound to actor, exact source generation and
  target format/group, so interruption resumes only that preparation, not a
  different group or empty replacement. Recheck all pins before CURRENT and verify
  the complete target after CURRENT before reconciling readiness/capabilities.
- Stage the compound notebook+selection contract/markers, exact immutable objects,
  typed closure and fresh local selection metadata BEFORE the single CURRENT
  switch. Use an explicit owned completion marker/contract the current recovery
  already validates; do not rely on a capability file alone. Inject failure/abrupt
  exit before each marker, objects, contract, CURRENT and capabilities publication.
  Recovery exposes old complete format4 or complete prepared format5; an
  interrupted capability publication reports incomplete until reconciled. If
  CURRENT already names complete format5 but capabilities are stale, resume the
  exact original preparation via existing-only maintenance custody. Normal open
  checks readiness first and cannot be used as that repair path. No new Store,
  alternate actor or generic marker repair is admitted.
- Preserve exact Source3 ArchivedNormalizedSource, NotebookPlan and NotebookStage
  envelopes, revision IDs, parents, object hashes, canonical archive media and
  ordinary history. Use notebook_generation::records::validate_records_with_budget,
  archive.validate_bytes and existing plan/stage/source consistency checks; do not
  round-trip JSON to substitute bytes. Decode must be allowed only with the valid
  compound generation feature and domain schema guards, not globally opened for
  arbitrary future versions. Extend the canonical storage contract with the exact
  namespace/schema/feature matrix and unchanged older-reader refusal evidence.
  Invoke the SAME notebook semantic closure validation in selected writer and
  adopter before live publication as Store::recover invokes on reopen. Generic
  selection object/lineage checks alone do not provide live/recovery parity.
- Domain document membership for a validated ArchivedNormalizedSource is its
  explicit stable document UUID, after canonical archive identity/bytes match.
  Current selected projection deliberately does not assign that field to an
  owner; amend that exact branch after domain review. NotebookPlan and every Map/
  Reduce stage must trace exact source/plan revision, operation, chunk coverage,
  prepared/generated outcome and predecessor digests to that same aggregate.
  Missing/ambiguous document identity defers; no title, page index or conversation
  ID is a fallback. These are historical source IDs, not current native authority.
- Add a selected-aware notebook producer by reusing writer/notebook's validated
  archive, planner, payload and runner. Prepare and finish through the existing
  selected domain guard/commit, carrying the captured accepted base/generation
  across EACH Map/Reduce request and result. The actual command/runner prepares
  a stage BEFORE its model call: capture the selected gate/token at preparation,
  then hold actual admission through synchronous model submission and recheck at
  result commit. The ordinary runner's progress check alone cannot fence model
  handoff. A winner during the real producer
  makes late completion historical/unknown, never a new active stage or automatic
  replay. Imported NotebookStage/Receipt is not a model/native permit. Keep the
  ordinary format4 command path intact; this is a real selected producer consumed
  by the Worker, not a test-only Store initializer.
- The winning notebook closure activates with fresh receiving-local tokens and
  preserved unresolved local intent/media in one selected transaction. Source3
  canonical archive media needed for semantic validation cannot be treated as an
  optional thumbnail: if absent/omitted, keep observed candidate/unapplied/incomplete
  status and do not claim a domain-valid committed/applied winner. Optional media
  omission is reported separately and never deletes local source evidence.
- Scope includes storage/notebook_generation.rs and records.rs, selection feature/
  preparation/recovery, exact contract/capabilities, conversation/notebook and
  selected projection/adoption, writer/notebook command/runner and real maintained
  notebook fixtures. Inspect current runtime routing so selected notebook state is
  consumed by the product entry, with qualification unavailable before any provider
  access. Do not change native export/page admission, SDK profiles or unrelated
  ordinary maintenance. New format5 acceptance does not enable the deferred
  --inspect-selected-outbox format4 extension.

Required tests use the current product notebook producer to create Source3,
NotebookPlan and prepared/generated/failed stages with canonical media, then call
Worker publication/recovery and second-Store adoption. Cover multi-chunk notebooks,
noncanonical original envelope bytes, different documents, stale completion after
activation, missing canonical media, intentionally omitted optional media, invalid
stage ancestry, old-reader refusal and CURRENT/capability crash boundaries. Include
actual held domain/model/backend interlocks without a live LLM, Drive or tablet.
An implementation omitting this stage is not this candidate's completed route.

## Truthful status and qualification

Extend existing sync/health.json with a bounded versioned shared projection:
mode/group/root/binding digest, latest verified committed descriptor, applied
local generation/revision, pending original operations, offline/auth/contention/
replacement/recovery and media coverage. No secret/account ID/text/path dump.
Reconstruct applied/retired state from actual receipts/journal, not the last health
write. Committed-but-unapplied, stale intents, incomplete media and unsupported
domain/family cannot report Current/complete. Times are diagnostic only. Do not
reopen the delivered historical outbox CLI or deferred format4 observer.

Provider eligibility is a REAL remaining external input. The existing
[provider qualification contract](provider-qualification-contract.md) still needs
an explicitly authorized suitable account/OAuth application, protected grant/
operator, exact supported client registrations and private resource ledger. Prefer
an existing explicitly authorized binding with isolated disposable app-data
resources if its registration, visibility, namespace isolation and exact-ID cleanup
satisfy the contract. A new account/project is not mandatory: the earlier resource
contract's dedicated-account/project text is a proposal to reconcile at the later
concrete qualification selection, not authorization or a prerequisite to this source
work. Keep proposed32 files/2MiB/ten contention slots and exact-ID cleanup under
that separate selection. No connector permission substitutes for hidden app-data
application binding. Production selected publication remains unavailable until
actual binding/visibility/contention evidence and independent approval exist.
Source fixtures exercise the real worker with test-only HTTP inputs; they cannot
construct production qualification. No credentials/resource lookup occurs here.

Google's [create-file guide](https://developers.google.com/workspace/drive/api/guides/create-file)
documents pre-generated IDs and retry conflicts. Its
[app-data guide](https://developers.google.com/workspace/drive/api/guides/appdata)
describes application-specific hidden data and sharing restrictions. These support
the candidate protocol, not a claim that the complete contention/client matrix
has been exercised or qualified.

## Implementation footprint and evidence

- `storage/sync.rs`, `main.rs`: one worker/mode routing, current wake/cancel/backoff,
  qualification before credentials and status; preserve ordinary compatibility.
- New `storage/sync/selected.rs` and narrowly split protocol/tests if needed:
  connected root/catalog/publish/recover/adopt orchestration using existing
  Drive/Store primitives; no inspection-only CLI or generic workflow engine.
- `storage/drive.rs`, `drive/slot.rs`: narrow read-only agreed SlotBinding
  observation with typed absence/invalid and no fictitious candidate; share exact
  validators with existing PreparedSlot APIs. Nonsecret binding/deadline plumbing
  reuses HTTP/error/object methods; no arbitrary provider request interface.
- `mode_maintenance.rs`, existing main mode dispatch and worker checkpoint:
  explicit CreateGroup control, OrdinaryModeLease nonpublishing ID allocation,
  durable IDs before exact conditional shared-mode selection/root creation.
- Existing worker checkpoint: bounded original ReceiveRequest and staging/readiness
  reconciliation for passive join/pull, not synthetic outbound intents.
- `storage/selection/outbox.rs`, publication.rs: reuse existing custody/replay;
  alter only if receipt reconciliation needs an explicitly reviewed bounded seam.
- `conversation/admission.rs`, reader_uncertainty.rs, pending.rs/settlement.rs
  and selected.rs: ready-mixed-scope admission, domain-owned validation/retention,
  separate active/retained projections and verified local-original uncertainty.
  No raw activate bypass, new native operation schema or qualification; coordinate
  exact shared-file ownership before editing another author's retained drafts.
- `memory/selected.rs`, aggregate.rs/catalog.rs: portable-to-local genesis bridge
  and strict receiving validation, preserving current key/schema/genesis rules.
- Notebook format5 composition and actual selected notebook producer are required
  above, preserving format4 maintenance and the deferred observer.
- Handwriting/preference selected adapters require explicit domain contract
  decisions above; retain source refusals until coordinated, and parent tasks open.
- Real Store/HTTP integration tests must call selected Writer or memory mutation,
  Worker step and receiving adapter; existing lower-level fixtures are reused.
  Cover two clients same base, different documents/global facts, clock skew,
  original restart/lost ack, stale/changed binding, root/catalog races, invalid
  winner closure, media omission/corruption, atomic fault/kill recovery, retained
  local intent, active model/backend gate races and receipt-before-withdraw crash.
- Extend the maintained simulator only for these changed sync/admission effects;
  keep modeled evidence separate from actual provider/native evidence.

Successor review should verify the concrete agreed-read, CreateGroup ordering,
current-original retry/stale-observe split, passive receiving custody, exact mixed
readiness and local-original uncertainty rules above, plus notebook compatibility
and optional-domain key/schema coverage. Previously accepted storage/slot primitives
remain reused; their existing acceptance is not reopened. The coordinating maintainer owns
current-main reconciliation and shared-file ownership with domain authors before code.
Keep implementation, focused checks, as-built canonical sync and archival of only
completed named scope in the eventual linked Rust/Docs delivery. Do not merge
this precode alone or archive the unfinished parent to make the checklist green.
