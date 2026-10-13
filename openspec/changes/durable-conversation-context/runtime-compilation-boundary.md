# Unqualified Reader scaffold compilation boundary

October 13, 2026. Proposed bounded delivery repair on Rust parent
`7b207ec8a42548c12960699854107236eb2bbd7f` and Docs
`60a8e0e7ec6ec181ed36652b9b7e33d222086a6c`. PR32 inherits PR30's 24 strict-lint
diagnostics. Repair the owning parent once, then reconcile the inspection child.
Do not suppress diagnostics, expose private effect constructors to satisfy lint,
or manufacture a production qualified source adapter.

The [Reader admission contract](reader-admission-api.md) explicitly has no
production `ReaderSourceAdmission` implementer. The controlled context mint,
dispatch reservation/permit, selected backend effect wrapper, development-only
capture carrier and Attempt attachment have recording test callers only. Their
verification remains useful, but including this unreachable scaffold in ordinary
runtime compilation misstates the current integration boundary.

Compile those private, unqualified execution pieces under `cfg(test)` until the
qualified production integration is implemented and reviewed. Keep their source,
all refusal/currentness/uncertainty/foreign-binding/consumption guards and tests
intact; do not use lint allowances or delete unfinished coverage. Retain production
storage/publication/recovery schemas, public bounded Reader plan validation,
historical selected binding inspection and the existing unbound Reader behavior.
Public read-only Workflow inspection remains available with its existing refusal
for an unbound Workflow. Do not add a selected runtime constructor or change stored
formats, SDK dependency, Cargo metadata or native implementation files.

Private fields used only by test-only execution are also conditionally compiled.
Ordinary Attempt has no attachable execution context; where existing checks inspect
that optional field, use a private helper that is always false in ordinary runtime
and reads the original field in test compilation. Preserve the original errors and
guards in the recording path. Keep selected-mode refusal and read-only inspection
logic in production; conditionally compile only effect ownership members of the
private facade. The non-test build still cannot mint or dispatch selected effects.

This does not complete task2.10, production bootstrap, native source association,
Writer, recovery or whole REM37. Reintroducing these execution pieces into ordinary
runtime requires the actual qualified owning adapter and all existing acceptance
scenarios; a lint pass is not permission to enable them. Preserve the protected nine
files and pins in the separate active checkout byte-for-byte.

Before delivery, compare the narrow source boundary with the exact 24 diagnostics,
run required all-target/all-feature strict lint, formatting and the affected
context/dispatch/Attempt/development/binding tests, and verify ordinary library
compilation. Independently review unchanged public/storage/legacy behavior and the
explicit remaining production gate. Reconcile PR32 on the repaired PR30 parent,
repeat only affected child lint/inspection integration checks, and publish exact
source/Docs revisions and remaining gates. Keep existing drafts and same-delivery
Docs lifecycle; no merge, sync, archive or Done follows from this slice alone.

Source basis: current parent/child PR comments and retained exact committed-source
Clippy diagnostic log, current source and accepted Reader admission API. No new
native test or runtime qualification is asserted.
