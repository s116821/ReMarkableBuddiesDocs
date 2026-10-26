## ADDED Requirements

### Requirement: Explicit stored ordinary feedback receiving
The ordinary feedback receiving API SHALL resolve an explicit conversation and outcome-fact identity from one bounded current-head Conversation metadata snapshot under existing ordinary-mode custody, using existing domain/root/chronology validation. It SHALL describe only the exact retained fact with an existing matching turn through the delivered static catalog. It SHALL preserve original historical identity and refuse incomplete, conflicting, tombstoned, unsupported, foreign or ambiguous context without returning a partial or fabricated no-error result. Source: retained outcome facts and the existing static catalog's caller-validation contract; unfinished pre-page feedback receiving scope.

#### Scenario: Persisted error survives a later read
- **WHEN** an ordinary associated terminal fact is persisted and the Store is reopened while no current Buddy page is admitted
- **THEN** explicit identity resolution returns the same original fact/conversation/turn and deterministic static description without image reads, writes or native permission.

#### Scenario: Context is unsafe or absent
- **WHEN** root, fact, turn, mode, schema, chronology or complete Store availability cannot be established under the existing snapshot result bounds
- **THEN** the operation refuses with no description, partial list, fabricated complete empty result or persistent mutation.

### Requirement: Historical feedback does not imply pending presentation
The stored receiver SHALL return at most one bounded static catalog description, preserve the catalog's completed/no-error and uncertainty behavior and exclude raw conversational, completion, diagnostic and credential content. An explicit historical selection SHALL NOT imply current outcome, undisplayed state, queue membership, successful presentation or permission to modify a page. It SHALL create no new persisted state and SHALL NOT claim pre-attempt/unassociated error retention. Source: original feedback catalog boundary, historical-not-live identity rules and separate native admission requirements.

#### Scenario: Repeated or older historical selection
- **WHEN** the same retained fact is requested repeatedly or after its turn later advances
- **THEN** the original historical description remains stable without a new receipt, duplicate record, current-state claim or inferred presentation acknowledgment.

#### Scenario: Completed and uncertain facts
- **WHEN** a resolved fact is completed or records uncertain external action
- **THEN** completed history returns no error description and uncertainty retains deterministic checking language without promising cancellation, undo or delivery.
