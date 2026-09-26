## 1. Preserve source and establish central authority
- [x] 1.1 Import exact main OpenSpec/archive/workflow bytes and unfinished REM-9 snapshot, with blob provenance and history instructions.
- [x] 1.2 Publish central workflow/config, public architecture/roadmap and scoped ownership; hand snapshot to parent and Manager.
## 2. Public setup and contribution
- [x] 2.1 Add repository manifest, selective portable bootstrap and manual/fork/worktree guidance.
- [x] 2.2 Test docs-only, clean clone selective paths, repeat setup, dirty clones, worktrees and invalid destinations/remotes.
- [x] 2.3 Add portable CI and validate public links, migration provenance and OpenSpec artifacts.
## 3. Coordinated migration
- [x] 3.1 Remove central-owned artifacts from Rust and update live references without changing runtime or release code.
- [x] 3.2 Prove Rust migration paths do not trigger app builds/tags; coordinate Manager pointers.
- [x] 3.3 Sync only ecosystem-contribution and archive only this completed change after its acceptance checks.
- [x] 3.4 Open linked Docs/Rust PRs with exact revisions, evidence comments and merge order; inspect required CI and bug-bot feedback for parent review.

Delivery evidence is in Docs PR #1 and Rust PR #26 comments. This checklist covers
the central migration only; Manager foundation and responsive-reader retain
separate implementation owners and acceptance gates. It does not close all of
REM-21 or REM-9. Independent coordinated review and final CI remain merge gates.
