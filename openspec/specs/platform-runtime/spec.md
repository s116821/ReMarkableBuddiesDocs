# platform-runtime

## Purpose

Describe the implemented platform runtime contracts, initially baselined from v0.1.4. Known gaps are explicit and require a later change delta to alter.

## Requirements

### Requirement: Runtime startup and configuration
The executable SHALL parse arguments before normal .env/configuration resolution. Fixed one-shot personalization maintenance SHALL dispatch before dotenv, normal credential/model/device or sync startup; personalization SHALL require explicit existing REMARKABLE_BUDDIES_CONFIG and follow its bounded maintenance contract. Normal and simulator paths SHALL load optional .env after one-shot dispatch. Normal configuration SHALL default to model gpt-5.6-terra and corner LL, and support --api-key with OPENAI_API_KEY fallback and --base-url with OPENAI_BASE_URL fallback. Explicit CLI values SHALL take precedence, followed by existing relevant environment overrides, validated nonsecret versioned file configuration, then existing defaults. Model/corner parser defaults SHALL NOT mask an intended file setting when no explicit CLI value was supplied. Selected secrets SHALL remain separate from ordinary configuration. Normal configuration, owned storage and credential validation SHALL complete before device initialization; absent/blank selected credentials or invalid configuration SHALL fail without printing values. Scripted simulation SHALL retain its isolated path before normal storage/credential/sync initialization. Personalization disk readback SHALL NOT claim running-runtime reload or Reader/Writer application. Source: REM6/REM28/REM34/REM36/REM53; src/main.rs, src/config.rs, shared-storage and personalization-config-contract.

#### Scenario: Normal initialization
- **WHEN** usable normal configuration and device access are available
- **THEN** the runtime initializes validated local storage and cache/capture/input, preserves the existing 1000 ms device-startup wait, then waits for triggers in its continuous loop

#### Scenario: Missing or blank credentials
- **WHEN** no usable selected credential is supplied
- **THEN** startup fails before device initialization with a value-free error

#### Scenario: File configuration and explicit overrides
- **WHEN** the file provides model/corner or another supported setting and an explicit CLI or existing environment override is also present
- **THEN** explicit CLI wins first, relevant environment next, and otherwise the validated file setting applies before the unchanged default

#### Scenario: Offline scripted simulation
- **WHEN** a scripted --simulate scenario is selected
- **THEN** production credentials/storage configuration and cloud sync are not initialized, preserving its offline fixture-only behavior

#### Scenario: Personalization maintenance before normal startup
- **WHEN** an explicit --personalization-operation is selected
- **THEN** only bounded existing configuration maintenance runs, without normal credential/model/device/sync startup; successful mutation reports verified disk readback and restart-required, not running-runtime activation

### Requirement: Existing diagnostic flags
The production CLI SHALL expose only --api-key, --model/-m, --base-url, --trigger-corner, --log-level, --debug-dump and --simulate; --personalization-operation inspect|set|disable|clear; and help/version. Other production flags SHALL be rejected. Personalization maintenance SHALL be exclusive with simulation, normal key/model/endpoint/corner/dump/logging overrides, and SHALL receive mutation JSON only through bounded stdin. Simulation SHALL reject explicit normal key/model/endpoint/corner/dump overrides, while allowing logging control. Screenshot-only and one immediate native iteration SHALL remain available as explicitly built diagnostic examples using production components, outside the production CLI and distributed archives. Source: REM6/REM22/REM34/REM53; src/main.rs and personalization-config-contract.

#### Scenario: Image dump configuration
- **WHEN** --debug-dump is present
- **THEN** image dumps are enabled; otherwise READER_BUDDY_DEBUG_DUMP true/1 enables, absent/false/0 disables, and invalid values fail before device initialization.

#### Scenario: Offline scenario
- **WHEN** --simulate selects a scripted scenario
- **THEN** it executes without real devices or credentials and preserves exact declared workflow assertions; scenario live mode remains explicit.

#### Scenario: Bounded development tools
- **WHEN** the screenshot example is invoked with its output path
- **THEN** it captures without input initialization or credentials; the separate reader_once example runs one immediate production iteration using environment credentials and default model/corner.

#### Scenario: Personalization selector isolation
- **WHEN** personalization maintenance is combined with a normal runtime override
- **THEN** argument parsing refuses rather than ignoring the extra operation or starting the runtime

### Requirement: Logging and service lifecycle
The runtime SHALL use env_logger with millisecond timestamps. --log-level SHALL validate off/error/warn/info/debug/trace and override RUST_LOG; absent explicit control SHALL use RUST_LOG, otherwise info globally and debug for Reader Buddy application targets. No dedicated debug enable toggle SHALL be required. The supplied service SHALL retain /opt/bin/reader-buddy from /home/root, its protected environment file, journal output and five-second restart-on-failure policy. Source: REM14/REM34; src/main.rs; deploy/reader-buddy.service.

#### Scenario: Useful diagnostics by default
- **WHEN** no explicit logging override is set
- **THEN** Reader Buddy debug messages are enabled while dependency debug messages are disabled, and image dumps remain independently opt-in.

#### Scenario: Service configuration
- **WHEN** the supplied unit is used
- **THEN** it reads /home/root/.config/reader-buddy/environment and orders after home.mount, xochitl.service and network-online.target.

#### Scenario: Debug data exposure
- **WHEN** default debug diagnostics are emitted
- **THEN** logs may include question/answer and parsed model text but explicit request diagnostics exclude authorization headers and entire image-bearing request bodies; page images are saved only with dump opt-in.

### Requirement: Implemented product boundary
The application SHALL process independent Reader Buddy iterations on real devices or the maintained simulator and provide generic local storage/configuration and opt-in Drive record-sync infrastructure. It SHALL NOT yet claim Writer Buddy, follow-up conversation history, document retrieval, external search tools, domain-level persistent subject memory or handwriting learning, or native answer-page creation merely because their storage adapters exist. Source: REM36 infrastructure scope and owning follow-up issues; src/main.rs, src/workflow/orchestrator.rs and src/storage/.

#### Scenario: New question after previous answer
- **WHEN** another Reader iteration starts before the conversation feature is implemented
- **THEN** model content is still rebuilt from the current page rather than claiming a retained conversation or document corpus

#### Scenario: Generic persistence is not a domain feature
- **WHEN** a synthetic memory or handwriting envelope passes storage/sync tests
- **THEN** evidence describes the infrastructure only and does not claim REM-24 or REM-26 behavior is implemented
### Requirement: Git-derived application version
The CLI version SHALL derive from Git history through maintained semantic tooling
and vergen-gitcl, never an independently maintained Cargo package version.
A controlled candidate build SHALL require full clean history and exact frozen
candidate tag/version and source SHA; it MAY precede remote tag creation.
Its embedded value alone SHALL NOT grant official publication or native trust.
An existing published-tag build SHALL additionally verify the actual tag/SHA.
Only the final release job after all build/artifact integration gates SHALL create
the official tag and publish those exact already-tested bytes. Development or
unavailable metadata SHALL be explicit. Source: REM-56 superseding REM-30 order.

#### Scenario: Official tagged build
- **WHEN** an existing published-tag build checks out its verified release tag
- **THEN** --version and package provenance report that tag's semantic version and exact source SHA.

#### Scenario: Verified candidate before publication
- **WHEN** controlled CI builds a frozen clean candidate before the remote tag exists
- **THEN** both target artifacts report the frozen candidate version and integration consumes those bytes; only later successful final tag/release proof establishes publication eligibility.

#### Scenario: Missing or conflicting official metadata
- **WHEN** candidate/published metadata has shallow or missing history, dirty source, conflicting profiles/overrides or wrong source/tag identity
- **THEN** the build refuses instead of substituting a manifest version or misleading release identity.

#### Scenario: Development build
- **WHEN** a build has neither valid controlled candidate nor verified published-tag metadata
- **THEN** --version identifies development or unavailable Git state explicitly.
