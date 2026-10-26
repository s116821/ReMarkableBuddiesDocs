# Reader personalization after verified recognition

## Why

REM-53's accepted configuration maintenance and Manager editor save an optional preference, but the actual Reader currently never consumes it. Subject memory is optional and cannot be a prerequisite for a simple preference.

## What Changes

- Consume the accepted immutable personalization snapshot at ordinary Reader startup, preserving restart-required configuration semantics.
- Apply an enabled nonempty preference only to an answer request after independent transcription verification, separately from recognition, source images, subject memory and the persisted question.
- Generate one contextual answer when either personalization or usable subject memory applies. Preserve the existing default provider sequence when neither applies.
- Exercise the real workflow through offline simulator cases and representative authorized live-provider checks before merge.

## Scope

Reader receiving behavior only. Writer, conversational routing, gesture presets, live configuration reload, Manager active-state receipts, selected sync, native integration and whole REM-53 completion remain separate unfinished work. Reuse the accepted configuration implementation from Rust PR39 at 6254092cbcc7b9fb5ba7c116567fe8ccda373788; do not create a competing schema or maintenance CLI.

## Impact

Rust startup, receiving answer context and simulator inputs/assertions. Central Docs owns this change. Current Reader policy remains authoritative for source safety and output framing; preferences cannot change permissions or transcription.
