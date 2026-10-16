# Historical conversation ledger

## Purpose

Provide ordinary schema-one historical conversation persistence over the shared Store without activating Reader/provider or selected/native behavior.

## Requirements

### Requirement: Atomic historical identity and chronology
The historical library SHALL persist stable conversation, turn, operation and correction identities with exact text and Reader/Writer mode facts using the existing Store. It SHALL publish atomic root/record/receipt transactions, compare complete observed head sets and return an identical historical acknowledgment for an identical retry without restoring deleted current state. Source: REM-37 durable identity, exact history and interruption requirements; historical 18e1a741.

#### Scenario: Reopen and retry
- **WHEN** mixed-mode turns are reopened or an operation is retried after a lost acknowledgment
- **THEN** exact chronology and text survive, identical retries do not duplicate records, and changed-content or stale-head writes refuse without partial publication.

#### Scenario: Incomplete or conflicting chronology
- **WHEN** relevant records conflict, allocated sequence coverage is missing, or a relevant schema is unknown
- **THEN** historical inspection refuses a falsely complete view while retaining stored evidence and unrelated legacy records.

### Requirement: Retain complete source evidence and historical capture facts
The library SHALL retain every ordered source image and required native-parent image with exact bytes, digest, dimensions, crop/transform and recorded observation provenance. It SHALL validate full image decoding and geometry before publication, distinguish unavailable required committed content from explicitly omitted imported media, and retain references after logical deletion. Source: REM-37 all-screenshots/provenance/coordinates requirements; accepted historical and SDK regressions.

#### Scenario: Prepared image readback
- **WHEN** a valid ordered image request or synthetic SDK capture is persisted and reopened
- **THEN** original and parent bytes, ordering and historical facts read back exactly without recapture or a native effect.

#### Scenario: Corruption and omission
- **WHEN** image decoding/geometry is invalid, required committed media is corrupt, or imported coverage explicitly omits media
- **THEN** invalid publication or complete-context claims refuse, while declared omission remains distinguishable from corruption and retained historical text remains inspectable where permitted.

### Requirement: Exact bounded historical context
The ordinary historical context API SHALL preserve exact eligible interpreted/completed turns and correction links, require explicit ranges when configured bounds are exceeded, and refuse unknown provider token bounds rather than summarize or truncate silently. Its bounded Store snapshots SHALL include relevant tombstones/conflicts and refuse oversized metadata instead of returning partial history. Source: REM-37 exact context requirement and accepted inspection/context regressions.

#### Scenario: Context exceeds limits
- **WHEN** a full historical view exceeds byte, turn or caller-counted token limits, or a provider limit is unknown
- **THEN** assembly returns an explicit refusal and preserves the full ledger for a deliberate range selection.

### Requirement: Lightweight export correlation and historical authority boundary
The library SHALL retain lightweight stable export markers and associations, resolve only an exact unique backend/scope/revision match, and expose ambiguity or uncertainty. Saved binding, capture, completion, retry and export facts SHALL NOT confer current native observation, effect permission or selected causal-view authority. Source: REM-37 lightweight export and historical-not-live requirements; current roadmap and later chronology.

#### Scenario: Ambiguous export discovery
- **WHEN** exact marker discovery finds conflicting native notes or incomplete scope/revision evidence
- **THEN** reconciliation reports conflict or uncertainty without creating a native note or selecting a winner.

### Requirement: Library delivery preserves runtime and feature boundaries
This increment SHALL expose the ordinary historical library without changing installed Reader/provider/native behavior, selected mode admission or legacy storage ownership. The exact SDK dependency SHALL disable default features for ordinary builds, enable mock only in test builds and preserve serialized historical SDK provenance. Source: bounded main delivery design and current SDK compatibility verification.

#### Scenario: Ordinary build versus mock tests
- **WHEN** ordinary non-test features and synthetic SDK tests are examined separately
- **THEN** ordinary consumers do not acquire mock/development-capture through this dependency, tests explicitly identify synthetic evidence, and historical SDK source markers retain their original meaning.
