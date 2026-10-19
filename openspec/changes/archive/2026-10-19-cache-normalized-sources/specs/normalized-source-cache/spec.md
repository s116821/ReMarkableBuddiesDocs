## ADDED Requirements

### Requirement: Owned derived source cache requires exact validated identity
The local source cache SHALL consume the existing owned cache/persistence
primitives, bound encoded entries and capacity, rebuild the existing Index from
validated normalized input and require the caller's complete independently
selected key before returning an index. It SHALL NOT imply source freshness,
Reader integration, native authority or durable/synchronized evidence.

#### Scenario: Reopen and changed source
- **WHEN** a process reopens an owned cached source with the exact expected key or a changed source/extractor/normalized key
- **THEN** exact validated material can be queried after rebuilding, while stale, corrupt, unsupported or mismatched material cannot return an index.

#### Scenario: Refused replacement and scoped cleanup
- **WHEN** invalid input, exhausted capacity or a prepublication failure occurs, or the caller explicitly forgets one cached document
- **THEN** the previous accepted slot survives failed replacement and forgetting can remove only that document's owned derived slot, without deleting source/durable/other-domain or unknown files.
