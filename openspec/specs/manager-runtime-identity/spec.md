# Manager binary self-report observation

## Purpose
Read the known Buddy binary identity through the existing authenticated wired hosts without treating its echo as package or running authority.

## Requirements

### Requirement: Bounded authenticated known-binary identity observation
Both Manager distributions SHALL explicitly inspect the existing known Buddy binary's self-reported version through a fixed bounded host-owned command after the configured wired peer/connection/boot and safe executable metadata are checked. No arbitrary path/command, Vellum initialization, Buddy service API or tablet configuration mutation SHALL be introduced.

#### Scenario: Read known binary version
- **WHEN** the current verified connection and safe known binary return one supported bounded CLI release or Git-derived development identity line with stable metadata/observation brackets
- **THEN** the host returns sanitized self-reported identity to the shared UI without exposing credentials or invoking runtime/provider startup.

#### Scenario: Missing, unsafe or malformed identity
- **WHEN** the known binary is absent/unsafe, the command is unsupported, or output violates the exact identity shape, byte or time bounds
- **THEN** the UI reports unavailable/unsupported without echoing arbitrary stdout or trying another path.

### Requirement: Identity freshness and narrow host admission
The capability SHALL reuse current wired/session/frame/origin protections and suppress stale results after cancellation, connection/boot or executable/observation drift. The caller SHALL carry only the fixed operation/current opaque identity, never a remote path or command.

#### Scenario: Changed or cancelled observation
- **WHEN** connection, boot, executable metadata or request generation changes while the identity is read
- **THEN** no old identity is reported current and a fresh supported observation is required.

#### Scenario: Unauthorized caller
- **WHEN** caller/session/origin/frame or input shape is invalid
- **THEN** the action refuses before the fixed inspection is dispatched.

### Requirement: Self-report does not establish package or running authority
The shared UI SHALL label binary identity as self-reported and display unknown package ownership/provenance and running-process identity distinctly. An echoed version SHALL NOT be treated as a trusted Git tag, SDK/firmware compatibility, update/downgrade order or installation eligibility.

#### Scenario: Valid echo with unqualified provenance
- **WHEN** a valid binary version is observed without separate package/runtime proof
- **THEN** the value is displayed as reported while provenance/running/eligibility remain unverified and existing installation remains disabled.

### Requirement: Report the executable selected by the supported Buddy installation

When reading the binary version, both Manager hosts SHALL use the existing fixed-path launcher resolver. The version command SHALL use the selected executable and only the fixed `--version` argument. The host SHALL verify every protected parent directory and executable, and discard the report if the selected path changes during the read.

#### Scenario: Resident and standalone installations

- **WHEN** a loaded service points to the recognized resident or standalone Buddy executable and the existing wired, boot, metadata and output checks pass
- **THEN** Manager displays that executable's self-reported version.
- **WHEN** the service is absent and its launcher record is empty
- **THEN** Manager checks the known standalone executable.

#### Scenario: The selection disappears or changes

- **WHEN** the selected executable is absent, its parent is unsafe, the unit names an unrecognized executable, or its selected path changes during the read
- **THEN** Manager withholds the version and does not probe a second executable.
