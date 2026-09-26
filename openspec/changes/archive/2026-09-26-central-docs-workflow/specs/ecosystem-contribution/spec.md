## ADDED Requirements

### Requirement: Central specification ownership
The ecosystem SHALL keep all OpenSpec specifications, active changes, archives, config and workflow skills exclusively in the public Docs repository. Implementation repositories SHALL link to that authority. Migration SHALL preserve original source commit/blob provenance and incomplete change state.

#### Scenario: Historical and unfinished migration
- **WHEN** Rust main and an unfinished branch are migrated
- **THEN** canonical/archive bytes and active branch artifacts are traceable to exact source blobs, and unfinished work remains active without checked-off tasks or canonical sync

### Requirement: Public contribution without private dependencies
Contributors SHALL be able to discover requirements, implementation ownership, public issues/releases and applicable local checks from Docs alone using ordinary Git and local tools, without private reference repositories, Linear, Mem, plugins or tablet access.

#### Scenario: Component task routing
- **WHEN** a contributor starts a Rust, Manager, documentation or cross-component task
- **THEN** central guidance identifies the repositories, commands, spec workflow and any genuine unverified hardware gates

### Requirement: Safe selective workspace setup
The optional bootstrap SHALL default to no component cloning, clone only explicitly selected components, support explicit all-components selection, manual paths and fork URLs, and reuse matching clone/worktree roots without modifying their state. It SHALL reject conflicting paths or remotes before beginning the selected setup.

#### Scenario: Dirty worktree reuse
- **WHEN** a selected component points at an existing valid dirty clone or linked worktree
- **THEN** setup reports reuse and preserves HEAD, branches, tracked changes and untracked files

#### Scenario: Invalid existing destination
- **WHEN** a selected path is unrelated, nested in another repository or has an unexpected remote without an explicit override
- **THEN** setup fails with an actionable message and does not overwrite it or clone other selected components

### Requirement: Coordinated changes with independent releases
Cross-repository work SHALL create full central proposal/design/tasks/deltas before implementation, record linked PRs and exact revisions with merge order, and sync/archive only completed work. Docs-only changes SHALL not trigger application builds or tags. Rust and Manager SHALL retain independent release sources and versions; REM-35 SHALL exclusively own the 1.0 release gate.

#### Scenario: Documentation migration
- **WHEN** central artifacts move from Rust to Docs
- **THEN** the Docs addition precedes Rust removal, both PRs identify the tested revisions, and the Rust release policy classifies the entire migration as documentation-only

#### Scenario: Incomplete parallel work
- **WHEN** another implementation change has outstanding acceptance gates
- **THEN** migration leaves that change active and does not claim its behavior as canonical or completed
