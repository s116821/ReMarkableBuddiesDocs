## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
New Buddy conversations SHALL acquire targets through native-buddy-page-creation using exact source/target document/page IDs and session/revision ownership. Creation SHALL place a target immediately after source; binding reuse SHALL resolve the exact existing page. Screenshot similarity MAY corroborate navigation but SHALL NOT establish identity/completion. Existing REM-9 navigation SHALL retain its ordered native identity, fresh bracketed pixels, positive settled-chrome evidence, monotonic deadline and input guards until a separately qualified native route replaces it. Unsupported capability SHALL refuse automatic mutation without inheriting verified-layout claims. Source: REM25; reconciled against REM-9 Docs e7fbdc44 and Rust 3df3b1e6.

#### Scenario: End of document
- **WHEN** source is the final page and automatic insertion is qualified
- **THEN** acquisition creates/verifies one native writable successor without speculative reverse navigation or source feedback ink.

#### Scenario: Unconfirmed target
- **WHEN** target identity cannot be verified or ownership is cancelled
- **THEN** no rendering is authorized and fixed delay is not completion proof.

#### Scenario: Existing swipe route
- **WHEN** the accepted REM-9 swipe path is used
- **THEN** its 15-step, 10 ms physical gesture after 50 ms initial contact and guarded completion semantics remain intact; no timed-out swipe is repeated or unsupported-layout wait promoted to proof.

#### Scenario: Insertion changes native order
- **WHEN** the correlated owned insertion commits a new page
- **THEN** only the exact expected source-preserving order transition may establish the acquisition's new structural receipt; unrelated order changes, stale visits or external input cancel the operation without repinning the active source baseline.

### Requirement: Blank and existing answer page classification
The system SHALL classify verified native Blank, verified BoundBuddy, or unsuitable/unknown using native identity/full-page content and conversation binding. Header pixels and masked whiteness SHALL NOT alone establish binding/blankness. Source capture ownership and downstream content guards from REM-9 SHALL remain enforced; a fresh capture SHALL NOT silently replace a lost source baseline. Source: REM25/37/38.

#### Scenario: Hidden content
- **WHEN** a visually blank page has off-screen text/ink/layers or unknown content
- **THEN** it is not adopted as Blank and remains unchanged.

#### Scenario: Invisible header
- **WHEN** the exact bound page is scrolled or edited
- **THEN** verified binding identifies it without header recreation or clearing.

### Requirement: Invalid successor recovery
An unsuitable/unknown target SHALL stop rendering. Recovery SHALL require exact current ownership and a qualified bounded route to the saved source, without blind reverse swipes, repeated retries, compensating global undo or source feedback ink. Any retained REM-9 previous-page recovery SHALL remain limited to one guarded attempt and one verification, with no retry after failure/input loss. Its non-ink diagnostic classifications and latched cancellation behavior SHALL remain intact. Source: REM25; accepted REM-9 no-source-feedback behavior.

#### Scenario: User changes document
- **WHEN** recovery sees a different document/session
- **THEN** input stops with reconciliation/cancellation and no mutation/navigation in the unrelated document.

#### Scenario: Source already current
- **WHEN** exact native identity confirms the saved source
- **THEN** recovery emits no navigation.

#### Scenario: Recovery cannot confirm the source
- **WHEN** the single authorized recovery attempt fails, times out or loses input ownership
- **THEN** no further input occurs, the non-ink diagnostic is retained and latched input failure cannot be cleared by a later observation.

### Requirement: Reusable page decisions and Q&A composition
The workflow SHALL expose reusable acquisition/owner verification/native blank-bound classification for Reader, Writer refinement and blank-start, separate from REM38 layout and REM37 history and preserving content/failure guards. REM-9 completion events or paced fresh-state polling SHALL remain correlated to operation/page/session with monotonic deadlines and sticky cancellation. Physical gesture timing and documented unsupported-layout exceptions SHALL remain distinct from completion assumptions. Existing Q&A formatting remains unchanged until its owning renderer change. Source: REM25/37/38 and accepted REM-9.

#### Scenario: Contract regression coverage
- **WHEN** acquisition tests run offline
- **THEN** fixtures cover identity, unknown schema, hidden content, reuse, duplicate requests and uncertain commits without claiming native compatibility.

#### Scenario: Renderer handoff
- **WHEN** acquisition returns an exact target receipt
- **THEN** the consumer renews ownership before output; the receipt does not authorize clearing drafts or rewriting history.
