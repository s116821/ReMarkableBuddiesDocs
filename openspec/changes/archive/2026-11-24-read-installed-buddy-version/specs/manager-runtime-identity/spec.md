## ADDED Requirements

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
