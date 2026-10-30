## ADDED Requirements

### Requirement: Explicit text sources preserve honest scope and provenance
The Writer SHALL consume explicitly supplied normalized text with document/digest,
extractor revision and ordered page/section provenance, preserving it durably in
the existing Source domain before dispatch. Page scope SHALL include every
supplied unit for the selected page; notebook scope SHALL include all supplied
units in order. Neither SHALL imply original-byte retention, successful OCR,
native capture or complete physical-notebook extraction. Oversized source/history
SHALL refuse before dispatch rather than silently truncate or select relevance
hits while claiming complete source coverage.

#### Scenario: Page and supplied notebook differ
- **WHEN** generation selects one page or all supplied notebook units
- **THEN** the provider receives exactly the selected ordered text and locations, and the durable draft retains the corresponding source identity/digest.

#### Scenario: Source cannot fit
- **WHEN** complete selected source/history exceeds the receiving command's explicit bound
- **THEN** generation reports a bounded selection-required/too-large result without provider dispatch or a partial whole-notebook claim.

### Requirement: Durable Writer drafts refine within one conversation
The Writer SHALL use the existing provider and conversation Ledger, retain exact
user requests and separate explicit guidance/source data, and store proposals as
Writer Generated drafts. Refinement SHALL name one unique current draft and use
its original source within the same conversation, without rewriting prior turns
or treating unrendered drafts as native-verified Completed history. Optional
personalization SHALL remain a preference, and subject memory SHALL NOT be
required. Explicit selected-draft export preparation SHALL return the existing
PreparedNote without sending an external note or operating the tablet.

#### Scenario: Generate then refine after restart
- **WHEN** a saved Writer draft is selected with a new exact refinement request after Store reopen
- **THEN** a new draft in the same conversation preserves prior requests/source facts and the selected draft, and neither draft claims native completion.

#### Scenario: Prepare deliberate export
- **WHEN** a caller names a unique current draft/source and valid correlation/effect identities
- **THEN** preparation returns the exact selected content and provenance in PreparedNote with no Mem write, native capture or rendering.

#### Scenario: Regeneration retains logical export scope
- **WHEN** a new deliberate generation uses changed source content for the same document identity and explicit page/notebook selection
- **THEN** prepared export retains the same logical source scope and advances its content/draft revision, allowing the existing correlation to update the same note rather than being rejected as a different source scope.

### Requirement: Provider attempts have fresh ownership and truthful cancellation
Only this invocation's freshly committed preparation SHALL authorize provider
dispatch. Receipt replay, concurrent winners and lost local acknowledgments SHALL
NOT authorize another call. A same-Store owner SHALL span preparation, provider
wait and result publication without holding the Store index lock over HTTP.
Cancellation SHALL suppress late drafts; stale/deleted/conflicting state SHALL
refuse result publication. Unknown post-dispatch state SHALL NOT automatically
retry or claim no remote cost. Errors SHALL use sanitized fixed outcomes.

#### Scenario: Replay or overlap
- **WHEN** two same-Store callers overlap or a prepared operation is retried after an uncertain acknowledgment
- **THEN** at most one fresh invocation may dispatch, and the other reports Busy or historical/pending without another call.

#### Scenario: Canceled or stale result
- **WHEN** cancellation or relevant state change occurs while the model is pending
- **THEN** a late result cannot become a current draft or a native/export permission, and the recorded outcome does not claim the remote call was unbilled.

#### Scenario: Input changes before preparation
- **WHEN** conversation history or the selected draft changes after input assembly begins and before preparation commits
- **THEN** preparation must remain bound to the root captured before its reads and the exact selected draft content, refusing stale input instead of guarding new state while sending old text.
