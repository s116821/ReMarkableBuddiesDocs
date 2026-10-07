## Source basis and status

Source inspection at Buddy55c683499cdc7d9a177dfd531f73bf4788cd4894 and
Main-attributed tap-only evidence motivate this proposal. Main and Astra accepted
Docs377e63c before Main selected implementation. Buddy25c27d8c860b29d1174dd5b6e7327ea8b54e736d
implements the diagnostic; Main/Astra independently accepted the frozen source
and reproduced34 diagnostic plus8 legacy command checks.106 Linux production
device tests and feature-on/off Linux example checks passed. Target echo evidence
remains pending. Main remains the sole tablet operator.

## Minimal entry and reuse

Add a nondefault `development-input-diagnostics` feature and one Linux-only public
`Touch::diagnostic_tap_echo(point) -> Result<()>` entry behind it. The example's
`tap-echo` branch is available only with that feature. Keep InputObserver and its
owned methods at their existing visibility. The Touch implementation can access
the sibling production observer internally; no public observer/backend framework
is needed.

Before contact, reject anything outside the selected RM2/verified firmware scope
and finite strictly interior virtual coordinates (0 < X < 768, 0 < Y < 1024).
Use the exact existing `verified_contract` firmware/model gate; no new supported firmware is
declared. Obtain the existing writer identity and native_point, construct
InputObserver with no excluded owned devices, and begin_owned_touch. The fixed
corner is only observer configuration; this diagnostic grants no product menu
authority. Stock/session and chosen UI point remain Main's separate preconditions.

Use existing touch_start, wait100ms only after a successful start, then always
attempt touch_stop and finish_owned_touch once a window has begun, even when the
start fails. Combine write/release and finish errors as the existing
NativeTriggerDismiss::tap_once does. Return success only when all succeed.
No retry or second contact is allowed.

Reuse ContactFrames, InputObserver WindowAdapter and owned_touch_window unchanged.
They require matching reader/writer identity and inventory, released initial
state, exactly one slot0/tracking1 contact at the transformed point, positive down
and released frames, released snapshot and no other input. Preserve the current
one-second owned window,50ms drain and8192-event cap. These checks are cooperative
bounds; blocking device operations have no kernel hard cancellation guarantee.
An interruption before release still lacks a release guarantee.

The command returns before the example's common screenshot tail. Only after full
success, print a small fixed JSON receipt identifying the diagnostic with
echo_observed=true, ui_acknowledged=false and native_navigation_qualified=false.
Failures exit with an error and no success receipt. The command performs no
framebuffer capture or fixed PNG write. Existing commands remain unchanged.

## Alternatives and limits

RealDevice::prepare_reader_trigger runs full readiness/native-page checks and a
fixed outside-panel gesture; its constructor also creates cache, screenshot, pen,
keyboard and native-history machinery. It is unsuitable for an arbitrary selected
development tap. A separate event reader/classifier would duplicate production
policy and is rejected. No BTN_TOUCH, range, ABI or serializer repair is justified
by current evidence.

Positive echo establishes only observation through this evdev path. It cannot
prove xochitl consumed the contact or changed view. Failure evidence is inconclusive:
competing events, quiescence or other watch checks can fail even if an injected
event was delivered. Missing echo is not by itself a uniquely diagnosed kernel
cause. Physical frame/backend investigation remains
a separately selected follow-up if necessary.

## Verification and simulator impact

Exercise the actual existing decoder/window tests and observer replay hooks for
complete contact, absent echo, incomplete release, unexpected events, changed
identity/inventory, other input and existing time/event limits. Verify diagnostic
orchestration invokes release and finish after down failure and rejects invalid
scope/coordinates before contact; verify feature-disabled availability and no
capture/success receipt on errors. Tests may substitute OS I/O, never replace the
production classifier. Preserve legacy tap/press/tap-only regressions.

Production simulator behavior is unchanged. Owned replay cannot establish target
echo or UI behavior. Any artifact build, one device diagnostic and independent
source/artifact/receipt review require separate coordinated selection. Keep this
change active until applicable gates finish; do not sync/archive the proposal.
