# Host memory CLI

## Purpose
Explicit offline maintenance and query over Buddy-owned Store data.

## Requirements

### Requirement: Offline explicit memory maintenance
The application SHALL provide one-shot inspect, query, put, forget and explicit aggregate/selection initialization and registration over existing Store identities, revisions, CAS and tombstones, without starting model, Reader, device or sync workers. Provenance SHALL remain author asserted.

#### Scenario: Local and selected lifecycle
- **WHEN** valid explicitly configured local or selected memory operations are requested
- **THEN** the CLI preserves immutable fact identity and claim, records valid mutations, returns bounded report-v1 JSON and distinguishes empty, partial, busy, unavailable, unsupported, conflict and invalid input outcomes.

### Requirement: Storage mode and current handoff lifetime
The CLI SHALL acquire the correct ordinary or exact SharedGroup mode lease before domain authority and retain it through actual report output or failure cleanup. It SHALL reject incompatible legacy sync, foreign or isolated modes and preserve selected charged currentness, custody and report sealing.

#### Scenario: Output is still consuming authority
- **WHEN** mode replacement or selected-state change races a report handoff
- **THEN** mode replacement is denied while its lease is live and stale selected output refuses before writing data; a partial writer failure SHALL NOT append a replacement report or replay a mutation.

### Requirement: Bounded query input and consumer compatibility
Query and inspect SHALL accept exact-dash stdin, bounded to inclusive1MiB and EOF. Only the separately specified `prepare-forget`, prepared `forget` confirmation and `forget-receipt` protocol SHALL add stdin maintenance authority; put/setup operations SHALL refuse dash before config/input/Store admission. File inputs SHALL remain absolute and bounded, with their existing decoder/API behavior unchanged. Caller deadlines and cancellation SHALL remain caller owned. New inspect stdin SHALL strictly decode the canonical Key including duplicate/unknown nested-scope refusal, then reuse existing profile/domain validation, all-current-head Inspection and guarded single-report output. Search discovery SHALL NOT become inventory or write authority.

#### Scenario: Manager consumes a real report
- **WHEN** local/selected populated, complete-empty, Busy, missing-store or domain-invalid queries run through file and supported stdin input
- **THEN** real report-v1 output preserves Unicode, revisions and asserted provenance with truthful status; smaller consumer output caps fail without truncated or empty-success substitution.

#### Scenario: Explicit single-fact inspection
- **WHEN** the caller deliberately inspects one valid configured-profile Key using stdin
- **THEN** the existing report preserves every admitted current value/tombstone head and all local competing raw heads, retains selected whole-view conflict/domain refusal, and distinguishes no current heads for that key from refusal without implying a complete inventory or ongoing write authority.

#### Scenario: Strict new scope wire and legacy compatibility
- **WHEN** inspect stdin has duplicate/unknown top or nested fields, invalid/nil identities or a foreign profile
- **THEN** it refuses before Store admission; canonical global/document requests reuse the unchanged domain validator, and existing file decoding remains unchanged.

#### Scenario: Selected currentness at stdout
- **WHEN** a selected inspection is stale or forged before output, or writing a prefix fails
- **THEN** the existing guarded writer refuses stale data before any output and never appends a replacement report after attempted partial output.

### Requirement: Prepared conditional one-fact forget
The host CLI SHALL provide bounded strict stdin preparation and explicitly confirmed one-fact forget with original configured profile/paths, Store actor/generation, mode token and admitted local/selected identity. Selected catalog/aggregate acceptance evidence SHALL be compared under existing gates independently of Key/head IDs. Existing regular-file APIs SHALL remain unchanged and unrelated mutations/setup SHALL retain early stdin refusal. Search/inspection alone SHALL NOT authorize mutation.

#### Scenario: Same-view deliberate preparation
- **WHEN** a host prepares one deliberate configured-profile fact and intent UUID
- **THEN** one guarded supported-value preview and immutable same-admission evidence are returned, while absent/tombstone/conflicting/opaque or unavailable views refuse without head selection or initialization.

#### Scenario: Changed original binding
- **WHEN** config, paths, profile, mode/re-entry or selected catalog/base/aggregate generations change despite identical Key/head IDs
- **THEN** confirmation refuses before mutation rather than refreshing original preconditions or switching namespace.

#### Scenario: Historical acknowledgement and receipt-only reconciliation
- **WHEN** the original exact request has a provable accepted receipt and the target later changes
- **THEN** a historical acknowledgement may be returned only after original namespace/predecessor checks, without another tombstone or current-deleted claim; receipt absence or unprovable evidence SHALL NOT dispatch a mutation.

#### Scenario: Unknown outcome remains explicit
- **WHEN** confirmation may have committed but output is lost, partial, cancelled or disconnected
- **THEN** the host retains the exact original intent and uncertainty, clears stale detail, never auto-retries or creates replacement intent, and requires fresh deliberate inspection for current state.

#### Scenario: Tombstone scope and compatibility
- **WHEN** a valid prepared forget commits locally or to admitted selected membership
- **THEN** history and original documents remain, no disk purge or immediate cloud propagation is claimed, and legacy file/unsupported-build behavior remains explicit without remote staging or service/provider startup.
