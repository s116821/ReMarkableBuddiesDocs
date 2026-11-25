## ADDED Requirements

### Requirement: Target-specific note scope and About
Writer SHALL retain a logical document-plus-stable-target scope distinct from page/notebook, exact regional source revision and escaped About in its prepared/exported body. Later Refine/Export SHALL reuse existing deliberate identities/recovery and backend correlation; retarget SHALL not update an unrelated target note.

#### Scenario: Two targets in one document
- **WHEN** two distinct targets are generated and one later refined/exported
- **THEN** their note correlations remain independent and original unknown effects are not retried.
