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

## Frozen portable-LF executable source hashes, selected for 9477

| File under Buddy tools/native_shutdown_probe | SHA-256 |
| --- | --- |
| actor.sh.in | a4cdb6a35d6e848852ed3c75cca05e8231f81ed904ef2fd2847668b7f1ad5a4b |
| launch.sh.in | 00747bd76a6a7d556e77cca41afb04e978256a23975770ed29e8af1a186ada95 |
| prepare_packet.py | 732dbdd453f4aadea6e5e1d71941ef655547a5cbd9d13154018eff4ecac257fd |
| test_actor.py | 7733ac3e592bd0928f9309ddaa57120ea630e8184f735f3430f7612eab46912a |
| trace-stop-proof.awk | e7ad5e8b213b07230181fd608cf4bd706c65f78c6a0b43cf55d773755bb868c6 |

Selected 9477 Buddy commit `cdf4f55a94f166c7cec26963f3914b9b65209566` includes the
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
b06803122b6059adca5f7cf1f257d6483c9f2f2bdf6e52049c4b9e1eac08b759.

Root's paired review reproduced a post-quit ordinary before-render incorrectly
admitting STOP. The narrow repair requires quit_seen=0 on the qualifying render.
Its exact startup/install/about-to-quit/ordinary-before/late-before sequence now
returns incomplete exit 1; the normal pre-quit control still returns 0. The changed
parser fixture method passes in 0.079 seconds. No broader matrix, SDK rebuild,
legacy parser or actor/recovery change was made. Root review closure was pending
at this source checkpoint; Main's subsequent final 2b34 selection records closure.

Main critical review added prior-render consistency: any normal before/after-render
before a zero-frame installation invalidates the snapshot, even with a later
qualifying render. Missing installation alone remains incomplete. Both changed
Buddy fixture methods passed in 0.179 seconds, including spent-9477 preparer
refusal before output creation. Python AST passes. Earlier 95fdcce source remains
preserved in Git; this correction supersedes its marker-order interpretation.

Private host R5 copies preserved R4 and adds only spent-9477 rejection plus its
fixture/documentation; arming remains byte-identical SHA 904919e226490a1edb043d48bf286f16373a3c808cf001208d6d7bdaa9962a4c.
Its changed packet/pin method passed in 0.023 seconds, with Python AST and generated
shell syntax passing. Coordinator SHA ed445c8b00a7e51f58cb4ef30a6c82362ec7d65df6c0e7297443759fe108b52a.
No host mode logic changes: Main independently verifies future selected cohort
mode, parser manifest and matching SDK build. Synthetic fixture receipts stay
private, never native evidence or authorization.
SDK owns actual successful-installation emission, unchanged ordinary observer
connection ordering, actual frame counter and hard no-owner/getter/reader fence.
Concurrent render may make installation ineligible; shared-root actor evidence
may stimulate request callbacks. Paired SDK/Buddy critical review was open at this
source checkpoint; the final selection below records closure for its exact freeze.
No nonce, payload build, staging or device action was performed by this lane.
Source basis: current Main selection, repository source and exact local fixture
output; cohort causal interpretation is inference.

## Actual pretoken admission/recovery smoke, 2b34

Main alone operated nonce `2b34ff126957497285b66f77311df07e` after the exact
combined source review. The private final selection records Root review closed
with SDK `aa3b7a5827f549ec6fc7fb507c523ab1a8070208`, Buddy
`8d4de23911af12bdeec8389f75baf69e7c45c386`, selected Docs
`bb14f834b6ac92a622f027732a0efba4e1709508` and R5 coordinator
`ed445c8b00a7e51f58cb4ef30a6c82362ec7d65df6c0e7297443759fe108b52a`.
This later evidence update does not relabel the selected Docs revision.
Consumer mode was `pretoken-facts-entry-v1`, build mode
`pretoken-factsentry-cohort-v1`, parser `trace-stop-pretoken-proof.awk` with
SHA `b06803122b6059adca5f7cf1f257d6483c9f2f2bdf6e52049c4b9e1eac08b759`.
Main's matching-build verification records 30 artifacts and 13 source inputs;
the selected payload was 172388 bytes, SHA
`55f297e129bb281c18e055edba612fd644043c9321aad5e141db7cde24daace9`,
build receipt SHA
`357b558d87edeaff93e32641129b48dd735dd4a7682dd7fdbb8d66e7dc23b69a`.

The retained admission snapshot has four records: startup, entry-installed,
window, before-render. Installation records actual frames=0, startup/GUI TID,
quit=0 and dropped=0 before the qualifying pre-quit render with frames=1.
Exact attempt identity was PID12223/start3181208; stop.admitted contains the exact
nonce and diagnostic.outcome records primary_exit=0. The seven-record final
trace contains two render pairs, all quit=0/drop=0, with no quit/destruction
markers. Candidate STOP records inactive/dead, MainPID0, empty Job,
Result=success and ExecMainCode=2/ExecMainStatus=15 (SIGTERM). No matching SIGSEGV
was reproduced; this does not establish Qt lifecycle completion.

The actor records restored stock PID12830/start3183152. Main's independently
saved postattempt proof/readback confirm unchanged boot
`02b2347b-03aa-4a85-8dd7-d731aabf6f3e`, all24 protected hashes and three
unit/vendor/executable hashes unchanged, original policy/fragment/vendor-only
drop-ins, empty Job/NRestarts0, all three services individually active, no payload
maps throughout the unit and no owned runtime shadows. This lane read those
receipts locally; it did not perform a fresh remote device verification.

This lane independently verified archive size/hash and all61 retained file
hashes without extracting private inputs: 263680 bytes, SHA
`a3c75ba845699616af9b730e51431fed99491192f5a679096d0ae55530ab7b8d`.
Private evidence directory is
`main-shutdown-lifecycle-2b34ff126957497285b66f77311df07e` under Main's
device-private workspace. The cleanup receipt records all61 hash/mode validation,
collected actor unit absence proof (LoadState=not-found/MainPID0/Job empty),
exit0/no timeout and exact residue removal with archive preserved and no stock
STOP/start. No public artifact link exists in this receipt; canonical persistence
and the next discriminator remain Main/Astra-owned. Nonce2b34 is spent and cleaned.

This is narrow actual pretoken proof admission and guarded restoration evidence.
Material bootstrap limit: this lane read archived callback.json, whose stage is
facts-entry-bootstrap-refused, source_facts_reader_stage is empty and
engine_thread=false. No facts-waiting exists in the complete 61-file archive.
Main and Astra independently confirmed that installation did not establish
successful engine bootstrap. The absence alone is not proof of never-ready,
because SDK finish unlinks facts-waiting; the callback provides the refusal evidence.
The shared-root watcher stimulus and coarse setup/timing cohort remain causal
limits. It neither fixes the original 0404 SDK fault nor qualifies native MVP,
FactsEntry/Reader production, candidate host-loss recovery or complete prearm
ordering. The unfinished change is not synced or archived. Source basis: current
Main handoff, locally read final selection/build/postattempt/cleanup receipts and
independently hashed archive members; causal interpretation remains inference.
## Full actor simulated-host loss control

The complete rendered actor now has an owned host-only regression that starts
at main admission, consumes guard/start requests from a separate simulated host
session, reaches candidate activation, survives termination of that host session,
and lets its observation deadline expire before its actual EXIT/recovery child.
It requires exit1, preserved diagnostic failure, guarded candidate stop before
candidate/process/cgroup absence, removal of owned shadows and exactly one stock
restart plus final verification. Both process sessions are killed/reaped in the
test's finally path on failure. Services, process identities, health and clock
remain injected; no actual systemd or tablet candidate is exercised.

The initial run failed an assertion because stock and candidate both used fake
PID42/start561; the first matching disappearance event belonged to stock. The
fixture now uses candidate43/start562. This was a fixture identity/assertion
repair, not a runtime recovery defect. The targeted successor passed0.253s;
after requiring exact exit1 and candidate-before-cgroup ordering, the final
affected suite passed all21 tests in4.479s. Runs used the existing offline image
sha256:fd04716b488bc88f96b1ba1390783986fd75133992f3fe613182f98b2f52a86f,
network disabled and source mounted read-only. Original actor/launcher/parser
bytes are unchanged. Raw successor logs are retained privately without a public
transcript link; the original failing assertion remains in the tool record.

This strengthens modeled full-path coverage, not native candidate-hostloss,
complete prearm ordering, Reader readiness, write/persistence or REM25 closure.
Independent successor review and normal paired delivery remain pending. No
artifact build, transfer, nonce, activation or tablet operation was selected.
Source basis: existing actor/fixture code and the directly observed owned runs.

## Engine-ready consumer source freeze

The settled explicit mode pretoken-engine-ready-v1 selects
trace-stop-engine-ready-proof.awk. The original-file observation draft was
superseded before verification and preserved privately as unverified source only;
it produced no packet, SDK build, nonce or device action. The settled implementation
adds no actor observation phase or SDK edits in this lane.

Three focused fixture methods passed in 0.296 seconds in the pinned offline image:
engine-ready ordering/counter/refusal matrix, current pretoken matrix, and packet
preparation/selection compatibility. Cases cover installation→ready→later pre-quit
render, earlier/equal/post-quit renders not qualifying, absent readiness, duplicate
or out-of-order readiness, startup TID/quit/drop/canonical fields, exact process,
sequence/time/record cap, frame regression and adjacent uint64 counters above
double precision including the maximum. Both old parsers reject the new event.
Preparation checks exact explicit mode/proof source and manifest parser binding,
all other initial packet hashes unchanged, no added packet files, malformed-mode
refusal and identical output under simulated Windows CRLF defaults.

New parser source SHA
a5649c731eefff956ba334b213057f2449751985d9f143533d7307635edaefc7.
Actor, launcher, legacy and installation-only parser hashes remain unchanged.
SDK emission after original readiness write/destroyed connection and hard request
fences require paired Main/Root review of Astra's exact source. No native eligibility,
engine readiness result, fault fix or broader recovery qualification follows from
these fixtures. Source basis: current Main settled interface, repository source,
locally read 2b34 callback/archive and focused test output; timing rationale is
explicit design inference. New paired source-hazard review remains open.
