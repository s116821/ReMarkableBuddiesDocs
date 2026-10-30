## ADDED Requirements

### Requirement: Historical page associations are read atomically without effect authority
The historical Ledger SHALL inspect a desired conversation and exact document/page binding through one bounded Store snapshot that includes unavailable-commit status under the same lock. It SHALL retain all matching conflict heads, validate the historical conversation/receipt from that cloned snapshot without refreshing current heads, reuse the existing deterministic binding identity and return only immutable historical evidence or typed unresolved outcomes under historical-binding-projection-contract.md. Request-evidence validation SHALL select evidence/receipt envelopes from that same snapshot and validate only their pinned immutable references and original transaction afterward under a shared bounded read budget. It SHALL create no Store record, ownership lease, native receipt or effect permission.

#### Scenario: A saved root and binding agree
- **WHEN** a complete bounded snapshot contains one valid live conversation root and its matching historical binding for the queried document/page
- **THEN** inspection returns the original historical receipt and both snapshot revision IDs, without promoting saved evidence to current native reuse or insertion authority

#### Scenario: Stored association is missing or uncertain
- **WHEN** root or binding heads are missing, conflicted, tombstoned, unbound, bound elsewhere or owned by another conversation
- **THEN** inspection returns an explicit unresolved outcome and never treats stored absence as native page absence

#### Scenario: Snapshot or receipt cannot be validated
- **WHEN** unavailable commits, invalid identities, malformed historical records/receipt, incomplete chronology or item/metadata bounds prevent a consistent inspection
- **THEN** inspection refuses without refreshing current heads, writing or performing native operations

#### Scenario: Durable request evidence accompanies the historical binding
- **WHEN** the snapshot contains request evidence
- **THEN** inspection validates its exact snapshot evidence/receipt pair and bounded immutable references/original transaction; missing or replaced receipts and inconsistent evidence refuse without a second operation-head lookup
