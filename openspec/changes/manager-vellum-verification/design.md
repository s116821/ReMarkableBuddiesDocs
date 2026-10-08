## Context

Source authority: current REM-41/42/46 descriptions/comments and pinned upstream source. Released Vellum CLI v0.3.2 resolves cd3bc9978ec2d037bd5671d17e1043d212f15b9f; apk fork v3.0.3 resolves 505bb9b0fb5d7d35a613a1f991e04a25eedadeeb. CLI main initializes/repairs virtual packages before command parsing. Its index parser does not authenticate signatures and version helper ignores `-rN`. Therefore the wrapper is not the observation/verification interface for this increment.

Current Buddy official assets are binary tarballs/provenance, not signed APKs. Unfinished REM-46 candidate retains legacy toolchain metadata and no consumed OpenSDK revision. A synthetic signed fixture cannot fill these production gaps.

## Goals / Non-Goals

Goals: establish actual-tool behavior for explicit trusted keys, signed control/payload integrity, complete apk versions including pkgrel, database metadata and ownership readback; bound all files/processes to private fixtures and report exact receipts.

Non-goals: product eligibility, official APK signing/build pipeline, production trust distribution, tablet access, Vellum bootstrap or wrapper execution, add/del/upgrade, rollback, source equivalence, installer UX or release-engine replacement.

## Decisions

1. **Use actual maintained tool protocol.** Invoke a supplied separately built upstream apk binary. Build exact source in an existing Linux environment and retain revision, build configuration/dependency versions, binary digest and output receipts. Actual initial build of tag commit 505bb9b0fb5d7d35a613a1f991e04a25eedadeeb rejected the required `--install-root` protocol. The public workflow builds the `vellum` branch, then recreates a release under VERSION without moving the existing upstream tag. Successful run 21912939175 identifies branch commit ee31d275c7a2b7486e6de481ffe624b1de46d131, which contains the required separate metadata/payload roots. Select that unchanged exact source for host qualification; record the rejected tag build. Public workflow chronology is evidence for the build source, not cryptographic proof of current published ARM bytes. Published ARM release identity and Linux host source-build identity remain distinct. Do not substitute a handwritten signature/version/database implementation.
2. **Keep GPL source separate.** Fetch/build upstream reference outside Manager. Manager harness contains process orchestration/assertions only. Upstream license/notices/source requirements apply to any future binary distribution; this increment does not bundle a binary. CLI MIT reference remains reference, not a cloned implementation.
3. **Offline fixture boundary.** Create a unique temporary directory with independent metadata root, payload root, keys/config and output. Direct apk arguments and environment must select only these checked absolute paths; no `/` payload install root, inherited APK_CONFIG or system trusted-key fallback. Run with networking disabled. Never invoke wrapper, install, delete or bootstrap. Generate fixture keys transiently and remove them on ordinary completion; retain no private keys in receipts or tracked files.
4. **Use upstream package/index tools.** Synthetic name/version/payload/script metadata is test data, never a real Buddy release or supported compatibility assertion. Generate signatures using upstream tooling and ephemeral signing keys, and create malformed cases by modifying signed bytes. No new production package format or packaging engine is introduced. Fail if valid fixture verification fails; do not weaken signature settings.
5. **Observe full installed metadata without installing.** Seed a synthetic database fixture derived from documented upstream installed-index format/test data, then query it with actual apk JSON and file ownership commands. This proves query behavior only; seeded presence cannot qualify actual installation/service/provenance. Preserve full pkgver-rN and distinguish source-package `origin` from distribution source.
6. **Assert no mutation.** Snapshot file inventories, bytes, modes and symlink targets of fixture metadata/payload/key/config roots before and after each read command, including success and failures. Commands have bounded timeouts, diagnostics exclude keys, and nonzero/timeout remains explicit failure. Fixtures never touch original documents or real Vellum state.

## Required cases

Valid signed package and signed index verify with explicit vetted fixture key; missing/wrong key refusal; changed signed control and changed payload refusal; full `1.2.3-r2` versus `1.2.3-r1` comparison; exact installed version/arch/commit/dependency/script/status query and owned/unowned file lookup; unchanged roots after each read operation. Test-only versions do not mint project versions. Default Manager remains unable to install.

## Risks / Tradeoffs

Upstream tag, default master and Vellum branch source differ. Pin the evidenced Vellum branch source; source-build qualification cannot imply ARM binaries or supported-device qualification. Existing Linux images may lack build dependencies; task-owned container layers may supply them, but do not install host setup or invent a fake tool to conceal that gap. Source-signing algorithm, v2/v3 format and key filename behavior must follow actual tool evidence; no production selection follows from fixture success. `apk verify` authentication and read-only behavior remain acceptance assertions until actual results prove them.

## Verification and delivery

Run focused actual-tool harness and meaningful negative cases, syntax/lint checks for changed files and central OpenSpec/docs validation. Freeze exact paired sources/receipts for Main-owned independent review and CI. Synchronize/archive only the completed bounded capability after all gates; do not archive unfinished artifact/device integration or REM-46. Main coordinates merges and canonical persistence.
