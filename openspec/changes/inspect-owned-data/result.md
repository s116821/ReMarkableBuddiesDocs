# Owned-data inspection: bounded source increment

## Exact inputs and scope

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

## Observed verification

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

Independent review accepted the contract and final source/test/spec agreement.
The reviewer did not rerun the broad suite. The Unix FIFO lock regression remains
unexecuted on Windows and requires an actual Unix run. No hardware operation or
native authority was exercised by these results.

## Practical limits

The report measures apparent file lengths per owned path, not allocated or
reclaimable bytes. Namespace media references are nonadditive. Missing,
uninspected, mismatched and omitted references remain distinct. Media content is
not read or hash-verified. Windows handle/path identity checking is weaker than
Unix device/inode checking; neither protects against an external writer that
ignores the Store lease. Read access can change access timestamps.

Broad lifecycle tasks remain open. Required strict lint remains failed. Hosted
checks, Unix regression execution and paired draft publication must retain their
actual results before any stronger acceptance claim.
