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

Twenty host integration tests pass: Store reopen with Reader/Writer/Reader chronology;
concurrent identical retry and lost commit acknowledgment; stale-head refusal;
generated-to-verified completion; competing page/conversation claims and deletion
retry without resurrection; shared media retention/missing objects; exact prepared
batch reuse; failed storage/invalid dimensions before dispatch; and exact export
marker discovery; replica multihead refusal; explicit ranges, corrections and typed
budget refusals; duplicate/unallocated imported chronology refusal; retained media
after a source tombstone; truncated pixel data and missing allocated turn refusal;
unknown payload/legacy coexistence; four commit failure boundaries;
native-parent crop byte identity; competing different-page claims; malformed imported
identity/geometry; and isolation from unrelated oversized conversation metadata.
Strict all-target/all-feature Clippy passes. These are domain
tests, not a real Reader recording-provider integration or tablet smoke test.
The complete Windows all-target/all-feature suite passed 263 tests at Rust5772c25.
Later independently reproduced malformed-image and chronology-gap fixes pass the focused 20-test domain suite
and strict all-target/all-feature Clippy; that full-suite result is not attributed
to a later tree without another full run.

The generic Store snapshot selects matching logical records under one lock, including
every head and tombstone when any head matches. It refuses more than 4096 selected
heads or 8 MiB of selected serialized metadata before cloning instead of truncating.
Conversation inspection applies these bounds to the requested conversation; unrelated
foreign history does not consume its budget. The retained-media report also inspects
bounded historical source revisions, including references superseded by tombstones.
Imported payload identity, geometry and media
descriptors are checked; image retrieval verifies its encoded hash and dimensions
and fully decodes PNG/JPEG without reencoding. Image decoding refuses either axis
above8192, a four-byte-per-pixel preflight above32 MiB, or decoder allocations above
32 MiB; this is an image-decoder limit, not aggregate process memory qualification.
Live-root inspection requires unique allocated sequence coverage without allocating
an attacker-controlled sequence range. Independent review found the previous header-only
check and skipped-turn behavior insufficient despite the passing earlier suite;
adversarial regression evidence drove these fixes.
Reader still uses its existing orchestration; its Store handle, exact capture batch,
terminal outcomes and qualified restart/revisit seam have not yet been integrated.

The SDK consumer persistence checkpoint pins source7e8ffd51f27cc63d79475754071b6444eab048fb.
Its separate historical DTO preserves original scopes, synthetic labels, intervals,
u64 values and floating-point geometry bits without restoring a live SDK guard.
Synthetic preparation atomically commits the prepared turn, complete facts and exact
parent/provider media; retries retrieve the original ordered bytes. Eight additional
real-Store tests cover reopen, strict decoding, distinct acquisition scopes, storage
failure boundaries, tampered dimensions, nil operations and both recovery cases.
Unexpected required-media corruption discovered during Store recovery causes a typed
store-wide IncompleteStore refusal. This conservative refusal can affect unrelated
conversations because skipped commits cannot reliably be attributed. Explicitly
declared unavailable media in a selected-record restore instead preserves text/facts,
reports absent evidence and refuses image retrieval. Deleted capture history remains
in the retention report. No Store recovery protocol was changed.

The fixture dispatch counter observes bytes retrieved by the persistence API; it is
not a real Reader/LLMEngine recording-provider test. Initial SDK capture construction
validates derivation pixels; restored DTO checks validate descriptors and lineage,
not a second pixel derivation proof or cryptographic authenticity of imported facts.
Reader integration and native qualification remain open.

At exact Rust b4bee21ad4c5a4e0b280298922158509cbf05c1b,
`cargo test --all-features --locked` passes272 host tests and one compile-fail
doctest on Windows. Formatting and strict all-target/all-feature Clippy also pass.
This replaces the earlier full-suite checkpoint for this source tree; ARM/AArch64
builds, actual Reader recording-provider integration and native smoke remain open.

Independent review then found that individually valid restored derivative geometry
could contradict its parent/crop. SDK helper72a896e received independent Sol review
and was integrated unchanged at2d473f0954120889f8a04c6294151241576ff8c3. Buddy's
follow-up pins that source, requires the known derivation procedure and compares
the SDK-recomputed affine/valid region by exact stored bits. Proper child-envelope
tampering of affine and valid region now refuses retrieval/inspection, alongside
the dimension regression. The focused28-test suite, compile-fail doctest, formatting
and strict all-target/all-feature Clippy pass for the follow-up. The full272-test
result above remains attributed only to b4bee21. Independent consumer fix review
is pending; no native or entire REM37 acceptance follows.

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
