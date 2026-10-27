## MODIFIED Requirements

### Requirement: Independent domain envelopes and stable identity
The engine SHALL store versioned envelopes with namespace, domain schema version,
stable record/revision/operation/actor IDs, explicit parents, payload kind and
content-hash references. Domain adapters SHALL remain separate for conversation,
source, export association, subject memory and handwriting; subject memory SHALL
NOT be required to enable Writer or another domain. Format-one envelopes SHALL
admit domain version 1 across existing namespaces and version 2 only for current
conversation intent/settlement records, export-association attempts and
normalized-text Source records. Version 3 SHALL be scoped only to media-backed
normalized notebook Source records and non-visible conversation Writer plan/stage
facts. The offline JSON contract SHALL mirror each exact namespace/version
restriction. Existing formats, Source1/2 and Conversation1/2 bytes/receipt recipes
SHALL remain unchanged; ordinary roots/turns/receipts SHALL NOT be relabeled as
Writer stage or native admitted-intent records. Domain adapters SHALL validate their corresponding namespace/version/
payload shape without weakening current conversation or export admission.
Unknown versions SHALL be preserved or refused without being silently overwritten
or republished.
Notebook domain3 SHALL require explicitly adopted notebook-capable storage and
successor capabilities; it SHALL NOT be written under legacy generation1/2 or
feedback-only generation3. Generic envelope format1 SHALL remain unchanged;
payload schema3 SHALL NOT imply storage generation3. Existing contract1/2 bytes
SHALL remain immutable. Exact payload-kind reservations, numerical successor
generation/backup/contract allocations and shared-path ownership SHALL be accepted
before implementation; this proposal assigns no successor numbers.
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


#### Scenario: Scoped archived source and processing facts
- **WHEN** a notebook archive uses Source3 or a Writer plan/stage uses Conversation3, or an old capture/intent/export/memory shape claims version 3
- **THEN** only the exact supported new namespace/version/shape is admitted, all cross-labeling refuses, and old Source1/2, Conversation1/2 and Export1/2 facts retain their meaning without granting native authority.

#### Scenario: Older consumer meets new data
- **WHEN** a consumer that supports only prior domain versions opens or receives a version-3 notebook commit
- **THEN** it retains/refuses unsupported data without overwrite, partial complete-history claims or sync publication; newer support does not silently migrate old records.

## ADDED Requirements

### Requirement: Explicit identity-preserving notebook format adoption
Notebook preparation SHALL require a fresh uniquely owned Store, exclusive
stable-inode lease, no active clients/effects or incompatible modes and complete
retained history/media. It SHALL preserve generation identity, CURRENT,
historical envelope/commit/receipt/media bytes and existing feature bindings.
It SHALL stage notebook-specific actor/generation-bound metadata and immutable
successor contract documents, atomically commit the reserved unsupported format
discriminator, then publish/read back complete bound successor capabilities
before exposing notebook clients or provider/export effects. Ordinary open SHALL
NOT adopt or repair incomplete preparation. Explicit resume SHALL read actual
state and revalidate current closure under unique custody without automatic
downgrade. Format adoption SHALL NOT require copying retained media solely to
change a discriminator. Supported platform durability SHALL be qualified rather
than inferred from source or Windows host fixtures.

#### Scenario: Pending metadata precedes the format fence
- **WHEN** adoption stops with pending metadata while the old format remains, and an old writer subsequently changes legacy history
- **THEN** no notebook data/effects exist, the old writer may ignore the unknown metadata, and explicit resume revalidates actual current closure rather than activating stale preparation facts.

#### Scenario: Format acknowledgment is uncertain
- **WHEN** format replacement or parent-directory synchronization reports an error or loses acknowledgment
- **THEN** the caller starts no notebook effect, explicit resume reads actual discriminator and metadata under exclusive custody, and no failed return is treated as proof of rollback.

#### Scenario: Format fence precedes capability completion
- **WHEN** the new format is committed but bound capabilities or required metadata are missing, stale or malformed
- **THEN** predecessors refuse before history recovery/publication, new ordinary open refuses incomplete adoption without repair, and only explicit preparation may finish verified closure before clients/effects.

#### Scenario: Unique custody preserves identities and feedback
- **WHEN** deliberate preparation adopts an eligible complete ordinary generation or encounters a live Store/client/mode
- **THEN** adoption preserves CURRENT/generation, receipts and media without data copying, retains feedback marker/payload1 through an explicit successor composition branch without globally relaxing pending admission, or refuses the live/incompatible case before adoption/effects.

### Requirement: Notebook successor consumers refuse unsupported operations
Notebook-bearing generations SHALL use exact successor capability and archive
contracts. Actual predecessor writer/sync/import/restore/recovery/maintenance
entrypoints SHALL refuse unsupported current formats before history recovery,
publication or capability rewrite; no zero-auxiliary-metadata or unrelated-config
write guarantee is implied. Read-only inspection SHALL report unsupported
truthfully. Sync/selected/group and cross-actor notebook import SHALL refuse before
publication/mutation in this increment. Whole ordinary same-actor archive/restore
SHALL preserve exact immutable history/media/feature closure under its separately
reserved archive discriminator; it SHALL NOT reuse feedback backup3 or import
domain3 into legacy formats. Relevant narrow cleanup/native receiving SHALL
refuse before effects without silently dropping references or acquiring native
authority. Any supported predecessor bypass or unpreservable lineage SHALL block
delivery until the contract is revised.

#### Scenario: Actual predecessor entrypoints meet adopted storage
- **WHEN** pinned supported predecessor writer, sync, import, restore, recovery or cleanup commands encounter notebook-capable current storage or its successor archive
- **THEN** they refuse before history recovery/publication or capability rewrite and retain data; source inspection alone is not execution qualification.

#### Scenario: Unsupported sharing and native consumers
- **WHEN** notebook-bearing data reaches selected/group/sync/cross-actor import, narrow cleanup or native receiving
- **THEN** the operation refuses before publication or mutation, retains all referenced data and grants no native ownership; namespace filtering does not silently publish an incomplete history.

#### Scenario: Explicit complete same-actor archive round trip
- **WHEN** a supported deliberate whole ordinary same-actor backup/restore includes notebook JSON media and retained feedback
- **THEN** exact envelope/media/receipt/feature closure survives under the allocated successor archive policy, with no use of feedback backup3, legacy-generation domain3 import, silent rollback or historical byte rewriting.
