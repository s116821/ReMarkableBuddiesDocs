# Shared model consumer implementation evidence

Source basis: Manager33 42c9b040f4c82d26b27fd9e88232acd97c7b96be,
including explicit declared-null UI coverage, owned HTTP decode-buffer clearing and
the raw-newline review correction and synchronous DOM-lifetime correction after initialffaecd2; actual base8dfaf8550f64fbf84e474bce9a70ac895306e516; accepted precode
15e34308f77e3c4591d257ea34917b12a2631b6b/review5589113102 and actual
Docscc4cadf03deb285fcbbae43298a7057098f75478. This is an implemented, reviewed and verified consumer archived with its exact
canonical requirements. Final composed review/merge and broad/native qualification
remain separate. The basic
consumer delivery/publication is closed at Manager v0.19.0 and is not replayed.
Model producer actual8c90edab/v0.22.0 is likewise a closed input. No tablet,
provider/credential/trust action or local retained-package rebuild occurred.

## Implementation and private lifetime

The optional protected modelSettings HTTP/main-frame IPC operation, separate strict
private/public model validators, fixed Python selectors and shared explicit editor
are implemented. Reads expose origin/presence only. Keep/replace/remove actions send
only deliberate fields; opaque strings preserve Unicode/CRLF/control/trailing bytes,
without URL/provider interpretation or undisclosed old-string comparison. Rust's
nonblank predicate and scalar/UTF8 bounds are explicit; U+FEFF/U+0085 differ correctly.
The16384request cap belongs only to this new path; existing API/request/wire caps
are unchanged. Safe results reject action/phase/current mismatches, including status
returning ready and model unresolved pretending a current projection exists.

Renderer raw drafts are separate from safe state, cleared before submission's first
await and on editor/local navigation/pagehide (including persisted page transitions),
refresh/disconnect/other maintenance/Stop/expiry/destroy. Paste uses the user event
only, splices raw text through normalized textarea UTF16 offsets, preserves unchanged
CRLF/lone-CR spans on later edits, and refuses ambiguous/oversized/malformed edits.
No app draft persistence/logging/auto-restore/retry or JavaScript zeroization claim.

The host snapshots its own patch, binds canonical changes_sha256 and original file/
path/operation/target, then applies once. Caller mutation cannot replace that patch.
Raw changes/prepare/apply/base64 live only in the bounded Save path; mutable owned
buffers are cleared and references dropped on all terminal/exception paths. Retained
records contain exact original hash-only prepare bytes, original {intent} status
bytes/integrity hashes and safe presence fields, NEVER a retry patch. Status has no
changes field; mismatches stay unresolved/null current and later refusals do not
settle an earlier possibly dispatched Save. Old active references cannot be reused.

All three coordinators use the existing MaintenanceIO, original observer receiver,
explicit pairwise before-I/O invalidation and token-conditional cancellation/release.
Busy runs no hook/cancel/I/O. Remote status invalidates idle ready grants; host-only
snapshots do not. Original120s ready and one13s Save budgets, remaining child/Python
bounds and corrected post-await/Stop generation/reference/original rules are retained.

## Original bytes versus synthetic surrounding phases

Original32Windows reports/60raw stdin+stdout hashes remain byte-identical in the
90529-byte model-settings-c785afe-corpus.json, SHA256
1445676ff01ad2cfebbd94ed6a33845fccf63b5630848419f4fd15584408fcfe.
Capture sourcec785afe044fcd00d386ce9030cb06916245ba2c4/executable
2a624cfd80b87a945e3b0a8a7560100a0d0c92c3d4d62c386959ac57113b8fa6 attribution
is retained; no producer binary was replayed. The independent180canonical/227prefixed
patch reference matches7b8b312e53ce731e251614648218ebf89f994b4d03b047e67278ae0b8ff2c226.
A separate serialization reference confirms maximum valid control text requests:
public Save14139, producer apply14337, private envelope19304bytes, within caps.

All32 original report streams cross the actual strict parser/coordinator/shared
controller, with matching original inspection/prepare linkage as applicable. The
invalid-input original reports are consumed under valid surrounding host requests;
that does not claim the UI can submit their rejected original malformed stdin.
Synthetic surrounding apply-response loss is explicitly labelled for prepared/status
paths needing retained context. Original status-before-apply and status-after-verified
keep those original attributions; no actual induced transport-loss claim follows.
The normal UI can submit a logically unchanged opaque replacement, so the original
no-op crosses normal explicit replacement gestures without dirty-state injection.

## Executed controls and visual inspection

- All226Node tests pass:203baseline plus23model controls. They cover all32 original
  streams, exact finite/private shapes, wrong patch/hash/phase/current/identity,
  Unicode/scalar/byte/whitespace caps, original patch mutation, hash-only status,
  deadlines/ready expiry/late completion, capacity, all3lane ownership and stale Stop.
- Nine Python controls pass, including12actual local SSH selector/exit combinations
  for inspect/prepare/apply/status with exact original stdin/no stdin. Routes,
  notices, identities and report writer are fixtures. Framing/duplicate/UTF8/cap,
  stderr/nonzero/timeout/post-identity, hash-binding/status-no-patch and one-output
  controls pass. This is local SSH evidence, not native Windows/USB qualification.
- Actual child supervision verifies exact private stdin, inclusive24576output cap,
  overcap/identity/nonzero refusal, inherited500ms timeout and invalid-budget no-spawn.
- Both actual protected development browser HTTP and source Electron UI pass exact
  CRLF/non-BMP/trailing paste plus later typing, clear/null/unchanged and saved/runtime
  disclosure, same-ID refresh/other-panel/persisted-pagehide clearing, lost reply/reload
  recovery without automatic status/reapply, pre/post-apply Stop and no input refill.
  Original old forget/receipt bytes and basic/model/forget cancellation/status owners
  survive both guarded paths. Real Electron arity/sender/main-frame guards remain.
- Actual helper additionally rejects wrong origin/session/query/duplicates/UTF8/
  body caps/private extras and final stale public projection; document/resource/iframe
  lifetime and late same-ID reads remain covered. Input/output errors do not echo text.
- Existing basic editor browser/source Electron, exhaustive wired preload inventory
  (new modelSettings included, all old members retained), and development Tailwind/
  focus/startup controls pass. Lint, development/production builds and all10unchanged
  workflow-graph controls pass. Only commands inside existing jobs were added.

The native UI harness imports the test checkout's synthetic lower-report fixture;
actual packaged/source coordinators, HTTP/IPC and public guards remain installed.
Ordinary hosted retained jobs execute the frozen browser/Electron artifacts
without rebuilding; both current OS jobs passed as recorded below. Their fixture additionally checks packaged resources byte-for-byte
and the actual packaged Python refusal entry. No local package was rebuilt.

All four below are actual current source-host390/1280 captures inspected for origin
labels, keep choices, readable controls/disclosures, complete footer and no horizontal
page overflow/private text. They are presentation evidence, not device qualification.

![Browser](images/browser.png)

![Browser390](images/browser-390.png)

![Native Electron](images/electron.png)

![Native Electron390](images/electron-390.png)

## Implementation-review newline correction

Review5589498565 at initialffaecd2 confirmed that collapsed deletion beside equal
displayed newlines could choose the wrong raw CRLF/LF span. Before-fix regressions
reproduce both Root cases. Current1aa4980 anchors backward/forward deletion to the
recorded UTF16 caret and actual removed display span. Unanchored fallback accepts
only identical raw results across all minimal splices, refuses ambiguous/lossy
internal newline reconstruction, and leaves Save disabled on refusal.68independent
mixed CRLF/LF/loneCR/emoji caret cases and ambiguity controls pass. Adjacent loneCR+LF
is correctly treated as one CRLF display break and separately tested; the first
new regression fixture had incorrectly counted that pair as two breaks.

Actual guarded browser and source Electron keyboard controls also verify exact raw
submissions after Delete/Backspace for mixed/reverse/loneCR/non-BMP cases.225Node,
lint and both builds pass after this correction; nine Python and ten workflow graph
controls remain unchanged/passing. Independent source review5589608081 accepted through immutable1aa4980; its original
newline thread is resolved. The later DOM-lifetime successor below requires a fresh
focused review before final delivery. Extra HTTP decode-buffer cleanup clears the owned concatenated byte copy
as well as incoming chunks, without claiming immutable-string erasure or changing
existing guards/caps. The two added public rows also verify explicit declared-null
removal with untouched model omitted through both real guarded hosts.

## Synchronous DOM lifetime successor

After accepted source review5589608081, a new same-event-stack persisted pagehide
assertion reproduced a real lifetime gap on1aa: raw draft/signal clearing preceded
Angular rerender, leaving the old textarea value synchronously observable. The
42c9b04 successor adds an optional synchronous input-clear callback to the shared
controller and empties actual model textareas before publishing/resetting, including
before Save dispatch. Per-field action changes clear only their own field. Existing
central reset paths cover expiry, refresh, disconnect, maintenance, Stop and destroy;
generation guards prevent delayed old completion from clearing a newer editor.

All226Node tests, lint and development/production builds pass. New controller controls
prove clearing occurs before adapter dispatch/first await, per-field isolation and
stale retained completion safety. Actual guarded browser/source Electron checks pass
same-stack persisted pagehide and Read-button clearing; the browser additionally
checks empty values at Save fetch entry. The controller-order control applies to both
adapters; no native IPC interception claim is made. Probe state is reinstalled after
reload; an initial test-probe failure from missing post-reload flags is retained.
Presentation is unchanged and the previously inspected four images remain applicable.

The prior1aa hosted run39473280259 passed Title/Checks/Build but FAILED both Linux
Integration118804133524 and Windows Integration118804133374 at the same immediate
DOM-node-count assertion after Read. The helper wait checked already-visible tablet
state, so it did not establish completion of Angular node removal. The successor
checks actual input emptiness synchronously and uses condition-based toHaveCount(0)
for asynchronous node removal; no sleep, timeout increase or weakened privacy guard.
Full failed logs are retained: Linux76225bytes SHA256
0f971b7ab8288ce8d89d222bd1052096ce22d5bbe24d51128dae2e5b3c5e7a28;
Windows60142bytes SHA256
d592de936d714e1a1050eb9dfeedc761f216b6e2a4fbf6706646f4a4c8c5751c.
These failures are not qualified or blindly rerun. At that checkpoint fresh normal42c9b04 hosted CI and focused immutable review
were still required. Both have since passed as recorded in the final receipt;
actual merge/publication are not asserted by this archive.

## Preserved failures and limitations

Initial corpus test wrongly decoded rejected malformed stdin even when only its
failure report was being consumed; parsing successful original requests only fixed
that fixture, without changing any original byte/hash. Initial model coordinator
used the basic envelope's lexical key order; the separate model key order was fixed.
An old-status fixture accidentally used no-change (and another already retired a
matched diagnostic); distinct unresolved originals corrected those preconditions.
All original failed logs remain in the shared workspace.

The first native UI attempt loaded stale production output after only a development
build; building the current production output resolved the absent-model-panel failure
without increasing waits or changing guards. A declaration typo in the new module's
MODEL_KEYS export was corrected. Test cleanup now releases deferred synthetic gates
and attaches rejection observers so a subsequent browser close cannot mask the
underlying assertion. These are recorded as corrections, not independent passing
runs. Later full controls and current source-host captures pass as above.

## Scope and remaining gates

Source29paths (13existing/16new) preserve196other entries from actual8df base.
Basic/general/forget protocol/coordinator/transport files, original old corpora,
dependency lockfile and tag-only release/version machinery are unchanged. Optional
new model API adds no service, file fallback, provider/prerequisite or SDK behavior.
Docs normally composes delivered actual9fe02eb2458ede5289c747b61cbe076cb01fabb6,
preserving all584actual-main entries including ordinary-export and the seven
newly delivered saved-memory artifacts.
Only this own11file active consumer is added; no speculative producer branch merged.

Current42c9b04 both-OS hosted development/source/retained-package checks PASS.
Independent full source review5589608081 and focused successor review5589943370
accepted the implementation. Own4requirements/11scenarios synchronize exactly into
new canonical saved-model-settings-companion; only this completed change is archived.
Final composed review and current final Docs CI precede normal Docs-first linked
squash; actual-tree/mainCI/tag/provenance observations remain separate. Broader backend,
credential/provider/runtime/native, ordinary data and whole REM42 remain open.

## Requirement and scenario verification map

| Canonical requirement | Scenarios | Evidence |
| --- | --- | --- |
| Explicit origin-only saved model/endpoint editor | Untouched/replacement/null removal; saved versus effective | Protocol original corpus, coordinator and both guarded host UI controls |
| Bounded private text with hash-only reconciliation | Paste/edit/submission lifetime; lost apply/hash-only status; no response echo | Raw newline vectors, synchronous clear-hook/pagehide/Read/dispatch controls, original status packet and child/helper refusal tests |
| One-shot original authority and shared maintenance ownership | Expired/late reply; old cancel/status versus another coordinator; capacity | Coordinator fake clock/deferred gates, controller generation guards, actual both-host three-lane tests |
| Attributed protected-host verification and own lifecycle | Original corpus versus synthetic faults; protected boundary/exact delivery | Original32reports/all60hashes, HTTP/main-frame IPC guards, current hosted checks and separately reviewed canonical archive/delivery receipts |

## Final hosted and lifecycle receipt

Current source run39476665269 passes Title, Checks, Build and both ordinary integrations. Linux118815734431: 91018bytes SHA25628e1546df54d1860b0666ed4b03694cb1ca35643b7624e2013ab3061a68dc881; Windows118815734617: 67481bytes SHA2564b369cc13c1a5a117f6ea9b214190b9540cfc8534f17016fc7597d09cd40aaca. Each full raw log contains all four development/source/retained-browser/packaged-Electron model UI success markers and both before/after package-verification calls. Checks118814337922 is121519bytes SHA256a884ff8b22b2c2f82dbceae9304bf8005ee0cb5d4238791e1aa3e35cdf641f8e, with226Node and ten graph controls passing. Original1aa integration failures remain preserved separately. No local package rebuild/execution or tablet/provider contact.

Canonical requirements match all four archived requirement blocks and eleven scenarios
exactly. All584actual9fe02 entries remain unchanged; only this own archive and new
canonical capability are added. The producer-contract proposal link is mechanically
adjusted for the archive location. The four inspected image blobs remain unchanged.
No prior failed run is relabelled, no producer binary replayed, no native tablet
qualification or whole REM42 completion claimed.
