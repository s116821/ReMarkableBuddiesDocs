## ADDED Requirements
### Requirement: Measured responsive Reader interaction
Reader SHALL measure and distinguish trigger qualification/release, provider request/response, answer rendering and ready state. Local phase costs and provider time SHALL be separated. Source-page ink feedback SHALL be retired rather than optimized. Representative native trigger/capture/navigation/text and source-preservation evidence SHALL validate this salvage change; revised integrated feedback/latency/history acceptance belongs to REM40/43/35. Historical marker-width matrices SHALL remain explicitly superseded, not marked passed.

#### Scenario: Measured improvement
- **WHEN** before/after responsiveness is reported
- **THEN** individual repeated values, operation counts, median/max, source/build/tool state and provider spans are retained; fixed text/conditions distinguish local gains from shorter model answers.

#### Scenario: Guarded refusal
- **WHEN** a native status guard stops before output
- **THEN** the run is reported as failed availability, not successful Q&A or ready-state latency; exact internal frames are captured only with diagnostic opt-in and ownership guards remain enforced.

#### Scenario: Incomplete performance gate
- **WHEN** budgets, successful workflow or required preservation checks remain unmet
- **THEN** the responsible revised gate stays incomplete, with explicit evidence and downstream ownership; REM35 integrated acceptance is never implied by microbenchmark or simulator results.

### Requirement: No source-page feedback mutations
Normal Reader processing SHALL emit no source status/error pen strokes, erasures,
tool-selection operations or indicator recovery writes. Failures SHALL remain
sanitized diagnostic classifications until the Buddy-page feedback feature lands.
Existing recovery records SHALL be preserved and cause read-only startup refusal.

#### Scenario: Success or refusal
- **WHEN** a request succeeds, declines recognition, loses navigation, or encounters provider/output failure
- **THEN** the source status area, original ink and tool settings remain unmodified by feedback; no indicator lease or cadence wait occurs.

#### Scenario: Legacy recovery record
- **WHEN** any unresolved legacy status recovery path exists or cannot be safely checked
- **THEN** startup refuses further input without modifying the record or automatically restoring/erasing from it.

#### Scenario: Diagnostic-only legacy implementation
- **WHEN** historical diagnostic helpers remain in the source tree
- **THEN** normal construction and service/simulator paths cannot enable them; their old tests and timings do not claim current product feedback.

#### Scenario: Input or owner changes during inference
- **WHEN** completed external input or a different page/session appears after source capture while a provider is pending
- **THEN** the retained read-only request guard rejects the request before navigation/output and latches failure without drawing or acquiring a style lease; subsequent capture cannot silently establish a new source baseline for that request.

### Requirement: Deterministic completion sequencing
Reader operations SHALL prefer supported completion events and verified postconditions over assuming success after a fixed delay. When usable events are unavailable, operations SHALL use paced fresh-state polling with monotonic deadlines and cancellation. Observations SHALL be correlated to the active operation, page and session; device mutations SHALL remain serialized with existing ownership, restoration and recovery guarantees. Fixed waits SHALL be documented protocol, measured physical or observability exceptions, with scope and validation. Legitimate gesture timing, cadence, polling intervals, backoff and timeouts SHALL remain distinct from completion assumptions. Source: REM9 architecture steering September22.

#### Scenario: Supported completion event
- **WHEN** a completion notification arrives for an active operation
- **THEN** only a fresh correlated verified postcondition advances the operation; the notification alone does not prove readiness.

#### Scenario: Missing or unusable signal
- **WHEN** supported notifications are unavailable or lost
- **THEN** bounded fresh-state polling returns on the verified predicate or fails/cancels at its bound; elapsed time alone never means success.

#### Scenario: Stale or repeated signals
- **WHEN** stale, duplicate, out-of-order or wrong-operation/page/session events arrive
- **THEN** they cannot repeat a mutation or complete another operation, and cancellation prevents late observations reviving cancelled work.

### Requirement: Verified-layout navigation readiness
On the verified RM2 layout, navigation SHALL resolve the requested adjacent native
page from validated current page order before one swipe, then establish fresh
bracketed target identity and positive settled-chrome evidence within a monotonic
deadline under input guards. It SHALL preserve downstream eligibility and strict
source-content guards, never refresh an active baseline or repeat a timed-out
swipe. Unsupported layouts retain explicitly documented existing fallback behavior
without inheriting verified-layout claims.

#### Scenario: Metadata and pixels arrive separately
- **WHEN** metadata points at the target before its pixels arrive, or target pixels arrive before metadata
- **THEN** neither alone completes navigation; fresh correlated owner/order, positive chrome, distinguishable target content and matching observations are required, with late observations rejected.

#### Scenario: Inserted notes or page boundary
- **WHEN** the requested neighbor is an inserted notes page or no neighbor exists
- **THEN** native page order determines the neighbor regardless of PDF redirect index; a known boundary issues no swipe.

#### Scenario: Identical-looking pages or occupied gutter
- **WHEN** source and target cannot be visually distinguished, or legitimate gutter ink prevents the conservative chrome predicate
- **THEN** completion refuses safely at its bound without ignoring content, repeating input or claiming successful navigation; an inked question source to a blank successor remains a distinct positive case.

#### Scenario: Ownership or order changes
- **WHEN** a wrong neighbor/session/visit, page-order/redirect mutation or external input occurs
- **THEN** navigation cancels before further input or classification, with no stale success or unsafe repeated swipe.
