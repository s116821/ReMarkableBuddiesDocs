# Resident write, ordinary close and reopen

This continuation addresses an observed persistence failure, within the existing
REM-25 delivery. It does not close Reader, Writer, reuse or blank-start acceptance.

## Observed failure

The r14-r2 development run `22d74ad778d041c1ac1ff364a2ecdffe` created and selected
`f365ce14-ec00-444b-a810-fc0091cbf86e`, then drew a line. Fresh SDK facts before and
after its live image identified that target in the expected fifteen-page order.
The image SHA-256 was `592d8fe91c42466e112c94df59337211066506267e71ca0f01f8b66c649663a5`.
The saved page remained 424 bytes and its thumbnail 1706 bytes. The subsequent
read-only run `969ce07d585a4218a6248ba6b6867efe` reopened the same native target and
captured the known blank image, SHA-256
`055cf96da4c1b5c4174004eea7069c1a321aab8cfd866aa49b583f128e8fab5e`.
Creation persisted; the line did not. Neither successful input emission nor live
capture is a save receipt.

## Next implementation

Reuse the existing target with a fresh private plan and fresh operation IDs;
do not insert another page or replay the failed write. Bind the exact original
target page and thumbnail bytes to the retained source inventory before contact.
After fresh native target observation, perform the separately consumed own-pen
handoff, unconditional physical release and fresh input readmission.

Integrate the already researched ordinary Reader close through a typed,
development-only SDK request on the existing authenticated parent channel.
It must bind the expected live native page/runtime and original deadline, consume
its operation once, invoke the exact supported own-metaobject close route, and
observe the corresponding closed view. A returned close call, documentClosed
signal, empty loader and changed source bytes are distinct observations; none
alone proves persistence. Preserve unknown/lost outcomes without automatic replay.
The SDK owns its wire/native contract in its own OpenSpec change.

The r15 retry dispatched ordinary close and observed the closed view, but its
pre-close capture was already blank. Its storage deadline expired and the saved
target files stayed equal to the baseline. This establishes neither successful
ink delivery nor failure of ordinary close to save committed ink. Preserve those
facts separately from r14's live-ink/cold-reopen failure.

The known REM-57 sequence has an initial release, hover/down pacing, complete
movement trace and released-state evidence. It does not supply a Qt stroke-commit
acknowledgement. Reuse that measured input policy and record actual before/after
axes rather than inventing a different release ordering. The next experiment
also includes REM-57's same-process fixture reopen immediately after observed
closure, followed by fresh target identity and capture. A file-change wait must
not prevent this known sequence transition. This developer-only fixture route
does not introduce autonomous direct opening into the product or make that
deferred product capability a completion dependency.

After this sequence and verified recovery, reopen again in a fresh Reader
instance through explicit developer setup and obtain fresh SDK identity/order
and pixels. The fresh-instance check excludes retained display/document caches.
Compare all original pages, PDF
redirects, unknown metadata and file bytes. Admit only declared target ink and
thumbnail changes, the target's native modification field and exact document
size/activity accounting. Retain the before/after files and failed outcomes.
Do not replace this observed route with an unexplained debounce or elapsed-time
success condition.

Production profiles remain disabled until their actual integrated acceptance
passes. Development evidence must not be relabeled as a production output lease.

## Testing policy

### Measured continuation: saved ink across a fresh Reader

The r17 development run `0251bb47ba904941ad43f4d4a3fdd456` reused the existing
inserted page `f365ce14-ec00-444b-a810-fc0091cbf86e` at index 9 in the 15-page
disposable PDF. It emitted the exact known stroke, retained a valid independent
raw trace and controller release, captured live ink, dispatched ordinary close,
observed closed, then reopened the fixture in the same Reader. The live and
reopened capture showed the stroke. The native page grew from 424 to 515 bytes,
and its thumbnail from 1706 to 1805 bytes.

Independent ordinary readback `47bcd71557364fdb8bc21108dc780d95` used a fresh
Reader process and SDK before/after target identity. The stroke remained visible:
PNG SHA-256 `38f1cfe69477d50764b44a2d79c5ca626ed2c076ec3d45a5fb958fc851af4de5`,
18580 bytes. All 167 regular source files and 197 non-root inventory entries
matched the saved archive exactly. The normal Reader, sync and Buddy services
were active after recovery. This proves persistence of this measured development
stroke on that page; it does not qualify the full product renderer or Writer.

Retain the write-run preservation failure separately: native `sizeInBytes` grew
234 bytes while archived regular file bytes grew 190 bytes, leaving 44 bytes
unexplained. Only the selected target scene/thumbnail, its `modifed` field and
document size/activity fields changed; the other 163 files were byte exact.
The original failed comparator verdict is preserved. Root verified all current
source files before explicitly restoring the withheld Buddy service. Do not
silently normalize this discrepancy into full preservation qualification.

Simulator calibration must model input delivery, visible ink, ordinary closure,
serialization and reopened pixels as distinct transitions. Retain the earlier
live-ink/lost-on-restart case alongside this positive cold-reopen result. The
complete sequence changed several conditions together, so this evidence does
not isolate which earlier difference caused the lost stroke.

### Actual installed-main development route

The next integration uses the actual Buddy executable and its normal Reader
orchestrator. An explicit feature-gated version-4 development profile pins the
private fixture plan, exact executable arguments, SDK payload and fixed service
files. Existing ordinary profile versions keep their contracts. Each development
installation has a fresh nonce and its own protected activation directory; a
spent activation is retained. This is an experiment route, not production enablement.

The complete native runtime directory, including the session suffix and socket
name, must fit the platform Unix-socket length. Development paths use the short
`/run/rb-dev-NONCE` prefix. Activation and independent recovery must select and
bracket the same profile-derived directory. Checking the ordinary directory
before selecting the development directory is incorrect and can prevent recovery.

Verified artifact pins retain immutable file identity. Reading bytes after a
hash operation must rewind the owned descriptor; EOF is not an artifact mutation.
Configured watchdog duration must be distinguished from the disarmed zero
reported by PID1 while a notify service is inactive.

Temporary installation preserves the exact original fixed files before replacement
and arms a separate bounded installation restore first. Fixture input uses fresh,
named, bounded actions after service startup. Initial Library/NoDocument may leave
the same owned session available for explicit fixture setup and a fresh real
Reader trigger. Developer visual and classification captures remain diagnostic
images and cannot establish page authority or turn unknown pages into non-Buddy.

Native installed-run failures remain acceptance evidence: the first released
corner hold in the r21 run did reach activation, then native startup refused the
overlong socket path. The helper also exposed the incorrect ordinary-directory
lookup. The separate installation restore returned all normal services. These
observations require corrected reruns; compiled source alone does not close them.

The current user instruction supersedes historical review/test prerequisites
between exploratory tablet attempts: compile, run on the authorized tablet,
inspect, correct and retry with fresh actions. Unit tests and lint belong in PR
checks, with only a brief local pass when the change is PR-ready. Preserve exact
artifacts, input isolation, source backups and independent recovery. Feed observed
failures into simulator behavior in the delivery; simulator completeness does
not gate the next native experiment. Final merge and full acceptance remain open.

Source basis: retained native run receipts/images/source archives; the completed
REM-57 ordinary-close, closed-view and combined write/close/reopen sources; and
the current user's tablet-first instruction. No new native save proof is claimed.

Installed actual-main source and successor observations establish additional
simulator cases: the same retained Reader must survive an initial Library/
NoDocument result and accept a distinct released fixture request; the normal
proposal/independent-verification route can then read the saved question and use
supported Next to its immediate successor. A pre-existing legacy answer page is
not an insertion success or newly rendered output. Historical cached header
pixels may differ from the real native capture. An exact, explicitly selected
positive development fixture proof may be used only after existing Ledger
ownership/conflict checks; cached-header failure never proves non-Buddy. Save
claims still require a separate actual reopen and preservation result.

Input-driver readiness must refer to completed current-invocation application
initialization, not merely the service's earlier READY notification. A contact
overlapping startup can be ignored/seeded as initially held; it is not evidence
of an activation failure or authorization to replay its intent. Record a distinct
fresh action after the actual loop is ready. Post-render diagnostic captures
must remain fresh native captures with exact before/after facts; they confer no
target permission and cannot establish persistence by themselves.

The r10 tablet run adds three concrete calibration cases: a provider failure
before output admission, a later distinct trigger closing the stock menu and
therefore failing the exact development source-image proof, and /run exhaustion
preventing daemon-reload during installation restore. PID1 enforces a 16 MiB
reserve. Retained inactive runtime binaries must be archived with verified file
hashes on home and host, then retired only after exact path/incarnation/liveness
checks. The development installation helper now requires 64 MiB available in
/run before replacing installed resources. The independent restore completed;
fresh original-file hashes, all three active normal services and the absent
spent timer were verified. Neither a failed manual reload nor an already-absent
timer is a reason to replay the experiment or restart healthy restored services.

The r11 native-launch attempt observed PID1's original terminal service with an
empty ControlGroup while the pinned original cgroup still reported Populated.
After validating the original unit, policy and retained-or-cleared incarnation,
this is pending teardown under the existing deadline, just like an empty pinned
group awaiting deletion. It must never produce a stopped/recovery receipt or
admit replacement launch. Foreign nonempty group paths, replaced identities and
deadline exhaustion still refuse. The failed attempt and successful installation
restore are retained separately from the corrected rerun.

The r26 actual-main installation r12 completed one development-selected Reader
question/answer path on the tablet: real source acquisition and independent
question verification, supported Next to the immediate legacy answer page,
explicit exact-native-image adoption through the existing Ledger, and guarded
keyboard append. A fresh post-render native capture showed one new `A: 4` block
below all three historical Q/A blocks (PNG SHA-256
`2b4cb2638c6fc1ed48e3a754ec107dfac739a9037960e47b7b7788e556e2366e`).

After explicit developer ordinary UI close and reopen in the same retained
Reader10773, new admitted SourceCapture evidence was committed through the
actual Ledger. The unobstructed readback showed all three original blocks and
the new block (PNG
`e4c5d10c282e63f0d45a25da4d66d8c89ff197e502960541a89818035b4af983`).
The page remained `7f0c3323-1cd9-4d64-8a34-998f5f585ac0`, index9/order10, in
document `32a1c6ca-2821-42f5-9cd3-f082910563bf`. This is same-Reader readback,
not a cold-process claim, and the fixture was manually opened after initial
Library startup; automatic initial source restoration remains unfinished.

The complete saved source archive retained 167 regular files with no additions
or removals. Only the selected target `.rm`, its thumbnail and owning document
content/metadata changed; all 163 other files, including the question `.rm`,
were byte-identical. JSON differences were limited to last-opened fields,
the selected page's existing `modifed` field, document modification time and
size. Page order/IDs and all other JSON fields remained unchanged. Target `.rm`
grew102bytes and its thumbnail6423bytes, matching this document's6525-byte
size accounting change. This does not settle the separate r17 forty-four-byte
accounting discrepancy. Saved source archive SHA-256:
`53c48b790f2a71d2b34b5a6434d6b70eaa8a282002808b094b9eb6985d348630`.

The final capture was persisted before the temporary app's ten-minute lifetime
expired during a provider request. The subsequent live-only archive/input
prechecks refused without a new contact; the historical committed capture was
retained after restoration. Explicit installation rollback restored the original
app/unit hashes, removed temporary fixed files and returned all three normal
services; the spent timer was absent/inactive. The temporary native recovery
helper was interrupted by this explicit rollback and retains failed(signal),
so this run does not claim independent-helper success. Preserve those failed
attempts and the spent write plan. Repeated conversation selection/reuse,
same-activation multiple insertion capacity, new-page creation through actual
main, Writer/blank-start, interruption acceptance, simulator implementation,
real SDK publication/pinning and coordinated final delivery remain open.

The independent cold readback used fresh Reader19565 and the read-only SDK
adapter under candidate 24eaaa829c4b455397928212e7200fd0. After the developer
opened the saved notebook from the Library, native before/after facts matched
the exact target and ten-page order. The 82,382-byte PNG matched the unobstructed
r12 readback byte for byte and showed all four Q/A blocks. The actor verified
source preservation, reaped the Reader and companion, and the recovery helper
restored the three normal services. The setup helper initially lacked the
observed image hash for the after capture and refused before dispatch. The
corrected request used the inspected hash without another tap.

### Automatic end-of-notebook creation and cold readback

The r27 actual app automatically created page
`649dfa6d-ae52-4100-a34c-843b9948e75c` after the only page of disposable
notebook `641d66d8-9cac-4937-a08a-aef9c4f0d10d` and rendered the complete
question and answer on that page. The developer opened the fixture from the
Library and used ordinary Close after the render. The complete saved inventory
had two new target assets and two owning-document metadata changes. The other
170 files and the original question page record were exact. The document size
field increased 3,592 bytes beyond the two new assets, an unresolved accounting
difference. The saved archive SHA-256 is
`95913a26eb7606d9d3cc174b77f656577d10f2a02c22b487addd1beccc2f2f05`.

Read-only candidate `dcca9ee44e5242c3b5c4ea86227bb0c2` started Reader32681,
opened the saved notebook using the Library fixture setup, and captured the
exact target at index 1 of 2. Before and after native page identity and order
matched. The inspected PNG showed the full Q/A block (SHA-256
`0282ed29af91edbf9d451ce292a2eb393c46cb000b2e45bdaec1c731dbea37d4`).
The actor verified source preservation and reaped both children. The recovery
helper restored the three normal services. The scope was one development-selected
notebook, with stock Library fixture setup and one released Buddy request.

### Transient page-number overlay during successor inspection

The r15 actual-main middle-notebook experiment used a two-page disposable
notebook with original ink on both pages. The app captured the first page,
verified the answer and swiped to the exact original successor. The successor
capture included the stock “Page 2 of 2” footer. Its pixels differed from the
settled read-only capture only within the footer bounds (633, 1825) to
(771, 1850) in the 1404 × 1872 PNG. The development fixture's exact-image
classification refused before insertion. Simulator fixtures should model
the footer as a transient effect of an otherwise successful page turn.

The fresh r16 plan used the exact successor image observed during the r15
swipe. The same r27 binary inserted
`3f596052-02c9-4e88-b2cd-0bc474e59b37` between question
`43ea7106-5a9b-4750-b7f9-976b98f2950b` and original successor
`c02f4043-3f7b-44b8-aa56-1ec3ae62b881`. Native post-render facts reported
that exact order and the new page as active. The inspected PNG showed the
complete answer. After developer ordinary Close, the saved archive
`82402d3f69edaeba6c3a28264d62108f5736b352bc19ac4ec5a097ada7da979c`
contained just the two new target assets and two document metadata changes.
All other 179 files, including both original ink files and thumbnails, and
the two original page records were exact. The document size field grew
5,936 bytes while the new assets totalled 14,139 bytes. The accounting
difference remains open.

The restored stock Reader (PID 15677, distinct from the r16 native Reader
PID 14753) opened the notebook on page 2 of 3 and displayed the complete
saved answer. The stock screenshot SHA-256 is
`df96eb995e00caf54b4e3bb6832405dc376464ad47ba9cffc703d5f848287858`.
That screenshot corroborates the saved output. The earlier native capture
and saved page inventory establish target identity and order. All three
normal services were active after the fixture was closed.

### Actual-main insertion in an annotated PDF

The stock “Duplicate with edits” action created an isolated five-page PDF
copy with unchanged PDF bytes and redirect values. The developer added the
boxed question in the blank area on page 4. The r17 run verified the question
and retained the exact native source capture. The first r18 request returned
no clear selection and stopped before output. The next request verified the
question and reached the original page 5, supplying its fresh native capture
with the transient page-number footer. These discovery runs had no insertion
authority.

The r27 actual app, under fresh plan `0b26cf17-863d-454c-9e74-7f8cfa092fcc`,
inserted `37000d25-aeba-4d9a-a2ea-957d45c54293` after source
`0d1bdc61-bc1d-46f0-924f-68118f94553f` and before original successor
`a1969e24-b5bc-4ec9-80b1-776a3dca9d75`. Native facts confirmed the complete
order and active target. Ordinary Close persisted the note page with no PDF
redirect. The resulting archive SHA-256 is
`0585a49b2490bed1543081866f2191297b901ce715696141e723f991ecb324bd`.
The original PDF, all five original page records and redirects, all original
ink and thumbnails, and all other 194 regular files were byte-identical.
Only the two target assets and the owning content and metadata files changed.
Content fields changed were page count, page table and size. The page table
changed only its list and last-opened pointer. The size field grew 36,350
bytes against 14,141 bytes of target assets.

The restored stock Reader opened the saved answer on page 5 of 6. The
inspected stock PNG showed the complete question and answer
(`25810852c838342192e0aaabe340adf96fe3d0948049b00f93e777504941925f`).
The screenshot corroborates persistence. The native render facts and
saved inventory establish exact page identity and order.

The r27 actual app also exercised creation at the end of the same copied PDF.
After fixture setup, the last original PDF page contained its own boxed
question. The r20 discovery request retained the exact source PNG. Under fresh
r21 plan `fd69230a-5ddf-4ba1-864e-77980bf7daa5`, Buddy created
`af77d017-6e6f-4427-b8fd-9545b08a3648` after the final source
`a1969e24-b5bc-4ec9-80b1-776a3dca9d75`. Native facts reported the new active
target at index 6 with the six original pages in order. Ordinary Close saved
the two new target assets. All 197 other files outside the owning content and
metadata files, including the PDF and earlier answer, were exact. All existing
page records and redirects were identical. The new page has no PDF redirect.
The reported size grew 16,805 bytes against 14,093 bytes of new assets.
Saved archive SHA-256 is
`ebb348a7ec8752d3c4de17310d9ce1b5c8e2713fee5a31f5e7c71a8b846b5df0`.
A fresh stock Reader displayed the saved answer on page 7 of 7
(`cdbba431b1ed4ce543609a486820cc0fa2c7ae2644eafd7ceba9d6ea8b48c708`).

### Two requests in one Reader activation

The optional development plan can carry a second request nonce for the same
already-bound current or adjacent page. Both requests must resolve the
original document, order and exact existing target through the Ledger and
fresh native observations. Each nonce has its own durable claim. The
second claim requires a completed post-render capture and the same Reader
runtime and binding revision. This fixture exercises reuse only. Repeated
native insertion capacity remains a separate hardware case.

The r28 ARM app ran two fresh Reader requests in r22 under the distinct
claims `3d3fe1a9-0d6a-4a45-ae1e-73a48b62b4cb` and
`3bd5aff9-7eea-4297-bf91-8529be23cd66`. Both retained Reader PID 2869
with start ticks 231019351 and the same activation, target and ordered page
IDs. Two new exchanges were added to conversation
`1dfceb0c-6122-4009-888b-f812b8590256`. The original binding revision
`b2cad6ce-8ba6-425f-91be-2fdc701b1a06` was byte-identical. The
assistant turns remained reconcile-required in the Ledger.

After ordinary Close, all 197 other files and the question page record
were unchanged. Only the target ink file and thumbnail and owning content
and metadata changed. The source archive SHA-256 is
`46d9aa6cce4752fae01f03c726f73f50b47e38dafa409a4d3eb88f790232d947`.
A fresh stock Reader displayed all three saved answer blocks on page 2 of
2 (`42e2ab58f9ecc036fb6807e28dda59144938b1a0922256f095ed22bc655ec66b`).
The third block's start delimiter rendered bold and persisted that way.
The size field increased 6,132 bytes against 13,309 bytes of asset growth.

### Two distinct native insertions in one Reader activation

The r29 actual app under the r23 development plan created two answer pages
across two disposable notebooks in Reader PID 7389, start ticks 231128794,
activation `c0b5d67a-9d09-44e2-ad84-8d1923cbd41e`. The two separate request
claims were `56421613-f31b-4eec-826a-f2f13a9a6c7e` and
`ca709d25-4035-4329-b352-0fce0c7c2482`. The SDK reported executor reclamation
after each insertion. The developer switched notebooks through the stock
Library. A Library capture hold briefly entered selection mode on a tile.
Cancel cleared the selection before the second notebook opened.

The native captures identified targets `cff16965-bc40-470c-a125-f2597f4dbce9`
and `ebcf7b83-f011-4bfd-a3b2-1bc5004b1fe6` and the exact two-page and four-page
orders. Both answers rendered with identical PNG bytes. The native facts and
on-disk order establish distinct targets. After ordinary Close in each
notebook, the saved archive contained four new target assets, four owning
content and metadata changes, and 202 byte-identical files. All four original
page records were exact. The saved archive SHA-256 is
`ab3e2e04676f49855553ea9cbfa0fd7ec0c0336e3b0a3c018e22407411607591`.
Fresh stock Reader PID 8961 reopened both saved answers. The stock screenshots
showed the answer on page 2 of 2 and page 4 of 4. The run exercised normal
completion under the bounded development profile. Interrupted retirement,
last-owner release, and production admission remain separate.

### Blank-start creation with zero conversation turns

The r30 actual app ran the r25 explicitly selected blank-start request on
the single open blank page of Notebook 4. The r24 discovery request recorded
the exact live source PNG, including the stock toolbar menu. That request had
no accepted fixture proof and left an unbound empty test conversation.

With the fresh r25 plan and source proof, the app created adjacent page
`998ef3e0-5aab-4216-8957-38ec2759e734` and bound it to
`b5c195fd-e215-4bbf-b213-781f2d86e5ef`. The active target showed the existing
heading and empty text caret. The app invocation contained no provider
request. The saved Ledger contained the exact binding and zero turns.
Ordinary Close saved the new page while the original blank page and its
metadata remained exact. A fresh stock Reader showed the heading and empty
body on page 2 of 2. Saved archive SHA-256
`c23f32111abb1520ebe1ecb67828e91884adf1441dde82a296d2bf187f56045f`.
Stock reopen PNG SHA-256
`7a5d5b67bf08ad6c7a4d8bbc89020bd9fd884039bb9e17976bb9301f758676e6`.
The remaining work includes existing-bound blank-start reuse and the
ordinary gesture and unified layout integration.

### Writer refinement reused the bound answer page

The r31 app ran the r26 development-selected refinement on the original
question page of Notebook. The request selected a draft seeded from an
explicit transcript of the disposable question. The Writer Ledger recorded
the correction against the selected draft and a fresh generated draft in the
same conversation. The existing binding revision
`b2cad6ce-8ba6-425f-91be-2fdc701b1a06` stayed current.

The native render identified target `649dfa6d-ae52-4100-a34c-843b9948e75c`
in the original two-page order and displayed the refinement below all three
Reader answer blocks. After ordinary Close and service restoration, stock
Reader reopened page 2 of 2 and displayed the same content. The question
record and its saved bytes were exact. The target ink/text file, target
thumbnail, and owning content and metadata were the only four files changed.
There were 213 byte-identical files and no added or removed paths.

- Native render PNG SHA-256 `b42bcb33333b284024a852fc8c9cdbb832c15c4abe13cc8662bc66b5c1cceef4`
- Stock reopen PNG SHA-256 `f52cdcee424347fb4cf136452e402ca1ead03a78b1335e620b3f0421ac79a1ab`
- Saved archive SHA-256 `a330b46704e1f65fcf5d622058f00c7921982052e9513b9e2a51c99e9c35f8f0`
- Writer Ledger archive SHA-256 `3446c0ff4d4c2a98b00737e0c28fa2814c16ed6f33669721592d7fe043337822`

The simulator needs to distinguish the live render, ordinary Close, and
reopen from persisted storage. This save increased the target asset sizes by
1,240 bytes in total while the document size field increased by 7,245 bytes.
Preserve this discrepancy in the recorded evidence and use saved page data
and identity to check persistence. The live app reported submission with
persistence unverified. Writer creation, production request selection and
automatic persistence settlement remain open.

### Blank-start reuse without a write

The r31 app ran the fresh r27 development-selected blank start from Notebook
4's original blank page. It navigated to bound page
`998ef3e0-5aab-4216-8957-38ec2759e734` in the original two-page order and
returned reuse without a write. No model or renderer was dispatched. The
native capture displayed the empty body on page 2 of 2. The binding revision
`aa57f186-8455-4fe8-91bf-1db905682440` and zero-turn Ledger were unchanged.

After ordinary Close, both saved page records and all page assets were
byte-identical. The content file changed only its `cPages.lastOpened.timestamp`,
and metadata changed only `lastOpened` and `lastModified`. A simulator should
model those navigation and close timestamps independently of page writes.

- Native observed PNG SHA-256 `9867964dd73f6ada26f67f9b88e29ce32f4855bae976beb7c29f780e4789dbbd`
- Saved archive SHA-256 `4fa498a8c2943a277a12c4739469a28fc479a7cffb18f690dacacf977e8d07a5`

### Writer refinement created an adjacent bound page

The r31 app ran the r28 refinement on the single inked page of Notebook 5.
The developer seeded a new unbound conversation and generated a prior draft
from an explicit transcription of the fixture. The actual tablet request
generated a fresh correction, allocated page
`570fe981-2fdc-4f06-bed2-f1368fa4f86d`, and used the same conversation
`d8313b9c-3c0d-4c32-bb4f-c69957d8035a` for the new binding.

The only new paths were the target page file and thumbnail. The owning
content and metadata changed, with 220 other files byte-identical. The
source record and handwritten page bytes were preserved. After ordinary
Close and service restoration, fresh stock Reader displayed the refined
note on page 2 of 2. This uses the fixture heading and an explicit
development request. Ordinary Writer routing and automatic persistence
settlement remain open.

- Native render PNG SHA-256 `ca740b3e4550c5bddc29307ca6d06df903cf83a731d7d1465a179a5a38295ee6`
- Stock reopen PNG SHA-256 `dc14513888efe4ef0e52c1ef17c2533687a67e66d9eba10f89b9d8dacce15214`
- Saved archive SHA-256 `023b0247d9a7fb694cbe2273f57a2e4aebc3424c64c873200db7c25dd3d859b3`
- Ledger archive SHA-256 `e1d7ddfb29bdc07e03d6776c61a3da159511e929426244bb30f6f8ad435ddb15`

### Explicit startup activation and first-gesture placement

The r32 app activated the retained Reader at startup under the pinned r29
development plan. Activation finished about 36 seconds after app startup.
The operator observed the stock Library without a setup hold, opened Notebook
5 and returned to the handwritten question. The first released Reader request
captured and verified that source and appended an answer to the Writer page.
A second distinct request appended another answer through the same Reader PID
28553, start ticks 231413282 and native activation. Both captures identified
the original order and target `570fe981-2fdc-4f06-bed2-f1368fa4f86d`.

The Ledger preserved binding revision `b5730d3d-3dc3-4e14-ae95-ec42bc95d919`
and recorded two distinct Reader exchanges in the original Writer
conversation. Both app outcomes stayed reconcile-required. Stock reopen
after Close and rollback showed the prior Writer note and both answers on
page 2 of 2. The source record and bytes remained exact. Only the target
page file and thumbnail and owning content and metadata changed.

- Exact app SHA-256 `32f29f138824fe245c5758d495e886d1a4d68d87e47510ea68a034b94222129f`
- First and second native render PNG SHA-256 `a65d619b25b50769e3a1f8e9108622d9596addfe46b15c92c6ce2f33272f4db5` and `a878e636e480cda175f054e1c86fc5006ad9198698a54a1290e102bd0db1e9ce`
- Stock reopen PNG SHA-256 `deac735621b9aa5373bf7066d88714843cdbaf4764c19348fabccac37c022314`
- Saved archive SHA-256 `98984358d6db12b2859b2f042f484a331b14aa6d82ee0208704f8bab031c6a09`

The stock framebuffer helper initially looked only for a process named
`xochitl` and refused because the verified runtime executable is staged as
`reader`. The second operator capture scoped process lookup to the exact
owned executable and start ticks. Those pixels were used for fixture setup.
SDK facts supplied placement identity. Normal stock services were restored.

### Plain notebook recognition without preselected PNGs

The r33 app ran the r30 plan with no expected PNG digests. The plan scoped
the development run to the two-page Notebook 6 and selected the plain
notebook recognizer. Both original pages contained ink. The app accepted
their saved RMv6 scene structure, zero native text counts, live clear
heading area and current binding inspection. It navigated back to the
original source and inserted `4dcc51e8-2c65-49cb-8ebf-ab7f2cedef68`
between `080ae38b-457b-40dd-a913-96f73240fec2` and
`e28f5a63-ee5f-44b3-8b33-306f1b639dc6`.

Stock Reader reopened the saved answer on page 2 of 3. The two original
records, ink and thumbnails remained exact. Only the target page file and
thumbnail were added. Only the owning content and metadata changed, with
229 other files byte-identical. The Ledger showed one binding and one
exchange. The app recorded the answer as reconcile-required.

- Exact app SHA-256 `b560368bea5b3eb11c51a4e099a8655a774bb9fa6923738610f00fe4e6dd2a47`
- Native render PNG SHA-256 `1e410c7b3b95401014c5ac1514d67ac091561fbf9184402b48cac7b6adbaf787`
- Stock reopen PNG SHA-256 `5fe4c2c20b1f6953a3412bd572a20e86b0a71a724126e6436f4bd7ddb679faf6`
- Saved archive SHA-256 `9fd320423fb1d3a9c37a0b9c15022989bedc8b079e580b44a8733cc8803f4ecb`

This qualifies the observed plain, best-fit portrait notebook case under
the explicit development profile. PDF classification, legacy adoption,
other viewports, and the normal installed route remain separate.

### Original PDF recognition without preselected PNGs

The r34 app ran the r31 plan with no expected PNG digests against a stock
original-only duplicate of the four-page PDF. The original redirect at
index 2 had a saved ink question. The original redirect at index 3 had no
annotation file. Both received fresh SDK identity and capture checks and
qualified through their original PDF redirects. The answer rendered on
new native note `86cf5611-ad17-4aa7-9e47-3fd8b7865be9` between those
two original pages. The note has no PDF redirect.

Stock Reader reopened the answer on page 4 of 5 after ordinary Close and
service restoration. The original PDF, four page records, redirects, and
saved ink were byte-identical. There were two new target assets and only
two owning metadata changes. The other 240 files were exact. Ledger had
one binding and one exchange with a reconcile-required answer.

- Exact app SHA-256 `cd28b510c0a1ae59bdaba96ecc9211ce752a74f5aace053a6821136f519282e1`
- Original PDF SHA-256 `332446943966f6c3111a09c2df05673a94282ea247bf78c946f2c6e6d479e1f6`
- Native render PNG SHA-256 `3b570389753b548466325e6d39847cda633d116c6f3c1387325bd0a300d055f8`
- Stock reopen PNG SHA-256 `99bc61154ec1747ee6bcf71a45104cb3c9c1de64d76de9a3435f225a972728c6`
- Saved archive SHA-256 `be7da4faf1810935c419f113b11eba1234aae598c7027eeb4bddbab466a8b347`

The explicit development plan still selected the document and request.
The route is qualified here for the observed RM2 portrait best-fit
original PDF pages. Ordinary installed routing remains separate.

### Unbound PDF note refusal and source restoration

Stock Duplicate With Edits created a fresh PDF document with the previous
ink and answer note. The copied note had no matching Ledger binding.
The r35 app ran r32 from the annotated original source
`2342db2b-4603-403a-8936-d364545643b3`. It captured the immediate
unbound note `a885a166-3590-4d02-ab6d-0c81defe0190`, checked that
neighbor again, moved Previous once and verified the original source.
The restored screen showed the original question and the iteration refused
placement.

All five page IDs, records, PDF redirects and page assets remained exact.
No files were added or removed. Only the owning open-page register,
last-opened index, and open/modified clocks changed. The durable native
insertion journal was byte-identical. This verifies one pre-insertion
refusal and source return. Interruption during navigation or after native
dispatch still needs its own hardware evidence.

- Exact app SHA-256 `0eaefa9d1c00cd7f2e0a6a66fe781712c2baff457cf6c21073184c4eaabc0993`
- Inspected successor PNG SHA-256 `011c6e3f5734fd07e671a4fe54667be57341b662842bb505fe950f026868e39e`
- Restored source screen SHA-256 `4a9688b43d4dec32fe55f26a3bbc8370fb1e55ec2c9b9259abd76d81a6f76074`
- Saved archive SHA-256 `60168a01be142b2000212d3778c3d309f24f5f980f43a6f245f9c208bd4548e0`
- Unchanged insertion journal SHA-256 `d6d988a913f5a055398b1c79d0fd425778bd52d5b1fe676a36e49c4bcee92592`

### Reader creation and reuse through the installed service command

The r36/r33 candidate used an explicitly pinned version 5 recovery profile.
The live Buddy process command contained only the installed binary and
the fixture plan file was absent. After startup activation, the operator
opened a disposable PDF's last original page and sent a released Reader
gesture. The app recognized the native page and inserted
`9533667e-fb9c-417d-a44b-44a32ae76220`. A second distinct release from
the same source reused the same target and Reader PID 13268 with start
ticks 231700192.

The Ledger saved two exchanges and one installed binding. The native
insertion journal gained exactly one reservation with a historical reply.
After ordinary Close, the Buddy service was stopped and the installed
helper restored stock Reader and sync. The helper exited successfully.
It retained the activation record for evidence. The experiment separately
restored the original Buddy package and archived the inactive runtime.

Fresh stock Reader reopened both answers on page 6 of 6. The original PDF,
five prior page records, redirects, and assets were exact. The new note
and thumbnail were the only additions and the owning content and metadata
were the only changes. Both app answer outcomes stayed reconcile-required.
The second opening delimiter rendered bold in the current stock layout.

- Exact app SHA-256 `e4ad7d5597c476b1a67f752470fe6a1261fa6ff633c473c3aa2b246a1546eca4`
- Stock reopen PNG SHA-256 `a970ca5b17771015d51d7b5cd52391394d93ef2900f08dd171f9fa5463124dbb`
- Saved archive SHA-256 `470761e9c626133f09521b8df8368dc7478a043babc850689b025d3cb779b125`
- Native insertion journal SHA-256 `5466258f41f528527f5bbf38e525684357c012105c7e05623c716fc1d606eec6`

This exercised the installed Reader command with a temporary qualified
candidate and the current development-gated build. Package delivery,
startup after recovery, and post-dispatch interruption remain open.
