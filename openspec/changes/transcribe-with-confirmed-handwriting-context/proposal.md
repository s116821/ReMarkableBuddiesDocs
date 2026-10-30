# Explicit handwriting transcription with selected confirmed examples

## Why
Confirmed sample/text retention is delivered, but no shared recognition operation consumes those examples. Reader analysis and Writer generation currently do not use this domain. Add a bounded explicitly invoked transcription provider as a reusable seam before automatic product hooks. This is a proposed increment, not a statement of improved recognition.

## What changes
- Extend the existing provider-independent notebook OCR seam with selected examples and a one-shot transcription operation and exclusive `--handwriting-transcription` CLI using an admitted target PNG and zero to three explicitly selected correction revisions.
- Read one owned local snapshot, validate every selected example and its retained image, then send a fixed transcription task with clearly labeled example data through the existing LLMEngine transport.
- Return an unverified normalized historical page or explicit unreadability with exact captured provenance, bounded failure/attempt facts and ownership through actual output.
- Exercise real Store/CLI and captured engine payloads, cancellation/failure boundaries, and representative new live-model cases before delivery.

## Scope
No new persisted domain, inferred confirmation, automatic collection/application, training, accuracy promise, notebook schema allocation, native/SDK hook or selected sync. No Reader/Writer runtime route is silently activated. They may later call this shared provider under their own reviewed source/ownership contracts. Existing recognition paths remain unchanged in this increment.

## Delivery
Keep this Docs PR open through paired Rust implementation, meaningful executed checks, independent review, canonical sync/archive and normal Docs-first delivery. This is not a planning-only merge. Broader shared integration and efficacy remain open.

Source basis: current shared-handwriting requirements; delivered confirmed-handwriting-records capability; direct Source6e33bfd inspection of handwriting, existing retrieval/notebook normalization, Reader orchestration, Writer and LLMEngine; open Source PR/branch inventory found no matching correction-context work. Design choices below are proposals.
