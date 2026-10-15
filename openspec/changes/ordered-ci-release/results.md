# Ordered CI/release verification

## Exact scope and source preservation

This is the bounded Buddy/Manager/Docs implementation of the October 15 REM-56
instruction. Buddy PR46 starts at `ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`;
Manager PR19 starts at `7ff5167b0dd1dee89e0be448963940e2450feb49`; Docs PR38 starts
at `7686a67c2303cc675d544e2edf635c4f580b6a4c`. Historical REM-46 branches and failing
equal-date/security candidates are preserved. SDK release/core work is separately
owned; no native/source behavior or unfinished parent stack is imported here.

Buddy's Cargo dependency lock and SDK identity are unchanged. Its own maintained
package version is omitted, while Cargo's generated lock identity remains
unchanged. Manager removes only its own package/root-lock version fields; its
dependency graph, UI, host implementation and existing host tests are unchanged.
Build metadata adds a controlled candidate profile without changing the existing
four-field Manager wire schema. Unmerged Manager consumers that hash-import the
removed coordinator require explicit parent reconciliation before adoption.

## Requirement, implementation and evidence mapping

| Requirement/scenario | Implementation and focused evidence |
| --- | --- |
| Semantic selection, equal dates, breaking 0.x | Pinned Python Semantic Release 10.7.0, identical conventional-monorepo parser options and real disposable Git histories in `release/test_semantic_tools.py`. No private version arithmetic/history coordinator or maintained source version. REM-35 still refuses premature 1.0. |
| Misclassified application source | PR-title Action checks and `semantic_source.validate_source` independently parse the actual admitted main commit's exact GitPython message before build and final tag. An earlier untagged feat cannot authorize a current docs/unsupported/unscoped/leading-space subject. |
| Docs/mixed/unknown paths | Actual pinned dorny Action controls use `predicate-quantifier: every`; docs, mixed, executable, unknown, rename and later-page PR fixtures plus a real push base/ref fixture are covered. PSR docs-feat history does not inflate the next candidate. |
| Ambiguous push admission | `admission.py range` requires one known forward first-parent commit. A real edit/revert batch with net-zero diff and a zero-before range refuse before build/tag. Final GraphQL proof binds the exact source to a merged-main PR, including squash. Structural admission alone does not validate its message. |
| Gates and no early official tag | Metadata/checks -> read-only candidate -> build -> downloaded-artifact integration -> one main-only publish job. Action controls inspect DAG/failure/skip behavior; real PSR controls prove candidate reads do not create tags. Final publish is skipped in actual PR runs. |
| Exact artifacts and version | Build artifact IDs flow directly to integration and final publish. Fixed inventory, source/version and hashes are verified before/after integration. Buddy executes extracted binaries in pinned emulation images without Cargo/source mounts. Manager stages retained browser/native ZIPs and runs existing browser/Electron/packaged/wired fixtures without application rebuilding. |
| Preserved development coverage | Manager builds its preexisting development configuration under the same frozen profile, retains a separate CI-only artifact and exercises `tests/hosts.mjs --development` on Linux and Windows. It is absent from the production release inventory. |
| Failure, queue and retry | Native `queue: max`, no cancel-in-progress, exact SHA/candidate rechecks and explicit failed-job retry. Real histories preserve failed sources without backfill; later-main fixtures cannot retarget the admitted source. Retained-asset controls compare independent expected bytes, upload only missing names and refuse corruption/conflicts. |
| Maintained publication | Exact GraphQL/request Actions perform metadata operations. The source-built unchanged Svenstaro Action gets exact ID, only missing files, overwrite/promote false and draft true. Same-ID/all-byte proof precedes final PATCH. Actual Action controls cover partial draft recovery, list-time duplicate refusal, missing-ID replacement refusal and upload failure with retained assets. |
| Docs ordering and canonical reconciliation | Portable checks precede strict OpenSpec with read-only permissions. Only owned release-versioning, Manager artifact and runtime-version requirement blocks are synced; unrelated active changes and canonical requirements remain untouched. |

## Owned local controls

- Seven maintained PSR CLI/Git controls passed in 66.964 seconds. The added exact
  source-message masking regression passed in 10.728 seconds, including the raw
  leading-space case; only that new case was rerun after its input changed.
- Four guard/retained-byte controls passed in 1.287 seconds. Their asset unit uses
  a controlled verifier callback; it is not the actual package-consumption proof.
- Buddy build-metadata fixture passed in 37.169 seconds; local strict Clippy/fmt
  passed. Manager lint, 14 Angular units (2.652 seconds) and version tests passed
  using supported Node 24.21.0. Required hosted suites provide final full-head
  integration evidence separately below.
- Four actual upstream metadata-Action controls passed in 6.593 seconds after an
  initial harness setup failure was corrected. Four actual emitted uploader
  controls passed in 3.148 seconds. Those uploader controls have tool-output
  evidence, not a separately saved independent local execution receipt.

## Uploader source, audit and limitations

The maintained Svenstaro 2.11.5 source is
`29e53e917877a24fad85510ded594ab3c9ca12de`. Selected lock SHA-256 is
`40d12ef759acb50abe1245b46e7cab3ca13ecad579bdb7925ff3f59ad68ef84b`;
emitted bundle is `379dc8bce8a264c2f2badae81199160fbd485ef118d63ade01fd2113a2e1b2bc`;
provenance is `fbedae0c3a6db07b97164ba861321eb9781d5f8b02f5a52d66a32f2904b81f46`.
The selected recipe uses only needed supported runtime/build dependencies, retaining
unchanged upstream source, Action metadata, TypeScript config and license. It
transparently omits the empty Jest placeholder and unused test/lint graph. Its
full selected closure scan reports zero known advisories at qualification time.
The original/range-refresh/Jest30 closures remain failed with 41/34/20 advisories;
neither the original upstream suite nor aggregate security cleanliness is claimed.

The duplicate control inserts at asset-list time, not an executed upload-time 422
race. Unchanged source performs no DELETE with overwrite false. Upstream ID404
can create a replacement draft; final same-ID proof refuses its finalization.
An outside writer may publish concurrently and upstream may restore draft status.
There is no atomic/external-writer guarantee. Queue order is arrival order, not
guaranteed dispatch chronology. Conflicting candidates/assets refuse.

## Hosted evidence and current gates

Initial Buddy head `925f70afe393841e270b6b7cd9e19ba31c2d720f` completed
[CI38705897947](https://github.com/s116821/ReMarkableBuddies/actions/runs/38705897947)
on hosted merge `998095b7f0d8656641127b0a5d208a94a73c172f`. Checks, uploader,
candidate, both target builds and retained-artifact integration passed. Artifact
`11958329873` was downloaded by ID and both extracted binaries reported 0.2.1;
the output explicitly says emulation only/native unqualified. Final publish skipped.

Initial Manager head `46019e36b15ea6aa75a167b946c8e174d2e2d37a` completed
[CI38705913084](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38705913084)
on hosted merge `4802ac719a9fda0f4462d6a5269696b9b1839541`. Both native-host
integrations consumed artifact `11958482457`, staged retained ZIPs, exercised
browser/Electron/packaged/wired fixture paths and reverified unchanged archives.
They reported 0.4.1; Linux's native-adapter fixture and Windows's unsupported
adapter path are synthetic host evidence, not tablet qualification. Final publish skipped.

Initial Docs head `7cdc96b153ac60fb8c1f9a6ec3f067c0c6577f5e` completed
[CI38705950972](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/38705950972)
with both portable jobs then strict OpenSpec (21 items passed). These initial
successes are not final-head acceptance: subsequent exact-source eligibility,
restored development artifact coverage and canonical lifecycle edits require
their own final checks/readback. Final revision/CI and independent review addenda
will be recorded before this named change is archived.

## Remaining ecosystem limits

No production tag/release/settings experiment or tablet/provider/account operation
was performed. This delivery does not qualify native compatibility, real provider
behavior, installation, full lifecycle under host loss, external-writer atomicity,
SDK's separate release selection or REM-35/46/50 completion. Root owns the final
cross-repository readiness and human-note update after verified ecosystem delivery.

Source basis: current human instruction and REM-56 chronology; exact repository
source and retained failed candidates; current local tool outputs; actual hosted
job logs linked above; maintained upstream source/official command contracts.
