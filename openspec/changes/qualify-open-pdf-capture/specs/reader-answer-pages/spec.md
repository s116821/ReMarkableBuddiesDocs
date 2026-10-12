## ADDED Requirements

### Requirement: Buddy-page recognition and reuse precede automatic insertion
The automatic product workflow SHALL identify and reuse the relevant current Buddy page or its relevant immediate successor before creating another page, under buddy-page-reuse-contract.md. It SHALL reuse the existing REM-37 document/page-to-conversation Store binding with current native identity/order and device qualification, not invent a separate registry. Unknown or stale associations SHALL fall back to recognition; missing binding or uncertain recognition SHALL NOT imply a non-Buddy page or authorize duplicate creation. Legacy header-only candidates SHALL require qualified acquisition/adoption rather than a silently trusted claim. Lower-level SDK insertion tests SHALL NOT establish this product requirement.

#### Scenario: Current or adjacent Buddy page is already relevant
- **WHEN** qualified association and current state or recognition establish the relevant Buddy page is current or immediately follows the original source
- **THEN** the workflow reuses that page and creates no duplicate; a verified current-page binding avoids unnecessary successor inspection

#### Scenario: Association is unknown or stale
- **WHEN** a binding is missing, conflicted, stale or inconsistent with current native identity/order, or a legacy candidate is unbound
- **THEN** the workflow falls back to recognition and qualified adoption as applicable, preserving content; unresolved recognition grants no insertion authority

#### Scenario: Visual inspection discovers a non-Buddy neighbor
- **WHEN** an ordinary guarded successor inspection positively identifies the existing neighbor as a non-Buddy page
- **THEN** after fresh source/session/order revalidation the workflow inserts between the ORIGINAL source and that same neighbor, preserving both and all saved ink regardless of the displayed inspection page

#### Scenario: Placement changes during inspection
- **WHEN** the original source, immediate neighbor, document/session or ordered inventory changes before insertion publication
- **THEN** the planned insertion refuses without relocating its anchor, creating a duplicate or replaying an effect

#### Scenario: Recognized Buddy candidate has an unresolved association
- **WHEN** recognition identifies a Buddy candidate but its relevance or existing conversation association is conflicting or unresolved
- **THEN** acquisition resolves/reuses/adopts that candidate or safely refuses; being unbound or not yet established as relevant SHALL NOT cause insertion beside it

### Requirement: Local SDK acquisition planning preserves reuse and original placement without effect authority
The experimental local consumer SHALL assess a relevant current Buddy candidate before successor inspection, consume supplied read-only association projections and observation-bound recognition, and retain missing/stale/imported/conflicting ownership as unresolved evidence rather than permission to duplicate a page. It SHALL preserve the ORIGINAL source and exact order through an SDK-created successor navigation receipt, with complete opaque current/receipt observation equality. Only positive ordinary source and confirmed non-Buddy successor, or exact synthetic end, SHALL yield an explicitly synthetic placement plan after the original source. This seam SHALL allocate no target, dispatch no SDK creation/navigation, mutate no Store/binding, construct no NativeCommitted or renderer permission, and leave installed Reader behavior unchanged under buddy-acquisition-decision-contract.md.

#### Scenario: Relevant current association is supplied
- **WHEN** the complete fresh synthetic current observation and exact page/conversation association agree
- **THEN** the model returns a reuse candidate with only current lookup and no successor inspection or creation

#### Scenario: Association or recognition remains uncertain
- **WHEN** binding is missing/historical/conflicted or recognition is blank, unavailable, unknown or mismatched
- **THEN** no insertion plan is produced from that uncertainty, and an unbound Buddy candidate requires separately qualified adoption

#### Scenario: Confirmed ordinary successor is displayed after inspection
- **WHEN** SDK successor evidence matches the original source, exact immediate neighbor/order and fresh completed observation, and positive non-Buddy recognition has no contradictory claim
- **THEN** the model retains an after-original/before-neighbor plan without retargeting creation to the inspected successor or dispatching the stale original source guard

## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
After agreement, the automatic native acquisition path SHALL first resolve current Buddy-page reuse under buddy-page-reuse-contract.md. A relevant current Buddy page SHALL be reused without a successor navigation attempt. Otherwise the path SHALL retain the ORIGINAL source identity/order, resolve its immediate successor, reuse a qualified relevant Buddy successor, or insert after that original source and before a positively identified non-Buddy successor after fresh placement revalidation. A verified end of document SHALL allow qualified creation after the original source once current-page reuse is ruled out. Unknown recognition/association SHALL not authorize creation. Verified RM2 navigation SHALL use ordered native identity and fresh settled pixels under the reader-responsiveness contract.

The explicitly authorized legacy/manual fallback SHALL retain its one-successor visual heuristic for unsupported layouts and its separately documented REM-25 fallback limits; it SHALL not be represented as the automatic path. Masked screenshot similarity at least0.999 SHALL still identify unchanged pages. Neither failure nor refusal SHALL draw source feedback.

#### Scenario: Automatic end of document
- **WHEN** qualified current-page assessment rules out reuse and verified native order has no successor after the original source
- **THEN** the automatic path may create after that source under the native creation/identity/preservation gates; a callback alone does not establish a usable target

#### Scenario: Legacy fallback has no successor
- **WHEN** the selected legacy/manual fallback has no known successor or its next-page attempt leaves the screenshot sufficiently similar to the source
- **THEN** no answer is written and a non-ink NoSuccessor diagnostic is recorded without creating a page or swiping backward

#### Scenario: Physical gesture and completion
- **WHEN** navigation requires a swipe
- **THEN** ordinary product gesture timing remains15 steps at10ms after50ms initial contact; verified-layout completion uses correlated state, while unsupported layouts retain documented legacy waits without verified-layout claims

### Requirement: Invalid successor recovery
In the automatic path, a positively identified non-Buddy successor SHALL be preserved and may permit qualified insertion between the ORIGINAL source and that neighbor after current source/session/order revalidation. An unknown/uncertain successor or recognized Buddy candidate with unresolved association SHALL grant no insertion permission. If restoring the original displayed source is required, recovery SHALL check source identity before navigation, attempt at most one previous-page swipe and verify once; any failure SHALL stop without retry or relocating the insertion anchor.

In the explicitly selected legacy/manual fallback, an Invalid successor SHALL retain the existing source precheck and bounded return behavior: if already on the saved source at similarity0.999, do not navigate; otherwise attempt at most one previous-page swipe and verify once, with no retry after failed verification or input/capture error. The caller SHALL record a non-ink typed failure after recovery or recovery failure, with no source-page display mutation. Legacy Invalid classification alone SHALL not authorize automatic insertion. Source: src/workflow/navigation.rs and the planned automatic acquisition contract.

#### Scenario: Automatic inspection finds an ordinary neighbor
- **WHEN** the inspected successor is positively non-Buddy and original source/session/order remain qualified immediately before publication
- **THEN** the automatic path may insert before that preserved neighbor under the native contract instead of treating it solely as a legacy InvalidSuccessor failure

#### Scenario: First return fails
- **WHEN** the single previous-page swipe does not restore source similarity
- **THEN** recovery reports Unconfirmed and the caller records Device without another swipe or insertion

#### Scenario: Already on the source
- **WHEN** recovery's initial check matches the saved source, including a forward attempt that did not leave it
- **THEN** recovery reports AlreadySource with no previous-page swipe
- **AND** the legacy forward no-movement guard records NoSuccessor without invoking reverse recovery at end of document

#### Scenario: Successful return
- **WHEN** the source is initially absent and the single previous-page swipe restores it
- **THEN** recovery reports Returned after one precheck, one swipe and one postcheck; an automatic insertion still requires its separate qualified acquisition and placement checks

#### Scenario: Navigation or capture error
- **WHEN** a source-identity check or the previous-page operation returns an error
- **THEN** recovery propagates that error and performs no further navigation or insertion; the render-error handler records Device without feedback input
