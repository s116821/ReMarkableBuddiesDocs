# Stored feedback receiving design

## Current source basis

Actual delivered Reader source016d78a has the accepted ea13 tree. conversation_feedback::describe consumes an arbitrary caller-provided typed OutcomeFact and returns deterministic historical text. Ledger::inspect snapshots current heads, decodes roots/descendants, checks complete chronology, and additionally validates media. The feedback operation needs stored fact/turn metadata, not image bytes or current page evidence. Store::snapshot_heads_matching already has complete-result MAX_ITEMS and cumulative MAX_METADATA bounds, including conflicting heads and tombstones. Namespace::Conversation already contains roots, turns, receipts and outcome facts. No new persisted domain is needed.

## Why a receiving adapter is needed

A caller currently choosing Ledger::inspect followed by conversation_feedback::describe must open-code ordinary-mode custody, exact fact selection and fact-to-turn membership, while full inspect additionally reads/validates source media that a static feedback consumer does not need. Calling describe directly validates only nil IDs and outcome vocabulary, so a fabricated typed fact can look like stored history. The adapter centralizes this stored-identity boundary and exposes no arbitrary fact input. It does not add a new error catalog or persistence policy.

The actual intended receiving API is the public library function described below, usable by an ordinary domain caller after it already holds an existing Store/Ledger and exact operation-associated fact ID. This increment qualifies that callable receiving boundary through real Store tests. It adds no automatic runtime/Manager caller and does not claim the future owned Buddy-page presenter is implemented. Later callers must separately validate display/current binding and decide how older history is presented.

## Receiving API and custody

Proposed conversation::feedback::describe_stored(&Ledger, conversation UUID, fact UUID) returns Result<Option<FeedbackDescription>>. It accepts no arbitrary fact/record/JSON payload. Reject nil input before Store access. Obtain and retain the existing ordinary-mode lease from the Store's current mode token while reading; shared/isolated/recovery-selected state refuses. Do not initialize mode, open another Store, start sync or acquire native authority.

Require complete Store availability and capture one bounded current-head snapshot of matching Conversation-namespace records for that root using the existing Store API. Include conflicting and tombstoned heads in validation. Refuse unsupported schemas, including selected intent schema-two records in this ordinary receiving path. Reuse Ledger::inspect_snapshot for root/record/chronology decoding, including the existing live-root requirement. Resolve exactly the requested OutcomeFact and its existing turn, with original nonnil matching conversation/turn identities; ambiguous/type-reused/missing/deleted/foreign facts or turns refuse. This is a historical view at that read, with no expected-head or current-page write capability.

Use only metadata. Source/ExportAssociation payloads and image bytes are not fetched; no complete image, source binding, provider or native claim follows. Existing Store snapshot result bounds apply (MAX_ITEMS4096 and cumulative metadata MAX_METADATA8MiB). Output is zero or one static catalog description and has a small explicit serialized bound. This proposal does not upgrade the underlying Store index-filter traversal into a new global work/latency guarantee; record that inherited limit honestly and obtain review of its suitability before implementation.

## Historical versus pending semantics

Call the existing static catalog only after persisted identity validation. Completed fact returns None; unsupported states refuse. Preserve original fact identity and uncertainty precedence. A fact remains historical if a turn later advances: do not choose a latest fact by UUID/time, rewrite it as current, or infer that it has never been displayed. This API supplies a safe stored receiving seam for later owned presentation; it does not implement a pending queue or satisfy the broader pre-attempt/unassociated error requirement.

No return value contains request/answer/completion text, source images, diagnostics, credentials, native IDs or a presentation receipt. No file/ledger write, tombstone, cleanup, provider/network call, device input or rendered effect occurs. The existing catalog and all writers remain unchanged except the new child module's registration.

## Verification

Actual isolated Store/Ledger tests create persisted failures, cancellation and uncertainty using existing APIs; close/reopen before resolving exact facts. Cover two conversations, missing/foreign/type-reused/nil IDs, tombstoned/conflicted roots or descendants, unsupported schema, incomplete Store, missing/foreign turn, incomplete chronology and complete empty/non-error result. Include ordinary mode held through read and selected-mode refusal; preserve all before/after envelopes and files. Secret-looking turn/settlement text must not appear in serialized output. Repeated reads return identical historical identity/static text without duplicate records or claims about display. Include a later turn state test that preserves the explicitly selected historical fact semantics.

Run focused actual-store tests, formatting, strict Clippy and normal exact-head hosted checks; no new actual model or native run is required for this metadata-only receiving seam. Extend simulator only if integration changes its model; this API has no runtime/simulator dispatch, and exact Store regressions are its direct behavioral evidence.

## Open review points

Review ordinary lease/unsupported-schema behavior, precise fact-to-turn membership, tombstone and conflict handling, serialized output bound and inherited full-index scan cost before source implementation. If any required behavior needs an additional Ledger/storage implementation path or persistent schema, stop and revise the exact scope/precode first rather than bypass existing checks.
