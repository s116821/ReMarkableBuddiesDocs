# Verification status

Root accepted precode0c9fa3c in the canonical REM42 discussion before implementation. The paired branches normally reconciled delivered Buddycc3dd72 and Docs93907ce, preserving portable configuration and notebook restore. Implementation is [Buddy PR130](https://github.com/s116821/ReMarkableBuddies/pull/130), exactc0a2e1a4d93b5752dacadd361c3bc49b31ee49ed, paired with [Docs PR142](https://github.com/s116821/ReMarkableBuddiesDocs/pull/142). Independent final implementation review, exact-head hosted checks and finite sync/archive remain pending.

## Implementation and controls

Only product_settings::apply_with and research_settings::apply_with route to the new crate-private Store::open_existing_for_preferences. Maintenance uses the original ExistingCustody before choosing the notebook/legacy layout. A closed internal admission enum preserves existing Deny constructors and Restore behavior; only Preferences requires definite absent/empty selected and retained directories, ready notebook metadata, complete recovery, all local manifests and validated absent/LocalOnly mode. Existing publisher, raw target, intent/path/base/target checks, report custody and wire/runtime semantics are unchanged. Readiness is never repaired; staging is retained.

| Requirement | Meaningful control and current result |
| --- | --- |
| Config-only notebook save | Windows real retained record/media fixture; both writers, absent/LocalOnly mode, optional feedback/retained-selection markers with empty state, exact inventory/source/private-declaration preservation, Busy, reopen, original Status and repeated-Apply conflict; success group passes |
| Unsupported admission | Windows15cases per writer: readiness/contract/foreign marker/old format/selected and retained residue/wrong-type directory/corrupt and nonordinary modes/foreign owner/corrupt commit/object/nonlocal manifest/stale CURRENT; full trees unchanged; passes |
| Existing callers | Old generic/config/mode/archive/outbox refusal preserved on the same notebook; notebook restore still admits; empty regular selected directories admit; passes |
| Uncertain publication/output | Both writers use existing AtomicCall/AfterPublication/ChangedReadback faults; original unknown preserved, immediate/prefix write errors prove Busy throughout write and release afterward; data inventory unchanged; Status only observes original desired bytes; passes |
| Unix link refusal | New symlink directory control is Unix-only, not a Windows pass; hosted evidence pending |
| Actual command dispatch | Both notebook selectors and existing selected-family regression use real bounded subprocesses; Windows3/3pass; no provider/runtime startup |

Reports retain their existing consuming write_all interface, without a flush call. Product successful Apply remains restart-required; research remains runtime unverified. The precode's mistaken flush expectation was corrected to this actual unchanged source boundary. A downstream flush after write_to returns is outside existing custody; no stronger promise was implemented.

## Preserved failures and qualification limits

Initial unit-r1 failed because new fixtures used run_stdin for inspection and expected an existing report flush. Unit-r2 corrected those but its success case sent research Status an extra changes member and was refused as designed. Unit-r3 sends only the original intent and passes the corrected success group. Unit-r4 extends that group with both optional feature markers and passes. Other passing groups were not rerun after this fixture-only extension. Original logs and failed temporary fixtures remain retained; no production validation or assertion was weakened. Existing platform warnings remain.

Evidence logs live in the originating workspace as notebook-preferences-unit-r1/r2/r3/r4.log and notebook-preferences-cli-r1.log. Exact SHA256 logs: unit-r1 fda0c0a4743b22e23b4231b13d122620e07bd2627b17bcbe4bffd2c14b8436f1; unit-r2 c3af97bb9d5031eb3a9e1c2473ecbfa2c1eab6d47e7cf9d6d5c006508a648440; unit-r3 5aad9df6a1270d98abbfbaa6d595db6ece9432d6ea6dbb52b0d996f22143473e; unit-r4 0ccc1dc341128c40d350bce2dab7bbad5b4f226ce86a1ad1a8f9fb6cd6a96261; CLI-r1 ede28e5fa08eb43303cc1878561f62fa94c0f26b6b9f2c2f9e03cb615a17e9ad. The5Windows unit groups pass across r2/r4; the additional Unix symlink group is not compiled on Windows. Normal current-head Linux CI remains pending. The existing ordinary-configuration-target cache was reused, with no dependency added or held cleanup retried.

No real preferences, provider calls, tablet/native execution, credential-file mutation, settings beyond these two writers, notebook imports/sync or runtime activation are qualified. Root owns independent final review, paired integration and actual-main/release verification. Broader REM42/52/35 remain open.


## Preserved first Linux failure and custody correction

Normal run42148917154 at c0a2e1a passes strict Clippy and all6new notebook preference unit groups, including Unix symlink refusal. Its host library940passed/1failed/35ignored: the existing unchanged notebook_archive_descriptor_counts_metadata_without_reading_media_payload expects partial at inspection_v3/tests.rs676 but receives busy. Later binary/actualCLI/Build/Integration were not reached. Failed-stage log notebook-preferences-linux-failed-c0.log SHA2561df8c0f34411008be1819f8f54d4d354ace4d96189f85bff51bde5cdfc0511cb remains retained. The intentional composed memory panic earlier in output is not the failed assertion.

Source inspection identified a report-custody gap: inspection_v3 retained a raw locked File and relied on closing parent descriptors. Concurrent fork may retain that open-file description until exec/exit despite O_CLOEXEC. The Store already explicitly unlocks in Lease::drop for exactly this case. The corrective successor reuses that same existing Lease in inspection, immediately after successful lock acquisition, without changing refusal/witness/output rules. A deterministic Linux-only control holds inherited descriptors in a child, proves Busy during active inspection and requires immediate distinct-lock acquisition after output while the child remains blocked. Child execution uses only async-signal-safe syscalls before _exit; parent cleanup signals/reaps it. No expected status was relaxed, sleeps/retries added or failed workflow rerun. This mechanism is source-grounded; the original hosted log does not identify the exact fork involved. Corrective source review and current successor qualification remain pending.

Root independently accepted the original scoped preference implementation and all5local logs; the separate custody correction and final current-head evidence are separately reviewable. No Windows test rerun is claimed for Linux-only changes.
