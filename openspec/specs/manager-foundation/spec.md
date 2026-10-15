# Manager foundation

## Purpose

Describe the implemented shared Angular browser/Electron foundation and independent
release policy. This bounded REM-21 capability does not deliver REM-41 tablet
installation/updates or REM-42 configuration/data management. Semantic release
behavior preserves REM-30 and reserves the 1.0 gate for REM-35.

## Requirements

### Requirement: Shared browser and desktop foundation
The Manager SHALL render one Angular UI in browsers and Electron and SHALL state
when tablet transport and installation/update/configuration features are unavailable.

#### Scenario: Start either supported host
- **WHEN** a user opens the browser distribution or portable desktop distribution
- **THEN** the same Manager screen identifies its host/version and shows tablet
  connection as not configured, with no claim of installation or update success.

### Requirement: Restricted desktop boundary
Electron SHALL isolate and sandbox the renderer, disable Node integration, deny
unexpected navigation/popups/permissions, and expose foundation host identity plus
only separately specified narrow host capabilities. Arbitrary command IPC SHALL
remain unavailable. Neither distribution SHALL connect to a Buddy service API.

#### Scenario: Renderer inspects privileged capabilities
- **WHEN** the foundation screen executes in Electron
- **THEN** Node require/process and arbitrary command IPC are unavailable.

### Requirement: Independent semantic release policy
Manager SHALL derive official versions from immutable Git tags on application
squash commits using maintained semantic tooling. Pure documentation merges SHALL
create no tag or application build. UI releases SHALL not trigger Rust builds.

#### Scenario: Documentation-only merge
- **WHEN** only explicitly classified documentation paths change
- **THEN** required PR checks finish and main skips application compilation and tags.

#### Scenario: Relevant semantic change
- **WHEN** a scoped feat, fix, maintenance or breaking application commit is processed
- **THEN** semantic tooling computes the version from actual history; docs titles
  concealing code are rejected and major 1+ publication is blocked pending REM-35.

### Requirement: Exact source and recoverable artifacts
Manager SHALL freeze a read-only candidate version and source SHA, build its
browser/desktop artifacts, and test those exact bytes before final tagging or
publication. Its one final main-only release job SHALL reuse their verified
inventory/digests. Recovery SHALL not replace tags, overwrite differing assets,
rebuild substitutes or convert a failed/skipped predecessor into a successful gate.
Source: REM-56 superseding earlier tag-before-build ordering.

#### Scenario: Release interruption and retry
- **WHEN** build, integration or final upload is interrupted
- **THEN** failed predecessors create no new official tag/release; final-job recovery verifies the exact candidate/source/artifacts and retained matching bytes before publication.

### Requirement: Public central workflow
All Manager OpenSpec artifacts and workflow skills SHALL reside in Docs, with
linked implementation PRs, exact revision evidence and coordinated merge order.
Public setup and checks SHALL not require private integrations or a tablet.

#### Scenario: Public contributor builds Manager
- **WHEN** a contributor follows the central guide with a normal public clone
- **THEN** pinned setup and host/release tests are runnable with documented tools.
