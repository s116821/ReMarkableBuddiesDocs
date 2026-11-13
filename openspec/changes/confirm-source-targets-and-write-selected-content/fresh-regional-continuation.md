# Fresh regional receiver and continuation

Status: gated selected receiver implemented with focused offline evidence;
coordinator runtime review and broader qualification remain open. The original
interface review used Buddy928fad43 and paired Docs6eed6d9; exact implementation
and evidence revisions are recorded in verification.md. This remains part of the
same unfinished delivery and paired PRs, not a native or live acceptance claim.

## Receiver and eligibility

Use the existing gated `writer::command::CommandRequest::Resident` submission and
`resident_supervisor::writer_request` slot. Add an explicit
`GenerateRegionOnTablet { document, page, operation, request, guidance }` value;
its variant selects regional generation, with no default scope or arbitrary image.
Keep the existing activation pin, same-UID0600/single-link file checks, bounded
input and boot-time expiry. Do not remove the current development/qualification
gates or introduce a second command service or gesture meaning.

Extend the existing `SourceSession`/`Session::take_writer_request` typed return to
distinguish refinement from regional generation. A read-only peek pins the exact
pending digest/activation so `selected_resident_reader::run` can choose its policy
BEFORE opening ReaderPreferences. No queued request preserves the delivered Reader
route. Once a regional intent is selected, an expired, changed, missing or foreign
request refuses that attempt rather than falling through to Reader.

After the existing complete release and `ResidentSourceCapture` acquisition, claim
the same slot under its existing lock and require the exact activation, pending
digest and captured document/page. Keep this claim through first publication and
consume only the matching pending input before inference. Unknown publication
acknowledgment authorizes no model; a remaining queued copy encounters the original
receipt and stays terminal. Do not discard a different replacement request.

The first slice creates a new Writer conversation on an eligible source page,
as the existing retained-source preparation does. It does not infer an existing
conversation from historical page IDs or adopt a known Buddy page. Use already
target-capable selected family6 and the delivered installed service eligibility;
do not silently promote an ineligible legacy LocalOnly history. Writer-only
selected startup, production preset/gesture qualification, reuse of an existing
conversation for native retarget, and output/Submit effects remain explicit later
integration gates. This gated receiver grants no native rendering authority.

The ordinary installed loop must explicitly refuse the new regional-generation
intent until its own fresh receiver is supplied; it must not start Reader or call
the selected factory on an ordinary Store. Ordinary stored-target commands retain
their existing route. The ordinary slot reader must refuse an observed regional
intent before refinement's expiry/page filters can return Reader None. Keep
unexpired matching/foreign queued bytes intact; an expired owned record may be
retired under its existing lock, but that attempt still refuses. Preserve absent
input and all existing refinement page/expiry/consume behavior. The first implementation does not change startup eligibility.

## One operation from release to finalization

Set `S = ReleasedReaderInput.released_at`. Open ONE Writer RequestPreferences at S
through the existing `from_binding_at` machinery. Do not first open the420s Reader
policy and replace it. Acquire the existing Writer Store owner once and retain it,
the resident input/session, fixed policy, exact selected document scope and original
partitioned reads until normal Workflow finalization.

Clamp resident source acquisition to S+60 while preserving the Reader default90s
path. Reserve the existing300s/16-phase Writer read envelope once before acquisition;
do not replenish any partition later. Cold-path exhaustion or insufficient time
refuses. Validate that this envelope fits the concrete path with bounded fixtures;
any proposed initial reservation change requires review before implementation.

After the genuine original/provider image hashes are known, capture one confirmed
context excluding all of them and retain its selected owner even when complete
and empty. Freeze the existing selected memory view once before first inference;
it is not target-geometry authority. Geometry and recognition use only the retained
frame and the applicable confirmed examples. No new context selection, memory query,
Store owner or policy factory follows identification.

## Receipts and parent absence

Let X be the queued logical operation, C=`stage(X, "source-normalization-admission")`
and P=`stage(X, "target-normalization-admission")`. Preserve both historical IDs,
all existing capture/stored-target encodings and their fingerprints. A fresh request
uses P for its FIRST pre-inference preparation, not a third competing admission ID.

Factor the genuine retained-capture record construction from ResidentPrepared into
a narrow shared builder. Its existing Reader wrapper keeps its exact IDs, mode,
fingerprint and behavior. A private Writer factory creates the new root, one
Writer Prepared user `stage(X, "user")` with exchange X, the actual retained capture
and receipt P in ONE guarded selected commit. Bind a distinct fresh-request
fingerprint to the original selection/raw head, queued request/digest, prepared
root/user/capture references and effective model/context correspondence. There is
no separate capture transaction followed by an unfenced first inference.

The first commit uses `commit_selected_guarded` with prerequisites `[X, C, P]`,
the original admission allowance and S+60 time/cancel check. Keep Reader-only
SelectedReaderWrite admission unchanged. A known P or C is terminal evidence in
every input variant, including after restart; it cannot recreate a live operation.
The existing evidence-only normalization recovery can verify the accepted P,
predecessor, fingerprint and lineage without requiring a second normalization turn.

| Transition | Durable transaction | Model admission and time | Parent X |
| --- | --- | --- | --- |
| Genuine capture and Writer Prepared input | P, including original capture and user | None; complete by S+60 | Must be absent with C/P at publication |
| Identify target once | P already exists before dispatch | Joined handoff reads; `with_selected_operation_absent(current P token, X, ...)`; deadline min(S+60, now+45s) | Still absent |
| Accept interpreted or uncertain target | `stage(X, "target-interpretation")` | Guarded admission reads/marker by S+60; no model | Still absent; do not use X for this commit |
| Normalize the proven mask once | Reuse P; do NOT prepare P again | Existing normalization stage0, joined handoff reads and absent-X helper; deadline min(S+150, now+90s) | Still absent after own interpretation receipt |
| Accept RegionSource and draft preparation | X | Existing guarded source preparation; original finish allowance and marker by S+150 | Accepted here by its own original |
| Generate draft once | X already supplies existing draft permit | Existing stage1 with own preparation; deadline min(S+240, now+90s) | MUST NOT require absence of its own accepted parent |
| Accept Generated result and presentation binding | Existing finish child | Guarded final proof/marker by S+300 | Retain exact own X receipt |

These are atomic absence checks, not long-lived parent reservations. Both target
identification and normalization need the existing immediate handoff guard because
another local producer can accept X after P. Invoke only the worker-spawn callback
under Store's mutex and release it before response waits. Time/cancel checks there
must not re-enter Store or acquire gates. All three submissions remain one-use.

## Shared identification and continuation

Factor `Orchestrator::parse_target_candidate` and its geometry contract into the
target module; preserve Reader's header extraction and verification behavior.
Fresh Writer requests only one bounded Candidate against the exact original frame,
with its explicit request separate from source data. Do not run Reader's answer or
question-verification flow to obtain a target, infer extents from a center point,
or treat a subject as confirmed handwriting transcription.

Use a private fresh-frame proof extracted from the same selected retained-source
resolver; it has genuine source/user/frame/media correspondence but no target yet.
Factor the target-record builder behind `selected_reader_write::targets::interpret`
into a private mode-aware construction helper. Under the existing joined guards,
commit the original Writer user as Interpreted with its explicit request plus
SourceTarget/TargetUse/TargetState/root and the interpretation receipt. Invalid or
ambiguous localization becomes explicit uncertainty; no normalization or old-target/
page/notebook fallback follows. New-root state has no prior target to inherit.

Resolve current TargetState's use reference as its exact immutable selected member:
presentation may advance that use's hash revision independently. Keep the active
state, target and source checks current, including explicit retarget/clear refusal.

Advance current root/token ONLY through the returned P and interpretation receipts.
Retain the original pre-P selection for memory/policy correspondence. Then resolve
the newly accepted target through RegionalImage, derive the existing full-canvas
mask, and compare its hash with every already frozen example. A match refuses;
never drop/reselect an example after the first model use.

Refactor the private owned runner into an entry before identification and an entry
after interpretation. The latter consumes the SAME owned operation and context,
using its acknowledged current token/root and the existing P; it must not call
public run_target/run_input wrappers that acquire another owner or prepare again.
Track identification separately from the established normalization0/draft1 counters.
Use an explicit private step to choose time checks: identification must not inherit
the normalization150s cutoff merely because its normalization counter is still0.
Read partitions remain the original admission/handoff/finish/progress partitions.

## One user turn and one About

Keep the prepared Writer user as `stage(X, "user")`, sequence0 and exchange X.
Interpretation revises that user; normalized-source acceptance revises it again
through a sealed fresh-region input instead of adding a duplicate user/request.
Its sources become the exact original capture plus RegionSource. Retain the capture
association so SourceTarget's original-user proof remains valid. This two-source
shape is allowed only by exact fresh target/user/capture/region correspondence;
ordinary stored-target generation and Refine keep their existing source shape.
No generic caller-provided list or Boolean can select this exception.

The normalized-source commit creates the same existing SelectedWriterPrepared and
one draft permit under X, with exact current user/root/source references. The
assistant references RegionSource only and receives regional text units, not the
original whole page as requested coverage. Do not increment the user sequence when
revising it; the assistant is the next real conversation turn.

Reuse `present_regional_draft` and bind the actual Generated body hash into the
introducing TargetUse in the SAME final transaction. Existing layout suppression
requires Reader's About prefix; extend it narrowly for typed Writer Generated
bodies whose exact bound hash and validated Markdown About position match. Do not
suppress metadata by substring guessing. Preserve the Reader recipe. On reopen,
history and the proposed note show one About for this exchange; later Refine keeps
the frozen RegionSource/About without rewriting the old presentation hash.

## Minimum validation and ownership

Exercise the real gated receiver chain with a declared genuine fixture capture,
not a fabricated native permission: queued intent, exact session/page claim, P,
identify, interpretation receipt, exact-mask normalization, X and image-free draft.
Assert one user/request, one About in history/note, original capture retention,
unchanged outside region and the same context/view/owner across three submissions.

Cover changed/expired/foreign slot and activation, wrong document/page, duplicate
release, Source/target/policy/context/memory changes at actual joins, ambiguous
geometry, derived-mask/example collision,45s/60s crossings, original read exhaustion,
lost P/interpretation/X acknowledgments and restart with no repeated call. Reuse the
actual sibling/foreign-parent regressions for first identification as well as
normalization. Assert normalization still sees X absent after its own interpretation
and draft succeeds with its own X present. Keep all old capture wire/ID controls.

SCRAPPY owns the target/parser, selected Writer continuation/command, preference
window/context, shared preparation/target-record builder and layout seams. The
coordinator accepted the concrete installed slot/Session, selected receiver and
acquisition-deadline handoff before these runtime edits. No edits
to native recovery/effect qualification, activation permissions or other Native-owned
work follow from this plan. Live/provider and tablet acceptance remain separately
owned; full-feature canonical sync and archival remain open.


## Concrete runtime file handoff

The coordinator assigned these seams before edits; this table does not transfer
Native's isolated publisher or shared startup ownership.

| File and existing entry point | Narrow edit | Ownership boundary |
| --- | --- | --- |
| `src/writer/command.rs`: CommandRequest::Resident/dispatch | Decode the new explicit installed submission through the existing command | SCRAPPY Writer consumer |
| `src/workflow/resident_supervisor/writer_request.rs`: Submission, submit, read, take | Strict regional intent, digest peek/claim and matching consume | SCRAPPY after Session interface handoff; preserve lease/expiry/permissions |
| `src/workflow/resident_supervisor/recovery/activation.rs`: Session::take_writer_request | Typed request forwarder and peek/claim forwarding only | Coordinate this exact forwarder; no recovery/activation behavior edits |
| `src/workflow/resident_source.rs`: SourceSession::take_writer_request, Owner::take_installed_writer, begin_with_check | Propagate explicit intent and clamp Writer acquisition to original admission | SCRAPPY source seam; preserve Reader90s and native factory/qualification |
| `src/workflow/selected_resident_reader.rs`: run per-release policy/acquisition branch | Select Writer policy before Reader admission, claim exact capture/intent, invoke fresh continuation and common finalization | SCRAPPY body branch; keep startup signature/eligibility stable in this slice |
| `src/workflow/mod.rs`: selected_resident_conversation; `resident_output.rs`: SelectedConversationRequest | Carry typed intent without granting output capability | SCRAPPY data dispatch; no new renderer/effect route |
| `src/workflow/orchestrator.rs`: parse_target_candidate and run_iteration_inner | Shared candidate parser contract; explicit unsupported ordinary installed fresh branch | SCRAPPY narrow parser/dispatch only; no hidden Reader answer |
| `src/storage/sync/selected/preference_consumer.rs`: Writer factory/from_binding_at, capture_writer_targets | Original released_at factory and passed frozen context/remaining partitions | SCRAPPY Writer methods only; isolated publisher/Drive/package work stays Native-owned |
| `src/conversation/selected_reader_prepare.rs`: ResidentPrepared record construction | Shared immutable builder plus sealed Writer P packet; keep Reader wrapper unchanged | SCRAPPY after preparation interface review |
| `src/conversation/selected_reader_write/targets.rs`: interpret record builder | Share bounded record construction with private Writer interpretation, preserving Reader-only admission | SCRAPPY target-record helper |
| `src/conversation/target.rs`, `selected_writer.rs` and regional child; `src/writer/selected/image.rs` and regional child | Fresh frame, one-use identification, own-receipt advancement, sealed one-user source attachment and existing draft continuation | SCRAPPY existing target/Writer ownership |
| `src/conversation_layout.rs`: exact hash-bound inline About suppression | Retain Reader prefix recipe; add typed Writer Markdown position validation only after exact body-hash match | SCRAPPY presentation seam; ordinary note formatter stays shared |
| `src/main.rs`, `src/reader_runtime.rs`, `src/mode_maintenance.rs`, `src/workflow/conversation_dispatch.rs` | No startup edit selected by this first slice | Shared runtime: Root assigns Native's isolated-startup ranges/signatures before either lane edits |

If startup signatures change in the coordinated Native work, import the accepted
composition and adapt the call site after review. Do not independently implement
an isolated-mode startup fix or widen Reader/Writer eligibility. Physical input
reducer, production scope registry and native effect qualification remain with
their established owners. Public declaration/inspection of this intent is not
qualification of a production gesture or tablet output.

## Presentation-context implementation finding

The connected reopened-layout fixture exposed that `context_range` intentionally
filters Generated Writer turns as model context. A hash-bound layout recipe alone
cannot inspect a body missing from that view. Add a separate bounded read-only
presentation view over the same exact ordinary/selected records, including typed
Writer Generated assistant bodies. Route the existing history presenter through
that view; keep the model-context filter unchanged. Both views retain their text,
turn, token and exact selected-media bounds. This is historical data presentation,
not a selected/native effect route or a new binding. Check both the unchanged
model filter and the exact body/hash/Markdown-position layout recipe.

The fresh root has no fabricated presentation binding. Its reopened presentation
context exercises the shared read-only About-entry projection directly; the actual
bound-page layout calls that same projection after its existing identity checks.
Native rendering and a real bound tablet page remain independent integration gates.
