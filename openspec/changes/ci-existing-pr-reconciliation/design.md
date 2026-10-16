## Delivery order and ownership

Root owns coordinated CI delivery and the existing-PR rollout. Main independently reviewed the compact core. Merge the accepted core normally, then reconcile retained feature branches against that main. Refresh each head before updating it; preserve dirty worktrees and moving remote branches. Use isolated checkouts and ordinary non-forced updates.

Keep each feature's common source suites in Checks and supported-platform runtime controls in Integration. Manager PR21/22 require three WindowsNative cases from tests/wired/test_windows.py and the Windows-only NTFS grant refusal in tests/drive/test_store.py. These tests skip on Linux and cannot be replaced by Node host fixtures. Invoke only these selected cases on Windows; broad unittest discovery remains in Checks. The duplicate-suite guard must allow these exact Windows-gated selections while rejecting broad discovery, wrong-platform or mixed common-suite steps.

Read-only merge previews identify unrelated Rust conflicts in older Buddy branches and CI-only conflicts in retained Manager branches. Do not resolve a feature conflict by copying either entire source tree. Preserve released fixes, accepted feature behavior and source/test ownership, and obtain scoped review of any necessary resolution. A local preview is not a published branch or actual hosted pass.

The main pipeline remains four Buddy/five Manager running jobs on PRs and main merges. Title precedes Checks on PRs; Release follows Integration only on eligible main. Existing inherited publisher and retained artifacts remain unchanged. Recheck all open PRs after rollout, including newly created or advanced heads, before claiming completion.

## Existing consumer compatibility repair

Actual compact CI on Manager PRs13–18 exposes an obsolete `coordinator.archive_package` fixture import and runtime verifier coupling. Reuse the already reviewed PR21 commit973585003405e303cb555d91eca5a33c294e73ff current-producer repair: exact hash-qualified pure identity helper, current archive fixture and bounded consumer verification. Preserve tampered-helper refusal and add the existing current-only runtime control. Port packaging/download assertions only where that feature already exists; do not introduce later UI features into earlier branches. Keep workflow/job ownership unchanged, preserve original failed runs, inspect each source delta and verify relevant host/CI behavior before acceptance. This is compatibility with the delivered release contract, not whole-feature acceptance.

Carry the useful draft2 generated-dependency ignores through Manager24. Preserve both superseded draft heads and original failed GitVersion evidence when closing them; do not import old release-engine wiring or promote historical device authorizations. The central docs-layout instruction comes from the current human instruction, not new native permission.
