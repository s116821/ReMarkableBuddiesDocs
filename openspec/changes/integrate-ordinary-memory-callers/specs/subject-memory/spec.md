## ADDED Requirements

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
Source traceability: memory/receiving.rs (planned), writer/subject_memory.rs and
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
