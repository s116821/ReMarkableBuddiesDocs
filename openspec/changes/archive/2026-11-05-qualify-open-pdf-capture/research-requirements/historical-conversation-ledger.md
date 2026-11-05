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

### Requirement: Resident source history preserves distinct historical provenance
The proposed resident historical evidence bridge SHALL use the existing Ledger and Source schema2 record boundary under resident-source-handoff.md. It SHALL atomically retain original validated pixels, historical runtime/operation/source correspondence and every actual ordered provider image with the Prepared turn/root CAS. It SHALL preserve other evidence variants and confer no live observation, binding/adoption, selected-context or output authority. Missing or inconsistent stored media SHALL refuse without recapture or legacy relabeling.

#### Scenario: A resident batch is delivered to proposal and independent verification
- **WHEN** preparation is acknowledged and the stored evidence passes strict schema/link/hash/image checks
- **THEN** both calls use the same persisted provider bytes and the source remains ResidentHistoricalUnqualified

#### Scenario: A restored resident parent or derivative is absent
- **WHEN** retrieval cannot verify all required committed media
- **THEN** image-dependent use refuses without querying the device, substituting another source or issuing an effect permit

### Requirement: Resolve the resident answer conversation before preparing a repeat request
Given a fresh resident Reader capture, a request SHALL prefer the currently bound
Buddy page. If the source is a separate page, its immediate successor is eligible
only when the binding identifies the exact source and the native profile, adapter
and ordered page IDs agree. The Prepared turn SHALL append to that conversation
using the selected root revision and a fresh exchange. Conflicts or changed
associations SHALL refuse reuse. Before navigating or writing, the app SHALL
recheck the selected binding revision and confirm the current native facts.
A resumed request with an unavailable target SHALL refuse insertion.

#### Scenario: A new trigger on a question with its existing answer page
- **WHEN** fresh capture identifies the question and its bound adjacent answer
- **THEN** the Ledger prepares a fresh exchange on the existing conversation
- **AND** output uses the exact adjacent page after live admission
- **AND** a missing or changed binding does not result in a duplicate page

