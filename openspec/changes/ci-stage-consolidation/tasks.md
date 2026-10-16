## Preparation
- [x] Read current issue requirements, original cleanup contract, current main workflow sources and actual completed job list.
- [x] Specify consolidation before changing workflow files.

## Local candidate verification
- [x] Consolidate both application workflows into four logical stages without removing existing main coverage.
- [x] Preserve the existing publisher, integration steps, exact artifact/tool/source/version handoffs and docs-only behavior.
- [x] Enforce Buddy 3 PR / 4 main and Manager 4 PR / 5 main running jobs, counting matrix legs; eight local structural controls pass.
- [x] Add the Windows native-command failure control; its local execution is unverified because Bash cannot run in this sandbox.
- [x] Attempt existing Action controls and record sandbox failures: localhost connections and temporary Git config writes were denied. No execution PASS is claimed.
- [x] Run actionlint 1.7.12: only two inherited queue:max syntax findings; no other findings. Retain the existing serialization contract.
- [x] Validate the new OpenSpec change with strict validation.
- [x] Inventory all 37 open application PRs at exact heads and identify Manager feature-specific controls that must survive reconciliation.

## Delivery and acceptance still pending
- [ ] Verify protected required-status contexts before renaming/removing them; preserve protection without changing repository settings.
- [ ] Obtain independent review and pass actual hosted/platform CI on the final candidate.
- [ ] Publish linked Docs/component PRs; sync canonical specs and archive only after acceptance; squash merge normally.
- [ ] Reconcile all current application PRs against the corrected main, preserve each feature's tests and source, and validate the effective merged workflows.
- [ ] Recheck for newly opened or changed PRs and close the cleanup only after every retained PR satisfies the job budget.
