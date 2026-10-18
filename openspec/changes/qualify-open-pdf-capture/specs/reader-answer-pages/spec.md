## ADDED Requirements

### Requirement: Stored association input remains historical in SDK acquisition decisions
The existing SDK acquisition decision seam SHALL consume the real historical Ledger through a read-only lookup under historical-binding-projection-contract.md. A saved match SHALL map only to historical evidence, and missing/failed/conflicted/tombstoned stored data SHALL remain unresolved rather than the model's affirmative Missing or RelevantModelAssociation input. Existing complete Synthetic observation/receipt guards SHALL precede lookup. This increment SHALL leave installed Reader behavior unchanged and grant no reuse, insertion, adoption, binding or rendering permission.

#### Scenario: Matching saved association is supplied to current-first assessment
- **WHEN** the guarded SDK decision consults a matching historical Ledger association
- **THEN** it remains unresolved as a current-effect decision, without unnecessary successor inspection, Store writes or SDK effects

#### Scenario: Positive recognition accompanies uncertain stored data
- **WHEN** positive ordinary or non-Buddy model recognition accompanies missing, failed, conflicted or tombstoned stored inspection
- **THEN** it cannot erase that uncertainty to produce a reuse candidate or insertion plan through this lookup

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

### Requirement: Synthetic return matching does not refresh logical claims or effect authority
The local placement model SHALL retain either uninspected end or the actual validated successor completion. Its pure continuity matcher SHALL require explicit Synthetic origins, exact original order/adjacency and SDK-created Previous receipt source matching that retained completion, target matching original source and supplied source matching returned completion. End plans SHALL require no receipt and unchanged full original observation still at end. Results SHALL remain point-in-time SyntheticSourceContinuity under buddy-source-continuity-contract.md, not proof of collection freshness, logical association/recognition refresh, native qualification or creation/render/binding permission. No effects, allocation, SDK private-field reconstruction or CreationRequest conversion SHALL be added.

#### Scenario: Supported synthetic return preserves the original anchor
- **WHEN** the Previous receipt closes from the retained inspected successor to the exact original page/order and the supplied completed observation agrees
- **THEN** the matcher returns source continuity while retaining historical original placement and conveying no effect permission

#### Scenario: Return or end evidence is wrong or stale
- **WHEN** receipt is missing/unexpected/foreign, direction or target differs, order/adjacency changes, or opaque completion/current evidence disagrees
- **THEN** matching refuses without navigation, creation, target allocation or fallback to a stale original source

#### Scenario: Logical claims change independently of SDK state
- **WHEN** Store-like association or recognition changes while supplied SDK continuity remains equal
- **THEN** a continuity result does not validate those claims or authorize an insertion, and future effectful use still requires separate current logical and SDK guards

### Requirement: Legacy classification is not positive non-Buddy or relevant ownership evidence
The pure synthetic consumer bridge SHALL exhaustively map ExistingQA to LegacyBuddy, Blank to Blank and Invalid to Unknown under buddy-legacy-recognition-bridge-contract.md, with explicit Synthetic observation/full context/conversation binding and valid order. It SHALL NOT produce RelevantBuddy, OrdinarySource or ConfirmedNonBuddy, claim the supplied enum's capture provenance or grant reuse/insertion/adoption/binding/render permission. The classifier and installed Reader SHALL remain unchanged.

#### Scenario: Unbound legacy header match
- **WHEN** ExistingQA is supplied with a matching synthetic observation and missing association
- **THEN** the current or successor model requires separately qualified adoption and creates no insertion plan

#### Scenario: Blank or invalid page classification
- **WHEN** Blank or Invalid is supplied with missing association evidence
- **THEN** the model remains unresolved rather than infer Buddy absence or duplicate creation eligibility

#### Scenario: Supplied classification belongs to another context
- **WHEN** opaque observation, logical page or desired conversation witness differs from the decision's expected context
- **THEN** existing witness guards refuse, and matching fields alone still do not establish actual capture/current-device provenance

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
