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
