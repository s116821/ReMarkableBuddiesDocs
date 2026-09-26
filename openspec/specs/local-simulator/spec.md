# local-simulator

## Purpose

Define maintained local Reader execution, deterministic scenarios and explicit hardware/product fidelity boundaries.

## Requirements

### Requirement: Shared workflow execution
The simulator SHALL implement the same device-facing interface as the real tablet and run the production Reader orchestrator, model content/parsing/verification, image classification and recovery policies. Deterministic scenarios SHALL use scripted LLMEngine replies with no credentials or network calls. Explicit live scenarios SHALL use the configured provider through the same orchestration and result path. Source: src/device/backend.rs; src/simulator; src/workflow/orchestrator.rs.

#### Scenario: Accepted question
- **WHEN** proposal and independent transcription agree and the successor is blank
- **THEN** the production workflow writes one header and the exact Q&A block to the successor while preserving the source.

#### Scenario: Declined or disagreeing question
- **WHEN** a proposal is NONE or independent reading disagrees
- **THEN** the source receives no feedback ink, successor navigation or answer text; the matching non-ink diagnostic is recorded.

### Requirement: Structured reproducible scenarios
Scenarios SHALL specify initial page snapshots, active page, bounded iterations, gesture frames, scripted model replies, operation-indexed faults and expected results. Unknown fields, unsupported modes and invalid page/fault/gesture values SHALL fail before execution. Relative asset/output paths SHALL resolve from the scenario location. Source: src/simulator/scenario.rs; src/simulator/mod.rs.

#### Scenario: Bounded gesture input
- **WHEN** a short contact precedes a stationary two-second corner hold
- **THEN** the shared timer ignores the short contact and triggers on the valid hold without movement.

#### Scenario: Exhausted gestures
- **WHEN** a scenario has no valid remaining trigger
- **THEN** execution records a bounded error instead of waiting forever.

### Requirement: Page and fault model
The simulator SHALL retain ordered pages and page-local text/marks, model end boundaries, cached header recognition and requested delays, and inject capture, input, rendering, no-motion and stale-capture conditions at declared operation calls. Shared recovery SHALL never exceed one reverse swipe. Explicit owner-change and external-input faults SHALL invalidate the retained request independently of wrong-page pixels. Source: src/simulator/device.rs; src/workflow/navigation.rs.

#### Scenario: Existing answers
- **WHEN** a later iteration reaches a cached-header successor
- **THEN** it appends a Q&A block without duplicating the header or erasing prior answers.

#### Scenario: Failed return
- **WHEN** an occupied successor rejects output and its return swipe makes no movement
- **THEN** the Device diagnostic is recorded without feedback ink or an answer, and no second return occurs.

#### Scenario: End page
- **WHEN** no successor exists
- **THEN** the workflow stays on the source and records NoSuccessor without feedback ink, reverse navigation or insertion.

#### Scenario: Owner or external input changes at operation boundary
- **WHEN** capture, navigation or keyboard output observes changed ownership or external input
- **THEN** cancellation remains latched, later operations stop and a fresh capture cannot silently repin the request.

### Requirement: Inspectable results and meaningful assertions
Every executed scenario SHALL export page PNGs and a JSON report of exact rendered text, marks, active page, model calls, errors and ordered timestamped operations. Expected-result mismatches SHALL fail the command after output is saved. Optional text_contains assertions SHALL check stable substrings while exact text assertions remain supported. Reports SHALL label scripted-offline or live-provider execution. Source: src/simulator/mod.rs; tests/simulator.rs.

#### Scenario: Failed assertion
- **WHEN** expected text, page, operation counts or error behavior differs
- **THEN** the process exits unsuccessfully and the report identifies the mismatch.

### Requirement: Honest fidelity and extension boundaries
Documentation SHALL attribute modeled dimensions, holds, delays, masks and recovery to observed RM2 behavior and distinguish scripted replies/raster output from hardware and live-model validation. Writer/combined execution SHALL report unsupported until production Writer is implemented; REM-23/REM-17 SHALL extend coverage and REM-25 SHALL extend insertion. Source: docs/simulator.md; src/simulator/scenario.rs.

#### Scenario: Unsupported product
- **WHEN** a scenario requests Writer or combined mode
- **THEN** validation fails explicitly without simulated claims of those workflows.

### Requirement: Reproducible history sessions
The simulator SHALL drive the shared last-Q&A history state using declared undo/redo holds, departures/returns, new iterations and intervening edits. Reports SHALL expose transaction state, ordered events and exact page text. Faults SHALL exercise uncertain/partial mutation without silently claiming rollback. Source: src/simulator/scenario.rs; src/simulator/device.rs; tests/simulator.rs.

#### Scenario: Repeated toggle
- **WHEN** a scripted session accepts a Q&A and alternates valid undo/redo actions
- **THEN** only that block toggles, with no extra model calls and unchanged earlier page content.

#### Scenario: Invalidated session
- **WHEN** a page departure, new iteration or intervening edit invalidates the record
- **THEN** later history actions cannot revive it or mutate unrelated content.

#### Scenario: Partial operation
- **WHEN** a history mutation fault occurs
- **THEN** the report retains the actual failure state and history is discarded without an automatic retry.

#### Scenario: Persisted page lags visible typing
- **WHEN** the visible Q&A has completed but the persisted snapshot still contains the prior text
- **THEN** history remains unavailable until the complete expected content is observed; a timeout never arms stale history.

#### Scenario: Gesture cancellation and interrupted input
- **WHEN** contacts move, change identity, drop out, remain partly released too long, or input events are lost
- **THEN** the shared contact policy invalidates history without executing a mutation; valid stationary two-/four-contact holds execute at most once after full release.

#### Scenario: Native preservation evidence
- **WHEN** recorded native snapshots are replayed through the history policy
- **THEN** previous visible paragraphs, native ink and opaque records must be preserved, and restored Q&A text/styles must equal the applied state; reports distinguish this replay from live keyboard, physical gesture or vision validation.

#### Scenario: Stable metadata describes another view
- **WHEN** saved last-opened metadata refers to the wrong page, or the user opens the overview without changing the saved page ID
- **THEN** history cannot arm from the wrong observation, and the overview input invalidates existing ownership even when the saved ID stays unchanged.

#### Scenario: Reader release ordering
- **WHEN** a corner hold reaches two seconds while still touching the screen
- **THEN** the shared reducer waits for release before dispatching Reader, preventing the observed native menu from reopening after dismissal; canceled or moved holds cannot trigger Reader.

#### Scenario: Current identity absent after native restart
- **WHEN** the document is visible but native current-document identity is unavailable
- **THEN** the answer can render normally, but subsequent undo/redo does not gain ownership retroactively.

#### Scenario: Terminal observation failure during a guard
- **WHEN** native observation fails during persistence or mutation and that first error is consumed before the idle wait
- **THEN** subsequent polling still reports terminal failure, the idle path retires the observer and a fresh observer or legacy fallback can accept the next Reader gesture without reviving history.

### Requirement: Coordinate-tagged answer coverage
The simulator SHALL exercise production center parsing, normalization and Q&A formatting through scripted circle/highlight replies and explicit invalid-center cases. Tagged blocks SHALL use shared history unchanged; simulated location is declared model output rather than visual proof. Source: src/workflow/orchestrator.rs; src/workflow/mod.rs; src/analysis/mod.rs; tests/simulator.rs; tests/history_simulator.rs.

#### Scenario: Selected region differs from question
- **WHEN** a scripted question box and selected-content center occupy different places
- **THEN** the Q&A tag identifies the normalized selected-content center and not the question box.

#### Scenario: Invalid center
- **WHEN** a reply has a missing, malformed or out-of-bounds center
- **THEN** no successor navigation or answer occurs, and non-ink decline diagnostics preserve the source page.

#### Scenario: Tagged history
- **WHEN** a tagged Q&A is undone and redone
- **THEN** its tag and full text toggle together, preserving the header and earlier untagged answers with no extra model calls.

### Requirement: Development fixture and acceptance practice
The simulator testing skill SHALL choose maintained fixtures by changed behavior, assert exact text/forbidden operations and preserve negative cases and failed artifacts. Applicable model-facing checks SHALL include representative connected cursive/shorthand and ambiguous or absent questions, with scientific values and actual input/output inspected. Native findings SHALL extend the shared model, faults, fixtures or assertions in the same implementation PR where representable; remaining fidelity gaps SHALL be explicit. Source: REM33; .agents/skills/reader-simulator-testing/SKILL.md; docs/simulator.md; docs/validation/README.md.

#### Scenario: Expected rejection
- **WHEN** a no-question, transcription-disagreement or invalid-successor fixture runs
- **THEN** its assertions check the intended refusal, no forbidden navigation/output and preserved unrelated content rather than equating successful exit with a successful answer.

#### Scenario: Native-only behavior discovered
- **WHEN** device observation reveals behavior the current simulator omits
- **THEN** the implementation PR adds meaningful model/regression coverage when possible and retains native evidence or an explicit unsupported limit without claiming emulation of unmodeled typography, persistence or physical input.

### Requirement: Responsiveness state and timing regressions
The simulator SHALL model changed operation timing and reachable delayed/stale/changed-state outcomes in the same implementation PR, preserving exact output, forbidden writes/navigation, history ownership and bounded failure behavior. Simulated time SHALL be labeled modeled time rather than native latency. Source: REM9.

#### Scenario: Faster path with delayed observation
- **WHEN** a changed workflow sees delayed convergence or a changed page
- **THEN** it either verifies a fresh eligible state within its bound or refuses safely without stale input, preserving existing negative assertions.

#### Scenario: History remains free of status switching
- **WHEN** undo or redo is exercised after a complete answer
- **THEN** its exact content and ownership rules remain unchanged and no new status tool acquisition or indicator loop occurs.

#### Scenario: Completion signal ordering and cancellation
- **WHEN** production sequencing receives immediate, delayed, missing, duplicate, out-of-order, stale or wrong-owner signals, or cancellation
- **THEN** modeled checks assert fresh correlated completion or bounded safe failure, no duplicate mutations and no late revival of cancelled work; timed simulation is not proof of native event availability.

### Requirement: Source feedback retirement regressions
The simulator SHALL exercise the production retirement boundary and assert zero
source-page feedback drawing, erasure and tool leases across success/refusal/failure.
Historical diagnostic tests SHALL remain distinct from normal product scenarios.
Modeled tool footprints SHALL NOT establish native safety.

#### Scenario: Trigger observation recovery is read-only
- **WHEN** a modeled recoverable observation fault occurs after the single outside dismissal tap
- **THEN** the shared recovery/dismissal adapter permits at most one fresh capture under the retained guards, never a second tap; changed content/input/owner or expired budgets stop the workflow. Modeled faults do not prove native allocator detection.

#### Scenario: No simulated tool switching
- **WHEN** normal Reader runs with any declared tool or layout
- **THEN** the operation records zero source feedback, tool lease or toolbar/menu operations and unchanged original tool settings; core Q&A retains exact content and normal safety gates.

#### Scenario: Retired operation faults
- **WHEN** a normal scenario requests a legacy indicator fault
- **THEN** validation rejects it or reports it explicitly unreachable rather than silently claiming the fault was exercised; normal capture/input/ownership failures still stop safely without feedback mutations.

#### Scenario: Declared unsupported status capability
- **WHEN** a page declares an unsuitable tool, unknown tool or unverified layout
- **THEN** the shared workflow preserves exact core Q&A with no status drawing or erasure; this declaration is a modeled input and does not prove native recognition or notes-page eligibility.

#### Scenario: Conditional trigger dismissal
- **WHEN** a modeled hold qualifies
- **THEN** a declared closed overlay emits no tap, a qualified known-open panel receives one outside-panel tap, and unknown or failed dismissal stops before Q&A mutations; actual native overlay behavior remains a separate acceptance gate.
