# Ordinary Reader follow-up source inheritance

The ordinary Reader follow-up already appends to an admitted conversation and
answers from stored history and verified historical images. Its current input
visit guards that work, but supplies neither an original-document choice nor
fresh whole-document retrieval. This increment connects the existing ordinary
request-evidence preparation to that receiver. It covers the existing bounded
text-bearing PDF profile, the bounded offline EPUB text profile and explicit
no-document. See the existing
[ordinary dispatch](../../specs/ordinary-conversation-dispatch/spec.md),
[declared receiving](../../specs/declared-source-receiving/spec.md) and
[source resolution](../../specs/source-request-resolution/spec.md) contracts.

## Opt-in input and capture

Add an internal source-aware Reader dispatch entry beside
`ConversationDispatch::reader`. Keep its existing `RequestScope`, exact typed
request and optional history range. A trusted input owner supplies the existing
`SourceDirective`: either `Inherit` with an exact earlier request-turn ID and
evidence operation from this conversation, or `Explicit` with an exact
`RequestSource::Original` or `RequestSource::NoDocument`. An original choice
requires a complete independently established PDF or EPUB `IndexKey`, its
matching bounded query provider and a way to revalidate the admitted source
throughout the operation. The owner establishes these from current source material.
Historical evidence and a cache hit alone cannot establish current file identity.
The public receiving and resolver APIs, request-evidence representation and
dispatch without the opt-in retain their existing behavior.

`RequestScope.source` remains the guarded current Buddy-page input visit.
The admitted retrieval origin is a separate fact. Neither the current visit
nor absence of a prior source selects a document or declares no-document.
Do not select a prior operation by timestamp, page or inferred intent. A
deliberate retarget supplies its own validated source turn and record with
corresponding independent key and authority. An inherited no-document decision
requires the named earlier no-document evidence and no index key. Explicit
no-document uses neither an index nor a source provider.

Admit the original operation and append the exact interpreted request to the
existing conversation using its expected root. Prepare one bounded context and
request-evidence packet against the current ordinary Ledger capture. Use the
existing `prepare_request_evidence_with_directive` path with a private strict
inheritance check inside that captured read set. It verifies the same earlier
request and exact retained source record and compares the newly admitted key's
document, format and original-byte SHA-256 with the named evidence's key before
querying. The digest covers the complete original PDF file or EPUB archive.
Independently validated identical original bytes can be reindexed with a
different extractor or normalized digest. The standalone generic resolver
retains its existing independently reindexed same-document semantics.

For a bound PDF or EPUB, query the entire admitted index once using the exact new
request. Prior retrieval results remain historical. A zero-match
result remains associated with the admitted source. Missing, conflicting,
foreign, corrupt or changed evidence, absent source material, invalid key and
same-document changed bytes refuse without a replacement query, model call or
Generated draft. If the interpreted request has already committed, keep it
available for normal history and original-operation reconciliation.

For EPUB, reuse the existing [offline normalizer](../../specs/epub-source-normalization/spec.md)
and exact-key Index. Retrieval uses the declared spine and preserves its
canonical section paths, with no inferred page number. The same host
currentness check guards the admitted original archive independently of the
Buddy-page visit. This composition receives an already admitted source and
does not add an installed file observer or native page-to-section mapping.

## Supplied notebook admission

The proposed host route starts with an existing ordinary format-4 conversation
and its committed `ArchivedNormalizedSource` in `Namespace::Source`. The
original user turn owns that archive. An explicit first Reader question can
name that turn and record, including a Writer origin created by the existing
`Ledger::admit_notebook` path in `src/conversation/notebook/persistence.rs`.
Later questions inherit through the named earlier **Reader** evidence
operation. Retargeting requires its own explicit origin and fresh admission.
Require `SourceFormat::Notebook`, `TextScope::SuppliedNotebook` and unique
positive page locators in supplied order. Refuse section locators, page-scoped
input and partial or unavailable supplied sets.

At the existing `Dispatch::reader_with_source` boundary
(`src/workflow/conversation_dispatch.rs`), require a private admission from
the independent input owner on each request. The owner supplies the ordered
`retrieval::notebook::PageImage` set, the complete existing whole-page
`NotebookText` result, a freshly observed `ValidatedNotebook` and a short
source-currentness check tied to the explicit original or named evidence
operation. Reuse `ValidatedNotebook::from_bytes` for an owned buffer or
`read_document_file` for the existing supported file admission. A Store
archive, cache, bare `NormalizedDocument` or extractor prefix cannot issue
admission. This first route accepts the existing `retrieval::notebook::normalize`
whole-page OCR contract for supplied historical images.

Reuse the input-side checks and hash recipe from `admit_pages` in
`src/retrieval/notebook.rs` without invoking OCR again. For the bounded ordered
set of unique positive pages, compare each derived `ImageIdentity` (page, PNG
SHA-256, byte count and decoded dimensions) to the corresponding
`NotebookText.images` item. Recompute `document.source_sha256` over
`notebook-page-image-set-v1` plus a zero byte, the big-endian u32 page count,
then each big-endian u32 page, big-endian u64 PNG length and exact PNG bytes
in supplied order. Require one normalized unit per image in that order, with
the exact page number and no section. Require `blank_pages` to equal the
ordered page numbers of the empty units. The other units must contain
nonblank text. An unreadable page, partial transcription, or absent or
mismatched complete result refuses.

Require the existing public whole-page `Profile` (protocol 1,
`transcribe-visible-v2`, the declared nonempty model profile and no confirmed
context). Recompute the extractor revision using
`notebook-ocr-unverified-v2:` and the SHA-256 of the existing serialized
`Profile`. Require the entire `NotebookText.document` to equal the document
parsed from the independently supplied normalized JSON, including the source
digest, profile-derived revision and ordered units. Completeness applies to
the declared supplied set. Recognition, blank judgments and the declared model
profile remain unverified. Keep the complete result at admission and carry
the existing revision and digests in durable evidence. Input without this
complete-set OCR contract falls outside the first route.

In captured Ledger preparation (`src/conversation/evidence.rs` and
`src/conversation/resolution.rs`), pin the exact original turn and archive
`RecordRef` and the canonical media descriptor from that captured archive.
After releasing the capture lock, verify the committed canonical object
through `ArchivedNormalizedSource::load` in `src/conversation/notebook.rs`
and compare the fresh input's raw normalized JSON digest and byte count,
canonical media digest and size, document, format, source digest, exact
extractor revision and ordered units digest against the archive. The raw JSON
digest and the historical image-set digest represent separate inputs. Build
the existing `Index` over the independently admitted units. Require its
complete `IndexKey` to match the archive and, for inheritance, the exact
prior key, origin-turn reference and archive reference. Query it once using
the exact new question and existing limits. Preserve page, unit and UTF-8
range, including exact-key zero matches and a source-bound memory scope.

Perform input and archive reads, image and JSON validation, hashing, Index
construction and query outside Store and admission locks. `load` acquires
the Store lock briefly through `Store::read_object`; never call it from a
guard already holding that lock. Check the original request deadline around this bounded work and preserve the existing notebook input/object, image, frame,
passage and prompt bounds. Use only the established short owner-currentness
check and captured generation/head/transaction checks at guarded submission,
result acceptance and output. Reuse the existing deadline and budget
throughout each request.

Use the existing `SourceAssociation::Original`, `RequestEvidence` and
receipt. In `src/conversation/receiving.rs`, admit the archive as retrieval
origin only for the notebook-aware captured follow-up. Structural historical
readback validates the pinned origin, archive identity, media descriptor and
exact key and can report missing media. It can recover the original receipt.
The private fresh path requires the separately admitted source and existing
guarded research, answer and output handoffs. Keep the archive reference and
its media availability even if the origin precedes the selected history range.
In `src/conversation/receiving/images.rs`, the archive's canonical JSON is
text provenance. Only the existing verified capture path supplies PNG
attachments. In `src/conversation/receiving/answer.rs`, keep the source and
page/range in the frozen payload and citations and label OCR passages and
rendered references as unverified historical OCR.

Extend the ordinary source-aware fixture in
`src/simulator/combined/resident.rs` using the ordinary notebook Store
setup and archive producer in `src/simulator/combined/qualification.rs`.
Use the existing normalizer with a scripted whole-page result over three
nonconsecutive supplied pages, including one declared blank. Seed the actual
Writer-owned archive, ask an explicit Reader question, then inherit that
Reader evidence on a different Buddy visit with a history range excluding
the archive's origin. Verify one query per question, a later page and exact
range absent from the first result, preserved source and history, visible
unverified OCR and one Generated per successful operation. Verify an
explicit retarget to another admitted archive.

With the same archive and history, verify structural readback of the original
out-of-range association. The generic fresh receiver and evidence preparation
APIs must refuse that archive as the original even with its exact key and an
Index. The opt-in route must also refuse without independent admission. Check
zero queries/model submissions on refusal and exact PNG attachments from the
existing capture path on success, with zero attachments from canonical JSON.
Refuse changed raw JSON with unchanged units, changed image-set mapping,
changed profile, changed units, partial or missing input, and unavailable
archive media before a query or model submission. Reuse source-drift and
lost-ack cases to verify original receipt recovery without replay, new drafts
or output. Installed acquisition, native authority and live OCR accuracy
require their own evidence.

## Evidence, submission and output

Retain the prepared frame and the bounded media associations derived from the
same capture for the existing follow-up answer assembly. Resolve required
image bytes through the existing verified historical attachment path and
preserve its cumulative bounds and deduplication. The answer receives the exact
request, eligible ordered history, verified associated images and new bounded
passages with their source and page or section identities. Reuse the same frame and media
projection throughout; do not reread history, requery, or infer context from
rendered replies. Scope optional ordinary memory from the admitted retrieval
source. Explicit or inherited no-document runs no document query and names no
document for memory. Preserve eligible global memory and personalization.
The source-only implementation uses the existing plain answer. The researched
continuation below adds default research to the same opt-in entry.

Persist the prepared evidence and original receipt through the existing
captured conditional transaction. For an answering attempt require a definite
fresh publication and exact readback. Carry forward only the root revision
identified by that successful acknowledgment, after confirming it is still
the unique current root and the interpreted user revision is unchanged.
A replayable original receipt or an arbitrary current root in historical
readback cannot renew admission. The private publication return must distinguish
fresh success from historical recovery after a replay, race or uncertain
write, while preserving public evidence retry behavior. On uncertain or stale
publication, stop. Historical recovery can inspect or acknowledge only the
original operation and may not rerun retrieval, model submission or output.
Treat an uncertain request append or Generated publication with the same
original-operation discipline.

Keep a bounded in-process admission for the same Store generation, conversation,
current root, exact user, newly saved evidence and receipt, named anchor and
admitted original source. Revalidate those exact references and the current
input visit before handing off the model request. The opt-in path uses the
existing owned `LLMEngine` handoff for actual submission. Check the guarded
identities at that boundary and use progress/completion checks to revoke the
same attempt if currentness changes while waiting. Refuse an adapter without
the required handoff. The Store's conditional check covers exact persisted
references. The live owner rechecks the visit and source at bounded observation
points; these checks cannot freeze a separate native or filesystem owner.
Keep retrieval, image validation and provider response waits outside Store
locks. No result from a failed ownership check can enter Generated.

Carry the same admission into the conditional Generated write and rebind its
root to the exact new acknowledgment for the existing output-owner path. Keep
the immutable input visit and source association pinned when rechecking the
draft revision and admitting or recording its verified result. The guard may
recheck exact identities or pinned bytes; it must not rebuild context or select
a successor. Publication uncertainty does not convey output authority.

## Research in the same source-aware follow-up

Extend `Dispatch::reader_with_source` after its definite fresh evidence
acknowledgment. Use the researched composition in place of the opt-in plain
answer. Keep ordinary dispatch without source-aware opt-in and the standalone
historical APIs compatible. The router continues passing the exact question and
history. It does not select a research backend or run an additional model.

The trusted typed-input owner supplies the existing `ResearchDirective`
through the private dispatch input, bound to this operation, input visit and
exact current question bytes. The dispatcher checks that pairing before the
request append. This is in-process admission, with no new persisted record.
`UsePolicy` means the owner admitted the question without an explicit web
restriction. `NoInternet` requires an explicit denial in that same user's
request. Keep the denial in the question text. Missing, ambiguous or
mismatched intent refuses before web acquisition. The receiver does not infer
the directive from prior turns, printed or quoted text, retrieved material or
an answer proposal. Use existing input ownership and no new gesture. The
hosted fixture supplies the admitted directive. Installed typed or handwritten
input still needs an owner that can establish it for the current question.

Freeze `Config::research_policy_snapshot()` from the admitted configuration.
Absent or null is Required. Explicit NoInternet takes precedence over either
saved policy. NoInternet and configured Disabled retain their distinct reasons,
skip search selection and credential resolution, and construct no search
adapter. Each may still invoke the authorized answering engine with the local
context. Revocation of the original input or configuration admission stops the
attempt without replacing the directive or captured policy.

Use the single prepared frame and `FrozenRequestContext::with_memory` with
the existing admitted `LocalMemory`, profile and request time, or Disabled.
Keep the current ordinary validation, including refusal of unusable partial
memory and selected results. Scope the one memory query from the admitted
document and retain eligible global memory for no-document. Freeze that
observation for both stages. Resolve the existing verified image attachments
and their associations from the same prepared data before either network
stage. Do not reread history or repeat source or memory retrieval.

Compose `FrozenSourceMemoryContext::with_research` once. For Required, the
trusted host supplies the existing qualified search selection for this request
and one original deadline. Reuse the existing qualified OpenAI Responses
destination and credential admission, adapting its private selection helper
where necessary. The selected-only `reader.researched_pdf` setting does not
enable the ordinary route. Question text, renderer input and historical
evidence cannot choose the model, endpoint or credential. Resolve the search
selection and construct `OpenAIWebResearch::with_guarded_dispatch` only when
the original directive and policy require it. The current web adapter receives
the complete frozen source/memory context as text. Verified image bytes remain
with the answering stage. Missing or incompatible selection, unavailable or
invalid results, timeout and cancellation refuse before answer. CompleteEmpty
requires actual completed search witnesses. Any admitted partial result keeps
its diagnostic and unverified provenance.

Reuse `answer_guarded` and its existing structured citation validator through
a private attachment-aware entry. Preserve the standalone text-only prompt and
its digest contract. The composed answer receives stable instructions for the
attachment-aware variant, the exact frozen researched JSON, personalization,
and the verified historical image associations and image parts in known order.
Apply the complete prompt bound and caller count to the ordered content,
including attachment descriptors and image parts. Use the existing engine
content representation for the count and digest so they describe the actual
admitted content before submission.
Exhaustion refuses without dropping evidence. Reuse the existing S/M/R
validation and reference rendering for PDF pages, EPUB sections, associative
memory and provider-asserted research URLs. Distinguish useful citations from
verified truth. Save the bounded validated answer and rendered references in
one Generated draft.

Required research and answering each own one guarded submission within the
original deadline. The handoffs use the same exact input visit, source and
captured Store generation, root, user, evidence, receipt and anchor as the
ordinary follow-up. Recheck those identities during progress and before
accepting each result. Join owned cancellation before release. Stale
admission, a failed required search, malformed answer or citation, or uncertain
publication cannot yield a new output effect. A failed model, provider or
ownership check cannot yield a Generated draft. Only the exact Generated
acknowledgment may rebind the root for the existing output owner. Historical
reconciliation may inspect only the original receipt and does not recreate
either provider request.

Add one hosted group at the existing ordinary receiver seam. Confirm a
default-required loopback search sees the exact frozen question, history,
source and ordinary memory, then a guarded structured answer receives the
same data plus verified images and produces one Generated with validated
references. Cover explicit NoInternet and saved Disabled with zero search
adapter construction or calls, including a missing search selection. Cover
absent or unqualified Required acquisition, a failed or withheld search,
invalid citations and one guarded drift with no offline answer, Generated
draft or replay where applicable. Keep existing provenance, publication and
ordinary compatibility controls. Scripted input or answer peers and loopback
research establish host composition. Installed source and question ownership,
live-provider behavior and selected resumption remain separate.

## Hosted verification

Extend one existing ordinary simulator or qualification path with the actual
Ledger, dispatch, receiver and guarded adapter. Use the existing fixture seams
with independently provided source identities and keep source-open/currentness
observations labeled modeled. Assert the following:

- A named earlier PDF request on an existing conversation supplies exact
  history and verified image bytes even when the current Buddy input page is
  different. The exact new question queries once and finds a locator outside
  the earlier passage set. A second follow-up names the first follow-up
  evidence, uses another fresh query and keeps the original source identity.
- Identical original bytes with an independently validated new index key
  succeed. Changed bytes at the same document ID refuse before any query or
  model call and produce no Generated result. An explicit retarget queries the
  newly named exact origin, retains its own locator and leaves earlier evidence
  intact. A valid zero-match query remains bound to its named source.
- Add one EPUB composition using the existing ordinary fixture seam and an
  authored EPUB input through the existing normalizer and Index. A new
  question on a different Buddy input visit makes one query and retrieves an
  exact spine section outside the prior result, with no page number. Preserve
  the exact origin and history. Admit an independently validated reindex only
  for the same archive bytes. A same-document archive change refuses before
  retrieval or model submission, even if extracted text is unchanged. Reuse
  the existing source callback for one modeled currentness-loss refusal.
  Existing normalization and bounds fixtures retain their coverage.
- Explicit or inherited no-document makes zero document queries and has no
  document memory scope. Eligible global memory and the exact history remain.
- Missing or conflicting named evidence refuses. A change before evidence
  commit, at actual submission, or before Generated prevents new downstream
  work at that boundary. An uncertain evidence publication preserves the
  original receipt if committed, produces no draft, and cannot trigger another
  query, model call or output on historical readback.

The existing selected route still creates a fresh root. Installed selected
resumption needs its own verified current Buddy conversation binding and durable
retrieval-source identity. This ordinary increment does not supply those facts.
