## MODIFIED Requirements

### Requirement: Independent domain envelopes and stable identity
The engine SHALL store versioned envelopes with namespace, domain schema version,
stable record/revision/operation/actor IDs, explicit parents, payload kind and
content-hash references. Domain adapters SHALL remain separate for conversation,
source, export association, subject memory and handwriting; subject memory SHALL
NOT be required to enable Writer or another domain. Format-one envelopes SHALL
admit domain version 1 across existing namespaces and version 2 only for current
conversation intent/settlement records, export-association attempts and
normalized-text Source records, with the same restriction in the offline JSON
contract. Domain adapters SHALL validate their corresponding namespace/version/
payload shape without weakening current conversation or export admission.
Unknown versions SHALL be preserved or refused without being silently overwritten
or republished.
Source: REM-36 outcome/coordination; design section 2; scoped prepared-note export and normalized-text Writer admission.

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
- **WHEN** an export attempt uses domain version 2 or an export payload uses the wrong domain shape
- **THEN** the supported export envelope is admitted, the domain adapter refuses mismatched payloads, and envelope/store format remains 1.

#### Scenario: Scoped text source upgrade
- **WHEN** a normalized-text Source uses domain 2, a legacy image/capture claims Source2, a new text source claims Source1, or subject-memory/handwriting claims unsupported version 2
- **THEN** only the supported text-source schema/shape is interpreted, all mismatches refuse, and existing Source1 image/capture records retain their original serialization.

#### Scenario: Current conversation and export schemas survive composition
- **WHEN** current Conversation2 intent/settlement and Export2 attempt records are reopened alongside Source2 normalized text, or record kinds are cross-labeled into another namespace/version
- **THEN** each valid existing record retains its own admission, bytes and receipt fingerprints, supported text records remain distinct, and wrong-schema or wrong-namespace shapes refuse without rewriting history or granting native authority.
