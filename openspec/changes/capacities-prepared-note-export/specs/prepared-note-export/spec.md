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

### Requirement: Writer dispatch retains the selected source and existing export owner

Writer and notebook export flows SHALL use the selected provider's scoped association key for pending lookup and retain their existing Store export owner through dispatch and reconciliation. Admission SHALL bind the selected draft, source provenance, portable correlation, effect operation and provider scope. The original cancellation and deadline SHALL remain effective. The exporter SHALL revalidate the selected source immediately before polling a write. Existing Mem entrypoints SHALL remain compatible and no provider version or conditional-update guarantee SHALL be synthesized for Capacities.

#### Scenario: Selection changes before the write

- **WHEN** the selected Writer draft or source changes after local preparation but before write polling
- **THEN** the flow refuses the write and durably records no-send only when no write was polled.

#### Scenario: A scoped export is unresolved

- **WHEN** the selected provider and space have a pending or uncertain association for the conversation and correlation
- **THEN** another generation/export cycle is blocked and original-only reconciliation can read the retained candidate without changing provider or space or dispatching another create.

#### Scenario: Cancellation or replay

- **WHEN** the original operation is canceled or its result is replayed
- **THEN** the existing Writer ownership, historical result and uncertain-write rules remain effective without acquiring a second export owner or granting another write.

### Requirement: Saved selection and original reconciliation preserve connection identity

The product SHALL require an explicit Capacities backend choice and local verified space and enrollment selection for configured Capacities exports. Absent declarations and legacy Mem preferences SHALL retain their existing meanings. Portable preferences SHALL contain neither account-bound identifiers nor secrets. Each configured attempt SHALL bind its original enrollment independently of rotating token values. A command SHALL resolve required destination credentials before new Store creation or model invocation, and SHALL refuse missing, expired, mismatched or unsupported grants without fallback.

#### Scenario: Import a Capacities preference on another installation

- **WHEN** portable preferences select Capacities but the receiving installation has no local connection
- **THEN** no account, space, grant, token or external write is inferred and export reports that connection setup is needed.

#### Scenario: Reconcile after changing the active destination

- **WHEN** the current backend or active connection has changed while an original export remains unresolved
- **THEN** reconciliation uses exactly one retained association's original provider, space and enrollment from an existing compatible Store, without creating a Store, invoking a model or dispatching a new export.
- **AND** ambiguous or conflicted associations and unavailable original grants refuse instead of choosing a current default.

#### Scenario: Reconnect to the same space

- **WHEN** replacement consent creates another enrollment for the same space
- **THEN** it receives a new grant identity and cannot silently replace the original enrollment of an unresolved attempt.

## MODIFIED Requirements

### Requirement: Prepared content uses portable exact correlation

The exporter SHALL accept explicitly prepared content and source provenance and resolve only verified native note identities. Legacy destinations SHALL reuse the existing stable metadata key or title marker. Capacities SHALL retain the stable correlation marker in the object body alongside an independent operation marker, so title changes do not move the association. Discovery SHALL report missing, duplicate, malformed and incomplete results without fuzzy selection. Mem SHALL use bounded chronological title discovery. No second registry or network-queryable Buddy service SHALL be introduced.

#### Scenario: Create then find and update on a destination with verified update behavior

- **WHEN** a destination supports the required update safeguards, a prepared note is exported, and a later source revision is deliberately exported under the same correlation
- **THEN** the same verified destination note is updated, the stable marker and source provenance survive, and each operation retains its historical result.

#### Scenario: Ambiguous or incomplete discovery

- **WHEN** exact discovery finds duplicates, malformed scope, missing markers or exceeds its bounds
- **THEN** it reports the explicit unresolved or conflict outcome without overwriting a note or assuming a search miss permits creation.
