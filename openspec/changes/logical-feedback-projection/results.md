# Verification record

State: implementation candidate; hosted qualification and independent implementation review pending. No runtime acceptance.

Basis: current feedback/layout requirements and issue chronology, delivered src/conversation/feedback.rs, src/conversation_layout.rs and domain Turn/ContextView definitions. The delivered fixture correction is a separate completed source increment; its actual-main publication is still independently observed.

Planned evidence: actual Store tests through the composed public API, unchanged original receiver controls, exact three-path preservation, normal hosted current-head source/package checks, Docs validation and independent review. No model/tablet/SDK/native operation is requested or claimed. Pre-attempt/unassociated retention remains open.

## Implementation candidate

Central precode 598899b7aacbe4ba2118f07520e9d48062ffbe7d received independent acceptance before source implementation. Source [PR108](https://github.com/s116821/ReMarkableBuddies/pull/108), head f151fd5fcd9cbe62c03ca2b054580635aa5b2393 over delivered 40eb5c2ced066d2256fa2f87d173307d409cfdf8, changes exactly the three proposed paths. All 533 other existing source entries, including tests/stored_feedback.rs with its original 14 controls, are unchanged. Existing PagePlan/Exchange shapes and both public APIs remain; the new wrapper and plan_stored path share the existing ordinary validator and retain custody through the callback.

Six authored actual-Store tests cover reopened catalog/uncertainty composition and original content borrowing; mutations of every selected Turn field; planner/identity/context refusals; older fact versus later retained turn and stale context; snapshot/mode refusal privacy and custody release; and original-exchange linkage in newest-first history. Parameterized cases are subcases, not extra test entries. Formatting passes; no compile/test execution credit is claimed yet. Normal hosted [run40379469458](https://github.com/s116821/ReMarkableBuddies/actions/runs/40379469458) is pending.

## Precode qualification

Docs [run40378099753](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/40378099753) passed portable tests on Ubuntu and Windows and strict OpenSpec. Local guidance passed 25 current files/126 original blobs; strict validation passed 95 items. Local portable execution produced six passes and six fixture-setup errors on the Z network share: Git2.44 refused SMB-owned temporary repositories. A separate probe reproduced that ownership restriction; no global trust setting was changed. These environment failures and the later hosted passes remain distinct. An aggregate log retrieval failed before producing a file; actual completed per-job API logs are preserved instead.

State remains implementation/qualification in progress; no canonical sync, archive, delivery, presentation or native acceptance yet. Pre-attempt/unassociated retention remains open.

## Corrected candidate and test traceability

Static review of f151 found a fixture setup error before any execution-pass claim: Ledger::append requires caller sequence zero and allocates chronology. Corrective source 0a0d61d5216726f488715c8c2688cbc3b3e90d44 changes only that test to append without chronology and read back the actual persisted later turn. Production implementation remains identical. Initial run40379469458 is preserved separately; corrected run40380066811 qualifies only the corrected head. Independent static review of the corrected source is clear; execution remains pending.

| Contract scenario | Authored actual-Store control |
| --- | --- |
| Exact fact and unchanged logical content | reopened_actual_feedback_composes_without_replacing_original_content |
| Every selected turn field / stale or unrelated context | every_selected_turn_field_must_match_the_stored_snapshot; original_planner_and_explicit_identity_refusals_still_apply |
| Existing query/refusal/mode privacy | composed_receiving_preserves_snapshot_refusal_privacy_and_mode_release; unchanged original receiver suite |
| Older fact versus later retained turn | older_fact_keeps_its_identity_while_context_must_match_the_later_turn |
| Uncertainty and description privacy | reopened_actual_feedback_composes_without_replacing_original_content |
| Original exchange / newest-first content preservation | feedback_remains_with_its_original_exchange_in_newest_first_history |
| Missing pre-attempt identity refuses | original_planner_and_explicit_identity_refusals_still_apply |

The mode controls observe admission/refusal and release after the call. Custody during the internal callback is additionally established by the lexical RAII lease in the shared validator, not a claimed dynamic in-call race measurement. Privacy assertions apply to the new static description; the page intentionally borrows the original caller content unchanged.

## Observed initial qualification failure and schema fixture correction

Initial source f151 run40379469458 completed failure. The original receiver group passed all14 tests in3.50s. The new composition group passed4 and failed2 in0.19s: append rejected the multi-exchange fixture's caller-supplied chronology, and generic Store rejected its schema999 fixture before the receiving API ran. Raw Checks log723210 bytes has SHA256 8afa0f958e45fdb91d3c1f2d0088db1e6937154c887c0d7a0b8a28e04a05eb5d. These setup failures are not receiver-refusal successes or production defects. Later test groups and package stages receive no pass credit from that failed run.

Current source35115859f3e4ac7b27d74f4a90a392be2afd7d70 additionally corrects only the schema fixture to generic-supported envelope schema2, which the ordinary historical receiver explicitly refuses before domain decoding. Every refusal-matrix case now asserts its precise static diagnostic. Production implementation remains identical to f151/0a0d. Intermediate0a0d run40380066811 is retained separately; no full pass is claimed. Current run40381881821 qualifies only351. No assertion is weakened and no unchanged-head retry is used.

## Full later-exchange fixture lifecycle

Intermediate0a0d run40380066811 completed failure with4 composition passes and2 setup failures in0.18s. Its723203-byte raw Checks log has SHA256 5fc3f2679d183fa042e83541fd3d8fe67f22cc3d150ef0c203a23b02c206a0f5. Removing caller chronology exposed another existing domain requirement: Prepared turns cannot contain verified text. The schema999 setup refusal also remained in that intermediate candidate. Neither result qualifies current behavior.

Current source33b3bc6d4c6f6be89f7ae2013e35c04a76b3f13c uses the actual valid ledger lifecycle for the later exchange: append Prepared/None, inspect allocated chronology, record terminal Failed/text with fresh root and turn expected revisions, and inspect the actual final turn. It preserves every immutable field and still selects the original explicit fact.id/code despite the newly stored distinct later fact. Production and the original14 receiver tests are unchanged. Independent review of the complete call chain is clear; current run40382731211 remains the required execution gate. The schema-corrected351 candidate/run40381881821 is preserved separately and has no current-head pass credit.

Schema-corrected351 run40381881821 subsequently completed failure with5 composition passes and1 setup failure in0.20s. Its722423-byte raw Checks log has SHA256 60149f372a77a86ffaa2656c981bb78a7be42f019c1801be268ce5921fbf064d. The exact refusal/privacy/mode matrix passed; only the known Prepared/text setup failed. This result remains separate from current33b3 qualification. All earlier observers closed after retaining their actual results; only the current exact-head qualification continues.

## Current source checks

Current33b3 [run40382731211](https://github.com/s116821/ReMarkableBuddies/actions/runs/40382731211) passed Checks: all6 actual Store composition tests in0.23s, original14 receiver tests in3.57s, library548 passed with3 existing ignores, binary11 passed, full cargo tests, formatting, strict all-target/all-feature Clippy and release-tool controls. Raw Checks743494 bytes has SHA256 8a7680fb968813e0b7a576e91011a7183e3c8d59970af169fbb9168926300d1c. API-verified tested merge7d2fda932dddad0d77b396e0a53a2aaf9c31d7b6 has exact reviewed treeed9c92f8a536cfcf7e711abf4d153ec8928c17e5 and parents40eb plus33b3. Build/Integration remain pending, so no full qualification or archive is claimed yet.

Pre-merge lifecycle readiness includes a concrete post-merge observation handoff, not a claim that an unmerged candidate is already published. Actual-main and official release observation remain separately tracked after normal coordinated delivery; the task wording now states this explicitly to avoid a circular pre-merge publication checkbox. Broader retention/native/runtime gates remain open.

## Full current source qualification and canonical synchronization

Current33b3 run40382731211 completed SUCCESS: Title, Checks, package Build and Integration passed; Release skipped normally for the PR. The sole current observer closed after retaining all actual logs. Build178418 bytes has SHA256 f8140e2200e777ac244d0bb289636e93cd6c0d5dfd7bb3a9d7f4ef5103e15627; Integration43310 bytes has SHA256 a2ba854a9f95689c9828c5ae71ba99f5f5a76a05c0e09549e73078a013573e45. This is exact-candidate hosted/package evidence, not actual merged-main publication or tablet execution. All three earlier failed candidates remain separately retained.

The canonical feedback specification now preserves the complete original4-requirement/9-scenario prefix and adds exactly the accepted2 requirements/6 scenarios, for6 requirements/15 scenarios total. No other canonical capability changes. Only this change remains active while the synchronized Docs checkpoint obtains current portable/strict hosted qualification; archive and final delivery review remain pending.
