# Source provenance

Import commit `dd9d5e189dc0b901e54396e1cd8bc7ea9393ceac` preserves 126 exact Git blobs enumerated in [source-provenance.json](source-provenance.json). Each entry records source commit/path/blob and destination. Later deliberate live workflow/config/active-change edits remain normal visible history.

- [Rust main](https://github.com/s116821/ReMarkableBuddies/tree/33db26add721cea6c0121ad769a54d06ae600b4e): canonical specs, archives, config, all OpenSpec and testing workflow assets.
- [Unfinished REM-9](https://github.com/s116821/ReMarkableBuddies/tree/da8838db9863d504b12b5e8b44a3015af9ded0cd/openspec/changes/responsive-reader): active responsive-reader snapshot and unchecked tasks, later rescoping owned by its task.

Source history/branches were not rewritten. Clone full Rust history and run `git log SOURCE_SHA -- SOURCE_PATH` or `git show SOURCE_SHA:SOURCE_PATH` for prior authorship and revisions. Docs `git show dd9d5e189dc0b901e54396e1cd8bc7ea9393ceac:DESTINATION` retrieves original bytes. `python scripts/check_docs.py` validates source blob identity against that import commit, not perpetually frozen working files. CI needs full history (`fetch-depth: 0`).

**Initial migration merge requirement:** Docs PR #1 must use a history-preserving merge commit (`gh pr merge 1 --merge` after authorized review/CI), not squash or rebase, so the import commit remains reachable from main and fresh clones. This one-time provenance requirement is explicitly coordinated; repository merge settings are unchanged. Rust and later component PRs retain their normal semantic squash/release behavior. A later change to import-history retention must update and test the verifier first.

Historical archive wording is evidence, not current workflow authority. Follow [central workflow](../../openspec/README.md) and [roadmap](../roadmap.md). This migration syncs/archives only its completed central workflow scope; other active changes retain their owners and acceptance gates.
