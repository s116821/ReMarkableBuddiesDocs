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

This change remains active. Current full source CI, independent implementation
and actual consumer compatibility review, own canonical sync/archive and final
paired lifecycle/delivery remain required. Previous archive publicationv0.16.0
is observed separately. No tablet/provider/service/remote-staging action or
memory editor/mutation/setup authority was added.
