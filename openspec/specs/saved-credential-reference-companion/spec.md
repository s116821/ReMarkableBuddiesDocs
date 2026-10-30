# Saved credential-reference companion

## Purpose
Provide deliberate saved-only model credential-reference editing in both Manager companions.
The complete [consumer contract](../../changes/archive/2026-10-26-edit-saved-credential-reference-companion/contract.md)
defines fixed interfaces, private-name lifetime, original reconciliation and shared custody.
The [Manager manual](https://github.com/s116821/ReMarkableBuddiesManager/blob/main/docs/credential-reference.md)
keeps reference editing separate from credential-file operations and effective authentication.
Runtime activation remains unverified.

## Requirements

### Requirement: Shared deliberate saved credential-reference editing
Both companions SHALL expose the optional dedicated original-bound credentialReference editor under contract.md, preserving exact supported name spelling, missing/null/no-op declarations and full producer validation while showing only saved origin/presence. Source basis: canonical saved-model-credential-reference, archived producer contract/manual and current Config credential_name implementation.

#### Scenario: Explicit set, clear or keep
- **WHEN** a user begins an observed editor and deliberately sets a valid private name or clears the declaration
- **THEN** only the original-bound fixed change is prepared and applied at most once, producer no-change skips apply, Keep dispatches nothing and no name normalization, Config repair or credential-file operation follows.

#### Scenario: Invalid or stale input
- **WHEN** shape/type/duplicate/name/bounds/identity/path/file/change/target validation or capability admission fails
- **THEN** the bounded invocation refuses without private input echo, refreshed intent, fallback or broader authority.

### Requirement: Private lifecycle and original uncertainty
The consumer SHALL clear private draft and actual input synchronously at the contract boundaries, retain no raw name/change after possible apply, and preserve bounded hash-only originals for explicit status. Source basis: producer original-intent semantics and existing private editor/token/generation interfaces.

#### Scenario: Submission or invalidation
- **WHEN** Save, refresh, other maintenance, observation, disconnect, reload/pagehide, Stop, expiry or destruction supersedes a private editor
- **THEN** draft and actual DOM clear before the relevant await/event boundary, late replies cannot refill/clear a newer editor, and old ready text does not establish a fresh setup generation.

#### Scenario: Possible publication or unresolved followup
- **WHEN** apply may have run or unresolved status is followed by cancel/failed/late status
- **THEN** only the original reference/identity/hash-only intent supports read-only reconciliation, no retry/reapply/eviction occurs, unknown/null-report fallback retains the last unresolved original, and later refusal does not settle it.

### Requirement: Saved-only authority and shared seven-lane custody
The consumer SHALL keep reference editing separate from credential files/authentication/runtime, preserve existing peer uncertainty and use the shared owner across all seven actual lanes through independently reviewed both-host delivery. Source basis: canonical producer separation contract, current six-lane Manager factories and REM42 consumer ownership.

#### Scenario: Reference change or other maintenance ownership
- **WHEN** a reference change verifies, another lane owns I/O or stale cancellation/completion races newer work
- **THEN** saved-only/runtime-unverified results grant no credential-file action/readiness/revocation/two-file transaction or settlement of an older file original; all42 directed peer pairs preserve Busy without hooks/cancel/I/O and token/generation isolation.

#### Scenario: Attributed linked delivery
- **WHEN** this consumer is proposed for delivery
- **THEN** unchanged historical reports retain original attribution, synthetic/parser evidence is separate, actual guarded browser/Electron and both-OS source/retained checks plus independent reviews precede own canonical sync/archive/final Docs-first delivery, with actual publication and broad REM42/MVP separately observed.
