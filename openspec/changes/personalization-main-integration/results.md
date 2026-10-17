# Integration evidence

This is the independent-main successor of configuration PR39 and Docs PR28.
Pre-code design was committed as `cb74fbf` before implementation. Source
`daa4ea5` records both prior owned source `214db007` and current main `f1d697ce`
as parents; previous source history and other feature branches remain intact.

The source diff against current main contains seven paths: configuration,
personalization, CLI dispatch, the shared Store lease, its existing Linux lease
regression's field access, the new maintenance constructor and focused tests.
No SDK dependency, Cargo lockfile, pipeline or Reader/provider implementation is
imported from the old stacked branch.

On Windows with Rust 1.98.1, the final focused run passed 14 tests: four CLI unit
controls, eight filesystem/actual-process personalization controls and two
adjacent configuration controls. Compilation took 11.59 seconds on the second
run; test groups took 0.01, 1.93 and 0.01 seconds respectively. The initial run
had seven of eight personalization tests pass; its new fixture snapshot tried to
read the exclusively locked zero-byte lock file on Windows. The fixture now
checks that known empty file's metadata while retaining byte-for-byte comparison
of every other file. Production code was unchanged by that test correction.

The new controls cover missing identity/lock/current/owner/format/directories,
foreign ownership, unsupported generation format, nil generation and corrupt
commits; refusal leaves the directory tree and configuration unchanged. A later
actual child command succeeds after rejection, demonstrating lease release.
An already held owner refuses a child command as busy. Successful maintenance
retains exact Unicode, line endings, immutable prior snapshots and existing data.

Formatter passed. Pre-closeout Docs guidance verified 22 current files and 126
preserved source blobs; strict OpenSpec passed 30 items. Final strict lint,
supported hosted CI, independent review and final lifecycle checks are pending.
These are host filesystem/CLI results, not tablet, live-provider, running-runtime
activation, Writer or whole-personalization qualification.
