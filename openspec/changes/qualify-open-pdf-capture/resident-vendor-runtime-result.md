# Owned companion runtime source checkpoint

This implements the runtime portion of the [companion lifecycle](resident-vendor-companion.md).
The fixed measured RM2 selection is explicit in `Launch`; all existing installed
activation and disposable-bootstrap callers still pass no companion. They cannot
silently adopt a new service contract. No new native activation occurred.

## Implemented source

The runtime pins the original executable, binds exec to its retained inode, keeps
the original argv0 and owns the Child handle throughout the session. It applies the
fixed environment, working directory, nice level and umask without inheriting
injection or service notification variables. Metadata, process incarnation,
executable link/inode and exact command line are checked during progress. A retained
descriptor does not make root-writable executable bytes an atomic snapshot.

Reader starts before companion; both exist before SDK handshake. Broker readiness
is required after the handshake so the reader's main-loop startup cannot be blocked
by a circular wait. Startup and admission share the original deadline. The broker
must identify the owned companion, with its unique owner and broker ID retained
across later request admission/delivery and reconnect.

Witnessed process or broker integrity failure permanently retires the companion
session; restored historical broker evidence does not enable reconnect. Typed
caller cancellation/deadline remains ordinary request retirement, while integrity
and an unreaped helper retain precedence. Pending SDK effect uncertainty stays in
the existing journal. Direct unguarded connection access refuses a two-process
session; requests use progress and delivery admission.

Shutdown dispatches companion termination before reader termination, then waits
under one original deadline. It retains separate child results and reports overall
reaping only when both are reaped. Failure to reap still requires independent group
recovery. A partial companion spawn failure cleans up the already-owned reader.
The initial `0e414236` increment retained forced KILL cleanup. Fresh read-only
loaded-unit inspection confirmed the vendor's TERM-then-KILL policy; the ordered
shutdown follow-up below implements that bounded source path. Separate reaping
evidence still does not establish graceful vendor persistence.

## Source validation

The host fixture uses real owned Linux processes and an explicitly synthetic broker
file. It covers handshake-dependent companion readiness, launch environment,
same-session reconnect, missing/dead companion startup, foreign broker ownership,
sticky refusal after original evidence returns, ordinary cancellation/deadline,
partial spawn cleanup and uncertain dispatched insertion after companion death.
It does not prove actual D-Bus behavior, vendor functionality, native mutation or
installed two-service restoration.

Independent review found and resolved cancellation misclassification and a missing
sticky integrity state. The first host run compiled and passed 29 tests, but three
new tests failed because their reader fixture omitted required arguments; the
fixture arguments were corrected. The revised full runtime suite passed 34 tests;
its spawn-failure fixture instead produced a child whose executable identity was
rejected, with both children reaped. The fixture now uses a missing interpreter to
exercise an actual spawn error without relying on ENOEXEC behavior. All seven
companion tests and strict all-target/all-feature Clippy then passed on Buddy
`0e414236437ac1f405f7376e4ef723310aaa2c77`; production code is unchanged from
that 34-test run. Formatting/whitespace checks passed. The fixed profile digest was
independently compared to the measured vendor digest and matches. The preserved
host logs retain missing Git metadata warnings; they do not identify an ARM build.
Docs guidance and all 88 strict OpenSpec items passed before publication.

A later test refinement requires handshake evidence and a typed startup deadline
for the absent-broker case. It exposed two fixture limits: a two-second bound could
end before companion launch, and the reader's three-second socket timeout could
end the reader before the expanded startup deadline. The companion test now uses
a five-second startup bound and a dedicated ten-second reader-fixture idle bound;
other reader fixture modes retain their original timeout. A test-only witness at
the successful missing-owner return additionally proves startup reached broker
observation, rather than merely creating the handshake marker. Independent review
accepted this coverage refinement. All seven companion tests and strict
all-target/all-feature Clippy passed on final test revision
`08576dbec7cdd375dd97468b1570f62a98f6965d`; formatting and whitespace checks passed.
Production behavior remains that of `0e414236437ac1f405f7376e4ef723310aaa2c77`.

## Ordered shutdown follow-up

Buddy `ba143d81e39fb544d5b369686329444a56049dba` implements the fixed phase
boundaries in the lifecycle contract without extending the original two-second
cleanup cap or caller deadline. The explicit two-process path requests companion
TERM, observes its completion or allocated timeout, then terminates the reader.
KILL escalation and final reaping have reserved intervals. An exhausted deadline
still reaches forced dispatch for both retained children. One-process callers keep
the earlier forced-cleanup policy.

Each child retains ordered signal attempts/errors and actual exit code/signal;
the overall report includes both child receipts and succeeds only when both were
reaped without an error. Signal dispatch alone does not imply termination. The
emergency companion destructor remains bounded forced cleanup.

Independent source review accepted this implementation. All 39 runtime tests,
including explicit root-only fixtures, passed, as did strict all-target/all-feature
Clippy and formatting/whitespace checks. Cooperative handlers are installed before
readiness and prove the companion is reaped before the reader's TERM handler runs.
Other cases require KILL when both children ignore TERM, preserve a modeled signal
failure while still stopping the reader, and verify forced dispatch after deadline
exhaustion. That last fixture retains its actual Child handles for separate cleanup;
it never signals a saved PID from a report. These tests use real owned host processes
with synthetic broker/fault evidence and do not reproduce the vendor's ninety-second
stop allowance or establish native data preservation.

## Versioned disposable service admission

Buddy `6d9224b3d4e26c928380c59c19dde40666e6d77d` adds the shared fixed-profile
vendor admission module and connects it to the disposable controller/observer.
Candidate version 3 explicitly carries the original sync baseline; ownership
version 2 binds those exact bytes to the candidate digest. Older candidates and
fixture candidates cannot opt in. A separate strict loaded-policy parser preserves
the existing baseline serialization and its watchdog-reset handling.

Admission pins the original sync executable, unit and drop-in, firmware/kernel,
loaded dependencies, launch and termination settings. It observes original sync
process/argv, group and broker ownership before stock stop. The controller's stock
stop waits for both original services and groups, and includes sync in subsequent
terminal checks. The observer selects its companion profile only from the pinned
candidate and checks original sync termination at admission and delivery.

Recovery never starts sync separately. A new stock start waits for the original
sync group to drain, including after controller interruption, and rechecks before
dispatch. Already-active stock is independently observed. Recovery retains the
exact stock baseline written to its restoration record; it does not recapture a
possibly replaced process. It waits for dependency-driven sync activation and bus
name readiness, retaining the first captured incarnation. Missing name is pending;
replacement or integrity loss refuses. Both restored incarnations remain retained
through source checks, Buddy restoration and final verification.

Independent review identified and verified fixes for the asynchronous name race,
stock recapture and missing sync-drain admission in interrupted recovery. On final
source, all 118 Linux host supervisor tests and strict all-target/all-feature Clippy
passed; formatting and whitespace checks passed. New tests cover policy/schema
changes, duplicate and reordered dependencies, absent-name-to-ready, replacement
during waiting, canceled/lost delivery, candidate/ownership version boundaries and
retained-pair orchestration. The first draft's 115-test/lint result is preserved
separately and is not evidence for the corrected source.

These are source and host-model checks. The existing PID1 fixture models stock and
Buddy; it does not model native vendor-pair transitions or broker ownership. No ARM
artifact, new native candidate, vendor-pair execution, capture or recovery result is
claimed here. A separate new staging script has only been syntax-checked and remains
unexecuted and unqualified. Existing spent candidate inputs remain unchanged.

## Installed wiring and sampled group ownership

Buddy `3a4b53af8750e92377a8c64e2ba353841a058629`, with final launch-deadline
guard at `e919f4aecac0a2ac382c0aead09bd2a69e806f64`, connects the shared vendor
admission to installed activation and independent recovery. Recovery profile v2
explicitly selects `rm2-3.28.0.172-v1`; lease v3 retains the original sync baseline
in the same boot/cgroup context and a distinct service group. Profile v1/lease v2
preserve their one-process contract. Version, profile or baseline mismatch refuses.

Activation retains original sync before lease publication, rechecks it at the
final stock-stop boundary, then checks cancellation/health again before dispatch.
Launch and session checks require both originals stopped. Sync termination is
sampled inside stock's before/after bracket. Independent recovery waits for original
sync drainage before a new stock start and verifies it again at dispatch; active
stock is not restarted. It retains restored sync through closing admission and
returns a separate sync process/invocation receipt. No installed profile is shipped,
generated from live state, approved or installed by this source change.

The companion runtime now retains parent membership bytes and namespace
descriptors, sampling parent/child/parent membership and namespaces between child
PID/start checks. Observed loss is a sticky integrity failure. The launch deadline
is checked again after the final parent sample and before spawn. Recovery still
depends on its separately qualified directory identity, drainage and trusted
no-migration/fork-inheritance premise; sampling is not proof against unobserved
migration or movement after supervisor failure.

Independent review accepted the corrected source. On final `e919f4a` source,
all 40 Linux host runtime tests and 123 supervisor tests passed, as did strict
all-target/all-feature Clippy, formatting and whitespace checks. The earlier r1
installed draft passed 123 supervisor tests/lint; r2 passed both suites/lint before
the final spawn-deadline guard. Those logs remain separate from final r3 evidence.
New regressions cover profile/lease compatibility, baseline context and distinct
group binding, delayed/lost sync drainage, independent sync restoration/closing
failure, and sticky membership/namespace refusal with owned-process cleanup.
Injected membership mismatches fail at the parent sample; child-only divergence
and actual kernel migration are not independently tested.

At that source checkpoint, the new version-3 staging script had passed source
review for preparation only and remained unexecuted. The following attempt used
fresh verified artifacts and matching fixture/cleanup evidence.

## First version-3 native attempt and startup refusal

Full Buddy CI `40770948819` passed for PR head `e919f4a`, building merge
`8cc20ebdc8f1fda5325baef648985fde15d929d7`, tree
`755fde1ff0d3a36f2b5af37575a60ff25cf84cad`. The separately reviewed merge adds
unassociated-feedback storage paths; the bounded diagnostic review traced the
observer's fresh format-1 Store without selecting that feature. Archive and ELF
identity checks passed. The exact controller passed one clean fake-service PID1 fixture
and its separately verified cleanup. This fake-service case does not model the
vendor pair.

Fresh candidate `e4c06d386f8f4c21a982a3ea6683d95b`, digest
`cda5af11e99015b0d779abdb29dc404d6baee967c86a866531f5938401022957`, was staged,
independently reviewed and executed once. Its version-3 contract retained original
sync along with stock/Buddy and the complete 191-entry source inventory. The SDK
`80b29eb` profile remained mutation-disabled. Original services stopped, but the
owned Reader failed the first post-spawn executable/incarnation comparison before
companion spawn. The observer recorded startup failure, reader cleanup with
SIGTERM/reap, no companion child and no pending mutation. Both native output logs
were empty. There was no setup-ready record, screenshot, tap, capture or mutation.

The independent helper restored stock, dependency-driven sync and Buddy, retaining
the matching three restoration receipts and successful source-preservation result.
Separate cleanup rechecked live source/service/companion identity, proved diagnostic
group absence, reset only the failed diagnostic actor and removed its two definitions.
Closing checks confirmed unchanged restored services, full source inventory and
companion baseline. All failed inputs and records remain preserved; the candidate
is spent and is not replay authority. This is native evidence for this failed-startup
recovery case, not successful owned-pair startup, capture or installed activation.

A separate bounded screenshot after cleanup was retrieved and visually inspected:
the restored stock UI showed the normal My files screen. The screenshot helper
terminated successfully; all three service snapshots and the 161-file source
hash manifest were unchanged across capture. This visual observation establishes
neither native page identity nor SDK authority.

The failed comparison combined inode equality with start-tick equality, so its
record does not identify which check failed. Buddy revision
`6a67d19b894c314f5f70b14e27311e995b2ad618` retains
both expected/observed values, executable symlink target and sampling errors while
preserving refusal and owned cleanup. It introduces no identity relaxation, wait
or retry. An exec-race explanation remains unproven. Focused host controls inject
the two distinct identity mismatches; they do not reproduce the native cause.
All 41 runtime tests, including root-only cases, and strict all-target/all-feature
Clippy passed on the diagnostic source. All 88 strict OpenSpec items and the Docs
checks passed. No native result is attributed to this later diagnostic revision.

## Remaining integration

Both installed and disposable source paths now explicitly select the companion
through their new versioned contracts. Approved profile packaging/installation,
broader exact-artifact PID1 fault checks and fresh bounded native runs remain required.
No actual installed or disposable vendor-pair lifecycle is qualified by these
host checks. Host shutdown is not a guardian
recovery result. Native capture, automatic creation/reuse for Reader,
Writer and blank-start, broader simulator acceptance and coordinated delivery all
remain required.

Source basis: current runtime/request source and independent review; host-process
fixtures with synthetic broker evidence. The native profile constants come from
the earlier read-only vendor observations, not a successful owned companion run.
