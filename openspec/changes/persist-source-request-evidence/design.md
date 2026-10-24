# Durable historical request evidence

## Current contracts and preserved work

The implementation base is published Buddy v0.32.0, actual source
`7ca8646e220204ca956be31319ca4ab284526320`, and actual central Docs
`9f716ba4e53d0fd596bc3fe20deba9761a2d39c9`. That receiving increment is complete
and is not reopened by this proposal.

`Ledger::source_request_context` returns an immutable `FrozenRequestContext` with
an exact encoded frame, request, eligible history, explicit original/no-document
association, full key/passages and missing-media facts. It does not retain Store
generation or envelope revision/object identities. `Ledger::inspect` validates
one bounded head snapshot, then discards those envelope identities. Keep this
public read-only behavior and encoded schema unchanged.

Ordinary writes publish root, records and operation receipt atomically. Identical
operation/content replay precedes stale-head admission and returns historical
acknowledgment without resurrecting a deleted root. `Store::commit` checks parents
of written records, not a separate read set. `with_conditional_heads` holds the
Store mutex, so calling `commit` inside its callback would deadlock. The existing
`conditional_commit` is a single-tombstone maintenance primitive and is not this
publication interface. Do not weaken either maintenance contract.

Retained Writer PR62 at `e525b76683410137b6c47cf86e0c9ea85a930825` has
`NormalizedTextSource`/`Record::NormalizedText`: complete supplied normalized text,
Page/SuppliedNotebook scope, a 48 KiB bound and generation/refinement semantics.
It is not a retrieved-passage selection. Do not copy its implementation, embed a
receiving record into guidance text, or import its held runtime/model gate.
The preserved original retrieval branches provide Index/Provider, not a durable
passage record. BindingReceipt and ExportAssociation retain page-claim and
native-export purposes; neither becomes a general source registry.

## Public ordinary API

Add `conversation::evidence` with these data-only operations:

```rust
Ledger::prepare_request_evidence(
    conversation: Uuid,
    request_turn: Uuid,
    selection: Option<TurnRange>,
    source: RequestSource,
    budget: ReceivingBudget,
    retrieval: Option<&dyn retrieval::Provider>,
    token_count: impl Fn(&str) -> Result<usize>,
) -> Result<PreparedRequestEvidence>

Ledger::persist_request_evidence(
    operation: Uuid,
    recorded_ms: u64,
    prepared: &PreparedRequestEvidence,
) -> Result<WriteResult>

Ledger::request_evidence(
    conversation: Uuid,
    request_turn: Uuid,
    operation: Uuid,
) -> Result<Option<HistoricalRequestEvidence>>
```

`PreparedRequestEvidence` has private fields, no public constructor, Clone or
Deserialize. Its immutable `context()` getter exposes the existing frozen frame.
It owns the private captured read set and exact reference inputs, not a native or
selected token. A weak Store identity check binds fresh publication to the actual
Store instance without keeping its OS lease alive. The recorded historical view
is a different type and cannot be converted into a fresh preparation.

Preparation validates ordinary budgets first, obtains a single bounded Store
snapshot, validates the same ordinary chronology, then invokes a shared private
receiving assembly function on those captured records. The old read-only API
continues to use its original inspection path and that same assembly function.
The new path performs one local query for a bound request and zero for explicit
no-document, with the original unchanged request text. Counter/query callbacks
remain outside Store/domain locks. There is no second query to verify or publish
the result and no invented token counter on historical readback.

Only a successfully validated receiving result can produce this preparation.
Here unavailable evidence means the frame's explicit unavailable-media facts and
unavailable historical references on readback. Invalid association/key, unavailable
Provider, malformed result or unknown/exhausted counter still return the existing
typed refusal before any publishable preparation exists. This change does not
convert a failed retrieval into a source-less frame or claim to persist every
request-failure diagnostic; existing attempt-outcome facts keep that separate
purpose.

The shared assembly refactor must preserve existing read-only return/error order,
encoded schema and callback behavior. Persistence is always a separate explicit
call; constructing either kind of frame does not publish anything.

## Record and ownership

Add `Record::RequestEvidence(Box<RequestEvidence>)` under the existing
Conversation namespace and ordinary domain schema 1. This is a new strict
historical fact kind, not a source-capture record or another registry. Older
clients may refuse the unknown kind and retain it; they must not reinterpret it.
Store format and namespace/schema-version admission remain unchanged.

The strict serde representation contains:

| Field | Meaning |
| --- | --- |
| evidence_version | Exactly 1 |
| id | UUIDv5 derived from `urn:rmb:request-evidence:v1:{operation}` |
| conversation, request_turn, operation | Existing conversation/request and explicit operation identity |
| recorded_ms | Caller-supplied historical timestamp, not clock authority |
| frame_json, frame_sha256 | Exact original encoded UTF8 frame and its SHA256 |
| counted_tokens | Original caller-reported count of that exact frame |
| limits | Original turn/text/frame/result/count/neighbor/token admissions |
| snapshot | Historical actor, generation and digest of the complete captured relevant head set |
| root | Exact original root envelope reference |
| turns | Exact original references for every allocated turn through the requested sequence, including ineligible prepared/draft turns |
| sources | Exact original source-record references needed by the selected eligible context and explicit original association |

A historical record reference contains namespace, record UUID, revision UUID and
the original committed `ObjectRef` (hash and byte length). Obtain original object
identity from accepted Store index/manifest references; do not hash a parsed,
reserialized envelope and call it the original bytes. Pretty-printed imported
envelopes must retain their actual reference identity.

Snapshot actor/generation describe the Store at preparation. Referenced imported
envelopes may retain earlier actors; ownership checks bind their conversation,
request and source relationships, not equality with today's Store actor. Resolve
historical refs through accepted current Store history by hash, never by an old
absolute generation path or a new native authorization.

Only selected-context sources and the explicit original source are referenced.
The original user turn is already in the through-request turn prefix even when
outside the selected range. Do not copy the whole normalized document, cache,
source-image bytes, unrelated conversations or prior evidence records into the
fact. Original source facts and all selected passages remain in `frame_json`.
The through-request turn prefix permits historical eligibility/completeness
checks without following a recursive graph of prior request-evidence facts.

The fact is immutable per operation, with no parents on its first publication.
A deliberate new operation may record a new selection for the same request;
inspection exposes separate facts and does not silently choose the latest by
timestamp. No Turn.sources link is added for this fact. Existing capture-batch
membership, source-image ordering and prepared_images rules remain unchanged.

The fact's own media descriptors are empty: it owns logical metadata and exact
references, not a second image acquisition. Original source envelopes continue
to retain their image descriptors and immutable objects after logical deletion.
There is no garbage collection or physical pruning in this increment.

## Private ordinary Store dependency

Introduce an opaque crate-private captured-head value and two focused operations
along the existing ordinary Store path:

1. Capture relevant current heads with generation, Store identity and original
   record ObjectRefs in one existing inner-mutex interval. Reuse the current
   MAX_ITEMS/MAX_METADATA snapshot admissions and matching rule, including all
   heads for any matching record key so conflicts/tombstones cannot be hidden.
2. Publish ordinary records only if that captured Store/generation and complete
   relevant head set remain exact, with one mutex guard spanning comparison and
   the existing `publish_locked` path.

The capture retains the domain's pure matching function and conversation key;
publication cannot substitute a broader/narrower selector. Matching is an internal
pure predicate, not a user Provider/token callback. Unrelated conversation changes
do not invalidate the read set. New relevant records, changed revisions, conflicts,
tombstones or same-content replacement revisions do invalidate it. Restore into a
new generation invalidates a preparation even if its logical heads are identical.

Original metadata ObjectRefs are rechecked for accepted reachability and exact
bounded bytes before fresh publication. Do not claim that parsed equality alone
proves immutable identity. This verifies record metadata, not all image bytes or
current source-document freshness. Preserve existing required-commit corruption
versus declared imported-media omission semantics.

Refactor only the ordinary commit's manifest/object construction as needed to
share it with this new path. Keep existing commit/import/fault order, CAS,
notifications, ownership and recovery semantics. No callback reacquires the Store
mutex. Do not reuse selected publication, alter CURRENT by hand, add a storage
protocol, or change the existing tombstone-maintenance helpers.

## Publication, stale input and retries

Persist the exact prepared frame without calling a Provider, tokenizer or image
reader again. Derive a stable fingerprint from the versioned operation purpose,
conversation/request, recorded_ms, exact frame bytes, reported count and limits.
Keep transient Store-instance/generation/read-set pins out of that input
fingerprint, as expected heads are excluded from existing ordinary retry inputs.
The published fact retains its original historical pins.

Check an existing ordinary operation receipt first. It must match the stable
fingerprint and point to the exact request-evidence fact in its original atomic
root/fact/receipt transaction. A matching historical retry returns that original
acknowledgment/fact; it does not attach a new frame, refresh provenance, recreate
a deleted root or confer current authority. Changed frame/source/key/limits/time
under the same operation refuses. Missing, contradictory, conflicted or wrong-type
receipt/fact state refuses rather than selecting a retained winner.

For a fresh operation, require the actual originating Store instance and captured
generation/read set, the original existing Reader/User/Interpreted request and
all validated reference relationships. Publish exactly the evidence fact, a root
successor and the existing ordinary receipt atomically. Keep next_sequence and
binding unchanged; root.updated_ms may advance to max(old, recorded_ms). The root
parent set is the captured current root. No new visible turn or response is added.

One Store mutex spans currentness checks and the normal atomic publication. A
changed request/history/source during a counter/query callback or concurrent
write therefore cannot escape as a newly attached stale fact. Failure before
the manifest leaves no visible fact/receipt/root successor; a durable commit with
lost acknowledgment is recovered by its original receipt. Concurrent identical
operations produce one historical fact. A new fact for a deliberately changed
selection requires a new explicit operation and fresh preparation.

After process restart, `request_evidence` recovers a committed result by its known
IDs without a query or publication. An uncommitted preparation is not restored
from JSON; obtain a new preparation if a fresh write is required.

## Historical readback and reference validation

The historical result exposes the stored record and acknowledgment plus explicit
currently unavailable media under the existing ordinary object checks. It does
not return a writable preparation. Recorded `frame_json` and its missing-media
facts remain unchanged; present availability is a separate historical-read report,
not selected logical coverage or native/source freshness.

Validate strict record/version/identity/digest/limit fields and parse the bounded
frame with a private strict frame DTO. Reject unsupported fields/kinds and require
the receiver's canonical encoding for the exact stored frame. Validate its request,
source association, full key/result structure, no-document/zero-match distinctions,
range and admitted text/count/encoded bounds. Counted tokens remain the originally
reported caller count, never a newly invented tokenizer/model-window proof.

Resolve pinned record references by their actual committed bytes. Verify namespace,
record/revision/owner, complete through-request turn allocation, eligible history,
correction/source identities and exact original turn/source relationship. Reuse
the existing context-selection machinery for structural comparison without
claiming a historical tokenizer has been rerun. Compare the rebuilt eligible
request/history and source facts with the exact stored frame. A source key remains
a historical extraction assertion; reading it never performs a fresh query or
uses a cache key as freshness evidence.

Reference checks are bounded and cache repeated exact record refs within a read.
General ledger inspection must not return an apparently validated evidence fact
whose required record references are absent or contradictory. Apply the same
domain checks when evaluating ordinary settled-history cleanup eligibility; do
not treat a malformed fact as harmless because it is not a visible Turn. Keep
existing incomplete/pending/export/deletion rules intact.

No-document remains explicit with no fabricated original/key/result. Bound zero
matches remains a source-bound empty result. Declared unavailable source images
stay unavailable evidence; missing/corrupt required record objects refuse. No
retained winner is substituted for a pinned record. Historical SDK/development
classification and source markers remain exact; no native capability is recreated.

## Export, import and deletion

Ordinary Store export already preserves logical records and immutable objects.
No new export format or side registry is added. A complete export/import must
retain the evidence, original record refs, exact frame and original operation
receipt. Metadata-only media policy retains the logical text/evidence records;
omitted image bytes are reported separately on readback. A new Store actor or
generation does not upgrade old historical pins or block reading valid history.

Logical conversation deletion retains the fact and referenced historical source
envelopes/objects, following current retention semantics. Historical operation
lookup may still return its original record after deletion; a stale preparation
cannot publish or resurrect the root. Existing inspection with retained=true stays
historical, while ordinary live-root context remains refused after deletion.

Malformed imported frame/ref/receipt relationships refuse domain interpretation
while retaining underlying Store evidence. Unsupported old/new clients preserve or
refuse unknown record kinds instead of rewriting them.

## Resource contract

| Admission | Bound and meaning |
| --- | --- |
| Receiving assembly | Existing 64 turns / 64 KiB text / 512 KiB complete frame / 16 passages / 16 KiB complete result and caller-token rules |
| Captured current heads | Existing 4096 head and 8 MiB metadata limits; original committed ref sizes also admitted before new reference reads |
| Saved historical refs | At most 4096 unique references, each at most 1 MiB and at most 8 MiB cumulative original record bytes |
| Durable evidence envelope | Existing MAX_RECORD 1 MiB for the entire encoded envelope, including escaped frame_json, references, limits and identity |
| Atomic transaction | Existing MAX_METADATA 8 MiB and MAX_ITEMS admissions for fact/root/receipt |
| Historical reference work | Cache duplicate exact refs and refuse beyond 8 MiB / 8192 visits in a bounded read or inspection, without a partial validated result |

A valid read-only frame can still exceed the durable envelope admission once
provenance and JSON string escaping are included. Report an explicit persistence
bound refusal; do not shorten the frame, drop refs, truncate passages or change the
original query. Serialize the complete evidence/envelope with a capped writer
before publication. These are data/work bounds, not hard global RAM/CPU/deadline
or final model-window guarantees.

## Compatibility and implementation boundary

Expected Buddy files are the ordinary conversation evidence module/record adapter,
shared private receiving assembly, ordinary inspection/cleanup reference handling,
a private Store captured-head publication module with minimal registration/shared
commit construction, authored fixtures and public guidance. A typed Record enum
addition requires two selected-projection compatibility arms: identify its owner
and explicitly refuse this ordinary evidence in selected projection. Do not alter
selected effect, lifetime, bootstrap, source-admission or settlement behavior.

No Writer source, SDK/Cargo pin, CI/release policy, settings, Manager consumer or
reserved central capability is changed. Record-kind additions must compose with
the held Writer variant later; no competing normalized-text implementation is
introduced. Detailed final paths and preservation proof accompany source review.

## Original verification and coordinated delivery

Use real temporary Store/Index fixtures for bound selection and fresh follow-ups,
changed-source isolation, no-document zero query and honest zero matches. Verify
reopen/readback without querying; exact frame/provenance/qualification; original
outside-range source and imported media omission; exact byte bounds/escaping;
same-content changed revisions and restore generation; counter/provider callback
changes; concurrent identical/conflicting operations; all ordinary commit fault
boundaries and lost acknowledgment; deletion/no resurrection; and malformed,
foreign, absent or pretty-printed original record references. Exercise complete
and metadata-only ordinary export/import and settled cleanup eligibility.

Retain original failures. Run affected ordinary conversation/receiving/cleanup and
storage regressions, a separate non-mock library check, fmt and strict Clippy.
No artificial model/UI/native simulator claim is needed for this data-only seam;
fixtures use the real data path. Obtain independent precode review before source
edits, then source/spec review and current normal hosted/cross-target gates. Sync
and archive only this completed capability, request final paired review, merge
Docs first/Source second normally and observe actual-main/tag/small provenance.
Do not download/replay old application packages or claim broader completion.
