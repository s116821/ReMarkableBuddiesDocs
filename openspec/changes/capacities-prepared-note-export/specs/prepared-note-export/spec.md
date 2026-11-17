## ADDED Requirements

### Requirement: Capacities create and readback use a verified destination scope

The Capacities exporter SHALL verify the authorized space and writable destination shape before preparing one typed object create. An enabled tag selection SHALL resolve to verified same-space tag IDs. Completion SHALL require exact-ID readback with the expected structure, stable correlation, operation marker and content evidence. A request to change an existing object's content SHALL fail closed until a reviewed provider update policy exists.

#### Scenario: Create response returns a candidate ID

- **WHEN** an authorized create returns a valid provider-assigned object ID
- **THEN** the exporter durably saves that candidate before exact-ID readback and binds the native identity only after the expected evidence is verified.

#### Scenario: Create outcome is uncertain

- **WHEN** a create may have dispatched and its response or trustworthy candidate ID is lost
- **THEN** the operation remains unresolved and replay performs no mutation.
- **AND** if a candidate ID is retained, reconciliation may read only that exact object in the verified space.

#### Scenario: Space, shape or tag mismatch

- **WHEN** authorization selects another space, required fields are unavailable, or a selected tag cannot be verified
- **THEN** the exporter refuses without a create.

#### Scenario: Existing object needs a changed export

- **WHEN** the verified association already has a native object and the requested export would change it
- **THEN** the exporter reports the unsupported operation and sends no mutation.

## MODIFIED Requirements

### Requirement: Prepared content uses portable exact correlation

The exporter SHALL accept explicitly prepared content and source provenance and resolve only verified native note identities. Legacy destinations SHALL reuse the existing stable metadata key or title marker. Capacities SHALL retain the stable correlation marker in the object body alongside an independent operation marker, so title changes do not move the association. Discovery SHALL report missing, duplicate, malformed and incomplete results without fuzzy selection. Mem SHALL use bounded chronological title discovery. No second registry or network-queryable Buddy service SHALL be introduced.

#### Scenario: Create then find and update on a destination with verified update behavior

- **WHEN** a destination supports the required update safeguards, a prepared note is exported, and a later source revision is deliberately exported under the same correlation
- **THEN** the same verified destination note is updated, the stable marker and source provenance survive, and each operation retains its historical result.

#### Scenario: Ambiguous or incomplete discovery

- **WHEN** exact discovery finds duplicates, malformed scope, missing markers or exceeds its bounds
- **THEN** it reports the explicit unresolved or conflict outcome without overwriting a note or assuming a search miss permits creation.
