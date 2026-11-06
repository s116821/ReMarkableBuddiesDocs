## ADDED Requirements

### Requirement: Explicit offline current configuration schema discovery
The application SHALL expose --configuration-schema as an exclusive read-only selector that emits a bounded embedded independently identified JSON Schema for the canonical supported configuration object declarations. It SHALL dispatch before selected configuration, stdin, environment-file, credential, Store or runtime work, with raw UTF8 JSON and one final LF. Schema-document identity SHALL be independent of application, storage and runtime-config versions. Existing operation protocols and frozen storage contract/capability bytes SHALL remain unchanged.

#### Scenario: Missing or poisoned local inputs
- **WHEN** schema discovery runs with missing/poisoned config, environment-file, credentials or notification settings and unread stdin
- **THEN** it emits the static current schema without accessing those inputs or constructing storage/runtime services

#### Scenario: Conflicting operation
- **WHEN** schema discovery is combined with another execution mode, runtime override or input selector
- **THEN** argument admission refuses before either operation executes

### Requirement: Faithful object declarations and explicit validation scope
The schema SHALL cover all thirteen current root properties and closed nested object/null/default declarations without materializing defaults. It SHALL retain absent/null/empty/partial product semantics and required children of present path objects. It SHALL describe faithful structural constraints and explicitly separate parser framing, duplicate members, lexical integers, UTF8 byte bounds, semantic constraints, filesystem/credential checks and runtime admission. It SHALL NOT silently change permissive legacy Config decoding or imply schema success activates settings.

#### Scenario: Current declaration variants
- **WHEN** canonical object declarations omit members, use allowed null parents, contain partial supported objects or include unknown members/null product leaves
- **THEN** supported structure is described accurately and unsupported structure refuses without writing defaults or relaxing unknown-field boundaries

#### Scenario: Schema success is not runtime admission
- **WHEN** an object satisfies the structural document but violates a parser, byte, semantic, filesystem or credential rule
- **THEN** existing typed/runtime checks remain authoritative and schema success grants no execution or activation authority

#### Scenario: Automated standards replay
- **WHEN** the current schema is checked in CI
- **THEN** the existing Checks job validates its meta-schema and expected structural corpus with a standards-conforming locked development engine against the already-built normal host executable selected from compiler provenance, without inserting defaults, creating another job or rebuilding the executable
