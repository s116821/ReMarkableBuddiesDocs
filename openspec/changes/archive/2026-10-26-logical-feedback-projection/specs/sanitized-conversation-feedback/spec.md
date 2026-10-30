## ADDED Requirements

### Requirement: Explicit stored historical feedback layout composition
The ordinary feedback API SHALL compose one explicit stored outcome-fact identity with the existing logical conversation planner using the same complete-store, ordinary-custody, single-snapshot, schema/head/identity/chronology validation as describe_stored. It SHALL accept no caller-supplied description or raw fact. The selected stored Turn SHALL equal the matching caller-supplied layout-context Turn in every field; missing, duplicated, foreign, stale or altered selected context SHALL refuse before returning a plan. The caller remains responsible for domain validation of other context turns. Existing planner validation SHALL still apply. Source: explicit stored historical receiving and original immutable layout contract.

#### Scenario: Exact stored fact and layout turn
- **WHEN** one supported historical fact resolves under ordinary custody and its stored turn exactly matches the supplied context
- **THEN** the result contains the existing logical page plan, original exchange identity and original static feedback description without modifying turns, draft, source links, geometry or Store state.

#### Scenario: Stale or unrelated selected context
- **WHEN** the matching context turn is absent, foreign, duplicated or differs from the selected stored turn in any field
- **THEN** the composed call refuses without returning a partial plan or rewriting either history.

#### Scenario: Original query and refusal behavior
- **WHEN** existing snapshot, mode, identity, schema, conflict, tombstone or chronology requirements refuse the query
- **THEN** the composed call also refuses using privacy-safe diagnostics and the existing describe_stored behavior remains compatible.

### Requirement: Logical feedback preserves historical authority boundaries
The composed result SHALL preserve the original fact/conversation/turn identity and catalog uncertainty behavior, retain the 1024-byte serialized description bound, and associate the description only with its original exchange. An older fact SHALL remain historical even if its retained turn now has a later outcome. The result SHALL NOT create a Turn, pending queue, new persisted state, presentation acknowledgment, live status or current native authority. Existing layout APIs and shapes SHALL remain compatible. Source: historical-not-live receiving and read-only presentation boundaries.

#### Scenario: Older failure and later turn outcome
- **WHEN** a selected older error fact belongs to a retained turn whose outcome later changed and the supplied context exactly matches that retained turn
- **THEN** the original sanitized historical description remains tied to that turn without replacing its current text or outcome.

#### Scenario: Private diagnostic or uncertain outcome
- **WHEN** stored records contain raw completion/provider/diagnostic canaries or an uncertain effect
- **THEN** feedback contains only static catalog text and original identities, uncertainty remains reconciliation, and no presentation or cancellation-success claim is added.

#### Scenario: Missing pre-attempt identity
- **WHEN** an error has no usable stored conversation and turn identity
- **THEN** this API refuses and does not fabricate an associated record or claim durable unassociated-error retention.
