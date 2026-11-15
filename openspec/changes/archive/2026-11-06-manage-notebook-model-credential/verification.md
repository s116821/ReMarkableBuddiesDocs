# Finite protected notebook credential-file verification

Paired delivery: [Buddy135](https://github.com/s116821/ReMarkableBuddies/pull/135) and [Docs147](https://github.com/s116821/ReMarkableBuddiesDocs/pull/147). Original source `f62a62a8b0e35d3ff571a2130abd1b07db0b5d05` was based on delivered `dc5118e15d4490efb22f04e4e6f2f96d24704356`; precode Docs `0dc7a097ac68f6343c7f8a9d3b6a40577999a807` was independently accepted before implementation. Initial implementation Docs `1de40daff3686027bb8b57ffeb4bb44a2883c90e` passed all three checks in42175501925.

## Source and review

Only Linux Apply and its single-consumer private constructor change production admission, using unchanged selected-aware Preferences recovery. The generic alias and obsolete generic-only test probes are removed; actual ordinary/mode/archive/outbox/conversation Deny paths remain. Protected binding/private modes, publisher/mutex/sealed-stage/race/unknown/readback logic, consuming custody, original-only Status and non-Linux early Unsupported are unchanged.

Independent source review identified a new stale-Status test expectation and obsolete guide wording; successor `818c357c45db4363f57e480fdc933a95bcad00e7` closes both. Status expects conflict/read-only while Apply preserves conflict/not-dispatched. The metadata permission accessor correction and these test/guide edits introduce no production/wire successor delta. Independent successor review accepted this finite scope. Original reference archives remain immutable.

Normal upstream merges then produced source `f32d5dc0ebc613007ab8734692d6a6f4d4a4a312` with main `6b52a6db5067f18dcaf4f8da03c6290bae98e702`, and Docs `1d76f5ef3857b37ec4074aeed872c2ee3ab803cf` with main `f0bad1743cf03c851e8af316804068709b4221b9`. Only unrelated package-inputs files were added by those merges; credential feature content was unchanged. The three accepted central deltas are synchronized in this finite archive delivery.

## Completed execution and retained failures

All paths below are task-local logs under the originating workspace's `work/`, retained separately from source. Values and fixtures are synthetic; no actual key is included.

| Revision / scope | Observed result | Retained log, bytes, SHA256 |
|---|---|---|
| Precommit original source content, Windows | Early Unsupported1/1; no stdin/config/key access | `notebook-credential-file-windows-unit-r1.log`,2912, `d1d6f0adfa7c5b14b7c9b83c8a47847092a513b9936a7ef3ca81f0a33934f2b1` |
| Same Windows source content | Notebook preference regressions3/3; actual remaining Deny probes preserved | `notebook-credential-file-windows-notebook-r1.log`,3221, `18e6c1ce040cbb815e66bb366edaa6cb78ac974eabd69fa952f11a9c319a2149` |
| f62, CI42175438485 | Clippy compile failure in new CLI Metadata.mode() assertion before test execution | `notebook-credential-file-linux-failed-f62.log`,120650, `7c14bf61dc4eeec8e0e8bc66aeca2a53bca0dee28415ff7437f7291518183fad` |
| c1e51ed913bc059c7ecd1d6f8a100392442ad333, CI42175822492 | Permission accessor fixed; Linux CLI failed stale-Status oracle, actual read-only vs expected not-dispatched | `notebook-credential-file-linux-failed-c1e.log`,1384770, `c300eceaaef35e8e6bab21c09a936edf33700a32be7fec7397be6bdcf27f20e1` |
| 818, CI42176163296 Checks job127755042769 | COMPLETE PASS, strict Clippy and host tests; library949passed/0failed/35ignored, binary13passed, both credential CLI tests passed | `notebook-credential-file-linux-checks-818.log`,1699951, `4f2f17ec5ba3c71f05f89c04b0679f90971a0b7b6f46a2f42c8b334f797d12ed` |

Linux controls cover real record/media notebooks with absent/LocalOnly modes, install→distinct replace→remove, exact CRLF/Unicode/trailing text,0400/0600 preservation, no-op, legacy1/2/3, Busy/original Status/stale Config, refusal without repair, no-clobber competitor, original condition drift, unsafe modes/aliases, sealed-stage tamper, phase failures/changed readback, actual Config/file mutex exclusion and immediate/prefix output failures with ownership held and flush forbidden. Successful CLI operations preserve Config/data/cache/other-file inventories; only the declared target changes. Legitimate parent entry-time effects and retained unsafe/unknown stages are not falsely graded invariant. Existing clean-checkout/executable corpus provenance and unusable provider sentinels remain. Windows does not execute these Linux positives; no duplicate Windows run is credited for Linux-only oracle/guide corrections.

## Required final gates and limits

Author Docs validation passed: strict all-spec119/119, manifest/current guidance36 and preserved source blobs126, and diff whitespace checks. The archived contract link resolves to the original unchanged protected-file contract; canonical requirement blocks are unique and match the accepted deltas.

As of author archive, exact reconciled sourcef32 CI42177444274 is running and remains required; premerge818 Checks PASS does not validate this later revision or establish its Build/Integration completion. Final Docs revision checks and final paired feedback remain required before coordinated merge/main/release. This is completed finite feature implementation/review/focused execution, with final delivery gates explicitly pending rather than waived. Broader REM42/52/35, credential authentication, host setup/UI/private buffer lifetime and integrated release/native qualification remain open.

No real credential/provider/device/native/service/root relocation/reference edit/synchronization or runtime activation occurred. An existing development Cargo cache was reused after free-space/ownership checks. No cleanup was selected; validation logs remain preserved. Source basis: exact repository revisions, current CI/job output, hash-verified local receipts and independent review.
