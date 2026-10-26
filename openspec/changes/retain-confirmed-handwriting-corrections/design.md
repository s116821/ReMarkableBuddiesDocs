# Current basis and boundaries

Current Source9be8862822e4ff0f110d91a0127b1af6db379e5c already provides
Namespace::Handwriting, domain1 envelopes, Store::stage_blob/read_object,
snapshot_heads_matching/snapshot_revisions_matching, commit/CAS, retained media,
ordinary-mode leases and offline whole-store backup. This does not implement a
typed handwriting provider. Existing SubjectMemory, Source and Conversation
schemas/validators and SDK integration are not changed by this proposal.

The first useful unit is explicit sample/confirmed-text retention and invalidation.
The user supplies a sample and confirms the replacement; the provider does not
infer confirmation from a refinement, canceled response, model confidence or
successful export. This is caller-asserted confirmation, not authenticated proof
of a human event or recognition accuracy. Future Reader/Writer hooks must resolve
their actual source provenance before claiming stronger links.

# 1. Local explicit provider and transport

Add a provider-independent handwriting module with confirm/update, inspect,
query, forget and non-mutating operation status, plus a one-shot --handwriting command using strict
tagged JSON on stdin. Reject duplicate/unknown fields, nil identities, partial
reference triples and invalid values before Store opening/admission. No automatic
sample capture, network provider, model construction or native startup occurs.
Use the existing configured owned Store; no alternate database or registry.

Require explicit profile, correction and operation UUIDs on mutations and exact
expected head UUIDs (empty only for new records). Profile is a caller-selected
logical grouping, not a personal account or discovered identity. All runtime
selection/sync modes except absent/LocalOnly refuse before opening the domain.
Hold existing OrdinaryModeLease and LegacySyncLease through actual stdout/error
completion, using the established host-command ownership pattern. Store opening
may perform documented recovery writes; zero command mutation is not a blanket
claim of filesystem read-only behavior.

Confirm carries confirmation:"user-confirmed", original_text, corrected_text,
confirmed_ms, sample_png_base64 and provenance. Both texts are nonempty UTF-8,
at most4096 bytes, no NUL/unsupported controls (LF/CR/tab allowed). Equal text
is allowed as explicit confirmation of an interpretation. Provenance carries
kind:"caller-confirmed-sample", description at most512 UTF-8 bytes, and either
null or [conversation,turn,source_record] UUIDs. These optional links are asserted,
not resolved native/document ownership. Labels must state that distinction.
No free-form prompt/policy or confidence-improvement claim is stored.

Stdin is at most768 KiB plus one rejection byte followed by EOF. A sample is
strict standard padded base64, decoded at most512 KiB; reject excess encoded
length before decoding/allocation. Accept PNG only, verify decoded format,
width/height1..2048 and at most4,194,304 pixels with bounded decoder allocation
before full decode. Do not accept external image paths, URLs or filesystem
fallback. The exact admitted PNG bytes are retained unchanged; sample cropping
is caller-provided and does not establish a mapping onto a tablet page.

Query/inspect do not return image bytes, only typed facts/descriptors and truthful
availability. Sample display/training consumption is a later supported boundary.
Confirmation/update retains complete original sample bytes and provenance.
Updates may change confirmed replacement/confirmation time/description under CAS;
profile/correction, original_text, optional source links and sample digest/bytes/
dimensions remain immutable. Replacing those requires a new correction identity.

# 2. Exact identity and durable shape

Existing Handwriting/domain1 gets a strict payload discriminator
kind:"confirmed-correction". This is proposed until ordinary owner/precode review;
generic namespace admission does not reserve the shape. Never deserialize old
unknown/synthetic handwriting payloads into this shape by defaults.

Record fields in serialization order: kind, profile, correction, original_text,
corrected_text, confirmed_ms, provenance, sample, width, height. provenance order
is kind, description, source; sample uses unchanged Media fields sha256,bytes,
media_type with media_type exactly image/png. Every value field is strict and
required; optional source is explicit null or an exact three-UUID array.

C means compact serde_json UTF-8 with no BOM/LF, no string/Unicode normalization,
lowercase canonical UUIDs, null option values and unsigned decimal integers.
H means lowercase hexadecimal SHA-256; U means UUIDv5(URL namespace, UTF-8 name).
record_id = U("urn:rmb:handwriting-correction:v1:" + profile + ":" + correction).
Value digest = H(C(the complete ordered record struct above)). Tombstone payload
is null and its media_descriptors is empty, following the existing storage contract;
never invent a confirmed empty record.

Mutation fingerprint = H(C(["handwriting-mutation-v1", action, record_id,
sorted_expected_heads, value_digest_or_null])). action is confirm/update/forget;
sorted_expected_heads sorts canonical UUID strings ascending and rejects duplicates.
revision_id = U("urn:rmb:handwriting-revision:v1:" + operation + ":" + fingerprint).
Envelope actor is the owned Store actor; operation_id is the explicit operation;
parents are exactly expected heads. Envelope media equals exactly the value's
sample descriptor; tombstone descriptors follow the existing tombstone contract.
No current wall-clock/random revision value may break exact replay. confirmed_ms
is the supplied assertion time, not an observed filesystem/model timestamp.

An operation reused for changed action/key/heads/content refuses. Repeated identical
operation returns historical result, never another learning event. Check this
across all retained Handwriting revisions, not only current heads. On replay,
compare the semantic fingerprint, deterministic revision, payload/parents/media;
return the original envelope without replacing its actor or rewriting it using a
restored Store's newer actor. No cross-domain
receipt/intent reuse. Ledger/Source1/2 bytes and all native admission stay unchanged.
The literal recipe vectors in identity-vectors.json cover Unicode/newline/null
and changed-field cases. Their artificial media descriptor is recipe data, not a
decodable image or completed confirmation fixture. Implementation must assert
literal expected values independently of the production function; no source
implementation is accepted by this initial design checkpoint.

# 3. Publication, retained bytes and read outcomes

Validate the full mutation/sample before staging. Stage admitted bytes with the
existing generic blob primitive and publish one typed value envelope using the
existing CAS transaction. Staged-only content is not a visible correction.
Unknown commit acknowledgment is not proof of rollback. The separate status
command looks up the exact operation/key in retained history and never stages or
commits. Absence means unknown, not rolled back/not-dispatched. Do not automatically
resubmit a mutation. A new explicit confirm/update/forget invocation is a deliberate
CAS submission: an exact accepted operation returns historical without commit;
changed content refuses; absent accepted history may still proceed through CAS
as an explicit submission and is not represented as read-only reconciliation.
This distinction avoids pretending a first dispatch and an absent uncertain
dispatch can be distinguished without a durable intent. Return receipt/identity and
observed result honestly; no automatic retries or alternate destinations.

Each typed envelope must have exact namespace/version/discriminator/record ID,
expected parents and media descriptor equality. Required image bytes must pass
content hash/size and image validation before a complete usable result. An
available metadata-only historical record is not a complete training sample.
Unavailable commits refuse completeness. Current conflicts are withheld from
ordinary queries, with partial diagnostics; no newest-timestamp winner heuristic.

Query takes explicit profile, optional query text (at most2048 bytes), max_matches
1..16 and max_encoded_bytes512..65536. Scan at most4096 current envelopes under
the existing bounded snapshot primitive and its8 MiB metadata cap; fail on
exhausted/incomplete traversal. Reserve the selected fact/output subset before
image reads: verify at most16 samples and8 MiB compressed image bytes per command,
with at most16 times4,194,304 decoded pixels processed sequentially. Validate typed
descriptor size before reading; never decode every matching/nonmatching sample
while scanning4096 heads. Omitted sample availability is not-examined, not available;
missing_media counts only the actually examined subset and cannot prove corpus-wide
availability. Inspect applies the same aggregate verification bounds.
Filter exact profile and strict confirmed values. Optional text performs plain
Unicode-lowercase token matching over original/corrected text; no semantic claim.
Order matching keys by canonical record UUID, not asserted confidence/date. Count
actual complete JSON encoding, including diagnostics. If matches cannot all fit,
return bounded Partial/omitted counts or a fixed budget refusal, never false empty
or silently truncate a text/sample. Do not emit partial JSON on output failure.

Inspect returns exact captured current heads and completeness/conflict/unsupported
state. Status returns only the requested retained operation, including a historical
tombstone; it does not construct new confirmation or infer no effect from absence.
Exact public facts, diagnostics, failure codes and outcome matrix are fixed in
report-schema.md; all reads are historical observations, not live consumption grants.
Forget requires explicit nonempty current heads and publishes a tombstone; it
removes the correction from active query without rewriting/deleting historical
samples or other keys/profiles. Invalidating one record does not wipe a corpus.
Reports are explicit user artifacts and may contain the requested text; routine
Debug/error logs redact texts, image/base64 and paths. No second error report after
partial stdout; preserve actual mutation uncertainty separately from output errors.

# 4. Compatibility and scope closure

Whole owned backup/restore must preserve exact typed record bytes, source samples,
parents, conflicting heads and tombstones using existing storage infrastructure.
Retained historical values keep media referenced after forget. Existing owned-data
inspection reports the Handwriting category but gains no recognition authority.
Unknown/new typed payloads must be preserved/refused, never overwritten or treated
as generic learned examples. Existing raw synthetic storage fixtures remain valid
generic fixtures and are not relabeled confirmed corrections.

Selected aggregate membership, Drive sync, narrow conversation cleanup, native
receiving and automatic Reader/Writer context consumption remain unsupported for
this new domain. Do not expand those consumers or edit SDK integration. A future
consumer must validate this domain explicitly and preserve source/media closure;
opaque generic backup success is not domain-level sync/native acceptance.

# 5. Verification and remaining product requirements

Use actual Store and early CLI subprocess tests: malformed/duplicate/one-over input;
bad base64/PNG/pixel bounds; explicit confirmation requirement; Unicode/newlines;
CAS conflict, changed operation replay, lost acknowledgment/reopen; immutable
sample/provenance; foreign profile; query ordering/budget/partial/conflict/missing
media; tombstone filtering and retained-byte backup/restore; mode/lease refusal;
stdout failure and routine-log canaries. No model/provider/tablet is needed.
Preserve failed logs. Current-head hosted checks and independent review precede
delivery; do not run a large local build while disk space remains constrained.

Keep one linked Source/Docs implementation delivery, canonical sync/archive only
when implemented/qualified. Broader effective recognition, confirmed correction
hooks, contextual application, efficacy/regressions, Reader/Writer/combined native
flows, sync and whole product acceptance remain open. Stored corrections alone
must never be called improved recognition or trained external-model state.
