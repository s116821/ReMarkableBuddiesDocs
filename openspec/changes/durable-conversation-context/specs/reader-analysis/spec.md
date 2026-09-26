## ADDED Requirements

### Requirement: Durable actual inference evidence
Reader SHALL persist a guarded evidence batch containing the exact overview/details submitted to proposal and independent verification before provider dispatch. It SHALL reuse the prepared bytes, retain REM-9 ownership checks across storage work, and record verified request and actual terminal outcome without changing recognition prompts or mistaking a draft for visible output. Source: REM-37 source-image retention and actual Reader integration.

#### Scenario: Evidence commit fails
- **WHEN** capture succeeds but required evidence cannot be committed
- **THEN** Reader reports the storage failure before model dispatch, navigation, erasure or output, and source bytes remain unchanged.

#### Scenario: Verified answer with durable evidence
- **WHEN** the guarded Reader iteration completes native persistence verification
- **THEN** its exact interpreted request, visible response and source-use IDs survive Store reopening, while an uncertain/partial render instead retains an explicit incomplete outcome.
