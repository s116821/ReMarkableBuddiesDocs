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

## Actor budget and fences to implement

Experiment cleanup is separate from the case controller/guard that T6/T7 terminate.
Normal case operation reserves two slots for the external operator and its one
command, two for experiment cleanup and its one bounded command, and four for
case actors. T6/T7 case actors use controller+guard+stock and at most one command
child shared by serialized ownership: total eight processes and sixteen tasks.
Before ownership transfer, confirm the prior actor's complete owned cgroup/command
child gone; a PID-only exit or lost reply cannot authorize a second writer/fork.
Handler cases run without controller/guard/stock: operator2+cleanup2+norestart1+
handlers2=7. Notify/claim/separate/barrier/queued cases use only their enumerated
workers, remaining under eight. These are design allocations, not measured proof;
freeze needs an exact table for every barrier/failure/cleanup overlap. If native
command containment cannot meet it, revise before execution, never expand live.

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
