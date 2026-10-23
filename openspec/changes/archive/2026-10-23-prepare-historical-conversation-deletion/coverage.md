# Implementation coverage and evidence boundaries

This map names executable checks in the paired Buddy source. Exact committed
heads, executed results and corpus identities are recorded in verification.md and
the separately attributed corpus wrappers. A test listed here is not evidence
that every filesystem, kernel, service or hardware failure has been reproduced.

| Contract area | Source checks and evidence kind |
| --- | --- |
| Closed wire, canonical identities, frozen encodings | `frozen_original_vectors_and_closed_wire`, `complete_closed_request_shapes_and_intent_mutations_refuse`, `refusal_encoding_and_no_input_platform`; both original vector cases remain byte-identical. |
| Actual CLI early refusals | `tests/conversation_cleanup_cli.rs`: clean source/tree/executable identity, all four operations, held input/nonliteral selectors/non-Linux, recognized startup conflicts, missing Config, malformed/duplicate/oversized/nil/array bodies. Every actual CLI path stops before the real observer. |
| Fixed OS observation | `closed_properties_and_states`, `fixed_unit_and_environment_are_not_user_selected`, `synthetic_process_success_errors_limits_environment_and_null_input`, `synthetic_child_timeout_and_overflow_are_reaped`; controlled child bytes, exit, environment, null stdin, missing program, timeout and stream overflow. The fixed production executable is reviewed statically, never invoked. |
| Existing-only custody | `existing_only_missing_markers_and_unknown_layouts_never_initialize_or_repair`, `synthetic_unsettled_busy_and_changed_original_refuse_without_writes`, header-race tests, final-observer Config tests and Unix named-lock replacement; real isolated stores and byte/mtime comparisons. |
| Mode, generation and selected history | `explicit_local_mode_is_supported_and_changed_mode_or_generation_is_not`, `shared_isolated_and_legacy_sync_enabled_never_grant_local_deletion`, `retained_schema_two_is_refused_even_with_current_schema_one`, selected format/feature controls in existing-layout test. |
| Settled exchange eligibility | Empty/interpreted-completed, terminal-failed, `settled_exchange_variants_and_ambiguous_or_pending_states_are_distinct`, `orphan_contradictory_and_ambiguous_outcome_facts_refuse`; original Ledger producers plus deliberate adversarial local commits. |
| Source, binding, export preservation | `synthetic_historical_binding_is_tombstoned_without_history_loss`, `missing_foreign_conflicted_and_changed_original_bindings_refuse`, `synthetic_used_image_survives_logical_deletion_byte_exact`, all four original source producers and twelve orphan/foreign/changed-link controls, completed/unsettled export association checks. Original history, media and association bytes/mtime survive. |
| Inventory reservation | `every_inventory_reservation_boundary_refuses_before_mutation_or_fits` injects exact numeric cap-minus-reservation, one-over and full-cap counters for both two/three-record plans across all five aggregate counters. It does not create hundreds of MiB on disk. |
| Target reservation | `target_count_and_exact_encoded_byte_headroom_are_enforced` models the exact 4096-envelope and encoded 8MiB array limits; its padding envelope is a capacity buffer, not a domain-valid conversation. Domain eligibility is tested separately. |
| Physical commit-directory boundary | `synthetic_commit_entry_headroom_refuses_before_prepare` and `actual_commit_entry_boundary_still_allows_original_receipt_reopen` create actual bounded staging entries. The admitted case publishes and reopens original apply/status under unchanged global caps. Other huge aggregate boundaries use numeric models above. |
| Cumulative work | Sticky byte/visit meter test and `shared_sixteen_mib_object_in_thousand_manifests_refuses_within_one_budget`; actual shared 16MiB object and 1000 valid manifests, no unbudgeted legacy recovery fallback. |
| Atomic publication and uncertainty | `before_objects_fault_has_no_effect_and_original_status_remains_unchanged`, `synthetic_lost_ack_partial_objects_and_original_status_never_republish`; existing BeforeObjects/AfterObjects/BeforeCommit/AfterCommit hooks. Output failure/held-lock test covers transport loss, without appending a second report. |
| Historical receipt/current state | Exact original retry, later competing revision/conflict, raw-manifest formatting rewrite, receipt corruption/changed identities and `matching_tombstone_without_original_receipt_is_unresolved_not_acknowledged`. Original receipt alone acknowledges; partial evidence cannot dispatch again. |
| Same-process writer exclusion | `active_legacy_publisher_handle_is_not_external_maintenance_authority`; one held Store mutex/ordinary mode lease and existing worker handles. Existing legacy APIs and unchanged regressions remain in normal CI. |
| Staging and external documents | `ordinary_staging_and_unrelated_original_documents_remain_unchanged`, plus preservation assertions in other fixture groups; no cleanup, physical reclamation, remote deletion or native authority. Unix symlink/hardlink refusal executes only on Unix. |

The shared contract's source review also checks pre-read metadata limits, bounded
EOF sentinels, exact transaction membership, no fallback recovery and one mutex
through final revalidation/publication. Numeric reservation controls complement
these mechanisms; they are not physical I/O stress qualification. Fault hooks do
not reproduce power loss, every kernel atomic-write interruption, or tablet
directory durability. Production `systemctl`, live credentials/providers, native
pages and service mutation are outside this execution. The Linux normal pipeline
supplies Linux source/fixture/build evidence only. Manager consumption, runtime
activation and integrated project qualification remain separate work.
