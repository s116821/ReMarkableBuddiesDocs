# Inspection stdin implementation

Precode86bb4c0 was accepted in full [review5582800963](https://github.com/s116821/ReMarkableBuddiesDocs/pull/66#pullrequestreview-5582800963)
and all three hosted checks39395955684 pass. Its local-versus-selected correction
preceded implementation. Review's subject-nonblank precision and explicit ASCII
whitespace clarification are included in contract.md and the implementation guide;
the operative proposal/design/delta requirements remain unchanged.

Source [Buddy69](https://github.com/s116821/ReMarkableBuddies/pull/69)
4e2f8dec4d5bcb5032bca2ea6953747e61394989 is based on delivered029354f.
Only five paths change: maintenance's private strict Key/scope decoder and
Query/Inspect whitelist plus unit controls, actual CLI fixtures and three guides.
File decoding, query decoder/domain behavior, all core Key/Fact/selected projection,
guards/writer, main routing, storage, archive, Cargo and SDK bodies are unchanged.
All other base entries are preserved; no Reader/model/native code is imported.

Actual local results: six maintenance unit tests pass, including raw duplicate
top/nested keys, global/document/nil/foreign identities, legacy file-global
compatibility, read errors and mutation/setup MustNotRead. The existing real
Store writer test was expanded with three parsed-inspect contexts: stale current
view, forged report and prefix I/O failure; its focused rerun passes. No-default's
six maintenance controls pass with that final eight-context writer fixture, and
strict all-target/all-feature Clippy passes.

The first full19-case actual memory CLI run had18 passes and one negative-fixture
failure: generic commit correctly rejected stale parents while trying to install
a selected conflict. Explicit replacement also correctly refused conflicted
selected membership. A subsequent test-only use of unwrap_err failed compilation
because the publication success type has no Debug; that test expression was fixed
without changing production types. Both failures and the compiler error remain
separate logs, never relabeled as passing evidence.

The final fixture asserts supported storage refuses conflicting membership and
the exact admitted selection/tombstone remains unchanged. It does not force that
invalid state into storage or fabricate an unavailable report. A separate valid
generic opaque commit in another registered aggregate causes actual requested-key
inspection to refuse its whole view, as required. Final focused CLI run passes all
three new cases; the original16 existing CLI cases retain their first-run passing
attribution. No production decoder change followed the initial18-pass result.

Those three final cases cover local values, complete-empty, tombstone, mixed
conflicting heads and opaque raw payload preservation; selected values/empty/
tombstones, publication refusal and unrelated invalid whole-view refusal; exact
file/stdin reports, inclusive1MiB bounds/EOF/invalid UTF8, missing/Busy/invalid
states and no read-created Store. A final corpus records13 actual raw stdout
reports and their exact request bytes with SHA256 manifest, supplied to the
independent consumer owner. It includes the healthy selected report AFTER refused
conflict, not a falsely successful conflict publication. Earlier failed-fixture
captures remain separate. Binary SHA256 is
e6354379733fb7e0954ff458c28ec380232c0360e10965df3f4b76f660eede0b;
tested workingtree source bodies were promoted unchanged to4e2f8dec.

Implementation and consumer compatibility are qualified below. Own canonical
sync/archive is included in this final composition; final paired review, merge
and separate actual-main/publication observations remain delivery gates. Previous archive publicationv0.16.0
is observed separately. No tablet/provider/service/remote-staging action or
memory editor/mutation/setup authority was added.

## Independent implementation and actual consumer evidence

Full independent [source5583148862](https://github.com/s116821/ReMarkableBuddies/pull/69#pullrequestreview-5583148862)
and [Docs5583149844](https://github.com/s116821/ReMarkableBuddiesDocs/pull/66#pullrequestreview-5583149844)
reviews accept4e2f8dec/8b1d441a without blocking findings. Reviewer read all five
source paths, surrounding dispatch/admission/writer paths and six own Docs
artifacts; all375 source and485 Docs unrelated base entries remain exact.

The first corpus handoff failed with Windows cp1252 UnicodeEncodeError, not a test
failure or a successful consumer delivery. Original raw bytes/hashes and failure
output were retained; ASCII-escaped JSON resent the exact13 request/stdout pairs
after verifying every hash, exit0 and complete JSON. No CLI run was repeated for
the resend. Independent review verifies all26 hashes and feeds the exact report
values to immutable Manager1047410 with an explicitly synthetic connection
wrapper: eleven supported pairs retain status/incomplete/head counts, the opaque
local array refuses its whole view, and the actual invalid request refuses before
consumer dispatch. This is actual producer-to-parser compatibility, not actual
SSH/device transport or renderer acceptance.

Current source39398700933 Checks118547803639 passes formatting, strict Clippy,
full all-feature tests and release/tooling controls. The completed Linux log
confirms strict wire/read-error controls and all three new actual inspection CLI
cases pass; prior Windows attribution remains separate. The complete exact-head
run now passes Checks118547803639, Build118551918131 and
application/Integration118556237810. PR Title passes; application/Release is
correctly skipped for a pull request. Current implementation Docs39399049158 passes
all three checks, local Docs12/checker126/strict57 also pass.

One modified canonical requirement is synchronized with the accepted delta;
both unrelated host-memory requirements and the original query-consumer scenario
are preserved. Only this own change can be archived after full qualification.

## Final canonical composition

The own delta is synchronized and this six-artifact change is archived as
2026-10-20-inspect-memory-fact-over-stdin. Canonical host-memory-cli has three
requirements and six scenarios; both unrelated requirements and the original
query-consumer scenario remain unchanged. Source4e2f8dec stays frozen. Final
independent composition review and Docs-first/source-second delivery remain
required; archive completion does not claim actual main or official publication.
