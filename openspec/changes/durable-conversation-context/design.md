## Context

REM-37 supplies durable conversation context on accepted REM-36 storage. Current Reader orchestration captures an overview and derives detail images for proposal and independent verification; native undo ownership is process-local. REM-9 already guards capture, provider waits, navigation and keyboard output. REM-25 owns native page acquisition and its device-local recovery journal. Its static firmware inspection identifies a possible explicit page UUID argument but proves no runtime insertion or persistence semantics.

Authority is the complete REM-37 description and September 26 correlation clarification, plus the resumed roadmap. The public acceptance mapping accompanies this plan. The inspected REM-36 checkpoint is an interface candidate, not permission to begin implementation before independent review and dependency acceptance.

## Goals / Non-Goals

## October 1 authority and platform boundary

The current REM-37 description and comments remain applicable; October 1 REM-25/35/38/39/40 clarifications establish ReMarkableOpenSDK as the independent owner of hardware-facing capabilities and its own OpenSpec. Buddy/Manager integration requirements remain here. No SDK canonical API, firmware adapter or native implementation is defined by this change. SDK capabilities supply qualified current document/page identity, normalized capture/viewport provenance and verified native output/creation receipts. Buddy records those observations without inferring native success from a callback, elapsed time or model output. Unsupported or unqualified capability results fail closed at the native integration boundary. The existing DeviceBackend/simulator seam remains mockable; do not introduce new raw xochitl/evdev/model/firmware branches in conversation code. Existing legacy mechanics may be used only through that seam during incremental migration; their limits remain explicit. XOVI cannot be a production dependency.

The domain store, exact-image preparation, chronology/context, logical binding CAS and export association work can proceed on accepted REM-36 independently of native SDK qualification. Native Reader receipt/capture integration and hardware verification stay open until the required SDK contract is reviewed and qualified, with exact SDK revision/capability evidence recorded. No host fixture can close that gate. SDK operation journal and contract details are coordinated with its owner rather than duplicated into Buddy canonical specs.

Accepted dependency bases: Rust `ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`, Docs `8008389fa676d395401e6f28e049b47baa7b10ef`. Shared Store limits and existing API were accepted in REM-36; this change owns only the minimal bounded read-only namespace/head enumeration needed by the domain, preserving the one manifest authority.

**Goals:** exact shared Reader/Writer history, stable conversation/turn/page identities, retrievable original source images, explicit interrupted-operation states, restart/revisit lookup, safe binding CAS, lightweight export correlation and storage-backed regression evidence.

**Non-Goals:** implementing Writer UI, newest-first renderer, automatic page insertion, provider prompt redesign, restored native undo ownership, external export adapters, media garbage collection, release automation or 1.0 acceptance. These remain their named roadmap deliveries. Shared APIs are tested with both Buddy modes; simulated Writer calls are not native Writer evidence.

## Decisions

### 1. Typed records on the one shared Store

Use `src/conversation/` domain types over REM-36 envelopes and media objects. Do not add a database, second storage root or service. Conversation, turn and binding records use the Conversation namespace; source-use records use Source; export associations use ExportAssociation. Each payload carries a domain schema version and kind. Unknown versions permit inspection of the generic envelope but refuse domain mutation. Generic envelope revision and parent heads remain the conflict authority.

A conversation root holds stable conversation ID, creation/update timestamps, status, next sequence and binding reference. Separate bounded turn records avoid an ever-growing root payload. A turn has stable turn ID, conversation ID, exchange/operation ID, sequence, role, Buddy mode, lifecycle state, exact text when known, source-use references, optional correction target and timestamps. Wall clocks are descriptive; root-CAS-allocated sequence determines chronology. An explicit correction appends a new record referencing the original rather than replacing its words.

Commit sequence allocation, root revision, turn and associated source-use records atomically. Every operation supplies the complete expected head set; multihead conflict is surfaced rather than choosing the newest timestamp. Retries look up the same operation and verify an immutable request fingerprint. Identical retries return its recorded result; changed content under that ID is a conflict. Concurrent preparation must not reserve two sequences or fork silently. An operation that lost the CAS re-reads the winner before any side effect. Generic Store internals stay owned by REM-36.

REM-36's envelope `operation_id` is unique per envelope revision/content, not a shared transaction ID. Keep the domain exchange/request ID and immutable fingerprint in domain payloads; use distinct envelope operation/revision IDs for every participating record, preserving exact envelope bytes on generic retry. Domain fingerprint lookup precedes a new commit. Stream `stage_blob(ObjectRef, Read)` then commit descriptor references with an empty inline media map; only committed objects are visible through normal `open_object`. Validate each serialized envelope against 1 MiB, aggregate transaction record metadata against 8 MiB, required objects against 4096 and each media object against 256 MiB. These inspected limits are rechecked against accepted REM-36 before code. Oversized atomic operations fail explicitly rather than being silently split.

Alternative: serializing the whole transcript into one envelope is initially simple but exceeds record limits and rewrites unrelated history. Per-turn records with a small CAS root preserve bounded writes and explicit concurrency.

### 2. Save the actual inference images before using them

Prepare a reusable evidence batch from one guarded capture. Store the exact decoded image bytes whose encodings are submitted, including every overview and useful crop/detail used by either provider call. Each source-use entry records document/page ID, observed revision and page order fingerprint, capture/session/visit identity, pixel dimensions, orientation, viewport transform, normalized coordinates, image hash/MIME, purpose and ordinal. Derived images identify the immutable parent capture and crop rectangle/transform. Persist the parent capture when used to derive submitted images or determine an erasure region. Repeated use can share a content-addressed object while keeping separate provenance/use links.

Stage objects using REM-36 streaming APIs, then atomically commit a Prepared exchange and its evidence references before the first model request or source mutation. Reuse that exact prepared batch for proposal and verification, avoiding fresh independently generated crops. Check the REM-9 guard before and after storage work and each existing protected phase. A failed/oversized/corrupt evidence commit stops before model dispatch, navigation or erasure. A later page target creates new source-use records within the same conversation; it never changes earlier evidence.

Prepared user text is absent until interpretation is verified. Unverified recognition, model drafts and machine instructions do not masquerade as user-visible turns. Store diagnostics separately with sanitized error categories, not credentials or raw hidden prompts. Provider output may be retained as a generated draft, but becomes a completed visible assistant response only after the existing native persistence check proves the complete response. Partial or unknown native output becomes ReconcileRequired; failure/cancellation is retained without claiming a complete visible response.

Alternative: storing only filenames or recapturing after output loses exact evidence and fails after page changes. The extra local write is intentional; measure its native latency and preserve the guard throughout it.

### 3. Binding is an atomic logical association, not a native command

A canonical binding record has a deterministic logical identity from native document ID and Buddy page ID, independent of installation/Store actor identity. Freeze its encoding as UUIDv5 using the RFC URL namespace and UTF-8 name `urn:remarkable-buddies:binding:v1:<document-uuid>:<page-uuid>`, where each UUID is canonical lowercase hyphenated text. Device qualification belongs to the receipt, not this key. Thus reinstall/restore retains the same claim key and cannot create a second claim merely by changing installation identity. Copied documents that retain identical native IDs intentionally contend on the same logical claim; ambiguity fails closed. It contains the logical conversation association and qualified receipt reference. Atomically CAS this record and the conversation root; do not build a separate identity registry. Imported logical associations do not authorize native operations on another device. Fresh current-device qualification is required even if the same logical IDs exist there.

Initial acquisition is create-or-identical only: a conversation already bound to another live page refuses a new claim. A future page migration must atomically reconcile the old claim through an explicitly designed transition; it cannot overwrite the root reference and strand the old claim. Concurrent same-conversation/different-page acquisitions contend on the root CAS.

REM-25 owns Prepared, NativeCommitted, BindingCommitted and ReconcileRequired journal phases. `commit_binding` consumes its exact NativeCommitted receipt and expected full head sets. Required receipt fields include operation/conversation IDs, adapter/protocol/capability fingerprint, captured source document/page/revision/order/session/visit, intended target if supported, observed target document/page, exact expected post-insertion order, persisted revision and observation time. A bool, callback, aggregate idle or generic change signal is insufficient. Fresh renderer guards remain required after binding.

Check the immutable operation/receipt fingerprint before ordinary expected-head validation. An identical receipt after a lost acknowledgment returns the original commit acknowledgment even if the caller supplies its original stale heads or later turns advanced the root. This is historical acknowledgment only: return the current binding/root state alongside it; subsequent tombstone, reassignment or conflict never regains native-use authority through a retry. Different content under the same operation ID is a conflict. A new operation with conflicting target, order or head set refuses binding and leaves reconciliation to the same REM-25 journal. Receipt conversation/operation/device qualification and observed document/page must match the root and deterministic claim. If an adapter accepted a caller-assigned intended target UUID, any different observed target is ReconcileRequired, not an implicit rebind. Restart never automatically reruns native insertion, provider calls or export writes. The storage ledger is evidence, not a replay queue. Runtime page lookup uses verified identities, not header OCR. Legacy header-only pages remain explicitly unbound until REM-25 qualifies acquisition/adoption. Reader can record a legacy run with its observed target without silently creating a trusted binding.

Alternative: storing page IDs only in each conversation allows two conversations to claim one page without a shared CAS point. The deterministic binding record is a domain record in existing storage, not a new registry subsystem.

### 4. Exact chronology and explicit context bounds

Expose inspection, source-image retrieval and context assembly through the same APIs for Reader and Writer. Canonical completed user/assistant turns and corrections remain in ascending sequence; the later newest-first renderer receives a view and cannot rewrite storage order. Hidden presets, transport instructions and drafts are separate typed fields/records and excluded from visible history and default context.

Context assembly accepts an explicit caller budget and selection policy, returns the included turn/media IDs and exact text, and never silently truncates, summarizes or rewrites history. Enforce storage byte/object bounds separately from provider token limits. Provider-specific token accounting belongs to its adapter; an unknown or exceeded provider bound returns a typed explicit-choice-needed result rather than treating byte counts as tokens. Starting another conversation or an explicitly selected context range preserves the full original ledger. Missing media in a partial restore remains identified by hash and provenance; text inspection still works, but any image-dependent operation reports unavailable evidence rather than recapturing or substituting another image.

### 5. Lightweight portable export identity

Keep a stable export-correlation UUID and small ExportAssociation record containing conversation/native-note identity, requested scope and revision, operation ID, backend kind and outcome. Prefer backend metadata key `remarkable_buddies_export_id`; use exact title marker `[RMB:<uuid>]` only where metadata cannot survive the backend's supported round trip. REM-23 must confirm the adapter's round-trip behavior before external execution. The shared contract can be implemented and tested without an external account or a separate registry service.

Retries use the same marker and operation identity. Exactly one matching backend object may be associated after verification; multiple matches are a conflict. An unknown prior write with no discoverable match remains ReconcileRequired instead of blindly creating another note. No external export or delete is performed by this change.

### 6. Deletion and legacy coexistence

Explicit conversation deletion atomically tombstones its root and current binding using full-head checks; tombstone envelopes have null payload and no media descriptors. All ordinary conversation/context lookup and append APIs enforce root liveness, so retained descendant turns/source-use/export records are hidden from normal live views and cannot revive a deleted conversation. An explicit retained-history inspection can report those records and their evidence. This bounded transaction avoids promising an unbounded all-turn deletion or silently chunking atomicity. Conflict or limits refuse the operation without partial deletion. Shared objects remain retained while referenced by any live/conflicted record or retained revision. REM-36 currently has no destructive media collector; REM-37 therefore provides logical deletion and a reference-aware retained-media report, not a claim of immediate physical erasure. REM-42 owns later explicit garbage-collection policy. Deleting a ledger does not delete source documents or external notes.

No automatic OCR import or destructive rewrite of existing pages. Persisted context does not restore the process-local native undo transaction. Existing departure, new-iteration, restart, ownership and native-size/time guards remain until REM-43 changes them through its own delivery.

## Risks / Trade-offs

- Additional capture persistence latency and disk pressure -> streaming/content addressing, preflight bounds, measured native run and fail-before-side-effect behavior.
- Concurrent imported heads or duplicate page claims -> full-head CAS on root and deterministic binding record, explicit conflicts and no LWW.
- Crash after native output but before ledger acknowledgment -> ReconcileRequired with draft/evidence retained; no automatic repeated typing.
- Partial restores omit media -> exact missing hashes and bounded retrieval errors, no invented evidence.
- Native creation is not yet qualified -> receipt-based offline tests are labeled simulated; REM-25/38 integration remains open until actual native proof.
- Sensitive image retention -> use existing private Store permissions and explicit inspection/deletion controls; no logs or public fixtures containing personal captures.

## Migration Plan

After REM-36 acceptance and exact-plan review, implement domain schemas/APIs and tests, then integrate the shared Store handle into actual Reader capture/terminal recording. Preserve config defaults and source/navigation behavior. No old-page rewrite is needed. Unknown newer schemas fail closed for writes; rollback to an older application must not delete newer storage. Use REM-36 backup/restore contracts and document that rollback cannot replay interrupted effects. Verify native capture/persistence with a disposable authorized fixture and restore the original device state. Sync/archive only after every REM-37 gate is satisfied in the linked Docs/Rust delivery.

## Open Questions and Dependency Gates

Before code: confirm final REM-36 commit/CAS/media APIs and accepted limits; independently review this exact plan with REM-25 and coordinator. Before native binding: REM-25 must qualify the receipt and insertion/adoption operation. Before external export: REM-23 verifies marker preservation on its actual backend. Before complete native mixed-Buddy experience: REM-38/39 provide routing/rendering and Writer; domain tests here do not close their gates. These dependencies do not permit weakening automatic page creation or silently treating unbound legacy targets as trusted.
