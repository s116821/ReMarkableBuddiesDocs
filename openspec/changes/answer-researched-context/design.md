# Answering an explicitly frozen researched request

## Current gap and ownership
Actual Source main9be8871 exposes FrozenResearchContext with getters for complete
encoded historical context, source/memory reports and research. No production
answer consumer references it. workflow::orchestrator::analyze_and_answer still
clears the engine and supplies ANALYSIS_PROMPT/current-page images. Its proposed
answer is unrelated to the declared source/memory/research assembly APIs.

LLMEngine in src/llm/mod.rs exposes clear_content, add_text_content,
add_image_content and execute(_with_progress). It has no system-role method.
Its default progress implementation calls once before blocking execute; generic
engines therefore do not promise interruptible waits. The existing OpenAI engine
owns its transport/worker, a90-second default timeout,10MiB response cap and
max_completion_tokens4000. This change does not rewrite that transport or infer
one HTTP request from one arbitrary engine invocation.

Current public held PR37 owns selected Reader/memory/workflow admission; PR50
owns Reader cancellation/OpenAI/runtime changes. Do not edit, rebase or merge
those candidates or their implementation bodies. Add a separate ordinary module
conversation::receiving::answer with a single module declaration in receiving.rs.
Keep LLMEngine/OpenAI, workflow/main, all source/memory/research wire shapes,
configuration, selected/native and Manager code unchanged.

The thin router requirement preserves the current request/history verbatim.
Stable instructions belong to this receiving buddy, above the SDK, without fake
history turns or modifying the captured request. Separate text content is not a
separate system/developer protocol role. No role-priority/security guarantee is
inferred from the existing trait.

## Explicit call and complete prompt budget
Expose answer(context:&FrozenResearchContext, engine:&mut dyn LLMEngine,
options:AnswerOptions, token_count, progress)->Result<AnswerDraft>. Neither
constructor, environment/config lookup, discovery nor automatic runtime caller is
added. The maintained example is an actual explicit caller.

AnswerOptions declares complete input text-parts bytes (1..1MiB), positive caller
token allowance, raw returned text bytes (1..64KiB), answer text bytes
(1..16KiB), citations (0..32) and complete result bytes (1..128KiB), with finite
defaults within those bounds. Invalid/unknown/excess limits and zero positive-only
limits refuse; a zero citation allowance is valid. A raw limit
may be lower than valid output and honestly refuse. These bounds do not configure
an arbitrary engine's network transport, output tokens or model context window.

Build exactly two ordered text parts:
1. Stable fixed buddy-owned instructions defining evidence interpretation,
   disagreement/uncertainty handling and the exact response/citation grammar.
2. The complete exact context.encoded_json(), byte-identical; no summary,
   request/history rewriting, truncation, selected evidence dropping, image reload
   or provider/retrieval/memory reacquisition.

Bound serialization of the full ordered [{type:"text",text:...},...] descriptor
with a capped writer before dispatch, including fixed instructions and JSON
escaping. Run the caller counter once on that complete descriptor and require a
positive admitted count. Never sum earlier component counts or assume monotonicity.
The descriptor describes the declared text content, not an arbitrary engine's
complete HTTP/model protocol overhead. Preserve this distinction in reports.

After preflight/progress admission, clear owned engine state as described below,
add the two text parts without images and invoke execute_with_progress exactly
once. No retries, second-call repair, model substitution or empty answer fallback
are added by this layer. The engine's own transport behavior remains its contract.

## Engine content ownership and progress
The function exclusively borrows the engine for the call. Establish a scope guard
before option/count/callback work; clear preexisting text/images at entry. Clear
again on every normal success/refusal/error and during unwinding from counter,
callback, engine execution or parsing/allocation panic, so later ordinary reuse
does not inherit the previous prompt. Never restore a prior prompt: it is not an
owned session history. This relies on clear_content implementing its documented
operation without panicking; the trait cannot prove physical/remote erasure or
the behavior of a malicious/shared custom engine. Do not catch a panic and return
successful content, and do not promise cleanup if the engine's cleanup itself
panics. No new unsafe code or detached work.

Finite callback phases: BeforeDispatch after prompt budgets but before adding
content; EngineProgress whenever the selected engine invokes its callback;
AfterResponse after engine return; BeforeReturn after output admission. A callback
error is latched, so an engine that ignores it cannot yield admitted success.
Counter/engine/progress errors expose finite sanitized failure labels, not raw
context, provider bodies, paths or credentials. Panic propagates with the guard.
Late callback failure suppresses the draft. No callback runs after return.

The generic boundary cannot preempt an engine that blocks or never polls and
does not independently own or join its worker. Existing OpenAI loopback controls
must separately establish its real cancellation/owned cleanup behavior at this
call seam. No local return implies remote rollback, currentness or billing undo.

## Strict generated output and captured citation references
Instructions request one JSON object with exactly:
{status:"answered"|"clarification", text:string, citations:[string,...]}.
Clarification means a nonempty user-facing clarification request, not an answer;
its citation array must be empty. Both statuses require bounded nonblank text,
without controls except CR/LF/tab. Empty/NONE/free-text/fenced/extra-field/duplicate-
key/malformed output refuses. Bound the raw returned String before strict parsing;
this is admission after the engine returns, not a promise about its peak memory.

Citation IDs are one-based exact ASCII S1/S2..., M1/M2..., R1/R2..., without zero,
leading zeros, signs or aliases. S indexes captured retrieval.passages in order;
M indexes captured memory.context.facts; R indexes captured research.sources.
An ID must resolve within the corresponding captured array. No-source/disabled/
empty arrays provide no references. Repeated response IDs refuse. The text uses
matching inline markers [S1], [M1], [R1]. Reserved uppercase S/M/R marker forms
must be well-formed and resolve; the distinct marker set must exactly equal the
citations array set. Repeating a valid marker in text is allowed. Other prose/math
brackets are not citations. No model-provided URL/title/locator is accepted as
citation metadata. An answered result may have no citations; code cannot prove
which facts the model used. Instructions require citing relied-on evidence and
identifying relevant disagreements, but those semantic properties require actual
qualification and remain unverified model assertions.

Resolve IDs locally to bounded metadata from the captured context only:
- Source: complete original IndexKey/document identity plus unit/page/section and
  half-open normalized UTF8 range; label declared historical source text, not
  rendered glyph/current source proof.
- Memory: record/revision and existing provenance/basis, preserving associative
  author-asserted/not-source-verified attribution; never upgrade confidence.
- Research: original URL/title and Synthetic/ProviderAsserted basis, explicitly
  unverified. Generated summaries remain summaries, not fetched quotations.

AnswerDraft retains conversation/request IDs, SHA256 of exact frozen context,
status/text/resolved citation records and the declared whole-prompt count/basis.
Bound its complete encoded result before returning. It is transient generated
historical answer data, not a durable turn, selected request, currentness receipt,
truth verification or native effect authority. No automatic logging/persistence.
Caller presentation may render captured research URLs as clickable citations;
this scope supplies metadata and a maintained JSON caller, not a tablet UI.

## Qualification and actual caller
Extend actual Store/Ledger/Index/LocalMemory/saved-policy fixture composition to
this real answer boundary. Cover unchanged Unicode/whitespace request/history,
changed/absent source, empty/partial/disabled research/memory, unfamiliar citation
IDs, missing/duplicate/malformed markers, strict JSON/size/count bounds, failing
and nonmonotonic counters, provider error and callback error/panic/ignored-error
cleanup. Reuse one engine with old text/images to prove entry/exit clearing and
no prompt bleed. Invalid preflight must invoke no engine; admitted calls invoke
it exactly once; no Store/object heads are written by the answer boundary.

Actual existing OpenAI loopback must inspect its sent messages/content: two exact
text parts, no old images/history, unchanged model/endpoint behavior. Use withheld
headers/body and exact request/partial-write witnesses for cancellation; retain
bounded local return and joined transport/server cleanup. Do not relabel scripted
LLM results as actual HTTP or hosted evidence. No old production transport edit.

Add a maintained development example that actually constructs the existing frozen
context, invokes this function with existing OpenAI, and privately records the
admitted draft, context/prompt/response digests and finite engine-call count.
An example-only engine wrapper may retain bounded returned model text for private
diagnosis even if later strict output admission refuses; that is not a successful
draft receipt. Capture no HTTP error body, header, credential or automatic log.
The call count means engine invocations, not arbitrary transport retry/billing
guarantees. No new production observation surface is needed.
Explicit --live, new absolute private output, public authored fixture only,
<=90s configured development timeout, one model invocation maximum. Current-
directory protected dotenv is loaded only inside the example using the approved
existing setup; no key argument/log/search/copy. A nondefault configured base must
refuse without an explicit admitted --base-url; validate HTTPS host-only base or
numeric loopback fixture base before the existing engine appends its path.

The representative new hosted answer case compares an authored SI-mole source,
an explicitly stale authored associative note and synthetic attributed research
about the fixed Avogadro value. Preserve all three labels and original history.
Check strict status/citation correspondence plus stable expected numerical facts
and acknowledgement of the discrepant note. Record actual response and limitations
privately. Synthetic research is explicitly synthetic; this qualifies answering,
not another hosted acquisition. No replay of the closed v0.43 acquisition request.
No retry/fallback/model replacement after refusal; retain the result and report
the concrete gate. Development credentials/presence do not imply model success.

Qualify exact local/default/affected integration/Clippy/example controls and actual
hosted answering, independent implementation acceptance, owned sync/archive/final
review, normal Docs-first squash delivery and distinct actual-main/publication
closeout. Do not reopen old releases or imply installed runtime/native acceptance.
