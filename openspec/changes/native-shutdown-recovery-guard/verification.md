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

Shell `sh -n` on both templates and Python AST parsing of both Python files passed
after the critical failure-marker correction. Central `scripts/check_docs.py`,
`openspec validate native-shutdown-recovery-guard --strict` and diff checks passed.

## Frozen executable source hashes

| File under Buddy tools/native_shutdown_probe | SHA-256 |
| --- | --- |
| actor.sh.in | ca1a903301f7a616e2a09f8c9f88b022af7366c068e707a4ea3c3b3874ec3671 |
| launch.sh.in | 00747bd76a6a7d556e77cca41afb04e978256a23975770ed29e8af1a186ada95 |
| prepare_packet.py | 5bf7d1e05b98b9624a378601a88076004ec9d3ae13367d4709603fa1badb176e |
| test_actor.py | e8a4e287f7fee8d368d238cdae17f9f19d5b4451745ee7f1f7c8d7ef0b1b0517 |
| trace-stop-proof.awk | e7ad5e8b213b07230181fd608cf4bd706c65f78c6a0b43cf55d773755bb868c6 |

Corrective Buddy commit `8f1dd1d2f22c9ed30376f1c34d98d85670c9e5c2` supersedes the earlier frozen
`8d03c00d89d7c69318efab51c4067e4fb6289c0b` and includes the thirteen-check guide.
The linked Docs commit freezes this receipt and central proposal/design/tasks/delta.
No production eligibility, full native candidate host-loss recovery, complete
lifecycle trace, canonical spec synchronization or archive completion is implied.
