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

Nineteen host integration tests pass: Store reopen with Reader/Writer/Reader chronology;
concurrent identical retry and lost commit acknowledgment; stale-head refusal;
generated-to-verified completion; competing page/conversation claims and deletion
retry without resurrection; shared media retention/missing objects; exact prepared
batch reuse; failed storage/invalid dimensions before dispatch; and exact export
marker discovery; replica multihead refusal; explicit ranges, corrections and typed
budget refusals; duplicate/unallocated imported chronology refusal; retained media
after a source tombstone; unknown payload/legacy coexistence; four commit failure boundaries;
native-parent crop byte identity; competing different-page claims; malformed imported
identity/geometry; and isolation from unrelated oversized conversation metadata.
Strict all-target/all-feature Clippy passes. These are domain
tests, not a real Reader recording-provider integration or tablet smoke test.
The complete Windows all-target/all-feature suite passed 261 tests at Rustde355b2.
Later chronology and retained-revision changes pass the focused 19-test domain suite
and strict all-target/all-feature Clippy; that full-suite result is not attributed
to a later tree without another full run.

The generic Store snapshot selects matching logical records under one lock, including
every head and tombstone when any head matches. It refuses more than 4096 selected
heads or 8 MiB of selected serialized metadata before cloning instead of truncating.
Conversation inspection applies these bounds to the requested conversation; unrelated
foreign history does not consume its budget. The retained-media report also inspects
bounded historical source revisions, including references superseded by tombstones.
Partial-restore coverage still needs expansion. Imported payload identity, geometry and media
descriptors are checked; image retrieval verifies its encoded hash and dimensions.
Reader still uses its existing orchestration; its Store handle, exact capture batch,
terminal outcomes and qualified restart/revisit seam have not yet been integrated.

Source basis: current checked-in source/tests and observed local commands; accepted
Docs amendment 0694cb53c761141d01be377218d2d862e82d36f8 over Docs8008389/Rustff8ad75;
independent Sol amendment review; coordinated SDK design e63010e. SDK prototype
review accepted only its explicitly synthetic unpublished slice at source6390526,
with identical rebased tree at523d396. Identity amendment5818938 and accepted capture
contract49171a0 preserve fail-closed unknown identities and native-parent sibling
derivation. Sol capture implementatione0175f7 passes16 synthetic SDK tests, one
compile-fail doctest and strict Clippy with full/minimal features. Independent Sol
review accepts that exact synthetic scope; it supplies no qualified native capture or
page-creation capability yet.
