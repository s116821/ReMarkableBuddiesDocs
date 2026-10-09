## Why

Reader currently retains only process-local undo ownership, so a restart cannot recover a canonical conversation or its original source images. REM-37 establishes the shared durable history and binding contract that Reader, Writer, page acquisition and later conversation rendering can consume without OCRing old replies.

## What Changes

- Propose the REM-52-coordinated existing Receipt/OutcomeFact schema-2 migration,
  selected-only projector and shared effect admission described in
  [selected-intent-migration.md](selected-intent-migration.md); preserve historical
  schema-1 inspection and keep unsupported native/shared effects refused.

- Add typed conversation/turn/source/export-association records on accepted REM-36 storage, with stable IDs, chronological order, explicit states and full-head conflicts.
- Persist every source image actually supplied to inference with exact bytes, hash, dimensions, parent/crop transform and source document/page/viewport identity before use; retain explicit missing-media recovery states.
- Integrate evidence and terminal turn recording into actual Reader orchestration while preserving REM-9 capture/input guards and current prompts/rendering; expose shared APIs for future Writer/routing consumers.
- Define idempotent binding CAS after REM-25 native receipts, restart reconciliation, exact history/context limits, explicit corrections and a portable lightweight export marker.
- Keep machine/preset instructions outside visible history, old native undo ownership separate from durable history, and legacy pages unadopted unless explicitly verified through the page-acquisition contract.
- Provide reference-aware logical deletion/export/inspection through shared storage, deterministic restart/conflict/interruption/media tests, and representative authorized native evidence for changed Reader capture/persistence.

## Capabilities

### New Capabilities
- `conversation-context`: durable domain schemas, bindings, source evidence, chronological/exact context, recovery and lightweight export association.

### Modified Capabilities
- `reader-analysis`: persist exact used source evidence before provider dispatch and terminal outcomes without changing recognition prompts.
- `reader-qa-history`: clarify that existing process-local restrictions govern native undo/redo eligibility, not the new durable ledger; keep all native mutation guards until REM-43.
- `local-simulator`: real storage-backed restart/history/media and operation failure regressions without pretending unimplemented Writer/UI behavior exists.
- `platform-runtime`: distinguish optional diagnostic image dumps from mandatory durable source evidence, and update the implemented boundary after accepted REM-36 without claiming future Writer UI/routing.

## Impact

Rust owns a new conversation module and scoped orchestration/capture/main integration consuming one shared Store handle. No new Buddy HTTP/RPC/admin service, database/root, release logic or second identity registry. REM-36 owns generic storage/sync; REM-25 owns native effects and its device-local journal; REM-38/39/43 own renderer/router/native history. Manager consumes shared file contracts later. This checkpoint changes central Docs only; canonical specs remain as-built until verified implementation delivery.

## Authority and delivery

Read the complete REM-37 description (updated September26 21:28:14UTC), its sole21:12:36 correlation comment, and full resumed roadmap. The resume supersedes historical planning-pause wording. Export identity is the portable metadata/title convention, not a separate architecture blocker. New REM-46 requires upstream Action release logic and remains separate. Base Docs e7fbdc44/Rust3df3b1e6 include accepted REM-9; inspected REM-36 API checkpoint7483087 is not yet accepted. No production implementation until accepted REM-36 plus independent exact-plan review. REM-25 binding interface is coordinated before either consumer implements it. One coordinator owns hardware. Stop/checkpoint at90% reported usage; no reset/credits. Full linked Docs/Rust delivery, Summary-only PRs, squash-only merges, no planning-only feature PR or premature archive. REM-35 owns1.0.
