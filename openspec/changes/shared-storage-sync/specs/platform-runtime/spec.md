## MODIFIED Requirements

### Requirement: Runtime startup and configuration
The executable SHALL load an optional .env before argument parsing, default to model gpt-5.6-terra and corner LL, and support --api-key with OPENAI_API_KEY fallback and --base-url with OPENAI_BASE_URL fallback. Explicit CLI values SHALL take precedence, followed by existing relevant environment overrides, validated nonsecret versioned file configuration, then existing defaults. Model/corner parser defaults SHALL NOT mask an intended file setting when no explicit CLI value was supplied. Selected secrets SHALL remain separate from ordinary configuration. Normal configuration, owned storage and credential validation SHALL complete before device initialization; absent/blank selected credentials or invalid configuration SHALL fail without printing values. Scripted simulation SHALL retain its isolated path before normal storage/credential/sync initialization. Source: REM6/REM28/REM34/REM36; src/main.rs, planned src/config.rs and shared-storage contract.

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

### Requirement: Implemented product boundary
The application SHALL process independent Reader Buddy iterations on real devices or the maintained simulator and provide generic local storage/configuration and opt-in Drive record-sync infrastructure. It SHALL NOT yet claim Writer Buddy, follow-up conversation history, document retrieval, external search tools, domain-level persistent subject memory or handwriting learning, or native answer-page creation merely because their storage adapters exist. Source: REM36 infrastructure scope and owning follow-up issues; src/main.rs, src/workflow/orchestrator.rs and planned src/storage/.

#### Scenario: New question after previous answer
- **WHEN** another Reader iteration starts before the conversation feature is implemented
- **THEN** model content is still rebuilt from the current page rather than claiming a retained conversation or document corpus

#### Scenario: Generic persistence is not a domain feature
- **WHEN** a synthetic memory or handwriting envelope passes storage/sync tests
- **THEN** evidence describes the infrastructure only and does not claim REM-24 or REM-26 behavior is implemented
