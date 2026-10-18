## MODIFIED Requirements

### Requirement: Independent domain envelopes and stable identity
The engine SHALL store versioned envelopes with namespace, domain schema version,
stable record/revision/operation/actor IDs, explicit parents, payload kind and
content-hash references. Domain adapters SHALL remain separate for conversation,
source, export association, subject memory and handwriting; subject memory SHALL
NOT be required to enable Writer or another domain. Format-one envelopes SHALL
admit domain version 1 across existing namespaces and version 2 only for export
associations, with the same restriction in the offline JSON contract. The Ledger
SHALL validate the corresponding export payload shape. Unknown versions SHALL be
preserved or refused without being silently overwritten or republished.

#### Scenario: Idempotent local mutation
- **WHEN** a caller retries an operation with the same ID and content
- **THEN** the store returns the existing committed result, while reusing that ID for different content fails without altering either record.

#### Scenario: Independent memory and handwriting
- **WHEN** a fixture writes one domain while another domain is disabled
- **THEN** persistence remains available to the selected domain and does not mix their payload schemas or enable the other domain.

#### Scenario: Unsupported future envelope
- **WHEN** a stored or imported envelope requires an unsupported version
- **THEN** its bytes are retained for recovery and a bounded unsupported-schema result prevents interpretation, overwrite or sync publication.

#### Scenario: Scoped export domain upgrade
- **WHEN** an export attempt uses domain version 2, another namespace uses version 2, or an export payload uses the wrong domain shape
- **THEN** only the supported export envelope is admitted, the domain adapter refuses mismatched payloads, and envelope/store format remains 1.
