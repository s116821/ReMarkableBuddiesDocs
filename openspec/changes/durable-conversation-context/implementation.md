# Partial implementation checkpoint — October 1, 2026

This active change is unfinished. No canonical sync, archive, native compatibility,
Reader integration, PR readiness or release completion follows from this checkpoint.

The Buddy-owned Rust domain now has typed roots, turns, source-use records, page
binding receipts, export associations and operation acknowledgments over the
accepted REM-36 Store. It allocates chronology with root CAS, finds identical
operation acknowledgments before stale-head checks, stages exact inference batches,
distinguishes prepared/interpreted/generated/completed/failed/canceled/uncertain
outcomes, records verified completion facts, atomically claims a deterministic page
binding, and tombstones root/binding together. Stored facts never grant native
permission. Native-assigned page allocation remains outside this consumer contract
until a separately reviewed REM-25/SDK amendment.

Exact context excludes prepared/generated attempts, refuses unknown or exceeded
provider budgets, and reports missing media. Retained-history inspection reports
referenced bytes and global retained revision reference counts without deleting
objects. Export marker discovery produces unique/conflict/uncertain decisions and
never performs an external write. SDK/native receipt qualification and real export
adapters remain separate gates.

Nine host integration tests pass: Store reopen with Reader/Writer/Reader chronology;
concurrent identical retry and lost commit acknowledgment; stale-head refusal;
generated-to-verified completion; competing page/conversation claims and deletion
retry without resurrection; shared media retention/missing objects; exact prepared
batch reuse; failed storage/invalid dimensions before dispatch; and exact export
marker discovery. Strict library and conversation-test Clippy pass. These are domain
tests, not a real Reader recording-provider integration or tablet smoke test.

The generic Store snapshot is bounded to 4096 selected heads across the inspected
namespaces and refuses an oversized result instead of truncating. This bound is
global to that snapshot, not a per-conversation scalability claim. Complete conflict,
partial-restore, unknown-schema and failure-boundary coverage still needs expansion.
Reader still uses its existing orchestration; its Store handle, exact capture batch,
terminal outcomes and qualified restart/revisit seam have not yet been integrated.

Source basis: current checked-in source/tests and observed local commands; accepted
Docs amendment 0694cb53c761141d01be377218d2d862e82d36f8 over Docs8008389/Rustff8ad75;
independent Sol amendment review; coordinated SDK design e63010e. SDK prototype
review accepted only its explicitly synthetic unpublished slice at source6390526,
with identical rebased tree at523d396; it supplies no qualified native capture or
page-creation capability yet.
