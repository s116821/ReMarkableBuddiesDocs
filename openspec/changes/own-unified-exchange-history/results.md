# Owned exchange history verification

Buddy candidate `77043c8008a8ccf0d678c24dcd9cb31d4b305383`, tree
`dbae3e5243ec89b9f11e9f8a17ac9db19ea475da`, is based on delivered
`5e18c63edbde1b69970a6540668a0d9f08f96a90`. Docs starts at delivered
`3fa30982e55d8405cfdb28d2823a8deb0e024f81`.

Exact Windows verification passed strict library Clippy, the maintained
ownership fixture and all six existing layout tests. The actual binary
reported 20 modeled cases and zero native effects. The authoritative log is
`02-windows-exact.log` in the local evidence directory.

The fixture uses the actual Ledger and newest-first logical layout, with
ordinary source bytes and a retained external export association. Its page
owner is modeled. It exercises first and latest exchange ownership, repeated
undo and redo, incomplete exchange refusal, changes to protected regions or
older text, page/visit/session/content drift, stale receipt, cancellation,
replacement and reopening. It verifies exact presentation readback and
unchanged source and transcript records and export association. Unknown
effects, a wrong operation receipt and changed readback require reconciliation.

The increment does not dispatch a native range edit or settle a durable native
effect. Existing legacy history remains separate. No tablet files are needed
for this host work.

## November 5 delivered-main integration

The original standalone receipts above retain their exact revisions. Hosted PR
merge run `41993283777` failed because delivered main added the explicit
`Interaction::BlankStart` variant and the history controller's exhaustive match
had no corresponding arm. The failing log remains preserved by the coordinator;
this is an integration defect, not a waived check.

Buddy successor `6e0f78cdc59fbfa2c7bb04289ba9eca3d05f08ef`, tree
`ab94b7237e95527ce9c959451f0f6b122012da73`, normally merges original
`77043c8008a8ccf0d678c24dcd9cb31d4b305383` with delivered main
`91dcc601154507790254946f8f0f811204a0fd43`. The controller explicitly discards
ownership on Blank Start, consistently with Reader and Invalidated. It performs
no edit on that event. The maintained scenario adds visible and already-undone
Blank Start cases, verifies unchanged presentation/effect count at the transition,
then refuses old Undo and Redo even after restoring the old modeled page state.
Existing source, transcript and external-export invariance assertions still run.

The effective source delta remains five paths: the controller, maintained
scenario/module, and their workflow/simulator registrations. Delivered startup,
interaction reducer, legacy history, resident workflow and Cargo/SDK pins are
unchanged. Docs normally incorporates delivered main
`db4c4b2a25e1b54ef8f8d8add7446d5725f54ced`. The OpenSpec change remains active;
native range effects and durable native settlement are still unqualified.

The maintained ownership test and all six layout tests pass on Windows. The
actual simulator binary reports 22 modeled cases and zero native effects.
Default-feature library Clippy completes with the three existing Windows
resident-platform warnings. The broader Windows all-features invocation fails
in unchanged delivered resident-client code because `digest` and `encode` are
unavailable in that platform configuration; its log is preserved separately.
It is not a passing all-features receipt. Hosted strict Linux checks remain
required for this successor.

The coordinator independently reviewed the three-file merge-resolution delta
and the two new invalidation cases. No blocking source finding remains in this
bounded correction. The exact logs are retained under
`work/rem43-owned-exchange-evidence/nov05-*.log`; no new tablet operation,
provider call or build-cache directory was used.
