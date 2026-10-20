## ADDED Requirements

### Requirement: Private intent and read-only desired-file reconciliation
The host SHALL retain original base/path/target evidence privately before one apply dispatch and SHALL expose only a reduced safe view/opaque reference. Status SHALL only observe exact original target bytes and SHALL NOT prove historical publisher identity, refresh conditions, mutate or settle uncertainty from later command refusals.

#### Scenario: Lost apply report
- **WHEN** apply may have run but its complete verified report is unavailable
- **THEN** original evidence remains unknown and explicit status can report desired-file-observed only for exact prepared target bytes without replaying apply.

#### Scenario: Fresh deliberate edit after an unknown outcome
- **WHEN** the user explicitly begins a distinct edit from fresh current state
- **THEN** it has new conditions/reference and preserves the prior diagnostic without claiming rollback or evicting unresolved evidence at capacity.

### Requirement: Shared explicit editor with preserved session lifetime
Both browser and Electron SHALL offer the same three-field saved editor using protected fixed host adapters, no-saved-override choices, truthful origins and neutral pending/readback status. Before-I/O external invalidation, original receiver, serialized cancel and after-await generation checks SHALL preserve ready/unknown references and unrelated memory-forget uncertainty.

#### Scenario: Refresh or navigation races a save
- **WHEN** cancellation, same-ID refresh, real document navigation or target change occurs
- **THEN** ready references and late views are invalidated while possibly dispatched original apply remains unknown with no repeat.

#### Scenario: Saved preference versus running behavior
- **WHEN** a disk save or desired-file observation succeeds
- **THEN** both hosts show its exact limited saved-state result without service/provider checks, automatic restart or effective environment claims.
