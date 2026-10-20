## ADDED Requirements

### Requirement: Explicit modes and namespace isolation
The application SHALL expose local-only, isolated device backup and explicitly selected shared-group modes with distinct persistent bindings. A mode transition SHALL preserve local data and pending-work provenance without merging backups or deleting remote namespaces.

#### Scenario: Empty replacement and group join
- WHEN a replacement tablet with no local Buddy data selects an existing verified group
- THEN it pulls committed state before any publication, creates its own device/actor identity, and cannot upload an empty replacement or reuse another device's secrets.

#### Scenario: Leave or switch during pending work
- WHEN pending work belongs to the old backup/group binding and the device switches mode
- THEN the old publisher stops, the pending work cannot enter the new namespace, local data remains recoverable, and no other backup/group is deleted.

### Requirement: Document aggregate and independent global keys
Shared adjudication SHALL group related Buddy records by stable logical source-document identity across conversations, pages and operations. Domain-owned projectors SHALL supply membership without duplicating domain schemas. Global subject memory, handwriting and portable configuration SHALL use independent stable keys.

#### Scenario: Different documents and global records
- WHEN two clients edit different documents and independent global records
- THEN all accepted scopes remain present; applying one scope cannot replace or delete the others.

#### Scenario: Unknown source identity
- WHEN a record lacks an unambiguous stable source-document identity
- THEN isolated backup may preserve it but shared document publication is visibly deferred, without deriving identity from a title, page position or conversation ID.

### Requirement: First valid upstream commit wins the same accepted base
Shared mode SHALL use a provider-qualified exclusive commit primitive. All contenders for a base SHALL address the same commit location; success/uncertainty SHALL resolve by verified committed content. A losing stale local aggregate SHALL be replaced by the accepted upstream aggregate and SHALL NOT be republished against a later base.

#### Scenario: Concurrent same-base edits
- WHEN A and B create different candidates for the same document/base/commit slot
- THEN exactly one valid upstream commit wins, both clients apply that winner, and the loser retires its old attempt without acquiring a new slot for that payload.

#### Scenario: Lost acknowledgement and old process retry
- WHEN A loses the response after creation and an old process later retries
- THEN it reads/retries the exact same pinned slot; identical operation/digest is acknowledged once, a competing valid winner is adopted, and no successor publication follows without a new edit from the applied base.

#### Scenario: Clock skew and interrupted ownership
- WHEN clocks differ or a process stops during publication
- THEN winner selection does not depend on timestamps, expiry or sleeps; uncertainty remains explicit until the exact commit location is verified, and an invalid/incomplete occupied slot causes recovery-required rather than deletion or alternate-slot bypass.

### Requirement: Unique explicit bootstrap and registration
A group SHALL be selected by verified immutable root identity, not filename. Registration SHALL preserve all existing key-to-genesis mappings and allow only one mapping per stable aggregate key.

#### Scenario: Competing initial registration
- WHEN clients concurrently register the same key
- THEN they converge on the winning catalog's one genesis slot before content publication; a losing different-key registration may retry against the accepted catalog while preserving its existing entries.

#### Scenario: Duplicate group names
- WHEN distinct group roots have the same display label
- THEN joining requires explicit root selection and cannot silently merge them or infer uniqueness from listing order.

### Requirement: Atomic selected view and operation invalidation
Applying an aggregate SHALL verify and stage its complete selected view before one durable local activation boundary. Reader/Writer durable writes SHALL atomically revalidate generation/base with commit. Stored historical branches SHALL NOT resurrect as active shared heads on recovery.

#### Scenario: Pull during an active operation
- WHEN a winning upstream revision replaces a generation used by an in-flight operation
- THEN stale completion cannot append active history, claim success or dispatch native effects; unrelated aggregates remain unchanged.

#### Scenario: Crash around activation
- WHEN a crash occurs before or after activation
- THEN recovery exposes either the prior complete selection or the new complete selection, with no partial mixture or automatic loser re-enqueue.

### Requirement: Serialized native admission and historical settlement
Reader/Writer operations SHALL serialize actual native handoff with selection activation through a domain-owned admission guard. Already-admitted uncertain effects SHALL retain reconciliation guards and prevent conflicting admissions until settled; replacement SHALL NOT retroactively cancel them or infer success.

#### Scenario: Selection races native admission
- WHEN selection activation occurs between a preliminary generation check and attempted native dispatch
- THEN the serialized admission guard refuses stale dispatch, or records admission before activation and requires guarded settlement; the OS process lease alone is insufficient.

#### Scenario: Already-admitted uncertain effect
- WHEN selection changes while an admitted external effect lacks verified completion
- THEN it remains reconciliation-required, conflicting admissions are blocked, and late completion cannot attach stale history to the new selection.

#### Scenario: Undo and drawing handoff invalidation
- WHEN activation invalidates an operation before history mutation or bitmap drawing, or either already-admitted effect returns a late uncertain result
- THEN stale dispatch is refused and uncertain original effects retain historical reconciliation without repeated undo/redo or fallback drawing; imported history/receipts cannot authorize these effects.

### Requirement: Buddy data coverage and native authority separation
Backup/sync SHALL include selected Buddy-owned history, bookkeeping, references, export correlation and portable domain records; screenshot/confirmed-sample media SHALL have explicit coverage. It SHALL exclude native documents/pages/ink/file metadata and device secrets/runtime state. Imported native references SHALL remain historical/unbound until separately verified against current native state.

#### Scenario: Native pages arrive later
- WHEN Buddy history arrives before native cloud pages
- THEN references remain waiting/unbound; no missing-page deletion, recreation, erase, export or undo replay is inferred.

#### Scenario: Large media omitted or missing
- WHEN remote policy intentionally omits a large sample or an included sample is unavailable
- THEN status distinguishes intentional omission from incomplete promised media, retains required local media, and never reports a complete restore for missing included content.

### Requirement: File/OS management status and protected restore
Versioned file/OS contracts SHALL expose mode/identities, committed/applied revisions, generation, successful-sync time, pending/offline/auth/contention/replacement/recovery state and media coverage. Selected backup restore SHALL be an explicit validated hardwired maintenance transaction with rollback and new local actor identity; no Buddy service API SHALL be introduced.

#### Scenario: Corrupt or incompatible restore
- WHEN a selected backup is interrupted, corrupt or has unsupported schema
- THEN existing local state remains active, the restore reports its specific incomplete/incompatible status, and neither credentials nor native source data are replaced.

#### Scenario: Provider unavailable during offline edits
- WHEN internet/auth is unavailable
- THEN local interaction continues with visible pending work pinned to its accepted base; later contention adopts the committed winner rather than auto-rebasing stale edits.

### Requirement: Qualified application visibility
Shared mode SHALL require an explicitly qualified browser/Electron/tablet OAuth application-binding matrix; account equality alone SHALL NOT establish app-data/private-property visibility.

#### Scenario: Unsupported client registration
- WHEN a selected account is used through an unqualified or incompatible OAuth application binding
- THEN shared mode remains disabled or refuses activation, without widening scopes or exposing credentials.
