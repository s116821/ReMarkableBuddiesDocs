# REM-37 integration proposal for REM-52

Status: proposed shared-path changes, not implemented. SCRAPPY-DOO owns REM-52 storage/transport work; Main owns the unfinished REM-37 domain and Reader workflow. This proposal follows acceptance of the integration contract at Docs `7e06d9f96f7fb037698b4b44a71ed2518e44ff06`. It requests owner review of the following concrete seams before either lane edits shared paths. Generic transport remains at Buddy `8d1f1512e39575e3ea162b062d5b4389df9daea5`; it does not activate these seams.

## Inspected source and gap

The inspected REM-37 source is `673c5781cd5d89a89d712b9d8253433c920dc37c`. Changes to that source require refreshing this mapping with Main before implementation.

- `src/conversation/mod.rs`: `Ledger::publish` commits root, domain records and operation receipt through `Store::commit`. `advance_fact` and `record_attempt_outcome` resolve current live root/turn heads before committing. Their existing causal checks do not pin a selected aggregate generation, and the outcome path cannot simply be reused for a late completion after replacement: it would resolve or mutate the newly active history.
- `src/conversation/types.rs`: `SourceObservation.document`, `ImageUse`, `BindingReceipt`, `CaptureEvidence`, `OutcomeFact` and the existing `Record` variants remain the domain schema. `Root` has no source-document field. Neither a conversation ID nor the legacy capture path supplies a qualified stable source-document key.
- `src/workflow/reader_attempt.rs`: `Attempt::prepare`, `interpret`, `generated` and `outcome` already persist captured evidence, generated drafts and unverified facts. `Attempt` currently has no aggregate generation/base pin. Its existing `ReconcileRequired` state is valuable evidence, not a generation admission guard.
- `src/workflow/orchestrator.rs`: Reader records OutputPending before `render_answer`; the latter can navigate and then type. The current qualified scope remains legacy output; SDK output is refused as NativeOutputUnavailable. No sync change may promote SDK/native output.
- `src/workflow/mod.rs`: actual backend calls occur in `navigate_to_next_page`, `navigate_to_previous_page`, `set_body_text_mode`, `render_text`, `render_qa`, `history_action` -> `DeviceBackend::history_mutate`, and `draw_symbol` -> `DeviceBackend::bitmap`. A guard around the orchestrator's preliminary check alone would leave a check-to-dispatch race at these calls. Imported history/receipts never authorize undo, redo or drawing.
- `src/storage/mod.rs`: `snapshot_heads_matching` takes one `inner` lock but reads the all-history causal index. `snapshot_revisions_matching` deliberately includes retained revisions. `publish` locks `inner`, persists objects and the commit manifest, then applies the index; it has BeforeObjects, AfterObjects, BeforeCommit and AfterCommit failure points. There is currently no selected-aggregate overlay or generation token.

## Proposed division of changes

Main owns domain decoding, projector reference closure, attempt pinning, operation admission and historical settlement semantics. SCRAPPY-DOO owns a domain-opaque selected storage view, guarded commit/activation primitives and sync coordination. Interface names below describe responsibilities; they are proposals, not existing APIs or permission to implement a second operation framework.

1. Add an opaque selected-view token and bounded snapshot primitive in `src/storage/mod.rs`. Under one store lock, capture selection identity, accepted base and generation together with opaque envelope references and media coverage. Preserve the existing all-history index for recovery; explicitly distinguish selected reads from retained evidence reads. The ordinary local-only/isolated-backup path retains its current behavior. Do not globally change the meaning of all-history import to mean shared winner activation.
2. Add a guarded selected commit and atomic winner activation under that same store lock. A commit checks the caller's captured base/generation at the actual durable publication boundary, in addition to current record-parent checks. Stage and validate before activation; atomically switch durable selection metadata only after the complete closure is available. Recovery must rebuild the selected view from that metadata, not every retained branch. A lost acknowledgement replays the same operation identity without bypassing the generation check or duplicating an active append.
3. Main adds a domain-owned projector adjacent to `Ledger::inspect`. It consumes one selected snapshot, decodes the existing Record variants, and enumerates opaque envelope references across all conversations belonging unambiguously to one SourceObservation.document. Include roots, turns, source uses, capture evidence, bindings, operation receipts and export associations, with their media descriptors and explicit coverage. Validate reference and chronology closure without reserializing a substitute domain model. Take record metadata from one pinned snapshot; open content-addressed media by those pinned immutable descriptors. Activation cannot change which revision or descriptor is being validated halfway through projection.
4. Main threads the captured selection token through Attempt preparation and every resulting durable mutation, including interpreted text, generated drafts, outcome facts, binding and export association. Head sets alone are insufficient. Writes with a stale token fail closed or enter the domain's existing historical reconciliation route; they do not rebase onto the new winner.
5. Main places admission at the actual workflow-to-device handoff. Admission and activation use the same domain guard, with lock order domain guard then store lock. Persist the existing operation intent/evidence and its pins before external handoff, recheck under the guard, and hold the guard through the actual backend submission. Do not hold the store mutex across network I/O or completion observation. For a synchronous backend with no separable submission/completion API, hold admission through the backend call rather than releasing it before effects; Main must review the resulting activation latency and any required backend split. A multi-step navigation/render sequence must revalidate at each subsequent handoff and stop after invalidation.
6. Activation preserves unresolved admitted intent, original request identity and required evidence/media in retained reconciliation storage outside the replaced active view. Main supplies a settlement path that addresses that original intent rather than calling advance_fact against new active heads. Late verified or uncertain results remain historical facts; unresolved settlement blocks conflicting admission for that aggregate. Imported receipts, wall-clock expiry or a sync success cannot clear that latch. Restart reconstructs the latch before admitting effects; no resume path automatically repeats native output.

## Owner decisions required before shared-path edits

The following API responsibilities are the precise next owner decision, not existing methods or accepted durable schemas:

- `selected_snapshot(scope, bound) -> (SelectionToken, opaque snapshot)`: store-minted, non-forgeable token pins the store generation, selected aggregate generation, accepted descriptor digest and selected scope/binding identity. The opaque snapshot contains exact envelope/object references plus media coverage; it is captured at one lock boundary. The aggregate generation is separate from the existing whole-store generation. No implicit current-head lookup replaces those references during later projection.
- `commit_selected(token, existing envelopes, media) -> commit receipt`: revalidate all token pins and causal parents at publication under the store lock. A stale token refuses even when record parents still match. Existing operation replay must remain scoped to its original selection, not become authorization to append to a replacement. Main holds the domain admission guard first where the commit participates in admission.
- `activate_selected(expected token, verified winner closure, retained unresolved closure) -> new token`: one durable local selection transaction covers both the selected opaque references and preserved unresolved-intent/evidence references. It must be crash-recoverable with old-or-complete-new semantics, maintain unrelated scopes, and refuse absent/corrupt required objects. Main supplies the validated unresolved closure while holding the shared admission guard; storage does not infer intent status from domain payloads.
- Main extends the existing OutputPending `OutcomeFact`/operation receipt path to associate the operation with those pins, original external request identity/payload fingerprint, qualified source/evidence references and settlement state. Proposed extension belongs in the existing domain journal, not a parallel storage operation schema. Main decides the compatible encoding/migration and exact request type; current OutcomeFact/Receipt fields do not already contain these facts. Imported facts cannot manufacture a locally admitted intent or native authority.
- `settle_retained(original intent references, original-request evidence)`: Main's historical settlement route targets the retained intent, not `advance_fact` resolving new active heads. Storage persists those new opaque historical facts without adding them to active selected membership or enqueueing them as a new shared document edit. Its exact receipt/index transaction and reconstruction of the unresolved admission latch require Main's journal decision before implementation.

The disconnected fixture slice may exercise explicit references, immutable media handles, all-history/selected separation and refusal boundaries in the real Store. It must not present a caller-supplied fixture token or reference list as implemented selected activation, domain closure, durable journal pins or native admission. SCRAPPY-DOO owns that isolated storage evidence; Main owns the domain extension and actual handoffs. No shared domain/workflow edit follows from this API proposal until owner agreement.

- Agree the selected-view/guarded-commit interface and which lane lands each shared file, with exact refreshed source heads. Domain guard ownership must work across every Ledger/workflow handle used by activation and admission; a fresh unrelated mutex per handle is insufficient.
- Main identifies the existing operation intent record and exact durable location for its aggregate pins and historical settlement. The inspected OutputPending/OutcomeFact path lacks these pins; this proposal does not assert that its current fields already provide them or mint a parallel journal schema.
- Agree how one durable selection transaction references immutable manifests and preserved unresolved intent/media, including recovery at each current storage failure point. An in-memory overlay or two independently durable writes is not accepted as atomic activation.
- Main defines and tests projector ownership for every supported Record variant. Missing, nil, ambiguous or multiple document identities remain visibly deferred; unknown schema is refused. Legacy records stay recoverable and cannot acquire shared document identity from titles, page order or conversation IDs.

## Required verification before integration acceptance

- Pause an operation after preliminary validation, activate a new winner, then release dispatch: the actual backend receives no stale effect. Exercise navigation, mode change, text/Q&A render, undo/redo `history_mutate` and bitmap submission, including a later step in an already-started sequence. Imported history/receipts cannot arm any of these effects.
- Admit and durably record an operation first, activate a winner, then deliver late success and late uncertainty: no new active append, no stale rebase, evidence/media retained, and conflicting admissions remain blocked until original-request reconciliation qualifies settlement. Include late uncertain history mutation and bitmap results; no replay, fallback drawing or repeated undo/redo follows from uncertainty.
- Inject activation during every durable mutation path. Generation and parent checks are evaluated at commit, and unrelated document/global keys remain unchanged. Concurrent handles share the admission ordering.
- Crash before/after object staging, before/after selection activation and after commit acknowledgement loss; reopen the store and prove exactly one complete selected generation plus preserved unresolved intent/media. Corrupt or missing required media refuses activation; intentional omission is reported distinctly.
- Project two conversations with one document from one consistent snapshot; replace selection during media reads and prove immutable reference pinning. Exercise receipts, bindings, exports, tombstones, source/capture closure and sequence validation. A record with conflicting owners, unknown variant or absent stable document is not silently assigned or dropped.
- Retain the existing local-only, isolated backup, REM-37 fact/reconciliation and generic adapter tests. Host interleavings do not qualify live Drive exclusivity, actual OAuth application visibility, native source identity or SDK/native output.

The first implementation slice after owner agreement should be bounded selected storage/projector fixtures with no worker or native activation. Actual admission/settlement integration follows only after Main's journal and backend seam decisions. Docs and code remain one unfinished delivery; no canonical as-built change or archival follows from accepting this proposal alone.


## Accepted storage implementation detail (owner agreement 5442770097)

The next bounded implementation keeps one authoritative per-scope selection JSON
transaction. It references the complete selected winner, retained opaque closure,
original request digest, prior selection digest and bounded history depth. Before
publishing its successor, the current transaction is durably archived by digest.
Only history reachable from the authoritative transaction counts as accepted;
unreferenced staging cannot authorize replay. Recovery validates that chain and
rebuilds all-history evidence separately from selected membership. Guarded writes
compare the private token and selected causal heads under the store lock at the
atomic metadata publication boundary. A repeat returns its original receipt and
original token only after matching the original parent/request; it does not append
or issue authority for the current replacement. A fresh selected snapshot is needed
for further mutations. Bootstrap is an explicit initialize operation requiring a
nonempty validated closure; snapshot absence supplies no implicit authority.

History count and combined metadata are bounded; saturation refuses further writes
rather than dropping replay evidence. Compaction is not implemented in this slice.
Required object corruption or incomplete lineage refuses reads/activation; explicit
media omission remains represented by coverage. Complete reference closures may
include ancestors, but their selected head set must be unambiguous. Storage remains
domain opaque and does not infer which retained facts settle an admitted intent.
Main must validate retained-intent preservation before invoking activation. Existing
backup/restore/migration paths refuse selected metadata until their portable policy
is implemented, preventing silent loss. No worker/native/provider activation follows.


Retained closures may share immutable ancestor/context references with the winner,
but each must contain historical evidence outside selected membership; retaining
only the active closure is refused. Separate selected/retained lists do not cause
the retained losing head to become active. Domain validation decides which opaque
references are unresolved intents and whether an activation preserves all of them.

The storage API is `initialize_selected(scope, SelectionChange, objects)`,
`activate_selected(token, SelectionChange, objects)` and
`commit_selected(token, operation, envelopes, media)`. `SelectionChange` carries
operation, accepted-base digest, selected manifest and retained manifests. Each
returns `SelectionPublication { transaction, token, replayed }`; replay returns the
original transaction/token, whose token is stale after replacement. Full closure
reads include ancestor envelopes; they require exactly one causal head per selected
record. The domain projector must use those pinned envelopes rather than resolve
all-history heads. No portable live token can be deserialized.


Main's coordinated storage boundary additionally admits domain schema2 only for
Namespace::Conversation; schema1 continues for every existing namespace. Unknown
versions and schema2 outside Conversation refuse commit/import/activation/recovery.
Storage payloads remain opaque: Main owns strict Receipt/OutcomeFact variant and
field validation, legacy migration and old-reader refusal evidence. This explicit
namespace gate is not generic future-version acceptance or native authority.


A read-only `selected_receipt(scope, operation)` recovers the original accepted
transaction after process restart without deserializing or minting a live token.
The domain owner compares original intent/request evidence; missing receipt is not
permission to publish or repeat a native effect. Existing mutation replay compares
the original live token/request when that caller still exists. After restart a
fresh snapshot can authorize a pending mutation only if Main independently verifies
its persisted intent pins still match; replacement cannot be bypassed by history.

A lifetime registration held by every enabled legacy SyncEngine serializes its
eligibility with selected publication under the store lock, without holding that
mutex during provider I/O. Existing active handles must stop/drop (or disable and
step) before initialization; an enabled legacy handle cannot be opened/re-enabled
on a selected store. This prevents the old all-history sync path from accidentally
publishing retained branches. A selected-aware coordinator remains unfinished.
