# Generate and refine durable Writer drafts from supplied text

## Why

Prepared-note export is a bounded separate increment. Ordinary source exposes
normalized text, cancellable model transport and conversation storage, but no
Writer consumer combines them. Source records currently preserve images/captures
only, so normalized text cannot be persisted truthfully as an image fixture.

## What changes

- Add an explicit normalized-text source record to the existing Source domain,
  preserving input text/order/locations/digests without claiming original-byte,
  OCR or native qualification.
- Add bounded generation/refinement using the existing provider and Ledger,
  preserving verbatim requests and storing unrendered Writer drafts.
- Expose a bounded one-shot Writer command and explicit selected-draft preparation
  for the existing export consumer, with cancellation/retry/concurrency guards.
- Verify actual local HTTP/Store behavior and representative authorized live-model
  draft quality separately from unavailable native capture/rendering.

## Scope and exclusions

This increment consumes supplied normalized text. Page selection covers every
supplied unit for the named page; notebook selection covers every supplied unit
in order. Neither proves physical notebook completeness. Oversized source/history
refuses before dispatch; exhaustive large-notebook chunk/reduction remains open.
Drawing/image ingestion, handwritten guidance recognition, retrieval enrichment,
subject memory, native triggers/rendering and automatic direct-export sequencing
remain unfinished. Generation/refinement never sends Mem writes. REM-23 and the
integrated MVP gate remain open.

## Impact

Central writer-drafts, historical-conversation-ledger and shared-storage contracts;
Buddy ordinary library/command, Source2 decoder/Store contract and focused tests.
No Manager or SDK workflow files. Implementation follows the paired prepared-note
export delivery and preserves all native/selected WIP.
