# Manager current-producer bundle consumption

## Purpose
Keep the bounded Manager bundle consumer compatible with the current producer identity contract while preserving resource qualification and delivery boundaries.

## Requirements

### Requirement: Current producer identity in called verification
The existing Manager bundle consumer SHALL use the unchanged, hash-qualified current producer identity validator through its existing bounded verifier and fixed package inventory. It SHALL NOT require obsolete producer modules, copy a release engine into a new consumer engine, or execute downloaded code. Exact source bytes SHALL be checked before loading the selected trusted helper.

#### Scenario: Current-only runtime resources
- **WHEN** a supported consumer or packaged host verifies actual current-producer ZIP fixtures with only the selected qualified helper present
- **THEN** verified tag/source/manifest/embedded identity agrees without policy/coordinator files or new installation/update authority.

#### Scenario: Selected helper changes
- **WHEN** selected helper bytes are absent or differ from their qualified source identity
- **THEN** verification refuses before that helper can execute or publish a successful receipt.

### Requirement: Preserve consumer and delivery boundaries
The replacement SHALL preserve all existing bounded input, source/artifact, ZIP/path, cancellation/receipt and nonexecution checks. Desktop resources SHALL contain only the fixed selected helper for this dependency. Fixture, live release, native and cumulative parent evidence SHALL remain distinct.

#### Scenario: Consumer dependency is reconciled
- **WHEN** the dependency replacement is qualified and packaged
- **THEN** existing called host/UI behavior and ineligibility flags remain, affected controls pass, stale legacy dependency resources are excluded, and unfinished foundation/physical/provider/native/updater gates stay open.
