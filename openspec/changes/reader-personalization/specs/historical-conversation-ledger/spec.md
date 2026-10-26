## MODIFIED Requirements

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

