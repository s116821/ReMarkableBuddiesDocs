# shared-storage

## Purpose

Define owned local persistence, conflict-preserving recovery and offline maintenance contracts.

## Requirements

### Requirement: Versioned owned storage categories
The storage layer SHALL publish versioned locations and ownership for durable logical records/source media, nonsecret configuration, credentials, rebuildable caches/indexes, temporary diagnostics and installed components. It SHALL default to local storage, reject unsafe/unowned or overlapping roots and symlink traversal, and never treat original xochitl documents as Buddy-owned data. Source: REM-36 layout/retention requirements; design sections 1 and 4.

#### Scenario: Local startup without network
- **WHEN** a valid local configuration is used with no Drive credentials or network
- **THEN** durable records and media remain readable/writable and no sync request is initiated

#### Scenario: Unsafe ownership boundary
- **WHEN** a requested root is a source-document/system location, traverses a symlink or would adopt unrelated populated content
- **THEN** initialization refuses before mutation and preserves the existing files

#### Scenario: Diagnostic cleanup
- **WHEN** disposable diagnostics or derived caches are removed under the maintenance contract
- **THEN** committed logical records and every retained source blob remain intact and indexes can rebuild

### Requirement: Independent domain envelopes and stable identity
The engine SHALL store versioned envelopes with namespace, domain schema version, stable record/revision/operation/actor IDs, explicit parents, payload kind and content-hash references. Domain adapters SHALL remain separate for conversation, source, export association, subject memory and handwriting; subject memory SHALL NOT be required to enable Writer or another domain. Unknown versions SHALL be preserved or refused without being silently overwritten or republished. Source: REM-36 outcome/coordination; design section 2.

#### Scenario: Idempotent local mutation
- **WHEN** a caller retries an operation with the same ID and content
- **THEN** the store returns the existing committed result, while reusing that ID for different content fails without altering either record

#### Scenario: Independent memory and handwriting
- **WHEN** a fixture writes one domain while another domain is disabled
- **THEN** persistence remains available to the selected domain and does not mix their payload schemas or enable the other domain

#### Scenario: Unsupported future envelope
- **WHEN** a stored or imported envelope requires an unsupported version
- **THEN** its bytes are retained for recovery and a bounded unsupported-schema result prevents interpretation, overwrite or sync publication

### Requirement: Atomic durable publication and recovery
The engine SHALL stage and sync required immutable record/media objects before atomically publishing a commit manifest. Only complete validated committed manifests SHALL make objects visible. It SHALL validate digests, sizes, bounds and required-object availability, preserve the last committed state on failure, and rebuild derived indexes from committed content. Policy-neutral media descriptors SHALL be distinct from required objects; metadata-only imported transactions SHALL preserve explicit omitted coverage and expose unavailable-media results without claiming full-media recovery. Newly captured local source transactions SHALL require their captured bytes. Source: REM-36 atomic writes/interruption recovery; design sections 2 and 6.

#### Scenario: Interrupted transaction
- **WHEN** a process fails before the commit manifest is durably published
- **THEN** recovery exposes the previous complete state, never a partial record/media transaction, and incomplete staging remains distinguishable from committed data

#### Scenario: Commit succeeds before index update
- **WHEN** a process fails after commit publication but before rebuilding a derived index
- **THEN** recovery reconstructs the correct committed heads without losing or duplicating the transaction

#### Scenario: Corrupt media or full disk
- **WHEN** a referenced object is corrupt/missing or staging cannot complete because storage is full
- **THEN** the operation does not report complete success or silently evict committed records, and a sanitized recovery/capacity status identifies the failure

### Requirement: Explicit revisions conflicts and tombstones
The store SHALL use parent lineage rather than wall-clock timestamps to identify causal successors and conflicts. Multiple concurrent heads SHALL be retained until an explicit resolution names all observed heads. Deletion SHALL be an explicit tombstone revision; file absence SHALL NOT imply deletion. Tombstones and conflicts SHALL survive export/restore. Source: REM-36 concurrency/deletion requirements; design sections 2 and 7.

#### Scenario: Concurrent edit and delete
- **WHEN** two devices create a value and a tombstone from the same parent
- **THEN** both revisions remain recoverable as an unresolved conflict and neither clock ordering nor arrival order silently discards a branch

#### Scenario: Stale resolution
- **WHEN** a resolver submits a result based on a head set that changed
- **THEN** the store reports conflict and requires a new resolution rather than losing the unseen revision

### Requirement: Safe maintenance ownership
The runtime SHALL hold one exclusive OS lease on a stable store-lock inode for its lifetime, with shared in-process access serialized by the store. Mutating external maintenance SHALL confirm the unit is inactive and acquire that same lock before touching owned data. Lock files SHALL NOT be deleted to break ownership. Failures SHALL preserve committed data and SHALL NOT restart through partial restoration. Source: REM-36 quiesce/lock requirement; design section 4.

#### Scenario: Competing writer or maintenance
- **WHEN** another process owns the store lease
- **THEN** a second writer or external mutation refuses promptly without modifying records, even if a stale PID/status file suggests otherwise

#### Scenario: Interrupted maintenance session
- **WHEN** the maintenance process exits during staging
- **THEN** its OS lock releases, partial staging remains invisible and later recovery uses the last valid committed state

#### Scenario: Missing compatible lock adapter
- **WHEN** a companion can stop the unit but cannot acquire the declared compatible lock
- **THEN** it refuses mutation rather than treating elapsed time or service stop alone as ownership proof

### Requirement: Offline companion capability contract
The component SHALL expose versioned file schemas, supported read/write formats, owned paths, lock protocol, domains and sanitized status via offline-readable files and public documentation. The companion SHALL use files, SSH and OS commands, never a queryable Buddy HTTP/RPC/admin service. Capability versions SHALL be independent of app release numbers. Source: REM-36 companion boundary; design section 4.

#### Scenario: Public inspection without a running app
- **WHEN** a compatible companion or manual contributor reads installed contracts and stored descriptors with the service stopped
- **THEN** supported schemas/paths/maintenance preconditions are discoverable without private tools or a service request

### Requirement: Atomic configuration and credential separation
Nonsecret configuration SHALL be versioned, validated and atomically replaced under maintenance. Existing explicit CLI/environment precedence and existing protected environment files SHALL remain supported. Secrets SHALL live in restricted credential storage or existing environment input, never ordinary records, snapshots, logs or diagnostics from this subsystem. A redacted effective-config descriptor SHALL identify override sources without values for secrets. Source: REM-36 credentials/configuration requirements; design section 3.

#### Scenario: Environment overrides a UI file edit
- **WHEN** a config file and existing service environment both provide the same supported setting
- **THEN** the environment value wins and the redacted descriptor identifies its source so the companion can explain the effective behavior

#### Scenario: Invalid or insecure configuration input
- **WHEN** a config schema/root/selected secret is invalid or a credential file is symlinked or insecure on the target platform
- **THEN** validation fails before device initialization without printing secret values or replacing a usable configuration

### Requirement: Verified export restore and migration
The store SHALL export a versioned manifest plus verified immutable objects into a new destination, excluding credentials/caches/binaries. Restore and registered migrations SHALL validate in an isolated generation before atomic activation, preserve rollback/source data, refuse malformed paths and unsupported versions, and never infer deletion from absent input. An empty-device restore SHALL preserve logical IDs but establish a new actor for future writes. Source: REM-36 migration/export/restore; design section 5.

#### Scenario: Offline restore with conflicts
- **WHEN** a complete verified export containing values, tombstones and concurrent heads is restored without network
- **THEN** all logical identities and conflict state survive, while credentials and pending device-specific operations are not replayed as new edits

#### Scenario: Corrupt restore or interrupted migration
- **WHEN** input has traversal/symlink/hash/schema faults or migration fails before activation
- **THEN** the original store remains active and no partially migrated generation is exposed

#### Scenario: Post-activation recovery
- **WHEN** migration activation completed but later cleanup was interrupted
- **THEN** the new validated generation remains authoritative and the retained old generation is available for deliberate recovery

### Requirement: Honest persistence survival evidence
Documentation and tests SHALL distinguish ordinary app replacement/reinstall preservation from unverified firmware/reset survival. The implementation SHALL separate installed components from user roots, retain export/recovery paths and make no unsupported guarantee that a vendor update or factory reset preserves Buddy data or authorization. Source: REM-36 survival investigation; design section 1 and research notes.

#### Scenario: App replacement fixture
- **WHEN** a fixture replaces/removes installed binary files while retaining owned user roots
- **THEN** records/config remain usable and the evidence is labeled host fixture, not proof of actual firmware/reset persistence
