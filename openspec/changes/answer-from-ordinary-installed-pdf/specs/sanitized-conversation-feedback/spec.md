## MODIFIED Requirements

### Requirement: Explicit stored ordinary feedback receiving

The ordinary feedback receiving API SHALL resolve an explicit conversation and outcome-fact identity from one bounded current-head Conversation metadata snapshot under existing ordinary-mode custody, using existing domain, root and chronology validation. Snapshot matching SHALL include explicit root and fact record IDs regardless of malformed or foreign payload metadata and retain all selected heads. Before domain snapshot inspection, the receiver SHALL refuse selected tombstones, conflicted or duplicate heads, and unsupported record types or schemas. It SHALL accept validated ordinary target-use and target-state metadata and existing-page bindings in the same conversation. It SHALL describe only the exact retained fact with an existing matching turn through the delivered static catalog. It SHALL preserve original historical identity and refuse incomplete, conflicting, tombstoned, unsupported, foreign or ambiguous context without returning a partial or fabricated no-error result.

#### Scenario: Persisted error survives a later read

- **WHEN** an ordinary associated terminal fact is persisted and the Store is reopened while no current Buddy page is admitted
- **THEN** explicit identity resolution returns the same original fact, conversation, turn and deterministic static description without image reads, writes or native permission.

#### Scenario: Current ordinary conversation has Reader target metadata

- **WHEN** an exact historical outcome in an ordinary conversation has supported target-use, target-state or existing-page binding metadata
- **THEN** the receiver validates the metadata and resolves the same static feedback from the matching fact and turn.

#### Scenario: Context is unsafe or absent

- **WHEN** root, fact, turn, mode, schema, conflict freedom, chronology or complete Store availability cannot be established under the existing snapshot result bounds
- **THEN** the operation refuses with no description, partial list, fabricated complete empty result or persistent mutation.
