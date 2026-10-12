## MODIFIED Requirements

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

### Requirement: Logging and service lifecycle
The runtime SHALL use env_logger with millisecond timestamps. --log-level SHALL validate off/error/warn/info/debug/trace and override RUST_LOG; absent explicit control SHALL use RUST_LOG, otherwise info globally and debug for Reader Buddy application targets. No dedicated debug enable toggle SHALL be required. The supplied service SHALL retain /opt/bin/reader-buddy from /home/root, its protected environment file, journal output and five-second restart-on-failure policy. Optional diagnostic image dumps SHALL remain separate from the durable source-evidence retention contract. Source: REM14/REM34/REM37; src/main.rs; deploy/reader-buddy.service; conversation-context.

#### Scenario: Useful diagnostics by default
- **WHEN** no explicit logging override is set
- **THEN** Reader Buddy debug messages are enabled while dependency debug messages are disabled, and diagnostic image dumps remain independently opt-in.

#### Scenario: Service configuration
- **WHEN** the supplied unit is used
- **THEN** it reads /home/root/.config/reader-buddy/environment and orders after home.mount, xochitl.service and network-online.target.

#### Scenario: Debug data exposure
- **WHEN** default debug diagnostics are emitted
- **THEN** logs may include question/answer and parsed model text but explicit request diagnostics exclude authorization headers and entire image-bearing request bodies; diagnostic page-image copies require dump opt-in, while every actual source image used for a turn is retained privately under the durable evidence contract regardless of dump settings.

### Requirement: Implemented product boundary
The application SHALL process Reader Buddy iterations on real devices or the maintained simulator, provide generic local storage/configuration and opt-in Drive record-sync infrastructure, and persist conversation/source evidence through shared domain APIs and actual Reader orchestration. It SHALL NOT claim Writer UI, unified follow-up routing/rendering, document retrieval, external search tools, domain-level persistent subject memory or handwriting learning, or native answer-page creation merely because shared ledger/storage APIs exist. Source: REM36/REM37 infrastructure/domain scope and owning follow-up issues; src/main.rs, src/workflow/orchestrator.rs, src/storage/ and src/conversation/.

#### Scenario: New question after previous answer
- **WHEN** another Reader iteration starts before unified routing is implemented
- **THEN** recognition still uses its current guarded source image batch and unchanged prompts, while retained prior conversation records and images are inspected directly from the ledger rather than reconstructed by OCR of old replies.

#### Scenario: Generic persistence is not a domain feature
- **WHEN** a synthetic memory or handwriting envelope passes storage/sync tests
- **THEN** evidence describes the infrastructure only and does not claim REM-24 or REM-26 behavior is implemented.

#### Scenario: Mixed-mode domain evidence
- **WHEN** shared Reader/Writer ledger API fixtures pass
- **THEN** evidence identifies domain persistence and does not claim native Writer UI, unified page routing or automatic acquisition is implemented.

#### Scenario: SDK integration qualification
- **WHEN** conversation persistence consumes device identity, capture provenance or a native output result
- **THEN** the Buddy integration uses the reviewed ReMarkableOpenSDK capability boundary through the mockable device seam, records the exact SDK contract/revision and qualification limits, and refuses unsupported or unqualified native success rather than adding hardware-specific logic to the conversation domain; SDK canonical contracts remain in the SDK repository.
