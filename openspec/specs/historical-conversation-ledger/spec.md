# Historical conversation ledger

## Purpose

Provide ordinary schema-one historical conversation persistence over the shared Store without activating Reader/provider or selected/native behavior.

## Requirements

### Requirement: Atomic historical identity and chronology
The historical library SHALL persist stable conversation, turn, operation and correction identities with exact text and Reader/Writer mode facts using the existing Store. It SHALL publish atomic root/record/receipt transactions, compare complete observed head sets and return an identical historical acknowledgment for an identical retry without restoring deleted current state. Source: REM-37 durable identity, exact history and interruption requirements; historical 18e1a741. The fact-only outcome API SHALL additionally allow an ordinary interpreted Reader user turn with no completion evidence to record Failed with ProviderFailure or Canceled with Canceled, retaining exact verified text and all immutable facts. This narrow transition SHALL require the explicit corresponding reason and SHALL NOT permit reason-free advance, changed text, Writer transitions, selected/native admission, replayed effects or reconciliation bypass.

#### Scenario: Reopen and retry
- **WHEN** mixed-mode turns are reopened or an operation is retried after a lost acknowledgment
- **THEN** exact chronology and text survive, identical retries do not duplicate records, and changed-content or stale-head writes refuse without partial publication.

#### Scenario: Incomplete or conflicting chronology
- **WHEN** relevant records conflict, allocated sequence coverage is missing, or a relevant schema is unknown
- **THEN** historical inspection refuses a falsely complete view while retaining stored evidence and unrelated legacy records.

#### Scenario: Context fails after interpretation
- **WHEN** an ordinary Reader question was verified and persisted as interpreted, but contextual generation fails or progress is canceled before a draft/output
- **THEN** the existing atomic root/turn/outcome-fact transaction retains the exact question and records Failed/ProviderFailure or Canceled/Canceled without an assistant turn or effect permission.

#### Scenario: Narrow terminal reason and text guards
- **WHEN** the caller changes interpreted text, omits or changes the corresponding reason, requests another terminal transition or targets an interpreted Writer turn
- **THEN** this additional transition refuses with no partial record change, while previous transitions and reconciliation guards remain unchanged.

### Requirement: Retain complete source evidence and historical capture facts
The library SHALL retain every ordered source image and required native-parent
image with exact bytes, digest, dimensions, crop/transform and recorded observation
provenance. It SHALL also retain explicitly supplied normalized text as its own
immutable typed Source record with exact ordered text, locations, source and
normalized digests, and extractor revision; these SHALL NOT imply original-byte,
OCR or native qualification. It SHALL retain full image decoding and geometry
validation before publication, validate complete required content before
publication/readback, distinguish unavailable required committed content from
explicitly omitted imported media, and retain references after logical deletion.
Existing Source1 image/capture serialization SHALL remain unchanged; new
normalized-text Source records SHALL use explicit domain 2 with schema/shape
validation. Source: REM-37 all-screenshots/provenance/coordinates requirements;
accepted historical and SDK regressions; bounded REM-23 supplied-text consumer.

#### Scenario: Prepared image readback
- **WHEN** a valid ordered image request or synthetic SDK capture is persisted and reopened
- **THEN** original and parent bytes, ordering and historical facts read back exactly without recapture or a native effect.

#### Scenario: Corruption and omission
- **WHEN** image decoding/geometry is invalid, required committed content is corrupt, or imported coverage explicitly omits media
- **THEN** invalid publication or complete-context claims refuse, while declared omission remains distinguishable from corruption and retained historical text remains inspectable where permitted.

#### Scenario: Normalized text survives restart
- **WHEN** a Writer request with explicit normalized source text is persisted and reopened
- **THEN** exact supplied unit order, text, page/section locations and digest/revision facts remain available through its linked Source record without a synthetic image or native observation claim.

### Requirement: Exact bounded historical context
The ordinary historical context API SHALL preserve exact eligible interpreted/completed turns and correction links, require explicit ranges when configured bounds are exceeded, and refuse unknown provider token bounds rather than summarize or truncate silently. Its bounded Store snapshots SHALL include relevant tombstones/conflicts and refuse oversized metadata instead of returning partial history. Source: REM-37 exact context requirement and accepted inspection/context regressions.

#### Scenario: Context exceeds limits
- **WHEN** a full historical view exceeds byte, turn or caller-counted token limits, or a provider limit is unknown
- **THEN** assembly returns an explicit refusal and preserves the full ledger for a deliberate range selection.

### Requirement: Lightweight export correlation and historical authority boundary
The library SHALL retain lightweight stable export markers and associations,
resolve only an exact unique backend/scope/revision match, and expose ambiguity
or uncertainty. A stable association SHALL support distinct deliberate export
operations and changed source revisions after confirmed completion, retaining
each operation's immutable attempt facts, historical receipts and complete
expected-head checks. An uncertain attempt SHALL require reconciliation before
a new export cycle. A positively known no-send Canceled/Failed attempt MAY begin
a new deliberate effect UUID under current heads without replaying its old effect.
Older records SHALL remain readable without being promoted
into verified current remote-body or dispatch authority. Saved binding, capture,
completion, retry and export facts SHALL NOT confer current native observation,
effect permission or selected causal-view authority.
Source: REM-37 lightweight export and historical-not-live requirements; current roadmap and later chronology; prepared-note export increment.

#### Scenario: Ambiguous export discovery
- **WHEN** exact marker discovery finds conflicting native notes or incomplete scope/revision evidence
- **THEN** reconciliation reports conflict or uncertainty without creating a native note or selecting a winner.

#### Scenario: New revision preserves stable note identity
- **WHEN** a new export operation follows a confirmed completed attempt using current expected heads
- **THEN** it may advance source revision while retaining correlation/backend/source scope and verified native identity, and old operation retries still return their original historical acknowledgment.

#### Scenario: Prepared operation is replayed
- **WHEN** preparation is retried, won concurrently or committed with a lost acknowledgment
- **THEN** its historical result does not grant fresh dispatch, and the caller must reconcile the known external identity without resending the effect.

### Requirement: Library delivery preserves runtime and feature boundaries
This increment SHALL expose the ordinary historical library without changing installed Reader/provider/native behavior, selected mode admission or legacy storage ownership. The exact SDK dependency SHALL disable default features for ordinary builds, enable mock only in test builds and preserve serialized historical SDK provenance. Source: bounded main delivery design and current SDK compatibility verification.

#### Scenario: Ordinary build versus mock tests
- **WHEN** ordinary non-test features and synthetic SDK tests are examined separately
- **THEN** ordinary consumers do not acquire mock/development-capture through this dependency, tests explicitly identify synthetic evidence, and historical SDK source markers retain their original meaning.
