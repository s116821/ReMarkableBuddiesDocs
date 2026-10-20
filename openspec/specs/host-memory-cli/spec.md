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
Only query and inspect SHALL accept exact-dash stdin, bounded to inclusive1MiB and EOF; mutation/setup operations SHALL refuse dash before config/input/Store admission. File inputs SHALL remain absolute and bounded, with their existing decoder/API behavior unchanged. Caller deadlines and cancellation SHALL remain caller owned. New inspect stdin SHALL strictly decode the canonical Key including duplicate/unknown nested-scope refusal, then reuse existing profile/domain validation, all-current-head Inspection and guarded single-report output. Search discovery SHALL NOT become inventory or write authority.

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
