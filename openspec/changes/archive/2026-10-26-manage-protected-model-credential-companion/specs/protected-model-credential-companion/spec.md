## ADDED Requirements

### Requirement: Shared fixed-reference protected-file management
Both companions SHALL deliberately install/replace/remove only the already declared protected model-credential file under contract.md, preserving exact accepted UTF8 and producer original/no-op/admission semantics without reference, provider or runtime changes. Source basis: canonical declared-model-credential, archived exact producer/manual/current source and REM42 selection.

#### Scenario: Deliberate valid action or no-op
- **WHEN** a user begins a fresh observed file editor and explicitly chooses Install, Replace or Remove
- **THEN** only the original-bound action is prepared/applied at most once, absent/present/mode constraints and producer-only no-op are preserved, and no discovery/root setup/reference edit/transaction or authentication claim follows.

#### Scenario: Invalid original, text or envelope
- **WHEN** original admission, strict shape/identity/binding/action/target, Unicode/nonblank/byte or encoded envelope bounds fail
- **THEN** the invocation refuses without normalization, unsafe fallback, private echo, refreshed conditions or late apply.

### Requirement: Confidential lifetime and safe original-only reconciliation
Raw credential text and all secret-derived hashes/BINDING/INTENT SHALL remain private bounded-lifetime transport state, excluded from safe DTOs, signals/logs/errors/persistence, with synchronous private draft/actual DOM erasure and original-only status under contract.md/lifetime.md. Source basis: producer confidentiality/uncertainty contract, existing opaque-text helpers and explicit consumer TTL/tombstone design.

#### Scenario: Submission, supersession or expiry
- **WHEN** private entry is submitted, invalidated, superseded by any peer, stopped, hidden, disconnected or expired
- **THEN** raw draft and actual input clear before the relevant await/event boundary, owned mutable buffers/references are released within their bounds, and late replies cannot refill/clear a newer editor.

#### Scenario: Unknown original, refused status or private expiry
- **WHEN** apply may have run or status fails/cancels/expires after an unresolved observation
- **THEN** only the original confidential intent can be checked; no replay/refresh/settlement occurs, private expiry leaves a safe unavailable unknown tombstone counting against capacity, and no secret-derived material enters public output.

### Requirement: Eight-operation custody and separate reference authority
The consumer SHALL use the shared owner across eight actual operations/all56 directed pairs, preserve other originals/drafts and keep saved-file observation separate from reference/config history, effective authentication and runtime. Source basis: seven delivered Manager consumers, producer/ref contracts and current ownership.

#### Scenario: Peer, reference or Config changes
- **WHEN** another lane owns I/O, an old targeted cancel races a new owner or reference/config changes make a file original stale
- **THEN** Busy sends no hook/cancel/I/O, token/generation isolation and synchronous peer erasure hold, unknown originals are retained without following a new target or settling/retrying a prior file/reference invocation.

#### Scenario: Attributed qualified paired delivery
- **WHEN** this consumer is proposed for delivery
- **THEN** original synthetic producer evidence/failures keep their identities, meaningful new both-host/privacy/lifetime and required both-OS source/retained checks plus independent reviews precede own canonical/manual sync/archive and final Docs-first delivery, with actual publication and broad REM42/MVP separately observed.
