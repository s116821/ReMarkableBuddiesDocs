# Prepared forget implementation evidence - active work

Full corrected [producer review5583523433](https://github.com/s116821/ReMarkableBuddiesDocs/pull/68#pullrequestreview-5583523433)
and exact [consumer agreement6288406539](https://github.com/s116821/ReMarkableBuddiesDocs/pull/68#issuecomment-6288406539)
were read before implementation. Consumer's independent host/UI precode and its
bounded live-host custody/restart limit remain separately owned. No durable
journal or private SelectionToken API is added by the producer.

Source work is on the existing checkout's published feature/rem-24-prepared-forget,
based on actual4fad1681. Current source candidate is
60940ac577aa25eb11573619e6c8ea7e86d74885 in
[Buddy70](https://github.com/s116821/ReMarkableBuddies/pull/70); all372 unrelated
actual4fad entries remain exact. This is implementation, not final acceptance. It adds strict conditional evidence,
separate prepare/confirm/receipt paths, guarded local/selected preview and output,
pure local receipt lookup and a narrow conditional Store publication. The existing
publish body is factored into an already-locked helper so new generation/head/
content checks and first publication use ONE mutex guard. Legacy file routing and
its admission/order/duplicate-wake behavior are preserved.

Initial actual three CLI cases passed: local/selected original acknowledgement
after later values without re-deletion, exact replay, tampered original content/
pins, original mode re-entry/config drift and bounds/no initialization. The initial candidate five-case
actual CLI capture passes all five, adding actual valid selected/catalog acceptance
replacement with identical heads plus non-confirmable/Busy cases. The replacement
fixtures establish the new states still admit ordinary domain inspection before
asserting original-intent refusal; they do not manufacture invalid membership.

Six new focused controls pass, plus one existing conversation test selected by
the name filter. They exercise actual ordinary restore retaining identical heads
and unchanged mode token, original-generation refusal, Store mutex held through
the consuming writer, before/after commit uncertainty and pure content-bound
receipts, and both local/selected stale/forged/prefix preview and post-commit prefix
failure without a second report. Initial unit compilation failed only because
assert_eq required Envelope Debug; assertions were corrected without changing
production Envelope types. The first library compile also needed the Context
import and a serde skip for private pending state. Those failures are not passing
evidence.

Initial bfa candidate strict all-target/all-feature Clippy passes. Default memory10
and storage88 pass, covering the factored legacy publish body and existing selected
history/media/fault/mode controls. Independent no-default memory10 and conditional
storage3 also pass. New strict-wire fixture compilation initially hit a test-only
mutable/immutable JSON borrow; cloning the fixture value before mutation corrected
it. Original failed log is retained. No production type/guard was weakened to fix
fixture errors. Ordinary current hosted source39407517919 is still a separate gate.

The final actual CLI corpus contains35 raw stdout/request pairs, with all70 SHA256
values verified before complete ASCII-escaped transfer to the independent consumer.
Binary SHA256904da10a40beb732f8a63b4fb529248d4a1e4a7e15b0bb10687ec2ff65dbbd2e;
tested workingtree production bodies were promoted unchanged to bfa8a131. That is
not an official build metadata or device qualification claim. Exact raw strings
and manifest are retained, with no report reserialization or test replay for the
handoff. Actual consumer compatibility remains independently pending. Before/after
commit/prefix uncertainty evidence is from actual domain/consuming-writer controls,
not falsely labeled as CLI fault injection.

Current Docs composition includes actual consumer inspection8503aad from main;
its canonical requirements/archive remain untouched. This own change stays active
and canonical prepared-forget requirements are not synced or archived prematurely.
Implementation review, actual attributed producer/consumer corpus compatibility,
final current-head CI, own canonical sync/archive, final review, paired delivery
and actual main/publication remain gates. No tablet/provider/service/model/native
execution occurred.

## Corrected successor and separate UTF8 corpus

The corrected-UTF8 candidate was77e92306091d3d0bf10cd8443d9327198a8105b4, superseding bfa8a131
for final implementation review. Review found the two original Greek literals in
existing CLI fixtures had been unintentionally mojibaked by Windows default text
decoding in edit helpers. An audit found one original en-dash guide line as well.
All three are verified byte-exact against base4fad UTF8 Git blobs; the new fixture
uses an explicit Rust Unicode escape. A corrective attempt also exposed CR/CRLF
conversion and failed compilation; that failed log remains separate. Edits now
use explicit UTF8/LF. No production guard/type was weakened.

A separate source self-review found ordinary import can retain distinct accepted
manifest UUIDs for the identical original tombstone. The new pure receipt path
now requires one uniquely matching manifest, refusing ambiguity without mutation.
Four current conditional-storage controls pass, including actual duplicate import,
no arbitrary receipt selection and no republication. Legacy Store/file replay is
unchanged. The restored original Unicode query case passes. Current strict
all-target/all-feature Clippy and independent no-default memory10/conditional4
pass; the original default storage88 result remains attributed to the preceding
unchanged legacy-publish body rather than being replayed or relabeled.

All six current actual CLI cases pass in a NEW corrected-utf8 capture directory,
with39 exact raw stdout/request pairs and all78 SHA256 values verified. Actual
U+03B1/U+03B2 in stdout were checked. Original bfa35-case capture and its904da10a
binary digest remain unchanged historical evidence, not edited or relabeled.
Corrected capture production bodies were promoted unchanged to77e92306; its
executable hash was not retained before a subsequent metadata rebuild replaced
that file, so no retrospective binary digest is asserted. Exact raw bytes/hashes
and source-body attribution are verified independently of build qualification.
The complete ASCII-safe corrected corpus was supplied to the consumer; its actual
parser/host acceptance remains separately required.

Current sourceCI39408551182 targets77e92306. Cancellation of superseded bfa run
39407517919 was requested to release runner capacity; its final state is recorded
separately and never counted as current success. Current hosted checks,
implementation review, consumer compatibility, canonical sync/archive and final
paired delivery remain gates. This own change remains active.

## Fresh handoff and accessible native corpus

Source60940ac5 explicitly rechecks the exact original receipt/direct predecessor/
parent-content proof against the fresh selected target and requires the same
transaction before sealing stdout. The operation and fresh read have no retained
selected gate between them. A focused real target-activation interleaving passes:
the accepted base/generation changes while the exact historical operation remains
provable through fresh validated lineage, without a current-deleted claim.

The inline corrected-corpus transfer was truncated at the receiver; sender-side
complete JSON/hash verification alone did not establish consumer receipt. Without
replaying any cases, the exact corrected39 pairs and original manifest were added
as a reusable native [fixture](https://github.com/s116821/ReMarkableBuddies/blob/60940ac577aa25eb11573619e6c8ea7e86d74885/tests/fixtures/prepared-forget-77e92306-corpus.json).
It is88192 bytes, SHA256c80dabef103ab0e6844abf5a3228c6e702a52bcfb92654b338a0db524fdf016b;
embedded original manifest SHA256da10879b89803761e5a1fc693bc21f2b4aa1d81145aa20fbe75a3fddfc40269e.
All content is synthetic; private-path/secret-sentinel audit passed. Exact original
request/stdout strings and all78 per-file hashes remain intact, as does the missing
capture-time executable hash limitation. A native recorded-fixture verifier passes
all hashes,39 pairs,nine original Greek previews and stable logical acknowledgement
UUIDs without running any CLI cases. Receiver acceptance remains independent.

The delta now explicitly modifies the pre-existing query/inspect-only whitelist
while preserving all four old scenarios byte-for-byte, alongside the added five
prepared-forget scenarios. Both unrelated canonical requirements remain untouched;
canonical sync/archive still waits for complete qualification.

## Current focused qualification at60940ac5

Fresh selected handoff interleaving1, recorded-corpus integrity1 and affected
actual selected CLI1 pass. Current strict all-target/all-feature Clippy passes;
independent no-default memory11 and conditional storage4 pass, including the new
fresh-lineage proof. Existing corrected six-case capture remains pinned to77e92306,
not relabeled as a new run. No CLI cases were replayed merely to publish artifacts.
Current sourceCI39410088631 targets60940ac5. Superseded77e run39408551182 is confirmed
CANCELLED, separate from earlier bfa cancellation and never counted as passing.
Current full hosted checks, receiver compatibility and final lifecycle remain gates.
