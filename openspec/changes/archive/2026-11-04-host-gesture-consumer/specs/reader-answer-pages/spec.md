## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
After agreement, the system SHALL recapture the source and resolve one successor attempt. Verified RM2 navigation SHALL use ordered native identity and fresh settled pixels under the reader-responsiveness contract. Unsupported ordinary layouts or missing portrait admission SHALL refuse before a swipe. Masked screenshot similarity at least0.999 SHALL still reject unchanged pages without a reverse swipe. Neither failure nor refusal draws source feedback.

#### Scenario: End of document
- **WHEN** the known native page order has no successor or the next-page attempt leaves the screenshot sufficiently similar to the source
- **THEN** no answer is written and a non-ink NoSuccessor diagnostic is recorded without creating a page or swiping backward.

#### Scenario: Physical gesture and completion
- **WHEN** navigation requires a swipe
- **THEN** physical gesture timing remains15 steps at10ms after50ms initial contact; verified-layout completion uses correlated state, and unsupported ordinary layouts refuse before emission.

### Requirement: Reusable page decisions and Q&A composition
The workflow SHALL expose reusable source-page verification and pure answer-page classification/Q&A composition helpers, preserving existing thresholds, masks, formatting and verified completion semantics. Recovery SHALL use the single-attempt policy in Invalid successor recovery. Source: src/workflow/mod.rs, src/workflow/navigation.rs and src/workflow/orchestrator.rs.

#### Scenario: Equivalent navigation comparison
- **WHEN** forward movement or return-to-source is verified
- **THEN** both use the same masked source-page identity helper at threshold 0.999.

#### Scenario: Regression coverage
- **WHEN** rendering and classification regression tests run without device access
- **THEN** they cover blank/occupied/header-match decisions, UI-mask changes, different image sizes and exact Q&A separators/line breaks.
