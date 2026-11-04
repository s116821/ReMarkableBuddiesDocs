## MODIFIED Requirements

### Requirement: Faithful object declarations and explicit validation scope
The schema SHALL cover all fourteen current root properties, including the closed Reader declaration and its optional selected scope, and closed nested object/null/default declarations without materializing defaults. It SHALL retain absent/null/empty/partial product semantics and required children of present path objects. It SHALL describe faithful structural constraints and explicitly separate parser framing, duplicate members, lexical integers, UTF8 byte bounds, semantic constraints, filesystem/credential checks and runtime admission. It SHALL NOT silently change permissive legacy Config decoding or imply schema success activates settings.

#### Scenario: Current declaration variants
- **WHEN** canonical object declarations omit members, use allowed null parents, contain partial supported objects or include unknown members/null product leaves
- **THEN** supported structure is described accurately and unsupported structure refuses without writing defaults or relaxing unknown-field boundaries

#### Scenario: Schema success is not runtime admission
- **WHEN** an object satisfies the structural document but violates a parser, byte, semantic, filesystem or credential rule
- **THEN** existing typed/runtime checks remain authoritative and schema success grants no execution or activation authority

#### Scenario: Automated standards replay
- **WHEN** the current schema is checked in CI
- **THEN** the existing Checks job validates its meta-schema and expected structural corpus with a standards-conforming locked development engine against the already-built normal host executable selected from compiler provenance, without inserting defaults, creating another job or rebuilding the executable
