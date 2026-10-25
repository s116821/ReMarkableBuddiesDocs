# Isolated systemd recovery result — October 25

The actual development tablet passed five disposable fake-unit cases under
[resident-supervisor-integration.md](resident-supervisor-integration.md). This
is platform lifecycle evidence, not stock takeover or native product acceptance.
Buddy `6514b4ce31ad005dee9ff5049be6982864055c7e` contains the reviewed script
`tools/systemd_fixture/recovery_lifecycle.sh`, SHA256
`6be67aa2672c0760aba0d8dc4a7f0e774473c6b070a5fc65ec711acc73b055df`.
All source bytes were frozen and retained before each invocation. Shell syntax
and all three generated unit templates passed the upstream systemd 255.21
offline verifier before device execution.

Actual platform: firmware 3.28.0.172, kernel 5.4.70-v1.6.3-rm11x, systemd 255.21,
hybrid cgroup layout. Executed at 21:56–21:58 UTC, with a fresh nonce per case:

| Case | Nonce | Actor result | Distinct recovery invocations |
| --- | --- | --- | --- |
| Clean exit | `00f6caeeaef64b1eac510081b9d1d388` | success | 2 |
| SIGKILL | `4c9b235c440b44f98a74bf962e50d297` | signal | 2 |
| Watchdog expiry | `c27945465ed941d59bd1f69b279765f1` | watchdog | 2 |
| Explicit stop | `353b08ecccf24e5f97d0d79d15f09cf3` | success | 2 |
| Helper failure then retry | `26b785910137415d808cd13f105df2ba` | success | 3 |

Each fake stock started exactly twice: initial and restoration. A distinct
subsequent helper invocation left it running without another start. In the retry
case, the first helper deliberately failed after recording restoration intent;
the second completed restoration, and the third demonstrated idempotence. The
actor's owned child no longer existed when recovery began. PID1 reported the
expected actor result and completed the ordered recovery without an ExecStopPost
cycle. No host timeout or test failure occurred.

Every helper invocation found the original actor cgroup absent. Its identity
and populated state had been captured while the actor was live. This confirms
the reviewed after-exit identity-handoff problem; it does not solve it. Missing
paths were explicitly labeled observations in this fake-only fixture. Production
recovery must implement a qualified emptiness/deletion predicate before use.

All runs reported successful cleanup after verifying owned unit inactivity,
no MainPID or pending job, and empty existing groups. Runtime unit definitions
were removed and PID1 reloaded. The before/after real-service snapshots are
byte-identical: stock PID10366/invocation `0ba7fd058b8e4c399cca8f5e24a3bbf9`,
Buddy PID11238/invocation `991fb85bd8c54b8f9b523979f3922183`, both active/running
with no job. The stock executable/unit/drop-in SHA256 values remain those in the
design's live inventory. No real-service restart, input, UI/document mutation,
native loading, firmware change or account operation was performed.

Local preserved evidence is `work/rem25-resident-local/recovery-fixture-NONCE/`:
exact source, UTC/SSH/return-code receipt, stdout/stderr and remote archive. The
five archive SHA256 values, in table order, are:

- `f1424ae21147309e8240aeb66fdad104a43402c08b12b956b9b4158ea10ed9d0`
- `99fd6805ddf1d3175ad78c8bbebfe37bc376c134b70f57693837c1b3d6ca73f4`
- `ff74bc84c5ac7a6eef78dfc9f17fea97a79eff2ffdb0c8c773e3e059d51aaf82`
- `3070d092602a3c071726612e0844803e38b162d4d8908a6f8aefc904e3c3697d`
- `a470563e02ea633cf5668aa0615126018eed440edb951c113c496209b5c29bbe`

The archives were independently read after collection and checked for matching
real snapshots, expected actor results, exact stock/recovery counts and successful
cleanup. Logs also show PID1 declining trigger-exit-status propagation when the
same actor is configured in both OnSuccess and OnFailure; the helper does not
depend on those optional environment values.

After archive verification, a separate bounded cleanup checked all fifteen owned
units were not loaded and their definitions absent, removed only the exact
archived regular files, then removed the five empty run directories. It succeeded;
the original local archives remain preserved.

Remaining: implement the service lease and actual recovery predicate, verify
shutdown-job cancellation, integrate main-loop watchdog/Manager lifecycle and
Reader reacquisition, then qualify native bootstrap and full document workflows.
The fixture's marker files are not the production durable lease or native effect
journal. No capability promotion, merge or archive is justified by this result.

## Service-incarnation retention on a later retry

A separate fresh clean case at 22:21:51 UTC answered whether PID1 retains the
original actor incarnation across distinct recovery calls. The only script change
adds read-only samples of InvocationID, ExecMainPID and
ExecMainStartTimestampMonotonic before fake-stock stop and in each helper call.
Exact script SHA256:
`b2d256b0844e09da1f0ecc850f1f4d8f78231d998d0043199bdae31c61cbd3d5`.
Nonce: `b30eb9f512ad483f8404bf2cdacef94e`. Archive SHA256:
`d900597b170fe7920f5af8a08d201b170b64f3fabf11e4b622d2ef3f6c21d6cd`.

| Sample | InvocationID | ExecMainPID | ExecMainStartTimestampMonotonic |
| --- | --- | --- | --- |
| Before fake-stock stop | `fe85417f07d445a8ad7986c92e7ee0b4` | 31750 | 1493716388120 |
| First recovery | `fe85417f07d445a8ad7986c92e7ee0b4` | 31750 | 1493716388120 |
| Second recovery | explicitly empty | 0 | 0 |

The actor was inactive/dead with successful result. Fake stock started exactly
twice and there were two distinct recovery invocations. Execution, archival and
the separately verified exact-file cleanup all returned zero. Actual stock/Buddy
before/after snapshots remained identical. Original archives remain local under
the nonce-specific evidence directory; earlier five-case evidence is unchanged.

This finding requires the explicit cleared-metadata branch in the integration
design. Cleared metadata alone is not proof of no native process: the original
lease, qualified deleted group, approved loaded terminal unit, bracketed state and
common activation latch remain required. The new branch and the regression for
failure before any terminal proof marker still require implementation. This run
did not exercise actual production recovery or native activation.

## Populated-group deletion refusal

One fresh `populated-delete` case ran at 22:47:16 UTC with nonce
`2af5cf4268e642ad83cf9a9324f73893`. Frozen script SHA256:
`83277f48f88baeb5c57a9f4bc8f967f7f1d0e5465dba89a1f4431517e87bfd75`.
Archive SHA256:
`3972c12ae3a0461ba2afe60e3955468e32e82e5064112b40133e12e231767f82`.

The actual actor shell and sleeping child both belonged to the exact owned actor
group in the unified and named-systemd hierarchies. A single nonrecursive `rmdir`
against that exact unified group returned 1 with the C-locale diagnostic
`Device or resource busy`. Group identity was `21:80421` both before and after;
`cgroup.events` still reported `populated 1` afterward. The actor then exited
successfully. Both subsequent recovery calls observed the group absent after
PID1 shutdown. Fake stock started exactly twice, with two recovery invocations.

Execution and archival returned zero; before/after real-service snapshots were
byte-identical. The verified archive contains 31 regular files. After verification,
a separate bounded cleanup checked owned unit definitions absent and units not
loaded, removed only those exact archived files and the empty owned directory,
and returned zero. Local source, receipts, archive, verification summary and
cleanup output remain preserved in the nonce-specific evidence directory.

This demonstrates refusal to remove this directly populated group and subsequent
PID1 removal on the observed vendor kernel. The actor itself was a member, so it
does not independently establish child-only nested-group behavior, resistance to
privileged migration or production native recovery. The helper still needs its
installed policy/latch checks and actual stock restoration integration; no native
capability is promoted by this fixture.

Source basis: frozen fixture source, direct target PID1/process/filesystem output,
retained archives, independent source review and upstream unit verification.
