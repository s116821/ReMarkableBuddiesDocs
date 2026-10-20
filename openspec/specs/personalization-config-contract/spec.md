# personalization-config-contract

## Purpose

Define the optional portable preference and bounded existing-writer configuration maintenance contract, separately from receiving-runtime activation and synchronization.

## Requirements

### Requirement: Optional portable personalization setting
The configuration SHALL contain defaulted version1 personalization enabled/text settings. It SHALL preserve valid multiline UTF-8 bytes up to16384, reject NUL/unsupported version, retain disabled text and make unset/empty text ineffective without deleting other settings/history/learning. Debug output SHALL redact the text.

#### Scenario: Default, disabled and exact text
- **WHEN** an old config is loaded or personalization is edited/disabled/cleared
- **THEN** old/default behavior is preserved, valid text roundtrips unchanged and only the selected preference changes.

### Requirement: Guarded existing-writer maintenance
The fixed inspect/set/disable/clear CLI SHALL select an existing configuration explicitly, bound strict mutation stdin, compare the whole-file revision and reuse existing Store ownership/exclusive lease/atomic replace. It SHALL refuse active/missing/unsupported stores, stale revisions and invalid input without credential/provider/device startup or a new backend writer.

#### Scenario: Mutation and verified readback
- **WHEN** a stopped owned Store and current config revision are supplied
- **THEN** only personalization changes, the exact setting/digest reload from disk is verified and no routine log contains the text.

#### Scenario: Refusal
- **WHEN** ownership, version, revision, input or lease validation fails
- **THEN** the command reports a fixed sanitized failure and cannot claim a verified successful write.

### Requirement: Honest reload and request snapshot boundary
The maintenance report SHALL distinguish verified disk reload from running-runtime activation, reporting restart-required rather than claiming the running Reader/Writer changed. Validated preference snapshots SHALL be immutable; new verified loads may produce a new snapshot without mutating an in-flight snapshot. This preference SHALL NOT represent operation/safety grants or rewrite request/history.

#### Scenario: Snapshot before and after reload
- **WHEN** a saved preference is validated and loaded after a prior snapshot was taken
- **THEN** the new snapshot reflects the setting while the prior snapshot remains unchanged, with receiving-buddy/provider/sync qualification explicitly separate.
