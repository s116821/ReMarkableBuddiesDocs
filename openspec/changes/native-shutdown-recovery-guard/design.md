## Context

Main's fresh RM2 observation: firmware3.28.0.172, stock PID291/start561, protected14document+10baseline hashes unchanged. Stock effective OnFailure=remarkable-fail.service, OnFailureJobMode=replace, FailureAction/StartLimitAction=none, Restart=on-failure, RestartMode=direct, TimeoutStopSec90s, WatchdogSec60s, KillMode=control-group, SIGTERM then SIGKILL. These values require fresh exact validation at selected execution; source notes are not a current baseline. Original native crash outcome remains separately preserved.

## Goals / Non-Goals

One fresh lifecycle-only diagnostic can recover under an independent actor even after host loss. Before first stockstop prove an owned runtime guard setting Unit OnFailure empty, FailureAction/StartLimitAction none and Service Restartno. Retain guard while stopping candidate and proving exact process/cgroup absence. No facts entry, pagegetter, input, forcedrender, native semantic operation, blanket restart, retry, oldnonce reuse or production eligibility.

## Decisions

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

Thirteen current local fixtures pass, including actual actor entry/recovery shells
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
