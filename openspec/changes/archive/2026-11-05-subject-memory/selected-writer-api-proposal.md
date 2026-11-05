# Selected Writer: concrete API proposal for precode review

Status: proposed types/seams and test matrix, not implementation authorization.
Parent outline: [selected Writer contract](selected-writer-receiving-contract.md).
Ordinary source is b8cc818; exact joined Reader dependency is 550805a in
`composed-memory-integration_rust-rem37`. That dependency is reviewed and hosted
qualified, but is not present as a joined Writer API in the ordinary source.
Root must name its actual delivered/reconciled revision before implementation;
do not silently merge another lane's branch or duplicate its admission code.

## Proposed types (names provisional; existing domain formats retained)

```rust
struct SelectedWriterPrepare {
    operation: Uuid,                 // existing user-stage operation
    accepted: SelectionToken,        // exact pre-preparation selection
    root: IntentRecordRef,
    request: String,                 // verbatim new request
    source: SelectedWriterSource,
}
enum SelectedWriterSource {
    Generate { normalized: NormalizedTextSource },
    Refine { source: IntentRecordRef, draft: IntentRecordRef },
}
struct SelectedWriterPrepared {
    accepted: SelectionToken,        // acknowledged post-preparation token
    root: IntentRecordRef,
    user: IntentRecordRef,
    source: IntentRecordRef,
    refined_draft: Option<IntentRecordRef>,
    preparation_fingerprint: String,
}
enum SelectedWriterPreparation {
    Fresh { receipt: Receipt, prepared: SelectedWriterPrepared,
            model: SelectedWriterModelPermit },
    Historical { transaction: SelectionTransaction,
                 prepared: SelectedWriterPrepared },
}
struct SelectedWriterFinish {
    operation: Uuid,                 // deterministic finish-stage ID
    prepared: SelectedWriterPrepared,
    assistant: Uuid,                 // deterministic draft-stage ID
    outcome: Outcome,                // Generated / Failed / Canceled only
    text: Option<String>,
    updated_ms: u64,
}
enum SelectedWriterPublication {
    Published { publication: SelectionPublication,
                acknowledgment: SelectedWriterAcknowledgment },
    Historical { transaction: SelectionTransaction,
                 acknowledgment: SelectedWriterAcknowledgment },
}
```

SelectedWriterModelPermit is private, non-Clone/non-serializable, bound to the
receiving Store and preparation fingerprint; consumed once by the selected
receiver before model execution. It is not action authority or durable retry
permission. SelectedWriterPrepared contains verifiable references, not a claim
that a recovered preparation is fresh. Reuse existing Receipt, normalized source,
Turn and root records; these proposed structs need no new persistent record kind.
Do not expose ordinary WriterSelection from either publication variant.

## Preparation and model admission

Proposed `SelectedAdmission::prepare_writer(SelectedWriterPrepare)` validates
same Store/scope, accepted token and selected projection with complete objects,
then performs one selected commit of root/user/source/receipt. Fingerprint covers
version tag, original accepted-token evidence, exact root, request, source or
Refine source/draft references; deterministic revisions and receipt identity
allow reconstruction from the exact selected predecessor. Sequence and time
are assigned after replay comparison; persisted assigned time participates in
recovery, never a new retry clock.

Generate source identity must validate, belong to root conversation/new user and
the selected aggregate's document; reject a preexisting conflicting source ID.
Refine source must be exact current NormalizedTextSource in Namespace::Source;
draft must be exact current Assistant/Writer/Generated with the same root and
single source. Preserve the original source's owning user and set the new user's
correction_of to that exact draft. Validate projection.inspect/root ownership,
source document selection and chronological history; do not require Refine's
old source.turn to equal the new user. Never resolve these through ordinary
Store::value or Ledger::writer_turn, which would cross selected ownership.

Historical preparation returns no permit. Resolve an existing exact finish via
selected receipt/predecessor only; if absent, report interrupted/unresolved and
do not query memory, rerun the model, silently restart or publish a new failure.
Lost preparation acknowledgment therefore sacrifices automatic continuation,
not at-most-once model admission. No recovery mode manufactures a fresh permit.

The selected receiver builds exact history/source from the acknowledged
projection. After fresh preparation, selected memory query uses original request
and immutable document scope; before dispatch, check Writer currentness and
memory result integrity/currentness without consuming the final view. A failed
pre-model check stops. The final join remains necessary across model I/O.

## Finish seam and memory composition

Proposed internal `SelectedAdmission::finish_writer_joined(finish,
additional_admissions, verify_new)` follows Reader's recover-first/with_gates/
commit_selected shape. All participating handles use the same Store. Check
scope/token/root/user/source/refined-draft exact references and fresh assistant
absence under the complete ordered admission set. Commit new root, assistant
and Receipt; source/history are retained unchanged, with no fake guard rewrites.

Provider gets explicit `require_selected_writer` and
`publish_selected_writer(result, writer, finish)` methods with rejecting defaults.
SelectedMemory validates Store/group/binding, provider-instance/result digest,
catalog membership and all queried aggregate token/raw-head pins using its
existing cumulative budget. It delegates all handles to finish_writer_joined
once. The verifier uses only the supplied Store and never reacquires an admission.
New-attempt validation consumes the view even on refusal/failure/panic;
historical recovery runs before that callback and grants no new model/effect.
No memory query/result means no additional admission handles, but selected Writer
admission is still required. Enabled empty Complete results retain their selected
pins even though they add no prompt part. Usable Partial retains all queried pins.

Generated with enabled memory requires the joined result even when its text part
is empty. A typed pre-model retrieval failure/cancellation can publish only
Failed/Canceled under current Writer admission without memory pins, and cannot
carry generated text or create a selectable draft. If Writer selection is stale
or commit uncertain, report refusal/reconciliation instead of writing ordinary
failure evidence. This outcome distinction needs Root acceptance before coding.

Recovery must validate original operation/scope/predecessor token, fingerprint,
exact expected records and post-state projection, as Reader recover does. For
finish lost-ack recovery, reconstruct from the stored original assistant plus
preparation references and require exact deterministic record/receipt identity;
never accept caller-supplied replacement text or a receipt in another selection.
Historical results expose original text as history only, with no fresh local
WriterSelection/export/native permit. Provider failures never retry a model.

## Focused test matrix

| Area | Actual boundary and required result |
| --- | --- |
| Fresh Generate/Refine | Selected prep+finish, reopened Store, exact normalized source/history/correction; one model call per fresh request |
| Mode/optionality | Disabled/empty/Partial, explicit selected entry; ordinary selected refusal and ordinary 32-test behavior preserved |
| Projection/identity | Foreign Store/group/binding/profile; wrong root/source/draft owner or revision; missing objects; old source.turn in valid Refine |
| Joined replacement | Each Writer root/user/source/draft, catalog membership and every queried aggregate replaced between query/model/commit: no Generated write |
| Isolation/order | Other document/global records intact; duplicate and opposing admission sets; verifier cannot reacquire; bounded completion |
| View/budget | Foreign/tampered/consumed result, empty result pins, aggregate cumulative budget exhaustion; refuse without fallback |
| Prep recovery | Before commit / after commit lost ack / exact replay / changed request: no second permit/model; historical or unresolved only |
| Finish recovery | Before/after commit, lost ack, exact replay, changed text/token/receipt: exact historical recovery or refusal, never duplicate draft |
| Cancellation/failure | Before/after query/model; selected Failed/Canceled only when current; no generated capability or ordinary writes |
| Panic witness | Fresh join consumes view even when verifier panics; locks released; historical recovery does not reconsume |
| Authority | No native/export backend calls, no ordinary WriterSelection from Published/Historical; restored bindings remain historical |

Root review gates: exact dependency/reconciliation revision; these types and
recovery fingerprints; pre-model permit semantics; failure-only publication
without unavailable memory pins; projection ownership rules; focused tests.
Only after that review generate OpenSpec delta/tasks and implement in the
existing pair. No duplicate builds/cache/model runs for proposal review.

Source basis: exact current ordinary writer.rs and reviewed Reader selected
publication/SelectedMemory pins code, plus current REM24/37/23 comments.
API names, permit and outcome policy above are proposed, not existing behavior.
