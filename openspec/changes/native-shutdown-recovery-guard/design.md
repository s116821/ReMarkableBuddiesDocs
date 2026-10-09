## Context

Main's fresh RM2 observation: firmware3.28.0.172, stock PID291/start561, protected14document+10baseline hashes unchanged. Stock effective OnFailure=remarkable-fail.service, OnFailureJobMode=replace, FailureAction/StartLimitAction=none, Restart=on-failure, RestartMode=direct, TimeoutStopSec90s, WatchdogSec60s, KillMode=control-group, SIGTERM then SIGKILL. These values require fresh exact validation at selected execution; source notes are not a current baseline. Original native crash outcome remains separately preserved.

## Goals / Non-Goals

One fresh diagnostic can recover under an independent actor even after host loss. Before first stockstop prove an owned runtime guard setting Unit OnFailure empty, FailureAction/StartLimitAction none and Service Restartno. Retain guard while stopping candidate and proving exact process/cgroup absence. Observer-only mode has no FactsEntry; explicitly selected pretoken mode installs its fenced setup cohort only. No pagegetter, reader/request admission, input, forcedrender, native semantic operation, blanket restart, retry, oldnonce reuse or production eligibility.

## Decisions

Main selects a source-only pretoken FactsEntry setup cohort as the next controlled
variable after the observer-only 9477 smoke. It uses the existing nonce-owned
shutdown root and unchanged launcher, actor, guard, claims and 360-second budget.
SDK owns the diagnostic hard request-admission fence, including unexpected tokens,
and successful installation proof; no owner discovery, getters or reader admission
is permitted. The shared directory means actor evidence creation can stimulate
the FactsEntry watcher and queue additional request callbacks. Results therefore
describe a coarse setup/timing cohort, not an isolated watcher or individual cause.

Preserve the legacy trace-stop-proof.awk byte contract. A separate canonical
trace-stop-pretoken-proof.awk is selected only by diagnostic_kind equal to
pretoken-facts-entry-v1. Explicit lifecycle-only-v1 selects the legacy parser;
historical selections missing this field retain legacy behavior only. Any present
unknown or malformed mode refuses packet preparation before output creation.
The preparation receipt identifies the effective mode and canonical parser source;
the selected parser is copied to the existing packet trace-stop-proof.awk name
and bound by its manifest hash. Missing mode never selects the pretoken parser.
Payload compile provenance and correspondence to the selected mode remain Main's
separate exact source/build review gates; preparation cannot inspect that property.

The pretoken parser retains v1, ten scalar fields, exact identity, sequence/time,
96-record, 192-byte-record and 18432-byte snapshot limits. It permits exactly one
entry-installed event after startup, with startup/GUI TID and quit_seen=0,
dropped=0, frames=0, followed by a qualifying before-render with frames>=1 and
quit_seen=0. A normal before-render recorded after quit begins cannot qualify,
even if a late-before-render follows; such otherwise valid incomplete proof returns 1.
Window may occur on either side of installation. Missing installation or no later
qualifying render returns no admission; duplicate or invalid installation refuses
the snapshot. Earlier before-render alone cannot admit STOP. Installation is proof
of installed runtime state only; the hard no-reader fence requires SDK source and
targeted fixtures. Neither event proves display drain or healthy Qt shutdown.
SDK must preserve ordinary observer signal/window connection ordering before the
entry helper and record the actual frame counter without resetting or fabricating
zero. If concurrent rendering advances it before installation, the parser refuses
that attempt and recovery follows; eligibility need not always succeed.
Any earlier normal before-render or after-render event makes a subsequent zero-frame
installation semantically inconsistent with the nonreset counter and invalid,
including when another qualifying render follows. Observer-only incomplete traces
without installation remain incomplete. The preparer and private host selection
must also refuse the spent and cleaned 94774266c10f41e2aa8d410012fee601 nonce.

Main's actual 94f attempt verified the full guard and recorded render lifecycle,
but observation timed out because tablet BusyBox od rejected -A. The subsequent
tr pipeline returned success with empty output, preventing parser admission.
Main's read-only diagnostic confirmed the actual snapshot passes native AWK.
Both final-LF checks will use a checked tail-c1 read to a private one-byte file
and numeric wc-l=1, avoiding od/tr flags and masked read failures. Failure-marker
length/nonce/ownership checks remain strict; the attempt remains spent and failed.

Actual a22 guard admission failed before STOP/payload and recovered original stock,
per Main's current report. A single policy.observed file allowed later stock proof
to overwrite the failed guard readback. Policy checks will retain separate exact
stock.policy.observed and guard.policy.observed snapshots before comparisons.

Primary systemd-stable v255.21 parser evidence shows OnFailure is a dependency:
config_parse_unit_deps returns on an empty value without removing prior dependencies.
Its unit documentation says removing dependencies requires a full unit override.
Thus the current empty OnFailure drop-in cannot establish the required guard. The
next guard design must use an exact-owned xochitl-only runtime full-unit shadow
and, if the dependency originates there, an exact same-basename vendor drop-in
shadow. Exact stock/vendor contents and hashes are prerequisites to deriving it.
Main supplied private original bytes and source derivation now verifies them;
the source design is implemented and 9477 proved native guard/admission/restoration
for one controlled harness smoke; broader coverage and Qt shutdown remain open;
it authorizes no shared remarkable-fail masking, watchdog change or unguarded STOP.

The preparer will require original unit/vendor file inputs whose exact bytes match
the pinned stock hashes. It will remove exactly one Unit OnFailure assignment to
remarkable-fail.service from each file, preserving every other byte, and retain
both originals and derived hashes in the packet. Runtime destinations are
/run/systemd/system/xochitl.service and the exact vendor basename under
/run/systemd/system/xochitl.service.d. Per-file exclusive install-intent claims
precede each owned creation. All initially absent paths, directory ownership and
derived file hashes are checked. Partial installation before STOP removes only
present, exact-hash owned files with matching intent; unknown/foreign content
refuses cleanup. Once guard.ready or stock-stop admission is persisted, missing
guard pieces refuse further cleanup/start. Activation removal precedes all guard
shadow removals, then one reload and original fragment/drop-in/policy proof.

Guard readback will include FragmentPath, DropInPaths and ExecStart in the same
bounded query as policy, avoiding extra query latency. It must prove the exact
runtime fragment and full runtime drop-in set, original execution before admission,
and exact launch execution after activation. Stock proof requires original vendor
fragment/drop-in provenance. Every original watchdog, timeout, kill, start-limit,
dependency and execution directive remains preserved except scoped OnFailure
removal and the existing explicit Restart=no/failure-action guard.

Primary sources:
- https://github.com/systemd/systemd-stable/blob/v255.21/src/core/load-fragment.c
- https://github.com/systemd/systemd-stable/blob/v255.21/man/systemd.unit.xml

1. Separate bounded source branch from clean Buddy0093baseline; central change precedes code. Never modify frozen Manager PRs or SDK-owned files.
2. Main selects fresh32hexnonce, exactpayloadhash and fresh baseline. Packet root `/run/rmb-qt-shutdown-<nonce>` is rootowned0700; owner0600 contains nonce without newline. Launcher writes exclusive0600 `attempt.identity` canonical `pid start\n` before exec. SDK trace is bounded fixed lifecycle scalar records with matched process identity; absence/drop/truncation/malformed trace is diagnostic uncertainty, not healthy completion.
3. Save the absolute deadline before arming; prearm one independently started transient actor service before ANY policy/activation change, with no failure dependency/actions/restart. It owns physical service mutations after preparation, holds an exclusive singleton lock and persists one-use claims before activation/stockstart. A host request authorizes one activation only after actorprearm and effectiveguard proof. Actor survives host disconnect and uses monotonic absolute deadline with reserved recovery time. No global watchdog/service setting changes.
4. Actor applies/validates its exact ownedguard before any stockstop; original stock/vendor hashes and policy are validated first. It stops stock once, installs ownedactivation override underguard, reloads, starts candidateonce, and waits for one verified `before-render` identity event or crash/observation cutoff. Either outcome enters the same restoration path; no automatic candidate retry.
5. Restoration requests candidateSTOP whileguard remains effective; preserves pre/post-stop result/signal/exit data; verifies attempted PID/start is gone (PIDreuse never permits a foreign signal) and entire original unit cgroup empty. Initial stockstop similarly checks originalstockPID/start. Preactivation hostloss/timeout uses the same actor to clear ownedpolicy safely; absence of attempt.identity is permitted only when activation was never admitted and originalstock state is verified. Only then removes exactownedactivation+guard, reloads, starts stockONCE if stock was stopped, and verifies original effectivepolicy/hash/services and no payloadmapped. Cleanup failure or budget exhaustion retains evidence/guard and reports failure, never stock success or implicit retrypermission.
6. Main selects fixed360s absolute recoverybudget savedBEFOREarm, covering guard/prearm, firststop, observation, candidateSTOP, cleanup/reload/start and final verification. Stock/candidateSTOP caps95s each against effective90s unitstop policy; observation atmost30s; stockstart/verification reserve at least90s; setup/query slack50s. Queries cap3s and prearm requests10s. Stage admission/reserved cutoff may shorten observation to preserve restoration within the same deadline, never extend it. InitialstockSTOPfailure aborts candidateactivation and preserves failure separately from subsequentstockhealth. Timeout is never success. Failure records are exclusive and survive final healthy stock status; a crash result is not overwritten by restoration.

## Verification

The source uses an owned systemctl child with PID/start-bound termination and a
three-second query bound; it does not assume GNU or BusyBox timeout. An unconfirmed
child blocks subsequent queries and restoration. Property reads return explicit
status before testing their output, including when called from shell conditionals.
Recovery runs in a separate shell retaining the singleton lock descriptor; duplicate
recovery claims refuse further mutations. Original unit/vendor/executable hashes
are pinned separately from the 24 protected baseline hashes.

Eighteen current local fixtures pass, including actual actor entry/recovery shells
on host-request expiry before and after guard installation, exclusive claim/lock
refusal, synthetic packet preparation and refusal when only xochitl is active.
Final readiness checks each service separately; multi-unit is-active exit status
cannot establish all three services are active. These fixtures do not prove native
candidate recovery after host loss or every prearm ordering boundary; independent
source review and Main's selected native verification remain open.

Critical review found that a primary failure marker could be claimed again during
candidate crash recording and abort recovery. The dedicated preserve_failure
helper is idempotent only for an existing private root-owned single-link 0600
diagnostic.failed file with exact nonce plus one LF (33 bytes). Invalid evidence
refuses; all physical actor/restore/start claims remain exclusive. A regression
exercises actual finish and its separate recovery shell with the existing marker,
candidate signal result, owned cleanup and stock start exactly once.

SDK trace wire confirmed with Astra: `v1 sequence event monotonic_ns tid pid start quit_seen dropped frames\n`, single ASCIIspaces, atmost96records/192bytes each/18432bytes total; eventenum startup/window/before-render/after-render/about-to-quit/window-destroyed/application-destroyed/late-before-render/late-after-render. Validate canonical decimalfields, complete lines, strict sequence/time and exactattemptPID/start. Droppednonzero refuses stopadmission evidence. Firstvalidbefore-render requiresframes>=1 and canauthorize only oneSTOP, never a displaycompletion fence. Missingterminalmarkers remain unknown even if currentstock recovery verifies.

Focused owned local fixtures exercise exact actor code with injected proc/service/file/clock boundaries: ordering guardbeforefirststop, STOPwhileguard, process+cgroupgonebeforecleanup, stockstartonce; crash evidence and healthy restoration distinct; hostloss actorcontinuation; deadline/reserve failure without retry or policyremoval; concurrent actors admitone. These prove choreography only. Validate shell/Python/PowerShell syntax as applicable, strictcentralOpenSpec/docs/diff, thenfreezeexactsource/artifact/packet forMain and independentreview. No device execution by this lane.
