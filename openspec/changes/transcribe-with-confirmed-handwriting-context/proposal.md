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

## Explicit partial-transcription v2 review scope

Extend this same operation only for a request with version 2 and the exact
partial-transcription policy. Its separate prompt and result schema preserve
visible uncertainty without making a partial report a normalized source or
confirmation. The default notebook normalizer and v1 operation keep their
existing wire bytes and whole-page policy. The [v2 precode](partial-v2-review.md)
is pending implementation acceptance. The spent r2 recognition result stays
NOT MET and no fresh provider execution is admitted by this change.

## Explicit mathematical layout policy

Add an opt-in `partial-math-transcription` policy within the existing v2 envelope.
Its general layout addendum and distinct profile identity request unambiguous
LaTeX for readable mathematics while preserving existing policies and schemas.
The [prospective contract](math-layout-profile.md) records the partial-span
representation limit and required regressions. This is not an accuracy claim or
permission to reinterpret either failed mathematical comparison.

## Explicit structured mathematical transcription

Add a separate version 3 `structured-math-transcription` request and bounded
inert result to preserve known mathematical relationships around unknown child
expressions. The [structured contract](structured-math-contract.md) defines the
strict MathML-role subset, compatibility, provenance and unchanged recognition
gate. This does not establish that the recognizer can identify those structures
or correct its observed relation-symbol errors.


## Standalone ready-notebook context admission (precode)

Extend only the existing handwriting-specific read-only admission so explicit
confirmed-context transcription can consume an already-ready ordinary notebook
format4 as well as its existing legacy family. Reuse the existing correction
store, exact-revision capture and report-held ownership; do not introduce a new
provider, persistence schema or lifetime. Readiness, local recovery, selection
history and absent/LocalOnly mode must be validated without mutation.

This is proposed storage/admission work, not an implemented or qualified result.
Automatic Reader/Writer consumption still requires a separately reviewed
same-Store handoff; the standalone command must not be installed as that runtime
path. Recognition quality and all unfinished delivery gates remain unchanged.


## Reviewed runtime integration successor (proposed)

Extend this same active change with [the concrete runtime precode](runtime-integration-contract.md).
Its scope supersedes the standalone-only exclusion solely for the specified ordinary
Reader/Writer receiving chain: explicit enabled active profile, deterministic bounded
confirmed-record selection, exact same-Store capture, Reader two-pass payloads,
Writer source-image normalization and distinct explicit correction intent. Disabled
retains current behavior; no native Writer ingress or implicit Refine confirmation.
No new Store/domain/retrieval framework or model/device execution. Independent
precode acceptance precedes source edits; learning efficacy remains unproved.
