# E1 consumer counterpart and read-only baseline

Status: production qualification remains planning only. The historical E1/E0T
mechanism discussion below is superseded for the next minimal development test
by the October 2 checkpoint here. No minimal callback tablet run has occurred yet.

The user/coordinator prioritized native experiments and preserved the unfinished
E0T framework for reassessment after integration needs are known, before a
production unattended-recovery claim. The generic eight-case suite and its
server/ledger/lease implementation are not prerequisites for every reversible
development experiment; this does not complete or discard those sources.

One independently reviewed read-only R2-4096 run found a sampled existing
DocumentController chain (types3096/matches1/requested74426bytes, non-atomic).
Exact helper termination/removal and original process/three-service continuity
were verified. [SDK evidence4f57fb4](https://github.com/s116821/ReMarkableOpenSDK/commit/4f57fb4953107790b51f95d9b823e8283a4dfcb1)
owns the detailed finding. It proves neither lifetime nor current-page binding
nor permission to call page operations. Raw target addresses stay private.

The next scoped experiment uses [SDK public Qt startup source2265](https://github.com/s116821/ReMarkableOpenSDK/commit/2265ebb2f993e8806a77d94a352a7fd0de2c3e42)
for nonce/application-thread proof only. No XOVI, controller lookup, getter or
page mutation is present. Source/matching ARM payload and host fixture have
independent bounded acceptance; tablet delivery is unverified. Main remains sole
tablet operator, announces UI restart, and runs once only after exact ordinary
operator review. [Buddy operatorb100493](https://github.com/s116821/ReMarkableBuddies/commit/b10049308856fa030907fbfed339f8979208bfe1)
is under review after fixing a reproduced late-entry/rollback timing hole:
runtime-only stock-name drop-in, consumed one-attempt preload, original restart
policy retained, shared admission closure and prearmed existing-systemd timer
to one singleton restoration service. Forty-five seconds requests rollback; it
does not guarantee completion within that time. Require fresh stock verification
and exact owned cleanup, retaining evidence/staging on uncertainty. No boot,
firmware, account, broad service or native-page change is part of this test.

Source basis: current project direction, exact repository revisions, ordinary
independent review and actual private R2 receipts. This is development research;
no production lifecycle, source continuity, page creation or MVP gate is complete.

Historical E1 discussion: SDK owns the mechanism comparison and adapter contract at
[390fe8b5fa0caed4597ffa2f4f093bbe56533f83](https://github.com/s116821/ReMarkableOpenSDK/tree/390fe8b5fa0caed4597ffa2f4f093bbe56533f83/openspec/changes/establish-native-platform-contract).
Buddy owns retained intent, Supervisor lifecycle and its same-artifact Manager
installation. Host lifecycle corrections remain under independent review; no host
result substitutes for target service-manager or source continuity evidence.

## Actual authorized read-only inventory

After advance notice, three bounded configuration-only SSH reads on RM2 firmware
3.28.0.172 observed systemd255.21. Vendor xochitl unit SHA
adb0a2654ce9ec884f67c0627c22d539d6475dd0af80816819ee80bf13c0e6d6, sole
vendor drop-in SHAb15560e1dca2f4451b59537c490015aa2f5ea691437bd7ddddc7a65411aaad6e.
Effective policy: Type=simple, Restart=on-failure/100ms, RestartMode=direct,
start limit4/600s, Watchdog60s, NotifyAccess=all, start/stop/abort90s. Unit job
bounds are infinite; no xochitl job was outstanding. Two unrelated preexisting jobs
were observed and preserved; do not globally cancel jobs as recovery.

Manager RuntimeWatchdog60s and RebootWatchdog120s are separate scopes from the
service watchdog, not a single interchangeable countdown. Character watchdog devices
exist; no watchdog device was opened. The vendor failure handler SHA
59d92c2fbb03a47325b0bc6d34606fd2297284c97bc2cff502c5d78b2f381968 can reboot
immediately and has conditional filesystem/boot-environment recovery branches. Only
its script text was read; no handler, boot-environment access or recovery action ran.
Restart=no alone can expose that handler. An empty OnFailure dependency in a drop-in
cannot be assumed to clear the vendor dependency; SDK source investigation rejects
that recipe. No runtime safety override is selected.

/run is tmpfs, root-owned mode755, with204804KiB available at this snapshot.
/run/systemd/system exists; runtime and /etc xochitl drop-in directories were absent.
No LD_PRELOAD entry was observed in the current xochitl environment. Existing xochitl
PID30974/start100545844/stateS and both services remained unchanged/active. These are
SSH/process/service facts, not physical UI responsiveness or injection timing proof.
Private receipts remain outside Git. Baseline receipt SHA
636ca12ed10cfb6057ed2685ae2d2a676709daca937de67f6dec8a22bad56009,
recovery receipt SHA52a076104ddb7bc1c74f7f474a9a5a9721f127351fdb0538484946b5ae5d9f0e,
job receipt SHA0c83dfa107f00d878a2cc73fe4e4bd36fb76c5db13920f3b2fc932ec89b91752.
Initial inventory stopped after a no-matching-watchdog-unit exit and was preserved;
that absence never established no watchdog. Later reads completed successfully.

## Remaining pre-entry gates

- Demonstrate actual surviving-Supervisor recovery at every activation handoff,
  transaction-owned idempotent restoration, late-writer rejection and honest failure
  under blocked restoration in the host harness, with independent exact review.
- Compare a separately owned transient injected service against any stock-unit
  runtime change. Unchanged vendor-unit normal stop/start is a comparator, not an
  approved recipe: investigate exact notify/DBus/environment/singleton/dependency
  and stock stop-side effects. Host-only matching255.21 fake-unit fixtures may test
  parser/job/failure relationships without xochitl or device changes.
- Freeze loader/typed no-override callback and complete artifact/dependency/source/
  compiler/license manifests, then a concrete finite independently reviewed operator
  packet with actual device-derived timing, separate recovery and outstanding-job
  fencing. Infinite default jobs and immediate failure-handler behavior remain entry
  blockers until a justified bounded alternative is established.
- Preserve Manager one-install ownership and stock cold boot; no broad UI replacement,
  persistent startup injection, source guessing or automatic native operation replay.
  Retain only intent/historical evidence across activation and reacquire fresh source,
  cancellation and action applicability before a later semantic stage.

E1 would be one load/GUI challenge/stock restoration observation only after separate
coordinator authorization. It contains no page calls, getters, document/account reads,
input, deliberate faults or cold reboot. A finite unattended UI observation can be
reviewed or physical UI responsiveness explicitly left unverified; no human response
is prerequisite. E2 native/source qualification remains separate. All broad tasks
are open and no canonical sync/archive follows.

Source basis: actual current private read-only receipts, coordinated SDK source
investigation and current project direction. Candidate mechanisms and gates are
engineering proposals; no activation or production qualification is claimed.

## Exact upstream parser and actual coupling findings (October 2)

Original Buddy tooling at22ff4e8fc782624dab4ea2e41c446183f43dd07f builds
upstream systemd-stable255.21 commit70500d37992a01d3275b1c414c3ed161d6f91f9e.
Independent Sol accepteda93fbe5193e84269388d94ac8c982f49befb5774 and reran all
four offline assertions; it accepted the single-line default-parser follow-up22ff4e8.
Empty OnFailure retains vendor and added handlers; a full runtime fragment retains
vendor unit-specific drop-ins; separate names have no handler absent configuration;
generic service.d handlers affect separate names. No unit/job executes in test mode.
The rebuilt default-parser image7176a0bc5ab9432d73ed2e447f18c27e5b3a2f00e957c43faaddddfede47e209
passed all four; ELF SHAf132ac4469673ce3aead14c70b286ebfab2d0e22f572d25d95040b7b7f54f4be,
GCC13.3.0. Ubuntu base/packages are unpinned and vendor patch equivalence is unknown.
Host system/user-manager attempts failed to allocate a manager under the isolated
read-only cgroup v1 hierarchy. Owned containers were removed; host cgroups unchanged.
Parser proof does not qualify live jobs, stop timing, notify or failure recovery.

Further read-only actual tablet inventory, receipt
SHA8f39ed85979abc4db2ea7eb465ee5f1ddbddee1872b82ebef378fa743c0497ac,
found rm-sync BindsTo and PartOf stock xochitl, with After ordering. Xochitl Wants
rm-sync and Reader Buddy Wants xochitl. A separately named service cannot assume
sync persists, and starting unchanged sync can reactivate stock. Generic service.d
directories were absent under /usr/lib,/etc,/run at that snapshot; dash-prefix lookup
and later drift still need gating. Original PID/start/state and both services stayed
unchanged. No introspection, account/document read, service change or activation ran.

The [SDK E0T proposal at a2f68c9](https://github.com/s116821/ReMarkableOpenSDK/blob/a2f68c91e48c3eebf763cc15bfc214b44907fb49/openspec/changes/establish-native-platform-contract/e0t-dummy-unit-plan.md)
proposes finite actual-manager tests using only unique owned dummy units. Preparation
is authorized; staging/starting requires review and approval of exact helper, units,
operator, manifest, limits, effective-property gates and independent cleanup. No real
vendor dependency/handler, global setting, XOVI/native payload or boot change belongs
in that packet. It tests dummy-manager behavior only and does not authorize E1.

Source basis: exact original source/report, independent Sol review, actual private
read-only service receipt and coordinated SDK proposal. The E0T cases are proposed.
