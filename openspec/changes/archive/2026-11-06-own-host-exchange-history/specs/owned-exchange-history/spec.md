## ADDED Requirements

### Requirement: Live exchange history ownership

The unified history controller SHALL identify one latest complete exchange from the original Ledger and newest-first projection. It SHALL require a fresh live owner receipt and matching conversation, turn, page, visit, session and content facts before a reversible effect.

#### Scenario: Verified undo and redo

- **WHEN** the same live owner applies and verifies an eligible history action
- **THEN** only the owned exchange is removed or restored and all unrelated presentation, transcript, source and export facts are preserved.

#### Scenario: Stale ownership and uncertain effects

- **WHEN** protected content, page ownership, Ledger heads or the effect receipt changes or becomes unavailable
- **THEN** the controller refuses the action or reports reconciliation required, and cannot replay the previous effect.

#### Scenario: Restored history

- **WHEN** persisted history is reopened or a newer revision replaces it
- **THEN** historical records remain readable and supply no live undo or redo grant.

#### Scenario: Blank Start retires history ownership

- **WHEN** Blank Start begins after an exchange is armed or after its Undo
- **THEN** both old Undo and Redo eligibility are discarded without a backend edit, transcript change, or recreation of an old ownership grant.
