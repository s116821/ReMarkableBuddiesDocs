# Design

Reuse apk_source_build.build and its bounded owned processes. A small build-only
entry emits both existing targets, ARMv7 installed-resident-output then ordinary
AArch64, with explicit real stable Buddy tag/commit and independent SDK v0.2.0
source. It copies the already qualified descriptor-frozen binary and canonical
existing build metadata, saves private evidence and publishes an exclusive final
hash manifest only after complete validation. Partial outputs remain incomplete;
there is no signing/key/trust/package stage or inferred install eligibility.

Fresh build/output roots must be disjoint and outside source/SDK/producer roots.
The completion verifier rejects changed bytes, extra/missing files, invalid
metadata/source/target/SDK/profile or absent completion. It validates retained
evidence identity, not historical truth of caller-authored JSON or production trust.
The artifact is installation-ineligible and later consumers need explicit review.

YAML owns orchestration. A separate workflow_dispatch has a default-false build
execution gate; no push/pull_request/release trigger. Three ordinary full
standalone checkouts (producer, actual release source, SDK proof) use the pinned
checkout action with set-safe-directory:false and no persisted credentials.
Inputs go through environment/argv, never shell text interpolation. Existing
release actions/toolchain/pinned Cross/images are reused. A narrow reviewed Linux
Cross mapping admission adds maintained revision8c1a8aa while preserving the
already reviewed49cd054 path and unchanged Windows mapping. No rootless/userns
alternative or ownership/config rewrite is introduced.

Normal PR tests cover filesystem/metadata/completion/tamper/failure and workflow
gates without compiling target binaries or running Docker. Actual compiler,
container, SDK tag observations and runtime remain a separately selected manual
operation. Workflow timeout and existing phase/diagnostic bounds stay explicit;
failure uploads only bounded compiler diagnostics, success retains the finite
input artifact14days. Heavy intermediates remain ephemeral on the hosted runner;
no self-hosted workspace or held Windows operation is selected.

The unfinished build-signed-buddy-apk parent retains signing/lifecycle/production
and actual build qualification. This finite source contract is synced/archived in
its own paired delivery only after tests and independent review.
