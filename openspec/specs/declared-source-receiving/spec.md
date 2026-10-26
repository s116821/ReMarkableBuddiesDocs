# Declared source receiving

## Purpose

Assemble caller-declared ordinary source context within one validated record
snapshot while preserving independent receiving and captured publication admission.

## Requirements

### Requirement: Declared receiving resolves within its frame snapshot
The ordinary ledger SHALL offer opt-in receiving that resolves the existing source
directive against the same validated records used to assemble its immutable frame.
It SHALL preserve explicit no-document/change, named prior-operation selection,
independent complete keys, exact request/history/provenance and complete existing
budgets, without a separate public resolution/receiving snapshot gap. Existing
receiving and standalone resolver APIs and their qualification SHALL remain intact.

#### Scenario: Inherited source and deliberate change
- **WHEN** a caller supplies a valid named prior choice or explicit original/no-document directive
- **THEN** receiving assembles exact captured request/history and that declared source, querying the independently keyed local source once when bound and making zero queries for no-document.

#### Scenario: Invalid anchor or receiving admission
- **WHEN** a directive omits its operation, has missing/foreign/future/corrupt/changed-source dependencies, or its key/result/context exceeds existing admission
- **THEN** receiving refuses with the applicable sanitized typed resolution, context-budget or receiving error without choosing another operation, substituting the visible page, rewriting history or returning partial source-less success.

#### Scenario: Store changes during callbacks
- **WHEN** Provider or token callbacks change current source, anchor or history after the frame snapshot
- **THEN** the read-only frame retains its captured facts without rereading a new winner or claiming unchanged current state, and callbacks run outside Store locks.

### Requirement: Declared evidence preparation preserves existing admission and history
Opt-in declared preparation SHALL resolve and assemble from its existing captured
read set and reuse sealed preparation, complete bounds and atomic currentness
checked publication. It SHALL preserve old APIs, frame/evidence schemas, exact raw
references and historical retries, without a directive-lineage record, source
registry, model consumption, active-intent or selected/native authority claim.

#### Scenario: Relevant changes before fresh publication
- **WHEN** a captured named anchor, source, history, generation or relevant head changes before fresh publication
- **THEN** publication refuses without re-resolving, requerying, partial writes or resurrecting state, while unrelated conversations remain independent.

#### Scenario: Equivalent selection and historical retry
- **WHEN** explicit and inherited preparations target equivalent existing frame/count/limits/timestamp content for one stable operation, or committed evidence is inspected/retried through supported historical recovery after restart or logical deletion
- **THEN** unchanged retry rules recover the original historical acknowledgment without another write/query, fresh preparation still requires valid current dependencies, and evidence retains resolved source provenance without pretending to record directive lineage or fresh authority.
