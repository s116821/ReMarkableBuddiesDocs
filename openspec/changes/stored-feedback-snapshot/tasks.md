## Pre-implementation review

- [x] Read current REM-40 requirements and all32 accessible timestamped comments and inspect existing catalog/Ledger/Store/mode boundaries.
- [x] Independently accept the exact three-source-path scope, snapshot/custody/refusal behavior and inherited scan-cost limit before implementation.

## Implementation and verification

- [x] Implement the stored receiver using existing ordinary custody/domain snapshot validation and static catalog, with no new storage schema or runtime wiring.
- [x] Add actual Store/Ledger reopen, secrecy, identity, explicit-ID malformed/foreign-head capture, pre-inspection conflict/tombstone/schema/mode refusal, unsupported-completed refusal, 1024-byte serialization and later-turn historical-stability controls; retain original failed evidence.
- [ ] Run focused tests, formatting/strict Clippy and required exact-head source/Docs CI; read current reviews/bot feedback.
- [ ] Obtain independent implementation/preservation acceptance and publish exact paired evidence/limits.

## Coordinated delivery

- [ ] Sync only accepted stored-feedback requirements and archive this completed change, preserving all unrelated active/archive and held work.
- [ ] Obtain final paired review and normal Docs-first/source delivery; keep broader pending/native/runtime/REM-40 acceptance open.
