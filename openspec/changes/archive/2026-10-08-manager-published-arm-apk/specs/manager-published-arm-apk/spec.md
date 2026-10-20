## ADDED Requirements

### Requirement: Distinct published asset qualification
The Manager developer harness SHALL qualify pinned unchanged ARMv7 and AArch64 apk assets through a verified explicit emulator, with published-asset evidence distinct from local source-build evidence. It SHALL preserve the original source-build417entrygate and refuse mismatched inputs before execution.

#### Scenario: Published bytes have known identity
- **WHEN** downloadedasset and emulator match the adapter's pinned identities and a valid distinct local evidence receipt
- **THEN** fixed emulator/tool invocation runs only in isolated taskcontainers and records asset/runtime/emulatoridentity without claiming signed provenance or hardware compatibility

#### Scenario: Input identity or mode is inconsistent
- **WHEN** asset/emulator digest, receipt identity or mode arguments mismatch
- **THEN** qualification refuses before launch and does not reinterpret the input as a sourcebuild

### Requirement: Actual ARM fixture behavior
The harness SHALL reuse all13actualtool observations for both ARM assets, retain signature refusal classifications, full revision/database/script/ownership semantics, unchangedroots, absent script sentinel and existing isolation/cleanup. Synthetic metadata SHALL NOT assert ARM package compatibility.

#### Scenario: Both assets complete bounded observations
- **WHEN** signed, tampered, untrusted, version and seeded database cases execute
- **THEN** each asset must satisfy the existing exact assertions under emulation, with explicit emulatedoffline evidence and no installation eligibility

#### Scenario: Original source build remains available
- **WHEN** originalsourcebuild mode is selected
- **THEN** its exact source/archive/binary/image checks and417entrygate remain enforced without an emulator
