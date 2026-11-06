## MODIFIED Requirements

### Requirement: Independently pinned public fixture inputs
The observer SHALL preserve its historical six-file legacy-no-sdk default and
SHALL accept a current resident fixture only through an explicit independently
pinned external manifest. The current original root SHALL remain the exact five
public artifacts/receipt, read-only and unchanged; its bounded manifest, source/
version/SDK metadata and actual public DER-SPKI SHALL be independently checked.

#### Scenario: Historical fixture
- **WHEN** the existing legacy input/default is selected
- **THEN** its original schema, three-file ordinary payload,32MiB APK bounds,
  independent trust pins and ineligibility behavior remain unchanged

#### Scenario: Explicit current resident handoff
- **WHEN** the schema2 external manifest and original five public files match
  independent pins and current finite source/profile/SDK/size constraints
- **THEN** only the current public-key-only fixture observation may proceed

#### Scenario: Unrecognized or changed input
- **WHEN** profile, inventory, manifest/receipt/file identity or size differs
- **THEN** admission refuses without rewriting originals or granting authority

## ADDED Requirements

### Requirement: Finite resident signed fixture correspondence
The current fixture observer SHALL require exact reviewed ARMv7 resident and
AArch64 ordinary SDK-bound layouts, modes/root ownership, source/version/pkgrel,
SDK/bundle/profile/dependency/tag and authenticated-index correspondence. A
manifest alone SHALL NOT invent allowed paths or prove compiler/native provenance.

#### Scenario: Complete current metadata
- **WHEN** signed metadata and index match independently pinned canonical build
  bytes and the finite reviewed per-target layout
- **THEN** the report may describe those actual public-only correspondences

#### Scenario: Changed resident or ordinary contract
- **WHEN** SDK/feature/bundle/firmware/dependency/layout/mode/source/tag/index differs
  or a script/trigger/link/unknown path appears
- **THEN** observation refuses and update/install eligibility stays false

### Requirement: Preserve bounded operation and qualification limits
The extension SHALL reuse readonly no-network verify/adbdump and existing negative
controls, nonroot ownership, snapshots and bounded timeout cleanup. It SHALL NOT
sign, mutate a package database, execute/extract payloads, enable a runtime profile
or infer production trust/install/native support. Actual invocation requires deliberate opt-in execution and is distinct from
synthetic source controls.

#### Scenario: Successful current public-only result
- **WHEN** a deliberate opt-in actual operation completes all original-byte and
  controlled signature/integrity checks with owned cleanup
- **THEN** its result remains test-key, installation-ineligible host evidence
