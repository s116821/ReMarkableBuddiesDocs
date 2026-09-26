# Shared storage and optional Drive sync, version 1

REM-36 supplies generic persistence and synchronization. Conversation/source schemas, memory behavior, handwriting learning and native page creation remain with REM-37, REM-24, REM-26 and REM-25. Synthetic envelopes do not establish those features. The contract has no Buddy HTTP, RPC or admin listener.

## Files and ownership

| Category | Tablet default | Authority |
| --- | --- | --- |
| Durable data | `/home/root/.local/share/remarkable-buddies/` | `identity.json`, `CURRENT`, immutable generations, objects and committed manifests |
| Nonsecret settings | `/home/root/.config/remarkable-buddies/config.json` | Validated JSON; controlled restart applies changes |
| Credentials | `/home/root/.config/remarkable-buddies/credentials/` | Protected model references, `drive.json`, private resumable-session state; excluded from exports |
| Existing model environment | `/home/root/.config/reader-buddy/environment` | Existing service support and precedence are preserved |
| Rebuildable cache | `/home/root/.cache/remarkable-buddies/` | Owned auxiliary root; indexes are reconstructed from committed manifests |
| New transient diagnostics | `/tmp/remarkable-buddies/` | Reserved disposable category; never the source-media retention API |
| Installed components | Existing `/opt/bin/reader-buddy` and systemd unit | Separate from user data; extension installation remains REM-41 |

The data root also exposes `capabilities.json`, `contract-v1.json`, a source-only `effective-config.json`, a nonsecret `config.snapshot.json`, and `sync/health.json`. The embedded [machine-readable contract](https://github.com/s116821/ReMarkableBuddies/blob/main/src/storage/contract-v1.json) contains JSON Schemas and additional validation rules. Register each entry in `schemas` under its `$id` in an offline schema registry; backup definitions reference the manifest/config schemas by those identifiers. Contract/schema versions are independent of application release tags.

Roots must be absolute, non-overlapping, free of symlink/reparse traversal and outside protected system/xochitl locations. Populated roots without the expected owner marker are refused. A new store creates an installation actor ID; credentials/cache markers bind to that identity. Linux owned directories use 0700 and secret/staged files use 0600. Windows fixture results do not establish Linux permission or power-loss behavior. Existing Reader caches, legacy symbol state and xochitl documents are not silently adopted or migrated.

## Logical records and commits

An envelope contains `envelope_version`, `namespace`, `domain_schema_version`, `record_id`, `revision_id`, `operation_id`, `actor_id`, `parents`, `kind`, opaque `payload`, and policy-neutral `media_descriptors`. Version 1 recognizes conversation, source, export-association, subject-memory and handwriting namespaces. No native page-operation journal is registered. Domain schema adapters currently accept version 1 only; future versions must be explicitly implemented.

Record, revision and operation identities are distinct. Identical operation retries are idempotent; conflicting reuse is refused. Local writes compare the full expected parent/head set while holding the store transaction mutex. Conflicts expose all competing revision IDs. `value` returns no value for a sole tombstone; `heads` retains history/conflicts. Clocks do not resolve conflicts. An explicit resolution must name every current head. Concurrent edit/delete retains both branches; no tombstone expiry or automatic physical garbage collection occurs.

Media can be staged through a bounded streaming reader before a commit. Staged/orphaned objects are not readable as committed content. A manifest publishes records and its declared required media atomically after object hashes/sizes and lineage validate. Its namespace map must exactly match the referenced envelopes. File contents, newly created directory entries and manifest publication are synchronized in order on Unix. Incomplete staging is invisible; unavailable/corrupt committed content is retained and reported, not treated as deletion. A missing `CURRENT` with retained generations fails closed instead of creating an empty store.

Current safety bounds are 1 MiB per envelope, 8 MiB aggregate record bytes/metadata, 4,096 required objects per manifest, and 256 MiB per media object. Backup manifests and object inventories each have a 4,096-entry bound; oversized exports refuse before publishing their completion marker. A completed marker therefore describes a bundle the same version can parse. These are explicit version-1 bounds, not a promise of unbounded storage. Capacity errors preserve committed data and never silently evict source media.

## Configuration and maintenance

Production precedence is explicit CLI, existing relevant environment/.env, file configuration, then existing defaults. The model remains `gpt-5.6-terra`, corner LL, and logging/debug defaults remain unchanged. Model/corner file values apply only when the corresponding CLI argument was not explicit. `REMARKABLE_BUDDIES_CONFIG` selects an alternate configuration file; an explicitly selected missing file is an error. Unknown fields/versions and invalid roots fail before device initialization. Scripted simulation branches before normal configuration/storage/credentials/sync and remains offline.

No secret value belongs in ordinary configuration. A `model_credential` is a simple filename reference inside the protected credential root; explicit CLI/environment keys still win. Effective-setting descriptors contain source labels, not keys, tokens or upload locations. Configuration supports `model`, `base_url`, `trigger_corner`, `log_level`, `debug_dump`, `paths`, and `sync`; the shipped schema defines their exact shapes/defaults.

The external maintenance sequence is:

1. Remember whether `reader-buddy.service` was running; stop it and confirm inactive state through systemd/OS inspection.
2. Acquire an exclusive nonblocking OS lock on the existing stable `store.lock` inode. Never delete or replace it. Linux uses `flock`; Windows tests use the standard library's Windows file lock. A PID/status file or elapsed delay is not ownership proof. A companion must probe for a compatible locking adapter and refuse mutations if unavailable.
3. Validate ownership, supported versions and expected revision. Use staged writes and atomic publication. `Store::replace_config` additionally compares the expected SHA-256 of the existing config file (or expected absence), so stale edits fail.
4. Release the lease. Restart only if the prior state warrants it and the resulting data/configuration is valid. A partial restore or failed validation must not trigger a blind restart.

The runtime holds the OS lease for its lifetime and shares one `Store` handle internally. Consistent export also needs exclusive ownership; ordinary read-only inspection may use an explicitly stale health snapshot. Session/process exit releases the OS lease; staged files alone never become authoritative. REM-41/42 own SSH transport and companion UI implementation.

## Export, restore and migration

`Store::export` creates a new directory containing `backup.json` and verified content-addressed objects. The completion marker is written last. A nonsecret configuration snapshot is included when captured by the runtime. Tokens, environment files, outbox/session state, caches and binaries are excluded. Copy/archive the whole completed directory using normal public file tools; a partial copy is not a verified backup.

`Store::restore` validates paths, versions, inventory, sizes, hashes and lineage into a new generation. Restore into an existing store is additive: absent input is not deletion, and conflicts/tombstones remain. Activation replaces `CURRENT` atomically; the prior generation/source remain available. Restored settings are retained as `restored-config.json` in the new generation for deliberate review, never automatically applied to a different device's active config. A new empty store keeps its newly generated actor ID and never clones pending device operations.

`MigrationRegistry` accepts explicit code-registered source/target adapters. The shipped version-1 registry has no historical migration because no earlier generic store shipped. Tests register a clearly synthetic v1-to-v2 layout adapter and exercise failures before/after activation and rollback retention. A v1 runtime refuses that unsupported actual v2 format. Future domain migrations require their own implemented adapters/readers; legacy Reader files are untouched.

Binary replacement/reinstall must retain these roots. Host fixtures validate that separation. Actual vendor-update, factory-reset and native power-loss survival remain unverified; keep a separate verified export. Factory reset is treated as potentially destructive, including loss of local authorization. No reset/update/tablet operation was used for REM-36 validation.

## Optional Drive protocol

Sync is off by default. Enabling it requires deliberate collection/account binding and protected credentials. Namespace and media selection applies independently in both directions. Memory does not enable handwriting; conversation/export/source namespaces and media are explicit. Default media limit is 32 MiB, configurable up to the supported 256 MiB bound. Limits/deferred data are reported, not silently described as full recovery.

The worker starts after local runtime initialization, never waits for network before local input, wakes after durable commits and polls remote changes without requiring local edits. Default polling is 60 seconds with jitter; batches default to 32 items. Network work occurs outside the store mutex. Wake signals are only hints; durable outbox/observation state drives replay. Shutdown cancellation has bounded waiting and pending transfers resume from durable state. Missing credentials or damaged/stale sync state pauses sync while Reader/local storage continues.

Drive uses ordinary immutable JSON/binary files in `appDataFolder` under `drive.appdata` scope. App-private storage cannot be shared, moved between spaces or trashed; users/app removal can delete it. It is an optional recovery set, not a shareable or deletion-proof backup. Independent export remains available. No remote physical delete, trash, sharing or moving is implemented.

Objects are uploaded before an immutable transaction manifest. There is no mutable shared head and no reliance on unverified media `If-Match` behavior. Generated Drive IDs are journaled with exact content identity before upload and reused after uncertain completion; a 409 only succeeds after metadata and content verification. Large uploads use bounded streaming chunks, server-confirmed offsets and explicit expired-session restart with the same file ID. Tokens/session URLs are excluded from normal diagnostics/exports.

A transport manifest is a selected-record projection of local transactions, never the original all-domain manifest. Excluded domain objects and identifiers are absent from projection metadata. Selected opaque payload associations remain intact and do not recursively enable another domain. Each media descriptor has included or explicitly omitted coverage. History-only transactions can be complete as metadata while incomplete as media recovery. Later media availability adds immutable coverage without changing logical revision IDs or conflict heads. Disabling a policy preserves existing local/cloud content.

Receivers inspect namespace metadata before fetching record payloads, then verify it against decoded envelopes. Disabled domains/media remain deferred and replay when policy changes. A durable fair queue prevents earlier unresolved children from starving later parents. Full paginated discovery precedes publication; a start token captured before listing closes the initial arrival race. Durable observations survive cursor replay. Rejected cursors trigger fresh discovery without forgetting prior evidence. Missing remote items, `removed`, 404, lost access or an unexpectedly empty prior collection pause recovery; they never manufacture domain tombstones or recreate cloud defaults.

## Manual credentials and evidence boundary

Grant acquisition/consent UI remains REM-41/42. A maintainer can use the official installed-application OAuth flow with their own client and the app-data scope, then provision an already-owned credential root under the maintenance protocol. `drive.json` has `credential_version: 1`, `client_id`, nullable `client_secret`, `access_token`, `refresh_token`, Unix `expires_at`, granted `scopes`, `account_permission_id`, and the selected `collection` UUID. Validate the selected account using Drive `about.get` before writing the binding. The runtime rechecks it before publication and refreshes authorized expired tokens. Never place populated files in source control or an export.

Public tests use synthetic records, fake grants and in-memory/localhost transport fixtures. They exercise actual HTTP request construction, pagination, generated IDs, 409 verification, resumable expiry/offsets, token refresh, failures and two-device recovery. They are not live-account or native-device evidence. No user Drive connection, upload, consent or tablet mutation is authorized or performed by this implementation lane.

Protocol sources and survival limits: [REM-36 research](../openspec/changes/shared-storage-sync/research.md), [Drive app data](https://developers.google.com/workspace/drive/api/guides/appdata), [uploads](https://developers.google.com/workspace/drive/api/guides/manage-uploads), [error handling](https://developers.google.com/workspace/drive/api/guides/handle-errors), [installed-application OAuth](https://developers.google.com/identity/protocols/oauth2/native-app).
