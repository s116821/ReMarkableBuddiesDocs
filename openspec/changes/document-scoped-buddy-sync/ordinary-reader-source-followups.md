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
Notebook sources remain outside this admission.

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
document for memory. Preserve eligible global memory, existing personalization
and the receiver's existing research behavior. This increment adds no internet
dispatch or research-policy change.

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
