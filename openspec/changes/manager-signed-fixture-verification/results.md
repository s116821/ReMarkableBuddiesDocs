# Actual original-fixture verification on SCRAPPY-DOO

Manager implementation: `10263fb82ad94ab670fd759de4e8dd367d775f29`, [PR14](https://github.com/s116821/ReMarkableBuddiesManager/pull/14), five-file delta over accepted Manager46cc. Central pre-code commit9d4037d preceded implementation, based on administrative Docsde00. Parent PR13 behavior/accepted history preserved. Exact Docs publication and required CI are recorded in PR comments; independent review and Main/Root parent-first delivery remain pending. This change is intentionally active, not synced/archived unilaterally.

## Original handoff and independent trust
Main producer helper4e79104cc5948ee77cca517fb71f333bae056bba / Docsfdb33b7ef79e4f6773bf96ad884782ab8d80958b built historical v0.2.0/ff8ad75bec45fca403d55a7b6d93eb83ab732e3d. Owner actual compilation/runtime and saved producer comparison remain separately attributed: [owner proof](https://github.com/s116821/ReMarkableBuddies/pull/38#issuecomment-6145439700), [saved-evidence inspection](https://github.com/s116821/ReMarkableBuddies/pull/38#issuecomment-6145472860). No producer rerun here.

Authenticated Drive transfer of [original public transport ZIP](https://drive.google.com/file/d/1wVwlgTsJbp3wZw0IGbzqlaW2WaGijrNP/view) matched31,078,236bytes/SHA2566ddeff4ae7fe45b855f829018edf5db59f77550dadae42719b003f5a89efc062. [Independent manifest](https://drive.google.com/file/d/1kMM0A6dnXiiNy9x4h7h9OSqP3LN96PpR/view) matched1,594bytes/SHA256e8b3e47e0d42b64342bfe53eb3bb362abefa92c11a355fd754f4a5a238a37d40. Exactly six public entries matched separate original hashes/sizes before bounded unwrap; no APK payload extraction. Original artifact identities are in verification.json.

The separately communicated generation DER-SPKI SHA256233571d3c096b188fcb10db17da80edf2f51b3b52c5aaef68a8721d028f5d39f matched actual OpenSSL public PEM→DER output. The adjacent key/receipt is not its own trust authority. No private key was transferred, generated or requested.

## Executed evidence
Final report `real-fixture-r4.json` reproduced12focused observations using existing exact-source ee31d275c7a2b7486e6de481ffe624b1de46d131 tool. Consumer binary1f574216fca1b0145931f7cdb8e843634c909f578d791d0cabddd8a826d5ef8f is a separately qualified build, not producer tool7488. Source archive27f5038970258cb61ea55d9b373c4c4d5e9605a693bf15aa8b661a98d65763a0 and417-entry build receipt were revalidated; prior417-blob audit was reused, not repeated. Immutable local runtime48608ea0b7ce360f41a27f8d3c4c7d8d897366a03cc32de0c5f45da4f2fe4983, effective UID/GID, actual read-only mounts, empty isolated config/repositories/keys and no network were used.

- Actual SPKI matched; a wrong independent expected pin refused actual DER correspondence.
- Original ARMv7 APK, AArch64 APK and index: verify exit0, empty stderr.
- Three bounded actual JSON adbdump readbacks: standard fields/full0.2.0-r0/pkgrel/source/arch/vendor tags and the exact signed three-file inventory matched reported producer claims and both authenticated index entries. No scripts/triggers/extra paths were admitted.
- Different public RSA modulus/key set: verify exit1, UNTRUSTED signature.
- Modified signed package description and signed index description: verify exit1, UNTRUSTED signature.
- One modified actual raw ELF payload byte: verify exit1, file integrity error.
- All originals and isolated inventory/content/modes stayed unchanged. Payloads were neither extracted nor executed. Owned containers were removed by --rm; no signer, device, service, release/tag or enrollment action.

The first broad-field positive runr1 passed. A stricter info-field check inr2/r3 correctly stopped the report because the initial consumer omitted the upstream package's embedded40-hex `hashes` member. Source inspection of pinned app_mkpkg confirmed this is its SHA1 UID, distinct from mkndx's64-hex SHA256 metadata identity. The corrected finalr4 admits/records both separately and passes. Those failed consumer runs remain local history; they were not signature failures or qualified results.

## Limits and checks
Package payload integrity is verified by actual apk; signed metadata file digest/size is inspected, but embedded build.json contents are not extracted/parsed and the binary is not rebuilt/run. The signed index matches the saved producer regenerated readback; public-only independent metadata-hash regeneration/binding is not claimed. Signature-valid malformed/replacement-package cases, source/compiler truth, historical source-version gap, production keys, consumed SDK, firmware/native/lifecycle/source handoff/reproducibility remain open. Every result retains legacy-no-sdk/not-qualified and update/install eligibilityfalse.

Focused guard suite8/8PASS covers duplicate/nonfinite/UTF8/bounded JSON, pins, actual manifest mismatch, snapshot content/inventory/links and actual subprocess output/deadline cleanup. Manager lintPASS, diff whitespacePASS. Normal CI runs these guard tests (threeLinuxprocess/link controls explicitly skipped on Windows); it does not run/claim external-tool observations. Docs20currentguidance/126preservedsource,12portabletests and26strictOpenSpec items PASS. No broad accepted actual-tool/producer/hardware matrix rerun.

The report is sanitized actual observation evidence, not private build diagnostics. Its SHA256 is 5dcb830d09882a7ad0c277f363e7754795637524a943aec9baca644ab193fba7; its consumer script hash is 8cd52768b8bfd636df971747652d84edda832b8dc497f309f6e242f2bc8240dd. Publication SHA metadata changes leave the checked file tree unchanged.

Source basis: authenticated Drive outputs and independent Main/Root control-channel hashes; current source/contracts; actual SCRAPPY execution; separately attributed producer/save-evidence reports.
