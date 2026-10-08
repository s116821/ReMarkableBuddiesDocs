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

## October 1 actual Reader persistence checkpoint

The actual Orchestrator now receives the shared Store ledger and selects acquisition
kind before capture. Explicit legacy runs persist strict, unbound evidence with
absent native identity and qualification. Both provider passes retrieve original
ordered encoded bytes from the ledger, with one acquisition and no repeated detail
query. SDK failures refuse without legacy downgrade. Verified requests and generated
assistant drafts precede effects; output entry first records ReconcileRequired.
Only proven no-output cases become Failed. Submitted or ambiguous output remains
ReconcileRequired; no qualified completion, restart binding or automatic effect replay
is claimed. The accepted consumer geometry fix at Rust18e1a741 received independent
Sol acceptance; its earlier full-suite attribution remains unchanged.

The current Reader checkpoint passes 280 host tests across all targets and features,
plus one compile-fail doctest. One additional live test is excluded by the existing
live-run gate. Four actual Orchestrator recording-provider tests exercise exact stored
bytes, storage faults before provider/output, cancellation and output uncertainty,
and unsupported/failed-SDK refusal. Three legacy-ledger tests cover strict records,
retention, write boundaries and fact-only outcome CAS/idempotency. The failed-return
scenario now expects the deliberate unconfirmed-return error instead of claiming
confirmed recovery. This is host evidence; target builds, independent exact-checkpoint
review, representative authorized live-provider validation, qualified native binding,
Writer integration and full REM-37 completion remain open. All broad tasks remain
unchecked.

## October 2 live-provider and target-build evidence

Exact Rust6d3d23c0a3675521f4461b6d3dd39558cff24c8c Windows debug binary
SHA4c40c74060241f1812166ca857079405bdb7a632a364087031cc8aa6ecb6bc47 ran
the maintained live reader.json using the project's existing protected credential
configuration privately through ordinary dotenv loading, without another credential
copy. Two actual provider calls accepted the visible cursive question why flat plate?
and selected the circled abstract at0.5,0.23. Answer text explains the flat plate's
quadrupole/inertia ratio independence from mass distribution and finite-thickness
corrections, consistent with the supplied page. Source unchanged, one navigation,
two text operations/onebody, zero assertion failures/errors. Input and simulated
answer PNG were visually inspected; bitmap typography is approximate.

Maintained live highlight-illegible.json independently made one provider call and
refused the scribbled question: zero navigation/text/body/status strokes, both pages
unchanged, zero assertion failures/errors. This is representative current live-model
integration evidence using simulated pages; it does not prove handwriting generally,
qualified native output, tablet persistence or real page identity.

The exact checkpoint's AArch64 release build passed, artifact SHA
5a67acdc258ee0bbb16bfc51d61183e6e0b9474588ec86acd8de33016d8eb978. The first
concurrent ARM build refused host build-script GLIBC imports from the shared newer
AArch64 cache; that infrastructure failure is retained. The isolated ARM target-cache
build passed, artifact SHA8939329e80b193f3bc5ca0511704ccbd51b738090e417cefe0bb50a524a5b944. Neither compilation nor simulated model evidence completes
native/revisit/Writer/fullREM37 gates. Local raw live reports/logs remain private
working evidence; no credential/document log duplication into source.

## October 7 selected-domain implementation checkpoint

Rust89d619527da40a62866e7f3de090ae0da49c758e includes the schema2
Receipt/OutcomeFact extensions, selected ancestor projection with actual stored
ObjectRefs, historical document ownership, shared Store/aggregate admission gate,
original intent recovery and atomic four-record pending publication. The gate is
mechanical admission, not native qualification. Production SourceAdmission has no
implementer while native qualification remains open. Historical retries recover
original prepared UUIDs, object bytes and logical fingerprint before new IDs;
they never mint a current token or replay an effect. First publication returns the
actual Store token, which must remain exact at every later synchronous handoff.

Independent review found settlement references could name a different admitted
Turn and correction chronology could use an old target ancestor. Repair52bf1a
requires equality to the actual referenced Receipt.admitted_intent, rejects
schema1 receipts, and checks the correction target's typed current head. Nineteen
conversation unit tests and strict library Clippy passed at52bf1a, including an
actual Store pending intent followed by fingerprint, selection, original Root/Turn
reference and legacy-receipt substitutions. Bounded independent reruns are pending.

Historical recovery's foreign selection-pin finding remains OPEN. Partial repair
89d6195 compares group/key/binding/store generation/base/predecessor digest against
the actual original publication. Four focused admission tests and strict library
Clippy passed, including individual foreign pins committed before a lost ack and
Store reopen. Actual predecessor aggregate UUID validation awaits the storage-owned
read-only predecessor lookup; the existing tests do not cover that missing check.
The separate Root-only historical SourceObservation grouping concern was withdrawn
by the reviewer; historical grouping does not require a native source capability.

Retained settlement, durable uncertainty-latch reconstruction, selected Attempt and
every actual backend handoff remain unfinished. Existing legacy Reader behavior and
prior checks retain their original attribution. No full task completion, canonical
sync/archive, merge readiness or native qualification follows from these slices.

Source basis: current repository source and observed local test/Clippy output;
GitHub PR30 review comments4214001560,4214001565,4214048815 and withdrawal4214081221;
parent-routed review coordination. Private synthetic fixtures provide no device
qualification.

Follow-up Rust256a4059e4864ad132839ecd0cfaf45fdbdca830 cleanly merges
published storagebc25322 without hand edits. Its read-only selected_predecessor
returns validated original historic evidence without a token. Domain recovery now
compares the stored pre-publication aggregate UUID with that actual predecessor
and checks predecessor scope/store generation/base agreement. The seven foreign-pin
restart cases, all20 conversation tests, three predecessor storage tests and strict
library Clippy pass. The foreign-pin P2 awaits an independent rerun before closure;
the other two original settlement/chronology reproductions independently passed at
52bf1a. Portable archive code arrives unchanged through the storage merge and
retains the storage owner's separate review and check attribution.

Independent final256a4059 foreign-pin rerun now closed the remaining reported P2:
[exact review comment](https://github.com/s116821/ReMarkableBuddies/pull/30#discussion_r4214231772).
The reviewer reproduced original foreign group and added foreign aggregate refusal,
valid original recovery, missing/corrupt byte refusal, and seven-pin lost-ack/restart/
replacement cases. This supersedes the preceding pending rerun status, without
claiming full REM37/native acceptance. Tests-onlyb51dd7 adds a distinct validTurnB
borrowed ReceiptA settlement rejection; focused conversation tests/Clippy pass.
A full working-tree352 host tests plus1 compilefail doctest passed, but compilation
overlapped that tests-only edit; it is not attributed as exact cleanb51 fullbinary
provenance. Retained settlement/latch/Attempt/backend integration remains open.

Retained source increment [f87859f](https://github.com/s116821/ReMarkableBuddies/commit/f87859ffa925daaa54c1d7e23ac302694f7c7188)
implements the bounded [retained settlement contract](retained-settlement-increment.md).
It appends the original pending fact's causal successor through Store.commit_retained,
preserving active winner content and all previous retained references. New transitions
require a current token; exact historical retries return no live token and append
nothing. Unknown retains uncertainty. Verified terminal states require sealed proof
checked twice and a current Store actor when reconstructed; no production proof
implementer exists. Completed outcome facts are accepted only for explicit schema2
verified-submitted settlement. No storage implementation was edited.

Main's 356 host tests plus1 compilefail doctest passed before an enum-layout-only
boxing change. Final-source all-target/all-feature Clippy with warnings denied and
three focused retained Store tests passed afterward. Those fixtures cover restart/
lost-ack replay, changed requests, winner content preservation, foreign references,
stale tokens, missing/revoked verification and foreign actor refusal, including
negative decoder cases. Verification is synthetic, not native qualification.
[Source and test receipt](https://github.com/s116821/ReMarkableBuddies/pull/30#issuecomment-6052587667).
Independent source review is pending. Selected Attempt, actual backend handoffs and
the remaining feature acceptance gates are still unfinished; no task checkbox or
merge/native acceptance is inferred from this increment.

The independent f87859f review reproduced a valid original closure split across
retained manifests with an ExportAssociation. Settlement unnecessarily recopied
that record into the receipt manifest as Conversation and refused with a namespace
mismatch. Repair [2aae114](https://github.com/s116821/ReMarkableBuddies/commit/2aae1142635c814d8e23e9ec54ba17ac983c01a5)
removes that redundant copy: the validated closure remains in its original retained
manifests, preserving namespaces, media and completeness metadata, while only the
new outcome fact is appended. No storage implementation change was needed.

Main's exact repair passed four retained Store tests, all24 conversation library
tests and all-target/all-feature Clippy with warnings denied; no current-repair
full-suite result is claimed. [Repair receipt](https://github.com/s116821/ReMarkableBuddies/pull/30#issuecomment-6052986365).
The independent reviewer reran four supplied tests and all four original appended
adversarial fixtures: the unchanged split-history reproduction and unsplit control,
shared immutable winner ancestry, six crash/restart boundaries with historical
retry, and nine changed-request mutations all passed. [Original P2 closure](https://github.com/s116821/ReMarkableBuddies/pull/30#discussion_r4215152772)
supersedes the preceding pending source-review status for this bounded increment.
Production verification, selected Attempt/every actual backend handoff, imported
restore and native/full-feature acceptance remain open.
