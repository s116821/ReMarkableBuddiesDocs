# sanitized-conversation-feedback Specification

## Purpose
Describe typed historical outcomes with static user-facing text while preserving diagnostic secrecy and separate current-rendering/cancellation authority.
## Requirements
### Requirement: Sanitized historical feedback description
The feedback catalog SHALL consume existing typed historical outcome facts and return only original identity plus deterministic static code/text. It SHALL NOT copy raw diagnostic, provider, auth, request or answer text into user-facing descriptions or grant current rendering permission.

#### Scenario: Malicious or secret-containing conversational text
- **WHEN** recorded request/output or diagnostic text contains sensitive data
- **THEN** catalog output remains typed static text with original fact identity and no source-text serialization or ledger mutation.

### Requirement: Truthful uncertainty and refusal
Uncertain reason or ReconcileRequired state SHALL produce reconciliation feedback rather than claiming canceled, undone or delivered output. Completed facts SHALL produce no error description; nil identities and unsupported non-feedback states SHALL refuse.

#### Scenario: Cancellation overlaps uncertain external action
- **WHEN** historical outcome or reason denotes uncertain submitted/device action
- **THEN** description requires checking and cannot claim rollback, cancellation completion or a new successful delivery.

#### Scenario: Unsupported or completed historical fact
- **WHEN** identities are missing, state is unsupported or a fact is already completed
- **THEN** invalid context refuses and completed context yields no new error or success receipt.


### Requirement: Explicit stored ordinary feedback receiving
The ordinary feedback receiving API SHALL resolve an explicit conversation and outcome-fact identity from one bounded current-head Conversation metadata snapshot under existing ordinary-mode custody, using existing domain/root/chronology validation. Snapshot matching SHALL include explicit root/fact record IDs regardless of malformed/foreign payload metadata and retain all selected heads. Before domain snapshot inspection, the receiver SHALL refuse every relevant selected tombstone, conflict/duplicate head and non-schema-one or unsupported record. It SHALL describe only the exact retained fact with an existing matching turn through the delivered static catalog. It SHALL preserve original historical identity and refuse incomplete, conflicting, tombstoned, unsupported, foreign or ambiguous context without returning a partial or fabricated no-error result. Source: retained outcome facts and the existing static catalog's caller-validation contract; unfinished pre-page feedback receiving scope.

#### Scenario: Persisted error survives a later read
- **WHEN** an ordinary associated terminal fact is persisted and the Store is reopened while no current Buddy page is admitted
- **THEN** explicit identity resolution returns the same original fact/conversation/turn and deterministic static description without image reads, writes or native permission.

#### Scenario: Context is unsafe or absent
- **WHEN** root, fact, turn, mode, schema, chronology or complete Store availability cannot be established under the existing snapshot result bounds
- **THEN** the operation refuses with no description, partial list, fabricated complete empty result or persistent mutation.

### Requirement: Historical feedback does not imply pending presentation
The stored receiver SHALL return exactly one static catalog description of at most 1024 serialized UTF-8 bytes on success, refuse unsupported completed records and preserve uncertainty behavior and exclude raw conversational, completion, diagnostic and credential content. An explicit historical selection SHALL NOT imply current outcome, undisplayed state, queue membership, successful presentation or permission to modify a page. It SHALL create no new persisted state and SHALL NOT claim pre-attempt/unassociated error retention. Source: original feedback catalog boundary, historical-not-live identity rules and separate native admission requirements.

#### Scenario: Repeated or older historical selection
- **WHEN** the same retained fact is requested repeatedly or after its turn later advances
- **THEN** the original historical description remains stable without a new receipt, duplicate record, current-state claim or inferred presentation acknowledgment.

#### Scenario: Completed records remain excluded
- **WHEN** a selected record is a completed OutcomeFact requiring schema two and VerifiedSubmitted settlement, or an invalid schema-one completed fact
- **THEN** the receiver refuses without changing domain validation or claiming an ordinary completed/no-error success.

#### Scenario: Uncertainty and numeric output bound
- **WHEN** a supported historical fact records uncertain external action or any supported catalog branch is serialized
- **THEN** uncertainty retains deterministic checking language without promising cancellation, undo or delivery, and output over 1024 UTF-8 bytes refuses before return.

#### Scenario: Historical fact outlives its turn state
- **WHEN** the explicitly selected retained fact has an outcome different from its turn's later current outcome
- **THEN** matching original fact/turn/conversation identity remains the membership check without rewriting history or requiring outcome equality.
