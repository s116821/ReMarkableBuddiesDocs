# Optional local and selected subject memory

## Purpose

Provide bounded optional associative context to ordinary and selected Reader/Writer
receivers using the existing Store, with explicit ownership, historical recovery
and evidence limits. Remote sync/restore and native qualification remain separate.

## Requirements

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
The local and selected receiving memory domain SHALL reuse the existing generic Store and selected-closure/admission primitives and coordinate stable logical scopes with the shared sync contract, without creating a second sync/export/restore engine. A document conflict SHALL NOT discard unrelated global or document facts. Writer use SHALL be optional. Simulated/protocol, live-provider and real-device evidence SHALL be distinguished. Host receiving and historical recovery SHALL NOT imply remote shared/isolated synchronization, selected restore activation, replacement-device recovery or native acceptance; undelivered broader capabilities SHALL remain explicitly unqualified.

#### Scenario: Local proof before cross-device qualification
- **WHEN** local/protocol memory checks pass but shared/isolated selected membership or clean-device recovery has not been verified
- **THEN** the result SHALL describe only the observed local/protocol capability and SHALL NOT declare the whole memory feature complete.

### Requirement: Selected memory membership and consumption
An explicitly selected memory Provider SHALL discover current facts only through a validated typed append-only catalog and complete Store-created selected closures. Document facts SHALL share the stable source-document aggregate; global Fact chains SHALL remain independent. Registrations SHALL preserve exact immutable owner/genesis identity. Unknown or ambiguous mixed-domain ownership SHALL refuse rather than become empty or usable partial memory. One cumulative budget SHALL bound all historical metadata/media validation before excess I/O. Ordinary heads and retained records SHALL NOT supply current membership.

#### Scenario: Losing registration adoption
- **WHEN** another registration wins for the same aggregate key
- **THEN** adoption SHALL validate the accepted identical owner/genesis and acknowledge current membership separately from original replay, without republishing a losing fact payload.

#### Scenario: Selected answer admission
- **WHEN** the Reader is explicitly supplied a selected Provider and its verified question retrieves a selected view
- **THEN** the Reader SHALL check the sealed payload and current Store tokens before sending the selected context to the answer model. This check SHALL preserve the one consuming admission for journal publication. Ordinary startup SHALL continue to use its existing local Provider when enabled.

#### Scenario: Replacement before answer publication
- **WHEN** a catalog or queried aggregate changes after retrieval or model response and before the consuming Ledger write
- **THEN** shared admission SHALL revalidate all participating Store-issued tokens at that actual write boundary and refuse the stale answer without a generated assistant draft or native authority.

#### Scenario: Cumulative read exhaustion
- **WHEN** catalog, aggregate, retained/history or media verification would exceed the shared read budget
- **THEN** reading SHALL refuse before the excess read/hash and report unavailable rather than a truncated authoritative view.

### Requirement: Optional ordinary Writer memory snapshot
The explicitly enabled ordinary Writer enrichment path SHALL retrieve bounded local associative context using the existing Provider and the same Store, separately from exact source/history/current-request and personalization data. Current request, current source and fixed task/source-safety instructions SHALL take precedence. The context SHALL grant no actions or permission and SHALL be labeled an author-asserted retrieval snapshot, without a claim of atomic local-memory freshness across model I/O. Actual publication SHALL retain fresh Writer preparation, same-Store ownership and finish_writer CAS.

#### Scenario: Disabled and empty Writer context
- **WHEN** ordinary Writer memory is absent, disabled or returns a valid empty view
- **THEN** existing model parts and outcomes are preserved; disabled memory performs no memory read and deliberate PrepareExport remains memory/model/destination-free.

#### Scenario: Bounded context and receiving failure
- **WHEN** the enabled receiver retrieves usable local facts or cannot admit/retrieve/encode them within the existing query and context bounds
- **THEN** usable facts appear once as labeled separate data, while unsupported configuration, unavailable or unusable Partial context and excess bounds refuse before model dispatch without silent fallback; fresh failure, cancellation, stale ownership and replay retain truthful Ledger outcomes.

#### Scenario: Selected Writer remains separately admitted
- **WHEN** the new ordinary enrichment path is given selected configuration, a selected view or a foreign/unsupported provider
- **THEN** it refuses before model use and never interprets selected data as ordinary all-history context or replaces the required selected consuming publication with an ordinary write.

### Requirement: Explicit selected Writer preparation and joined publication
The selected supplied-text Writer library receiver SHALL require an explicit acknowledged Writer selection independent of memory configuration. Fresh selected preparation SHALL preserve exact request/source/history and admit model work once; historical preparation SHALL NOT admit another model call. Generated publication with enabled selected memory SHALL validate Writer and all catalog/queried-aggregate pins under one ordered same-Store admission set at commit_selected. Empty usable memory SHALL retain its pins. Ordinary snapshot behavior and ordinary-command selected refusal SHALL remain unchanged.

#### Scenario: Reopened selected refinement
- **WHEN** a current selected Writer request refines a generated draft after reopening its Store
- **THEN** preparation SHALL validate exact current root/source/draft references, retain the original source owner and verbatim history, and record the new correction link without ordinary all-history lookup.

#### Scenario: Supplied source logical grouping
- **WHEN** a validated normalized source and its owning turn establish a stable source-document ID
- **THEN** selected ownership MAY use that ID for historical logical document grouping and memory partition validation, but SHALL NOT treat supplied text as current device/page identity or native permission; foreign or ambiguous document ownership SHALL refuse.

#### Scenario: Changed selection or lost acknowledgment
- **WHEN** Writer or memory membership changes before publication, or a preparation/finish acknowledgment is lost
- **THEN** new stale publication SHALL refuse; exact historical receipts SHALL reconcile without a new model permit, duplicate draft, ordinary fallback or fresh native/export capability.

#### Scenario: Memory failure without a usable view
- **WHEN** retrieval fails or cancellation occurs after fresh preparation while the acknowledged Writer selection remains current
- **THEN** only selected Failed/Canceled evidence without generated text or selectable draft MAY publish without unavailable memory pins; stale or uncertain writes SHALL remain refusal/reconciliation.

### Requirement: Explicit selected Writer caller and evidence exchange
The existing conversation operation/input command family SHALL expose bounded explicit Writer inspect/generate/refine/recover operations with typed request identity, original ObjectRefs and explicit selection evidence/raw-head digest. Production SHALL validate saved shared-group/binding/mode without inferring Writer selection from memory or Reader configuration. Neither live tokens nor private fresh model permits SHALL be serialized. Ordinary selected-memory refusal SHALL remain unchanged.

#### Scenario: Lost report or replaced winner
- **WHEN** an exact request is recovered after preparation/finish/report acknowledgment loss or replacement of current membership
- **THEN** evidence-only historical verification SHALL run before fresh admission and credentials, returning original Historical/HistoricalPending or NotFound without a model/query/new write; conflicting input SHALL refuse.

#### Scenario: Publication changes before response emission
- **WHEN** a fresh draft was acknowledged but membership changes before current handle emission
- **THEN** the bounded report SHALL preserve the original publication as Historical without current handles or fresh action authority, rather than undoing the commit, misreporting it as uncommitted or rerunning its model.

### Requirement: Ordinary caller memory composition
The application SHALL compose enabled ordinary typed Reader follow-ups, routed
Writer Generate/Refine and notebook reduction with the configured local Provider
on the exact receiving Ledger Store. Disabled memory SHALL construct no memory
provider and perform no memory query/write/network dependency. Selected memory
configuration or foreign admission SHALL refuse without ordinary fallback.
Existing captured Reader and standalone supplied-text Writer behavior SHALL be
preserved. Source traceability: main.rs, workflow/conversation_dispatch.rs,
conversation/receiving/answer.rs and writer/mod.rs at the design baseline.

#### Scenario: Same enabled provider across ordinary receivers
- **WHEN** an admitted ordinary conversation switches Reader, Writer Generate/Refine and back to Reader with memory enabled
- **THEN** the actual receiving paths SHALL query the configured profile on that same Store, preserve original request/history/source/image associations and retain generated draft identity.

#### Scenario: Disabled or valid empty context
- **WHEN** memory is disabled or an enabled query returns a valid CompleteEmpty view
- **THEN** existing model parts and outcomes SHALL remain unchanged, and disabled memory SHALL perform zero memory queries or provider construction.

#### Scenario: Unsupported selection or foreign Store
- **WHEN** ordinary memory receives selected configuration, a selected result or a provider/lifetime from another Store
- **THEN** admission SHALL refuse before the model without treating it as empty memory or changing the operation's scope.

### Requirement: Already-ready local memory lifetime
Local memory used by ordinary receiving SHALL retain the existing same-Store
ordinary mode/local-domain lifetime through its final consumer. It SHALL support
an already-ready ordinary generation 4 Store while preserving existing legacy
constructor, publisher and sync-lease restrictions. Admission SHALL NOT create,
prepare, upgrade or repair a Store or activate selected/remote synchronization.
Source traceability: mode_maintenance.rs, memory/mod.rs and storage/maintenance.rs.

#### Scenario: Provider outlives dispatcher
- **WHEN** the dispatcher is dropped while its captured Reader still owns the admitted local Provider
- **THEN** the existing ordinary mode and local-domain exclusion SHALL remain held until the last provider/lifetime consumer is released.

#### Scenario: Invalid notebook readiness
- **WHEN** enabled notebook memory encounters missing or incomplete readiness, selected history, nonordinary mode or incompatible publisher custody
- **THEN** admission SHALL refuse without changing CURRENT, markers, capabilities or generation format and without constructing a model or destination.

#### Scenario: Legacy admission remains bounded
- **WHEN** an existing legacy caller requests legacy_sync_lease or LocalMemory::new_local on generation 4
- **THEN** its prior refusal SHALL remain unchanged; ordinary memory support SHALL use its separately admitted local lifetime.

### Requirement: Bounded separate ordinary memory snapshots
New ordinary receiving composition SHALL validate the configured profile,
original document/global scope, provenance, expiry, diagnostics and existing
query/context bounds before model dispatch. It SHALL preserve exact request,
history and source data and label usable memory once as author-asserted contextual
data. It SHALL NOT grant effects or claim atomic freshness across model I/O.
Enabled requests exceeding the existing 2048-byte query bound SHALL refuse
without truncation; disabled receivers SHALL retain their existing request bounds.
Source traceability: memory/receiving.rs, writer/subject_memory.rs and
conversation/receiving/memory.rs.

#### Scenario: Original source scope on refinement
- **WHEN** a Writer refines an existing draft while another page is viewed
- **THEN** its memory query SHALL use the original validated source document and exact new request, with current Writer root/draft/image ownership preserved.

#### Scenario: Context failure after Reader interpretation
- **WHEN** a typed Reader has persisted an interpreted request but enabled memory is unavailable, malformed, unusably Partial or over budget
- **THEN** no model answer SHALL be generated and only a truthful bounded Failed/Canceled terminal fact MAY be recorded under existing operation/root guards; the receiver SHALL NOT silently omit memory and continue.

#### Scenario: Source evidence outranks associative instructions
- **WHEN** usable memory contradicts current source facts or contains tool/export or transcript-rewrite instructions
- **THEN** it SHALL remain separately labeled contextual data without operation authority, while actual request/history/source parts remain unchanged for independent semantic assessment.

### Requirement: Frozen notebook reducer memory
Fresh ordinary notebook Generate/Refine SHALL query optional memory once from its
original archive document before stage admission, freeze the bounded snapshot and
include usable context only in the existing reducer. Existing map inputs,
coverage, stage/call/deadline limits and source/draft ownership SHALL remain.
Complete reducer memory SHALL be included in prefix/actual input digests and the
existing worst-case reservation before any map dispatch. Exact replay SHALL NOT
query memory or invoke a model. Source traceability: writer/notebook/command.rs,
writer/notebook/payload.rs and writer/notebook/runner.rs.

#### Scenario: Reducer-only bound context
- **WHEN** an enabled notebook generation or refinement has usable local memory
- **THEN** maps SHALL receive no memory part and reduction SHALL receive the single frozen snapshot, with its encoded bytes and identity covered by existing reservation/digests.

#### Scenario: Reservation or retrieval refusal before maps
- **WHEN** enabled notebook memory cannot be retrieved/validated or leaves insufficient reducer capacity
- **THEN** preparation SHALL refuse before any paid map or new selectable draft and SHALL NOT shrink map coverage, enlarge caps or continue without memory.

#### Scenario: Spent notebook operation
- **WHEN** a notebook operation is replayed after memory changes or an acknowledgment is lost
- **THEN** the original historical/reconciliation behavior SHALL apply with zero new memory queries/model calls, without refreshing the spent operation's snapshot or resuming stages.
