## MODIFIED Requirements

### Requirement: Explicit bounded saved-file inspection
The producer SHALL expose one fixed explicit inspect operation over an existing absolute configuration selected by REMARKABLE_BUDDIES_CONFIG, without stdin, default-file fallback, declared-root probes, Store/provider/runtime initialization or writes. It SHALL enforce the exact caps, strict parsing and sanitized whole-view refusal in contract.md. The Config root and every present schema-defined struct record (paths, memory, sync, personalization and non-null memory.selection) SHALL be JSON objects, not positional arrays; legitimate collection arrays and absent/default/explicit-null semantics remain supported.

#### Scenario: Valid saved file
- **WHEN** the explicit bounded regular file has supported strict typed declarations
- **THEN** one bounded complete snapshot is emitted without reading declared roots, credentials, environment overrides or stdin.

#### Scenario: Invalid or unavailable file
- **WHEN** selection, read, schema, duplicate, type, value or bound admission fails
- **THEN** the exact sanitized refusal has null snapshot and no fallback or side effect.

#### Scenario: Positional struct arrays refuse
- **WHEN** the selected saved configuration uses an array at its root or a schema-defined struct position
- **THEN** maintenance reports invalid-input with no snapshot, rather than inventing default/declared origins, while supported namespace arrays and valid object reports remain unchanged.
