# local-simulator

## Purpose

Define maintained local Reader execution, deterministic scenarios and explicit hardware/product fidelity boundaries.

## Requirements

### Requirement: Shared workflow execution
The Reader simulator SHALL retain the real device-facing interface and production
Reader orchestration, parsing/verification, classification and recovery policies.
Writer host scenarios SHALL run the production joined Writer/export flow and
Ledger with declared normalized text and a scripted destination. Deterministic
scenarios SHALL use scripted LLMEngine replies with no credentials or network
calls. Explicit live Reader scenarios SHALL retain the configured provider path.
Separate loopback HTTP integration tests SHALL remain distinct from scripted
simulation and live account/native evidence.

Notebook host scenarios SHALL run the production planner, stage runner, typed
Ledger/media and guarded exporter with scripted model/destination behavior. They
SHALL NOT replace production calls with hand-built successful status reports.

#### Scenario: Accepted question
- **WHEN** proposal and independent transcription agree and the successor is blank
- **THEN** the production workflow writes one header and the exact Q&A block to the successor while preserving the source.

#### Scenario: Declined or disagreeing question
- **WHEN** a proposal is NONE or independent reading disagrees
- **THEN** the source receives no feedback ink, successor navigation or answer text; the matching non-ink diagnostic is recorded.

#### Scenario: Writer create and refined update
- **WHEN** a scripted Writer host scenario generates/exports, reopens and deliberately refines/re-exports one correlation
- **THEN** the production flow retains exact drafts/source history, creates then updates the same scripted destination identity and records actual stage/poll counts without claiming tablet output.


#### Scenario: Larger notebook generation and refinement
- **WHEN** a bounded declared normalized asset exceeds inline limits and is processed/refined across restart
- **THEN** production paths retain complete source/range/stage facts, enforce actual call budgets and update the same scripted note without a native-transition claim.

#### Scenario: Stage or media fault
- **WHEN** a declared stage loses acknowledgment, is canceled/stale/invalid or loses required media
- **THEN** actual admission/cancellation rules stop subsequent calls/writes and report truthful partial/uncertain state without automatic replay.

### Requirement: Structured reproducible scenarios
Reader scenarios SHALL preserve their existing page, iteration, gesture, reply,
fault and expected-result contract. Writer host scenarios SHALL declare bounded
normalized source/selection, steps, scripted replies, restart and phase-indexed
cancellation/state/destination faults. Unknown/duplicate fields, unsupported
modes and invalid values SHALL fail before execution. Relative assets/output
SHALL resolve from the scenario location; mode dispatch SHALL use strict schemas
without silently accepting Reader fields as Writer instructions.

Writer notebook scenarios SHALL resolve declared source assets relative to the
scenario, validate at most 8 MiB per asset and 32 MiB total before execution, and
keep the existing Writer scenario-JSON limit separate from Reader admissibility.
Reader SHALL retain its current larger valid inputs. Unknown/duplicate fields,
unsupported native modes and invalid work/call/asset budgets SHALL refuse before
Store/model/device effects. Original fixture files SHALL remain unmodified.
Each new asset SHALL declare its raw SHA-256 and follow the same regular-file,
opened-handle, bounded-read, strict JSON and path-sanitization contract as notebook
generation; special files and changed/unsupported bindings SHALL refuse.
Relative notebook assets SHALL resolve against the scenario file's directory,
not the build machine's source checkout. Complete validated observed buffers
SHALL freeze before fixture Store creation; production preparation SHALL consume
those buffers without reopening mutable transport paths. The sum of declared
raw notebook asset bytes SHALL be at most 8 MiB per scenario.

#### Scenario: Bounded gesture input
- **WHEN** a short contact precedes a stationary two-second corner hold
- **THEN** the shared timer ignores the short contact and triggers on the valid hold without movement.

#### Scenario: Exhausted gestures
- **WHEN** a scenario has no valid remaining trigger
- **THEN** execution records a bounded error instead of waiting forever.

#### Scenario: Writer phase faults
- **WHEN** replay, acknowledgment loss, cancellation or selected-state change is injected at a declared joined-flow phase
- **THEN** actual production admission/dispatch rules determine the result and assertions verify exact forbidden model/destination/write counts without sleeps as success.


#### Scenario: Asset and admission bounds
- **WHEN** a Writer asset/total budget is exceeded or a valid Reader history is larger than 1 MiB
- **THEN** the Writer request refuses before execution while the original valid Reader admission remains supported, without sharing the new Writer cap globally.

#### Scenario: Asset substitution or special file
- **WHEN** an asset is a FIFO/symlink/reparse path, changes opened-file binding or does not match its expected raw hash
- **THEN** the scenario refuses before Store/model/destination effects with a fixed sanitized error, without a blocking special-file read or fallback to newer path content.

#### Scenario: Relocated maintained fixture
- **WHEN** a scenario and its declared relative notebook asset are copied outside the build checkout
- **THEN** the actual application resolves and freezes the asset beside that scenario, retaining its exact raw hash and complete coverage.

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
Reader scenarios SHALL preserve page PNGs and JSON reports of exact rendered
text, marks, active page, model calls, errors and timestamped operations. Writer
host scenarios SHALL save exact draft/export content, source preservation,
ordered phase/destination traces, call/write counts and assertion failures,
without invented tablet PNGs or native output. Expected mismatches SHALL fail
after artifacts are saved. Existing Reader exact/text_contains assertions SHALL
remain supported, and execution labels SHALL distinguish scripted simulation,
loopback transport and explicit live-provider observations.

Notebook reports SHALL expose actual source/media digests, selected unit/range
coverage, planned/invoked calls, stage outcomes, fixed error codes, bounded final
content and actual destination/write observations. They SHALL distinguish
processed coverage from semantic quality, invoked model cost from zero writes,
and failed recording from local zero-invocation/no-send observations. Reports
SHALL be saved before assertion failures and SHALL NOT fabricate tablet PNGs.
An explicit `retain_store_fixture` option MAY retain a closed test-owned data
directory beneath a new `store-fixture` directory in the declared scenario
output. It SHALL default off, refuse existing/symlink destinations, exclude
credential/cache roots, and bound the copy at 8192 regular files/64 MiB with
relative-path/hash evidence. This diagnostic fixture SHALL NOT claim backup
restore compatibility, native authority or fresh model/export admission.
Unused scripted replies and unreached declared phase faults SHALL fail assertions.

#### Scenario: Fresh empty host fixture
- **WHEN** a scripted scenario performs only a restart and explicitly retains its Store fixture
- **THEN** it saves the actual closed ordinary Store and newly created conversation with zero model/destination calls, without creating a fake model result or native binding.

#### Scenario: Failed assertion
- **WHEN** expected text, page, operation counts or error behavior differs
- **THEN** the process exits unsuccessfully and the report identifies the mismatch.

#### Scenario: Writer report is not rendered output
- **WHEN** a Writer host scenario succeeds
- **THEN** its report exposes the actual production draft/export state and no fabricated navigation, page drawing, tool/menu operation or native-completion claim.


#### Scenario: Partial-stage report
- **WHEN** two model stages were invoked before cancellation or storage failure prevents continuation
- **THEN** actual recorded/uncertain stages and zero later calls/writes remain inspectable rather than being labeled no cost, complete generation or native success.

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
