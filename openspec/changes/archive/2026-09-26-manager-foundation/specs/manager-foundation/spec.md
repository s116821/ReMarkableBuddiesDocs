## ADDED Requirements

### Requirement: Shared browser and desktop foundation
The Manager SHALL render one Angular UI in browsers and Electron and SHALL state
when tablet transport and installation/update/configuration features are unavailable.

#### Scenario: Start either supported host
- **WHEN** a user opens the browser distribution or portable desktop distribution
- **THEN** the same Manager screen identifies its host/version and shows tablet
  connection as not configured, with no claim of installation or update success.

### Requirement: Restricted desktop boundary
Electron SHALL isolate and sandbox the renderer, disable Node integration, deny
unexpected navigation/popups/permissions, and expose only foundation host identity.
Neither distribution SHALL connect to a Buddy service API.

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
Official browser and desktop artifacts SHALL be built only after the remote tag
exists at the exact source SHA. Runtime metadata, package names and checksummed
provenance SHALL agree. Local and PR builds SHALL identify themselves as development.

#### Scenario: Release interruption and retry
- **WHEN** a build or upload fails after tagging and main advances
- **THEN** retry recovers that tagged source before later versions, preserves
  completed artifacts and verifies checksums before publishing a draft.

### Requirement: Public central workflow
All Manager OpenSpec artifacts and workflow skills SHALL reside in Docs, with
linked implementation PRs, exact revision evidence and coordinated merge order.
Public setup and checks SHALL not require private integrations or a tablet.

#### Scenario: Public contributor builds Manager
- **WHEN** a contributor follows the central guide with a normal public clone
- **THEN** pinned setup and host/release tests are runnable with documented tools.
