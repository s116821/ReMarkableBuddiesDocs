## ADDED Requirements

### Requirement: Deliberate single-fact inspection in both hosts
The Manager SHALL offer the same explicit read-only current-head inspection for a
key selected from displayed global search results in browser/helper and Electron.
It SHALL use only the published inspect-stdin contract through fixed protected
wired host adapters and SHALL NOT infer a complete inventory or write authority.

#### Scenario: User selects a discovered fact
- **WHEN** the user deliberately requests current revisions of a displayed search fact
- **THEN** both hosts send only that exact global Key through the fixed bounded operation and distinguish prior search context from fresh detail.

#### Scenario: Older or unavailable producer
- **WHEN** the installed producer lacks inspect stdin or configuration/store admission refuses
- **THEN** the UI reports unsupported/unavailable with truthful status and actual incomplete flag, without staging files, query fallback or empty-success substitution.

### Requirement: Complete supported heads and requested identity
The host SHALL validate every head against the requested derived record UUID and
supported envelope/Fact schema before exposing a fresh reduced public view. It
SHALL retain all supported admitted heads and tombstones, including all local
concurrent heads, and preserve selected whole-view refusal. Unsupported data SHALL
refuse the entire view rather than silently filter, round or truncate it.

#### Scenario: Multiple heads or tombstone
- **WHEN** a complete valid local report contains concurrent value/tombstone heads
- **THEN** every distinct current revision is preserved, multiple heads are identified as conflict and no array order, time or confidence selects a winner.

#### Scenario: Selected whole-view refusal
- **WHEN** selected projection refuses a conflict or invalid domain/ownership/custody state, including unrelated registered state
- **THEN** the UI preserves the actual unavailable/refusal status and incomplete flag without manufacturing a successful conflicting array, choosing a winner or falling back to local memory.

#### Scenario: Foreign or unsupported head
- **WHEN** any head has a foreign derived record ID, mismatching payload key, unsupported shape or unsafe numeric value
- **THEN** the whole view refuses, including null-payload tombstones that still require record identity verification.

#### Scenario: No current heads
- **WHEN** the valid requested-key inspection is ok with incomplete false and an empty array
- **THEN** the UI reports no current heads for that key in the admitted view, without asserting a globally empty inventory or erased history.

### Requirement: Bounded private transport and public validation
The fixed transport SHALL preserve exact EOF, input/output caps and deadlines,
reject malformed/duplicate/trailing/partial output and nonzero exit, and retain
existing wired trust/session/identity checks. Public HTTP/IPC and controller SHALL
revalidate reduced supported views and refuse raw private reports or caller paths.

#### Scenario: Partial or oversized output
- **WHEN** output exceeds the consumer cap or fails complete single-report validation
- **THEN** no partial head set, stale success or healthy empty result is exposed and diagnostics contain no raw input or report content.

#### Scenario: Guarded public host entry
- **WHEN** a caller sends an invalid key/connection, raw private report or arbitrary command/path through a public bridge
- **THEN** actual host/IPC guards refuse before granting the fixed inspection capability.

### Requirement: Detail lifetime and evidence boundaries
Fresh detail SHALL be bound to the explicit request and current host/connection/
boot/session generation and SHALL be invalidated on new search, tablet read,
refresh, cancellation or disconnect. Evidence SHALL distinguish actual producer
reports, synthetic transports/UI and physical/provider/native qualification.

#### Scenario: Stale asynchronous completion
- **WHEN** detail finishes after invalidation, even when connection and boot IDs repeat
- **THEN** it cannot restore an old result or imply continuing freshness or future mutation authority.

#### Scenario: Host fixture qualification
- **WHEN** the paired increment is verified for delivery
- **THEN** actual attributed producer reports feed the consumer parser, both host distributions exercise real guards and retained packages, and synthetic success does not become tablet/provider/native qualification.

Source traceability: producer Docs66 contract at86bb4c0a594666b98135d6552fd3504a488af4a7;
current public memory search/host-maintenance guidance and selected-fact coordination.
Implementation is present in paired Manager29; current source hosted package gates pass;
producer delivery is verified and final composed review/merge remain external gates. This traceability
checkpoint is retained with the change, not copied into the canonical requirement body.
