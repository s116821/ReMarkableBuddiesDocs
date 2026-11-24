## ADDED Requirements

### Requirement: Capacities evidence remains scoped within the export association ledger

The Ledger SHALL key Capacities export records by provider, verified space, conversation and the separately retained portable correlation. It SHALL preserve legacy export encodings and record keys. It SHALL retain the immutable source scope, destination structure and per-attempt operation and payload identity, distinguish a returned candidate from a verified native ID, reject candidate replacement and prohibit promotion of an uncertain dispatch to no-send.

#### Scenario: The same source has historical Mem evidence

- **WHEN** the same portable correlation is prepared for Capacities and has Mem history
- **THEN** the Capacities association is distinct and legacy native IDs and attempts retain their original meaning.

#### Scenario: Interrupted verification after a create

- **WHEN** a create has recorded a candidate before verification and the process restarts
- **THEN** the Ledger can reopen that attempt for readback without granting another create or replacing the candidate.
