# Source request context

## Purpose

Assemble immutable ordinary historical Reader request context with explicit original-source association, fresh local retrieval and complete output budgets. This capability does not authorize selected/native effects or model dispatch.

## Requirements

### Requirement: Ordinary receiving preserves exact request context and explicit original association
The ordinary receiving API SHALL derive one immutable per-request frame from an
existing validated Ledger snapshot, preserving the interpreted Reader request,
eligible chronological history, correction/source identities and explicit range
verbatim. It SHALL validate an explicitly chosen existing original turn/source
relationship and independently supplied complete index key, or explicit no-source,
without modifying capture batches, creating a source registry, using a current
Buddy page as fallback or granting selected/native authority.

#### Scenario: Follow-up and changed target
- **WHEN** a follow-up retains its original reference or deliberately supplies another valid original reference and complete key
- **THEN** unchanged request/history and exact source provenance enter the frame, a fresh local Provider query can reach new passages anywhere in the selected source, and wrong-document or stale keys refuse.

#### Scenario: Explicit no-source and unavailable association
- **WHEN** no-document is explicitly selected, or an original reference is absent, foreign, future, unlinked or lacks document identity
- **THEN** explicit no-source invokes no retrieval and fabricates no source, while unresolved/invalid original associations refuse rather than silently becoming a blank source or current visible page.

### Requirement: Complete receiving frames have honest resource and evidence outcomes
The receiver SHALL reuse existing context and retrieval machinery, bound complete
encoded frame and caller-counted token input including provenance, preserve explicit
range/omission/budget metadata and refuse incomplete history, mismatched Provider
results or exhaustion without partial output or request/history rewriting. It
SHALL preserve captured records across callbacks, retain historical qualification
and unavailable media, and SHALL NOT write durable records, invoke a model/device
or imply current source freshness from a saved/cache key.

#### Scenario: Context and retrieval exceed complete budgets
- **WHEN** chronology is incomplete, a limit/counter is unknown or exhausted, or Provider output is malformed or mismatched
- **THEN** assembly refuses without truncating history, shortening the request, querying an unintended document or returning partial/source-less success.

#### Scenario: Historical source and snapshot changes
- **WHEN** media is explicitly omitted or later heads change during counting/query callbacks
- **THEN** the frame retains exact captured request/history/original-source facts and explicit unavailable evidence, without retained-byte substitution, rereading a new winner or reconstructing native effect permission.
