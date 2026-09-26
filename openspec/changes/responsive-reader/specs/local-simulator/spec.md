## ADDED Requirements
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

## REMOVED Requirements

### Requirement: Observable indicator lifecycle
**Reason**: Source feedback and normal style leases are retired.
**Migration**: Source feedback retirement regressions replace normal lifecycle tests with zero-mutation checks. Historical diagnostic tests remain distinctly labeled and do not satisfy product acceptance.

### Requirement: Status style lifecycle and rollback model
**Reason**: Source feedback and normal style leases are retired.
**Migration**: Source feedback retirement regressions replace normal lifecycle tests with zero-mutation checks. Historical diagnostic tests remain distinctly labeled and do not satisfy product acceptance.


## MODIFIED Requirements

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

### Requirement: Shared workflow execution
The simulator SHALL implement the same device-facing interface as the real tablet and run the production Reader orchestrator, model content/parsing/verification, image classification and recovery policies. Deterministic scenarios SHALL use scripted LLMEngine replies with no credentials or network calls. Explicit live scenarios SHALL use the configured provider through the same orchestration and result path. Source: src/device/backend.rs; src/simulator; src/workflow/orchestrator.rs.

#### Scenario: Accepted question
- **WHEN** proposal and independent transcription agree and the successor is blank
- **THEN** the production workflow writes one header and the exact Q&A block to the successor while preserving the source.

#### Scenario: Declined or disagreeing question
- **WHEN** a proposal is NONE or independent reading disagrees
- **THEN** the source receives no feedback ink, successor navigation or answer text; the matching non-ink diagnostic is recorded.

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
