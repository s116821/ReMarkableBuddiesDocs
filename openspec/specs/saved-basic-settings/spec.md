# Saved basic-settings producer

## Purpose
Deliberately edit only the three supported saved declarations through the existing guarded atomic writer. Verified disk bytes remain distinct from runtime activation and historical publisher identity. The immutable [accepted contract](https://github.com/s116821/ReMarkableBuddiesDocs/blob/82717f481005bfd403ec35c149dfbbf28805d156/openspec/changes/edit-saved-basic-settings/contract.md) fixes wire shapes, bounds and phases. Its shared-host/editor obligations remain unimplemented in the active [companion change](../../changes/edit-saved-basic-settings-companion/proposal.md); they are not producer delivery claims.

## Requirements

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

### Requirement: Bounded private intent and read-only desired-file observation
The producer SHALL prepare a private intent bound to the original base/path and exact deterministic target bytes. It SHALL expose only the contract's bounded three-field declarations and private intent data, never arbitrary configuration values. Status SHALL read only the original selected file and compare the complete original target; it SHALL NOT mutate, refresh conditions, prove historical publisher identity or infer runtime activation. A later refusal SHALL NOT settle an earlier possibly dispatched apply.

#### Scenario: Exact desired file after an uncertain apply
- **WHEN** the original intent is checked after its complete apply report is unavailable
- **THEN** status reports desired-file-observed only for exact complete target bytes, otherwise unresolved, without replaying apply or claiming who published those bytes.

#### Scenario: Refused reconciliation
- **WHEN** a status request, file read or original intent fails admission
- **THEN** its bounded refusal does not acknowledge, roll back or settle an earlier apply.
