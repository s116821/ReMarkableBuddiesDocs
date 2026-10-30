## ADDED Requirements

### Requirement: Owned unassociated error observations
The retention domain SHALL store immutable typed observations with original actor/operation identity and no fabricated conversation, turn or page identity. It SHALL accept no raw provider/auth/request/answer/diagnostic message and SHALL derive only static error or reconciliation descriptions through the shared catalog. It SHALL NOT certify completion, cancellation, rollback, display state or native authority. Source: errors before a usable Buddy page and the delivered historical-feedback privacy boundary.

#### Scenario: Error before conversation association
- **WHEN** a valid owned pre-association operation and typed reason are explicitly retained in prepared supported ordinary storage
- **THEN** a durable observation can be reopened with exact original identity/static text without creating a conversation or changing native content.

#### Scenario: Uncertain effect or private payload
- **WHEN** an observation needs reconciliation or supplied metadata contains unsupported/raw fields
- **THEN** uncertainty never becomes canceled/completed/undone, and invalid payloads refuse without leaking their content.

### Requirement: Exact bounded retention and historical query
Publication SHALL use existing Store custody, actor/generation/parent/operation checks and enforce identity/capacity atomically. Equal literal callbacks SHALL resolve the same observation; contradictory content, conflicts, tombstones, unsupported identity/schema or incomplete storage SHALL refuse. A bounded explicit snapshot/query SHALL return only validated historical descriptions, never a known-undisplayed queue or partial success. Source: immutable local storage and explicit historical receiving contracts.

#### Scenario: Repeat and conflicting observation
- **WHEN** the same literal operation is retried or its content is changed under the same identity
- **THEN** only the identical retained observation is recognized; a contradictory observation does not overwrite it.

#### Scenario: Interrupted publication or capacity limit
- **WHEN** publication is interrupted, ambiguous or beyond the admitted capacity
- **THEN** success is reported only from verified literal committed state, otherwise uncertainty/refusal is explicit and no guessed delay or blind replay proves retention.

### Requirement: Retention is not presentation or runtime activation
The APIs SHALL expose prepared data retention and historical query only. They SHALL NOT auto-associate an observation, insert a Turn, mark it displayed, add runtime error hooks, enable native output, delete/expire observations or share the new domain through live sync. Existing data/current/native admission requirements SHALL remain independent. Source: separate pre-page retention, presentation and SDK authority requirements.

#### Scenario: Later usable page
- **WHEN** a usable page appears after retention
- **THEN** the observation remains historical and a separate explicit association/current-admission/presentation protocol is required before any page effect.

#### Scenario: Unsupported live sharing or maintenance
- **WHEN** a caller requests unqualified sharing, deletion, maintenance or production activation
- **THEN** the request refuses rather than widening existing validators or treating retained data as effect permission.
