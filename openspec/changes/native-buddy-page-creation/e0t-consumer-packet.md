# E0T consumer packet preparation

Status: preparation only. No runnable or approved device packet yet. The exact
SDK proposal02398cf318f10676c7526c1c9009769fc430268f owns the dummy-manager
contract; Buddy supplies original helper, manifest, unit and operator tooling in
this unfinished REM25 delivery. Parent approved preparation of the eight finite
cases. Every source/artifact/unit/operator hash and property/cleanup expectation
requires independent review and final coordinator packet approval before staging.

## Fixed role and path budget

Exactly twelve named roles: cleanup, controller, guard, stock, fail-a, fail-b,
claim, norestart, separate, notify, barrier, queued. Names are compiled/frozen as
buddy-e0t-<128-bit-nonce>-<role>.service; there is no arbitrary unit argument.
T1 and T2 reuse the unchanged norestart unit with two owned marker handlers. T2
expects both markers. Each case has a distinct generation and disjoint bounded
records; terminal jobs/processes/handlers are verified before reuse, and rate
limits across starts are accounted for. No per-case daemon reload.

The manifest must list twelve exact runtime fragment paths, the T1 norestart
unit-specific drop-in parent and file, the owned root, and every helper/control/
record/claim artifact. Initial absence, no symlink traversal, exact inode/token
ownership and file/hash identity gate use/removal. Only an owned empty parent can
be removed; never recursively delete systemd directories. No dynamic paths or
vendor dependency/action targets belong in the implementation.

## Current authoritative preparation resource table

This table supersedes the earlier separate operator2/cleanup2 reservations and
case command-child allocation. SDKc0753644631652c49462c6ce0e6cdf097d2bcc49 flagged
those conflicting historical figures. There is ONE shared CLI slot across the
external operator and independent cleanup actor; case actors never spawn CLI
children. The table is preparation design, not a frozen or measured packet.

| Barrier/case overlap | Helper processes including always-present cleanup + operator | Helper maximum | Shared CLI maximum | Program process maximum |
| --- | --- | --- | --- | --- |
| T1/T2 marker overlap | cleanup, operator, norestart, fail-a, fail-b | 5 | 1 | 6 |
| T2 claim stand-in / T3 / T4 | cleanup, operator, one claim/separate/notify worker | 3 | 1 | 4 |
| T5 including unexpected queued start | cleanup, operator, barrier, queued | 4 | 1 | 5 |
| T6/T7/T8 including fixed stock child | cleanup, operator, controller, guard, one stock child | 5 | 1 | 6 |
| Abort/cleanup while case workers exit | cleanup, operator, remaining case workers, bounded by the case row | 5 | 1 | 6 |

Reserve at most TWO additional process slots for transport/wrapper overhead:
program6 + transport2 must fit the overall8-process bound. Exact SSH session,
wrapper and any CLI descendant/thread creation must be enumerated and measured
before freeze. A command shell must exec the fixed operator rather than persist
as an uncounted wrapper. These reservations are not proof of SSH process counts,
source containment, or task enforcement. Overall16tasks remains a measured/source
obligation; do not infer a two-task-per-helper kernel limit or CLI one-thread
maximum from a prior sample. More overlap/threads/descendants requires redesign
before execution, never live cap expansion. Do not modify the SSH service.

| Process row | Candidate AS soft/hard | Other candidate per-process limits | Status |
| --- | --- | --- | --- |
| Ordinary worker/case actor/stock child | 8MiB / 8MiB | stack512KiB, data1MiB, file2048bytes, core0, CPU2s | Host source/set-get evidence; target artifact headroom open |
| Operator or cleanup manager parent | 8MiB / 20MiB | same | Parent retains soft8; hard20 is not an enforced8 ceiling |
| Sole fixed CLI child | 20MiB / 20MiB | same | Child raises only its own soft limit; target command peaks/headroom open |
| SSH/transport/wrapper overhead | Unfrozen | Unfrozen | Enumerate/profile actual overhead; not inside the helper rlimit proof |

At most five helper soft-AS8MiB rows plus one CLI20MiB row yield60MiB of
program-specific summed AS candidates. This excludes unresolved transport rows
and is neither aggregate kernel enforcement nor RSS/whole-tablet memory proof.
Each command/helper artifact and all fork-before-exec overlaps need mapping,
limit-readback and headroom evidence. Cleanup duration/CPU budget is still open;
no lease extension or runtime resource growth is authorized.

Before ownership transfer, confirm the prior writer/command identity actually
gone, its complete owned cgroup empty and pending manager requests/jobs reconciled.
EOF, lock release, PID-only exit or missing reply cannot authorize another command
or stock-child fork. Unknown state refuses further case starts and retains failed/
unknown cleanup. No duplicate restore child compensates for unknown publication.

## Gates and resource limits

Before any dummy start, including cleanup, verify every effective unit command,
fragment/drop-in/environment/dependency/action/limit against the frozen allowlist.
Inspect generic and dash-prefix drop-in paths. Snapshot originals and outstanding
jobs before explicit manager-wide daemon-reload, reject unknown configuration drift,
then verify originals after reload and between cases. No enable/boot target/global
setting, reboot handler, real service mutation, XOVI/preload, native/document/account
operation or input belongs here. Stage at most16MiB; evidence at most256KiB; helpers
at most8MiB/two tasks each. Case15s, first start to cleanup initiation180s plus30s
cleanup, independent finite lease and worker self-exit caps. Stop first unexpected
result; no retry/lease extension. A timed-out operation is failed/unknown.

Use nonce/generation/process-bound events and observed manager job terminals; never
sleep-as-success. A lost start reply reconciles the owned unit/job rather than sends
another start. Only exact correlated owned jobs may be cancelled; preserve unrelated
jobs. Restoration requires all late writers/start jobs fenced, exact owned-state
postconditions, and live stock stand-in. Cached receipt is historical and must be
revalidated. Runner cleanup is separate and cannot turn failed recovery into pass.

The finite eight cases remain those in the pinned SDK proposal. Task execution,
helper/manifest/operator implementation, artifact review and real-manager evidence
are still open. E0T would establish dummy behavior only, not xochitl timing, sync
lifetime, loader/GUI/source semantics, actual stock recovery, cold boot or E1.

Source basis: current coordinated preparation authorization and pinned SDK proposal;
role allocation/concurrency fences are proposed implementation design.

## T6-T8 concrete actor refinement

SDKbb39af192db7ea3893e77c9e2742480907bd1475 accepts a fixed-self stock-child
implementation for these cases. Controller/guard may manipulate only owned dummy
files and spawn the same fixed helper as their stock stand-in; no manager transport
command belongs in a case actor. External operator and experiment cleanup are the
only manager writers. Prior actor start jobs must be terminal and further actor
starts forbidden during handoff. Confirm old OS identity gone, entire old cgroup
empty and any old child gone before surviving actor forks. Job/cgroup observations
must fit the existing process cap. EOF/lock release/parent-death signal alone is
insufficient. A spent restore claim without a published child identity is unknown;
never create a second child to compensate. Restoration and closed-generation fences
must serialize late file publication; repeated queries revalidate child liveness.
T6/T7 prove owned-process/file recovery inside manager-launched units; T5 separately
proves the bounded pending-manager-job case. No combined E1 job-recovery claim follows.

## Read-only resource profile: execution blocker

Actual tablet receipt057181a226c15041e284f65f8dfc250d96b02ee0df307e586e5e0519d77e5af9
shows the hybrid name=systemd hierarchy at /sys/fs/cgroup/systemd/system.slice,
with original xochitl cgroup containing multiple process IDs. MainPID death alone
cannot prove an empty unit. No cgroup was modified.

Further receipt7fcc0b0d2e58e0f9d7705b0fbf416d9af6f7220b9a038ec46f56512c13420768
shows /proc/cgroups with only its header, an empty unified cgroup.controllers and
subtree_control, and absent legacy memory/pids controller roots. The proposed
MemoryMax/TasksMax cannot be claimed enforced merely because effective unit
properties display them. The current contract requires refusal when required
resource limits cannot be enforced; this is a pre-execution blocker. No controller
mount/enable/configuration change or silent fallback is authorized. Astra/coordinator
must review any resource-contract revision before a runnable packet can freeze.
Both read-only commands preserved original xochitl/rm-sync PID/start/state and all
three observed active services. Physical UI responsiveness was not tested.

## Revised dummy-only resource design for preparation

The SDKbc5e87a9762ef192b8332d651d60a17fc226efda revision supersedes the mandatory
cgroup recipe for design, while retaining refusal before execution until the exact
replacement controls are demonstrated. No controller/kernel/global change follows.
Kernel per-process address-space, stack, data, file, core and CPU limits must have
frozen numbers, exact initial mapping/headroom evidence and successful set/get reports.
They do not establish RSS or an aggregate descendant-memory guarantee. Concurrency
remains source-bounded and observed (12roles/8processes/16tasks), not kernel pids-capped;
root RLIMIT_NPROC cannot prove it. All creation sites, children, threads, failure and
cleanup overlaps need an exact table and actual slot termination before reuse.

An initial helper sizing proposal is AS8MiB, stack512KiB, data1MiB, file2048bytes,
core0 and CPU2s. These values are preparatory candidates, not frozen device limits.
The helper profile must report its initial mapped bytes and getrlimit results before
case effects. Reject insufficient loader/stack/heap headroom and failed limit checks.
A separate manager-command artifact needs its own measured mapping/headroom/limit
row; do not assume the helper's limits fit systemctl or treat inherited settings as
post-exec verification. Reduce concurrency before enlarging workload. Fixed buffers,
checked allocation/output, aggregate evidence accounting and independently reserved
cleanup budget supplement kernel per-process controls. Finite owned refusal fixtures
must remain small; no fork/memory stress or unreviewed ninth device case is added.

The exact numeric table, source/artifact proofs, complete operator and independent
packet review remain missing. Preparation is authorized; no stage/start is authorized.

## Reviewed read-only command preparation

Buddy553d9cfdfb3a9591289160d7e0d341ce0253fd36 and follow-up
fca1b670a0d3b950310db64b49f9825b906b7aab have bounded independent host acceptance
for one shared fixed read-only CLI slot. Parent AS remains8MiB soft/20MiB hard;
only its one child raises its own soft limit to20MiB. A retained intent/child
publication refuses reuse after parent death or lock release. Actual child wait
and output EOF must both occur within2s; capture is4096bytes. This does not prove
arbitrary executable descendants or writable manager-job reconciliation.

SDK43b0e220389c62caef23c64c513545b4dc11e7cc fixes list-jobs query arguments:
--no-legend --plain --full --no-pager --no-ask-password plus twelve exact nonce
unit names, localeC/no colors. The independent pure decoder298d78a and integrated
fca1b67 reject incomplete/foreign/duplicate/malformed rows before publication.
An empty observation or disappearing job is not terminal/canceled proof or start
attribution. T5 still needs fresh manager-instance/case/job tuple correlation,
exact numeric cancel, observed unit/process/cgroup/marker outcomes and a no-late
start check after barrier release. Bare/global cancel is never representable.

Barrierf10642d independently verifies one explicit R control message sendsREADY;
startup is silent and repeated R refuses. This is worker readiness protocol only,
not a manager queue/cancellation result. The local manifest is still non-runnable,
166explicit owned paths, with unresolved cleanup/operator/resource/job gates.

Actual inherited-child target limit receipt
041bd7b1af19e36d0b7172b31d4f47257243a283eda301bdbcf550980d75f135 verifies kernel
AS20MiB/stack512KiB/data1MiB/file2048/core0/CPU2 settings. It profiles a cat child,
not systemctl headroom. Fixed capped-query receipt
f8b9c79553da8e3a1fb1adfe9d6b7cedd4b1f580f5414805f297f45c9abfa788 stopped BEFORE
systemctl because the tablet lacks timeout. No unbounded substitute or extra
helper transfer follows. SDK a4868b75ba157d0815c83d887b1f07ec09a11881 independently
read/hash-checked those receipts. A separate main-operator follow-up receipt
903835f17cd9c121c93c90dc66d8594c283b07ca1732394054ffaa4df73a9754 confirmed original
xochitl identity/state and all three services active with empty jobs. No physical
UI, writable service command, unit staging or helper load was tested.

ARM fca1b67 preparation build imports libc only/maxGLIBC2.38, synthetic nonce,
SHA1c22e4dc870ed487197e6e62231d59fc158b22e5cfadbf830920c0e3b52f2db6. Build-only
is not a frozen packet or runtime qualification. Exact cleanup/operator, command
artifact peaks/headroom/termination, concurrency/evidence accounting and final
independent packet review remain open. No E0T staging/start or E1 is authorized.

Source basis: exact public source/review checkpoints and operator-attributed
private read-only receipts; raw configuration remains private. These bounded
preparation results do not close native creation or the broad OpenSpec tasks.
