## ADDED Requirements

### Requirement: Logical Store owner releases its exclusive lease
Dropping a Store owner SHALL explicitly release its private operating-system lease so a duplicate Unix descriptor inherited before exec cannot extend that owner's lifetime. A live replacement Store SHALL retain exclusive ownership even when the old duplicate closes. Acquisition SHALL continue to refuse a second live owner without retries or status-based permission.

#### Scenario: Old descriptor outlives owner
- **WHEN** an old Store's private file descriptor is duplicated and that Store is dropped
- **THEN** another Store can acquire the lease while the old duplicate remains open

#### Scenario: Replacement remains exclusive
- **WHEN** a replacement Store owns the lease and the old inherited descriptor closes
- **THEN** a second Store still refuses until the replacement owner is dropped, after which a new owner can acquire it
