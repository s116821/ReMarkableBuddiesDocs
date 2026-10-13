# Scoped implementation and verification

Initial Rust source ac60b62f28f30a9f05fc87076388ef079fc97b1e, [PR39](https://github.com/s116821/ReMarkableBuddies/pull/39), was a four-file increment over public PR37 parent3e87abc862b40c98a8a7c9dd4586ab377e268d37. Paired [Docs PR28](https://github.com/s116821/ReMarkableBuddiesDocs/pull/28) initially started from actual Reader Docs PR22 parenta64b068f8563e6d1524caa919be96478f227bbbf. Initial precode d412bee preceded source work; Root corrected the unrelated initial Docs parent before publication. Exact frozen interface is in docs/personalization-config.md, initially published at66e8d9b1cc8efd8d971174c2594d6dd05e813fdb.

## Reconciled delivery

Successor Rust6254092cbcc7b9fb5ba7c116567fe8ccda373788 is rebased onto public PR37 1f4b29134532f720dd4aba34a14549b295861ad7; paired Docs branch is rebased onto PR22 bea05aba7191fd22ca1ad7bbc806e9d50a971140. Rebase was conflict-free. The four reviewed personalization source files are byte-identical to ac60b62f; the frozen guide and synchronized canonical specifications are unchanged. Independent source acceptance therefore still covers this new delta, without claiming acceptance of the entire inherited unfinished Reader stack.

Actual Windows successor checks pass: formatting,10focused/adjacent/binary controls and cargo clippy --locked --offline --all-targets --all-features -- -D warnings. The previous20 inherited warnings no longer occur. The tested actual CLI identifies dev.v0.2.0-73-g6254092 with a clean source tree. Docs12portable tests,20guidance/126preservedblobs and strict OpenSpec19/19 pass. Successor hosted Docs run38433018033 reports success and Rust title38432994795 passes; Rust required run38432994629 remains running at this checkpoint. Earlier failed runs below remain historical evidence, not the successor outcome.

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

## Hosted and independent evidence

The independent Sol reviewer accepted the bounded Rust ac60b62f/Docs66e8d9b1 source and interface without rerunning owner controls or claiming runtime adoption. Its two Docs followups are resolved: chronology identifies the then-sole comment as the historical precode checkpoint, and full MODIFIED platform-runtime requirements reconcile startup ordering and exclusive maintenance selectors. Independent source review is separate from owner execution evidence.

Rust run38430677016 executed a hosted merge bddb660 containing ac60b62f. Actual Linux Test job115411818078 logs show all five new personalization controls passing. The overall run failed: strict Build and Lint job115411818409 reports20 inherited conversation/workflow dead-code errors, and cross builds were skipped. None is in the four-file personalization delta; this is still failed required CI, not a lint waiver. The title and release-policy checks passed. Docs run38431560946 at23480d337dd3b8655adc18cae1629f40174ce22a reports success; final Docs evidence will use the delivery head after reconciliation/sync.

Initial local tested binary Git metadata honestly identified dev.v0.2.0-69-g3e87abc-dirty because compilation preceded the source commit; its source bytes match the reviewed increment. A later focused rebuild on clean committed ac60b62f passed the same five personalization controls and the actual CLI identified dev.v0.2.0-70-gac60b62 without a dirty marker. Neither artifact is a release. Final parent validation will record its actual resulting identity. Additional actual parser checks refused personalization plus a normal model override and personalization plus conversation selectors/inputs.

The reviewed three personalization requirements and two platform-runtime MODIFIED blocks are now synchronized into canonical specs. A scoped preservation check confirms the unaffected platform-runtime remainder is byte-identical, requirement headings are unique and canonical files contain no delta markers. Strict OpenSpec validation passes19/19 after adding the canonical capability; guidance/provenance validation passes. Other active Reader changes remain untouched.

Synced Docs cae70139a37815ac0711858d97c39f99ab2887bd run38432160121 passed all three jobs at hosted merge2c89aadfc710f87f84cd3b76ee69254fb63c7bfb into main7686a67. Actual strict job115416836878 logs show24/24 items (including five extra main Manager specs). Actual Windows job115416837380 logs show12 portable tests and21 current guidance files/126 preserved source blobs passing. These hosted merge counts are separate from the19-item isolated Docs source check above.

Final required hosted Rust CI and archive remain pending. Root controls final readiness; Main owns parent-first ancestry delivery. Broader REM-53/REM-42/REM-52 and unfinished active Reader specifications remain open. No whole-issue Done, release/tag or merge follows from this evidence.

Source basis: current REM-53 full requirements/all available timestamped comments, REM-36/REM-42/source/public guidance, actual isolated compiler/filesystem/CLI/Docs outputs and Root's explicit ownership/parent coordination. This is owner evidence, not independent acceptance.
