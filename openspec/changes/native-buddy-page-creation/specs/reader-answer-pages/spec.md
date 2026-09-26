## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
New Buddy conversations SHALL acquire targets through native-buddy-page-creation using exact source/target document/page IDs and session/revision ownership. Creation SHALL place a target immediately after source; binding reuse SHALL resolve the exact existing page. Screenshot similarity MAY corroborate navigation but SHALL NOT establish identity/completion. Source: REM25; reconcile onto accepted REM9 before implementation.

#### Scenario: End of document
- **WHEN** source is the final page and automatic insertion is qualified
- **THEN** acquisition creates/verifies one native writable successor without speculative reverse navigation or source feedback ink.

#### Scenario: Unconfirmed target
- **WHEN** target identity cannot be verified or ownership is cancelled
- **THEN** no rendering is authorized and fixed delay is not completion proof.

### Requirement: Blank and existing answer page classification
The system SHALL classify verified native Blank, verified BoundBuddy, or unsuitable/unknown using native identity/full-page content and conversation binding. Header pixels and masked whiteness SHALL NOT alone establish binding/blankness. Source: REM25/37/38.

#### Scenario: Hidden content
- **WHEN** a visually blank page has off-screen text/ink/layers or unknown content
- **THEN** it is not adopted as Blank and remains unchanged.

#### Scenario: Invisible header
- **WHEN** the exact bound page is scrolled or edited
- **THEN** verified binding identifies it without header recreation or clearing.

### Requirement: Invalid successor recovery
An unsuitable/unknown target SHALL stop rendering. Recovery SHALL require exact current ownership and a qualified bounded route to the saved source, without blind reverse swipes, repeated retries, compensating global undo or source feedback ink. Source: REM25; preserve REM9 no-source-feedback behavior.

#### Scenario: User changes document
- **WHEN** recovery sees a different document/session
- **THEN** input stops with reconciliation/cancellation and no mutation/navigation in the unrelated document.

#### Scenario: Source already current
- **WHEN** exact native identity confirms the saved source
- **THEN** recovery emits no navigation.

### Requirement: Reusable page decisions and Q&A composition
The workflow SHALL expose reusable acquisition/owner verification/native blank-bound classification for Reader, Writer refinement and blank-start, separate from REM38 layout and REM37 history and preserving content/failure guards. Source: REM25/37/38.

#### Scenario: Contract regression coverage
- **WHEN** acquisition tests run offline
- **THEN** fixtures cover identity, unknown schema, hidden content, reuse, duplicate requests and uncertain commits without claiming native compatibility.

#### Scenario: Renderer handoff
- **WHEN** acquisition returns an exact target receipt
- **THEN** the consumer renews ownership before output; the receipt does not authorize clearing drafts or rewriting history.
