## ADDED Requirements

### Requirement: Deliberate bounded edits to supported saved fields
The producer SHALL accept only explicit set/clear of current trigger corner, log level and debug dump under contract.md. It SHALL preserve unrelated decoded values and declaration origins, keep a no-op byte-identical, and never change credentials, paths, schema, mode, data or runtime/provider state.

#### Scenario: Selected declarations change
- **WHEN** a supported explicit set/clear patch is prepared and conditionally applied
- **THEN** only those root declarations change, all unrelated values/origins remain intact and a logical no-op writes nothing.

#### Scenario: Invalid or expanded patch
- **WHEN** unknown fields, nested extras/duplicates, invalid types/values, unsupported schema, paths, missing conditions or byte bounds fail
- **THEN** the command refuses before publication without general Config editing or fallback.

### Requirement: Existing guarded atomic write and honest readback
Apply SHALL reuse the existing exclusive Store/mutex/CAS atomic writer with current validated ordinary or explicitly selected-aware custody and unchanged declared roots. It SHALL NOT initialize, repair, retarget, activate, stop or restart anything. Exact disk readback SHALL remain distinct from runtime activation and possible post-publication failures.

#### Scenario: Changed base or active owner
- **WHEN** the original file revision changes or current existing Store admission is Busy/unsupported
- **THEN** publication is not dispatched and the original conditions are not refreshed or weakened.

#### Scenario: Verified save or uncertain publication
- **WHEN** exact target readback succeeds or a failure occurs after publication might have happened
- **THEN** the result is respectively verified disk/restart-required or unknown, never invented rollback or automatic retry.

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
