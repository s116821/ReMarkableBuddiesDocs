# CI stage consolidation: review package

Status: the main CI implementation has exact-head independent source/spec acceptance and successful final Buddy, Manager and Docs CI. Its canonical requirement is synced and the completed implementation is archived. Normal merges, actual-main publication and current-PR reconciliation remain open in `ci-existing-pr-reconciliation`. None of the 37 inventoried application PR branches has been updated. REM-46 remains open; REM-56's shipped release behavior is preserved.

| Repository | Running PR jobs | Running main-merge jobs |
|---|---:|---:|
| Buddy | 4 | 4 |
| Manager | 5 | 5 |

Counts include matrix legs and exclude skipped jobs that allocate no runner. The latest human clarification adds a dedicated PR Title prerequisite, increasing the earlier PR count by one. Main merges skip PR Title; PRs skip Release. Documentation-only changes run metadata checks without entering the application release queue.

PR Title performs semantic-title admission before Checks. Common lint/unit, release-policy, workflow and Python/fixture dependency audits run once in Checks on Linux. Build contains read-only candidate calculation, pinned uploader compilation and the application build. The uploader recipe retains its single build-time dependency audit. Integration consumes exact retained artifacts; Manager keeps distinct Linux and Windows runtime checks without repeating the common source suite. Release preserves publication safeguards and never rebuilds. Downstream hash-locked tool installation does not repeat the dependency audit already owned by Checks.

## Evidence

- Ten focused structural tests pass: job budgets, title prerequisite, platform coverage, one owner per common suite, dependency/failure gates, docs-only behavior and retained-artifact publication.
- The preparation script compares the final publisher after reversing mechanical output-owner renames and the deliberate downstream-audit opt-out; existing original integration steps and concurrency are preserved.
- Strict OpenSpec validation passed with exit 0. Its optional telemetry flush failed because network resolution is unavailable; that did not fail validation.
- Actionlint 1.7.12 found only the two existing `concurrency.queue: max` compatibility warnings. No new lint findings. This is not a clean actionlint result.
- The Windows Bash first-failure execution control was attempted but cannot run under this sandbox. It remains mandatory on a permitted runner.
- The six existing real Action controls were attempted but could not complete: subprocess localhost connections returned EACCES, and temporary Git config writes were denied. They are not passing evidence. Uploader loopback controls were not repeated after that shared restriction was established.
- Manager's final revision `678b6d406d23131c151e280ba40f56f2e38ec33c` passed all five PR jobs in [run 38831149009](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38831149009): PR Title, Checks, Build, Linux Integration and Windows Integration. Release was correctly skipped. These hosted jobs include the actual Action/uploader controls and Windows first-failure control that the local sandbox could not execute.
- Buddy's final revision `798cbe398b31d11a1f1fe6a562abe9846799f232` passed all four PR jobs in [run 38831146595](https://github.com/s116821/ReMarkableBuddies/actions/runs/38831146595), including Build116752380546 and Integration116759450069. Release correctly skipped. These are actual final-head results, not an older revision or a restarted queue.
- Main independently reviewed all nineteen changed component/Docs blobs, complete publisher equality after mechanical owner normalization, original integration steps, actual Action controls and concurrency. Exact reviews: [Buddy5541792700](https://github.com/s116821/ReMarkableBuddies/pull/59#pullrequestreview-5541792700), [Manager5541792787](https://github.com/s116821/ReMarkableBuddiesManager/pull/23#pullrequestreview-5541792787) and [Docs5541792871](https://github.com/s116821/ReMarkableBuddiesDocs/pull/53#pullrequestreview-5541792871). They found no source/spec issues; the original Buddy CI hold was subsequently satisfied. The lifecycle-only Docs revision still needs its final review/checks.
- Earlier drafts exposed a removed YAML helper still used by an existing Action control; it was restored, and ESLint passed for both changed fixture files. The final twelve changed component files were read back from GitHub and all Git blob hashes matched the prepared local bytes.

## Review files

Source revisions are in [source-manifest.json](source-manifest.json). The [open PR inventory](open-pr-reconciliation.md) identifies every observed branch and its feature controls. The verified main implementation is under `openspec/changes/archive/2026-10-15-ci-stage-consolidation/`; its unfinished dependent rollout remains under `openspec/changes/ci-existing-pr-reconciliation/`. This split preserves the required main-first merge order without archiving unfinished branch updates.

At the review package root, `candidate/` holds both component candidates, `baseline/` holds the exact changed-file baselines, `prepare.mjs` reproduces workflow transformations and checks preservation, and `patches/` holds three reviewable repository patches. Package support files copied to candidate for tests are unchanged and excluded from the component patches.

## Remaining delivery

Current GitHub branch metadata for all three repositories has empty required-status contexts, and Buddy's active Main Rules has no required-status-check rule. No settings have been changed. Complete the lifecycle-only final review/checks, squash merge the accepted core, verify actual-main publication, then reconcile every retained open application PR and recheck the inventory. Do not close REM-46 until that rollout is complete.

The rollout preview review found missing native Windows coverage when the old cross-platform source suite moved to Linux Checks. The prepared Manager PR21/22 previews now retain the three WindowsNative tests and the Drive NTFS refusal in the existing Windows Integration leg. Their guard permits only the exact selected Windows commands and rejects broad, ungated or mixed common-suite discovery. Each preview passed six static controls and its separate Git Bash first-failure control; the earlier WSL launcher failure is retained, not relabeled. Actual selected native execution against PR21 passed three wired tests and one Drive NTFS test on BYORBSAX. No tablet or host route was changed, and no feature branch was updated by this preparation.

Linked delivery: [Docs PR53](https://github.com/s116821/ReMarkableBuddiesDocs/pull/53), [Buddy PR59](https://github.com/s116821/ReMarkableBuddies/pull/59) at `798cbe398b31d11a1f1fe6a562abe9846799f232`, and [Manager PR23](https://github.com/s116821/ReMarkableBuddiesManager/pull/23) at `678b6d406d23131c151e280ba40f56f2e38ec33c`. Exact Docs/code revision sets and subsequent hosted evidence are recorded in the PR comments. Publication does not establish acceptance, merge or reconciliation of the inventoried PRs.

Source basis: direct October 15 human instructions; current GitHub workflow sources, run job list and open-PR trees; current Linear/Mem chronology read before preparation; local checks described above. Prior tablet memory is not evidence for these CI claims.

