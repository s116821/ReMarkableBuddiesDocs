## ADDED Requirements

### Requirement: Shared ordinary local dispatch
The ordinary local application SHALL route through a shared coordinator using the existing module settings and Ledger. The coordinator SHALL preserve exact request and eligible history, route only admitted intents, and retain one active operation. It SHALL exclude background nonlocal activation from this path.

#### Scenario: Switch receiving buddies
- **WHEN** a request is admitted to a different enabled buddy in the current conversation
- **THEN** the receiver gets the unchanged request and ordered Ledger history, with bounded verified associated media and separate preset and personalization content.

#### Scenario: Refuse unresolved intent
- **WHEN** the module, page authority, required media or requested capability is unavailable, or export intent is ambiguous
- **THEN** dispatch refuses or requests clarification without a destination effect.

### Requirement: Guarded operation effects
The coordinator SHALL preserve release and invalidation semantics, reject duplicate and stale operations and revalidate ownership under the effect gate. Blank start SHALL call the admitted page owner with no model call.

#### Scenario: Cancel or replace before effect
- **WHEN** cancellation or a newer admitted revision invalidates an active request before effect dispatch
- **THEN** the old operation cannot render or export.

#### Scenario: Uncertain export settlement
- **WHEN** the existing destination owner cannot verify an attempted effect
- **THEN** reconciliation is required and the coordinator does not repeat dispatch.
