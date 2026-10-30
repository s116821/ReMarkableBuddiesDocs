# Ordinary source request context

## Status and delivery
Concrete proposal before source edits. Implementation requires independent
precode review. Deliver this completed data seam and its own canonical sync/archive
in one coordinated Rust/Docs pair, Docs first after verification. Existing PDF,
EPUB and cache deliveries stay closed. No source implementation has begun.

## Actual existing contracts and reuse
At Rust main104e3f27, Ledger.inspect takes one bounded relevant Store snapshot,
decodes records, checks allocated chronology and refuses conflict/incompleteness.
context_from_records preserves interpreted/completed turns, original text and
correction links with explicit range and byte/turn/caller-token refusals. Source
facts are historical, never live/native admission. The selected context and
controlled Reader preparation APIs remain separate and are not changed here.

Turn.sources is a list of existing source-record identities. Ordinary append
allows references to older same-conversation source records, but prepared_images
requires its capture batch to belong to the current turn. Therefore this receiver
does not add an old book reference to a current capture batch or reinterpret an
image's purpose string. Its explicit association is part of the returned request
frame and uses an existing original user turn/source-record relationship.

The preserved original retrieval branches provide Index/Provider, not this frame.
The nearby held memory answer path invokes an LLM and is not imported. Writer's
pending NormalizedTextSource embeds a complete selected NormalizedDocument with
Page/SuppliedNotebook selection and guidance under a 48 KiB record bound. This
receiver retrieves bounded passages through the existing Provider and does not
copy that durable record, import its workflow, enlarge its bounds or manufacture
a second source registry. No durable record variant or data-schema change.

Use the existing IndexKey, Retrieved, Passage, Turn, TurnRange, Media and source
Record variants. The existing normalized index/cache owns passage selection,
fresh full-index queries, exact source keys and immutable source units. No search,
cache, image decoder or provider execution stack is reimplemented.

## Concrete API
Expose a new ordinary conversation receiving module and immutable frame:

```text
RequestSource =
  NoDocument
  | Original { origin_turn: Uuid, source_record: Uuid, expected: IndexKey }

ReceivingBudget {
  context: ContextBudget,
  max_encoded_bytes: usize,
  max_passages: usize,
  max_passage_bytes: usize,
  neighbors: bool
}

Ledger::source_request_context(
  conversation: Uuid,
  request_turn: Uuid,
  selection: Option<TurnRange>,
  source: RequestSource,
  budget: ReceivingBudget,
  retrieval: Option<&dyn retrieval::Provider>,
  token_count: impl Fn(&str) -> Result<usize>
) -> Result<FrozenRequestContext>
```

The request must exist in the captured conversation, have Reader mode, User role,
Interpreted outcome and nonblank text. It is not fabricated from a parameter or a
rendered answer. The existing record is returned unchanged; no trimming,
transcription, prompt rewriting or new turn occurs. Other modes/statuses refuse.
Historical context can include both Reader and Writer eligible turns as before;
unrendered Generated drafts remain outside ordinary eligible history.

Limit history to eligible turns through the specified request sequence. Never
include later answers/future requests when an older request is inspected. A
selection must end exactly at request.sequence+1 and include the request; None
means all eligible chronology through that request. Reuse the existing context
machinery on this bounded sequence view, then separate its exact request from
the preceding chronological history. Keep correction/source identities and text
verbatim. Allocated chronology is validated before this deliberate temporal/range
selection, not repaired by filtering. Explicit selection is carried in the frame.

The frame has private fields and immutable getters for the request, history,
association, retrieval, selection and missing media, plus one stable encoded JSON
view. It has no mutation/dispatch/publication methods. Its closed version-one
encoding contains conversation, complete existing request Turn, history Vec<Turn>,
optional TurnRange, source association, optional Retrieved and missing_media.
Adding Serialize to the existing TurnRange is additive; do not create a rival
range or conversation type. The encoding is an ordinary historical data frame,
not a final model payload, selected causal snapshot or native permission token.

## Association and inheritance semantics
RequestSource is mandatory and has no implicit/default resolution. NoDocument is
an explicit caller declaration that this request has no original document. It
returns no retrieval, performs zero Provider queries and invents no document/key;
it does not claim that the Ledger or a screenshot proved a physically blank page.
An unresolved source must not silently become NoDocument.

For Original, the referenced original turn must be an existing User turn in this
conversation at or before the request. It must link source_record in its sources,
and that current source record must name the same conversation and original turn.
It need not be added to the current request's image batch. Resolve only from the
same captured ordinary records, never retained losing data or current UI pixels.
Supported recorded document assertions are:

- ImageUse.observation.document;
- SDK historical CaptureEvidence.facts.source.document, preserving its exact
  synthetic/historical qualification;
- DevelopmentCaptureHistory.expected_binding.document_id only when it is a
  canonical nonnil UUID, preserving DevelopmentUnqualified classification.

LegacyCapture explicitly lacks document identity and cannot be bound merely by
supplying an expected key. Unknown record kinds, absent/foreign/future/unlinked
origins and unsupported identity refuse. Include the complete original existing
source Record as provenance in the association; do not mint a new stored source
identity. Saved SDK/development labels remain assertions, not current native facts.

The caller independently supplies every expected IndexKey field. Validate nonnil
document, exact lowercase SHA256 fields and bounded nonblank extractor revision
before query/copy. Its document must match the recorded original document, not
the current request image or BindingReceipt.observed_document. Do not derive
content/extractor identity from image hashes or observation revision strings.

A follow-up carries the explicit original turn/source-record reference from its
prior association, supplies its independently refreshed complete expected key and
performs a new full-source Provider query using the unchanged current request text.
The receiver neither discovers a source nor persists/invents automatic association
inheritance. A deliberate target change supplies a different explicit original
reference/key with its own provenance. A changed original byte/extractor/normalized
key must be accepted only by the matching Provider; stale/mismatched results refuse.
Never read a cache/index's own key as proof that the source is fresh.

## Local query and result acceptance
Original requires a supplied retrieval Provider. Call its existing query exactly
once with the independently expected key, unchanged request text, declared count/
byte/neighbor budgets. No previous hits, memory facts or current visible page
constrain that search. Requests outside the existing query profile (including
over 2048 UTF8 bytes) refuse rather than being shortened. No LLMEngine or external
model/research/account request is made; fixtures use the real existing Index.

Refuse a failed query or wrong returned key; never return an apparently successful
frame without the requested source. An honest zero-match Retrieved is allowed.
Preserve budget_limited and passage page/section/unit/range/direct-match fields.
Before encoding, require the declared result count/bytes and structurally valid
nonempty passage text/ranges, bounded locations, no duplicate unit/range and at
least one direct match when passages exist. Preserve existing UTF8/control/location
constraints. A provider owns content/offset fidelity under its existing contract;
the receiver checks key/structural/budget consistency, not independent extraction
proof against unavailable raw source units. Do not invent native confidence.

## Budgets and unavailable evidence

| Admission | Contract |
| --- | --- |
| Existing snapshot | Reuse Ledger/Store metadata/record bounds and complete chronology; no global parser/Store allocation guarantee |
| Eligible context | 1–64 configured turns including the request, 1–65536 configured raw text bytes; reuse ContextBudget and explicit TurnRange refusal |
| Tokens | A positive known ContextBudget.provider_token_limit and caller counter are required; counter receives exact serialized eligible turns and the final complete encoded frame; no bytes-to-tokens estimate or model-capacity claim |
| Whole frame | Caller limit 512–524288 encoded UTF8 bytes, including metadata, escaping, source record, complete key and passages; bounded serializer refuses before growing beyond the cap |
| Local retrieval | 1–16 passages, 512–16384 encoded result bytes, existing neighbor policy |
| Key and result | Existing index identity/location/text bounds; reject oversized/malformed metadata before output copying/serialization |

Serialize the no-retrieval base frame under the whole-frame cap before querying.
Reserve the actual remaining encoded room for the Retrieved value (replacing
JSON null); if less than the Provider's minimum 512-byte budget remains, refuse
before query. Pass the smaller of the declared retrieval cap and remaining room.
Validate and encode the final complete frame under the cap, then count its exact
encoded token input against the known limit. Token exhaustion refuses the frame;
never silently truncate history, rewrite the request or retry with fewer passages.
Counter failure/unknown limits refuse rather than recording a fake token count.
These are data/output controls, not a final model-window or hard CPU/RAM deadline.

Existing required committed corruption/incomplete history refuses. Preserve
explicitly unavailable imported media from the existing context. Include missing
media for the original source record even when its original turn falls outside
the selected history range. Do not recover omitted bytes from retained history or
claim image availability merely because the text index exists. The frame contains
references/facts, not image bytes or an OCR reconstruction.

All request/history/source records are captured before token/query callbacks. A
callback may change later ordinary heads; the resulting frame must retain its
captured records and may not reread a new winner into the packet or hold selected
admission across callbacks. It remains historical data, not current effect authority.

## Refusals, tests and delivery
Return explicit failures for invalid budget/request/history/association, unavailable
identity/provider/media required by the existing Store, stale/mismatched retrieval
and encoded/token exhaustion. No partial frame or source-less fallback escapes.
Keep diagnostics free of request/history/source text. Neither success nor refusal
writes Ledger/Store/caches or invokes rendering, navigation, service/native/model
operations. Caller callback effects are separate from this read-only API.

Original real Store/Index fixtures must exercise first request and follow-up
reaching another page, wrong current-Buddy document, changed source/extractor/key,
blank explicit no-source with zero queries, origin relation/legacy refusal, exact
Unicode/whitespace/history/corrections, temporal and explicit range selection,
incomplete chronology, unavailable imported media, malicious/mismatched Provider
results, byte escaping and full-token exhaustion, and snapshot replacement during
callbacks. Compare Store hashes/heads across ordinary assembly. Keep Writer's
normalized-source source files and selected Reader/runtime files unchanged.

Run affected conversation/retrieval/adapter fixtures, ordinary non-mock library
check independently of feature-unified tests, fmt and strict Clippy, then required
normal hosted/cross-target checks and independent source/spec review. Complete
only this capability's canonical sync/archive, final pair review and normal
Docs-first/Rust-second delivery. Observe actual-main/tag/small provenance separately;
no additional application archive replay. Broader receiving/model/durable/native
integration remains unfinished; no source image, native or model test is invented.
