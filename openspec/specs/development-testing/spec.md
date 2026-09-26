# development-testing

## Purpose

Define portable local testing discovery, evidence gates and scoped native diagnostics for contributors and maintainers.

## Requirements

### Requirement: Discoverable portable development workflow
The repository SHALL provide a separate local simulator testing skill linked from AGENTS and simulator documentation. It SHALL also be usable as a manual checklist with ordinary repository files and CLI tools. Public GitHub discussions, specifications and supplied task requirements SHALL support contributors without private board or agent access; maintainers with accessible private chronology SHALL read complete timestamped comments and publish relevant acceptance criteria. Missing optional tools or private context SHALL be stated once, without repeated credential/integration requests, while useful independent work continues. Source: REM33; AGENTS.md; .agents/skills/reader-simulator-testing/SKILL.md; openspec/README.md.

#### Scenario: Contributor without private integrations
- **WHEN** a contributor has the repository and public task but no Linear/Codex/tablet access
- **THEN** they can select and execute offline scenarios, edit artifacts and submit their contribution using manual equivalents, with genuinely missing acceptance evidence clearly identified.

#### Scenario: Optional agent tool unavailable
- **WHEN** a bundled skill names a tool unavailable in the contributor's environment
- **THEN** equivalent conversation, file or CLI steps preserve the workflow outcome without requiring that tool or silently omitting required review/spec artifacts.

### Requirement: Evidence and authorization boundaries
Development guidance SHALL distinguish deterministic scripted behavior, real-model interpretation and native device behavior. Model-facing changes SHALL receive representative authorized live validation before merge; unavailable contributor access SHALL become a maintainer verification responsibility. Existing task authorization SHALL remain effective without repeated approval, and application API costs SHALL remain distinct from assistant capacity restrictions. Secrets SHALL stay in ignored local/process configuration and never be printed, included in scenarios or committed. Source: REM22 comment674a9fc1; REM28; docs/local-development.md; .agents/skills/reader-simulator-testing/SKILL.md.

#### Scenario: Offline execution
- **WHEN** a scripted scenario is selected without credentials or SSH
- **THEN** local execution and exact assertions remain available and its evidence does not claim model handwriting recognition or hardware fidelity.

#### Scenario: Model-facing acceptance unavailable locally
- **WHEN** a contributor changes prompts/model interpretation but lacks live access
- **THEN** they preserve local results and the missing live gate, and a maintainer supplies appropriate authorized live evidence before merge rather than treating scripts as vision proof.

### Requirement: Scoped native diagnostics
Unattended tablet guidance SHALL link or describe bounded journalctl unit/time/output inspection and RUST_LOG application emission, while preserving its authorized idle development tablet scope and original service/environment state. Journal priority filtering SHALL not be presented as guaranteed Rust log-level filtering. Logs and debug images SHALL be reviewed for sensitive content before intentional publication. Source: REM14 commentf4e309cb; .agents/skills/reader-buddy-testing/SKILL.md; README.md.

#### Scenario: Authorized native investigation
- **WHEN** an authorized idle tablet run needs diagnostics
- **THEN** the maintainer can capture bounded relevant logs, enable scoped debug emission if needed and restore prior service state without broadening authorization to firmware, accounts or a personal tablet.

### Requirement: Completion-driven workflow guidance
Repository AGENTS/workflow guidance SHALL establish supported completion events plus verified postconditions, otherwise bounded fresh-state polling with deadlines/cancellation, as the default for future Reader/Writer features and improvements. Necessary fixed-wait exceptions SHALL include reason, scope, bound and validation; gesture/cadence/timeout behavior SHALL be distinguished from completion assumptions. Public/manual contributor workflows SHALL remain supported without a private integration or invasive event dependency. Source: REM9 and REM35 September22 architecture steering.

#### Scenario: Future feature introduces a wait
- **WHEN** a contributor plans sequencing for a new operation
- **THEN** the change records the required completion condition, supported signal or bounded polling fallback, owner correlation and tests for delayed/lost/stale/repeated signals and cancellation.

#### Scenario: Integrated final gate
- **WHEN** REM35 validates later Reader/Writer features
- **THEN** it audits new waits and verifies preservation of completion-driven sequencing, safety guarantees and REM9 responsiveness gains before1.0.

### Requirement: Predictable menu-free product interaction
Reader, Writer and future features SHALL NOT autonomously navigate device menus,
including opening menus to inspect state. They SHALL prefer supported direct
interfaces, verified simple gestures or documented safe fallback. Simple left/right
page swipes and keyboard text input remain permitted under their existing guards.

#### Scenario: Feature requires a menu
- **WHEN** no supported non-menu mechanism can implement a proposed feature
- **THEN** the limitation and design choice are surfaced explicitly instead of introducing hidden autonomous menu navigation.

#### Scenario: Developer setup
- **WHEN** deliberate developer/manual validation setup uses a menu
- **THEN** it is separated from normal product execution, announced and labeled as setup; it is not evidence that normal product behavior is menu-free.

#### Scenario: Integrated audit
- **WHEN** REM35 validates the integrated Reader and Writer release
- **THEN** every normal feature path is audited for menu automation, with permitted gestures and keyboard input distinguished explicitly.

### Requirement: Targeted community investigation at architecture roadblocks
When the no-menu architecture blocks a required operation, contributors SHALL
investigate relevant current open-source reMarkable implementations, inspecting
actual code, issues/releases and firmware compatibility. Findings SHALL link
sources/revisions and distinguish supported direct APIs, native/file mechanisms,
injected extensions and UI automation. Research SHALL remain bounded to the
concrete roadblock, with safety, maintenance cost and unresolved limits explicit.

#### Scenario: Promising community mechanism
- **WHEN** a community implementation offers a non-menu alternative
- **THEN** its compatibility and tradeoffs are reviewed before adoption; investigation alone does not authorize invasive installation or establish native correctness.
