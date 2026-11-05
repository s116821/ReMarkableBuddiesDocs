# Historical association inspection: bounded host result

The host-only increment is implemented at Buddy
`8f1749ee2343069ece7b9c3f70f313ea4c31d747` after the preserving foundation merge
`03342b5dbd3da84eb89aaac84ede82f4e41689d9` (parents: the existing REM-25 topic
and delivered main `cc317ff53e1dd6f612b2e82707e5a5e4b50e0265`). Docs foundation
merge `de6bacb` likewise retains the existing topic and delivered contracts.
The dependency stays at the delivered SDK `32b86e4fef04844cbf2ec31129bf029cc1d9899a`,
without default features for ordinary builds and with mock only for tests.

## Implemented boundary

`Ledger::inspect_page_association` obtains matching current heads and the
unavailable-commit count under one Store mutex, retaining the exact queried
binding key even when its payload names another conversation. Existing item and
metadata bounds remain. The cloned snapshot supplies both head revision IDs;
validation reuses the historical chronology helper and existing binding receipt
rules without another Store read. Missing, conflicted, tombstoned, unbound or
foreign claims remain unresolved; incomplete/malformed snapshots refuse.

`HistoricalLedgerLookup` borrows the existing Ledger and implements the existing
read-only decision interface. A matching saved claim maps only to Historical.
Uncertain/failed inspection never maps to Missing or RelevantModelAssociation.
The existing observation/receipt guards still precede lookup. No new registry,
Store schema, ownership lease, receipt issuer, Store write, platform operation or
installed Reader wiring was added. A returned candidate remains historical after
later Store changes; its revisions are not current-state admission.

The protected unmerged selected-admission implementation was inspected only to
avoid duplicating its scope. It was neither copied nor edited. The independent
helper artifact, Python consumer pins, existing fixture pages and held/spent
operations remain preserved.

## Executed checks

Windows used rustc 1.98.1 / Clippy 0.1.98. Commands ran with `--locked --offline`
after the delivered dependencies were available; a fresh contributor can fetch
those declared dependencies normally before using offline mode.

| Check | Observed result |
| --- | --- |
| `cargo test --test historical_association` | 8 passed: actual Store/SDK Mock current and successor paths, exact historical pair/revision retention, missing/foreign/conflict/tombstone states, malformed evidence, unavailable transaction and incomplete chronology; no decision Store writes or SDK effects |
| `cargo test --lib storage::snapshot_status_tests` | 1 passed: an actual writer observes Store mutex contention while the predicate is paused; the snapshot retains both old heads and the next snapshot observes both committed replacements |
| `cargo test --lib workflow::sdk_buddy_decision` | 19 existing decision regressions passed; the subsequently extended logical-claim loop was separately rerun and passed with UnresolvedStored included |
| `cargo test --test conversation` | 20 existing ledger regressions passed after the shared validation extraction |
| Ordinary `cargo check --lib` | Passed; no mock feature was added to the ordinary dependency |
| Owned RGB32 layout/refusal and asymmetric-channel pixel tests | Both affected existing tests passed after the two-expression lint repair |
| `cargo clippy --all-targets --all-features -- -D warnings` | Final exit 0; original exit 101 with two inherited constant-chunk diagnostics is retained |
| Formatting, diff checks and targeted strict OpenSpec validation | Passed |

The lint repair changes only two constant-size screenshot expressions to array
chunks and removes an unnecessary fixed-word conversion assertion. It does not
alter framing, dimensions, channel mapping or remainder handling. No ARM/tablet
artifact was rebuilt: the previously frozen stock screenshot and gesture helper
artifacts remain unchanged. The modified logical-claim test and two affected
image tests were checked directly; no unrelated association or hardware matrix
was repeated for this cleanup.

The initial six-case, later seven-case and final eight-case association runs are
distinct retained observations. The table reports the final eight-case run, not
a relabeled predecessor. Private raw logs and the frozen precode/source review
record `ef955d9b6d0cda0918839dca916320612c8cdd64ff3f5a29e063d85975ee9dcc`
are retained locally without public download links. Independent review verified
its 20 files and the actual check logs, found no blocking source issue, and
accepted the separate two-expression quality repair and final quality outputs.
This is owner execution plus independently inspected evidence, not a reviewer
rerun, minimum-compiler run, native test or hosted CI pass.

## Remaining delivery and runtime gates

This accepts only the historical read/projection increment. It does not approve
the entire older native topic or finish current native identity, source5
creation/navigation/blank display, association adoption, installed Reader,
writing/persistence or independent runtime recovery. No tablet, provider,
account, credential or sync operation was performed for this increment.

Linked source/spec review and required hosted checks remain part of coordinated
delivery. The whole change is unfinished; its unimplemented native requirements
are not promoted to the canonical baseline or archived by this host result.

Source basis: delivered public Store/Ledger/SDK revisions above, actual current
source and private executed logs, and independent source/evidence review. The
new query establishes historical correspondence only; it is not a native
freshness, document/page absence or effect-authority oracle.

## Hosted Linux follow-up

The initial hosted Linux Rust/Clippy 1.99 check failed on four inherited
Linux-only diagnostics that the Windows run did not compile. Commit
`e3b875fa6e02ce710085796e3e7de33201ce97c9` names the existing fixture callback and
gesture path types, groups the same four worker-evidence references, and uses
the equivalent positive-count divisibility expression. Independent review found
no runtime change or remaining source issue. No warning suppression was added.

The affected Linux x86_64 gesture suite initially recorded 28 passes, one
failure and three explicit fixture skips. The report-loss test started the
production fence immediately after spawning its child, giving startup only the
50 ms normal-exit grace. The unchanged case passed in isolation; that supports a
timing sensitivity without proving the original failure's cause. The original
assertion did not retain the exit status, and its container-local child log was
not retained. These evidence limits remain explicit.

Independently reviewed test-only commit
`5a7381f65829a5c2e00d364255f09d0ed266dafb` observes actual child exit within the
original fixture write deadline before calling the same production fence. A
hung child is still killed/reaped under the original recovery bound and fails
the normal-exit assertion. Production grace, native profiles and helper behavior
are unchanged. Final affected Linux checks passed: 29 gesture tests with three
intentional fixture skips, and five touch tests. The first failure, isolated
pass and final run are retained separately; an unnecessary intermediate Cargo
diagnostic rebuild was stopped, not counted as a test result.

These local checks used Rust 1.98.1 in the existing host fixture container with
networking disabled and source/toolchain mounted read-only. Missing container
Git metadata produced explicit development-build warnings; this is not an
official release build. The frozen ARM helper was neither rebuilt nor deployed.
Final hosted checks for the successor commit remain a separate delivery gate.
