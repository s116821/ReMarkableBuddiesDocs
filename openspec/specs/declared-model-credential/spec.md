# Declared protected model credential

## Purpose
Deliberately manage only the existing saved model-credential reference with confidential original conditions and truthful file observation. The detailed [contract](../../changes/archive/2026-10-22-manage-declared-model-credential/contract.md) fixes the exact protocol. Host UI, new reference binding, provider/runtime/native qualification and remaining delivery checks are separate.

## Requirements

### Requirement: Deliberate fixed-reference protected credential maintenance
The producer SHALL install/replace/remove only the already declared protected model-credential file under contract.md, preserve exact UTF8 text and existing permitted private mode, and refuse absent reference, unsafe aliases/permissions or changed original conditions without Config/reference/runtime/provider changes.

#### Scenario: Install or replace exact pasted text
- **WHEN** an explicit original-bound install or replacement supplies valid bounded UTF8 text
- **THEN** exact decoded bytes including CRLF/trailing contents are published through the owned writer, no race-created install target is overwritten, and only exact readback/private permissions can verify.

#### Scenario: Remove or refuse changed state
- **WHEN** deliberate removal or a changed original file/config/root/metadata condition is encountered
- **THEN** only the admitted file is unlinked and directory-synced, or the operation refuses without refreshing conditions, repairing permissions or changing unrelated data.

### Requirement: Confidential conditions and same conditional custody
Secret text and secret-derived fingerprints SHALL remain confidential host transport state. Reports SHALL never echo credential bytes/reference/path/error text; public UI/logs SHALL receive no confidential intent/fingerprint material. Apply SHALL reuse current existing Store/mode ownership and one narrow same-mutex conditional writer through consuming output.

#### Scenario: Secret-like text or output failure
- **WHEN** pasted values contain controls/Unicode or output fails after a prefix
- **THEN** exact accepted bytes remain unchanged, reports contain no secret text, no second report/replay occurs and custody is retained until consumption ends.

#### Scenario: Busy, non-Linux or unsafe filesystem
- **WHEN** current ownership, platform privacy/durability prerequisites or original admission cannot be established
- **THEN** bounded truthful refusal occurs without fallback, initialization, credential discovery or provider execution.

### Requirement: Saved-file observation is not effective authentication
All operations SHALL report runtime unverified. Status SHALL require original confidential intent and prove only desired current bytes/private permissions or absence under unchanged original Config/root conditions, never historical publisher identity, active environment selection or provider validity.

#### Scenario: Possible publication or removal
- **WHEN** publication/unlink may have occurred without a complete verified report
- **THEN** the original invocation remains unknown without rollback/replay, and later status/refusal cannot falsely settle its history.

#### Scenario: Explicit current observation
- **WHEN** desired current saved state can be inspected under the original bindings
- **THEN** status reports desired-file-observed or unresolved without raw replacement text, Store/provider probe or effective-authentication claim.

### Requirement: Scoped ordinary notebook protected-file admission
The existing Linux protected-model-credential Apply SHALL admit a ready owned ordinary notebook through a distinct file-specific entry under the original exclusive Store/mode custody, reusing the complete current notebook gate. It SHALL require exact identity/current/readiness/capabilities, definite absent/empty selected and retained history, complete local recovered manifests and validated absent/LocalOnly mode without initialization/adoption/repair. Legacy selected-aware1/2/3 and supported mode behavior SHALL remain. Other writers and legacy-only maintenance admissions SHALL not inherit this scope.

#### Scenario: Exact original notebook credential operation
- **WHEN** supported ready notebook custody and every original confidential file/config/parent/action condition match
- **THEN** the existing sealed single writer may install, replace or remove only the declared protected file under unchanged text/private-mode/no-clobber/readback rules, preserving Config/reference/owned data/media and unrelated credentials.

#### Scenario: Busy or unsupported notebook state
- **WHEN** notebook ownership/readiness/layout/history/mode/current state is busy, unavailable, corrupt or interrupted
- **THEN** existing refusal categories apply before publication without repair/fallback, broad cleanup or configuration/data change.

#### Scenario: File observation is separate from reference and runtime
- **WHEN** a notebook file operation verifies or becomes uncertain
- **THEN** existing confidential report/custody/status and runtime-unverified rules remain, with no reference edit, effective authentication, revocation, atomic two-file setup, rollback or automatic replay.
