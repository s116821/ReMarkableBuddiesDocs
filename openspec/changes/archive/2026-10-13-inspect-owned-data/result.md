# Owned-data inspection: bounded source increment

## October 13 parent reconciliation

Current inspector source is `0d4409025875ba876be1f8f7764ad81486f8b39b`,
rebased onto owning PR30 repair `b085b3684edfe5e2bb3f8738fd28030772730279`.
The inspector patch is exactly equivalent to original6b1b9fd by Git range-diff;
no inspector source/test behavior changed. The four original inspector Docs
commits were rebased unchanged onto parent Docs
`5382bb79984ca200a34c3358e8ae03cdb673d34f`. The
[parent compilation result](../../durable-conversation-context/runtime-compilation-result.md)
records the explicit test-only boundary for unqualified private execution,
preserved runtime/public contracts and missing production bootstrap.

Required child all-target/all-feature strict Clippy now passes on Windows
Rust1.98.1 (11.22s), along with whole-tree formatting. Actual affected child
integration checks pass:16 filesystem inspection tests and3 CLI subprocess tests.
The Windows case-alias case runs here; Unix FIFO success below belongs to the
earlier hosted revision and is not claimed rerun locally. No broad library/native
or fixture suite was repeated. The existing reviewer accepted exact successor
ancestry, preserved inspector patch and paired result without rerunning builds or
tests; internal review has no public transcript link. Required hosted CI associated
with source0d440902 passes in run38419851583 (and its earlier same-head run38419849331).
The actual hosted source is the normal PR merge
`067192c53ff3e346f5c55a58b41ed835903a979c`, not a bare0d checkout. Its Test,
Check Build & Lint and Release policy jobs pass; Linux inspection16+CLI3 includes
the FIFO lock case. ARM/AArch64 cross-builds pass, which is source-build evidence,
not tablet/native ABI qualification. These hosted checks are separate from the
bare-head Windows results and are not added together as distinct coverage.

Independent named-capability review accepted the functional scenarios and the
precise platform-runtime flag/startup correction at Docs9ca1de7. Canonical sync
preserves unrelated requirements; only inspect-owned-data is archived in this
paired delivery. The original broader REM-42 obligations remain unchecked in
[external follow-ups](external-followups.md). Final coordinated parent/child
review and merge readiness remain separate; this does not complete broader REM42
or parent native/bootstrap/lifecycle gates. Prior failed-lint evidence remains
historical.

## Original exact inputs and scope

Rust source revision: `6b1b9fd539c33ced6ab56541ef332ba05e4ed693`.
Preimplementation Docs contract: `19b5b515f7a3bc786208e4ad6d524251d6686319`.
The Rust parent remains `7b207ec8a42548c12960699854107236eb2bbd7f`
([draft PR 30](https://github.com/s116821/ReMarkableBuddies/pull/30)); the
Docs parent remains `60a8e0e7ec6ec181ed36652b9b7e33d222086a6c`
([draft PR 6](https://github.com/s116821/ReMarkableBuddiesDocs/pull/6)).

This increment implements the existing-owner storage report and actual CLI.
It does not complete REM-42, Manager browser/Electron integration, cleanup,
backup/restore, tablet transport, native qualification or release acceptance.
The protected preexisting Rust changes and untracked pen-path tool were preserved.

## Observed verification at original6b1b9fd

On Windows, a normal Git archive with command-local `core.autocrlf=false`
produced byte-exact committed Cargo/source/test inputs. Seven input blobs were
checked against the source commit. The archive SHA-256 is
`3da097a4cbd208865a300b8b1811abe966341f710ff58d01d381cd7ab626e4df`.
The committed SDK dependency remains `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`;
the protected working-tree SDK pin was not substituted for this verification.

The exact committed inputs passed 16 filesystem inspection tests, three actual
inspection CLI subprocess tests, two existing CLI tests and three binary argument
tests. The tests use real temporary Stores and verify file content, paths and
modification times, including shared references, busy ownership, missing inputs,
bounded incomplete scans and credential/configuration sentinels. The regression
for a truncated history inventory asserts an uninspected reference rather than a
false missing object or missing entry.

Ordinary nonmock library/binary checking passed. All-target/all-feature diagnostic
Clippy completed with the same 24 existing unfinished-runtime dead-code warnings
and no additional inspection warnings. Diagnostic Clippy is not the required
strict lint gate. Required strict Clippy failed with those same 24 existing errors
(exit 101); existing warnings are neither suppressed nor waived.

The full committed-source all-feature test command subsequently completed
successfully on Windows, including library, binary, integration and compile-fail
documentation tests. Whole-tree formatting also passed. The existing ignored
library test remains ignored; these checks do not qualify native behavior.

The paired drafts are [Rust PR 32](https://github.com/s116821/ReMarkableBuddies/pull/32)
and [Docs PR 14](https://github.com/s116821/ReMarkableBuddiesDocs/pull/14).
Hosted Docs Ubuntu, Windows and OpenSpec checks passed. Rust hosted build/lint
failed; the completed job log confirms the same 24 existing dead-code errors.
The hosted Rust test job also passed on Ubuntu in
[run 38282563168](https://github.com/s116821/ReMarkableBuddies/actions/runs/38282563168).
Its completed log explicitly records
`fifo_at_existing_lock_is_refused_before_blocking_open ... ok`, with 16 filesystem
inspection and three actual inspection CLI tests passing on Linux. The Linux
filesystem set includes the Unix FIFO regression; the Windows set instead includes
the Windows case-alias regression.

Independent review accepted the contract and final source/test/spec agreement.
The reviewer did not rerun the broad suite. The Unix FIFO lock regression was
executed by the hosted Ubuntu job, not by the Windows local run. No hardware
operation or native authority was exercised by these results.

## Practical limits

The report measures apparent file lengths per owned path, not allocated or
reclaimable bytes. Namespace media references are nonadditive. Missing,
uninspected, mismatched and omitted references remain distinct. Media content is
not read or hash-verified. Windows handle/path identity checking is weaker than
Unix device/inode checking; neither protects against an external writer that
ignores the Store lease. Read access can change access timestamps.

Broad lifecycle tasks remain open. Strict lint failed at the original revision;
the October13 parent reconciliation above passes locally and in associated hosted
CI. Paired publication does not close broader Manager, native,
release or lifecycle requirements.
