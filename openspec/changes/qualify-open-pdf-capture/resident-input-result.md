# Owned input for installed resident requests

Buddy `b20f9427311c9f432fb2114d28959bf7bbb4420a`, with test compile correction
`4fdabf38d9dd431b038f434b8dc6fda4f2a30bc4`, connects the installed Session
API to `device::request_input::RequestInput`, which owns the existing Linux
InputObserver. Production activation/request/reconnect no longer accept an
arbitrary input callback. The common dispatcher retains its private callback seam
for owned-runtime verification and installed authority composition.

Any interaction or nonquiescent contact cancels this request permanently. Quiet
input cannot revive it. Polling continues after cancellation so observer failure
still becomes integrity loss. The guard has no page identity, capture or output
capability and does not inject or grab input.

Activation retains its original deadline and renews input descriptors before
returning the Session. The old observer brackets fresh descriptor construction;
the new observer is then polled before replacing the old one. Both contribute
to cancellation. Any replacement failure invalidates the guard without retry.
Final installed admission follows the handoff; failure drops the owned Session
under its existing fatal health/recovery rules.

New host regressions cover sticky cancellation for every interaction, observer
error after cancellation, raw unfinished contact and SYN_DROPPED handling, quiet
and canceled replacement, creation/old/new observer failures, and no renewal
after cancellation. An owned-child test passes the actual guard through the
request/reconnect dispatcher and checks cancellation versus integrity outcomes
with the same process identity. OS reads are scripted; raw contact decoding,
observer loss, guard state, dispatcher classification and child ownership are real.

Formatting and whitespace checks pass. Independent source review accepted the
observer overlap, sticky cancellation, error precedence, original activation
deadline and refusal/drop behavior. Initial pipeline
[40258399289](https://github.com/s116821/ReMarkableBuddies/actions/runs/40258399289)
failed compiling a new test's unqualified `anyhow!` macro. The error was corrected
to `anyhow::anyhow!`, without production changes or weakened assertions. Its
failed log is retained as `input-b20f942-failed.log`. Corrected exact-revision
execution [40258687350](https://github.com/s116821/ReMarkableBuddies/actions/runs/40258687350)
has passed Checks: 686 library tests passed (3 ignored), 11 binary tests and
the integration/CLI/simulator suites passed, together with strict lint. The
application build remains running. The completed Checks log is retained as
`input-4fdabf3-checks.log`. Prior `b585517` full CI also passed but does not
validate this increment. No local build was attempted with insufficient disk space.

This supplies input continuity to the installed Session component. Workflow
still needs first-gesture ownership, source reacquisition and actual capture/
Writer composition. No source-page continuity, native owner reuse, installed
profile, Manager lifecycle or tablet acceptance is claimed. No tablet action
or capability activation occurred; the coordinated change remains incomplete.
