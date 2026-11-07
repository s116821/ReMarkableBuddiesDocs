## ADDED Requirements

### Requirement: Explicit transcription consumes only selected confirmed examples
The component SHALL offer a provider-independent explicitly invoked transcription operation over one admitted target PNG and optional exact profile/correction/revision references. It SHALL validate every selected example through one bounded owned local snapshot, requiring a single active supported current head, retained causal identity and available verified sample. Invalid/stale/conflicted/deleted/incomplete context SHALL refuse before provider invocation without selecting another revision/profile or silently falling back to no context. Null context SHALL avoid opening the Store. Every selected example SHALL additionally pass existing notebook static PNG complete framing/CRC/IEND checks, excluding APNG and trailing bytes within unchanged correction decode bounds. An otherwise valid retained sample that is ineligible for this consumer SHALL refuse as context-unavailable with null context before invocation; it SHALL NOT be rewritten or reclassified as invalid storage. No transcription SHALL stage or commit a confirmation.

#### Scenario: Selected current examples
- **WHEN** a caller selects up to three distinct current confirmed correction revisions and a valid target
- **THEN** only their exact retained text/image data is admitted in requested order with captured revision/sample provenance, without profile-wide retrieval or mutation.

#### Scenario: Stale or unusable context
- **WHEN** any requested example is stale, conflicted, tombstoned, unsupported, missing/corrupt or outside the requested profile
- **THEN** the entire operation refuses before provider invocation and does not claim complete usable context or substitute another example.

### Requirement: Bounded model invocation preserves unconfirmed results
The operation SHALL use a fixed transcription-only instruction, distinctly labeled example data and target-last ordering through the existing progress-aware engine. It SHALL enforce the exact versioned input/reply/report contract and resource bounds in the change contract. Exactly one provider invocation SHALL be attempted with no automatic retry/fallback. V1 SHALL accept only the existing strict page reply, distinguishing normalized text/blank from unreadability; all proposed text SHALL remain unconfirmed and distinct from learned state or improved-recognition evidence.

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
- **THEN** the WholePage instruction SHALL describe the effective per-page text, aggregate text and full response byte limits. The revised prompt and extractor identities identify that instruction while Profile protocols 1 and 2, target-only source digest and persisted schemas retain their existing contracts. Changed captured identities change the extractor identity. A revision-only change SHALL change extractor/profile identity while preserving an unchanged payload prompt digest; sample/text/order changes SHALL change prompt identity only when serialized payload bytes change.

### Requirement: Ownership and attempt facts survive cancellation and output failure
With selected context the ordinary/local-domain ownership SHALL span snapshot capture, provider invocation and actual report output/error/drop, excluding incompatible publishers/modes. The operation SHALL check progress before dispatch and after return, pass cooperative progress through the engine request and expose fixed privacy-preserving attempt/failure facts. Arbitrary engines SHALL remain explicitly cooperative; the default single pre-execute callback SHALL NOT be described as mid-call preemption or joined work. The configured OpenAI transport SHALL retain its existing repeated progress and owned-worker cancellation/joining without a wrapper worker. Called SHALL mean only invocation was entered, not HTTP acceptance. A later explicit invocation SHALL be a new call without a fabricated durable idempotency receipt.

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

### Requirement: Explicit versioned partial transcription preserves uncertainty

The proposed v2 operation SHALL require the exact version and policy pair,
use separate pinned v2 prompt and identity bytes, and enforce the strict
admission and outcome matrix in the v2 review contract. The default notebook
normalizer and explicit v1 request, report, prompt and profile bytes SHALL
remain compatible. The explicit admitted-page limit SHALL remain 4096 UTF-8
bytes. The operation SHALL continue rejecting duplicate JSON fields before
version routing.

#### Scenario: Admitted partial reply
- **WHEN** an explicitly opted-in v2 call returns a strict partial response with both bounded known and uncertain spans
- **THEN** the operation SHALL return a distinct unconfirmed partial result with the exact span order and null normalized result. No automatic source, index, export, or confirmation path SHALL consume the partial result.

#### Scenario: Malformed opt-in or malformed provider reply
- **WHEN** an input cannot admit the v2 version/policy pair or a called engine returns a malformed v2 variant
- **THEN** the operation SHALL refuse at the respective boundary, keep the applicable versioned envelope and attempt facts, and preserve no partial or normalized result.

### Requirement: Mathematical layout is an explicit inert-text policy

The v2 envelope SHALL additionally accept the exact explicit policy
`partial-math-transcription`. It SHALL reuse the existing partial response schema
and parser with the general layout addendum and distinct prompt/profile identities
specified in the math layout contract. Default, v1 and original v2 policy bytes
SHALL remain unchanged. Mathematical notation SHALL remain unverified inert
string content, without rendering, execution, repair, automatic confirmation or
cross-uncertainty concatenation. All existing custody, limits and invocation rules
SHALL remain applicable.

#### Scenario: Explicit mathematical layout
- **WHEN** a caller selects the math policy in a valid v2 request
- **THEN** the prompt requests grouped mathematical notation through one additional fixed instruction part, retains target-last context isolation, and identifies the new profile without changing target-only source identity or the output schema.

#### Scenario: Unknown mathematical attachment
- **WHEN** a glyph or attachment cannot be encoded as an independently complete known fragment
- **THEN** the prompt requires an uncertain enclosing expression instead of guessed arguments or flattened structure; absence of required positive structure remains a failed recognition criterion even when the response is a safe abstention.
### Requirement: Explicit structured math preserves unknown children without confirmation

An exact version 3 `structured-math-transcription` request SHALL admit the
bounded typed tree and report contract in structured-math-contract.md. The
normalizer SHALL preserve declared child roles, token bytes and unknown slots,
derive coverage and provenance from admitted state, enforce shared byte/node/
depth limits, and emit only inert unconfirmed data. Versions 1 and 2 SHALL retain
their current wire and identity behavior. Failure and output-limit fallback
SHALL clear every result slot without retry or salvage.

#### Scenario: Known structure with unknown children
- **WHEN** a valid structured reply contains a fraction and a subscripted radical with unknown child expressions
- **THEN** the exact tree and unknown boundaries are retained with partial coverage and no invented token or automatic normalized-source conversion.

#### Scenario: Malformed or excessive structure
- **WHEN** a reply has unknown fields, invalid arity, deep nesting, duplicate keys, forbidden token controls or excess shared nodes/bytes
- **THEN** the called operation refuses with no result payload, preserving its exact invocation/attempt facts and owned context lifetime.

#### Scenario: Well-formed but wrong recognition
- **WHEN** an allowed tree asserts a wrong glyph or attachment from the source image
- **THEN** parser success is not recognition acceptance; independent source-based qualification retains the failure and does not confirm the output.


### Requirement: Standalone confirmed context admits ready ordinary notebooks narrowly

The existing explicit transcription operation SHALL admit selected confirmed
context from an already-ready ordinary notebook format4 in addition to its
unchanged legacy-family behavior, through a handwriting-specific read-only
existing-store entry. Format4 SHALL satisfy existing readiness/actor/generation/
contract, complete recovery/local-manifest, absent-or-empty selection AND
selection-history and absent-or-LocalOnly mode checks. The operation SHALL retain
existing LocalCorrections custody through report completion/error/drop and SHALL
preserve request/prompt/identity/failure contracts. It SHALL NOT broaden generic
maintenance or legacy sync/publication, initialize/adopt/repair/restore a notebook,
activate automatic consumers or open a Store for null context.

#### Scenario: Explicit prepared notebook context
- **WHEN** a caller selects an exact current confirmed correction revision in a real prepared ready4 store with absent or LocalOnly mode
- **THEN** query/inspect/capture preserve its exact retained PNG/text/provenance and one explicit fake-engine invocation can produce an unconfirmed result with existing identities and no transcription commit.

#### Scenario: Correction history survives reopen on notebook4
- **WHEN** explicit confirm/update/CAS/forget/status operations run through their existing correction APIs on4 and the store is reopened
- **THEN** exact revision history/media/tombstone semantics remain coherent, stale context refuses and no forgotten or alternate example is silently selected.

#### Scenario: Notebook state is not read-only admissible
- **WHEN** readiness/actor/generation/contract is missing or mismatched, recovery is unavailable/nonlocal, selections or history are nonempty, or mode is nonlocal/configured sync
- **THEN** context refuses under existing typed failure mapping before any provider invocation, with context=null and unchanged existing path/content inventory including capabilities and staging.

#### Scenario: Real ownership survives failure and output
- **WHEN** a valid4 context is captured or its capture fails after ownership, including stale/media capture refusal, cancellation or report output failure
- **THEN** acquired real mode/local ownership excludes competing changes until report drop, no second call/report occurs, and format4 legacy publication/sync stay unsupported afterward.

#### Scenario: Legacy and null-context boundaries remain
- **WHEN** a caller uses existing legacy fixtures, a null context or an unrelated maintenance admission
- **THEN** existing legacy outcomes/identities remain, null context creates no Store roots, and generic maintenance plus legacy sync/publication still deny notebook4 without automatic Reader/Writer activation.


### Requirement: Ordinary runtime selects bounded confirmed examples on its existing Store

An explicitly enabled active handwriting profile SHALL select confirmed examples
using confirmed-recency-v1 in runtime-integration-contract.md before calling
the unchanged exact-revision capture contract. Disabled/unset SHALL preserve
current no-context behavior. Selection SHALL use one complete bounded metadata
snapshot, descending asserted confirmed_ms order with stable record/revision-ID tie-breaks, at most sixteen candidate media checks, declared
skip/omission diagnostics and no replacement after capture failure. Capture SHALL use the exact receiving
Ledger/Dispatch Store and retain real successful/refused ownership through the
operation. No Store reopen, automatic confirmation or model-assisted retrieval
SHALL be introduced.

#### Scenario: Stable bounded automatic selection
- **WHEN** an enabled ordinary profile contains current confirmed values, conflicts, tombstones and unusable samples
- **THEN** the fixed sixteen-candidate window, at most three usable examples and exact ordered revision IDs/counts/media reads follow the declared recency policy; target sample hashes are excluded and no other profile is used.

#### Scenario: Later learning and forgetting affect selection
- **WHEN** a later explicit confirm/update has a newer asserted confirmed_ms in the active profile
- **THEN** its current eligible head can enter subsequent context ahead of older corrections, with deterministic ID tie-breaks; forgetting removes it, while skewed/future caller timestamps remain an explicit ordering limitation.

#### Scenario: Empty differs from failed capture
- **WHEN** selection is genuinely empty or all candidates were explicitly skipped
- **THEN** the operation may use None with truthful CompleteEmpty/PartialEmpty diagnostics and unchanged old payloads.
- **WHEN** storage/ownership/cancellation fails or a frozen selected revision drifts before capture
- **THEN** the operation refuses before a model call without refill, reselect or null-context fallback.

#### Scenario: Receiver and configuration lifetime
- **WHEN** a foreign Store, selected/sync route, changed source/root, canceled or replayed operation attempts context admission
- **THEN** existing ownership/currentness checks refuse; successful/refused owners remain held through receiving/output/error/drop and configuration does not switch midway.

### Requirement: Runtime recognition uses task-specific examples without changing target semantics

Ordinary Reader SHALL capture one same-Store context for its real initial analysis
and independent verification. Writer source-image receiving SHALL reuse existing
admitted whole-page normalization before normalized-source validation/archive.
None SHALL retain exact old payload/identity behavior. Examples SHALL remain
labeled data, never target sources, instructions, inferred confirmation or a
substitute for the independently verified reading. The concrete payload byte
bounds and intended source/test changes are in runtime-integration-contract.md.

#### Scenario: Reader independent verification with context
- **WHEN** a captured Reader operation sends its existing analysis and verification calls
- **THEN** both receive the same frozen example IDs/PNGs and original target images, verification receives no proposed question/answer, and original response formats/agreement/two-recognition-call budget remain.

#### Scenario: Writer recognizes before generating a note
- **WHEN** an admitted retained source-image operation enters Writer receiving
- **THEN** examples affect the existing normalization call before validated normalized-source/archive admission, only a whole Page result proceeds, and examples never become source units or note-generation instructions.

#### Scenario: Native ingress remains absent
- **WHEN** no genuine native Writer source-image or explicit correction-intent input owner exists
- **THEN** typed receiving fixtures do not claim automatic physical integration and the attachment remains an unfinished delivery task.

### Requirement: Runtime handwriting confirmation requires explicit source-bound intent

Only an explicit handwriting-correction confirmation intent SHALL publish a
Handwriting1 confirm/update through existing validation/CAS/status on the same
Store. The adapter SHALL retain exact original conversation/turn/source revision,
eligible PNG and original/corrected text with caller-asserted provenance. No
image transformation, synthesized sample, native authority claim or blind retry
of unknown publication SHALL follow.

#### Scenario: Explicit correction round trip
- **WHEN** the input owner explicitly confirms corrected handwriting text for an exact eligible retained original source
- **THEN** the existing record contract stores the exact original sample/text and correction under stable identity, preserves expected-head conflict/status semantics, and exposes it to later admitted profile selection.

#### Scenario: Refinement is not confirmation
- **WHEN** ordinary Refine, dissatisfaction, model agreement, cancellation or question-mark erasure occurs
- **THEN** zero handwriting correction records are created unless a separate explicit confirmation intent was supplied.

### Requirement: Explicit Writer enrollment after abstention

The typed Writer receiving owner SHALL be able to enroll user-confirmed
transcription text for the exact retained Writer image after valid WholePage
abstention, subject to explicit user intent, same-Store custody and existing
correction publication and replay guarantees.

#### Scenario: Explicit enrollment of the retained image

- **WHEN** the admitted owner supplies the user's explicit enrollment intent and current bound abstention evidence
- **THEN** publication stores the exact admitted PNG and confirmed text with null original and distinct abstention provenance
- **AND** the operation creates no normalized source or generated note

#### Scenario: Missing intent or invalid custody

- **WHEN** the owner lacks explicit intent or valid current abstention evidence, or image, turn, scope or correction heads changed
- **THEN** no correction is published and existing records remain unchanged

#### Scenario: Legacy correction and mixed context

- **WHEN** a legacy correction is read or used alone
- **THEN** its existing representation and payload identity remain unchanged
- **AND** a context with an enrolled example explicitly represents the absent original and uses the pinned mixed recipe

#### Scenario: Older typed consumer and opaque backup

- **WHEN** an older typed consumer encounters an unsupported enrollment record
- **THEN** it refuses unsafe interpretation or mutation
- **AND** supported opaque backup and restore preserve exact record and media bytes
