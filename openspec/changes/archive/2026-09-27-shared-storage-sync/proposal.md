## Why

Reader/Writer conversations, source images, export associations, subject memory and handwriting learning need durable local storage before their domain features are built. REM-36 establishes shared persistence and optional Drive recovery without making private accounts, connectivity, memory, or a queryable Buddy service prerequisites.

## What Changes

- Introduce a versioned local store with atomic publication, interruption recovery, stable logical identity/revision lineage, explicit tombstones, migration hooks and verified export/restore.
- Separate durable records/media, rebuildable indexes/cache, temporary diagnostics, nonsecret configuration, credentials and installed components. Document survival evidence and limits rather than promising firmware/reset persistence.
- Add nonsecret file configuration below existing explicit CLI/environment overrides, retaining the lean Reader CLI and protected existing environment file.
- Publish a versioned, offline-readable file/SSH/OS maintenance contract with service quiescence, lock ownership, capabilities and bounded failures. No HTTP/RPC/admin listener.
- Implement opt-in Drive synchronization of immutable logical revisions with local working copies, independently selectable memory/handwriting domains and explicit conversation/media policy. Detect conflicts instead of overwriting; preserve local data on transport removals or lost access.
- Add deterministic offline transport/storage fixtures for two devices, restore, deletion/conflict, retries, corruption and interrupted migrations. No real user Drive or tablet operations in this lane.

## Capabilities

### New Capabilities
- `shared-storage`: versioned durable layout, generic record/blob primitives, configuration, credentials boundary, migration/export/restore and maintenance contract.
- `optional-drive-sync`: local-first domain policies, immutable Drive protocol, discovery/restore, conflict/tombstone semantics, retries/checkpoints and credential isolation.

### Modified Capabilities
- `platform-runtime`: only **Runtime startup and configuration** and **Implemented product boundary**, as coordinated with REM-9. Preserve diagnostic flags, service identity, logging policy and unrelated requirements.

## Impact

Docs owns `openspec/changes/shared-storage-sync`, the two new capability paths and scoped platform-runtime blocks, plus eventual `docs/storage-contract.md`. Rust changes are planned under `src/storage/`, `src/config.rs`, minimal `src/main.rs`/`src/lib.rs` wiring, `tests/storage*`, `tests/drive_sync*` and owned fixtures. Review any dependencies for hashing/UUID generation and preserve both ARM targets. Shared scaffold, Manager code and REM-9 retirement paths remain with their owners.

REM-37 owns conversation/source schemas; REM-24 subject memory; REM-26 handwriting; REM-23 export semantics; REM-41/42 install, authorization UX and companion management. This change supplies generic infrastructure and a real optional Drive adapter, not those domain features. Neither future Writer nor export may require subject memory to be enabled.

Planning is authorized now. Code starts only after REM-21 Manager acceptance and independent plan review. Keep this change active; no planning-only PR, premature canonical sync or archive. Later deliver linked Docs/Rust PRs with exact revisions and evidence comments; the coordinator alone squash-merges after checks/review. REM-35 alone owns 1.0.
