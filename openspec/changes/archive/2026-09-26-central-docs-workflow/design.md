# Design

## Context and authority

The September 26 explicit resume instruction overrides component-local OpenSpec text in older REM-21/roadmap descriptions and comments. Three repositories remain separate. Source baseline is Rust main 33db26add721cea6c0121ad769a54d06ae600b4e; unfinished responsive-reader source is da8838db9863d504b12b5e8b44a3015af9ded0cd. Both source histories remain unmodified.

## Decisions

1. Preserve original relative OpenSpec paths, archive dates and byte contents on import. Record repository, source commit, source path, Git blob and destination for every imported file in a checked-in provenance manifest. Retain source-history links and verification commands rather than rewrite or graft unrelated histories. Config and guidance may subsequently change with ordinary visible commits; imported canonical/archive content stays exact.
2. All OpenSpec config, canonical specs, changes, archives and workflow skills live in Docs only. Also move shared testing workflow guidance to Docs and make its execution root explicit. Component AGENTS files link central workflow and retain component commands. Parent owns responsive-reader after the snapshot; Manager owns manager-foundation. REM-21 must not sync or archive either unfinished change.
3. Use one versioned JSON repository manifest. A Python 3 standard-library bootstrap is portable to Windows, macOS and Linux and requires only Git. Default is list/docs-only; explicit component selection or --all clones only needed repositories. Existing paths must be exact clone/worktree roots with the expected upstream or explicit fork remote. Never fetch, reset, checkout, clean, install, run hooks or modify existing repositories. Refuse collisions and mismatched roots. Allow explicit paths and URL overrides for manual layouts/forks. Fail before cloning if any requested destination is invalid.
4. Keep independent component release sources in the manifest. Compatibility is a separately versioned contract description; version numbers need not match. REM-36/41 own implemented schemas and transport. Publish no unsupported compatibility promises.
5. Commit proposal/design/tasks/deltas before implementing. Use linked Docs plus implementation PRs, exact revisions, per-repo checks and explicit merge ordering. Docs import merges first, Rust removal next, Manager pointers after central targets exist. Rebase and verify later component work against the combined state. No automatic merging or tagging.

## Risks and mitigations

- Migration omissions: enumerate every tracked OpenSpec and workflow asset and compare source blobs, including REM-9 active files.
- Stale local references: search live guidance/scripts and change links; archives retain historical wording as evidence.
- Existing contributor work: test dirty clones, linked worktrees, incorrect remotes, nested destinations, repeated setup and fork overrides; no destructive operations.
- Releases: inspect current policy and evaluate all changed Rust paths as documentation-only; do not modify runtime or release machinery.
- Partial linked merges: Docs is additive first; removal requires reachable central content. Keep exact source provenance for recovery.

## Validation

Run bootstrap integration tests using temporary local Git repositories, actual clean public Docs clone flows selecting Rust and Manager, repeat/dirty/worktree checks on Windows, OpenSpec strict validation, link/path and provenance checks, and Rust release-policy classification. CI repeats portable tests on Windows and Linux. Hardware and model behavior are unchanged and untested in this lane.
