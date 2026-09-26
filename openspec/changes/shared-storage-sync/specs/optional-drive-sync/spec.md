## ADDED Requirements

### Requirement: Explicit local-first per-domain sync policy
Drive sync SHALL be off by default and optional for all local operations. Subject-memory and handwriting selection SHALL be independent. Conversation/export history and source-media policies SHALL be explicit, separately configurable and default off, while local turn-linked retention remains available regardless of sync. Partial recovery sets SHALL identify unsynced/deferred media rather than claiming complete recovery. Source: REM-36 optional Drive/screenshot requirements; design section 6.

#### Scenario: Disabled or unavailable cloud
- **WHEN** sync is disabled or credentials/network are unavailable
- **THEN** local persistence continues and no default empty state or record data is uploaded

#### Scenario: History-only backup policy
- **WHEN** conversation sync is enabled but source media is off or exceeds configured limits
- **THEN** synchronized metadata identifies local-only/deferred references and recovery does not claim missing source images are restored

### Requirement: Immutable causal synchronization
The Drive adapter SHALL publish immutable logical objects and transaction manifests with stable collection/domain/record/revision identity, content digests and explicit parents. It SHALL confirm all required objects before publishing a complete manifest, retain concurrent revisions, and SHALL NOT depend on an unverified conditional media-update/CAS guarantee or mutable common-head file. Source: REM-36 concurrency/partial upload; design sections 6 and 7.

#### Scenario: Two devices edit offline
- **WHEN** both devices independently edit the same known parent and later synchronize in either order
- **THEN** both branches converge as the same unresolved head set until explicit resolution, with no last-clock/last-upload overwrite

#### Scenario: Partial object upload
- **WHEN** one referenced media/record upload has not completed or fails integrity verification
- **THEN** a complete remote transaction manifest is not published and neither device exposes a falsely complete transaction

### Requirement: Idempotent bounded Drive uploads
Before create/upload, the adapter SHALL durably bind a Drive-generated appData file ID to exact operation/content identity and reuse it across retries. Ambiguous completion or 409 SHALL be verified by reading existing metadata/content before success is recorded. Resumable media SHALL use server-confirmed offsets, restricted session state and bounded retries/cancellation. Source: official upload/generateIds references in research.md; design section 6.

#### Scenario: Timeout after successful create
- **WHEN** an upload succeeded remotely but the response was lost and retry returns 409
- **THEN** matching identity/digests are verified and the existing object is acknowledged without a duplicate logical edit

#### Scenario: Conflicting allocated ID
- **WHEN** a 409 object has unexpected collection/operation/content identity
- **THEN** the adapter reports an integrity conflict and does not acknowledge or overwrite that file

#### Scenario: Interrupted resumable media
- **WHEN** a session is interrupted or expires
- **THEN** the adapter queries confirmed progress or starts a new session for the same allocated file ID, without advancing a complete manifest until final content validation

#### Scenario: Quota or authorization failure
- **WHEN** retryable failures exhaust the batch budget or authorization is revoked
- **THEN** sync pauses with a sanitized status, persistent retry state and intact local content instead of blocking foreground input or retrying indefinitely

### Requirement: Non-destructive initial discovery and restore
A new/unbound/empty local device SHALL discover complete remote collections before publication. It SHALL require deliberate binding when collections exist and explicit create-new after successful empty discovery. Imported transactions SHALL validate identities, schemas, hashes and ancestry before local publication. Existing local edits SHALL remain branches during restore. Source: REM-36 empty-device recovery; design section 7.

#### Scenario: Empty replacement device
- **WHEN** a newly initialized device attaches to an existing selected Drive collection
- **THEN** it restores validated values/tombstones/conflicts without publishing empty defaults or treating absent local files as remote deletions

#### Scenario: Incomplete discovery or ambiguous collection
- **WHEN** pagination fails or multiple remote collections require selection
- **THEN** outbound publication remains paused and no new default collection or deletion is inferred

#### Scenario: Out-of-order or unsupported content
- **WHEN** a manifest arrives before parents/objects, or a remote schema/lineage is unsupported or invalid
- **THEN** it remains pending/quarantined without false complete status, without overwriting local heads and without republishing unknown content

### Requirement: Durable pagination and transport-removal safety
Sync SHALL process complete Drive pages and persist cursors only after validated local observations/commits are durable. Replays SHALL be idempotent. Drive removed entries, 404s or lost access SHALL NOT create domain tombstones; only validated explicit logical tombstone revisions may delete a domain value. Source: official changes-list/manage-changes references; design section 7.

#### Scenario: Crash before checkpoint
- **WHEN** a process exits after applying a change page but before saving its cursor
- **THEN** replaying that page causes no duplicate logical edits or lost changes

#### Scenario: Removed or inaccessible remote item
- **WHEN** Drive reports an item removed, inaccessible or absent
- **THEN** local data remains intact with a transport/recovery warning, and the adapter neither synthesizes a domain deletion nor blindly recreates the collection

#### Scenario: Explicit tombstone propagation
- **WHEN** a valid logical tombstone revision reaches another device
- **THEN** the store applies the causal deletion rules, retaining concurrent edit conflicts and the tombstone's recovery history

### Requirement: App-data limitations and credential isolation
The adapter SHALL use app-private ordinary files and least-required configured scope, retain local working copies and support a separate export path. It SHALL NOT use appData trash/share/move behavior, depend on appData surviving user removal, or expose tokens/session URLs/account bindings in ordinary records or logs. Granted scope/account/collection binding SHALL be validated before publication. Source: official appdata/OAuth references; design sections 6 and 8.

#### Scenario: App data or authorization removed
- **WHEN** the remote app-data folder or authorization disappears
- **THEN** sync requests deliberate recovery/reconnection while local data and independent exports remain available

#### Scenario: Token refresh and secret failure
- **WHEN** the credential provider refreshes an expired grant or receives a rejected grant
- **THEN** it atomically updates restricted token state or pauses sync with a value-free status, never serializing token bodies or private upload URLs in normal evidence

### Requirement: Account-free protocol verification
Public tests SHALL exercise the real adapter's request/response behavior using hermetic fixtures and fake credentials, including two-device conflicts/restore/deletion, pagination, retries, corruption and partial transfers. Evidence SHALL distinguish those tests from a separately authorized live-account/native test. No test default SHALL contact user Drive or tablet resources. Source: REM-36 acceptance and current lane authorization; design validation section.

#### Scenario: Offline public acceptance
- **WHEN** a contributor runs storage/sync tests with no account, plugin or device
- **THEN** deterministic protocol and failure tests execute without external requests and report their hermetic evidence boundary
