## ADDED Requirements

### Requirement: Native range effects and durable history settlement

Native exchange Undo/Redo SHALL consume an actual current platform-owned presentation/range capability, conditionally compare the entire before-state, verify operation-correlated completion/readback and preserve all non-owned content. Interrupted or uncertain native effects SHALL be durably reconciled without automatic replay, compensation, stale response resurrection or transfer of historical authority. Actual device ownership/latency and legacy newline/persistence compatibility SHALL be qualified before native completion is claimed. The delivered host controller and modeled fixture alone SHALL NOT satisfy this requirement.

#### Scenario: Current native owned exchange
- **WHEN** actual native input and exact page/session/visit/content/turn ownership authorize a conditional history action
- **THEN** only the eligible newest complete exchange may change after verified completion/readback, preserving composer/focus/header/status, older content, source records and external exports.

#### Scenario: User edit or uncertain native completion
- **WHEN** the native owner changes, a protected/unrelated region is edited or completion/readback is lost or contradictory
- **THEN** eligibility is invalidated and durable reconciliation is required without broad deletion, automatic replay or fabricated success.

#### Scenario: Restart or restored replacement history
- **WHEN** a process restarts or a newer/restored aggregate replaces the prior history
- **THEN** old native grants cannot be recreated from stored bindings or modeled receipts, and interrupted effects cannot resurrect stale content or duplicate an external side effect.
