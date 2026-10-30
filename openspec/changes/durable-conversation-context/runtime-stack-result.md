# Reconciled unfinished Reader stack

October13,2026. Accepted parentb085b368 is propagated through the existing drafts.
These replacement heads preserve the unfinished feature scope, not native readiness.

| Rust draft | Old head | Replacement head |
| --- | --- | --- |
| PR34 runtime | 4d539b80 | 18980329a031d2a8809d9a1b351cff192d81f4d2 |
| PR35 mode | 62a5376f | 973441af0341c0490d680332fbba883509de6412 |
| PR36 selected | fac54284 | c23e0b887eca9ed25e7473ab1afb899a4c068a1b |
| PR37 composed | 3e87abc8 | 1f4b29134532f720dd4aba34a14549b295861ad7 |

Runtime retains its actual production selected_runtime/with_selected and
RefusingBackend path. The same supplied backend is owned until facade destruction
in the non-test retained field; no early drop, fake read, lint allowance or public
effect constructor. Selected admission, mode/Store and composed publication remain
production code. Only unqualified context/dispatch and existing test carriers are
test-compiled. The no-memory generated wrapper has only recording-test callers;
production already calls generated_with_memory and keeps all memory/selected
refusal guards. Conflicts preserve new public exports and guards together with
the reviewed test-only context helper.

Independent final source review accepted the clean endpoint and ancestry. Net
diff against original3e87 is fivefiles48 insertions/5 deletions; refusal backend,
selected Attempt body and Orchestrator production body are unchanged. Mode patches
and three focused panic witness commits compare exactly by range-diff. Historical
test outputs remain bound to their original revisions.

Observed owner Windows Rust1.98.1 checks: required all-target/all-feature strict
lint passes at runtime adaptation7.01s, mode29.78s, selected12.71s and final
composed8.42s. Formatting/diff pass. Final endpoint passes14 runtime/mode CLI tests
and four targeted actual Orchestrator/context/development controls. The earlier
runtime10-case check is included in later14 coverage, not added. A selected_runtime
unit filter matched zero tests and is not a pass/coverage claim. No broad test,
native/gesture matrix or unchanged isolated panic witness was rerun.

Docs PR16/18/20/22 patches are reconciled on parent37e10df. Existing accepted task
and result text stays historical; distinct tasks3.21/3.22 preserve the parent
boundary without overwriting startup3.7–3.9. Protected active nine files and pins
remain outside the replacements. Committed SDK staysd01b4bdf; protected gesture
WIP/SDK5c0bc303 is not silently adopted or described as committed.

Exact paired Docs reconciliation/final checks, public branch readback, required
hosted checks and Root final readiness are separate. Production qualified
bootstrap/source/page/orientation/lifetime/native/Writer/recovery, full task2.10
and whole lifecycle remain open. No sync/archive/merge/Done for this unfinished
Reader change. REM53's separate owner rebases onto the final published PR37/22
parents before its own final validation.

Source basis: exact Git ancestry/diffs, executed focused local outputs and
independent source inspection without test reruns; internal review has no public
transcript link.
