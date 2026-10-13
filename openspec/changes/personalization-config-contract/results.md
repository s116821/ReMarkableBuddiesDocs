# Scoped implementation and verification

Rust source ac60b62f28f30a9f05fc87076388ef079fc97b1e, [PR39](https://github.com/s116821/ReMarkableBuddies/pull/39), is a four-file increment over public PR37 parent3e87abc862b40c98a8a7c9dd4586ab377e268d37. Paired [Docs PR28](https://github.com/s116821/ReMarkableBuddiesDocs/pull/28) starts from actual Reader Docs PR22 parenta64b068f8563e6d1524caa919be96478f227bbbf. Initial precode d412bee preceded source work; Root corrected the unrelated initial Docs parent before publication. Exact frozen interface is in docs/personalization-config.md, initially published at66e8d9b1cc8efd8d971174c2594d6dd05e813fdb.

The implementation adds defaulted version1 personalization,16KiB UTF-8/noNUL validation and redacted Debug. Its immutable snapshot retains exact enabled text only as preference, with no permission/grant API. Fixed one-shot inspect/set/disable/clear uses existing explicit config selection, bounded strict stdin, whole-file expected revision and REM-36 Store preflight/lease/replace_config. Save revalidates the published config/setting and reports restart-required. It never reports running runtime adoption.

## Actual local controls

Windows Rust1.98.1 focused final source checks passed:

- Five new personalization tests: default/bounds/version/redaction; exact Unicode/CRLF/whitespace edit-disable-clear and immutable snapshot reload; stale CAS/busy/missing Store; invalid UTF-8/duplicate/oversize stdin and fixed failure output; actual host CLI save/readback/disable/clear without model credentials/device startup. Unrelated model setting and retained history/learning fixture bytes were checked unchanged.
- Two existing storage-config controls passed, preserving CLI/environment/file/default precedence and secret handling.
- Three existing binary interface controls passed after adding the one fixed option to the exact CLI inventory.
- cargo fmt --check and ordinary nonmock cargo check --locked --offline --bin reader-buddy passed. The20 inherited unfinished Reader dead-code warnings remain explicit, not suppressed or claimed strict-lint acceptance. Root/Main own the parent lineage reconciliation.
- Central Docs guidance/provenance (20currentfiles/126preservedblobs),12portable tests and strict OpenSpec1.2 all18items passed, including this named change.

No broad unchanged accepted runtime/native/provider/SDK matrix was rerun. Tests use actual isolated temporary host config/Store files and the actual CLI, but do not qualify Linux/native durability or runtime restart. No tablet, routing, service/account/provider or credential operation occurred.

## Requirement/scenario mapping

| Requirement | Evidence | Limit |
| --- | --- | --- |
| Optional portable setting; defaults, disabled and exact text | Config default/validate and five focused controls; serde portable Config serialization; redacted Debug | Selected cross-device policy is unfinished; no sync operation was performed |
| Guarded maintenance; mutation/readback and refusal | Existing Store lease/replace_config, actual config/CLI controls, stale/busy/missing/invalid cases | Hostile same-user atomicity and power-loss behavior are not new guarantees; unsuccessful postdispatch report can be an uncertain write |
| Honest reload and immutable snapshot | Actual fresh Config reload/digest readback and old/new snapshot tests; restart-required/unverified report | Receiving Reader/Writer application, unchanged transcript routing, live provider precedence and running-runtime activation are not implemented by this increment |

Independent source/contract review, final reconciled-parent validation/required CI and canonical sync/archive remain pending. Root dispatches the existing reviewer and controls final readiness; Main owns updated parent ancestry. Broader REM-53/REM-42/REM-52 and unfinished active Reader specifications remain open. No whole-issue Done, release/tag or merge follows from this evidence.

Source basis: current REM-53 full requirements/all available timestamped comments, REM-36/REM-42/source/public guidance, actual isolated compiler/filesystem/CLI/Docs outputs and Root's explicit ownership/parent coordination. This is owner evidence, not independent acceptance.
