## ADDED Requirements

### Requirement: Explicit ordinary notebook archive maintenance
The archive command SHALL provide explicit format-4 notebook export and
detached inspection operations. Export SHALL admit only a complete existing
ordinary notebook Store under its exclusive lease and validate complete
lineage and required media. The destination and configured owned roots
SHALL be canonically disjoint. Inspection SHALL require the explicit
complete notebook format, with bounded work and no runtime activation.

#### Scenario: Export and detached readback
- **WHEN** an admitted existing notebook Store is exported to a new directory under a trusted local parent
- **THEN** publication verifies complete original objects, publishes a no-replace marker last and verifies the committed archive before reporting success.

#### Scenario: Refused custody or incomplete archive
- **WHEN** custody, path separation, format, bounds, required media or the detached inventory witness fail
- **THEN** the operation refuses without falling back to a legacy route, overwriting an archive or granting restore or runtime authority.
