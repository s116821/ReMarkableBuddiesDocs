# Supplied-text Writer draft verification

This increment implements a bounded ordinary source consumer, not full Writer.
The baseline is delivered Buddy03d51ac and Docsfadbc5c, with an independently
reviewed proposal/design before implementation. This active change remains
unarchived while live-model quality and final code/hosted review are unfinished.
Initial implementation is pinned at `4d1f226fe6057e5565efd69ceef69c9e090b66d4`;
the focused stable-export-scope correction is
`82c0d640f65127141801027f974aa4b2395c120b`.
The subsequent input-snapshot repair is
`e525b76683410137b6c47cf86e0c9ea85a930825`.

## Implemented behavior

Source2 carries explicit normalized document/selection/guidance in the existing
Source domain. Content-bound identity and typed readback validation preserve
ordered text, locations, original adapter-asserted digest and extractor revision.
Encoded document/guidance is at most 40 KiB; the complete source record 48 KiB,
so it fits directly in the existing immutable envelope without another object or
registry. Source1 and export-domain2 shapes are retained; unsupported namespaces
and cross-version shapes refuse. Outer Store/envelope format stays1.

The ordinary provider is reused through LLMEngine/OpenAI. Exact user requests,
eligible chronological Reader/Writer history, separate explicit guidance,
optional personalization, selected units/provenance and the explicitly selected
prior draft form the bounded request. Excess history/source refuses before
dispatch rather than silently truncating. Page scope includes all supplied units
for that page; supplied-notebook includes every supplied unit, without proving
complete extraction of a physical notebook. Large-source chunk/reduction remains
unfinished.

One same-Store Writer owner spans preparation, provider and result. Fresh local
preparation alone authorizes dispatch; a replay or lost preparation acknowledgment
does not. Atomic bounded head snapshots check the prepared root/source/draft
before dispatch and while polling; compare-and-swap guards reject a stale result
at publication. Guard revisions retain identical immutable source/draft facts.
Canceled, failed or lost replies cannot become generated drafts or authorize an
automatic paid retry. Cancellation does not claim remote computation was unbilled.

Generation/refinement stores unrendered Mode::Writer/Outcome::Generated drafts.
Refinement uses the same conversation/original source and adds exact user/draft
turns plus a correction link. Ordinary context still excludes Generated drafts;
the selected draft is explicit. No native completion is fabricated. The bounded
`--writer-note` command resolves credentials/settings before Store opening, owns
and joins its provider operation, and starts no Reader/device/sync path. Explicit
prepare-export returns the existing PreparedNote and performs no HTTP call.

## Actual local evidence

Locked offline Windows runs use actual OpenAI HTTP transport against a loopback
server, fake credentials/invented text and real owned temporary Store roots.
The positive one-shot test executes the actual binary, releases/reopens the Store
and prepares export without a model credential or another provider request.

| Check | Observed result |
| --- | --- |
| Initial focused Writer cases | 9 passed; retained separately |
| Added prepared-state dispatch guard case | 10 passed; retained separately |
| Added actual positive one-shot command case | 11 passed; retained separately |
| Final eleven cases after publication-time cleanup | 11 passed, 0 failed, 0 ignored; 1.97 seconds |
| Stable-scope follow-up at 82c0d640 | 12 passed, 0 failed, 0 ignored; 12.19 seconds |
| Before-preparation selected-draft regression at e525b766 | 1 passed; 0.20 seconds |
| Final input-snapshot repair suite at e525b766 | 13 passed, 0 failed, 0 ignored; 2.29 seconds |
| Existing Ledger regressions | 20 passed |
| Existing Store regressions | 15 passed; nested child output is included, not an extra test count |
| Prepared-export regressions | 12 passed; unsupported-namespace case now uses SubjectMemory because Source2 is intentionally supported |
| Configuration regressions | 2 passed |
| Binary interface unit tests | 5 passed, including new flag/default and conflict assertions |
| Strict all-target/all-feature Clippy | Initial source passed in 5.66 seconds; scope follow-up in 6.59 seconds; final input-snapshot repair in 6.81 seconds, without warning suppression |

Cases cover exact source order and request preservation, page/all-supplied-unit
selection, guidance/personalization, restart and same-conversation refinement,
selected-draft PreparedNote, lost local preparation acknowledgment/reopen with
zero requests, same-Store overlap/Busy, pre-dispatch and post-response stale
state, cancellation, malformed/oversized/lost replies, Reader history continuity
and explicit oversized-history refusal, schema-one text and tampered source
refusal, missing credentials with no input echo/Store writes/startup, and the
positive real command path. First compilation exposed a missing `self` on the
existing correction-target validator; it was corrected before these passing
executions. Initial compile diagnostics are not relabeled as a successful run.

Self-review before final source acceptance found that the initial PreparedNote
scope used a content/turn-bound Source ID. Regeneration of changed source for the
same logical document selection would then conflict with the existing export
association's stable scope. The follow-up uses document identity plus explicit
page/supplied-notebook selection for scope, while retaining content/draft-bound
revision. Its new actual-HTTP generation/PreparedNote case confirms the same
correlation/scope across changed source/Markdown and a changed revision. All12
Writer cases and strict Clippy passed on that follow-up. The broader20/15/12/2/5
matrix above is the retained initial-source execution; no unchanged core matrix
was relabeled or unnecessarily repeated for this Writer mapping correction.

Independent review and owner self-review identified a further input-snapshot
ordering gap: expected root was captured after reading history, and preparation
could protect a newer selected draft than the cached text sent to the provider.
The repair captures root before all related reads and compares the exact cached
Turn before guarding its current version. Its focused actual-path test injects
a valid changed Generated draft successor without changing root at the existing
poll after assembly/before preparation; preparation refuses before a second
provider request. That repaired-path test passed, followed by all13 Writer cases
and strict Clippy. The original race was identified by source inspection, not
claimed as an observed execution against the old source. Earlier snapshots/logs
remain retained. Final independent review must confirm this repair.

## Unperformed and pending checks

At the original R3 checkpoint, no live provider credential/configuration was available in this process or the
inspected current-project checkout locations. Only presence was checked; no key
values read, unrelated-project search or live attempt occurred. Representative
invented-text generation/refinement through the actual live provider remains a
separate required quality check, not something the scripted HTTP replies prove.
The coordinator is aware of that concrete remaining setup/gate. Independent
final source/spec review and exact-head hosted checks are pending. Canonical sync
and archive are not claimed complete while required verification remains open.

No tablet operation, Mem account write, OCR/drawing interpretation, native page
creation/rendering, installed module/gesture integration, full physical notebook
coverage or whole Writer/MVP acceptance is claimed. Source basis: actual current
source, retained local command/HTTP/Store outputs and central contracts. Private
raw logs/review conversation have no public transcript link.

## October 25 reassessment, not successor qualification

Current main is Source49fbf8a / Docs63c1720. The old accepted Source e525b766 and
Docs bd4e7fe, R3 review5561793519, private two-call plan/launcher/build and all
earlier failures/results remain preserved. Docs has been composed with current
main without changing the seven active Writer files (six precode artifacts plus
results) during that merge. Source
composition, renewed review and current-head checks are still pending; no old CI
or local result is credited to the future successor.

Current REM-23 and all16 accessible comments, REM-28 description/sole setup
comment and the actual private harness were read. The approved protected
current-directory environment source is available, verified by presence/access
metadata without values or unrelated search. Root confirmed current-roadmap local
quality authorization; this is a scope interpretation, not a fabricated direct
Writer-specific quote or authorization based only on an earlier API call.

The old harness requires a Config JSON and cannot directly consume that dotenv
setup. Its reviewed successor will load only the approved cwd `.env`, choose the
same OpenAI/default model in memory, cap before the third invocation and retain
bounded exact invented inputs/results in a new private Store. No saved settings,
credential copies/store, Mem send or tablet effect is selected. The original
invented two-page generation/refinement expectations are unchanged. No Writer
live call has occurred; semantic quality remains an unperformed required gate.

Current-main Conversation2 intent/settlement support must survive the Source2
text addition. The old global schema2 text/export condition must not be reused
unchanged. The updated design/delta and launcher require independent review
before repair or dispatch. New quality evidence and final lifecycle/delivery
remain pending; full Writer/MVP is unfinished.

## October 25 frozen current-main composition

Updated precode at Docs739c82e was independently accepted before Source repair.
Source2828bb2479d87cb8006273bb60e6c998e77b1e7d is an ordinary merge of the
preserved e525b766 Writer branch and actual main49fbf8a. It preserves current
Conversation2 intent/settlement and Export2 attempts while admitting normalized
text only as Source2. Current CLI modes and input flags conflict with Writer
before runtime/configuration effects.

The first composed compile refused two unhandled normalized-text projection
cases; that failure is retained. The repaired compile passed. Review then caught
that later Writer turns reuse the immutable original source: the projection now
checks its original same-conversation turn and source relationship while allowing
later references. Supplied document metadata does not become native ownership.

Intermediate execution passed 13 Writer and 10 CLI cases. The new projection
suite initially passed nine of ten: its synthetic fixture incorrectly combined
Prepared state with text and was correctly refused. The fixture was corrected to
the production Interpreted state, preserving the failure; all ten cases then
passed, including actual Store generation/refinement, missing/foreign source
origin, schema-one text refusal and cross-namespace refusal. These local results
precede final frozen-head qualification and are not final qualification evidence.

Frozen-head strict checks, current Conversation2/legacy/export regressions and
hosted checks remain required. First frozen-head strict checking at2828bb2
failed because the current layout-test ContextView literal omitted the new
normalized-text field; the failed log is retained. Successor
e91a9a6a50c52f11169d3bce889e0fd2e81a43aa adds that empty fixture field only,
with a separate current-head qualification run pending. Earlier2828bb2 checks
and hosted run40237080271 cannot qualify this successor.
The private launcher was initially blocked by a pending source pin. Its source
pin has since been updated for candidate builds; live dispatch remains blocked
pending completed current-head evidence and final launcher/executable/driver
review. A concrete one-attempt outer driver enforces 220 seconds;
its final source/spec/executable pins and review remain pending before dispatch.
No Writer live-model call, Mem send or tablet operation has occurred. Semantic
quality, final review, canonical sync/archive and coordinated delivery remain
open; full Writer/MVP acceptance is not claimed.

The e91 library run completed with 472 passing, one failure and three existing
ignored tests. The failure was the current generic storage selection matrix,
which still expected Source2 to refuse. Successor f78c042 updates that opaque
admission matrix to the accepted three namespaces. Independent review found the
same obsolete expectation in the storage integration matrix before its run;
that qualifier was deliberately stopped, not recorded as a test failure.
Successor2788b93c642890dd9403b34707bea059d2893333 updates the integration
matrix's namespace set, eight accepted records, JSON contract assertion and
test name. These two successors change tests only; production files remain
identical to independently reviewed e91. Current schema/shape refusal remains
unchanged. A separate full exact-head qualifier and hosted40237818486 are
pending; the focused selection import/reopen matrix already passes at2788b93.
The original e91 launcher executable and source/lock/build lineage are retained;
its locked offline successor build targets2788b93. No Writer live call occurred.
