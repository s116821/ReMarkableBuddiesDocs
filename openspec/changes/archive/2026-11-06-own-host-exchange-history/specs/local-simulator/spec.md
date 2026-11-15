## ADDED Requirements

### Requirement: Unified history ownership fixture

The maintained simulator SHALL exercise the production exchange ownership controller against actual local Ledger history and a modeled page owner.

#### Scenario: Preserve edits and exported records

- **WHEN** the simulator performs reversible actions and injects ownership loss or uncertain effects
- **THEN** it verifies exact presentation readback, stale-action suppression and unchanged durable transcript, source and export facts.
