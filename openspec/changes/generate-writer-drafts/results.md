# Supplied-text Writer draft verification

This increment implements a bounded ordinary source consumer, not full Writer.
The baseline is delivered Buddy03d51ac and Docsfadbc5c, with an independently
reviewed proposal/design before implementation. This active change remains
unarchived while live-model quality and final code/hosted review are unfinished.
Initial implementation is pinned at `4d1f226fe6057e5565efd69ceef69c9e090b66d4`;
the focused stable-export-scope correction is
`82c0d640f65127141801027f974aa4b2395c120b`.

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
| Existing Ledger regressions | 20 passed |
| Existing Store regressions | 15 passed; nested child output is included, not an extra test count |
| Prepared-export regressions | 12 passed; unsupported-namespace case now uses SubjectMemory because Source2 is intentionally supported |
| Configuration regressions | 2 passed |
| Binary interface unit tests | 5 passed, including new flag/default and conflict assertions |
| Strict all-target/all-feature Clippy | Initial source passed in 5.66 seconds; scope follow-up passed in 6.59 seconds, without warning suppression |

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

## Unperformed and pending checks

No live provider credential/configuration was available in this process or the
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
