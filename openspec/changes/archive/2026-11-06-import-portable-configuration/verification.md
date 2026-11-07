# Portable import source verification

## Scope and revisions

Accepted precode69f90bb771b4366bec72cbb78f4517ef6de16911 was normally reconciled
with Buddy516b60b29fe7d7db46a22480312d6155657a69d0 and
Docs1b26d39cd72442c373ad68c112d167c88ed52870 before implementation.
The Windows source contents tested below were committed as
Buddy e5bf3b8ad7f5681f3f90d7cfc097aee3cae53ca3. This is source/host evidence,
not an assertion that a release with that identity has been built or installed.
Exact paired delivery heads and current CI belong in the linked PR comments.

## Executed checks on November 6, 2026

Used the existing Windows x86_64-pc-windows-msvc Cargo cache and Rust1.98.1;
no second target directory, provider calls or tablet operation.

- `cargo fmt --all -- --check`: passed.
- `cargo test --locked --offline --lib config:: --all-features --target-dir ../ordinary-configuration-target`:
  all83 passed, including17 portable tests and the strengthened same-actor
  nonordinary-mode controls, actual Windows case aliases, original publisher
  faults and existing editor/notebook admission regressions.
- `cargo test --locked --offline --test portable_import_cli --test portable_configuration_cli --bin reader-buddy --all-features --target-dir ../ordinary-configuration-target`:
  all13 binary,2 existing portable CLI and3 new import CLI tests passed.
- Docs12 tests and manifest/current-guidance/preserved-source verification passed.
  Named strict OpenSpec validation passed before canonical sync/archive.
  Final strict all validation passed122/122 after explicit canonical sync/archive.
- Source and Docs diff checks passed; unchanged export/inspection regressions
  execute in both the library and real subprocess routes.

Windows emitted existing platform-gated dead-code warnings in unrelated runtime
and notebook test helpers. No new Windows warning suppression was added. Required
hosted Linux strict Clippy/CI remains a separate delivery gate. Unix symlink,
selected-directory link and real FIFO checks are present but were not executed
on this Windows host; no Linux/platform pass is inferred from Windows results.

## Requirement correspondence

- Real Config overlay tests preserve excluded model/endpoint/reference/paths and
  omitted parent/child declarations, explicit supported null, empty objects,
  disabled and exact Unicode/CRLF/tab text. Semantic no-op preserves exact bytes
  without an intent or Store admission, even when roots are missing or busy.
- Private reports contain only fixed parent names, origins, digests and original
  intent. Complete duplicate-free original/artifact/result checks, closed request
  shapes, malformed/numeric/version faults and independent inclusive request,
  compact artifact, original Config and computed-target bounds refuse as a whole.
- Actual-file/Store and subprocess round trips cover legacy1 and complete record/
  media notebook4, each with absent and LocalOnly mode. Inventories preserve owned
  records/media, CURRENT, identities, other credentials, cache and mode state.
  Busy, stale raw bytes, alternate paths and foreign artifact/target/base hashes
  refuse before publication. Artifact-free Status remains an observation only.
- Distinct common-family admission preserves other constructors. Corrupt/missing
  notebook readiness, ownership, commit/object history, retained/active selected
  residue, legacy2/3 markers and same-actor isolated/shared mode fixtures refuse
  without repair. Canonical Config/root and inter-root overlap checks include
  actual Windows case aliases while exact supplied-path binding stays distinct.
- Existing AtomicCall/AfterPublication/ChangedReadback hooks exercise actual raw
  publication uncertainty without rollback/retry. Original-intent Status only
  observes current bytes. Real OS ownership probes run inside output writes for
  successful, immediate and prefix-failing frames; mode mutation is also blocked
  under the original ordinary custody. No mutating output flush is performed.
- Actual bounded subprocesses keep Inspect stdin open, poison dotenv/runtime/
  provider environment, cover argument conflicts and exact-dash input refusal,
  and verify complete private frames without runtime/provider initialization.

This change affects the explicit saved-file maintenance boundary, not the Reader/
Writer execution model. Deterministic real-file/Store/CLI tests cover that boundary;
no artificial native gesture or model-response simulator scenario is introduced.

## Retained failures and corrections

The first unit compile failed with E0283 from an ambiguous AsRef conversion in a
new test helper. It was corrected to a typed slice borrow. The first binary run
passed11/13 but found missing exclusions on the new input flag: existing exhaustive
conversation/research argument-conflict checks failed. The input flag received
the same exclusions as its operation selector; all13 subsequently passed without
changing those assertions. Both failed logs are retained outside source alongside
the successful logs. A preliminary17-test pass preceded the stronger same-actor
mode fixtures; the final83-test configuration run includes those changes.

## Remaining gates

This archive completes the finite source implementation/host qualification/spec
sync, not the whole synchronization project. Independent source/evidence review,
current required CI, coordinated squash integration and main/release verification
remain required. No effective runtime activation, production credential authority,
cloud/archive integration, Manager UI, supported tablet/native qualification or
hostile live-filesystem race protection is claimed. Runtime activation is always
unverified in this new protocol. Unrelated unfinished changes remain active.
