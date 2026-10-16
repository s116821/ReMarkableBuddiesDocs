## ADDED Requirements

### Requirement: Quiet automatic connection refresh
The shared Manager connection UI SHALL retain the last successfully verified status, details and original verification timestamp while an automatic observation is pending, without a new checking label, spinner or pending announcement. Initial and explicit user-requested reads SHALL retain visible pending feedback. Only a successful result SHALL advance the verification timestamp. Actual failed observation, connection/boot identity change, cancellation or disconnect SHALL still clear current details and prevent late-result restoration; existing explicit-reconnection and transport safeguards SHALL remain.

#### Scenario: Automatic observation pending and successful
- **WHEN** a previously observed connection starts a scheduled read
- **THEN** its last verified status, details and timestamp remain visible without a pending-state update, and a successful same-identity result replaces them with the newly verified sample.

#### Scenario: Explicit read
- **WHEN** the user starts an initial or manual connection read
- **THEN** the UI shows pending feedback until that request resolves.

#### Scenario: Failure or cancellation during automatic read
- **WHEN** a pending automatic read fails, observes a changed identity or is cancelled by disconnect
- **THEN** the UI clears current details according to the existing failure/cancellation contract and a late response cannot restore them or silently reconnect.
