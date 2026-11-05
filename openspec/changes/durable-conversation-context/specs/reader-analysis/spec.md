## ADDED Requirements

### Requirement: Durable actual inference evidence
Reader SHALL persist a guarded evidence batch containing the exact overview/details submitted to proposal and independent verification before provider dispatch. It SHALL reuse the prepared bytes, retain REM-9 ownership checks across storage work, and record verified request and actual terminal outcome without changing recognition prompts or mistaking a draft for visible output. Source: REM-37 source-image retention and actual Reader integration.

#### Scenario: Evidence commit fails
- **WHEN** capture succeeds but required evidence cannot be committed
- **THEN** Reader reports the storage failure before model dispatch, navigation, erasure or output, and source bytes remain unchanged.

#### Scenario: One acquisition across both provider passes
- **WHEN** proposal and independent transcription use a prepared evidence batch
- **THEN** both submit the original stored encoded bytes in the same order, without a later detail query, recapture or reencoding; an attempted failed SDK capture never selects the legacy path.

#### Scenario: Output remains unqualified
- **WHEN** a generated answer lacks a qualified native completion receipt
- **THEN** its draft is committed before output and ReconcileRequired is recorded before navigation, SubmittedUnverified or ambiguous errors stay uncertain, proven unchanged-source/verified-return no-output records a fact-only CAS reconciliation to Failed, and no result is labeled Completed or automatically replayed.

#### Scenario: Terminal recording fails
- **WHEN** an output result cannot be durably recorded
- **THEN** the error includes the recording failure and the last acknowledged Prepared/Generated/ReconcileRequired facts remain for explicit inspection, without invented terminal acknowledgment or repeated effects.

#### Scenario: Verified answer with durable evidence
- **WHEN** the guarded Reader iteration completes native persistence verification
- **THEN** its exact interpreted request, visible response and source-use IDs survive Store reopening, while an uncertain/partial render instead retains an explicit incomplete outcome.
