## MODIFIED Requirements

### Requirement: Shared workflow execution
The Reader simulator SHALL retain the real device-facing interface and production
Reader orchestration, parsing/verification, classification and recovery policies.
Writer host scenarios SHALL run the production joined Writer/export flow and
Ledger with declared normalized text and a scripted destination. Deterministic
scenarios SHALL use scripted LLMEngine replies with no credentials or network
calls. Explicit live Reader scenarios SHALL retain the configured provider path.
Separate loopback HTTP integration tests SHALL remain distinct from scripted
simulation and live account/native evidence.

#### Scenario: Accepted question
- **WHEN** proposal and independent transcription agree and the successor is blank
- **THEN** the production workflow writes one header and the exact Q&A block to the successor while preserving the source.

#### Scenario: Declined or disagreeing question
- **WHEN** a proposal is NONE or independent reading disagrees
- **THEN** the source receives no feedback ink, successor navigation or answer text; the matching non-ink diagnostic is recorded.

#### Scenario: Writer create and refined update
- **WHEN** a scripted Writer host scenario generates/exports, reopens and deliberately refines/re-exports one correlation
- **THEN** the production flow retains exact drafts/source history, creates then updates the same scripted destination identity and records actual stage/poll counts without claiming tablet output.

### Requirement: Structured reproducible scenarios
Reader scenarios SHALL preserve their existing page, iteration, gesture, reply,
fault and expected-result contract. Writer host scenarios SHALL declare bounded
normalized source/selection, steps, scripted replies, restart and phase-indexed
cancellation/state/destination faults. Unknown/duplicate fields, unsupported
modes and invalid values SHALL fail before execution. Relative assets/output
SHALL resolve from the scenario location; mode dispatch SHALL use strict schemas
without silently accepting Reader fields as Writer instructions.

#### Scenario: Bounded gesture input
- **WHEN** a short contact precedes a stationary two-second corner hold
- **THEN** the shared timer ignores the short contact and triggers on the valid hold without movement.

#### Scenario: Exhausted gestures
- **WHEN** a scenario has no valid remaining trigger
- **THEN** execution records a bounded error instead of waiting forever.

#### Scenario: Writer phase faults
- **WHEN** replay, acknowledgment loss, cancellation or selected-state change is injected at a declared joined-flow phase
- **THEN** actual production admission/dispatch rules determine the result and assertions verify exact forbidden model/destination/write counts without sleeps as success.

### Requirement: Inspectable results and meaningful assertions
Reader scenarios SHALL preserve page PNGs and JSON reports of exact rendered
text, marks, active page, model calls, errors and timestamped operations. Writer
host scenarios SHALL save exact draft/export content, source preservation,
ordered phase/destination traces, call/write counts and assertion failures,
without invented tablet PNGs or native output. Expected mismatches SHALL fail
after artifacts are saved. Existing Reader exact/text_contains assertions SHALL
remain supported, and execution labels SHALL distinguish scripted simulation,
loopback transport and explicit live-provider observations.

#### Scenario: Failed assertion
- **WHEN** expected text, page, operation counts or error behavior differs
- **THEN** the process exits unsuccessfully and the report identifies the mismatch.

#### Scenario: Writer report is not rendered output
- **WHEN** a Writer host scenario succeeds
- **THEN** its report exposes the actual production draft/export state and no fabricated navigation, page drawing, tool/menu operation or native-completion claim.

### Requirement: Honest fidelity and extension boundaries
Documentation SHALL retain the modeled Reader dimensions/holds/delays/recovery
provenance and distinguish scripts/raster output from hardware/model evidence.
Writer host execution SHALL explicitly mean supplied-text production flow with
scripted destination behavior. Combined native Reader/Writer routing, physical
notebook/OCR coverage, gestures, insertion and on-tablet proposal rendering SHALL
remain unsupported until their production paths and evidence exist. Seeded
Reader Ledger history SHALL NOT be called actual combined workflow execution.

#### Scenario: Unsupported product
- **WHEN** a scenario requests combined/native Writer behavior outside the implemented host-flow contract
- **THEN** validation fails explicitly without simulated claims of that workflow.

#### Scenario: Same conversation fixture
- **WHEN** a Writer scenario starts with declared historical Reader turns
- **THEN** real Ledger preservation and subsequent Writer behavior may be asserted, while the report labels those initial turns as fixture history rather than a newly executed native Reader→Writer transition.
