# CI stage consolidation: review package

Status: prepared for linked review; implementation and current-PR reconciliation are not yet accepted. None of the 37 inventoried application PR branches has been updated by this delivery. Tracking scope remains REM-46, with REM-56's shipped ordering and release behavior preserved.

| Repository | Running PR jobs | Running main-merge jobs |
|---|---:|---:|
| Buddy | 3 | 4 |
| Manager | 4 | 5 |

Counts include matrix legs. PRs skip the final Release job. Documentation-only changes run metadata checks without entering the application release queue.

Checks now includes path/title admission and source checks. Build contains read-only candidate calculation, pinned uploader compilation and the existing application build. Integration consumes exact retained artifacts; Manager keeps Linux and Windows integration. Release preserves the current publisher and never rebuilds. Manager's Linux source checks run at the beginning of Build before candidate calculation or compilation; Windows source checks remain in Checks.

## Evidence

- Eight focused structural tests pass: exact job budgets, platform coverage, dependency/failure gates, docs-only behavior and retained-artifact publication.
- The preparation script deep-compares the entire final publisher after reversing the mechanical output-owner renames; it also confirms unchanged original integration steps and concurrency.
- Strict OpenSpec validation passed with exit 0. Its optional telemetry flush failed because network resolution is unavailable; that did not fail validation.
- Actionlint 1.7.12 found only the two existing `concurrency.queue: max` compatibility warnings. No new lint findings. This is not a clean actionlint result.
- The Windows Bash first-failure execution control was attempted but cannot run under this sandbox. It remains mandatory on a permitted runner.
- The six existing real Action controls were attempted but could not complete: subprocess localhost connections returned EACCES, and temporary Git config writes were denied. They are not passing evidence. Uploader loopback controls were not repeated after that shared restriction was established.
- Hosted CI and independent review remain pending. No application/hardware qualification is claimed from this YAML preparation.

## Review files

Source revisions are in [source-manifest.json](source-manifest.json). The [open PR inventory](open-pr-reconciliation.md) identifies every observed branch and the extra Manager controls that must survive reconciliation. Active proposal/design/tasks/spec delta are under `openspec/changes/ci-stage-consolidation/` in this prepared Docs tree.

At the review package root, `candidate/` holds both component candidates, `baseline/` holds the exact changed-file baselines, `prepare.mjs` reproduces workflow transformations and checks preservation, and `patches/` holds three reviewable repository patches. Package support files copied to candidate for tests are unchanged and excluded from the component patches.

## Remaining delivery

Check required branch-protection contexts before removing/renaming a required job. The current settings could not be read here, and no settings have been changed. Complete independent review and hosted checks, publish linked Docs/component PRs, sync/archive only accepted work, then reconcile every retained open application PR with the corrected main and recheck the inventory.

Initial publication was denied by this chat's approval policy. After the human changed access and requested a fresh check, the GitHub connector successfully created `codex/rem46-compact-ci-20261015` from the exact Docs main. This does not establish hosted CI, review, merge or reconciliation of the inventoried PRs; those remain explicit delivery gates.

Source basis: direct October 15 human instructions; current GitHub workflow sources, run job list and open-PR trees; current Linear/Mem chronology read before preparation; local checks described above. Prior tablet memory is not evidence for these CI claims.

