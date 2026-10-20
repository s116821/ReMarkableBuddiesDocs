# Prepared memory forget consumer: implementation verification

## Candidate and authority

Accepted precode Docs96c73a9 was independently reviewed in
[5583665573](https://github.com/s116821/ReMarkableBuddiesDocs/pull/69#pullrequestreview-5583665573)
against corrected producer64ff69ba, accepted in5583523433. Implementation started
only after acceptance. This active change remains paired with Manager PR30;
source candidate and hosted/review gates are recorded in the public PR packet.
Main owns all Rust/Store/selected publication and receipt proof. This lane has no
producer source changes. Broad management/native/package/provider gates remain open.

## Implemented boundary

One `MemoryForgetHost` per helper/Electron main owns the slot; synchronous prepare
reservation and irreversible claim precede awaits/I/O. Separate external invalidation
wraps the underlying observer while its internal cancellation remains unchanged.
Private original raw report/input bytes and hashes stay in memory; fixed original
input is reused only for explicit receipt. The public bridges carry strict reduced
projections; no private packet or caller-selected path/operation/heads crosses them.
Async validation rechecks host generation before public output. The shared controller
suppresses late completion, preserves uncertainty and serializes cancellation.

UI explicitly prepares a separately validated fact/target/scope, displays its full
supported Fact and requires confirmation. After confirmation it clears old detail,
shows historical acknowledgement only and never removes search results optimistically.
New reads remain deliberate. Refresh/disconnect preserve unknown state in the live
host; no durable custody is claimed. Same-reference retained acknowledgement recovery
requires no extra CLI invocation. New preparation clears an older terminal reference
before cancellation can use it.

## Local verification

| Check | Result and attribution |
| --- | --- |
| Full Node suite | 166 pass, including20 new feature controls; unchanged prior controls retained |
| Python fixed transport | Seven pass; actual local SSH peer uses deterministic public test identities and synthetic route/report data |
| Workflow graph | All ten existing controls pass unchanged; four feature commands added inside existing Linux/Windows Integration stages, no jobs added |
| Lint/development/production | Pass with Node24.21.0 and existing dependencies, no source release version |
| Browser development | Actual helper session/origin/public/coordinator guards; prepare/confirm/ack-only, private refusal, unknown/reload/receipt, cancel before/after dispatch pass |
| Source Electron | Actual IPC/main-frame/arity/coordinator guards and same UI states pass; lower transport/report methods synthetic |
| Responsive/captures | 390/1280 viewport overflow checks pass; both captures below visually inspected |
| Source preservation | All152 unrelated actual72a171a base entries exact;30 changed/new own paths, no SDK/dependency/release-tool changes |

New controls cover every exact phase row, safe numeric/canonical hash refusal,
malformed public/private fields, shared-session reservation/duplicate claim, ready
expiry, newer slot/epoch and post-parse/post-public-validation invalidation races,
full host restart custody loss and truthful prior uncertainty. Actual Node child
supervision exercises inclusive private/raw caps, malformed UTF8/base64/partial
output, foreign identity, nonzero exit, timeout and cancellation. Subsequent receipt
uses identical original input bytes and never repeats confirmation. Preparation
invalid-input preserves the actual report while mapping to public unavailable;
it cannot leave the shared slot permanently occupied.

Initial TypeScript/test-loading failures and canceled UI attempts are retained in
local execution evidence. Two earlier stale-preview tests paused the wrong crypto
step; fixed fixtures precompute report serialization before intercepting the real
public validation awaits. UI failures exposed old-reference cancellation and an
acknowledgement/cancel race; focused regressions and host/controller fixes passed.
One attempted graph command used a nonexistent Python test directory; the actual
unchanged Node graph suite subsequently passed. Guards were not weakened.

![Synthetic browser preparation](images/browser-prepared.png)
![Synthetic Electron preparation](images/electron-prepared.png)

These captures use synthetic transport/reports and the separately attributed
913-byte existing-library Rust serialization golden. They are not tablet execution.

## Actual producer compatibility

Exact native artifact copied unchanged from
[Buddy60940ac](https://github.com/s116821/ReMarkableBuddies/blob/60940ac577aa25eb11573619e6c8ea7e86d74885/tests/fixtures/prepared-forget-77e92306-corpus.json):
88192 bytes, SHA256 c80dabef103ab0e6844abf5a3228c6e702a52bcfb92654b338a0db524fdf016b.
Original manifest string SHA256
 da10879b89803761e5a1fc693bc21f2b4aa1d81145aa20fbe75a3fddfc40269e.
All39 actual request/stdout pairs verify all78 original hashes, all phase rows,
nine literal Greek previews and all nine exact canonical Envelope hashes. The
capture used disposable Windows host Stores with production bodies promoted
unchanged to77e92306. Capture-time executable digest was not retained; its explicit
null and note remain exact. No retrospective digest is manufactured. The earlier
bfa35-pair mojibake corpus remains separate historical producer evidence.

Every captured report passes the consumer phase parser with exact flags/outcome;
all successful previews pass public reduction without private pins/configuration.
Local and selected original reports also cross the real coordinator/controller.
A synthetic lost confirmation reply remains unknown; exact actual absent receipt
stays unresolved; exact actual later receipt acknowledges the same original
transaction. One confirmation and two byte-identical original-input receipt calls
occur per case. Captured exact replay and later acknowledgement data are equal.
No producer case was rerun to transfer or consume these reports. Atomic local/
selected interleaving and before/after-commit faults remain separate producer tests,
not claims inferred from the raw CLI corpus or synthetic UI/transport faults.

## Remaining gates

Ordinary Linux/Windows retained production package integration, independent paired
implementation review, own canonical sync/archive, final exact-head composition
with qualified producer delivery, final review/current checks, normal merge and
actual main/publication observation remain required. No local package regeneration,
physical USB, tablet contact, provider/account/service or native qualification
follows from these local checks. Whole management/memory/MVP scope stays open.

Source basis: current native source/spec files, original attributed producer
artifact and local test/tool outputs. Coordination selects ownership and sequence;
it is not independent execution proof.
