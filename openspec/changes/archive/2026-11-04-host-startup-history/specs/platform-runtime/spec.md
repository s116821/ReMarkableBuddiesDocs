## MODIFIED Requirements

### Requirement: Existing diagnostic flags
The production CLI SHALL expose the existing diagnostic and maintenance options --api-key, --model/-m, --base-url, --trigger-corner, --log-level, --debug-dump and --simulate; --inspect-owned-data; --export-note; --personalization-operation inspect|set|disable|clear; and help/version. Separately specified production selectors SHALL follow their own admission contracts. Unrecognized production flags SHALL be rejected. Personalization maintenance SHALL be exclusive with simulation, normal key/model/endpoint/corner/dump/logging overrides, and SHALL receive mutation JSON only through bounded stdin. Personalization, prepared export and owned-data inspection SHALL be mutually exclusive. Inspection SHALL reject simulation and explicit normal key/model/endpoint/corner/dump overrides, while allowing logging control. Simulation SHALL reject explicit normal key/model/endpoint/corner/dump overrides, while allowing logging control. Screenshot-only and one immediate native iteration SHALL remain available as explicitly built diagnostic examples using production components, outside the production CLI and distributed archives. Source: REM6/REM22/REM34/REM42/REM53; src/main.rs and personalization-config-contract.

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

## ADDED Requirements

### Requirement: Explicit selected Reader startup and historical handling
An explicitly configured selected Reader runtime SHALL use the existing shared Store/admission and selected refusing Workflow, and SHALL resolve unsupported committed SDK acquisition before model credentials, provider, sync or native device startup. It SHALL NOT downgrade to ordinary legacy acquisition or initialize an absent selected scope. One-shot historical inspection/recovery SHALL retain immutable provenance and grant no live context or effect authority.

#### Scenario: SDK native acquisition remains unsupported
- **WHEN** explicit selected startup uses the committed unqualified SDK platform
- **THEN** it SHALL report the typed unsupported capability without constructing ordinary RealDevice, invoking a model, publishing a pending intent or touching the tablet.

#### Scenario: Exact historical request recovery
- **WHEN** an explicitly supplied original PendingIntentRequest matches a validated historical publication
- **THEN** recovery SHALL return only its original historical acknowledgment/provenance, even if current SDK acquisition is unsupported, and SHALL NOT allocate new IDs, mint ReaderContext or replay an effect.

#### Scenario: Invalid selected startup metadata
- **WHEN** generic storage accepts a selected snapshot but strict conversation schema or chronology validation fails, or the opened Store contains unavailable commits
- **THEN** startup SHALL report unavailable without adapter-capability data, under the existing shared admission and cumulative read allowance.

#### Scenario: Availability before an active request
- **WHEN** startup needs to report the selected refusing transport's availability before a Reader request exists
- **THEN** it SHALL inspect typed availability without invoking acquisition or interpreting a request-guard failure as unsupported capture, and actual request acquisition SHALL retain its guards.

#### Scenario: Persisted mode before runtime construction
- **WHEN** an existing Store has an explicit nonlocal or contradictory publisher mode
- **THEN** startup SHALL validate the actual mode before credentials/model/device construction and refuse an unsupported or mismatched runtime without ordinary all-history fallback; unconfigured compatibility and local-only data access SHALL remain distinct from shared authority.
- **AND** with no `reader.selection`, the actual CLI SHALL exit unsuccessfully with empty stdout and a fixed private-data-free diagnostic while retaining early preflight/no-write checks; successful fixed JSON responses remain scoped to selected-config startup and explicit report commands.

#### Scenario: Configured shared receiving lifetime
- **WHEN** a current selected history report consumes data in configured shared mode
- **THEN** it SHALL retain the matched existing shared-mode lease alongside actual domain/Store admission through consumption, without granting provider/root/native permission or treating local data leases as mode guards.

### Requirement: Selected history command routing
The executable SHALL support --conversation-operation inspect|context|recover-pending with required --conversation-input FILE. Exact-dash inspect and ordinary prepare/apply/status SHALL retain their existing stdin contract. Selected context and recovery SHALL accept only a bounded file. Input errors SHALL remain within the selected operation family. Selected history maintenance SHALL dispatch before dotenv and ordinary credential, model, sync or device initialization. It SHALL be mutually exclusive with other one-shot selectors, and SHALL reject simulation and normal provider/runtime/logging overrides. Current inspection SHALL retain its existing sealed, budgeted and leased output contract; historical recovery SHALL return only original custody and grant no new effect authority.

#### Scenario: Competing history selectors
- **WHEN** history maintenance is combined with another one-shot selector in either argument order
- **THEN** argument parsing SHALL refuse before dispatch with no JSON report or owned-file mutation.

#### Scenario: Context without a tokenizer
- **WHEN** the history context command has no qualified provider tokenizer
- **THEN** it SHALL report choice-needed without inventing token counts or emitting model-ready context.
