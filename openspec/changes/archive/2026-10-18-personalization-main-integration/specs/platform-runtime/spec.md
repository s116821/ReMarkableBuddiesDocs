## MODIFIED Requirements

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
