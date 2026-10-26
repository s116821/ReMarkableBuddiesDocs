# Installed activation composition

The Buddy source now composes the existing installation verifier, fixed lease,
service sampler and resident runtime into a session owner. The normal product
gesture route and an approved installed profile are not enabled. This increment
does not qualify native creation, selection, writing or service recovery.

Reviewed Buddy source: `8c10f63afea97e190225b1769b5140f58472bb32` in
[PR 60](https://github.com/s116821/ReMarkableBuddies/pull/60).

Activation verifies protected artifacts and loaded policy, the actual Buddy
process/group and readiness owner, idle helper and original stock. A sticky
health guard is armed before exclusive lease publication can leave occupied
state. One fixed nonblocking stop uses job-mode=fail. Launch waits for stable
original stock termination and group emptiness/deletion under one 60-second
deadline. The session retains the lease, artifacts and resident child; ending it
permanently fails the same main-thread health owner for independent recovery.
No destructor starts stock.

The recovery state machine now distinguishes the original stock's verified
shutdown from startup or an unknown job. It retains shutdown identity through
terminal observation and can then issue its first start. Prior startup uncertainty
or an attempted start remains sticky and never grants a retry. Partial metadata
clearing, replacement identity, populated groups and timeout refuse. Approved
policy includes the exact 130-second helper start timeout, 90-second stock stop
timeout and 120-second Buddy watchdog. Recovery's total deadline is 120 seconds;
actual timing sufficiency remains an installed qualification requirement.

## Review and checks

Independent review accepted the state-machine design and then found two actual
handoff gaps: the last input check preceded service observations, and runtime
file preparation occurred after the last installed admission check. The final
source repeats input/health/deadline admission immediately before stop. A private
runtime callback rechecks the installed lease/artifacts/services, competing stock,
cancellation and health after file preparation but before spawn; the runtime
then rechecks copied files and the unchanged deadline. Review accepted these
fixes and the actual runtime/predicate regressions.

The preliminary `installed-activation-r1.log` compilation was intentionally
stopped with exit 137 to apply those fixes. It establishes no passing test result.
Final-source `installed-activation-r2.log` passed all 94 resident/library tests
in 41.18 seconds, including the new handoff, ownership and shutdown regressions.
The same unchanged-source chain completed with exit 0: 11 binary CLI tests,
the standalone binary build, all 22 bounded recovery/startup CLI cases, all 8
health-entry CLI cases, and strict all-target/all-feature lint (8m24s). The CLI
fixtures use owned host processes, without PID1 or tablet effects. The updated
Docs pass 88 strict OpenSpec checks and the manifest/source-provenance checks.
Docs revision `4f2b32a` passed hosted run `40251377764`; Buddy `8c10f63` hosted
run `40251260065` passed Title, Checks, application Build and Integration, with
Release correctly skipped. Native qualification is still separate.

## Refreshed read-only target evidence

The October 26 00:47 UTC inspection again found firmware 3.28.0.172 and kernel
5.4.70-v1.6.3-rm11x. Boot identity, actual stock/Buddy PIDs and invocations, and
the three stock artifact hashes match the prior inventory. Stock reports
TimeoutStartUSec, TimeoutStopUSec and TimeoutAbortUSec of `1min 30s`, stop failure
mode `terminate`, KillSignal 15, FinalKillSignal 9 and SendSIGKILL=yes. The new
TimeoutStartUSec property is available. Empty ExecStop/ExecStopPost arrays were
not emitted by this show request, so their absence in that output is not used
as proof about stop commands.

The retained local receipt is
`activation-stop-policy-d6587c085cba4f25803c9d1bd2de756a/receipt.json`.
No unit, payload, process, input, document, firmware or account state was changed.
This read does not qualify recovery timing or install the proposed units.

Source basis: current Rust source, independent source review, local validation
output and the bounded read-only target receipt. Product and native qualification
remain open in `tasks.md`.
