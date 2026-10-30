# Main-thread service health integration

This source increment implements notification ownership for the ordinary Linux
runtime. It does not install a unit, approve a native profile, stop stock, or
qualify service recovery on the tablet.

Reviewed and pushed Buddy source: `557e88c484dd995cd8d0902063bc128e94583b67` in
[PR 60](https://github.com/s116821/ReMarkableBuddies/pull/60).

The runtime captures notification settings before dotenv and ordinary
initialization. Explicit Writer, maintenance, recovery and simulator paths do
not attach a notifier. Supported settings require a 120-second watchdog and the
current process as owner (or an omitted `WATCHDOG_PID`). Readiness is sent after
ordinary initialization, including sync-worker construction, succeeds.

Actual successful idle input polls, direct trigger waits and active request
checks send due watchdog notifications on the same thread, at most every 30
seconds. No background pinger is introduced. The notifier is nonblocking and
close-on-exec. Wrong owner/thread, clock regression, expired last successful
notification and failed/full endpoints permanently fail the instance. A callback
without a send cannot refresh the 120-second deadline. Resident launch continues
to clear its environment and rejects all three notification variables.

`Workflow` retains health failure separately from input cancellation. The ordinary
orchestrator exits on either fatal condition; service failure is not recorded as
fabricated user cancellation. Callback errors escape the native input observer
instead of becoming an `Invalidated` event or starting its touch fallback.

## Review and validation

Independent module review accepted the ownership, socket and expiry behavior.
Integration review found a bounded-wait edge: the observation deadline must be
checked again after the progress callback, before delivering events. The final
source includes that check and a regression whose callback crosses the actual
deadline before returning a Reader event. Independent review accepted the fix
and the CLI fixture; executed final-source validation remains required.

Initial source validation passed six health tests, three native-input observer
tests and four touch regressions. Run `service-health-r1.log` was deliberately
stopped (exit 137) during its later simulator build to apply the reviewed deadline
fix; it is intermediate evidence, not a completed validation chain.

Final-source run `service-health-r2.log` at `557e88c` passed 81 resident tests,
three native-history tests, four touch tests, 11 binary CLI tests and 42 of 43
simulator tests. The remaining CLI simulator fixture failed because it creates
`CARGO_MANIFEST_DIR/target` while the source was mounted read-only. The failed
log is preserved. The unchanged-source continuation `service-health-r2-cont.log`
added a disposable writable mount for that output directory and passed the one
remaining simulator test, all 22 recovery/startup CLI cases and all eight health
entry cases, followed by strict all-target/all-feature Clippy (8m08s). The
continuation exited zero. No source correction was needed for that mount failure.
Hosted [Buddy run 40248344329](https://github.com/s116821/ReMarkableBuddies/actions/runs/40248344329)
also completed successfully at `557e88c`, including Checks, application Build and
Integration. [Docs run 40248460704](https://github.com/s116821/RemarkableBuddiesDocs/actions/runs/40248460704)
passed at `4d0c5df`; later documentation edits require their own checks.
Tests cover socket timing/ownership, endpoint failure/fullness, actual
orchestrator exit, native observer callbacks and existing contact/simulator
regressions. The CLI startup isolation fixture is
`tools/systemd_fixture/health_entry.py`. Later activation changes require their
own validation; these results describe `557e88c` only.

These shared workflow/socket fixtures test application behavior. They do not
model PID1 scheduling, actual native input ownership, recovery ordering or
tablet UI/persistence. Installed unit/profile qualification and the broader
Reader/Writer acceptance remain open in `tasks.md`.

Source basis: current implementation, prepared regression fixtures and independent
source review; no device actions or installed-service acceptance in this increment.
