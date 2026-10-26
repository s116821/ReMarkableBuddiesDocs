## ADDED Requirements

### Requirement: Explicit transcription consumes only selected confirmed examples
The component SHALL offer a provider-independent explicitly invoked transcription operation over one admitted target PNG and optional exact profile/correction/revision references. It SHALL validate every selected example through one bounded owned local snapshot, requiring a single active supported current head, retained causal identity and available verified sample. Invalid/stale/conflicted/deleted/incomplete context SHALL refuse before provider invocation without selecting another revision/profile or silently falling back to no context. Null context SHALL avoid opening the Store. No transcription SHALL stage or commit a confirmation.

#### Scenario: Selected current examples
- **WHEN** a caller selects up to three distinct current confirmed correction revisions and a valid target
- **THEN** only their exact retained text/image data is admitted in requested order with captured revision/sample provenance, without profile-wide retrieval or mutation.

#### Scenario: Stale or unusable context
- **WHEN** any requested example is stale, conflicted, tombstoned, unsupported, missing/corrupt or outside the requested profile
- **THEN** the entire operation refuses before provider invocation and does not claim complete usable context or substitute another example.

### Requirement: Bounded model invocation preserves unconfirmed results
The operation SHALL use a fixed transcription-only instruction, distinctly labeled example data and target-last ordering through the existing progress-aware engine. It SHALL enforce the exact versioned input/reply/report contract and resource bounds in the change contract. Exactly one provider invocation SHALL be attempted with no automatic retry/fallback. Only the existing strict page reply SHALL be accepted, distinguishing normalized text/blank from unreadability; all proposed text SHALL remain unconfirmed and distinct from learned state or improved-recognition evidence.

#### Scenario: Strict normalization or unreadability
- **WHEN** the engine returns an exact bounded valid result
- **THEN** the report preserves the exact proposed normalized page or explicit unreadability, selected captured provenance and confirmed=false without treating it as an answer or creating a confirmed correction; a schema-valid result remains semantically unverified.

#### Scenario: Provider instructions or malformed response
- **WHEN** source/examples contain instructions or the engine returns prose, wrong fields/types, excessive text or an invalid status/null combination
- **THEN** source instructions remain labeled task data and malformed output refuses without repair, partial salvage, tool action or new confirmation.

### Requirement: Existing notebook identities remain compatible
The operation SHALL extend the existing notebook normalizer, preserving the default normalize prompt/profile/source/result bytes and behavior. With selected context it SHALL distinguish extractor identity using the complete ordered revision/sample/text digest descriptor and include context in the exact prompt digest. Target source identity SHALL remain the existing target-only image-set digest. Example images SHALL NOT become target units or verified notebook/source ownership.

#### Scenario: No-context compatibility and changed examples
- **WHEN** the old normalize API runs without context or a new explicit call changes a selected example revision/order
- **THEN** old no-context identities remain exact, while changed context changes the new extractor/prompt identity without rewriting the target-only source digest or allocating a new persisted schema.

### Requirement: Ownership and attempt facts survive cancellation and output failure
With selected context the ordinary/local-domain ownership SHALL span snapshot capture, provider invocation and actual report output/error/drop, excluding incompatible publishers/modes. The operation SHALL check progress before dispatch and through the real engine request, join owned cancellation work and expose fixed privacy-preserving attempt/failure facts. Called SHALL mean only invocation was entered, not HTTP acceptance. A later explicit invocation SHALL be a new call without a fabricated durable idempotency receipt.

#### Scenario: Cancellation or lost provider outcome
- **WHEN** cancellation occurs before or during the one provider invocation, or its result is unavailable
- **THEN** no automatic retry or mutation occurs, called/not-called facts remain truthful and remote uncertainty is not relabeled rollback or successful recognition.

#### Scenario: Failed report output
- **WHEN** stdout fails after a captured or returned result
- **THEN** actual owned lifetime is retained until completion/error/drop, no second report/call occurs and logs reveal no target/example text/image or credentials.

### Requirement: Recognition qualification remains separate from storage
Delivery SHALL include production-path Store/CLI/payload/cancellation controls and representative bounded new live-model evidence with independent ground truth, comparing no-context and selected-context conditions on identical targets. It SHALL preserve misreadings and degradation and SHALL NOT substitute synthetic storage or scripted replies for recognition/real-pen/native evidence. Automatic Reader/Writer hooks, training, selected sync and whole-feature efficacy SHALL remain separately qualified.

#### Scenario: Representative live comparison
- **WHEN** connected cursive, technical shorthand, ambiguous writing and misleading examples are evaluated
- **THEN** baseline/context outcomes and stable expected facts/refusals are recorded without success fishing, easier fixture replacement or a generalized accuracy/training claim.
