# Independent controller for the bootstrap observer

The observer runs a copied Reader as its own child. The prior research actor
instead shadows the stock unit and invokes recovery from an EXIT trap in that
actor's group. Reusing that execution engine would change the launch being
qualified and would not supply independent recovery after actor-group termination.
Reuse its frozen packet, source manifest, intent and evidence conventions only.

Use a separate, development-only PID1 actor and ordered recovery service. Freeze
their complete unit policies, payload hashes, fresh nonce and document manifest
before selection. Do not create an installed production profile from sampled
state. No service changes or tablet execution follow from this design alone.
Use a bounded Type=exec actor: its main process runs in active/running, which
the baseline captures. A Type=oneshot actor remains activating/start and cannot
use this admission contract without separately modeled behavior.

## Original service evidence

Extract a read-only `service::baseline::ServiceBaseline` around the existing
GroupBaseline implementation. Capture an explicit validated unit's running
MainPID between identical bounded PID1 snapshots, verifying actual process
incarnation, namespaces and membership. Preserve the original policy and
systemd invocation/start timestamp separately from process start ticks.

`current()` must recheck that original snapshot and actual group/process before
and after the observation. `stopped()` must bracket the original group lookup
with bounded PID1 samples and preserve the existing installed stock-stop rules:
unchanged retained identity, or completely cleared inactive identity with
qualified original-group deletion. Reject population, changed policy or partial
clearing. Return typed retained/cleared identity plus EmptyOriginal/OriginalAbsent;
never return restoration authority. A legitimate stop transition may return
pending under the original deadline. Parameterize the unit identity and reuse
this same predicate for installed stock activation.

Provide a bounded encoded observation record for the independently ordered
helper. Decode through the strict service-property parser, validate the group
record and original running-state relationship, and reject unknown/duplicate
fields, incomplete records and excessive input. The controller must separately
protect and bind the record's exact bytes; a decoded observation is not a lease.

## Execution sequence still to implement and qualify

The diagnostic controller is an explicit example behind a development-only Cargo
feature, not an installed dispatch mode. Its fixed nonce selects the staging
directory and owned unit names; a bounded candidate record selects native or
isolated fixture mode. Fixture mode may address only the two nonce-owned fake
units and an owned source directory. Native mode fixes stock/Buddy units and
the reviewed observer paths. Native fault injection is forbidden. Unit text is
rendered deterministically and loaded policy is checked, including independent
runtime/stop bounds and shutdown ordering. Existing service policy defaults are
not changed to make this diagnostic pass.

The candidate binds exact original service baselines, executable and controller
hashes, a fresh complete bounded source manifest and external backup identity.
After validation, write one complete ownership record before consuming either
stop intent. A missing ownership record with any stop intent is an error.
Successful publication is durable; records and per-invocation recovery intents
are exclusive and never overwritten. Recovery failures remain recorded and may
be independently inspected. A durable per-service start intent survives helper
interruption: a later invocation may verify an already-running service but must
never repeat that uncertain start. Exercise interruption after publishing the
intent and after submitting the start request in isolated fixture mode.

Before stopping either existing service, verify fresh source preservation,
original service/process/artifact identities, the actual observer input guard,
and the independent loaded recovery path. Publish the actor and both original
service baselines durably before any stop intent. The PID1 actor must have an
absolute lifetime and control-group termination independent of SSH or its main
thread. Recovery must execute in a different service after actor termination.

Stop competing Buddy and stock at most once each with explicit pending intent
and non-replacing PID1 jobs. Prove both original groups terminal before starting
the fixed observer. Run it once, with no mutation, input injection or automatic
retry. Recovery must prove the original actor/child group terminal before stock
restoration, retain uncertainty, and verify the resulting stock process and
source preservation. Restore stock before running recovery source diagnostics;
their expiry or failure must withhold Buddy without preventing stock restoration.
Recheck input after authority sampling immediately before each stop, observer
launch and Buddy start. Account explicitly for shutdown interruption and partial
admission before permitting legacy Buddy restoration. Preserve every record,
log and payload until independently verified collection and exact cleanup.

Validate the read-only baseline with retained/cleared transitions, policy and
identity changes, populated/replaced groups, malformed records, racing snapshots
and deadline expiry. Then exercise controller failure and recovery with isolated
fake units before any real handoff. Existing kernel observations do not prove
privileged migration exclusion or arbitrary firmware behavior. Independent
review of the exact controller and fresh candidate remains required.

## Read-only baseline implementation

Buddy `13ce5b26020c4e3ca8d58211400db0682178a3b5` implements the baseline and
delegates installed activation's stock-stop predicate to its shared typed
implementation. Existing outer installed-profile checks remain in place;
the common predicate additionally requires equality with the original sampled
policy. It issues no service commands and provides no synthetic installed lease.

Four new host regressions cover bounded strict record round-trip and malformed
relationships, refusal to treat fixture files as kernel cgroups, typed terminal
observations, policy/identity changes on either side, partial clearing, populated
groups, racing transitions and expiry. Existing installed stock-stop controls
exercise the same extracted predicate. These tests model service snapshots;
they do not qualify live PID1 ownership, migration exclusion or recovery.

Independent source review accepted the implementation and identified the actor
service-type constraint recorded above. Formatting and whitespace checks pass.
Exact-revision hosted Checks passed in run 40261613767; the application build is
still pending. Local Rust builds remain unavailable with insufficient disk space.

## Controller source implementation

Buddy `884a07c799885f10b77beb60a462ac07f0f5aec7` implements the development-only
controller and independent recovery example with fixed native/fixture targets,
durable ownership and stop/start intent, original-group checks, artifact pins,
bounded input admission and stock-first recovery. Its separate PR diagnostic
artifact includes the controller and observer checksums and actual build-source
SHA. Installed release packages do not select the feature or contain these tools.

Independent source review identified and verified fixes for uncertain start
replay across helper invocations, late input checks and source diagnostics
consuming stock restoration's deadline. Six host tests include recovery ordering
and refusal after diagnostic expiry or uncertain stock restoration. Formatting,
whitespace and the focused artifact-workflow fixture pass locally. These Rust
tests have not yet executed for this revision; hosted compilation, full checks
and ARM artifact generation remain pending.

Isolated PID1 cases must still exercise normal completion, actor SIGKILL with
a child, runtime expiry, partial stop, recovery exit, interruption after durable
start intent and after queued start, repeated-helper refusal, source mismatch
and shutdown. No fixture fault execution, native takeover, service change or
document mutation is claimed by this source implementation. Native candidate
selection remains dependent on those results and fresh independent review.

## Isolated fixture driver requirements

The host-side driver selects a fresh nonce and exactly one fixture-mode actor,
followed by one explicit second helper invocation. It records every selected
command before dispatch, has bounded SSH observation, never replays on timeout,
and preserves failed evidence. It brackets the experiment with actual stock/Buddy
identities and artifact hashes while issuing service commands only for the four
owned fake units. Payload transfer, unit loading and fixture execution still
require the existing idle-development-tablet authorization and advance notice.

Verify the requested actor result and both helper outcomes, a distinct second
helper invocation, expected restored identities and durable refusal after an
uncertain start. Crash/timeout cases must first witness a live child in the
actor's original group. Publish readiness bytes durably before a completion
marker; parse and correlate the archived child identity/group with the original
ownership record. Empty/partial records or matching filenames cannot prove the
child-bearing fault. Preserve explicit recovery-fault phase markers as well.

Collect the control archive without extracting untrusted paths. Offline verifier
tests must reject missed faults, unchanged services when a stop was required,
accidental active-service restarts, repeated-helper snapshots, duplicate fields,
archive links, incomplete child witnesses and changed child groups. These are
evidence-verifier tests, not actual service-execution results. The first compiled
controller revision has passed hosted compilation/strict lint; its tests remain
running. The new child-handshake delta and driver still need their own exact
revision checks and live fixture qualification. Cleanup remains a separate
operation after verified collection and terminal owned-service/group checks.

Buddy `b4601c141738302bc791d540662248a8d476e464` implements this driver and
child-witness/fault-marker delta. Independent source review accepted the fixes
after identifying readiness publication and partial-witness false-pass races.
All ten offline verifier tests passed locally, along with formatting and
whitespace checks. Hosted CI now includes those verifier tests. This revision's
Rust checks and ARM artifact are still pending; no fixture run or tablet action
has occurred.

## Resume validation and native artifact refresh

The b4601c1 pipeline failed in an existing runtime startup test with
ConnectionRefused; the controller compiled and strict lint passed. The prior
884a07c controller pipeline completed successfully. The failure exposed a
bind/listen publication window in both the owned Python peer and native endpoint,
tracked in resident-runtime-integration.md. SDK
`83ed037636707ce8036774f04d19f28f42c0019a` implements reviewed atomic no-replace
publication after listen. Final host and ARM/QEMU endpoint suites pass 1825
checks each; these are owned endpoint results, not native Reader evidence.

The frozen rebuild in `endpoint-publication-library-r2` completed and all 48
input/artifact manifest entries were checked against current source and artifacts.
Adapter SHA256 is
`751098608084e342602c30a31807f5b578dbe4ad8ee4828dd82ad6c620b54eb2`;
profile SHA256 remains
`0ab8a72e32d978cbb0be14a01c6b0145240f83f13c64cdee6fef5431c411bdff`.
Mutation remains disabled. Buddy
`42a570ef7cadbcb01119824beba7f992999377c5` updates the observer's fixed adapter
pin with its SDK dependency and deterministic delayed-listen peer regression.
The first rebuild attempt is preserved and explicitly marked
unusable because source changed during compilation; it must never be selected.
The refreshed observer/controller CI and actual fixture/native runs remain open.
PR60 initially could not schedule a pull-request build because it conflicted
with upstream Reader personalization, Writer and handwriting changes. Buddy
`1a992291223d0de3af4c19c99d05bf7de71932a6` resolves the existing branch against
main `0ecdfc5`, preserving both exclusive early command paths, storage helpers,
Reader memory/personalization and the single sync worker before health readiness.
Independent source review accepted the merge for hosted validation. Reciprocal
CLI refusal cases and the handwriting health-entry fixture are included.
CI `40398709040` is the current combined-source run; do not credit the prior
controller's green build to this adapter or merged product code.

The fresh read-only prerequisite inventory in
`bootstrap-preflight-e301703907f54e8994514b379998aa6f` retains the same boot and
active stock/Buddy process and invocation identities as the earlier inventory,
with sufficient tablet storage and no installed resident profiles or latch.
It transfers no payload and performs no service or input action. Live fixture
and native qualification remain open.

## Current source checks and fixture preparation

Buddy `70c794159f153d33f9437136152d5e2641631c81` passes the Checks job in
`40399634191`: strict lint, 718 library tests with three separately ignored
cases, 12 binary tests, the full integration/CLI/simulator suites and ten offline
bootstrap verifier tests. The deterministic delayed-listen case passes. Earlier
combined-source runs are retained failures: `1a99229` referenced an inaccessible
test deadline helper, and `ec7e00e` retained unnecessary mutability after that
correction. Neither failure was suppressed; both were corrected before this pass.
The current ARM build and full application pipeline remain pending.

SDK `83ed037636707ce8036774f04d19f28f42c0019a` completes the full
`40397665119` pipeline successfully, including Linux/Windows checks, build and
integration. This qualifies the source/build boundary, not native activation.

Independent source review accepts the single clean fake-service invocation and
its separate cleanup. Cleanup must verify the collected control archive, original
real-service baseline, terminal actor/helper and exact runtime unit bytes before
stopping only the two stand-ins. It must bracket group observations with retained
boot/namespace/mount/slice context, compare surviving groups with fresh cleanup
incarnations and readable empty population, and distinguish explicit final-path
absence from missing parents, wrong types or other errors. Only then may the four
exact unit definitions be removed and reloaded, with real services verified
unchanged. Preserve staged payloads and control evidence. Source review is not an
execution result; the matching ARM artifact and live fixture evidence remain open.

## First compiled clean fixture: pre-ownership watchdog refusal

The full Buddy pipeline `40399634191` subsequently passed Checks, Build and
Integration. Its diagnostic artifact records build source
`ffce0bcf6899727c0766ceec0d48296e3c24f9b6`, whose tree equals Buddy `70c7941`.
Both manifest hashes and ELF32 ARM identities were verified. Controller SHA256:
`a123c3193cf0a4ed9a178ec615906b34e4905f495effd400b253b195181e9fdc`.
Observer SHA256:
`1e5537f933f9159190f1f154bc162debb1c3d67e0cdfc8757bf367abe1c785e3`.

The announced clean fixture selected nonce
`828e4398826b44138fd642fd0c76d641` once. It failed with
`unsafe diagnostic unit recovery: WatchdogUSec` before publishing ownership or
any stop/start/observer intent. Both helper invocations returned successful
no-ownership no-ops; this is not successful recovery qualification. The archive
contains exactly that actor error and two helper results. Original stand-in
invocations remained unchanged, as did the real stock/Buddy processes, service
definitions and stock executable. A subsequent read-only inspection confirmed
those identities and watchdog zero after the helper had run. No native adapter
was loaded. Preserve the failed selection; do not replay it.

The matching upstream systemd-stable v255.21 source explains the observed
transition: `service_init()` sets `watchdog_original_usec` to `USEC_INFINITY`,
`service_get_watchdog_usec()` returns it absent an override, and `service_start()`
copies the configured interval. The vendor patch set remains unknown; the
original run did not retain the pre-start numeric property. The next fresh
fixture therefore records that loaded policy before starting the actor.

The correction explicitly renders `WatchdogSec=0` and permits the infinity
sentinel only when the actor observes its never-started recovery helper:
oneshot, inactive/dead, no main/control/executed PID, start timestamp zero,
empty invocation/group/job. Exact rendered unit bytes and no drop-ins remain
required. Running actors and recovery invocations still require watchdog zero.
Regression coverage rejects each missing or contradictory sentinel field and
a finite nonzero watchdog. Formatting and ten offline verifier tests pass;
compiled checks and a new matching ARM fixture are still required.

The failed run requires separate cleanup admission, since the successful-run
cleanup requires ownership evidence that this refusal correctly never created.
Bind the exact error-only archive and original stand-in records, use the matching
stock/Buddy candidate group contexts, freshly prove actor/helper termination,
and apply the same owned-unit, group and real-service checks before removing
only these four definitions. Preserve payloads, candidate and control evidence.
Cleanup is now verified. The first selection refused during read-only admission
because BusyBox spells final-path ENOENT as `can't stat`. A separately reviewed
selection accepted exactly that diagnostic, stopped the original stand-ins once
and verified all four groups absent. Its failure reset cleared the actor but
returned errors for three already-unloaded inactive units. The final reviewed
selection repeated neither stop nor reset: it required fresh cleared terminal
states, group absence and exact unit bytes, removed only the four definitions,
verified not-found after reload, and confirmed unchanged real services. All
three selections and their source snapshots remain preserved. Future cleanup
resets only freshly failed units. This cleanup result does not change the
original fixture failure.

The same lifecycle distinction applies to installed activation's idle-helper
admission. Its approved profile must specify watchdog zero for the helper;
the idle check may match the infinity sentinel only with the complete
never-started predicate above. All other profile policy values still match
exactly, and active recovery must match zero normally. Share the predicate
between the diagnostic and installed paths, retain the approved unit hash and
no-drop-in requirements, and test first-use, already-used, changed policy and
partially populated service identities. This does not create or install a
production profile or authorize a native session.

Buddy `ce8bd9058385324b9417699b57b98ec48d81ca77` implements the diagnostic
correction; `4e7a0d7b58347ad758ac956bd7c4e2c8c11e29fd` shares that predicate
with installed activation and constrains its helper profile to zero watchdog.
Independent source review accepted both, including strict active-helper matching
and first-use versus previously-used helper tests. Source formatting and
whitespace pass. Hosted validation and the next fresh compiled fixture must use
the latter revision; no earlier green run validates these new paths.

## Cleared services and uninitialized runtime watchdog observations

Source review identifies the same runtime-property distinction after PID1
garbage-collects and reloads a stopped unit. This is not yet a live fixture result.
An exact policy comparison against the original running interval would reject
`infinity` even with all invocation metadata cleared. The affected paths include
the original-service baseline, diagnostic restoration, installed stock-stop
admission, original Buddy recovery admission and native stock observation.

Preserve raw snapshots and represent this case as a typed cleared/uninitialized
watchdog observation. Require inactive/dead, main/control/executed PID zero,
start timestamp zero, empty invocation/job/control-group fields, and separately
verified group absence under the retained context. The original service type
still matches its approved policy; this case is not limited to oneshot helpers.
Only the runtime watchdog value may differ from the original approved interval.
All other policy values, original identity and artifact checks remain in force.
Retained, running, stopping, partially cleared, replaced or populated cases must
retain strict watchdog comparison. Group absence must be established before
using the exception, including the native stock path that previously compared
policy before its group check. No snapshot or approved profile is rewritten.
Regression cases must cover zero and two-minute original watchdogs, changed
non-watchdog policy, every partial clearing, stable observation brackets and
empty-but-existing versus absent original groups.

Implemented in Buddy `9df989274e91782ceee7f845ca87167c6a0baf13`.
Independent source review accepted the five affected paths and their retained
raw observations. Predicate and policy regression tests do not exercise the
complete native stock observation sequence. Hosted run
[40407288991](https://github.com/s116821/ReMarkableBuddies/actions/runs/40407288991)
has passed formatting and strict all-target/all-feature Clippy; its test and
artifact stages remain pending completion. A fresh compiled fixture is still
required, followed by separate native qualification. Neither the previous
helper fix's green checks nor this source review proves those runtime gates.

Follow-up review found an earlier diagnostic-unit gate that could still reject
a fully cleared actor's uninitialized watchdog before original-group proof.
Recovery must decode and validate its durable ownership first, then admit this
actor-only sentinel through the original actor's stopped/absent observation and
a fresh matching service snapshot. Exact diagnostic unit bytes, no drop-ins and
all other policy checks remain required. The running recovery helper gets no
such exception. Missing ownership permits no service restoration; it does not
justify relaxing the actor watchdog check.

Buddy `49402bd16511a136f74f242991f0a6c8ef70eea4` implements this follow-up.
Independent review accepted the production path and corrected complete policy
fixture. Regression coverage checks proof-before-resampling, failed/missing proof,
retained identity, existing/populated groups, changed policy, unstable service
snapshots, read errors and ownership-free refusal. Formatting and whitespace
checks pass; hosted compilation and the fresh clean fixture remain pending.
This revision supersedes `9df9892` as the next diagnostic artifact selection.

## Disposable source-change recovery case

Keep the reviewed `49402bd` clean-case controller and host inputs frozen while
adding source-mismatch coverage separately. Never credit that frozen build with
the new fault path. The explicit fixture-only `source_mismatch` case adds one
new file under its nonce-owned disposable source directory after the stand-in
observer has exited successfully. It must never touch the native document root.
Record the injection durably before the actor's ordinary preservation check.

The expected actor result is source-manifest refusal. Each of two independently
selected recovery helper invocations must restore/verify the same new stock
incarnation, record the preservation refusal, and withhold Buddy. Require both
stop intents, the completed observer, the injection marker, exactly two failed
preservation receipts and no Buddy start/restored record. Live state must prove
stock restoration without a second restart and Buddy terminal throughout both
helper observations. Native mutation remains disabled; shutdown and the other
recovery cases remain separate qualification requirements.

Implemented in Buddy `9d803c9acf534c7b7118abf617e6d755b3820f65` and accepted
by independent source review. All twelve offline evidence-verifier tests,
formatting and whitespace checks pass. Compiled and device fault evidence are
pending. The frozen `49402bd` run continues only for its reviewed clean-case
question; it cannot validate this source-change injection or the current head.

## Recovery trigger transaction mode

Matching upstream systemd 255.21 commit
`70500d37992a01d3275b1c414c3ed161d6f91f9e`, `src/core/unit.c`, initializes
failure triggers with `JOB_REPLACE`, success triggers with `JOB_FAIL`, then
passes the selected mode directly to `manager_add_job`. Existing shutdown
conflicts and ordering do not choose that transaction mode. This is a source
policy gap, not an observed tablet shutdown failure or vendor-patch equivalence.

The diagnostic actor must explicitly render `OnFailureJobMode=fail` and
`OnSuccessJobMode=fail`, then verify both loaded properties. Missing values,
`replace` and other modes refuse admission. This prevents the trigger from
replacing conflicting existing jobs; it is not a general shutdown inhibit and
does not complete shutdown qualification. Future installed Buddy trigger policy
needs the same requirement before approval; retain the vendor stock policy.

Buddy `068c5328d252900739cee4611367fb56c7d7994d` implements the diagnostic
requirement and records both loaded modes in the host policy capture. Independent
source review accepted the change; formatting, twelve offline verifier tests and
scoped strict OpenSpec pass. Compiled and live evidence for this revision remain
pending. Frozen `49402bd` Checks job `121873106695` has passed in run
`40408694687`; its separate ARM build remains live for the clean-case question.

## Reloaded dependency ordering: observed refusal and correction

The frozen `49402bd` pipeline subsequently passed completely. Its build source
`c8b638eaa4c6064c4fb3d6cd28050604a0c1c3b1` has the same tree as that reviewed
head; the downloaded archive digest, binary checksums and ARM ELF identities
were verified. Controller SHA256 is
`799fb86c385e81f1d5276b09b1510ed957ced0fa7d03d8ff32fc0a3b37b8d337`.

Fresh clean fixture `3b69df8947f14223b667238e883d20b6` failed after publishing
ownership and stopping only its disposable Buddy stand-in. Actor and both
planned recovery invocations reported `service policy changed during stop`.
Neither stock stop nor observer launch was admitted. Both helpers verified the
unchanged stock stand-in and unchanged disposable source, then refused Buddy
restoration. Actual stock Reader/Buddy service identities remained unchanged.

The retained original and fresh cleared Buddy snapshots contain the same four
`After` dependencies in different order: `system.slice sysinit.target
systemd-journald.socket basic.target` versus `systemd-journald.socket basic.target
sysinit.target system.slice`. Its other policy difference is the already modeled
cleared `WatchdogUSec=infinity` sentinel. This is a failed fixture, not successful
recovery qualification. Separately reviewed cleanup stopped only the exact
original still-running stock stand-in, proved terminal groups, removed the four
definitions and confirmed unchanged real services. All evidence remains retained.

Compare `After` and `Conflicts` as unordered, duplicate-rejecting unit lists in
explicit policy matching, including the stopped baseline and diagnostic restore
paths. Share the existing installed recovery token validation. Keep raw snapshot
equality, encoded candidates/ownership, and property access unchanged; do not
normalize evidence. Preserve strict comparison for every other policy and the
separate original-group proof required by the watchdog exception. Regression
coverage must exercise reordered dependencies together with cleared watchdog,
added/removed/duplicate dependencies, unchanged raw serialization, and unrelated
policy changes. A corrected source build and fresh fixture remain required.

Buddy `59ab44e5147f6f130c59c3967ed7bcf9db5c4998` implements this correction.
Independent source review found no production-code blocker and corrected one
test expectation: changed raw samples yield pending (`Ok(None)`), not an error.
Formatting, whitespace and twelve offline bootstrap verifier tests pass; new
Rust regression execution and the matching ARM artifact are still pending.
Earlier `068c532` Checks passed 724 library tests (three ignored), twelve binary
tests and the integration/simulator suites, but do not validate this correction.

## Dependency ordering across terminal observation brackets

The full `59ab44e` pipeline `40413867926` subsequently passed, including both
dependency-order regressions. Build source `0b5a10566f7b4969a31c5f9d85bda5a8c53f114b`
has the reviewed tree. Its verified ARM controller SHA256 is
`ca60c48c1e35a7662b93c557a78c0a05266ecbef28dda1ae0cc3a08b4cce005f`.

Fresh fixture `2cfbbd565ecd4d099f9be2f227685fcd` stopped only its disposable
Buddy stand-in, then its actor reached the service-observation deadline. Both
planned helpers refused `recovery target policy changed before terminal state`.
Ownership and Buddy stop intent are the only effect records; stock stop, observer
launch and restoration-start intents are absent. Both helpers verified original
fake stock and unchanged source. Real Reader/Buddy identities remained unchanged.
Separately reviewed cleanup stopped only the original active fake stock, verified
terminal groups, removed all four definitions and preserved the collected evidence.

Four subsequent read-only full snapshots of the cleared Buddy contain identical
fields except `After` ordering: the first pair differs, the middle pair matches,
and the final pair differs again. Policy matching accepts these equivalent lists,
but raw snapshot equality in the terminal bracket can return pending indefinitely.
This also explains why recovery cannot obtain its required terminal observation;
the historical actor samples themselves were not retained, so that attribution
remains a mechanism supported by the fresh reproduction, not a reconstructed trace.

Use an explicit stable-observation comparison after existing state/identity/group
qualification. Require the same field set; compare only `After` and `Conflicts`
as duplicate-rejecting unordered lists. Every other field remains exact, including
watchdog value, invocation, PIDs, timestamp, pending job, state, control group and
all other policy. Keep raw equality, serialization and candidate bytes unchanged;
equal raw malformed lists must not bypass duplicate rejection.

Apply this to baseline and installed stock terminal brackets, original Buddy
recovery observation, cleared actor/stock watchdog resampling, the final startable
stock recheck after group proof, and the already-validated idle helper comparison.
Keep active-incarnation checks exact. Regression coverage must reproduce two
different permutations in one terminal bracket and preserve changed identity,
group, policy, runtime-watchdog and pending-state refusals. Independent review
accepted the terminal-bracket direction; final source and compiled/device checks
remain required. This does not extend the actor deadline or replay the failed run.

Buddy `cdeb0bb604a83cc01cf72e4ffb9e04bad53b5182` implements the correction.
Independent source review accepted all seven comparison sites, including the
post-group startable recheck and validated idle helper. Regression source covers
changed/missing fields, duplicate self-comparison, cross-sample permutations,
original-group refusal and one-start/no-start recovery behavior. Formatting,
whitespace, scoped strict OpenSpec and Docs manifest/guidance/source checks pass.
Compiled checks and a fresh corrected artifact/device fixture remain pending.
Previous `db5fd13` Checks passed 729 library tests (three ignored), twelve binary
tests and the integration suites; those do not validate this correction.

## Durable diagnostic completion observation

The full cdeb0bb pipeline passed. Fresh disposable fixture
`3e615cf3a7434ff981c17c9dcbbfefd8` recorded successful actor and first recovery
results, restored both stand-ins, and preserved real services. The Python driver
timed out because PID1 cleared the successful helper's invocation and start
timestamp before polling. No second helper was selected. Separately reviewed
cleanup completed; this remains an incomplete fixture, never a retroactive pass.

Correct the diagnostic driver only. Read the bounded nonce-specific control
archive with a successful collection status. For a cleared successful helper,
require exactly one new strictly named recovery result containing `Ok(())\n`,
then resample fully cleared terminal state (no PID, job or invocation). Preserve
all previous result filenames and hashes; freeze the first map before selecting
the one second helper. Its success needs exactly one additional successful result
and unchanged earlier bytes. Result UUIDs are independent of recovery-attempt
UUIDs and must never be correlated. Retained failed helper timestamps remain
usable for intentional signal faults that cannot write a result. Keep all existing
effect, restoration, source and state assertions and check final result stability.
Missing, stale, changed, extra, malformed or incompletely collected evidence
cannot authorize the second helper or constitute completion. Keep the original
deadline and no-replay behavior. Offline driver regressions and independent review
precede a fresh isolated fixture; none of this qualifies a public native SDK.

Driver `255506e1869e73460bee909511664596c936a674` implements this correction;
21 offline regressions pass and independent review accepted the final delta.
Intermediate collections use `completion-archive`, preserving the cleanup
contract's one final `control-archive`. Fresh clean fixture
`7cc413de5e46451ea9adb54e18928f1b` passed with the frozen cdeb0bb controller
(build source `4ab85a48e2ff5171a8da71d167d3fd322cb213bd`). Both helpers returned
success with distinct durable results; earlier result bytes remained unchanged,
both source checks passed, and both restoration receipts stayed identical across
helpers. The second helper did not restart either stand-in. Separate cleanup
passed, removed all four definitions and preserved payloads/evidence. Real
stock/Buddy remained unchanged. This is disposable PID1 fixture evidence;
remaining fault/shutdown cases, native runtime and installed/product acceptance
remain separate open work.

## Isolated failure and queued-trigger results

The same frozen cdeb0bb controller and independently reviewed 255506e driver
subsequently passed all seven selected disposable-service failure cases:

| Case | Fresh identity | Observed behavior |
| --- | --- | --- |
| Actor SIGKILL with child | `f516b2f3b0e54c2ab72ac2bd552cf38a` | Child witness recorded; actor group terminated; both stand-ins restored |
| Actor runtime expiry | `cf9a769c3cd540d3af69d7f1e26728c4` | PID1 timeout terminated the child-bearing group; both stand-ins restored |
| Failure after Buddy stop | `3dac5c0a245649199eafb888fed62118` | Original stock retained; Buddy restored |
| First recovery exits | `648a8dc2e1084648a2a68a5354c07c63` | Second helper restored both stand-ins |
| Recovery dies after start intent | `58457f2968e342578069f02f9aacad41` | Second helper refused uncertain start replay; both stand-ins remained stopped |
| Recovery dies after submitting start | `1d782628f11c498b8a2f69900ea392cd` | Existing stock instance verified; Buddy restored without another stock start |
| Source mismatch | `f2701fa42d4647baacc1ab783d5f313c` | Stock restored first; both helpers refused preservation and withheld Buddy |

Each case passed the unchanged effect/source/state assertions and separate
receipt-bound cleanup. All owned definitions were removed; real stock/Buddy
identities and policies remained unchanged. These are actual vendor PID1 runs
against disposable units, not native document or installed lifecycle acceptance.

The synthetic queued-target experiment also passed all four controls with separate
cleanup: fail/success `f25d5ef9a7a04d418c1e9292190f18cc`, fail/failure
`dfd412112fc44628ad376c44afe2dc93`, replace/success
`0263e4d1a0924fbcab90fa6311921676`, and replace/failure
`8b968e55844b41ac8e76a64f0c75ddf4`. Fail mode rejected the destructive recovery
transaction, retained the exact pending target job and never invoked the helper;
the target subsequently completed. Replace mode invoked the helper and canceled
that target job, establishing the negative control. This covers the vendor
scheduler's queued-conflict mechanism only. Actual reboot, shutdown, power-loss
and installed-profile behavior remain unqualified.

## Original-service dependency ordering across reload

Native candidate `2cae38feca39406cb5267a526e33bb54` refused before actor start:
installing the two diagnostic definitions and reloading PID1 reordered `After`
in the original stock/Buddy baselines. Source, executable/unit bytes, service
incarnations and group context remained identical. The candidate is spent; this
is not a native observation pass. Separate unused-definition cleanup is required.

That separately reviewed cleanup subsequently completed in 22 bounded calls:
both definitions removed and unloaded, both diagnostic groups absent with matching
namespace/mount context, original real-service identities and source unchanged.
No service start, stop or reset was issued. The failed execution receipt and
payloads remain preserved. The preceding full Buddy `255506e` CI pipeline passed;
it does not validate the subsequent comparison correction below.

Correct original-service comparison as well as the earlier terminal comparison.
Only duplicate-free `After`/`Conflicts` permutations may compare equal. Validate
both selected and fresh baselines, compare every other snapshot property exactly,
and require exact full group/process/context identity. Both samples surrounding
the live process check use this rule. Raw encoding and recorded evidence remain
unchanged. After proving the fresh baseline matches selection, ownership retains
the original candidate strings so recovery's candidate/ownership byte binding
does not change. Apply the same rule to existing restored-service receipts; it
must never authorize another start or conceal a changed incarnation. Host-side
inspection follows the same narrow dependency rule without rewriting the frozen
candidate. Test changed membership, duplicate self-comparison, all nondependency
fields and group identities, raw encoding preservation and ownership binding.
This correction removes an availability refusal, not a native capability gate.

## Native preparation must verify the installed invocation

Corrected build `4401852` passed its full CI and fresh clean fixture
`d55deb69d08044b0add8c262b7efef39`, followed by separately reviewed cleanup.
Native candidate `aee25250ed524cf5adfc31d117a78327` then reached actor admission
but refused with `running process argv mismatch`, before ownership publication,
stop intent or observer launch. Its control archive contains only the failed
actor result and successful no-effect recovery result. Stock and Buddy retained
their original running identities. This candidate is spent, not a native pass.

Read-only process inspection confirmed stock's `/usr/bin/xochitl --system` and
Buddy's `/opt/bin/reader-buddy` invocation. Buddy's actual executable and that
symlink target are `/home/root/.local/lib/reader-buddy/reader-buddy`. The diagnostic
must distinguish exact command-line spelling from canonical executable identity:
expect the reviewed installed alias in argv, while preserving canonical path,
executable hash, process incarnation, loader-environment and group checks.
Do not accept arbitrary aliases or infer arguments from untrusted process state.

Run the same process verification during read-only preparation inventory as
during actor admission and restoration. A command-line incompatibility must
therefore refuse before candidate selection. Include the service role in errors.
Exercise an actual child whose argv[0] differs from its canonical executable,
checking exact alias acceptance and rejection of a substituted argv, executable
hash, incarnation or loader environment. This is diagnostic admission work;
installed activation and native page capabilities remain unqualified.

The separately reviewed cleanup of `aee25250ed524cf5adfc31d117a78327` subsequently
passed. It verified the exact terminal invocation, absence of both diagnostic
groups, unchanged original services/source and the two-result control archive;
cleared only that actor's failure state; removed/unloaded both definitions; and
rechecked those invariants. No stock/Buddy start or stop occurred. Failed receipts,
payloads and control evidence remain intact. The correction is implemented at
Buddy `36e5f5681f5f1d0f70dc5f28e021fc0094441791`; its fresh CI and native evidence
must be evaluated independently of the prior successful `4401852` build.
