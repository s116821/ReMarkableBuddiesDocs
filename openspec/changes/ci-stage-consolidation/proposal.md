## Why

The October 15 user clarified that the earlier Things to Fix request requires a small CI graph, not merely correct dependency order. Buddy currently has eight jobs; Manager adds Windows matrix jobs. The current main implementations already use maintained semantic tooling and have removed owned source versions. Old REM-46 draft failures are preserved history, not a reason to redo that replacement.

## What Changes

- Use four Buddy jobs and five Manager jobs per application PR or main merge, counting matrix legs. The latest user direction adds a dedicated PR Title prerequisite; main merges replace Title with Release.
- Give each common check one owner in Checks. Downstream jobs depend on it instead of repeating the suite. Retain separate platform runtime integration coverage.
- Use the maintained semantic-title, path-filter, setup, artifact and release tools already selected. Keep custom logic bounded to project-specific policy and artifact identity.
- Fold candidate calculation and uploader compilation into Build, and emitted uploader/metadata Action controls into Integration.
- Keep one final publication job, exact retained artifact IDs and bytes, docs-only exclusions, and serialized application runs.
- Run the main-target PR title policy only in its prerequisite job; retain the existing standalone policy for non-main targets.
- Reconcile every existing application PR with the corrected workflow before merging it; add a job-count regression so later PRs cannot silently restore the fragmented graph.

## Scope and delivery

Buddy and Manager workflow wiring plus affected fixtures and documentation. No new release engine, SDK source/API or device change. Publish and review as a linked Docs/component delivery. Existing interrupted feature work and old drafts remain preserved during reconciliation. Verify actual required check names before removing legacy contexts; do not change repository settings without authorization.
