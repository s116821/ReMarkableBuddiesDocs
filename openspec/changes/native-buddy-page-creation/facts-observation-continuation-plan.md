# Proposed bounded callback-status continuation

## Concrete limitation and source basis

Main reports spent2f90 had12 successful callback-absent status reads followed by
one3s observation transport timeout, after which the existing finally path
restored stock before any live Main waiting proof, input or published request.
Main corrected the historical collection: facts-waiting was present; request,
callback, diagnostics and refusal were absent. Historical waiting cannot upgrade
live generation/readiness flags. The original receipt and all spent evidence stay
unchanged. These are Main-attributed current-chat facts, not independently verified
transcripts in this proposal.

Buddy25c27d8 source confirms that callback polling is read-only and every timeout
currently throws. Native kills a timed-out local transport and confirms its exit
before returning a timeout result; uncertain termination throws. ObservationSSH
checks the original150000ms stopwatch before and after transport and admits at
most min(3000ms, remaining time). Kill/exit-confirmation overhead also consumes
that original clock. Recovery has separate mandatory duties.

## Ownership and proposed scope

Keep this proposal under the existing active native-buddy-page-creation change,
which owns the facts consumer experiment and collector/recovery evidence. This is
a prospective source-only collector correction, not a new lifecycle framework,
timeout extension, SDK change or selected device attempt. Implementation awaits
Main/Astra coordination; no fresh nonce is selected by this proposal. Main and
Astra accepted Docs4ddbef before Main selected the narrow source change.
Buddy59789d0b4ae0f7c12d7ac890e0745b4bf62b3d43 implements it, pending independent
implementation review.169 exact collector/live/recovery assertions and10 existing
transport assertions passed with owned I/O; no device result is claimed.

Permit at most one returned timeout result in the initial callback-status poll
over the entire collector run to consume a single local allowance and continue
to a fresh execution of that exact read-only poll, only while the ORIGINAL live
window remains open. The allowance never resets on successful or callback-absent
reads. A second timeout restores through finally. Preserve both native result
records, including the timeout; never reuse partial stdout from a timed-out read.

Do not catch uncertain transport-exit exceptions, exhausted/late ObservationSSH
exceptions, malformed callback data, or non-timeout nonzero exits other than the
existing callback-absent exit3. Do not apply continuation to activation, upload,
publisher, generation proof, diagnostics/refusal collection or recovery transport.
Those retain existing failure behavior. No reset, sleep, pacing or changed
per-transport bound is added.

The callback-status shell currently rechecks stage directory type/mode/owner,
nonce and close/restore markers. It does NOT establish the attempted process
generation or pin directory inode while callback is absent. Preserve that fact:
exit3 means only a validated absent callback at that observation. A successful
follow-up grants no positive waiting, input, publication or product authority.
Main's independent live waiting/UI gate remains required before any separately
authorized external action. If a callback arrives, keep the complete existing
request/attempt identity, stage inode, live PID/start/executable/maps/empty-job,
diagnostics and final live rechecks before generation/facts qualification.

All existing bounds remain setup120000ms from entry startup, read5000ms from
accepted request, host150000ms from before arming, rollback initiation180s from
arming before activation and distinct restoration TimeoutStart240s. A read-only
remote command may outlive local cancellation; the added read issues no effects,
and this proposal claims no hard remote syscall cancellation guarantee.

## Evidence semantics and simulator impact

No new success flag is needed. The existing results list retains the failed
observation. A local one-use boolean controls allowance only and establishes no
delivery, readiness or generation evidence. Facts success requires the unchanged
full live proof; eventual historical observations after restoration cannot
retroactively set live flags. Preserve spent2f90 successfalse and its exact
restoration/cleanup evidence.

Product simulator behavior is unchanged. Extend the existing exact collector
branch/outer-finally owned mocks, without a new substitute harness, to verify:
one timeout then exit3 then complete existing proof; one timeout then valid
callback/proof; second timeout; timeout near deadline; late return; uncertain
transport termination; non-timeout refused/unsafe stage; malformed callback; and
subsequent identity/proof failure. Assert no partial stdout consumption, same
clock/3000ms cap, no renewed allowance after intervening success, original false
field semantics on failure and mandatory restoration. In particular,
callback_verified can remain true after a later identity/proof failure; the
allowance never changes a field. Tests cannot prove target stability.

Freeze exact Docs/Buddy revisions and obtain independent review before any
separately selected artifact/packet/device gate. Do not sync/archive this active
unfinished feature or repair its held generic guard framework.
