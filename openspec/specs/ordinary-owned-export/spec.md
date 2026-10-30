# Ordinary owned-archive export producer

## Purpose
Deliberately publish only a format1 archive from an existing ordinary unconfigured/local-only Store, preserving the original source and private portable snapshot policy. The [contract](../../changes/archive/2026-10-20-export-ordinary-owned-archive/contract.md) fixes shapes, bounds and phase distinctions. Consumer UI, selected activation, provider/runtime/native and broad project qualification remain open.

## Requirements

### Requirement: Deliberate original-bound ordinary owned export
The producer SHALL prepare/apply only an existing ordinary unconfigured/local-only format1 Store to a new outside-owned-root destination under contract.md. It SHALL bind original config/path/actor/mode/generation/full history/raw optional snapshot/destination/target and reuse the existing export copy/publication writer under the same mutex and custody. Selected activation, initialization and provider/runtime/native authority SHALL remain outside this scope.

#### Scenario: Ordinary source and explicit new destination
- **WHEN** one compatible existing ordinary source is deliberately prepared and applied
- **THEN** only a fresh verified format1 archive is published, source bytes remain exact, and completeness/configuration inclusion remain explicit.

#### Scenario: Changed conditions or occupied alias
- **WHEN** original source/snapshot/mode/target changes or destination overlaps roots through case/canonical/reparse/occupied/race conditions
- **THEN** the producer refuses without refreshing conditions, overwriting a competitor, modifying source or routing to selected restore.

### Requirement: Private bounded portable archive output
All requests/reports SHALL obey exact objects, recursive duplicate/unknown refusal, limits and sanitized fixed summaries/hash-only intent. The exported portable snapshot SHALL never install configuration or include credential files/cache/binaries/native documents. Existing wire/library behavior SHALL be preserved.

#### Scenario: Private configuration and unrelated files
- **WHEN** export includes a supported portable snapshot and source contains credentials/cache/native-original sentinels
- **THEN** reports echo no arbitrary text/path/reference, only the existing portable owned inventory is copied, and every unrelated source file remains exact.

#### Scenario: Invalid shape or unsupported source
- **WHEN** strict shape/version/cap/content or current ordinary-mode admission fails
- **THEN** no initialization/repair/fallback/provider/runtime operation occurs and refusal is phase-honest.

### Requirement: Honest archive publication and later observation
Complete verified apply SHALL require exact desired marker and complete closure readback. Partial staging, marker-attempt uncertainty and consuming output failure SHALL retain destination/source without retry/cleanup. Status SHALL read only original destination/intent and prove current desired archive content, never historical publisher identity or runtime/native readiness.

#### Scenario: Marker attempt or output failure
- **WHEN** publication/readback/report may have failed after dispatch
- **THEN** the result remains unknown with no second report/replay/delete, preserving exact original conditions and custody until consuming output ends.

#### Scenario: Original destination status after missing apply
- **WHEN** explicit status observes the original desired complete archive or a missing/different/incomplete archive
- **THEN** it returns desired-archive-observed or unresolved with honest fixed data, no Store/source/config/provider probe and no historical settlement claim.
