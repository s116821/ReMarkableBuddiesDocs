## MODIFIED Requirements

### Requirement: Safe visible activity
Normal Reader SHALL retire source-page visual feedback: no staged triangles, circles, spokes, failure X/segments, status erasure or tool-style leases. Provider progress callbacks SHALL be non-mutating and preserve input/cancellation failure propagation without cadence waits. New visible Buddy-page feedback remains a separate REM40 deliverable; diagnostic-only events SHALL NOT be presented as visible user feedback.

#### Scenario: Pending or completed model work
- **WHEN** proposal or independent verification is pending, finishes, or fails
- **THEN** the source page receives no feedback input and no status cadence delay; exact question/answer and cancellation policies remain unchanged.

#### Scenario: Existing corner ink
- **WHEN** the former status region is occupied or its tool/layout is unknown
- **THEN** its content and settings remain untouched and retirement adds no new eligibility restriction on Q&A.

## REMOVED Requirements

### Requirement: Owned-mark cleanup
**Reason**: September26 retires normal source-page feedback ink and its active lease/cleanup machinery.
**Migration**: No replacement source strokes. Preserve unresolved records with read-only startup refusal. Historical implementation/evidence remains available; Buddy-page feedback belongs to REM40.

### Requirement: Scoped readable native status style
**Reason**: September26 retires normal source-page feedback ink and its active lease/cleanup machinery.
**Migration**: No replacement source strokes. Preserve unresolved records with read-only startup refusal. Historical implementation/evidence remains available; Buddy-page feedback belongs to REM40.
