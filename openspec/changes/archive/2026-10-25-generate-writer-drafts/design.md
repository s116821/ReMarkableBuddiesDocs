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

Source-domain2 is explicitly admitted alongside existing ExportAssociation2 and
current-main Conversation2 intent/settlement records; subject-memory and
handwriting remain1, outer format stays1. Ledger schema/payload matching
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

## October 25 current-main composition and live qualification

The accepted R3 pair e525b766 / bd4e7fe and its review/build evidence remain
historical, not qualification of a composed successor. Compose the existing
branches with actual Source49fbf8a and Docs63c1720 using normal merge history,
preserving all unrelated current-main entries and the SDK/Manager owners. Source
is currently conflicting; Docs composition is clean. Do not create another PR,
worktree or component-local spec tree, and do not rewrite the old accepted refs.

Main now admits Conversation2 intent/settlement and Export2 attempt records. The
old Writer decoder's global version2 iff(text-or-export) condition is obsolete:
it would reject valid newer Conversation2 records. Composition must preserve the
current encoder, admission/settlement and receipt fingerprint rules, adding only
Source2 NormalizedText admission. Validate version/namespace/record-kind together:
Source2 only for normalized text, Export2 for its existing attempt shape, and
Conversation2 only for its existing intent/settlement shapes. Source1 images,
SDK/development/legacy captures, original receipts and all unsupported shapes
retain their current validation and original bytes. No payload is downgraded,
reinterpreted as another domain or upgraded into native authority. The offline
JSON contract must admit the same namespace/version union as the runtime.

Keep current-main source evidence, resolution, source/memory/research receiving,
cache/normalizers, credentials/settings, selected/runtime and native behavior
intact. Add the Writer Record/Context/CLI cases to current exhaustive matches;
do not replace newer modules with old branch copies or enable installed Writer.
Re-run affected actual Store/Ledger/Writer/command and current Conversation2
regressions plus current-head strict/default/hosted checks. Old13 Writer tests
and old CI are retained at their own source, never transferred to a new head.

The current project resume and required model-quality scope, together with
REM-28's local LLM development setup, cover this bounded qualification. This is
an authorization interpretation of the current scope, not an invented
Writer-specific human quote or permission inferred solely from earlier calls.
The old missing-configuration observation remains historical. The known approved
access-restricted current-directory dotenv source can be loaded inside the
private launcher without copying a key to either checkout or a new credential
store. No new credential question, provider/account choice or saved setting is
needed. Credentials and configured values must not be printed.

Preserve the original private two-page invented-text plan: cart mass2kg,
acceleration3m/s^2, force6N, initial velocity0m/s; Dana checks units, Lee checks the
derivation, no assigned due date, and unconfirmed scratch x=9 is omitted. Generate
once and refine that draft once in the same owned conversation; independently
inspect equations/units, source/page attribution, action ordering and absence of
invented deadline/scratch. PrepareExport may produce a local artifact, never send
a note. A generated status is not semantic quality or native completion.

The updated task-private launcher must be reviewed before execution and pinned
to the composed clean Source head. Its old source/plan/build are preserved. It
must require explicit execution, verify that cwd is exactly the approved setup
directory, load only cwd `.env` without parent traversal, and resolve an in-memory
configuration selecting the same OpenAI endpoint and default gpt-5.6-terra.
Configured provider/model mismatch refuses before dispatch instead of silently
retargeting. Original configuration/Store/sync paths are not opened or changed;
use a newly owned private Store. Enforce at most two invocations before dispatch,
retain the existing90second per-call timeout,24KiB Writer output and bounded
transport behavior, and use a bounded outer execution deadline. Preserve raw
invented-text returns, sanitized reports and incomplete/failure state without
automatic retry, easier fixture substitution or semantic relabeling. No tablet,
Mem export, new credential store, provider purchase or overage is admitted.

Independent precode/composition/launcher review precedes the repair and live
calls; freeze the composed pair and launcher, qualify that exact Source and
inspect actual quality before final sync/archive/review. Writer delivery follows
the preceding notebook-image publication closeout. Full extraction/drawings,
large-notebook reduction, installed/native behavior and whole Writer remain open.

Source basis: current Linear requirements/comments and directly inspected local
source/specs; private chronology has no public transcript link. Decisions above
are proposed implementation, not already delivered behavior.
