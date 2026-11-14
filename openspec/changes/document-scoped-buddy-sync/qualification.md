# Selected storage qualification

These checks use disposable host stores and real test binaries. They do not use a
tablet, provider credentials, native documents or a paid model. They qualify Store
generation refusal and recovery only. Main's strict domain decoder, admission guard,
historical settlement, live provider exclusivity/application visibility and portable
restore remain separate unfinished gates. Do not archive this change from these results.

## Retained publication and activation

From the Rust checkout, run:

```sh
cargo test --locked --all-features retained -- --nocapture
cargo test --locked --all-features process_death_at_activation_boundary
cargo test --locked --all-features selected_snapshot_preserves_exact_noncanonical
cargo fmt --all -- --check
cargo clippy --locked --all-targets --all-features -- -D warnings
```

The retained subprocess test exits without Store/Fixture destructors immediately
before or after publication, then reopens and checks original intent/media,
unchanged winner references/base, accepted receipt membership, replay and unrelated
scope preservation. Its parent kills/reaps a child that exceeds a 15-second bound.
The barrier race admits exactly one retained publication or replacement from one
captured token. It does not model Main's domain guard or native completion semantics.
Each accepted publication has a new manifest transaction identity; compare winner
references/namespace/media coverage rather than requiring the old manifest identity.

The snapshot regression stores noncanonical JSON bytes and reverses causal order.
After reopen, `selected_records` remains in the order of
`transaction.selected.records`; each corresponding ObjectRef reads the original
bytes. Pair these Store-validated references with parsed envelopes for exact domain
ancestor lookup. Reserializing an envelope may change hash/length and cannot recover
the original selected object identity. This storage guarantee does not validate
Main's domain projector; its own real-Store regressions are still required.

## Unchanged older reader

The tested older source is Buddy `7d1403cacc5fafe3a7ddc9a441a8b9200224e7ac`.
It has the existing format1-only Store open check and `process_lease_child` test.
Do not patch that older reader or substitute a reimplemented decoder. The tested
compiler was Rust1.98.1. Use the same compiler for both builds. Offline builds
require dependencies already present in the local Cargo cache.

From the Rust checkout, create a disposable detached worktree and build both
unchanged test executables. Keep the JSON compiler output so executable paths are
discovered rather than guessing Cargo's platform-specific suffixes:

```sh
READER_PROOF=$(mktemp -d)
git worktree add --detach "$READER_PROOF/old" 7d1403cacc5fafe3a7ddc9a441a8b9200224e7ac
cargo +1.98.1 test --locked --offline --all-features --lib --no-run --message-format=json > "$READER_PROOF/current.jsonl"
CARGO_TARGET_DIR="$READER_PROOF/old-target" cargo +1.98.1 test --manifest-path "$READER_PROOF/old/Cargo.toml" --locked --offline --all-features --test storage --no-run --message-format=json > "$READER_PROOF/old.jsonl"
python3 - "$READER_PROOF/old.jsonl" "$READER_PROOF/current.jsonl" <<'PY'
import json, os, pathlib, subprocess, sys, tempfile, time

def executable(path, name):
    artifacts = [json.loads(line) for line in pathlib.Path(path).read_text().splitlines()
                 if line.startswith('{')]
    matches = {a['executable'] for a in artifacts
               if a.get('reason') == 'compiler-artifact'
               and a.get('target', {}).get('name') == name
               and a.get('profile', {}).get('test') and a.get('executable')}
    assert len(matches) == 1, matches
    return matches.pop()

old = executable(sys.argv[1], 'storage')
current = executable(sys.argv[2], 'remarkable_reader_buddy')
qualifier = 'storage::selection::publication_tests::selected_reader_qualification_fixture'
environment = dict(os.environ)
for key in ('BUDDY_CRASH_FIXTURE', 'BUDDY_LOCK_FIXTURE', 'BUDDY_SELECTED_READER_QUALIFICATION'):
    environment.pop(key, None)

def run(binary, test, key, root):
    subprocess.run([binary, '--exact', test], check=True, timeout=30,
                   env={**environment, key: str(root)})

def version(root):
    headers = list((root / 'data' / 'generations').glob('*/format.json'))
    assert len(headers) == 1, headers
    return json.loads(headers[0].read_text())

with tempfile.TemporaryDirectory(prefix='buddy-reader-proof-') as directory:
    ordinary = pathlib.Path(directory) / 'ordinary'
    selected = pathlib.Path(directory) / 'selected'
    child = subprocess.Popen([old, '--exact', 'process_lease_child'],
                             env={**environment, 'BUDDY_CRASH_FIXTURE': str(ordinary)})
    try:
        deadline = time.monotonic() + 15
        while not (ordinary / 'ready').exists():
            assert child.poll() is None, 'old reader failed ordinary open'
            assert time.monotonic() < deadline, 'old reader readiness deadline'
            time.sleep(0.01)
        assert version(ordinary) == 1
    finally:
        if child.poll() is None:
            child.kill()
        child.wait(timeout=5)
    run(current, qualifier, 'BUDDY_SELECTED_READER_QUALIFICATION', selected)
    assert version(selected) == 2
    run(old, 'process_lease_child', 'BUDDY_LOCK_FIXTURE', selected)
    run(current, qualifier, 'BUDDY_SELECTED_READER_QUALIFICATION', selected)
    assert version(selected) == 2
print('PASS: old opens format1, old refuses selected format2, current reopens selected format2')
PY
git worktree remove "$READER_PROOF/old"
```

The old refusal fixture asserts `Store::open` returns an error. The preceding
ordinary-open positive control, supported generation header, absence of a live
Store owner during refusal, and subsequent current-reader reopen qualify that
observation. Inspect the old source's format check as part of independent review;
the fixture alone does not assert an exact diagnostic message. The current helper
reopens the same root and adds another synthetic scope; it does not exercise a
domain resume or grant portable binding authority. Its explicit fixture-only
environment variable preserves the root for the caller, whose temporary directory
then removes it. Retain compiler outputs/source revisions as review evidence and
remove only your owned temporary build directory when no longer needed.

## Portable namespace contract refusal

The unreleased format5 namespace increment changes its contract fingerprint. Build
an unchanged host reader from pre-portable format5 source
[`8c97cc2384bbe39fdee42582d7f2b77b8253532c`](https://github.com/s116821/ReMarkableBuddies/commit/8c97cc2384bbe39fdee42582d7f2b77b8253532c)
with the same supported compiler, then explicitly supply its trusted absolute
executable path from the current Rust checkout:

```sh
BUDDY_TEST_PRE_PORTABLE_FORMAT5_READER=/absolute/trusted/old/reader-buddy \
  cargo test --locked --offline --all-features --lib \
  pre_portable_format5_reader_accepts_its_control_and_refuses_new_contract_without_mutation -- --ignored
```

The test constructs disposable empty stores with the exact preserved old contract
and a current new-contract store. The unmodified older executable performs only
the early existing-only mode Inspect with a cleared environment and explicit
trusted Config. It must first accept its old format5 control, then refuse the
new contract while preserving critical metadata bytes and absent mode/checkpoint
state. The current reader must reopen the new store. This demonstrates contract
refusal, not migration, actual portable publication, provider/native behavior or
production compatibility for an earlier draft format5 store.

The default harness ignores this explicit maintainer gate when no trusted older
executable is supplied; that skip is not execution evidence. The Linux author run
actually passed it with Rust1.98.1 and the unchanged pre-portable executable SHA256
`32976758b6056c199ba2947bbdc7665df724de29e3bb208ee690725824023ddb`.
Its old schema SHA256 is
`14417dc53bf35ead00701737256f4f11dc28fc49645f2c7e4f3db3c0dfef24aa`.

## Shared preference command evidence

Use the actual fixed selector with explicit JSON stdin and the trusted installed
Config path:

```sh
reader-buddy --shared-preferences-operation inspect --shared-preferences-input -
reader-buddy --shared-preferences-operation edit --shared-preferences-input -
reader-buddy --shared-preferences-operation status --shared-preferences-input -
```

Requests and private host custody follow
[the accepted Manager contract](shared-preferences-manager.md); the implemented
response profile is recorded in [the design](design.md#one-shot-preference-report-profile).
Do not place private text in command arguments, logs or shared fixtures.

Maintainers can exercise the source admission/GET-only and actual executable
profiles separately from the Buddy checkout:

```sh
cargo test --locked --all-features --lib preference_command
cargo test --locked --all-features --test shared_preferences_cli
```

The test-only HTTP model exercises positive qualified-adapter admission and real
Store publication, current selected offline reads/edits, fresh absence versus a
new catalog mapping, conservative deadline/read exhaustion, raw Config changes,
actual activation fault and failed output, and historical original proof without
private patch text. It grants no production qualification. A missing local head
with unresolved original checkpoint custody is Joining, never fresh absence.
The mode/domain lease covers admission and CAS; HTTP observers assert that the
Store mutex is released while GETs run. Output handoff rechecks raw Config; a
committed edit with changed Config remains unknown until original Status proof.

The real executable cases cover strict bounded duplicate-free stdin, mutual
selector exclusion, missing existing Store refusal, sealed provider refusal
before credentials/runtime, and offline original Status after mode/Config change.
That Status fixture deliberately constructs synthetic original custody to test
correspondence; it is not a successful Inspect/Edit permission or live provider
result. Actual editable-command parity in browser/Electron remains a separate
coordinated gate that these tests do not close. Existing provider/native and old
reader evidence retains its original source and must not be rerun or relabeled
solely to populate this profile.

The producer/transfer regression is
`actual_command_producer_worker_second_store_and_reverse_edit_keep_original_custody`
in the same command test group. It uses the actual private admission/Store path,
existing Worker and two Store actors under the test-only HTTP adapter. Assert
original membership and receipt postconditions at each phase; elapsed time alone
is never success. Its group-sharing fixture does not qualify an external account
or a production executable command.

## Selected notebook producer and Worker fixture

Buddy #139 source `f8e0e9bebd091c8ea3ce57a5d6d9a0f3d75900f6` adds selected
Generate and Refine to the existing explicit Writer command. The Windows host
fixture supplies a validated synthetic notebook buffer and guarded scripted
model replies. The regular command keeps its platform-specific file admission.
The selected fixture exercises the production planner, model handoff, format5
publication, local HTTP Worker transport and second-Store adoption.

- Two Maps submit without images. Reduce receives the four exact validated
  historical derivatives, the ordered Map results and selected memory from the
  same document aggregate.
- The publisher and receiver retain the same record and media bytes, including
  a noncanonical original envelope and the canonical Source3 object. The
  receiver adopts the original winning descriptor with its own Store token
  and refines from the received archive.
- Required canonical-media omission leaves the observed descriptor unapplied.
  An optional image omission is reflected in the adopted closure and refuses a
  later Refine before model submission. A false Reduce preparation reference
  is refused before activation.
- Initial AfterCommit and AfterActivation faults are uncertain with zero model
  entries. Existing-only CLI reopen recognizes the exact request as historical
  and refuses a changed request. An intervening winner refuses the late result.
  A failed Map is durable and never starts Reduce.

Four selected notebook controls and thirteen ordinary notebook runner and
persistence regressions passed locally. These are host fixture results.
Provider, tablet, broader Worker qualification and final paired delivery
remain open.

### Selected notebook stage interlocks

Buddy #139 successor `0edd8854de9b8dfd9793302a80c455e15baad84d` passed two
additional Windows host controls. After the first Map was durably generated,
both tests observed the second Map's original Prepare. A shared Writer
preference edit then refused the second model submission. In the other test,
an independent selected global memory edit after submission refused the second
result while the document token still matched. Both runs stopped with one
confirmed Map and no Reduce or draft. The existing progress-versus-completion
read-reservation regression also passed on the same test executable.

### Selected Worker original recovery and intent custody

Buddy #139 source `43fefad54a1988b445ea289a47389120001bd0c9` exercised the
production Worker protocol with local HTTP and real format5 Stores.

- A restart after durable outbox preparation restores a missing descriptor
  from its original bytes and provider ID. A create whose observation fails
  retries the same fixed slot and retires the exact original only after
  verified local activation. The passive Store records its own receipt.
- A superseded original only reads its agreed slot. Invalid occupied data is
  reported as unsupported or corrupt. Changing mode stops old-epoch requests
  before the HTTP adapter is entered.
- An exact unresolved local receipt in either the local or competing winner
  keeps that winner committed and unapplied across Worker restart. A competing
  winner without the receipt applies once and preserves the losing closure.
  Health distinguishes observed, committed and applied custody, and an applied
  optional omission continues to report incomplete media.
- Active and retained graphs are checked separately. A Writer probe on the
  passive Store accepts the exact applied foreign receipt/fact pair alongside
  a retained sibling root, while the foreign operation grants no local original
  receipt. A copied pair without Worker provenance and locally attributed bytes
  without an original Commit both refuse. An exclusively retained local
  original still fences a new request until genuine settlement.

The five Worker recovery tests cover the new custody and status branches.
Provider qualification, optional domain integrations, broader end-to-end
delivery and the parent archive remain open.

#### Exact received manifest bytes

Buddy #139 source `d1177463505409291dd0144e0a78c44a1cb3dc44` passed all five Worker
recovery tests, including the original-byte controls below.

The Worker checkpoints a reference to the original manifest before applying
the received closure. The Writer guard verifies the local bytes against the
descriptor's length and digest and requires the decoded manifest to equal the
saved manifest. It then checks the existing application receipt and lineage.

The passive Worker fixture receives pretty-encoded JSON over local HTTP and
admits its exact foreign receipt. Replacing whitespace at the same length
fails the digest check even though the parsed value is identical. Changing
only the saved parsed value also fails. The guard makes no HTTP requests.
Older receipts can use a surviving incoming copy. When that copy is absent,
admission requires the saved value to reproduce the original descriptor's
length and digest exactly. A discarded noncanonical original remains
unprovable from the old receipt alone.

#### Confirmed handwriting through the selected Worker

Buddy #139 source `fd92de7ca47fc6dd1f3bd214e9c8b8b2853a94b9` passed 13 focused
host tests and three handwriting CLI subprocess tests.

Local HTTP fixtures use the selected command dispatcher and real format5
Stores. A first confirmation proves current catalog absence, commits its
typed original, and becomes discoverable by the existing Worker. The peer
reopens the Store after interrupted activation and finishes the same local
receive receipt. The exact sample and envelopes survive transfer. The peer
does not acquire a local command receipt for the foreign envelope operation.

An identical original replays historically. Changed content or a concurrent
attempt to publish the same local operation in another correction conflicts.
A competing update preserves the losing closure. Forget appends a tombstone
without purging its original sample. Rollback appends a fresh conditional
update. A missing included sample blocks activation. Explicit omission admits
metadata with incomplete media and exposes no sample, even with cached bytes.

The ordinary command subprocess tests cover confirmation, status, query,
input refusal and the legacy-sync refusal. Selected data transfer leaves
recognition ingestion, the shared profile-wide Query command, and live
provider/native qualification open.

#### Operation custody across preferences and handwriting

A real Store fixture submits a selected preference Edit and a handwriting
Confirm with the same operation UUID, in both orders on format 5 and on the
format 6 source-target family with a compound base. When Edit wins,
Confirm refuses at the inherited cross-scope operation check. When Confirm
wins, Edit refuses earlier because the record operation ID is already
committed. The losing scope keeps its previous token or remains absent.
The single winning Store receipt survives reopening. Both Status routes
report only originals owned by their domain. Handwriting Confirm and Status
also refuse a different profile for the same correction UUID.

#### Selected Reader document uncertainty

Buddy #139 source `5e27c12a3ef8fc75d130531287e2e76a760c7fa2` passed 13 focused
Reader, Worker, settlement and Writer guard regressions.

The installed Reader policy checks the shared document fence while holding its
ordered preference, catalog and document gates. Its acquisition, submission
and result checks use the existing phase allowance for original receipt,
predecessor, retained fact and exact Worker manifest reads.

A host fixture initially acquired the Reader policy with both an active and
an exclusively retained unresolved local original. With the fence in place,
both acquisitions refuse, including the retained case with a different
conversation root in the same document. A newly published unresolved original
also refuses at the submission boundary after earlier successful acquisition.
An unrelated registered document and a verified foreign Worker receipt remain
admissible. The fixture exercises policy and Store custody without a tablet
or model call.

#### Selected profile-wide handwriting Query

Buddy #139 source `256e2d62ca340a7227429df4f33c342be8fd6984` passed four focused
selected handwriting tests.

The format5 command checks the complete observed catalog, then rechecks the
pin under ordered catalog and correction gates. The local HTTP Worker fixture
queries two transferred correction scopes, filters text, and enforces match
and encoded report limits. A verified empty catalog and a profile with only
tombstones report complete-empty. Pending local registration and an omitted
sample report partial without promoting any cached bytes into usable evidence.
This evidence covers Query and selected Store custody.

#### Composition with confirmed recognition

Buddy source `aa71b2364a264b4b687842fcf5498bd50cc250d8` combines the selected
Query and test-helper correction at `dab34c8d5dad83c9208da318c02cc75b20553b7b`
with frozen Buddy #105 `cba080c10c407d9dbb7a536b74bfa6023a7f9fec`.
The paired documentation combines `6fc331a0c75aa49fb363933d83e17f4647613ba0`
with frozen Docs #108 `9c2ae290101a44b582bc766edec5d215bed6b564`.

The image loader keeps its supplied bounded read callback for both resident
evidence and ordinary attachments. Store maintenance retains the distinct
selected-mode and handwriting admissions. Both recognition calls retain the
model-content lifetime while using the selected attempt's execution wrapper.

Independent review reproduced a Query compile error because the imported
`original_text` is optional. Successor
`c3806f9fa387854890c4f4a95443e7e923bda904` fixes that compatibility issue and
explicitly preserves the existing selected null-original refusal. Ordinary
confirmed enrollment after abstention retains its separate admission rule.

The corrected source passed 55 focused host tests and the Windows non-test
library compile. Two receiving fixtures passed on the same production diff
with the preceding test-only fixture iteration. Both frozen Docs composition
and its requirements passed all 127 strict OpenSpec items. The initial compile
error, fixture mismatch and overlapping-test Windows relink failure remain
recorded; hosted Linux CI is still required on the final published source.

The imported recognition context still owns local corrections. Selected context
ownership and its submission/result checks remain open in the tasks above. No
provider, native-input, model-fidelity or complete shared-consumption result
follows from this composition. Both feature changes remain active and unarchived.

#### Explicit selected handwriting context

Buddy `227a938e0d714b091abec7a3a892004eaa74a8e8` captured exact registered examples into
the existing confirmed context. Its selected owner retains the mode lease,
catalog root and tail, and correction tokens. The phase callback revalidates
those pins under the caller's ordered gates and charges the same allowance.
The real Store fixture covers unchanged admission, a replaced correction,
catalog advancement, omitted media, target exclusion, and refusal with
an exhausted allowance or a foreign Store. The ordinary context still
holds its local correction owner through report delivery.

#### Automatic selected Reader handwriting context

The resident Prepared receiver captures one context from the current shared
profile using a metadata-first scan. Real format5 Store fixtures cover an
unobserved catalog tail, complete-empty, pending local registration,
omitted media, zero sample reads on exact target exclusion, and three
selected examples from five eligible corrections. A checkpoint proof blocks
concurrent local replacement during the admitted effect. A stale Engine
cannot overwrite a newer checkpoint and refreshes its saved state on the
next Worker step.

The receiving fixture publishes Prepared and then uses the installed Reader
receiver with a scripted model handoff. Analysis and verification receive
identical examples. A correction replacement after analysis blocks the
verification submission. A replacement after verification blocks the
Interpreted write and there is no Generated turn. The unchanged case reaches
Generated. The receiving fixture uses loopback setup and consumes an
established preference selection through the local Store.

#### Selected Writer image normalization

The real Store fixture exercises the typed source route through its existing
whole-page normalizer and the selected Writer preparation and finish commits.
It proves exact target-hash exclusion and a guarded complete-empty context,
an unregistered correction blocking partial-empty before preparation, and one
eligible non-target example sent only to normalization. The unchanged path
publishes one fresh normalized source and one Generated draft. Correction
replacement before the normalization handoff prevents submission. Replacement
after the response prevents normalized-source publication and draft submission.
Replacement after draft submission prevents the final Generated commit. These
refusals preserve the original preparation and prevent re-entry. A mismatched
numeric page refuses before preparation or model submission.

Additional real-Store interlocks advanced the selected source revision before
or after normalization submission. Both stopped the normalized-source commit
and draft submission. A portable preference edit with the document token
held constant blocked draft submission when applied before handoff, and
blocked the final commit when applied after draft handoff.

Store faults before activation and after commit or activation produced no
model submissions. A pre-activation fault left the selected token unchanged
and no preparation receipt. Each lost acknowledgment left the original
preparation durable and prevented a fresh in-process run. The selected
command reopened the Store and reported historical preparation for the
exact original request only. Changed request text and a changed predecessor
digest refused. The historical command used no Drive or model credential
file and left the Worker checkpoint and selected token unchanged.

The actual selected subject-memory provider held one query result through both
Writer stages. The normalization payload excluded memory text. The unchanged
draft payload included the original relevant fact and committed Generated.
An independent global fact edit with the document token held constant stopped
normalized-source publication if made after normalization. The same edit
after draft submission stopped the final commit.

The fixture uses modeled resident image evidence and a scripted owned model.
The image command's fresh path still requires live provider qualification.
Live model fidelity, circled-target ingress and tablet qualification remain open.


#### Combined Linux Reader and Writer validation

The merged Reader/storage source was compiled on SCRAPPY-DOO after importing
`9e0b31484a4382b962a5835ec7a2ab6b3043a1d2`. Its original-owned restore constructor
needed the same process-local checkpoint RwLock initialization as normal Store
opening. That one-line correction is frozen in `a7c10f37e60e8ccc26c82f9ddd3573ef639db8e5`.
Strict all-feature/all-target Clippy with warnings denied, formatting and all ten
focused selected-handwriting controls passed on those exact source bytes. The
controls include the original family5 Reader and real promoted-family6 variant:
unchanged examples reach both submissions and typed target publication; changed
corrections prevent later submission or Interpreted/Generated/target publication.
The archive/restore callers retain full-media verification; metadata-only ranking
uses the same validation core restricted to handwriting records. Both selected
context constructors retain boxed ownership.

The ordinary locked/offline/all-features Cargo command was executed from clean
`a7c10f3`. Its library result was 1,203 passed and 44 ignored; preceding integration
groups passed, including executable provenance. The command then stopped on the
old sync-mode diagnostic expectation and is retained as a partial failed run,
not a passing full suite. A prior dirty-tree provenance failure and the initial
missing-field compile failure also remain preserved. Test-only `5ccccbea9d386eefa960e7c047d0d759c5520306`
updates the expected typed Unsupported wording while keeping unsuccessful exit,
empty stdout, no private data and unchanged filesystem inventory. The affected
sync-mode executable group then passed all ten tests from a clean checkout.

The accepted Writer image increment `972f81cf8c3a1ad7661ce63e3f4e06259d84e6ae`
was normally composed with that test-only successor, yielding frozen source
`f146bb17e6be68ad25506d3ce5bf3516d2703791`, tree
`2da2c7b2c863d695e5b7b2fcb7d137dcb4c44216`. It differs from coordinator candidate
`e5cd51b265475e91d1e8705bae791910f8935477` only in that expected diagnostic.
On this exact clean composition, strict all-target Clippy and formatting pass;
11 selected handwriting/Reader/Writer controls and four selected-Writer/command
controls pass. Executable groups pass sync-mode10, unassociated-feedback4,
compatibility9 and Writer43; the compile-fail documentation test passes1. These
last groups also cover the tail not reached by the earlier broad command.

Review preserves detached catalog/profile pins, explicit inherited-family
publication/readiness checks, document registration and budgeted uncertainty
proof, both boxed constructors, full-media archive/restore and the promoted
Reader fixture. The image runner retains its joined two-stage source/preference/
correction/memory checks and original preparation, without treating a later
ordinary Writer call as a guarded commit. No later test-only fixture successors
or new runtime drafts are credited to this run. Final hosted CI must qualify the
published combined head. No ignored provider/hardware qualification was opted
into, and no live provider, Drive account or tablet was contacted. The active
changes remain unfinished; this is combined source/fixture evidence only.
