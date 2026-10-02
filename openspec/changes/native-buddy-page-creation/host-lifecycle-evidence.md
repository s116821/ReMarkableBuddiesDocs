# Host-only E0 evidence checkpoint

Status: bounded independent acceptance, not completed REM25 or candidate selection.

Exact original Buddy source6fe9da35da79cf720511034261b60abf7e776a50 implements
this change's E0 experiment. It references Docs plan1b8ea1b7345a2983d72f6b90fa4cb982ff257c26
and corrected SDK contracte2b3ebbb8c4c630e46041896bc266498518de437. Author21
unit tests passed22.163s Windows. Independent Sol reproduced frozen21tests in34.375s
and a real silent-child handshake refusal2.047s, reaping the child and closing pipes.
Review drove exception-safe constructor/child-startup cleanup and rollback deadline
corrections; initial1c1614a was not accepted unchanged.

The deterministic policy model covers scope rejection, compatibility/protection
refusal, duplicates, session cutoff and interruption. Separate owned fake guard,
Supervisor and runtime children verify actual process exits/start identities, exact
stock bytes, preservation of unrelated bytes and transaction-only cleanup. Supervisor
death at explicit stock/preflight/armed/partial/activating/Ready/rollback barriers is
observed independently by the guard. An actual blocked rollback watchdog becomes
RecoveryFailed after five seconds; a deadline never proves successful recovery.

Limits remain explicit: guard-alone death leaves an unprotected failure with
Supervisor alive. Runner orphan cleanup is not guard recovery. Simultaneous loss and
clean simulated boot reset are host assumptions, not service-manager/firmware evidence.
Synchronous filesystem operations cannot be interrupted at exactly five seconds;
late completion refuses a success claim, while the independent30s outer host-process
watchdog provides the final harness bound. Production recovery under blocked I/O,
real stock boot, licensing, installation, fresh source/action handoff and native
semantic operations remain unqualified. Tests do not exhaust arbitrary scheduler or
filesystem faults. No E1 activation is authorized by this checkpoint.

[Canonical evidence comment](https://linear.app/magentumdragon/issue/REM-25#comment-7a188a33-9e11-4b39-9ad9-2788e5f85ba1)
records exact review attribution. Public contributors can run the original harness
with Python without Linear, credentials or a tablet. No raw private firmware or
runtime locators are included. All broad qualification/delivery tasks remain open;
no canonical spec sync or archive follows.

Source basis: exact public source/specification revisions, observed author commands
and visible independent Sol review. Native behavior is unverified.
