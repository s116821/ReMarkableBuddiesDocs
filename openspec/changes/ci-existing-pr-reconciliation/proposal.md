## Why

The human requires the compact CI contract in every current application PR so later feature merges cannot restore fragmented jobs. The accepted main implementation must merge first; this dependent rollout remains unfinished and is not closed by the implementation archive.

## What Changes

- Incorporate the accepted main CI/release wiring into every retained Buddy and Manager PR while preserving feature source and required checks.
- Keep Windows-only native API and NTFS custody tests in the existing Windows Integration execution; run common suites once in Linux Checks.
- Preserve all earlier failures and superseded drafts until their useful work is accounted for. Resolve CI conflicts explicitly; unrelated feature conflicts remain visible and must not be silently overwritten.
- Verify final main publication, refresh changing PR heads and the inventory, and record actual branch/CI results before closing the cleanup.

## Scope

REM-46 follow-through for the archived ci-stage-consolidation implementation. No new release engine, device operations, repository settings change or feature acceptance. The initial 37-PR inventory lives in docs/ci-stage-consolidation/open-pr-reconciliation.md.
