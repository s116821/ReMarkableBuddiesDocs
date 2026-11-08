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
