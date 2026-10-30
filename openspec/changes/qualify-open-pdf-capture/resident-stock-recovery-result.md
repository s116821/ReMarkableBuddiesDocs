# Fixed-profile stock-restoration helper

Buddy `ce5b67c` implements the actual Linux restoration sequence in
`workflow::resident_supervisor::recovery` module. The subsequent CLI increment
below adds command dispatch and ordinary startup refusal; installed service
integration remains open. No qualified production manifest is shipped,
and no real stock stop/start or native load occurred in this increment.

The entrypoint has fixed service names, artifact paths and a 45-second monotonic
budget. It reopens the fixed boot lease, checks a separately bound version-2
recovery-profile digest, and verifies the protected root-owned installation and
actual helper process/service/group. Version-1 or missing-field records refuse
without replacement. The original native-profile digest remains distinct.

After verifying original Buddy terminal ownership and stock group emptiness,
it may request one nonblocking stock start with explicit `--job-mode=fail`.
An already running/starting stock instance is observed without a command. An
uncertain command or failed startup is never automatically retried. Stable actual
stock executable bytes, argv, incarnation, membership, namespaces, group population,
policy and service state must pass before a service-restoration result is returned.
The lease and helper/Buddy admission are checked again at completion. All large
artifact hashes stream through a 64 KiB buffer; commands retain bounded output
and owned-child cleanup from the service module.

Independent source review found and corrected a conflicting-job replacement race,
duplicate nested policy keys, a missing closing process-membership check, and the
need to verify actual stock group emptiness before starting. The firmware check
uses the observed `/etc/os-release` `IMG_VERSION`, not the OS distribution version
or an assumed separate version file.

## Verification

- Intermediate Linux run `resident-stock-helper-r1.log` passed 70 resident tests
  in 50.89 seconds. Later direct admission tests and streaming changes supersede
  that source; this is not final-source evidence.
- Final-source run `resident-stock-helper-r2.log` passed 73 resident tests in
  31.16 seconds: 26 client, 10 runtime, 16 ownership, 8 service and 13 recovery.
  Strict all-target/all-feature Clippy passed in 7 minutes 36 seconds. This is
  the helper revision before the separately validated main-branch reconciliation.
- Direct recovery tests cover original manifest/artifact binding, strict nested
  JSON, helper PID/ExecMainPID/invocation/oneshot state, missing/old lease fields,
  actual process executable/argv/environment checks, real-file empty/missing/link
  cases, concurrent state changes and uncertain-command/no-retry sequencing.
  The sequencing backend is private and synthetic; the installed admission path
  cannot take a substitute command, filesystem, unit or profile path.
- Formatting, all 82 OpenSpec items and Docs provenance checks pass. Hosted
  source validation must be checked against the reconciled committed revision.

GitHub reported PR60 `CONFLICTING` against main; its `pull_request` workflow had
no registered run for `ac7c040`. GitHub documents that conflicts prevent this
event's workflows from running in its
[workflow troubleshooting guide](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows).
Merge `093c0c6fe68d2b58596a45cd6f3c749267aa5786` incorporates current Buddy main
`1d1665f7860837f36403585dfd4482d5668a6e56`. It retains both existing-page Binding
and incoming Writer NormalizedText schema branches in one decoder chain; splitting
them into independent conditions would incorrectly reject schema-2 bindings.
Independent source review accepted that resolution. Merged-source local run
`resident-stock-helper-merged-r1.log` finished with 73 resident, 3 intent,
5 existing-binding, 8 historical-association and 20 conversation tests passing.
Writer passed 3 and failed 10; the chained lint did not run. A direct loopback
diagnostic identified client-construction failure because the test image contained
no system CA certificates. No Writer/schema/TLS production change was made.

The derivative test image `rem25-rust-qt-ca:review`, SHA256
`cb9d35cf24d37c1b5d69b091d4bc7014aa57b3dd75979be948b9627a5f4ece95`, installs
normal system CA certificates and Clippy. Running the same already compiled Writer
binary there passed all 13 Writer cases and the one diagnostic in 3.09 seconds.
The temporary diagnostic was removed from the repository test file and retained
locally with its exact error chain. This identifies the local environment failure;
it does not validate the later CLI source. Hosted merged-source run
[40244649358](https://github.com/s116821/ReMarkableBuddies/actions/runs/40244649358)
passed its Checks job, including full tests and strict lint; application build
was still running at the CLI checkpoint.

## Recovery CLI and ordinary startup latch

Buddy `ae78fb38df9b846a901629ad2b5b2580dae0f167` dispatches exclusive `--resident-stock-recovery` immediately after
argument validation, before Writer/configuration/Store/provider startup. A distinct
`NoRecordedActivation` no-op requires exact final-file absence below an existing,
unchanged protected boot directory. It does not claim stock readiness. Any occupied
invalid, partial, stale, linked or replaced record remains an error. Ordinary Linux
startup independently checks the same fixed latch before dotenv/configuration,
Store or device/provider startup; explicit non-device Writer and maintenance modes
remain separate. Native launch still requires future first-gesture admission and
exclusive publication, not this initial empty check.

Independent source review found no blocking defect. Initial run
`resident-stock-entry-r1.log` passed 75 resident tests, including appeared-record,
directory replacement, invalid-record and consumed-lease preservation cases. It
passed 10 of 11 binary tests: the explicit option inventory needed the newly added
flag; exclusivity itself passed. The final commit updates that inventory and checks
the default is off. Final-source run `resident-stock-entry-r2.log` exited zero:
75 resident tests, 11 binary CLI tests, 13 Writer tests and 22 actual recovery/startup
CLI cases passed, followed by strict all-target/all-feature lint (12m13s).
The fixture poisons ordinary configuration and exercises bounded
real subprocess calls; it never runs against PID1 or a tablet.

Hosted run [40246344504](https://github.com/s116821/ReMarkableBuddies/actions/runs/40246344504)
at this same commit has passed Rust tests and strict lint; later CI stages were
still pending at the health-integration checkpoint. Docs `52b099a` passed its
Windows/Linux portable and OpenSpec checks in
[40246379267](https://github.com/s116821/RemarkableBuddiesDocs/actions/runs/40246379267).
These results do not validate later service-health source changes.

A fresh read-only tablet query at 2026-10-25 23:15:47 UTC returned all 28 service
properties, including the new `Type` and `NeedDaemonReload`. Both existing units
report `Type=simple` and `NeedDaemonReload=no`; stock remains PID10366 with
invocation `0ba7fd058b8e4c399cca8f5e24a3bbf9`, Buddy PID11238 with invocation
`991fb85bd8c54b8f9b523979f3922183`, on boot
`02b2347b-03aa-4a85-8dd7-d731aabf6f3e`. These match the preceding inventory.
The source SHA256 is
`27e8c2acf3b039da149bd73dc7fa47ad80e7031899797f79d231533da807fb74`;
return code is zero and stderr empty. Original script, stdout/stderr and receipt
are retained locally in `recovery-properties-d35ccaedf8e649e2981b4bde93dd1317`.
Independent review checked the archive against its receipt and prior identities.
This establishes the property query, not execution of the Rust helper.

## Remaining integration

The next integration must enforce the common fixed boot latch in every installed
native-entry route, select an approved recovery/native profile, and install the
ordered watchdog/recovery units after actual main-loop health is integrated.
The explicit no-record command outcome above does not prove the installed lifecycle.
Do not reinterpret a missing/corrupt consumed lease as permission to reactivate.

Manager lifecycle must retain the helper/payload until verified recovery and use
the existing Vellum package ownership contract; there is no second ad-hoc installer.
Read-only inspection of Manager main `b8f04d406be76a767e9b1826a2ca32e54b765f81`
found service observation but no installed recovery hook to extend. This is a
delivery gap, not a reason to create an alternative installation engine.

Vendor deletion/no-migration semantics, real shutdown cancellation, actual native
bootstrap, Reader/Writer composition and document-preservation/write/persistence
acceptance remain open. Neither this source increment nor its tests qualify them.
Keep coordinated PRs open; do not archive or merge the incomplete feature.

Source basis: current Buddy/Manager source, executed Linux tests, direct read-only
tablet evidence and independent source/evidence review. No native restoration or
document-effect acceptance is claimed.
