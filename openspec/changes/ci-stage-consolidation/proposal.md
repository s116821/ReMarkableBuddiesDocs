## Why

The October 15 user clarified that the earlier Things to Fix request requires a small CI graph, not merely correct dependency order. Buddy currently has eight jobs; Manager adds Windows matrix jobs. The current main implementations already use maintained semantic tooling and have removed owned source versions. Old REM-46 draft failures are preserved history, not a reason to redo that replacement.

## What Changes

- Limit running application jobs to three or four on PRs and four or five on main merges, counting matrix legs. Buddy uses Checks, Build, Integration and Release. Manager uses one Checks job, one Build job, two platform Integration jobs and Release.
- Fold path/title admission and workflow wiring checks into Checks, candidate calculation and uploader compilation into Build, and emitted uploader/metadata Action controls into Integration.
- Keep one final publication job, exact retained artifact IDs and bytes, docs-only exclusions, and serialized application runs.
- Remove duplicate title-only workflow runs after preserving their checks in Checks.
- Reconcile every existing application PR with the corrected workflow before merging it; add a job-count regression so later PRs cannot silently restore the fragmented graph.

## Scope and delivery

Buddy and Manager workflow wiring plus affected fixtures and documentation. No new release engine, SDK source/API or device change. Publish and review as a linked Docs/component delivery. Existing interrupted feature work and old drafts remain preserved during reconciliation. Verify actual required check names before removing legacy contexts; do not change repository settings without authorization.
