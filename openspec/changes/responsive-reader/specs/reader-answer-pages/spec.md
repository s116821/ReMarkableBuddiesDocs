## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
After agreement, the system SHALL recapture the source and resolve one successor attempt. Verified RM2 navigation SHALL use ordered native identity and fresh settled pixels under the reader-responsiveness contract. Unsupported layouts retain the explicitly identified legacy fallback. Masked screenshot similarity at least0.999 SHALL still reject unchanged pages without a reverse swipe. Neither failure nor refusal draws source feedback.

#### Scenario: End of document
- **WHEN** the known native page order has no successor or the next-page attempt leaves the screenshot sufficiently similar to the source
- **THEN** no answer is written and a non-ink NoSuccessor diagnostic is recorded without creating a page or swiping backward.

#### Scenario: Physical gesture and completion
- **WHEN** navigation requires a swipe
- **THEN** physical gesture timing remains15 steps at10ms after50ms initial contact; verified-layout completion uses correlated state, while unsupported layouts retain documented legacy waits without verified-layout claims.

### Requirement: Invalid successor recovery
An Invalid successor SHALL trigger a source-identity check before any reverse swipe. If already on the saved source at similarity 0.999, recovery SHALL not navigate. Otherwise it SHALL attempt at most one previous-page swipe and verify the result once, with no retry after failed verification or an input/capture error. The caller SHALL record a non-ink typed failure after recovery or recovery failure, with no source-page display mutation. Source: src/workflow/navigation.rs; src/workflow/mod.rs return_to_original_page; src/workflow/orchestrator.rs render_answer.

#### Scenario: First return fails
- **WHEN** the single previous-page swipe does not restore source similarity
- **THEN** recovery reports Unconfirmed and the caller records the Device diagnostic without another swipe.

#### Scenario: Already on the source
- **WHEN** recovery's initial check matches the saved source, including a forward attempt that did not leave it
- **THEN** recovery reports AlreadySource with no previous-page swipe.
- **AND** the existing forward no-movement guard records NoSuccessor without invoking reverse recovery at end of document.

#### Scenario: Successful return
- **WHEN** the source is initially absent and the single previous-page swipe restores it
- **THEN** recovery reports Returned after one precheck, one swipe and one postcheck.

#### Scenario: Navigation or capture error
- **WHEN** a source-identity check or the previous-page operation returns an error
- **THEN** recovery propagates that error and performs no further navigation; the render-error handler records Device without feedback input.

### Requirement: Failure display and loop errors
Reader SHALL retain distinct Selection, Transcription, Provider, NoSuccessor, InvalidSuccessor and Device failure classifications without drawing, erasing, selecting tools or typing errors on source pages. The diagnostic SHALL be recorded at most once per iteration; it is not visible Buddy-page feedback. Provider/device errors in single-iteration mode SHALL propagate; loop mode SHALL log recoverable errors without arbitrary Error text and terminate on latched input/cancellation failure. REM40 supplies later sanitized conversation error turns.

#### Scenario: Proposal transport error
- **WHEN** a proposal request fails
- **THEN** Provider is recorded without ink and the original error propagates; loop mode writes no error text.

#### Scenario: Selection or transcription refusal
- **WHEN** analysis declines or independent transcription disagrees
- **THEN** the corresponding diagnostic is recorded with no answer/navigation or source feedback mutation.

#### Scenario: Six distinct causes
- **WHEN** selection, transcription, provider, no-motion, invalid-successor or device failures occur
- **THEN** logs/simulator diagnostics retain distinct classifications without any persistent X or segment.

#### Scenario: Unconfirmed recovery or input loss
- **WHEN** recovery is unconfirmed or guarded input is cancelled
- **THEN** no additional swipe or feedback input occurs; latched input failure prevents another iteration.

#### Scenario: Existing handwriting
- **WHEN** the former status corner contains user ink
- **THEN** it remains untouched on success and failure, with no new feedback eligibility requirement.

### Requirement: Reusable page decisions and Q&A composition
The workflow SHALL expose reusable source-page verification and pure answer-page classification/Q&A composition helpers, preserving existing thresholds, masks, formatting and verified completion semantics, with documented unsupported-layout timing exceptions. Recovery SHALL use the single-attempt policy in Invalid successor recovery. Source: src/workflow/mod.rs, src/workflow/navigation.rs and src/workflow/orchestrator.rs.

#### Scenario: Equivalent navigation comparison
- **WHEN** forward movement or return-to-source is verified
- **THEN** both use the same masked source-page identity helper at threshold 0.999.

#### Scenario: Regression coverage
- **WHEN** rendering and classification regression tests run without device access
- **THEN** they cover blank/occupied/header-match decisions, UI-mask changes, different image sizes and exact Q&A separators/line breaks.
