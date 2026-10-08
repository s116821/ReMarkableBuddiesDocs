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

Temporary executable permission allows only the owned query stub. Thirteen unittest
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

Shell `sh -n` on both templates and Python AST parsing of both Python files passed
after failure-marker, provider-path and Windows LF corrections. Central `scripts/check_docs.py`,
`openspec validate native-shutdown-recovery-guard --strict` and diff checks passed.

## Frozen executable source hashes

| File under Buddy tools/native_shutdown_probe | SHA-256 |
| --- | --- |
| actor.sh.in | ca1a903301f7a616e2a09f8c9f88b022af7366c068e707a4ea3c3b3874ec3671 |
| launch.sh.in | 00747bd76a6a7d556e77cca41afb04e978256a23975770ed29e8af1a186ada95 |
| prepare_packet.py | 3b5ba34576ba72c5739a56da5b9fb1599c57535d12c545da05c56f98943622c3 |
| test_actor.py | 9e4920c642567178df6337893266c20c6426d4f470402010af41d2ad85177a7b |
| trace-stop-proof.awk | e7ad5e8b213b07230181fd608cf4bd706c65f78c6a0b43cf55d773755bb868c6 |

Current Buddy commit `fbb8ea8749befc9722fe147d807f7f3818a08720` includes the
Windows LF correction atop provider-path commit
`293c1c8fc23e4ae75a7c012c9e9a91b40db74f3f` and failure-marker commit
`8f1dd1d2f22c9ed30376f1c34d98d85670c9e5c2`. Actor/launcher/parser and reviewed
private host coordinator source remain unchanged by these preparation corrections.
The linked Docs commit freezes this receipt and central proposal/design/tasks/delta.
No production eligibility, full native candidate host-loss recovery, complete
lifecycle trace, canonical spec synchronization or archive completion is implied.
