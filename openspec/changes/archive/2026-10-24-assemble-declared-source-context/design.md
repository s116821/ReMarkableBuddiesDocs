# Design

## Verified current mechanisms

`source_request_context` validates its budget, inspects one ordinary conversation
snapshot, and assembles its frame from those records. `prepare_request_evidence`
validates its budget, captures complete relevant heads/generation, validates that
capture and historical evidence, then uses the same assembler and retains exact
original references. Publication checks the captured read set atomically.

`resolve_request_source` separately reads a known historical fact and inspects
current records, checking that the fact remains present/equal. It returns ordinary
RequestSource data, not snapshot continuity into another call. Neither a page
binding nor historical evidence is an active user-intent registry. Retained
Reader placement and Writer supplied-text ownership remain unchanged.

## Additive public entry points

Add methods with the same arguments/return types as their existing counterparts,
replacing only the source argument with `SourceDirective`:

- `Ledger::source_request_context_with_directive` returns FrozenRequestContext.
- `Ledger::prepare_request_evidence_with_directive` returns the existing sealed
  PreparedRequestEvidence, published through unchanged persist_request_evidence.

Explicit directives preserve existing receiving validation and byte encoding.
Inherited directives require the caller's named prior request/operation, not the
latest timestamp or an inferred active choice. Omitted operation is AnchorRequired
even with one candidate. Prior NoDocument requires no key; prior Original requires
an independently supplied complete key. Reindexing the same document may supply
a different key; the Provider still owns actual local index freshness admission.

## One validated record snapshot

The new read-only entry point uses one ordinary inspect result. The new preparation
uses one existing Store capture. Select the named fact from those validated records
and resolve its source against the same records passed to the existing assembler.
Do not call the standalone public resolver and then take another receiving snapshot.

Historical evidence validation still checks exact bounded original references and
receipt/transaction relationships. Its current-head checks may conservatively
refuse a concurrent change; they must never substitute a different fact. Within
the frame's captured records, require the named fact, earlier same-conversation
interpreted Reader request, linked original turn/source and equal historical source
content. Identical-content source revision successors remain allowed. Missing,
foreign, future, corrupt, conflicted or changed-source dependencies refuse without
queries or fallback. Explicit no-document makes zero Provider queries.

Extract a conversation-private resolver over already validated records. It is not
a public snapshot constructor or new authority witness. The standalone resolver
retains its historical-readback/current-fact equality check and test-only deletion
boundary, then reuses that private logic. Preserve its public behavior/refusals;
do not remove its original deterministic regression.

The new receiving path resolves before Provider/token callbacks, outside Store
locks. The existing assembler owns immutable request/history/source copies and
complete budgets. Later callbacks may mutate current Store heads, but returned
read-only frames retain captured facts rather than rereading a new winner. This
is historical consistency, not proof that current state stayed unchanged.

## Durable preparation and compatibility

Factor existing evidence capture/validation and frame/reference construction into
private helpers. Keep the old public preparation's validation order and errors;
its explicit source path must not acquire new resolver errors. The new entry point
maps capture/history failures to sanitized HistoryUnavailable and uses existing
typed receiving/budget errors for assembly. Source-resolution errors retain their
sanitized types, without raw internal metadata/path error chains.

Fresh inherited preparation's existing complete captured read set includes the
named fact/receipt along with root, turns and sources. Missing or changed anchor,
source, history, generation or relevant heads before fresh publication refuses
through unchanged captured admission. No Provider requery, implicit re-resolution,
partial publication or new Store primitive is needed. Unrelated conversations
remain independent; callbacks never execute under Store locks.

Use existing frame schema1 and RequestEvidence version1 without new fields. The
saved fact records the resolved source/frame, not which directive/anchor produced
it. Do not claim durable directive lineage, active intent or model consumption.
Existing raw references and immutable snapshot digest keep their current meanings.

Stable retry equality remains based on the existing frame/count/limits/timestamp,
not a newly added directive fingerprint. Equivalent explicit/inherited preparation
can therefore recover the same committed historical acknowledgment. Fresh
preparation still needs a valid current anchor; replay of an already committed
matching preparation remains historical, even after deletion, without resurrection.

## Bounds, verification and delivery

Reuse existing record/reference, complete frame, passage and caller-counted token
bounds. Resolve only the named operation; never enumerate candidates to select a
winner. Preserve exact original request/history and explicit omission metadata.
The private resolution validation may repeat bounded association checks; it adds
no second Provider query or unbounded allocation of caller keys.

Use real temporary Store/Index fixtures following the shared offline checklist:
golden explicit/inherited frames; named choices among disagreeing facts; no-source,
missing/foreign/future/corrupt anchors and bad/stale/new keys; narrow history ranges
with original provenance outside the range; unavailable media; complete bounds;
callback changes preserving read-only captured frames; source/anchor mutations
rejecting fresh publication; unrelated writes; stable equivalent retries and
restart. Assert exact request/history, query counts, stored refs and no extra
writes/queries. Keep all original receiving/evidence/resolver regressions.

This changes ordinary library data flow, with no model/native route. Offline
fixtures qualify that scope only. Obtain independent precode review before Source
changes, then exact-revision verification/review, own canonical sync/archive and
final paired review. Prepare normal Docs-first/Rust-second squash and subsequent
actual-main/new publication observation; record external delivery results in PR
comments and canonical tracking without replaying closed packages or contacting
the tablet.
