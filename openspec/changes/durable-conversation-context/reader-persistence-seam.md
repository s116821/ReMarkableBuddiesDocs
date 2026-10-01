# Reader persistence seam — proposed, awaiting exact review

This additive plan implements tasks3.1–3.3 and4.4 in the active REM37 change.
It does not qualify SDK acquisition, page binding or native completion. The current
Rust18e1a741 capture-persistence checkpoint fixes the independently reproduced
derivative geometry defect and has bounded independent Sol acceptance.

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

SDK amendment [1072e12bcfff8fabf3c64ca7bb7b1c8396e8967b](https://github.com/s116821/ReMarkableOpenSDK/commit/1072e12bcfff8fabf3c64ca7bb7b1c8396e8967b)
now permits this explicitly selected Buddy-only unbound legacy history. It preserves
refusal for failed SDK capture, absent native qualification and all output guard and
receipt requirements. Detailed consumer implementation remains subject to exact review.

Proposed Buddy legacy payload: schema1, evidence ID, conversation/turn IDs,
origin LegacyUnqualified, identity None, qualification None, acquisition-parent
descriptor Option, and an ordered list of actual provider-image descriptors
(Media, decoded dimensions, overview/detail role and provider ordinal). Require
explicit null for absent fields and refuse unknown fields/versions. Do not add
affine, crop or viewport provenance when the backend did not provide verified
descriptors. A supplied parent is retained as acquisition pixels without claiming
an SDK-qualified owner or derivation. Preserve the distinction from SDK Capture
records in context and retained-history APIs. Conversation UUIDs identify Buddy
records only and are never replacement document/page UUIDs.

Preparation bounds:1–15 provider images plus at most one acquisition parent,
32MiB encoded per image and64MiB encoded total, checked before staging; existing
8192-axis/32MiB full-image decoding limits still apply. Fail rather than truncate.
Apply ordinary root CAS, operation fingerprint/retry, integrity and retention rules.
These are consumer persistence bounds, not native compatibility or aggregate
process-memory guarantees.

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

The current backend can report NoOutput for absent/invalid successors or
SubmittedUnverified for a render that succeeds without a qualified SDK receipt.
Neither state becomes Completed. Commit the generated assistant draft before
navigation/output; once input may have occurred, missing verification leaves
ReconcileRequired. Record a no-output refusal as Failed with an explicit reason,
preserving the interpreted user turn. Proven no-effect failures may record
Failed/Canceled; ambiguous device errors retain uncertainty. Storage failure before
rendering prevents rendering. Failure after possible input leaves the precommitted
draft for explicit inspection and restart reconciliation, never automatic replay.

## Concrete consumer choices for review

Add a distinct `Record::LegacyCapture` in the Source namespace, linked from the
Prepared user's sources. Keep `Record::Capture` exclusively SDK historical facts.
Expose legacy evidence separately in context, inspection and retained-media APIs;
never construct ImageUse/SourceObservation from it. Descriptor role/ordinal and
encoded-byte digest determine provider ordering and retry fingerprints. Integrity
checks fully decode PNG/JPEG under existing bounds without reencoding them.

The backend explicitly selects acquisition kind before Workflow starts capture.
The trait default is unsupported; RealDevice and simulator declare legacy selection
explicitly, while SDK fixtures opt into the SDK branch. Workflow freezes overview
and detail bytes once within the existing request guard before ledger preparation.
Base64 details are decoded once to their exact original encoded bytes. Any error in
SDK acquisition or in legacy capture/details refuses before provider dispatch.
No branch attempts a second acquisition as error recovery.

Until qualified source/binding lookup exists, each legacy iteration creates a new
explicitly unbound conversation. It does not infer continuity from headers, OCR,
image equality or process-local history. Stored unbound history can be inspected
by its Buddy conversation ID after restart; automatic same-page resume remains an
open qualification gate. This bounded integration is not complete REM37 acceptance.
No historical turns are silently injected into a provider request; future resume
must use the existing explicit context budget/selection contract.

Add an explicit Reader output result: NoOutput(reason) or SubmittedUnverified.
Commit the assistant Generated draft before entering render_answer. Navigation
attempts are effects: record ReconcileRequired before entering rendering, then
retain it after a submitted output or ambiguous error. NoOutput is restricted to confirmed unchanged source or a verified return without
answer input; an unconfirmed return stays uncertain. A proven no-output result
can be separately recorded as a reconciled Failed revision; it cannot masquerade
as Completed. This requires an explicit fact-only reconciliation operation with
root/turn CAS, retained history and idempotent fingerprint, rather than widening
ordinary advance to replay effects. No runtime restart automatically reconciles
or dispatches these attempts. The renderer preserves existing request/undo guards.

If preparation or assistant-draft publication fails, propagate the storage error
and make zero subsequent provider/output calls. If terminal recording itself fails,
return a combined error and leave the previously durable Prepared/Generated or
ReconcileRequired facts intact. The caller cannot invent an acknowledged terminal
state; restart inspection reports the interrupted state for explicit reconciliation.

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
