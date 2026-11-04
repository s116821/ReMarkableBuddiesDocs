## ADDED Requirements

### Requirement: Explicit large-input commands retain complete normalized source
The component SHALL offer explicit budgeted notebook generation/refinement and
joined-export paths through the existing Writer entrypoint, retaining complete
canonical supplied normalized text and provenance as required immutable media in
the existing Source domain before model dispatch. The admitted request SHALL bind
the actual resolved content, selection, guidance, request and history. Refinement
SHALL reuse its committed original source instead of rereading an input path.
An explicit history range SHALL reuse the existing exact range contract; omitted
range SHALL retain full eligible history, with no automatic selection or rewriting.
Legacy inline commands SHALL retain their bounds and one-call behavior. No path
SHALL imply original notebook bytes, extraction completeness or native ownership.
File/asset admission SHALL validate a regular local file through a safe opened
handle, reject special files/symlink/reparse traversal and changed bindings,
bound the read and verify declared raw SHA-256 before strict UTF-8/JSON/Index
validation or effects, as pinned in input-admission.md. The frozen observed
buffer SHALL NOT be presented as an atomic concurrent-edit filesystem snapshot.
Paths/handle identities SHALL NOT enter model input, durable source or reports.

#### Scenario: Larger source survives reopen and input-file removal
- **WHEN** an input larger than the inline bound is generated, its original file is removed and the saved draft is later explicitly refined
- **THEN** the complete original normalized units/text/locations/digests remain available through committed source media in the same conversation without rereading, truncating or recapturing them.

#### Scenario: Bad input or missing required credential
- **WHEN** normalized JSON, identities, history, caller allowance, source bounds or required model/destination credentials are invalid
- **THEN** the request refuses before durable admission or model/destination cost, without echoing sensitive input or changing legacy command behavior.

#### Scenario: Special file or raced input
- **WHEN** a path names a FIFO/device/reparse/symlink, changes binding or content during admission, lacks safe handle support, or fails its declared raw hash
- **THEN** admission refuses before Store/model/destination effects without a blocking FIFO open/read, weakened fallback, path leakage or snapshot claim.

### Requirement: Planning covers selected source under declared total bounds
The planner SHALL partition every selected unit in original order into explicit
UTF-8 ranges without gaps or silent relevance filtering. Optional adjacent
context SHALL be labeled separately from authoritative coverage. It SHALL
validate actual encoded payloads, caller allowance and worst-case reduction,
storage and output budgets before starting model work. Source, work and call
limits SHALL remain explicit; a refusal SHALL NOT masquerade as complete notebook
coverage or trigger a smaller/easier source or alternate provider automatically.

#### Scenario: Ordered pages and boundary facts
- **WHEN** selected units include repeated text, Unicode, paragraph boundaries and page/section transitions
- **THEN** the plan preserves original order and exact byte coverage, retains distinct units, and labels any duplicated context without counting it twice.

#### Scenario: Work cannot fit
- **WHEN** selected data exceeds the declared 256 KiB/256-unit, eight-map/nine-call or encoded/storage budget, or the caller permits fewer required calls
- **THEN** planning refuses before the first invocation and preserves complete retained facts rather than silently dropping source.

#### Scenario: Reduction budget
- **WHEN** every planned map returns a valid reply at its maximum encoded bound
- **THEN** all summaries and required fixed context fit the pre-reserved reduction payload; an invalid or oversized reply fails without trimming or starting unplanned calls.

### Requirement: Every model stage has fresh durable invocation authority
Each planned model stage SHALL require this invocation's positively fresh
Ledger preparation bound to exact source/plan/history/predecessor references.
Ordinary receipts and existing Store publication SHALL own this lifecycle, without
a second registry or native admitted-intent reuse. Successful stages SHALL return
private exact post-publication references. Lost acknowledgment, replay, conflict,
cancellation or uncertain model outcome SHALL stop automatic continuation and
SHALL NOT infer another call grant from saved Generated state or claim no cost.
Archive, plan, stage, transition, input and export identities SHALL follow the
exact ordered serialization/domain-separated recipes and literal fixed vectors
in identities.md and identity-vectors.json; old inline recipes SHALL remain exact.

#### Scenario: Lost preparation or result acknowledgment
- **WHEN** a stage commits but its acknowledgment is lost before or after a model response
- **THEN** no next paid stage or export starts from historical state, and replay/reopen of the original operation makes zero additional model/destination calls.

#### Scenario: Changed input reuses an operation
- **WHEN** source, exact request, guidance, history or plan identity changes under the same operation
- **THEN** the receipt comparison refuses changed content instead of reusing earlier summaries or dispatch authority.

#### Scenario: Stable identities across reopen
- **WHEN** the fixed Unicode/null/raw-LF vectors and old inline source/export vectors are evaluated independently and through the implementation across reopen
- **THEN** digests and UUIDs match the literal expected values, and changes in a covered field or input order cannot silently reuse the original content fingerprint.

#### Scenario: Canceled late stage
- **WHEN** cancellation, a deadline or selected-source/history change occurs while a stage is pending
- **THEN** late output cannot authorize a subsequent stage/final draft/export, ownership is released only after joined work ends, and remote cost uncertainty remains explicit.

#### Scenario: No-call recording fails
- **WHEN** zero invocations were observed but deletion/conflict prevents durable no-call recording
- **THEN** the report preserves the storage/refusal result separately from its local observation and grants no replay authority from the failed recording.

### Requirement: Final proposals and exports retain exact lineage and ownership
Only a positively fresh final publication SHALL return the private draft/source/
completed-plan/root selection used by the existing guarded exporter. Actual
Writer/export owners SHALL span the joined stages and destination lifecycle in
the existing fixed order, without a Store mutex over HTTP. Exact required media
and returned revision references SHALL be checked at admission and pre-write
boundaries; output SHALL freeze without refreshing to bless changed content.
Existing stable correlation, no-send persistence and known-ID uncertainty rules
SHALL remain authoritative. Processed coverage SHALL NOT imply semantic accuracy.

#### Scenario: Generate then refine and re-export
- **WHEN** two explicit notebook requests complete across reopen and deliberately export through one correlation
- **THEN** new drafts and stage facts retain the complete original source/history and update the same verified destination identity without rewriting old facts or claiming native completion.

#### Scenario: Deliberate inline-to-archive re-export
- **WHEN** an inline export has confirmed completion and a new explicit archived generation for the same document/selection is deliberately exported through that correlation with new operation/effect identities
- **THEN** the logical scope and verified backend ID remain stable, new export revision uses the archive recipe, old inline bytes/receipts remain unchanged, and old refine does not become multi-call implicitly.

#### Scenario: Final acknowledgment lost or source media changes
- **WHEN** the final draft was saved without fresh observed acknowledgment, or its archive/plan/root changes or required media becomes unavailable before writing
- **THEN** no automatic destination write occurs; a later explicit selected-draft intent must validate current exact lineage, and failed no-send recording stays distinguishable from zero observed writes.

#### Scenario: Earlier external write is uncertain
- **WHEN** an earlier effect may have been sent
- **THEN** known-ID reconciliation remains read-only, a new notebook/model intent cannot bypass unresolved uncertainty, and model work or writes are never automatically restarted.

### Requirement: Source compatibility and maintenance boundaries remain explicit
Known media-backed source and processing records SHALL have exact typed
namespace/version/descriptor/origin validation and complete supported reference
closure. Source1/2 and Conversation1/2 bytes, native meanings and receipt recipes
SHALL remain unchanged. Older or narrow unsupported consumers SHALL preserve or
refuse new data explicitly before mutation/publication rather than silently omit
it. JSON source media SHALL NOT become image/native evidence. Existing narrow
cleanup and native receiving SHALL NOT be broadened implicitly by this increment.
Modes requiring unsupported selected/outbox/receiving consumers SHALL refuse the
new command before cost rather than infer native/sync support from Store opening.

#### Scenario: Supported backup and historical readback
- **WHEN** a notebook archive and its stage history are reopened or fully exported/restored
- **THEN** all required source bytes, plan/stage references, conflicts/tombstones and media counts survive exactly; missing required bytes remain distinct from explicitly omitted imported media.

#### Scenario: Retained source remains referenced
- **WHEN** a conversation is logically deleted or another retained revision still references the archive
- **THEN** reference-safe retention prevents its media from being collected, while a narrow unsupported cleanup reports refusal before mutation.

#### Scenario: Older or native consumer
- **WHEN** an older binary, Source1-oriented cleanup or unsupported native receiving sees relevant new records
- **THEN** it returns an explicit bounded unsupported/refused result without overwrite, publication, false complete coverage or native activation.

### Requirement: Evidence distinguishes model quality from host and native coverage
Maintained host scenarios SHALL execute the production notebook planner/stages/
Ledger/exporter with scripted providers and declared bounded assets. Actual
loopback transport and a separately reviewed original model-quality attempt SHALL
remain distinct evidence. Reader contracts SHALL remain unchanged. This increment
SHALL NOT claim physical extraction, handwriting/drawing recognition, native or
combined Writer routing, live account acceptance or whole Writer/MVP completion.

#### Scenario: Scripted and loopback qualification
- **WHEN** stage faults, bounds, coverage, replay, export uncertainty or compatibility cases are exercised locally
- **THEN** actual source/stage/poll/count artifacts establish those mechanisms without credentials/network in simulation, invented tablet PNGs or a model-quality claim.

#### Scenario: New model-facing quality gate
- **WHEN** the new map/reduction prompts are ready for delivery
- **THEN** an original frozen beyond-inline-bound notebook/refinement plan receives independent bounded preparation and semantic review, retaining raw outcomes and failures without replaying the closed earlier two-call attempt or substituting easier inputs after failure.
