## ADDED Requirements

### Requirement: Optional portable local subject memory
The application SHALL expose replaceable explicit store/update/query/inspect/forget operations using the existing SubjectMemory namespace and generic Store. Records SHALL include independent stable logical identity, explicit portable profile/global/document scope, provenance, confidence basis and expiry. Local operation SHALL require neither subject-memory cloud service nor a particular answering LLM. Memory SHALL remain separate from conversation, document research, handwriting learning and personalization.

#### Scenario: Disabled memory
- **WHEN** Reader or Writer operates with subject memory disabled
- **THEN** it SHALL perform no subject-memory retrieval/write/network dependency and preserve ordinary operation.

#### Scenario: Concurrent correction and forgetting
- **WHEN** a fact has competing current revisions or an explicit forgetting tombstone
- **THEN** retrieval SHALL NOT select a retained ancestor or arbitrary timestamp winner, and unrelated independent facts SHALL remain independent.

### Requirement: Bounded contextual retrieval
Retrieval SHALL use bounded current membership, profile/scope restrictions, relevance and encoded context budgets. It SHALL distinguish stale, conflicting, unsupported and unavailable input. Current explicit/canonical facts SHALL outrank associative memory. Memory SHALL NOT grant effect permissions, rewrite visible transcripts or become source evidence.

#### Scenario: Conflicting or stale memory
- **WHEN** applicable current memory is expired or contains contradictory values for the same claim
- **THEN** the affected claims SHALL be withheld with explicit diagnostics instead of being asserted as current truth.

#### Scenario: Verified Reader enrichment
- **WHEN** an enabled Reader has independently verified a question and retrieved relevant memory
- **THEN** the receiving answer layer SHALL receive bounded labeled associative context separately from the unchanged question and source images, while transcription verification remains free of memory.

### Requirement: Honest shared-domain delivery
Memory SHALL reuse existing generic sync/export/restore and coordinate stable logical scopes with REM-52. A document conflict SHALL NOT discard unrelated global or document facts. Writer use SHALL be optional. Simulated/protocol, live-provider and real-device evidence SHALL be distinguished, and incomplete Manager, Writer, cross-device or native gates SHALL remain open.

#### Scenario: Local proof before cross-device qualification
- **WHEN** local/protocol memory checks pass but shared/isolated selected membership or clean-device recovery has not been verified
- **THEN** the result SHALL describe only the observed local/protocol capability and SHALL NOT declare the whole memory feature complete.
