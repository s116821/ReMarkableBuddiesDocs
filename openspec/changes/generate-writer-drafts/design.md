# Design

## Existing source and decisions

Inspected ordinary baseline cc317ff and prepared-export production5a1e0f88,
test repair65481cda and docs-link0b935880; central baseline6f7f1d4 and scoped
prepared-export archive14f5600. Actual current issue description and all accessible
timestamped comments were read. Remote Writer/generation/refinement branches and
open PRs were checked; no existing matching implementation was found. Historical
native/selected work stays in its existing checkouts.

Reuse retrieval::NormalizedDocument validation, source ordering/location/digests,
LLMEngine/OpenAI progress/cancellation, existing Config/PersonalizationSnapshot,
Ledger receipt/expected-head/fresh-publication patterns and Store objects. Do not
reimplement OCR, extraction, model HTTP transport or Mem export. Therefore the
prior-art ingestion/OCR survey is not repeated for mechanics not implemented here.

## Source records and compatibility

Add one immutable normalized-text source variant in the existing Source namespace,
linked to conversation/turn. Preserve document identity, format, adapter-asserted
original digest, extractor revision and exact ordered units; store a digest-bound
serialized object using existing required-object publication if needed. The small
consumer uses the existing immutable envelope payload directly: encoded document/
guidance is at most 40 KiB and its record at most 48 KiB, so no extra object is
needed. Validate content before model dispatch and after reopen. Do not pretend normalized text
is retained original bytes, a screenshot or a native observation. No synthetic
capture facts or extra identity registry.

Source-domain2 is explicitly admitted alongside existing ExportAssociation2;
other namespaces remain1, outer format stays1. Ledger schema/payload matching
rejects old-shaped Source2 and new-shaped Source1. Existing source/turn shapes and
ordinary Reader context behavior stay unchanged. Context carries the new linked
source facts without promoting Generated drafts into completed visible turns.

## Request and draft flow

One bounded command consumes JSON from stdin, with separate generate, refine and
prepare-export operations. Credentials remain environment/protected references;
no token argument or routine content logs. Validate input, Store ownership,
source/history limits and expected heads before any provider call. Installed
Reader/Writer mode admission remains a separate existing integration lane.
The command does not start device input, native rendering, sync or Reader.

Generation preserves the exact supplied request in an Interpreted Writer user
turn. Explicit guidance is separate data, never inferred from ordinary notes.
Trusted task instructions, immutable personalization, verbatim eligible history,
request and source/guidance data remain distinguishable in the model payload.
Source order/locations and original/normalized digests bind the draft provenance.
The provider proposes title/Markdown; malformed/empty/oversized output refuses.
Prompt separation is not a proof that a model obeyed source instructions.

Refinement names one unique existing Writer Generated draft and its original
source. It uses the same conversation and preserves every eligible request/history
turn exactly, plus the explicitly selected draft artifact. Do not widen ordinary
Ledger history to treat all unrendered Generated drafts as visible Completed
answers. New refinements are new immutable user/draft turns; no prior text edit.
Optional correction target records can refer to the selected draft; shared
personalization learning remains later work.

Draft completion means durable Outcome::Generated only. Outcome::Completed keeps
its existing native-verification requirement. Explicit prepare-export selects a
current unambiguous draft/source, validates the supplied stable correlation and
new effect UUID, and returns the existing PreparedNote without sending it. It
cannot turn a historical draft into fresh native permission or automatic export.
PreparedNote source scope is stable document identity plus the explicit page or
supplied-notebook selection, independent of turn/source-content identity. New
generation with changed source content retains that logical export scope while
advancing the digest-bound source/draft revision, permitting deliberate same-note
re-export through the existing stable correlation.

## Bounds and full-source coverage

Use explicit encoded input/output/source/history limits before dispatch; provider
capacity remains a separate receiving-provider constraint. Page scope selects
all supplied units matching exactly the named page; notebook scope selects all
supplied units in their given order. Reject empty/ambiguous selections. State
that all-supplied-units coverage does not prove the original notebook was fully
extracted. Do not claim scope completeness from relevance-ranked retrieval hits.
Oversized complete source/history returns selection-required/too-large with no
model call; chunked notebook generation/reduction is a later tracked requirement.

## Lifecycle and errors

One narrow same-Store in-memory owner spans prepare, provider and publication,
shared by all Ledger instances. No Store index mutex spans HTTP. Persist the
prepared operation with an exact fingerprint before dispatch. Only this
invocation's positively fresh publication can invoke the provider; replay,
concurrent winner or lost preparation acknowledgment returns historical/pending
without another paid call. A deliberately repeated operation uses a new UUID.
Capture the expected conversation root before reading selected draft/history,
so a concurrent append cannot be implicitly accepted after assembling older
input. Preparation compares the exact cached selected Turn with its current
value before protecting that revision; guarding a newer draft while sending an
older cached body is forbidden. Receipt intent remains stable across normal
replays, while fresh preparation still requires current compare-and-swap heads.

Once provider dispatch may have occurred, cancellation/failure does not claim
the call was unbilled. Existing progress cancellation must stop waiting and
suppress late replies. A crash after dispatch before durable result does not
authorize an automatic retry. Result publication checks the exact prepared root
and selected source/draft heads; concurrent changes refuse stale publication.
Typed sanitized errors contain no model reply, source/request or credential.
Unresolved operations are facts, not export or native-effect grants.

## Verification

Use real loopback OpenAI transport and actual Store/Ledger, with invented data,
for generation, restart, same-conversation refinement and PreparedNote selection.
Check full text/order/provenance, explicit guidance and personalization, page vs
all-supplied-unit scope, old operation replay/lost local ack/concurrent callers,
stale/deleted/conflicting state, malformed/oversized output, delayed/lost/canceled
responses, no late publication and refusal before dispatch for oversize inputs.
No Mem calls or native startup may occur. Run representative authorized live
model quality examples separately; do not substitute fake fixture responses for
model quality or native qualification. Central checks and independent source
review precede coordinated paired delivery, sync and archive of this scope only.

Source basis: current Linear requirements/comments and directly inspected local
source/specs; private chronology has no public transcript link. Decisions above
are proposed implementation, not already delivered behavior.
