# Historical source-plus-memory data boundary

## Ownership and compatibility

The existing source receiver owns the immutable schema-1 ordinary-historical
request frame. Memory owns its existing Query/Provider/Fact/ContextData semantics.
This addition combines those data products without copying the held model answer
wrapper or Reader runtime integration. No source association is rediscovered,
Ledger reread, retrieval repeated, record written, configuration discovered or
current selected admission acquired. Existing methods, errors, persisted evidence
and replay equality remain unchanged. Ordinary mode/data lifetime guards are not
reinterpreted as a selected or native lease.

## Proposed public API

Expose a receiving child module `memory` with:

- `CombinedBudget { max_encoded_bytes: usize, max_tokens: usize }` (512..=524288
  encoded bytes; positive known token allowance).
- `MemoryOptions { now_ms, current_claims, max_matches, max_context_bytes }`, using
  existing memory query bounds (64 canonical claims, 1..=16 matches, 256..=16384
  context bytes). Claim assertions are explicit caller input; do not infer them
  from question, source text or provenance UUIDs.
- `MemoryInput::Disabled` or `Query { provider: &dyn memory::Provider,
  profile: Uuid, options: MemoryOptions }`. Enabled profile must be explicit/nonnil.
- `FrozenRequestContext::with_memory(self, input, budget, token_count)` returns an
  immutable `FrozenSourceMemoryContext`, with getters for original source context,
  optional query/report, stable complete encoded JSON and caller token count.

The new transient wrapper is schema 1, scope `ordinary-historical`, with
`request_context` containing the existing typed frame unchanged and `memory`
containing a disabled marker or an ordinary query/report. Original
`source_context().encoded_json()` stays byte-identical. The wrapper adds no
instructions, answer policy, effects or conversation turns. No Deserialize/Clone
or writable preparation is exposed for the combined frozen object.

## Query and result rules

Derive Query.text byte-for-byte from the frozen interpreted request and
Query.document from its original IndexKey, or None for explicit NoDocument.
Enabled composition SHALL refuse with a typed incompatible-request outcome when
the exact question exceeds the memory Query's 2048-byte bound (or otherwise fails
that existing validator). A larger no-document source frame remains valid for the
existing source-only API; never shorten or rewrite it to fit memory.
Never use a visible Buddy page, history text, cached memory or adapter output to
choose scope. Pass explicit caller time/claims/limits without rewriting them.
Disabled makes zero memory calls and requires no profile/provider. Enabled makes
one query after input and minimum complete-frame preflight; do not retry.

Accept CompleteEmpty, Complete and Partial only when their structure is
consistent. Preserve diagnostics, including withheld conflicts and omissions,
and author-asserted provenance labels. Reject unavailable/disabled enabled-query
results, selected-pinned results, malformed labels/status, wrong profile/document,
invalid Fact/record/revision identity, duplicate records/claims, expired or
explicitly suppressed facts, count/context overflows and contradictory status.
Provider relevance/conflict completeness and asserted provenance are its contract;
structural validation cannot prove truth or discover omitted facts. Error messages
must not expose query/memory/provider/path contents or nested error chains.
Reuse the existing memory Query and Fact validation, not another query schema or
ranking/suppression algorithm. Before cloning/encoding returned context, check
fact count, exact labels and each existing bounded Fact plus record/revision IDs.
An oversized custom-provider result must refuse before unbounded serialization.
Status consistency includes snapshot-unavailable refusal and the existing rule:
conflict/contradiction/unsupported/budget omissions imply Partial; expired and
suppressed counts alone do not. Complete requires nonempty facts, CompleteEmpty
requires no facts; Partial may be empty without becoming CompleteEmpty.

A future receiving consumer can retain this wrapper's unchanged source context
and separately typed memory report rather than reconstructing history or adopting
another answer policy. Wiring that consumer to a model remains the held runtime
integration with its live validation, not part of this operation.

## Complete bounds and historical qualification

Validate all options and the positive token allowance before querying. Serialize
a proven encoded-byte lower-bound wrapper (`memory:null`, strictly smaller than
either real memory report) before the query so an impossible byte allowance
refuses without calling the provider. Do not call the token counter on this
placeholder: caller token counts need not be monotonic when content is added.
Use the existing capped serializer for complete final JSON, including escaping,
query identity, source metadata, diagnostic numbers and labels. Count the entire
final wrapper once using the supplied counter, with no placeholder token rejection,
count reuse or sum assumption. Zero/failed counter or exhausted bounds
refuse without partial output, truncation or empty fallback. An adapter may return
caller-allocated objects; output bounds do not promise acquisition allocation,
elapsed-time, process RAM or a model tokenizer/window guarantee.

Query/counter callbacks can change Store state; the source frame remains captured
historical data. Returned memory is a historical query observation at the supplied
time, not an atomic source-memory snapshot, verified document evidence or a lease
for later publication. The combined object cannot be persisted through the existing
request-evidence API and grants no model/selected/native execution authority.

## Verification

Real temporary Store/Index/LocalMemory tests cover bound source and no-document,
exact Unicode request/history/source bytes, global/document/profile isolation,
disabled zero-call, empty/partial/conflict/expiry/current-claim behavior, exact
encoded/token boundaries and restart. Injected adapters cover malformed/error/
selected results and callback changes, proving no source reread/query or writes by
assembly. A non-monotonic counter regression admits a valid completed encoding
even when a hypothetical placeholder would receive a larger count. Existing
source, evidence and memory suites remain controls. No prompt,
model, SDK, dependency, settings or device changes; existing live/native gates stay
open. Independent reviewer checks scope and exact final revisions before delivery.
