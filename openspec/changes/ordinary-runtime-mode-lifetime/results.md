# Ordinary runtime mode lifetime: implementation evidence

## Source and ownership

Central precode 1419627ac14fdd141c1ace02e4641f27cab0ac12 was committed and
published before implementation. Main read the current REM-24 description and
all 33 then-current timestamped comments, including the storage owner's precise
ordinary-data versus read-mode boundary. The API agreement is recorded in REM-24
comments dcb9c0c8 and 9fabde6c; public requirements are fully present here.

SCRAPPY's generic one-file commit a40503e89fec18bb6a342ce42b6e4664132a78b1 adds
OrdinaryModeLease and its tests in src/storage/sync/mode.rs. Main incorporated
only that commit with provenance as 6c5e662dadc7d8284750d69e7e6b25d0f6f09258;
the original base blob 88134fbb208b37692e5421cc818127962662634f matches the
inspected runtime parent, and the resulting blob is exactly
8eff48c4cca89971e3f8df89697d855998cc85df. No generic ancestry, Cargo or extra
storage files were imported.

Main's application commit a3b1c75 changes only src/reader_runtime.rs and
src/main.rs. The actual ordinary_store return now carries the checked mode
guard with its Store; main retains it through Ledger, optional memory, the
existing worker and the real loop. Existing selected and historical paths do
not acquire ordinary authority. Original checkpoint branches and all nine
protected unfinished files remain byte-exact. The existing unmerged conversation
foundation remains an explicit parent; this is not a deployed main feature.

## Actual local checks

Windows Rust 1.98.1, locked/offline/all features:

- Six affected reader_runtime tests passed in 1.68s. The new actual startup
  test covers both absent and LocalOnly modes, real Ledger creation, another
  Store handle's refused mode transition, continued exclusion after Ledger
  drop and successful transition only after the returned guard drops.
- Seven affected storage mode tests passed in 0.55s. These include the three
  new generic controls for multiple guards/last-drop, stale/foreign/nonlocal/
  malformed refusal, both-order legacy publisher coexistence and unchanged
  non-mutating original-operation replay. They are not seven additional tests
  beyond that affected group.
- All-target/all-feature strict Clippy with warnings denied passed in 27.52s,
  using one build job. This checks the actual binary caller as well as targets.
  Formatting and diff checks passed.

The generic owner separately reported its seven Linux Rust 1.98.1 affected
tests and strict lint passing; that is distinct from Main's actual Windows
consumer and mode results, not a second native qualification.

The initial filtered Cargo command omitted --lib and therefore compiled many
integration executables concurrently. Windows reported paging-capacity error
1455 while mapping metadata, followed by dependent metadata/import diagnostics
and compiler internal errors; the build exited 101 before tests ran. The full
original log remains retained. A narrower --lib --jobs 1 retry passed without
a source fix, cache deletion or system paging change. This does not establish
a general compiler-defect diagnosis or turn the failed run into a pass.

## Remaining delivery

Independent source/spec review, exact hosted CI, linked publication, canonical
sync and this change's own archive remain required. There was no model call,
device operation, provider/account change or new runtime setter. These host
tests prove the asserted local mode policy, not native Reader capability,
provider synchronization, current-page authority, live mode switching or full
REM-24/52 completion. REM-35 retains the integrated release gate.

Source basis: exact source commits/blobs, actual local retained Cargo output,
the coordinated public contract and separately attributed generic owner results.
Private local logs have no public transcript link until the linked PR evidence
is posted; no historical chat summary is treated as an execution transcript.
