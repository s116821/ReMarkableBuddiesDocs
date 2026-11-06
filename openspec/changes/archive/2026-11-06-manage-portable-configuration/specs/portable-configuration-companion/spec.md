## ADDED Requirements

### Requirement: Shared explicit portable preference file workflow
Both browser and Electron companions SHALL offer deliberate export and file-based
Review/Confirm import of the existing V1 allowlisted saved preferences. Preview
SHALL reveal only setting names and declaration origins, preserve backend omission/
null semantics and expose no reset/default/value editor. The backend SHALL remain
sole owner of overlay construction, whole Config validation, Store admission and
conditional publication; no direct Config writer or alternate sync engine is added.

#### Scenario: Sparse private preference import
- **WHEN** a user selects a valid bounded portable preference file for a supported connected target
- **THEN** review shows only actual changed names/origins and a distinct explicit confirmation may dispatch one original-bound Apply while omitted and excluded destination declarations are retained.

#### Scenario: No-op or unsupported target
- **WHEN** the producer reports no change or missing/unsupported capability/state
- **THEN** no Apply is dispatched and the UI reports the limited result without fallback or initialization.

### Requirement: Private file transport and honest export handoff
The consumer SHALL validate complete bounded public/private frames and original
phase correspondence, keeping artifact/text/intent/hashes out of reduced results
except the explicitly requested export-file payload. It SHALL use fixed guarded
wired commands, ephemeral private custody and the original producer bounds. File
selection/download SHALL NOT imply durable save, private OS permissions, restored
state or running activation; no artifact spool, log or automatic persistence is added.

#### Scenario: Explicit private export
- **WHEN** a complete original export and its content digest/summary match
- **THEN** only the deliberate file-save flow receives the bounded artifact, ordinary UI state remains redacted and the saved Config is unchanged.

#### Scenario: Malformed or leaking input/output
- **WHEN** duplicate/unknown/type/version/bound/encoding or original phase/digest/identity checks fail
- **THEN** the whole invocation refuses without arbitrary path/command access, partial preview or disclosure of private content.

### Requirement: Original import custody and cross-lane lifetime
One shared active owner and at most eight non-evicted unresolved originals SHALL
bound work. Ready authority SHALL expire after120seconds and invalidate before
external I/O/navigation/identity changes. Possible Apply dispatch SHALL retain its
original unknown through loss/cancel/late results without retry/rebase/rollback.
Explicit Status SHALL observe only the original desired bytes without artifact,
Store or historical-publisher/runtime claims. Stale cancellation SHALL NOT cancel
or release another operation or erase unrelated original uncertainty.

#### Scenario: Lost Apply with another active operation
- **WHEN** an import result is lost and its retained reference is cancelled or checked while another operation owns I/O
- **THEN** the original remains unknown, the newer owner is preserved and no repeated Apply or refreshed intent occurs.

#### Scenario: Original desired file currently observed
- **WHEN** explicit Status returns exact original desired-file correspondence
- **THEN** the UI may report current desired-file observation while preserving the distinction from historical publication and running behavior.

#### Scenario: Verified reply invalidated before final publication
- **WHEN** a private verified reply is invalidated before the last bridge generation/publication guard
- **THEN** its original reservation remains unknown and recoverable rather than being evicted before the late reply is rejected.

### Requirement: Attributed guarded two-host qualification
Acceptance SHALL separate exact implemented-producer captures from synthetic fault
fixtures and exercise both guarded browser/Electron file/UI paths, cross-lane owner
races, privacy and required both-OS current checks. Only the completed consumer
scope SHALL be canonically synced and archived in its linked delivery.

#### Scenario: Producer and consumer delivery
- **WHEN** the workflow is proposed for merge
- **THEN** exact producer/source/capture identities, meaningful host/file/fault results, current checks and independent review are available without claiming tablet/provider/native qualification.
