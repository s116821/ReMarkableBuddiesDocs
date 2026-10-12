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

#### Scenario: Failure after verified interpretation
- **WHEN** optional enrichment fails after the exact verified user question was persisted as Interpreted
- **THEN** the ledger SHALL permit only an explicit failure/cancellation fact with unchanged interpreted text and appropriate reason, SHALL preserve the verified question, and SHALL NOT create a generated or completed assistant answer.

### Requirement: Honest shared-domain delivery
Memory SHALL reuse existing generic sync/export/restore and coordinate stable logical scopes with REM-52. A document conflict SHALL NOT discard unrelated global or document facts. Writer use SHALL be optional. Simulated/protocol, live-provider and real-device evidence SHALL be distinguished, and incomplete Manager, Writer, cross-device or native gates SHALL remain open.

#### Scenario: Local proof before cross-device qualification
- **WHEN** local/protocol memory checks pass but shared/isolated selected membership or clean-device recovery has not been verified
- **THEN** the result SHALL describe only the observed local/protocol capability and SHALL NOT declare the whole memory feature complete.

### Requirement: Selected memory membership and consumption
An explicitly selected memory Provider SHALL discover current facts only through a validated typed append-only catalog and complete Store-created selected closures. Document facts SHALL share the stable source-document aggregate; global Fact chains SHALL remain independent. Registrations SHALL preserve exact immutable owner/genesis identity. Unknown or ambiguous mixed-domain ownership SHALL refuse rather than become empty or usable partial memory. One cumulative budget SHALL bound all historical metadata/media validation before excess I/O. Ordinary heads and retained records SHALL NOT supply current membership.

#### Scenario: Losing registration adoption
- **WHEN** another registration wins for the same aggregate key
- **THEN** adoption SHALL validate the accepted identical owner/genesis and acknowledge current membership separately from original replay, without republishing a losing fact payload.

#### Scenario: Replacement before answer publication
- **WHEN** a catalog or queried aggregate changes after retrieval or model response and before the consuming Ledger write
- **THEN** shared admission SHALL revalidate all participating Store-issued tokens at that actual write boundary and refuse the stale answer without a generated assistant draft or native authority.

#### Scenario: Cumulative read exhaustion
- **WHEN** catalog, aggregate, retained/history or media verification would exceed the shared read budget
- **THEN** reading SHALL refuse before the excess read/hash and report unavailable rather than a truncated authoritative view.
