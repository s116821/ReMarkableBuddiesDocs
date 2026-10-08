## Context

Exact mutable release v3.0.3 assets match GitHub digests: ARMv7 2fa969001cd8fbc8fa373b7c3dfcc99f858ceb516306d35d1b037c09861ac94a and AArch64 dab5b2b615cae41fd90a99fc6bdca87d26d04c0755440bded6b4832547c09cf7. Workflow run21912939175 sourceee31d275c7a2b7486e6de481ffe624b1de46d131 supports attribution, not signed provenance; tag names unpatched upstream source. Both static PIE assets actually execute under existing QEMU8.2.2, report architecture/version and retain pkgrel ordering. These probes do not qualify signatures/query.

## Goals / Non-Goals

Qualify exact downloaded ARM bytes against all existing actual-tool fixtures under explicit emulation. No tablet, bootstrap, install/add/del/upgrade, compatibility profile, publisher trust, source equivalence, new release engine or runtime product dependency.

## Decisions

1. Reuse qualify.py/fixture.py. Add mutually exclusive published-asset receipt mode; source-build mode still requires binary/archive identity, pinned source and417verifiedentries. No forged source-build receipt or sourcegate bypass.
2. Pin asset identity, architecture and QEMU byte identity in the adapter. Validate regular files/no link ancestors before processes. Published evidence records repository/release/asset/download digest, runtime and emulator identity, plus unsigned workflow/source attribution. A developer-supplied receipt does not authenticate a publisher or compiler.
3. Use explicit fixed `/tool/emulator /tool/apk` prefix only in published mode, never global binfmt. Extract dereferenced static emulator from existing pinned image into private evidence, hash-check and mountreadonly into existing Python/OpenSSL fixture image. No installs/rebuild/shared tag changes.
4. Preserve two phases, private Linux owner binding, read-only tool/emulator/harness mounts, networknone/capdropALL/no-new-privileges/containerread-only, tmpfsnoexec/nosuid, fixed config/key/dualroots, timeouts/cleanup and bounded diagnostics. Validate both tool and emulator hashes inside the container before generation/reads.
5. Same13cases for both architectures: signedAPK/index, wrong/missingkeys, signedcontrol/index/payloadtamper, fullpkgrel, seededmetadata/scripts/status, owned/unownedfile. Syntheticx86_64metadata is querytestdata, notARMcompatibility. Retain rootimmutability/script sentinel requirements.

## Verification and limits

Adapter guards must reject wrong asset/emulator/receipt/mode combinations before launch and prove fixed prefix/isolation and original source gate. Run actual13cases perARMasset and rerun originalhostsourcebuild. Focusedguards, Python syntax, docs/OpenSpec/diff validation, exactfreeze and independentreview/CI required. Emulation proves bounded behavior of these precise bytes, notnativehardware, realpackage trust, remoteSSH shell effects, lifecycle or installation eligibility. No binaryredistribution in this increment.
