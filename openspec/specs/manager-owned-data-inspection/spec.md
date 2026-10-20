# Shared Manager owned-data inspection

## Purpose

Describe the accepted bounded read-only CLI report integration through the shared
browser and Electron UI on supported existing host adapters. Windows native
inspection, deployment and broader data maintenance remain separately qualified.

## Requirements

### Requirement: Shared read-only owned-data inspection
Manager SHALL consume the reviewed report_version1 CLI through the existing wired host adapters in the shared browser and Electron UI without a Buddy service API or cleanup mutation.

#### Scenario: Explicit inspection on an observed tablet
- **WHEN** the user requests inspection with a current supported read-only profile
- **THEN** the host runs only the fixed known CLI and verifies the same cable/route/boot session before displaying a bounded validated report

#### Scenario: Older installed Buddy lacks inspection
- **WHEN** the fixed executable or inspection option is unsupported
- **THEN** Manager displays unsupported and performs no ordinary Reader startup or alternate filesystem inspection

### Requirement: Honest accounting and exclusions
Manager SHALL preserve report status and distinguish missing, uninspected, omitted and unavailable from an inspected empty category, with no reclaimable-space or native-health inference.

#### Scenario: Partial report and shared references
- **WHEN** a report contains partial inventory or shared/missing/omitted media
- **THEN** Manager shows observed apparent bytes, absent complete total and distinct counts with nonadditive domain media explanations

#### Scenario: Uninspected cache or diagnostics
- **WHEN** a category has no inspected value
- **THEN** Manager displays not inspected rather than zero and identifies excluded credentials/native documents

### Requirement: Inspection admission and stale result refusal
Manager SHALL validate report schema and host result and discard results after disconnect, changed session or cancellation.

#### Scenario: Connection changes during inspection
- **WHEN** a late reply belongs to an earlier boot, connection or UI request
- **THEN** no report becomes current and the user must explicitly observe again

#### Scenario: Invalid or future report
- **WHEN** report shape, schema or restricted disclosure claims do not match the supported contract
- **THEN** Manager shows unsupported or unavailable without displaying raw output or secret-bearing errors
