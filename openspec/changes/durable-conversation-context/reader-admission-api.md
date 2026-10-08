# Reader admission Rust ownership proposal

This is a source-only API proposal for the bounded decisions in
[the accepted inventory](attempt-admission-inventory.md). It does not enable a
selected backend, mint a production capability, or close task2.10. Implementation
base is Rust472de17; existing pending and retained settlement wire formats remain.

## Controlled minting

Add a crate-private `ReaderPreparation` enum with `Fresh(ReaderContext)` and
`Historical(HistoricalIntent)`. `ReaderContext` has private fields and no public
constructor, deserializer, Clone implementation, token setter or reset operation.
Its only constructor is inside a new controlled pending publication method on
`SelectedAdmission`, using the actual new branch of `publish_in_store`. It never
accepts a caller-supplied `PendingIntentPublication` as proof of fresh publication.
Existing public publication/recovery APIs retain their current behavior and
cannot construct the Reader context.

The method takes the accepted token, exact pending request, an owned sealed live
Reader source capability and a bounded immutable handoff plan. Recover and validate the original logical request first under the canonical
domain gate. A historical retry returns only Historical before current-source,
plan or uncertainty checks and cannot be converted into Fresh. Only the new branch
validates the plan (at most MAX_ITEMS steps and MAX_RECORD total serialized
argument bytes), source binding and relevant uncertainty before publishing. The fresh context retains
the actual publication token, original request, exact receipt/reference, original
closure references, admission handle, live capability and one shared dispatch
state. The plan is in-process authority, not a new persisted completion claim;
restart has no mint path and never reconstructs an executable plan.

Use a separate sealed `ReaderSourceAdmission` capability extending source
verification with exact plan and per-handoff native validation. There is no
production implementer. Current `SourceAdmission` implementers are not implicitly
Reader effect capabilities. Only test modules may supply recording capabilities.
Every verification binds the same original source/operation and exact handoff
arguments; storage token or stored identity strings alone cannot satisfy it.

Input preparation and output preparation are separate. The actual Attempt first
persists exact acquired evidence before provider dispatch. After interpretation
and provider work, it persists the Generated assistant draft. Only then can the
immutable output plan be finalized and the controlled Pending/context publication
occur, before any output handoff. A failed evidence/draft/pending write stops later
provider or effect work as appropriate. No output plan is edited after publication.

## Plan and dispatch ownership

Use typed handoff variants for navigation direction, body mode, text bytes,
Q&A text bytes, symbol coordinates/text, rectangle erase, smart erase rectangle
plus exact screenshot bytes, and progress text/clear. Plan order supplies the
ordinal. Bound total argument bytes and number of steps before publication;
retain exact values rather than accepting a digest supplied by the caller.
Unsupported trigger, history setup, undo/redo and selected status lease operations
are not plan variants. This increment's selected Q&A rendering must refuse the
existing input-producing history setup; it may use the separately admitted plain
text step without arming native history.

`ReaderContext` owns a shared operation state with the next ordinal and sticky
stopped flag. It is not copied into independent eligibility states. The actual
Workflow dispatch entry compares kind, ordinal and exact arguments before any
backend entry, validates current selection/closure/uncertainty/live capability,
marks the step Entered before I/O and holds the domain gate through the complete
synchronous outer composite. A successful return advances to a distinct next
step; the entered step never becomes eligible again. Error, panic or abandoned
entered submission leaves the operation stopped; an RAII entry guard defaults to
stopped unless completion is explicitly recorded. Backend Ok is not verified
completion and does not settle durable Pending.

A private under-gate admission helper reads the Store and supplies both snapshot
and original closure validation without acquiring the domain gate again. Store
locks are released before I/O. Do not call the public recovering/retained
uncertainty methods from this helper. Retained uncertainty uses the existing
validated retained chain rules; do not weaken exclusive-retained validation to
accommodate the fresh active context.

Own active Pending is accepted only when its exact original receipt, root, turn,
pending fact and closure are still selected and agree with the controlled fresh
publication. All earlier relevant pending operations must be inspected across
active and retained records: unresolved, unknown, malformed, forked, deleted or
incompletely retained relevant history blocks. Verified retained release requires
the existing original linkage, publication and current Store actor checks. A
binding/source ambiguity is refusal, not evidence that earlier history is irrelevant.
Relevant means the same qualified document ownership within this selected aggregate;
unresolvable ownership of an uncertainty record blocks conservatively. Unrelated
proved document ownership is not treated as this operation's pending state.

## Actual backend boundary

Add a selected backend facade with a private wrapped backend and no raw-backend
accessor or conversion back into the unbound Workflow. Its public effect methods
require a matching context dispatch; absent/foreign/consumed context refuses before
calling the wrapped implementation. Workflow's selected constructor consumes that
facade and retains selected mode for its lifetime. Existing unbound constructors
and legacy behavior remain explicit and cannot adopt selected authority.

Direct public Workflow effect methods in selected mode must route to the same
context-bearing dispatch or refuse; merely checking in Orchestrator is insufficient.
No reusable ambient boolean temporarily enables all backend methods. The admitted
outer composite receives a private borrow-scoped backend permit restricted to that
step. Lower helpers use that permit and preserve native guards without reacquiring
admission. The permit cannot escape the call or authorize a later public call.
The facade exposes no unrestricted `DeviceBackend` implementation. A future native
selected adapter must enter through this facade; the present RealDevice remains
LegacyUnqualified and is not promoted by wrapping it.

Selected pre-Attempt trigger/acquisition setup, input-producing capture, status
lease acquisition and idle history refuse before setup. Independent existing
lease restoration retains its owned journal/native checks and obtains no new
answer authority. Diagnostic-only failure reporting remains diagnostic. Header
cache and capture helpers must not bypass the selected facade to reach setup/input.

Attach only the controlled fresh context to the actual selected Attempt. Historical
Attempt state cannot request output. The current SDK fixture preparation remains
non-output until qualified selected preparation exists; adding synthetic context
tests does not change that production refusal. A complete Orchestrator bootstrap
still requires the separately reviewed selected acquisition ownership boundary.

## Required review and checks

Review this ownership/API proposal before source implementation. Actual Workflow
and facade tests use real temporary Store publications plus a recording backend:
missing/foreign/stale/historical contexts, duplicate and changed-argument dispatch,
replacement waiting during submission, replacement between steps, multiple handles,
backend native refusal, error/panic stopping later steps, and relevant earlier
uncertainty all require zero unauthorized backend entries. Include smart erase's
multiple lower calls, header/text/body/navigation/progress and unsupported idle
history/setup. Preserve the full legacy and SDK-no-fallback suites. No production
capability, native qualification or full task2.10 acceptance follows from mocks.

Source basis: current Rust472de17 pending/admission/settlement, actual Attempt,
Workflow and DeviceBackend; accepted Docs1ded7bc inventory. This document proposes
API behavior and does not report implemented behavior.
