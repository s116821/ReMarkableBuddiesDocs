# Actual Reader admission integration — source inventory and next increment

Status: source-only proposal, not implemented or independently accepted. This
inventory is against Buddy2aae1142635c814d8e23e9ec54ba17ac983c01a5 and the accepted
[selected intent contract](selected-intent-migration.md). Main owns task2.10.
Existing bounded admission/retained-settlement reviews do not verify these routes.

## Current source facts

`src/workflow/reader_attempt.rs` uses the ordinary Ledger. Preparation creates an
unbound Buddy conversation and records either explicit legacy evidence or a
synthetic SDK batch. It neither retains SelectedAdmission nor a Store-minted
selection token. The actual Orchestrator prepares before provider dispatch,
persists Generated before rendering and records uncertainty before navigation.
Its nonlegacy branch currently records NativeOutputUnavailable and returns.

RealDevice explicitly declares LegacyUnqualified. No current production
SourceAdmission or SettlementVerification implementer exists. SDK ancestry
discovery is a separate proposal, not qualified binding or output authority.
Legacy captures cannot be transformed into SourceObservation or native page IDs
to make this integration appear complete. Preserve the explicitly unbound Reader
behavior under [the existing persistence seam](reader-persistence-seam.md).

`SelectedAdmission::with_current` shares the canonical Store/group/key gate with
publication and activation, including replacement bindings. It compares an exact
current token and holds the domain gate through its synchronous closure. Store
locks are released before that closure. This mechanism is implemented; the actual
Workflow/DeviceBackend routes below do not currently invoke it.

## Handoffs requiring explicit routing

| Route | Current actual seam | Integration requirement |
| --- | --- | --- |
| Next/Previous and return navigation | Workflow navigation methods; RealDevice.navigate; NativeNavigation.swipe and legacy XochitlIntegration | Validate each selected handoff and hold admission through the whole synchronous composite call; preserve existing input/owner/navigation checks |
| Body mode | Workflow.set_body_text_mode to DeviceBackend.body_mode | Admit separately from later text; an earlier successful navigation check grants no mode authority |
| Answer/header text | Workflow.render_text/render_qa to DeviceBackend.render_text | Validate each text submission, including header writes; retain current keyboard/input/history guards |
| Undo/redo | Workflow.history_action to history_snapshot/history_mutate | Idle dispatcher can run without the original Attempt; require an explicitly retained selected operation context before selected mutation, never a historical receipt alone |
| Bitmap and erase | Workflow.draw_symbol/erase_region/erase_region_smart | Admit each actual backend call; smart erase loops cannot reuse one released admission check |
| Progress | Workflow.show_progress/clear_progress to keyboard progress | These calls can type; selected routing must not misclassify them as read-only telemetry |
| Trigger preparation | Workflow.prepare_reader_trigger before capture/Attempt; NativeTriggerDismiss touch start/release | Not covered by an answer intent that does not yet exist; selected trigger qualification/ownership requires a separate reviewed boundary |
| Status methods | DeviceBackend line/status_stroke/status_clear/status_style_begin/end | Existing source-status restrictions remain; owning lease/restoration rules require explicit classification before any selected route is enabled |
| Observation/cache/diagnostic | capture/details/history_snapshot/check guards/load-save header/record_failure | Inventory separately; cache or diagnostic success supplies no native effect authority, and observation may have backend setup side effects |

The public backend trait also serves simulator and direct callers. An Orchestrator
check alone leaves other entry points unaccounted for. RealDevice composite calls
reach keyboard, pen, touch, native history and observer/lease helpers; this inventory
does not claim that every internal native call has been individually verified.
Holding the canonical gate around a synchronous composite prevents competing
domain activation during that call, but does not replace lower native validity
checks or prove that the native page stays unchanged.

## Proposed bounded implementation sequence

1. Add an explicit selected Attempt state alongside the preserved unbound path.
   It must retain actual admission, exact original publication/Receipt refs and
   the Store-minted publication token. An identical historical retry carries only
   historical acknowledgment and cannot instantiate a live handoff context.
2. Bind that state to the actual Workflow handoff boundary. A selected call checks
   exact current token, original admitted intent/closure, relevant durable
   uncertainty and qualified live source under domain admission before entering
   the backend. Specify how the newly published intent's own pending fact differs
   from an earlier unresolved operation; do not reject every first submission or
   treat pending history as replay permission. Live in-process operation state
   must account for each intended handoff and prevent duplicate dispatch.
   Keep the gate through synchronous submission and revalidate each later call.
   No new production source capability is supplied by this proposal. Do not call
   another admission-locking method recursively inside with_current; any required
   fact/closure validation must use a reviewed locked read path while preserving
   domain-before-Store order.
3. Cover direct public Workflow methods and idle history explicitly; do not leave
   a bypass accepting an absent selected context. Unbound calls retain their
   existing explicit semantics and cannot switch into selected authority.
4. Route actual navigation/mode/text/bitmap/erase/progress composites through that
   seam, retaining native checks inside them. Specify trigger/setup and status
   ownership separately before enabling a selected route. Independent restoration
   remains controlled by existing owned cleanup/lease evidence; a stale answer
   token is neither permission for a new effect nor a reason to invent cleanup.
5. Record submission uncertainty durably before possible input. Qualified receipt
   settlement remains separate; backend Ok cannot become Completed. Restart
   reconstructs facts and latches and never dispatches interrupted operations.

Exact Rust ownership/API choices and the separation of selected trigger/setup,
status restoration and idle history need independent source-contract review before
implementation. Do not wire a synthetic implementer into production to unblock
tests. This proposal selects no new native action and does not close task2.10.

## Required bounded evidence

Use actual Orchestrator/Workflow with a recording backend and real temporary Store,
not a mirror of the intended wrapper. Verify every listed selected effect call
refuses stale/foreign/replaced/historical-only context before any recorded backend
entry, and that a competing replacement waits until synchronous submission exits.
Exercise multiple handles and replacement bindings with domain-before-Store order.
Verify a replacement between two handoffs blocks the second; include header text,
smart erase iterations, progress and idle undo/redo. Actual native validity loss
still refuses inside the backend; current token alone is insufficient.

Preparation/draft/pending write failures must produce zero later provider/effect
calls. Lost acknowledgment and restart return original history without replay.
Unknown or failed terminal recording retains durable uncertainty. Preserve exact
legacy evidence/behavior and SDK-failure-without-fallback regressions. Synthetic
backend evidence establishes mechanics only; production binding, every lower
native handoff and device/full-feature gates remain separately unfinished.

Source basis: current pinned Reader Attempt, Orchestrator, Workflow, DeviceBackend,
SelectedAdmission source and linked accepted contracts. The table states observed
seams; the sequence is proposed integration, not current behavior.
