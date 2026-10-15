## ADDED Requirements

### Requirement: Composed selected memory publication
Compatible selected subject memory and selected Reader draft publication SHALL use
one canonical ordered admission set, preserving original payload/token/raw-head
and budget seals. The writer SHALL NOT reacquire an already-held participating
gate. Unsupported or foreign providers SHALL refuse before model/publication.

#### Scenario: Memory and Reader share a document key
- **WHEN** the same selected document scope participates in both the memory view and Reader draft
- **THEN** its gate is held once with the complete ordered set, both inputs are revalidated, and the guarded draft publishes without duplicate gate acquisition or new native authority.

### Requirement: Development transport ownership
The source-only development capture transport SHALL exist only for explicit tests
and the opt-in retained-store harness. Normal selected backend operation SHALL
continue to refuse acquisition/request/effects without a qualified producer, and
needed native admission/dispatch interfaces SHALL remain intact and unqualified.

#### Scenario: Normal executable has no development transport
- **WHEN** the normal non-test selected backend is initialized
- **THEN** it refuses as before, without compiling a fixture producer or claiming an installed development/native acquisition path.

### Requirement: Selected request and draft publication
Actual selected Reader interpretation and Generated drafts SHALL publish through
canonical selected admission and Store.commit_selected, using exact acknowledged
root/user references and preserved source evidence. Historical retries SHALL
recover original acknowledgment without minting live authority; failed selected
publication SHALL NOT fall through to ordinary Ledger writes or later effects.

#### Scenario: Draft acknowledgment lost before retry
- **WHEN** the same stable operation and original input are retried after an acknowledged selected draft publication
- **THEN** original receipt/pins recover before stale current-head checks, one chronological draft exists, and no native context or effect is reconstructed.

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
