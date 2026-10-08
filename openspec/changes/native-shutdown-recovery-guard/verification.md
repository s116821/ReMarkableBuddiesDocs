# Source-local verification receipt

Verified 2026-10-08. Experimental source only; no native selection or execution.
Main completed the earlier source review, including corrected individual service
health queries. Critical combined review subsequently identified repeated failure
marker claims aborting restoration; this receipt now covers the focused correction.
Main previously reported independent execution of the earlier eleven
fixtures in the pinned image: exit 0, all eleven passed in 3.371 seconds, with
no-new-privileges added to the constraints below. Its private receipt is
`main-shutdown-lifecycle-review-r1/actor-focused-verification.txt`; this lane has
the current coordination message, not an independently read copy of that receipt.
Combined independent source review and native acceptance remain separate gates.

Main subsequently reviewed the corrective source without another finding and
reported independent execution of all thirteen updated cases: exit 0, all passed
in 3.433 seconds. Private receipt
`main-shutdown-lifecycle-review-r1/actor-focused-verification-r2.txt`; provenance
here is its current coordination message, not this lane reading the receipt.

## Fixture execution

Existing image: `sha256:8d79948df2c7c568a043683f786e7ce4ad2e25e469673b72b8da8d2dbb2fa9ac`.
No installation, image modification, network, actual service manager, SSH,
recorder loading, tablet operation or hardware correctness assertion.
The fixture uses real owned temporary files/processes and shell code with injected
service/proc/clock boundaries. Preparation uses synthetic payload bytes only.

From the Buddy checkout, substitute its absolute path for `BUDDY_CHECKOUT`:

```powershell
docker run --rm --network none --cap-drop ALL --read-only --tmpfs /tmp:rw,exec,nosuid,nodev -v "BUDDY_CHECKOUT/tools/native_shutdown_probe:/probe:ro" sha256:8d79948df2c7c568a043683f786e7ce4ad2e25e469673b72b8da8d2dbb2fa9ac python3 -B /probe/test_actor.py -v
```

Temporary executable permission allows only the owned query stub. Eighteen unittest
methods passed (some contain multiple subcases):

1. `test_one_active_two_failed_cannot_verify_stock`
2. `test_main_host_loss_before_activation_restores_guard_independently`
3. `test_packet_preparation_is_bound_and_prepare_only`
4. `test_prearm_host_loss_expires_without_policy_mutation`
5. `test_claim_and_lock_are_singleton`
6. `test_gone_refuses_failed_job_active_job_and_live_pid_with_empty_cgroup`
7. `test_restore_order_crash_and_one_stock_start`
8. `test_deadline_refuses_cleanup_and_retain_guard`
9. `test_process_read_failure_is_not_gone`
10. `test_query_hang_is_bounded_to_owned_child`
11. `test_trace_identity_and_invalid_drop_refuse`
12. `test_primary_failure_then_candidate_crash_restores_once`
13. `test_failure_marker_foreign_malformed_or_link_refuses_preservation`
14. `test_failed_guard_policy_snapshot_survives_stock_recovery_policy`
15. `test_partial_shadow_installation_cleanup_and_foreign_refusal`
16. `test_guard_policy_requires_exact_fragment_dropins_and_owned_files`
17. `test_shadow_derivation_removes_only_exact_scoped_dependency`
18. `test_minimal_busybox_od_failure_and_portable_actual_admission_boundary`

The updated thirteen-case run passed in 3.448 seconds. Case 12 runs actual finish
and its separate recovery shell with inherited singleton lock, primary exit 93,
then a mocked candidate signal result: failure evidence preserved, cleanup and
stock start once, original primary failure retained. Case 13 rejects foreign
nonce, missing/doubled LF, NUL-ending and linked failure markers. These are injected
service/proc fixtures, not native crash or service-manager proof.

Selected-baseline preparation subsequently exposed a literal path-character
omission: `/usr/lib/libstdc++.so.6` was refused. The narrowly corrected preparer
allows literal `+` in its rooted allowlist; traversal, duplicate paths, inventory
size and hash checks remain unchanged. Existing case 3 now verifies this actual
provider path and rejects semicolon, command substitution, backticks, glob,
parent traversal, space and newline paths before output creation. All thirteen
methods passed again in 3.874 seconds; final shell/Python syntax passed. Main's
earlier independent run predates this path correction.

Actual selected Windows preparation then exposed default CRLF writes rejected
by the coordinator's canonical LF manifest check. Every generated text output now
uses explicit LF, including policy, baseline, service, guard, activation, manifest
and receipt. AWK source is read with universal newline normalization and emitted
as LF text; payload copying remains byte-preserving. Existing case 3 asserts no CR
in every generated text file, unchanged payload containing CRLF bytes, and identical
packet bytes under a controlled default-CRLF write simulation with CRLF source
templates. All thirteen methods passed in 3.874 seconds and final syntax passed.
The failed Windows packet is preserved; Main will prepare a new packet-r2 and
verify actual Windows bytes and the strict coordinator before staging. No relaxed
manifest comparison or native qualification follows from this correction.

Main's actual a22 attempt subsequently failed guard readback before STOP or payload
and verified original stock after cleanup, per current coordination messages.
Primary systemd-stable v255.21 documentation/parser confirm that empty dependency
assignments cannot remove loaded OnFailure dependencies. Both private originals
contain that directive. Current source requires hash-pinned original file inputs,
derives xochitl-only runtime full-unit and same-basename vendor shadows by removing
exactly one scoped line, and keeps every other byte. Private original inputs are
not tracked in this public repository. Direct local byte/hash derivation verified:

| Source | Original bytes | Derived bytes | Derived SHA-256 |
| --- | --- | --- | --- |
| stock unit | 414 | 380 | 3c368f1da2c61f13e1e795bd44b6e0b42c40a0df4492aea37684642a9da75264 |
| vendor drop-in | 71 | 37 | 904e2a69d3a8aa9be8c6f2d509ce697708da356b24cabe0cfefd596b2a749ba3 |

All seventeen current actor methods passed in 3.847 seconds, with final syntax.
Case 3 uses synthetic original inputs and injected source-hash validation, while
preserving LF/payload/path checks; it does not claim native input provenance.
New cases retain failed guard snapshots across later stock proof, exercise five
partial installation stages and foreign-content refusal, require exact runtime
fragment/drop-in/exec provenance and owned hashes, and preserve every directive
except the exact scoped dependency. Cleanup validates the entire owned set and
directory-created claim before removing any protection. Missing pieces after
guard-ready/STOP admission refuse cleanup/start. Existing crash/EXIT/host-loss
fixtures remain passing with full shadow pieces.

Separate private host coordinator r3 extends packet inventory/hash checks and the
existing bounded guard query with both shadow hashes and runtime provenance; it
reads per-policy snapshots and refuses spent a22/4459 nonces. Its nine source-local
methods passed in 0.449 seconds, with final syntax. r1/r2 are preserved. No actual
r3 transient unit, SSH, native guard readback or payload qualification is claimed.

Main's subsequent actual 94f attempt proved the full guard, admitted candidate
6758/start2850967 and recorded startup/window/render events, then timed out in
observation with primary exit 1. Recovery stopped the candidate successfully and
Main verified stock 7883/start2855788, same boot and original policy/hashes/services.
The attempt remains failed and spent. This lane read the saved postattempt and
read-only native parser diagnostic JSON: native BusyBox 1.36.1 od rejects -A,
masked by final tr success, while the same 2101-byte snapshot passes native AWK.
Local replay also passed unchanged parser with the same identity: 36 records,
SHA-256 9b8c02191380cf344659f3c31204a97d328e560830c583b04bf0643f11656527.

The narrow correction replaces both LF checks with checked tail-c1 to a private
final-byte file, checked wc-l read and numeric 1. The 33-byte/private/exact nonce
failure-marker checks remain. Case 18 reproduces unsupported od plus masked old
output, then proves portable LF/parser/one-STOP admission and marker preservation;
empty/CR/noLF and failed tail or wc emitting plausible output refuse. All eighteen
methods passed in 3.859 seconds with final syntax. Main's current narrow review
accepted this approach; independent selected-case rerun remains separately reported.
Private r4 preserves r3 and changes only spent-94f rejection and capped read-only
final-byte retrieval; its arming template/timing remain byte-identical. No native
payload replay or new nonce selection occurred in this lane.

Shell `sh -n` on both templates and Python AST parsing of both Python files passed
after the portable LF correction. Central `scripts/check_docs.py`,
`openspec validate native-shutdown-recovery-guard --strict` and diff checks passed.

## Actual portable-LF harness smoke, 9477

Main selected nonce `94774266c10f41e2aa8d410012fee601` and matching payload
SHA-256 `82ebbee5843077f042219123539767748e04b32573fc08e714a3560b4c4f6020`
(26032 bytes). Exact selected source bindings were SDK
`a31f495eb0e2ae8294e78609495c24063bc3f8fc`, Buddy
`cdf4f55a94f166c7cec26963f3914b9b65209566`, Docs
`caec4d7ebf13c3b0ba867957bf0ccd53b12c80e4`. This lane read the private final
selection, matching-build verification, postattempt verification and archive
receipt; Main alone operated the tablet. No public artifact link exists here yet.

The actual diagnostic recorded primary exit 0 and stop.admitted with the exact
nonce. Candidate PID9384/start2913441 had a three-record admission snapshot
(startup, window, first before-render); final trace had six records/two render
pairs. Candidate STOP recorded Result=success, ExecMainCode=2/ExecMainStatus=15,
MainPID0 and empty Job. No SIGSEGV was reproduced. The actor recorded restored
stock PID9992/start2915381. Main's independent postattempt receipt confirms same
boot, all24 protected and three source/executable hashes unchanged, original
policy, empty job/NRestarts0, all three services individually active, all unit
payload mappings absent, and owned runtime unit/drop-ins gone. The saved readback
supports those statuses; no fresh remote verification was performed by this lane.

This lane independently verified the local archive against its receipt:
115712 bytes, SHA-256
`7c12f0c5f53823e21e5a14b4dd2284195da46d48e7a788eb7dea39f30dd02a9c`,
60 recorded files, and exact hashes for outcome/admission/snapshot/final trace/
candidate STOP/stock restoration. Private evidence directory:
`main-shutdown-lifecycle-94774266c10f41e2aa8d410012fee601` under Main's existing
device-private workspace. Cleanup/archive lifecycle remains Main-owned.

This qualifies the actual portable admission and restoration harness path only.
STOP by SIGTERM does not prove Qt quit/destructor behavior, the original 0404
fault is not fixed by this result, and native FactsEntry/Reader contracts were
not exercised. A before-render record remains a STOP trigger, not a rendering
completion fence. Nonce9477 is spent; no blind repeat is authorized. Broader
candidate-hostloss/ordering coverage and linked delivery remain unfinished.

## Frozen executable source hashes

| File under Buddy tools/native_shutdown_probe | SHA-256 |
| --- | --- |
| actor.sh.in | a4cdb6a35d6e848852ed3c75cca05e8231f81ed904ef2fd2847668b7f1ad5a4b |
| launch.sh.in | 00747bd76a6a7d556e77cca41afb04e978256a23975770ed29e8af1a186ada95 |
| prepare_packet.py | 732dbdd453f4aadea6e5e1d71941ef655547a5cbd9d13154018eff4ecac257fd |
| test_actor.py | 7733ac3e592bd0928f9309ddaa57120ea630e8184f735f3430f7612eab46912a |
| trace-stop-proof.awk | e7ad5e8b213b07230181fd608cf4bd706c65f78c6a0b43cf55d773755bb868c6 |

Current Buddy commit `cdf4f55a94f166c7cec26963f3914b9b65209566` includes the
portable LF correction atop full-shadow, Windows LF, provider-path and marker fixes.
Launcher/parser/full-shadow protection remain unchanged by this narrow correction.
The linked Docs commit freezes this receipt and central proposal/design/tasks/delta.
No production eligibility, full native candidate host-loss recovery, complete
lifecycle trace, canonical spec synchronization or archive completion is implied.
## Pretoken cohort source-only extension

Main selected the existing single shutdown root and a separate strict parser for
diagnostic_kind=pretoken-facts-entry-v1. The legacy parser, actor and launcher are
unchanged. Preparation records the effective mode/canonical parser and manifests
the selected bytes under the existing runtime parser name. Missing mode retains
legacy selection; present unsupported/malformed modes refuse before output exists.

Nineteen local Linux fixture methods passed in 4.053 seconds in the already pinned
offline image. The new matrix checks installation/window order, missing and
duplicate installation, startup TID, quit/drop/frame fields, actual nonzero frame
counter refusal, identity/sequence/time/canonical scalar violations and record cap;
legacy parser still admits observer-only records and rejects the new event.
Packet fixtures verify explicit/missing legacy equivalence, manifest binding of
the pretoken parser, all other initial packet hashes unchanged, invalid-mode
refusal and identical LF output under simulated Windows CRLF defaults.

These are source-local injected fixtures, not SDK fence or native qualification.
Python AST, unchanged actor/launcher shell syntax, Docs check, strict OpenSpec and
both repository diff checks pass. Actor SHA a4cdb6a35d6e848852ed3c75cca05e8231f81ed904ef2fd2847668b7f1ad5a4b,
launcher SHA 00747bd76a6a7d556e77cca41afb04e978256a23975770ed29e8af1a186ada95
and legacy parser SHA e7ad5e8b213b07230181fd608cf4bd706c65f78c6a0b43cf55d773755bb868c6
remain unchanged. The new parser source SHA is
271f93e6d12a42d9996b2226cafe8f08d0f6056c781b76dbd593a6dcd3821f83.
SDK owns actual successful-installation emission, unchanged ordinary observer
connection ordering, actual frame counter and hard no-owner/getter/reader fence.
Concurrent render may make installation ineligible; shared-root actor evidence
may stimulate request callbacks. Paired SDK/Buddy critical review remains open
before any new native selection. No nonce, payload build, staging or device action
was performed by this lane. Source basis: current Main selection, repository
source and exact local fixture output; cohort causal interpretation is inference.
