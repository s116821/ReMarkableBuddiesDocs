# Logical navigation and creation-to-write handoff

This is the October 3 selected contract for review before implementation. SDK owns
logical Next/Previous, device implementations and evidence types in its independent
OpenSpec. Buddy owns acquisition, bindings, journal/reconciliation and write policy.
Direct native openPageKey is deferred and is not an MVP/release prerequisite.

## Smallest selected route

1. Verify the live source, supported native creation capability, session/input and
   source revision/order before one correlated insertion. Preserve its operation
   identity and native outcome; an uncertain insertion is reconciled, never repeated.
2. Establish the exact committed target and expected source-preserving post-order.
   Freshly observe active page ownership. A creation receipt is historical structural
   evidence and does not certify which page is active or authorize rendering.
3. If the exact target is active, request no gesture and verify fresh target readiness.
   If the exact source is active and the intended target is its immediate successor
   in that committed order, request one SDK logical Next. Otherwise stop/reconcile.
4. Verify intended target, same document/session, accepted order, fresh settled
   pixels/chrome, input and current ownership. Transfer the verified owner/input
   observer and input epoch explicitly with runtime/session continuity and the
   verified target visit; then perform binding CAS and the separately guarded write.
   The source-to-target page transition may change the active visit only through
   this qualified correlated transition. Source and target visits need not match;
   unexpected visit changes remain sticky failures, never implicit repinning.
   Unknown blankness, binding conflict or lost ownership forbids writing.

Current Reader code already performs one next-page gesture and verifies native
identity/order plus fresh pixels on its qualified RM2 layout. It does not implement
this creation handoff or consume an SDK navigation capability. The existing request
guard is sticky over document/page/visit/session; navigation additionally requires
order/redirect equality. Insertion changes structure, so an explicit proven correlated
handoff is required. Do not clear a latched failure, silently repin source, relax order
equality, or substitute a new screenshot for source ownership.

## SDK logical action boundary

The request identifies logical Next or Previous, a fresh qualified source observation,
the exact intended adjacent PageKey, session/revision/input context and cancellation.
Direction describes native page order. It does not describe finger motion, screen
coordinates or orientation. Each tablet implementation owns its supported mapping;
unknown model/orientation/layout/mapping refuses before dispatch. RM1 qualification
does not qualify RM2 and vice versa. No per-tablet mapping is invented in this plan.

Before dispatch, verify source and intended neighbor under the same guarded order.
Perform at most one physical gesture. After dispatch, report a verified fresh exact
destination, verified no movement, cancellation/uncertainty or unsupported outcome.
Transport success, fixed delay, an image difference alone or a historical receipt
cannot certify completion. Timeout, wrong neighbor, changed session/order/visit or
external input stops the operation; no automatic repeated swipe or fallback route.
SDK evidence retains live-versus-synthetic provenance and cannot regain authority
through historical export/restore. SDK owns the exact type/API design and review.

The current REM-9 gesture/completion behavior, physical cadence, five-second
navigation observation deadline, pixel thresholds and single-attempt recovery remain
unchanged until a separately reviewed implementation explicitly preserves them.
No direct-opening-only setup gate, injected restart/Myfiles fixture reopen, optional
guard supervisor, or native-open experiment is required for logical navigation.
Nonadjacent moved bound pages still require a separately qualified route or honest
reconciliation; this adjacent path does not claim arbitrary-page reuse is implemented.

## Evidence and remaining gates

One explicit RM2 fixture insertion was observed to commit and persist after stock
restoration with originals preserved; that does not qualify product creation or
post-insertion active selection. The spent 604d OPEN run accepted no arm token and
attempted no native open; it ended at its setup deadline with stock restored and
the six-page fixture preserved. Active native owner observation/runtime integration
remain unqualified. Optional guard Buddy9d59087 remains held for two independent P1
recovery findings and is preserved, not archived or discarded.

Review the SDK contract with RM1/RM2 lane owners before code. Contract/model cases
must cover already-active target, source plus adjacent target with one gesture,
unexpected active page, wrong neighbor, no movement, unknown orientation, stale
session/input/order, insertion uncertainty and canceled handoff with no write or
repeat. Native qualification requires Main's advance notice and separately selected
device scope. Simulator facts remain synthetic; no tests in this plan have run yet.

Source basis: the current user decision relayed by Main; Buddy9d59087 baseline
orchestrator/navigation_completion/request_guard source; canonical and active Docs
contracts; independently reviewed saved insertion and spent OPEN evidence. The
proposed creation handoff is design, not implemented behavior or native proof.

## Source/model implementation checkpoint

SDKf6b7dc8954ba9f5a284d56568765e05c38483924 implements the small immutable
logical request, explicit synthetic outcomes, single-dispatch mock correlation
and single-use creation handoff. Main and Astra independently accepted its source
and ran all 36 Rust tests. Native defaults remain Unsupported; model correlation
is in-memory and is not the durable product operation journal.

Buddy's author implementation pins that exact SDK and adds a separate experimental
acquisition seam, not installed Reader rendering. A retained in-memory attempt
session prevents repeated creation/gesture calls after any previous operation,
including lost replies. Zero/one logical gesture branches return SyntheticPrepared
only; cancellation, unknown state and uncertain outcomes require reconciliation.
No binding/write callback is accepted. Consumer frozen semantic review remains
pending; runtime/native owner, pixels, correlated insertion, continuous input and
write integration remain active follow-on work. Existing Reader navigation cadence,
thresholds, observers and request guards are unchanged by this seam.

Existing gesture completion deliberately replaces its observer around the physical
gesture interval. That does not establish uninterrupted external-input exclusion
for a new authoritative SDK handoff. Persisted last-opened identity is a candidate,
not native UI authority. The next native slice should be separately reviewed
read-only owner/identity/order observation, decoupled from direct-opening methods,
before qualifying insertion transition and gesture/pixel/write authority. No such
new native source, build or device action is implemented by this checkpoint.
