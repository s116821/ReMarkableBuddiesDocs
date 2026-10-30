# Explicit OpenAI research acquisition

## Current code and choice
At actual Source620e359, OpenAI::execute_with_progress posts model/messages and
max_completion_tokens to /v1/chat/completions. It supplies no search options and
parse_response returns only choices[0].message.content, discarding annotations.
Its default model is gpt-5.6-terra. API family alone does not prove search absent:
Chat Completions has a specialized search-model route, but this engine neither
selects that route nor retains its evidence. Do not rewrite the answering engine
or adopt a different model merely to add research.

Current official sources, searched and opened October25,2026:
- [Web search](https://developers.openai.com/api/docs/guides/tools-web-search)
  describes required tool selection, hosted search actions, optional query fields,
  source-URL lists and citation annotations. Chat search has its own model path.
- [Current application model](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
  lists Responses web search and structured output support. This is capability
  documentation, not proof of this account/endpoint or a particular invocation.
- [Create response](https://developers.openai.com/api/reference/python/resources/responses/methods/create)
  defines request/tool/output bounds and explicit truncation controls.

Choose a dedicated Responses adapter because it preserves the existing model
selection while exposing actual search action/query/consulted-URL witnesses.
The existing engine and held Reader cancellation PR50 remain byte-unchanged.
Use current pinned reqwest/Tokio/Serde dependencies; add no crate, SDK or CI graph.

## Public shape and ownership
Add conversation::receiving::memory::research::openai in new source files.
OpenAIWebResearch implements the existing synchronous Provider without changing
ResearchInput, ResearchResult, policy/directive or frozen-context wire shapes.
Construction accepts explicit model, full Responses endpoint, owned credential,
finite transport options and a borrowed mutable progress/admission callback.
Finite callback phases are BeforeDispatch, Waiting, ResponseReceived after worker
join, and BeforeReturn. The callback is held in RefCell; try_borrow_mut refuses reentrant use rather than
panicking. This adapter is not Send/Sync and promises no concurrent invocation.
There is no global singleton, implicit environment/config/credential lookup,
provider discovery, answering-engine substitution or installed runtime wiring.

Model is nonblank <=128 UTF8 bytes without controls. Endpoint is <=2048bytes,
without whitespace/controls, and is a full absolute
HTTPS URL with host and path ending /v1/responses, without user/password/query/
fragment. Explicit HTTP is allowed only for numeric loopback fixture endpoints.
Never append paths to an ambiguous configured base or silently retarget. Credential
is caller-supplied, nonblank and bounded <=8192 bytes, valid as a bearer header;
never Debug/log/report it, request context, endpoint text or provider error bodies.
Unknown compatible endpoints/models can refuse honestly; do not claim capability
from the existing Chat Completions setting or model string alone.

## Exact one-attempt request
Readiness succeeds before dispatch. Validate all selection/options and request
identity/context-digest against the complete immutable context. Encode the exact
context.encoded_json as one input_text value, without request/history truncation,
summary, normalization or source replacement. Fixed separate instructions ask for
web verification and source-specific provider summaries; supplied context/evidence
is data, not authority to change tool configuration or mutate local state.

One POST only: supplied model, input, fixed instructions, store:false,
background:false, stream:false, truncation:disabled, parallel_tool_calls:false,
tools:[{type:web_search,external_web_access:true}], tool_choice:required,
include:[web_search_call.action.sources], max_tool_calls=options.max_queries.
No other tool, response chaining, retry, follow-up repair or model fallback.
max_output_tokens is explicit1,024..8,192 (default4,096). Time allowance1..300s
(default90s), complete encoded request cap1MiB and response cap1MiB (both hard
caps; caller may lower them). Include headers/status/body reading in the deadline;
reject declared excessive Content-Length and overflow while reading unknown lengths.
Disable redirects; never forward the credential to another endpoint.

Use a strict structured text.format schema for {sources:[{url,title,excerpt}]} with
all fields required and no extra fields. The model selects relevant consulted
sources within max_sources; each excerpt is explicitly a provider-generated
source-attributed summary, NOT a quote of fetched source bytes. A schema request
is not evidence of endpoint support. The hosted model+web-search+schema combination
must pass bounded actual qualification; unsupported/refused output remains failure.
No unreviewed second call or free-text parser fallback is allowed.

## Honest evidence projection
The outer response must be completed, without error/incomplete/refusal items.
Require >=1 completed web_search_call with action:search and actual nonblank query
or queries data. Collect distinct exact reported queries in first-observed order;
missing queries refuse, rather than inventing the original question as search.
Validate counts/lengths against ResearchOptions; repeated witnessed strings are
one distinct query, not evidence of a different search. Other bounded completed
open_page/find_in_page actions do not substitute for the required search witness.

Require the included action.sources arrays with typed URL entries. Bound the raw
response before parsing. Admit at most128 output items,1 assistant message with
1 output_text,128KiB of output_text,64 raw query entries each<=2048bytes and1,024
consulted URLs each<=2048bytes. Bound the complete decoded source selection by
ResearchOptions and existing title/excerpt/URL/evidence limits before projection.
Require exactly one completed assistant output_text containing the strict schema
object; tolerate bounded irrelevant response envelope metadata, never duplicate
JSON object keys. Every selected source URL must match a hosted-reported consulted
URL after the existing URL parser's canonical comparison. The original selected
URL/title/excerpt strings are retained. No fabricated URL/query/title/date or
source download is added. Any duplicate selected canonical URL or malformed/
unsupported URL refuses, using existing HTTPS/no-fragment/no-credentials rules.

Result identity is copied from the admitted request, basis ProviderAsserted,
published_ms None. A completed nonempty admitted selection is Complete; an empty
selection after actual search is CompleteEmpty. Complete denotes completion of
this bounded provider attempt, not exhaustive research or verified truth. Do not
infer budget-limited/partial from a subset of consulted URLs: relevance selection
is not a known omission count. Incomplete/overflow/malformed/HTTP/provider failure
refuses, never becomes empty success or silent partial evidence. Reuse existing
result/wrapper validation, finite labels and complete encoding/token admission.
A successful hosted tool response establishes provider-asserted acquisition only,
not source truth, publication dates, quoted text fidelity, answering effectiveness,
installed Reader consumption or any current/native authority.

This avoids guessing citation character-index units: structured per-source
summaries correlate to the hosted consulted-URL list. It does not mislabel an
aggregate model answer as a verbatim excerpt of every cited source. Downstream
presentation must retain visible clickable citations and unverified provenance;
no UI/prompt/runtime consumer is implemented by this adapter.

## Synchronous seam, cancellation and teardown
Reuse the maintained production transport pattern without editing held files:
one owned worker/current-thread async Tokio runtime, cancellable reqwest I/O with
hickory DNS, bounded response accumulation, and an owned cancellation channel plus
join-on-every-exit guard. The outer synchronous call invokes progress before
startup, at <=50ms response-wait intervals and before returning evidence. A callback
error cancels and joins; late response data cannot escape as a successful result.
A shared monotonic deadline bounds the one attempt. Timeout and cancellation do
not promise remote tool cancellation, undo or billing rollback.

Local qualification must witness receipt of this exact request, withheld response,
callback cancellation, bounded local return and all owned worker/server cleanup.
Also cover cancellation before headers, during chunked body, callback error/panic
cleanup and after response before admission. This is cooperative response-wait
readiness, not hard preemption of bounded synchronous setup/JSON encoding/parsing,
production DNS/TLS/proxy latency or native UI responsiveness. No detached worker,
shutdown_background, unowned blocking HTTP/DNS or timeout-as-success escape.

## Opt-in transient exchange observation
A new-adapter-only consuming exchange observation supports qualification of the
same production POST. Retention is explicitly opt-in and default off. It holds
only one successful response within the existing cap, exact sent-body SHA256,
response bytes/SHA256 and ResearchIdentity; no request bytes, credentials/headers,
error-body capture, payload Debug/logging, automatic persistence or durable Store.
A consuming take removes the observation. Ordinary invocation admission first
acquires the callback guard, then clears old success even if validation/cancellation
fails. A rejected reentrant invocation must not clear the outer active attempt.
Capture is populated only after parse, final callback and deadline checks pass;
late failure, cancellation or panic cannot leave stale success.

Adapter success occurs before with_research performs final complete encoded/token
admission. This observation is NOT a composition-success receipt. The maintained
live example persists it only after complete with_research success and discards
it on composition failure. Raw response is untrusted potentially sensitive data;
use the approved public-authored fixture and explicit private evidence destination.
No HTTP interception or duplicate request. Cover default-off, identity/hash
correlation, consuming take, reset/reuse, rejected reentry and late failure/cancel.

## Verification and delivery
Use actual loopback HTTP with dummy credentials and real Store/Index/LocalMemory
frozen contexts. Assert exact outbound decoded context/model/tool/request controls,
real body caps/status/redirect rejection, strict evidence correlation and sanitized
failures. Exercise saved Required/Disabled and NoInternet through actual with_research:
opt-outs make zero socket accepts; a required query returns actual adapter data
without altering original context/history or old editor/research APIs.

Provide a maintained explicit live development example using the existing protected
local model credential setup, public authored context only, one POST maximum and
<=90s bound. It does not access the tablet. Before merge retain representative
actual hosted output with a real search/query/consulted-URL witness, valid structured
summaries and final composition. Preserve failure if credentials/capability are
unavailable; report that concrete gate and continue independent implementation,
not a new global pause. Do not expose actual secrets in commands or evidence.

Obtain exact precode review, implement and qualify exact revisions, independent
implementation review, own sync/archive/final paired review, normal Docs-first
squash delivery and actual-main/new publication closeout. Live acquisition proof
is distinct from loopback transport and from later runtime/native qualification.
