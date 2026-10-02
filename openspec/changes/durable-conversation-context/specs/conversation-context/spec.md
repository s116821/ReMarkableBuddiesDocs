## ADDED Requirements

### Requirement: Explicit unbound legacy evidence
The domain SHALL keep identity-free legacy acquisition in a separate Buddy-owned LegacyCapture record, selected explicitly before acquisition, with native identity and qualification explicitly absent. It SHALL preserve every exact ordered provider image and any supplied acquisition parent without invented SDK source, affine, crop or viewport facts. Failed, unsupported or unknown SDK acquisition SHALL refuse without downgrade. Legacy schema1 SHALL require explicit absent fields, stable Buddy evidence/conversation/turn IDs, full image integrity and decoding, root CAS, fingerprint retry and reference-aware retention. Bounds SHALL be 1–15 provider images plus at most one parent, 32 MiB encoded per image, 64 MiB encoded total, and existing 8192-axis/32 MiB decoded-image limits.

#### Scenario: Legacy acquisition and historical inspection
- **WHEN** a backend explicitly selects legacy acquisition before capture
- **THEN** exact bytes are committed before provider use in an explicitly unbound conversation, missing parent/identity/qualification stay absent, and inspection/context distinguish them from SDK Capture/SourceObservation without inferring same-page continuity.

#### Scenario: Invalid or incomplete legacy evidence
- **WHEN** schema/required fields, image decoding, role/order, bounds, integrity or committed links are invalid
- **THEN** evidence retrieval/preparation refuses and no dependent provider call occurs; retry reuses acknowledged stored bytes rather than recapturing.

#### Scenario: Legacy history after restart
- **WHEN** a legacy conversation is reopened by its Buddy ID
- **THEN** its facts/images remain inspectable under retention rules, while native source/binding qualification, page revisit and automatic effect replay remain unavailable.

### Requirement: Stable shared chronological conversation
The shared domain SHALL retain versioned conversation and turn IDs, roles, Reader/Writer modes, operation IDs, revisions, states, timestamps and root-CAS-allocated chronological sequences. Corrections SHALL append with stable references. Conflicts SHALL expose all heads without LWW. Source: REM-37 durable history and mixed-Buddy acceptance.

#### Scenario: Restart and mode change
- **WHEN** Reader, Writer and Reader append through the shared API and the Store is reopened
- **THEN** all exact committed turns retain one conversation identity and chronological order, regardless of display order or wall-clock changes.

#### Scenario: Conflicting or repeated operation
- **WHEN** an operation is retried or competing heads exist
- **THEN** an identical committed operation returns its existing result, changed content under its ID or incomplete expected heads returns a conflict, and no duplicate turn is created.

### Requirement: Immutable source evidence for every used image
The domain SHALL persist every actual inference image and useful derived crop before provider use, with content hash, exact bytes, dimensions, MIME, parent/crop transform, document/page/revision/capture/viewport identity, normalized coordinates, purpose and turn links. It SHALL preserve earlier evidence when later turns use new targets. Source: REM-37 source provenance clarification and REM-4 dependency.

#### Scenario: Two targets in one conversation
- **WHEN** successive turns use different source pages and crops
- **THEN** both Buddy modes can retrieve each exact original image by its turn and hash with the corresponding target coordinates, and no old image is replaced by recapture.

#### Scenario: Failed or missing media
- **WHEN** required evidence cannot be committed or a selected-record restore explicitly declares media unavailable
- **THEN** provider dispatch that depends on it does not run, missing evidence is identified explicitly, and committed available text/facts remain inspectable.

#### Scenario: Unexpected required-media corruption during recovery
- **WHEN** Store recovery skips a commit whose required media is absent or corrupt
- **THEN** the domain reports typed IncompleteStore and refuses inspection and mutation rather than presenting an older root as complete; the refusal is conservatively store-wide because skipped commits cannot reliably be attributed to a conversation.

#### Scenario: Restored derivative geometry is inconsistent
- **WHEN** a restored derivative's individually valid affine or valid-source region differs from its declared parent/crop/output composition, or its derivation procedure is unsupported
- **THEN** historical SDK evidence is refused using the SDK-owned geometry semantics, exact descriptor-bit comparison preserves signed zero, and neither source-plane roundoff nor valid image hashes waive the structural mismatch.

#### Scenario: Historical capture facts cannot substitute for a live guard
- **WHEN** capture evidence is exported by the SDK, persisted, imported or restored
- **THEN** the domain retains the original bounded versioned SDK historical facts and exact parent/derivative bytes, does not fabricate missing scope or render provenance, and requires a separate fresh qualified guard before native use.

#### Scenario: Required capture facts are unavailable
- **WHEN** the SDK cannot export a required capture fact or its representation cannot be stored without loss
- **THEN** image-dependent provider dispatch is refused before calls or mutations, with the missing evidence reported explicitly rather than inferred from identifiers, timestamps or hashes.

### Requirement: Explicit outcomes without replay
The ledger SHALL distinguish prepared interpretation, verified request, generated draft, completed visible response, failure, cancellation and uncertain output. Hidden presets and machine instructions SHALL remain outside visible history. Interrupted operations SHALL require reconciliation rather than automatically replay provider/native/export effects. Source: REM-37 interrupted-write acceptance and REM-9 ownership guards.

#### Scenario: Crash across native output acknowledgment
- **WHEN** native output may have happened but its complete ledger acknowledgment is missing
- **THEN** restart retains the operation/evidence as uncertain, does not claim a completed visible answer and does not type or invoke the provider again automatically.

### Requirement: Qualified page binding with full-head CAS
The domain SHALL atomically associate a conversation and deterministic document/Buddy-page logical binding record using complete expected heads and REM-25's exact NativeCommitted receipt. Its versioned key SHALL remain stable across reinstall/restore; current-device qualification SHALL remain a separate requirement. Initial acquisition SHALL be create-or-identical for both page claim and conversation binding. Intended and observed target IDs SHALL remain distinct until qualified, and a mismatch after accepting a caller-assigned intended UUID SHALL require reconciliation. The REM-25 device-local journal SHALL remain the sole native operation journal. Source: REM-25 acquisition interface and REM-37 binding acceptance.

#### Scenario: Lost acknowledgment or competing binding
- **WHEN** a qualified binding receipt is retried or another conversation claims the same Buddy page
- **THEN** the identical committed association is returned once, while a conflicting association is refused and reconciled without repeating page insertion.

#### Scenario: Retry after later append or deletion
- **WHEN** the exact operation and immutable receipt fingerprint are retried with stale original heads after later appends or deletion
- **THEN** historical acknowledgment is found before ordinary CAS validation, current state is reported separately, and a deleted/conflicted binding is not restored or authorized for native use.

#### Scenario: Competing target or reinstalled actor
- **WHEN** one conversation concurrently claims different pages, or an installation actor changes after restore
- **THEN** only one initial page claim succeeds, the logical document/page key remains identical across actor changes, and current-device receipt qualification is still required.

#### Scenario: Legacy header and restored association
- **WHEN** only a legacy header match or imported association is available
- **THEN** it does not authorize native reuse; verified identity and current device ownership are required, and no OCR import or native edit occurs automatically.

### Requirement: Exact context with explicit limits
Context assembly SHALL preserve canonical chronology and exact visible turn text, return its included turn/media identities, and report exceeded or unknown requested bounds explicitly. It SHALL NOT silently truncate, summarize or rewrite the ledger, and SHALL keep storage-byte limits distinct from provider-token budgets. Source: REM-37 context limits and later REM-38/39 consumers.

#### Scenario: Context exceeds caller budget
- **WHEN** the requested history cannot fit the explicit adapter budget
- **THEN** assembly returns an explicit-choice-needed result with the full ledger unchanged, allowing an explicit range or separate conversation without pretending all history was included.

### Requirement: Portable lightweight export association
Export association SHALL use a stable correlation UUID in supported metadata or a preserved title marker, alongside native-note identity, scope, revision and operation outcome in existing shared storage. An uncertain retry SHALL reconcile the exact marker before any new export; no separate registry service is required. Source: REM-37 September 26 export-correlation comment and REM-23.

#### Scenario: Export outcome is unknown
- **WHEN** marker discovery returns one, multiple or no verified matches after an uncertain write
- **THEN** one exact match can be associated, multiple matches produce conflict, and no match remains uncertain without blindly duplicating the note.

### Requirement: Inspectable deletion and legacy coexistence
The domain SHALL support exact inspection/export and explicit full-head logical deletion by atomically tombstoning the root and current binding. Ordinary lookup/context/append SHALL enforce root liveness; retained descendants SHALL remain available only through explicit retained-history inspection and SHALL NOT revive a deleted conversation. Media retained by live/conflicted records or retained revisions SHALL remain intact; current logical deletion SHALL disclose retained bytes rather than claim physical erasure. Oversized/conflicting atomic operations SHALL fail without partial deletion. Legacy documents and external notes SHALL remain untouched. Source: REM-37 inspection/delete/legacy acceptance and REM-42 retention dependency.

#### Scenario: Shared evidence and deletion
- **WHEN** one conversation is deleted while another or a retained revision references its image
- **THEN** the deleted conversation is tombstoned, the shared image remains retrievable for its surviving reference and no native document is changed.
