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
