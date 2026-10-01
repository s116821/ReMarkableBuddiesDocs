# Reader persistence seam — proposed, awaiting exact review

This additive plan implements tasks3.1–3.3 and4.4 in the active REM37 change.
It does not qualify SDK acquisition, page binding or native completion. The current
Rustb4bee21 persistence checkpoint has an independently reproduced derivative
geometry validation defect; fix that before consuming its historical SDK DTO.

## Acquisition states

DeviceBackend supplies an explicit acquisition result alongside the captured Frame.
One state carries a complete SDK-owned CapturedBatch, retaining its original identity,
qualification, parent and derivative order. Another state explicitly declares a
legacy acquisition with identity and qualification unavailable. An attempted SDK
capture that fails, returns unknown identity or lacks required facts is a refusal,
never an implicit fallback to the legacy state. Backends opt into legacy acquisition
explicitly; tests can supply clearly labelled SDK synthetic batches.

Legacy evidence uses a separate Buddy historical container with absent identity and
qualification. It cannot inhabit SourceObservation or SDK facts, generate a page UUID,
or establish a native binding. Persist the exact overview and each detail actually
submitted, preserving their original order. Retain an acquisition parent whenever
provided; if a legacy backend supplies none, record that absence explicitly. Do not
claim sibling derivation or original acquisition pixels from overview alone.

This proposes a coordinated change to SDK capture-contract.md's present restriction
that identity-free diagnostic pixels cannot be associated with a conversation.
That restriction remains authoritative until the SDK owner accepts an amendment
distinguishing a Buddy-owned explicitly unbound legacy run from an SDK-qualified
source association. No SDK SourceObservation, live guard or binding follows from
such a run. Implementation of this proposed state waits for that exact agreement.

## Preparation and provider use

Orchestrator retains the shared Ledger created from startup's existing Arc<Store>.
Capture once through Workflow's guarded device seam. Freeze the returned original
image bytes, validate and commit a Prepared user turn plus linked evidence/media
under full root heads before adding any images to the provider. Storage failure
returns before provider execution, navigation or typing. Legacy runs allocate an
explicitly unbound conversation; matching images or headers never adopt old pages.
SDK-qualified page lookup remains a separate required capability.

Retrieve that prepared batch through the ledger for proposal and verification.
Both requests submit identical original bytes in identical order; base64 transport
does not reencode images. Preserve current prompts and progress callbacks. Any
future provider-specific image processing must produce a recorded derivative before
submission. Retrying an acknowledged preparation reuses its original operation,
turn and stored bytes; restart does not automatically dispatch interrupted attempts.

## Outcomes and authority

Prepared turns are excluded from visible context. A request becomes Interpreted only
after independent transcription verification. The answer remains Generated until
the device seam supplies a separately qualified output receipt containing exact
verified text and current native facts. render_answer returning Ok is insufficient:
it also returns Ok for absent or invalid successors. Provider/device errors and
cancellation retain explicit terminal facts; uncertain effects become
ReconcileRequired and are never automatically repeated. Existing process-local
undo ownership and request retirement guards remain intact.

Historical unbound context remains useful for inspection without page-revisit or
native-binding guarantees. SDK-dependent operations refuse unavailable or synthetic
qualification. This plan does not retrofit legacy verification into SDK receipts.

## Verification and remaining design work

Use the actual Orchestrator and recording LLMEngine with a real temporary Store.
Assert proposal/verification bytes equal ledger retrieval; test a backend whose
later detail query changes to prove no second acquisition, and storage failures
with zero provider calls/navigation/typing. Verify original source state remains
unchanged. Cover provider failure, transcription disagreement, no successor,
invalid successor, cancellation, output uncertainty and restart without effect replay.

Before implementation, exact review must settle the unbound evidence schema, bounded
legacy acquisition descriptors, conversation selection/resume seam, output-result
type and responsibility for terminal recording when storage itself fails. SDK owns
acquisition and native receipt meaning; Buddy owns ledger/container and orchestration.
Native smoke, release builds and canonical sync/archive remain separate open gates.

Source basis: current Reader/Workflow/DeviceBackend code, accepted REM37 tasks and
SDK boundaries, independent review finding, and coordinator's current semantic
direction. Proposed API shapes are inference until exact review accepts them.
