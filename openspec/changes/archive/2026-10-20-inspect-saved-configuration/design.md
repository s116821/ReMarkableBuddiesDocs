# Design

## Decision and authority
Read exactly one explicitly selected saved configuration, deserialize the actual typed Config, apply pure value validation, and project only a fixed allowlist. Do not call Config::load or Config::validate: they traverse declared storage roots through StorePaths::validate. The new snapshot deliberately does not establish path admissibility. Only the selected config path and its ancestors may be inspected to admit the bounded regular-file read. Declared data/cache/credentials paths are neither probed nor opened, even for metadata.

Preserve the existing REMARKABLE_BUDDIES_CONFIG selector. No new --config flag. Main source routes the new command before dotenv, environment/key resolution and runtime initialization. The snapshot is one saved-byte observation; it does not assert that the file remains current at stdout or is active in any service. No hash is a later write grant.

## Privacy and strictness
Never serialize Config wholesale. Model, endpoint, credential reference, declared paths, memory identities/selection binding and sync collection are presence-only. Endpoint validation currently permits userinfo/query/fragment/opaque token strings; configured presence avoids pretending redaction is safe. Personalization exposes enabled, schema version, text-present and UTF8 byte count, not text/hash. General snapshot does not replace the existing deliberate editor.

Typed deserialization occurs directly from raw bytes before any Value map for origin tracking, so duplicate typed fields cannot disappear. A duplicate-aware recursive second parse of those same bytes rejects any remaining repeated object names before constructing the origin map. Reject duplicate namespace elements rather than silently normalizing a BTreeSet. Unknown schema/shape refuses the entire view. Bounds and failure mapping are in contract.md.

Path declarations remain typed saved data only. Report validation_basis=typed-values-only and declared_roots_validated=false; do not claim full Config::validate success. This avoids adding a second path admission engine or touching unrelated storage. A future path editor needs its own contract.

## Consumer lifecycle
The new host method participates in MemoryForgetHost external-maintenance invalidation BEFORE I/O, as well as shared UI clear and connection/boot/observation generation checks. A same-ID explicit refresh invalidates old pending results. The host strips the raw configuration digest before the renderer. No background refresh loop or visible checking animation is introduced. Browser and Electron use the same strict parser/controller/view; explicit inspection is cancellable and bounded.

## Targeted prior art
At reManager commit b3047fbf12ad51193c5ff05563d2d7d677638c95, app_config.go reads a fixed Xochitl configuration through SFTP and ConfigEditor.tsx separates loaded/original content, validation and explicit save. Reference: https://github.com/rmitchellscott/reManager/blob/b3047fbf12ad51193c5ff05563d2d7d677638c95/frontend/src/components/ConfigEditor.tsx and corresponding app_config.go. This motivates clear saved-state and explicit-action UX only; its raw text editor, unbounded ReadAll and Xochitl writes/service controls are not adopted. No code was executed or copied.

## Delivery
Precode review and explicit consumer agreement precede code. Publish exact producer specimens for consumer parser/transport compatibility. Each component keeps one PR with its associated central artifacts; verify implementation, sync canonical specs and archive only completed own work. Docs-first normal squash, actual trees/main CI and official publication remain separate gates. No model or native qualification is implied by synthetic host tests.
