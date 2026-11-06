# personalization-config-contract

## Purpose

Define the optional portable preference and bounded existing-writer configuration maintenance contract, separately from receiving-runtime activation and synchronization. See the [declaration and family contract](../../changes/archive/2026-11-06-preserve-personalization-documents/contract.md).

## Requirements

### Requirement: Optional portable personalization setting
The configuration SHALL contain defaulted version1 personalization enabled/text settings. It SHALL preserve valid multiline UTF-8 bytes up to16384, reject NUL/unsupported version, retain disabled text and make unset/empty text ineffective without deleting other settings/history/learning. Debug output SHALL redact the text.

#### Scenario: Default, disabled and exact text
- **WHEN** an old config is loaded or personalization is edited/disabled/cleared
- **THEN** old/default behavior is preserved, valid text roundtrips unchanged and only the selected preference changes.

### Requirement: Guarded existing-writer maintenance
The fixed inspect/set/disable/clear CLI SHALL select an existing configuration explicitly, bound strict mutation stdin, compare the whole-file revision and reuse existing Store ownership/exclusive lease/atomic replace and exact readback. It SHALL preserve unrelated raw configuration values, omissions and supported null declarations, replacing only the selected personalization member with the existing complete value semantics. It SHALL retain legacy format1 admission and legacy2/3 refusal, and SHALL admit notebook4 only through the existing complete ready ordinary preference gate under the original custody. It SHALL refuse active/missing/unsupported stores, stale revisions and invalid input without credential/provider/device startup or a new backend writer.

#### Scenario: Mutation and verified readback
- **WHEN** a stopped owned Store and current config revision are supplied
- **THEN** only personalization changes, the exact setting/digest reload from disk is verified and no routine log contains the text.

#### Scenario: Refusal
- **WHEN** ownership, version, revision, input or lease validation fails
- **THEN** the command reports a fixed sanitized failure and cannot claim a verified successful write.

#### Scenario: Unrelated saved declarations remain unchanged
- **WHEN** a valid configuration has unrelated absent, sparse or null declarations and personalization is set, disabled or cleared
- **THEN** those unrelated raw JSON values and omissions remain unchanged rather than being materialized through whole typed serialization.

#### Scenario: Ready ordinary notebook
- **WHEN** the exact notebook readiness, complete local history, empty selected/history state and ordinary mode guards pass under existing custody
- **THEN** personalization may change only its configuration target without changing notebook metadata, records or media or repairing storage.

#### Scenario: Legacy selected or unsupported notebook
- **WHEN** legacy format2/3 or a busy, incomplete, nonordinary or selected/retained notebook is supplied
- **THEN** the existing refusal categories are retained without fallback, configuration publication or source repair.

### Requirement: Honest reload and request snapshot boundary
The maintenance report SHALL distinguish verified disk reload from running-runtime activation, reporting restart-required rather than claiming the running Reader/Writer changed. Validated preference snapshots SHALL be immutable; new verified loads may produce a new snapshot without mutating an in-flight snapshot. This preference SHALL NOT represent operation/safety grants or rewrite request/history.

#### Scenario: Snapshot before and after reload
- **WHEN** a saved preference is validated and loaded after a prior snapshot was taken
- **THEN** the new snapshot reflects the setting while the prior snapshot remains unchanged, with receiving-buddy/provider/sync qualification explicitly separate.

### Requirement: Existing personalization report and custody compatibility
Personalization maintenance SHALL preserve its existing version1 input/report and public Report API, private text/readback and uncertainty semantics. The Store lease SHALL span the mutation and verified readback; report output SHALL remain historical data after that lease ends. Output failure SHALL NOT trigger another publication or imply rollback, running activation or output-held custody.

#### Scenario: Report output fails
- **WHEN** the original mutation has settled and report output accepts a prefix or fails immediately
- **THEN** no second publication or replacement report occurs and a successful disk readback remains distinct from current/runtime authority.
