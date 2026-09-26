# Source provenance

The [source-provenance manifest](source-provenance.json) records 126 original source paths, their source commits, Git blob IDs and migrated destinations. The immutable [compressed blob archive](imported-blobs.zip) preserves their 113 unique byte sequences, keyed by Git blob ID. This is historical evidence, not a second normative OpenSpec tree. Later live workflow/config/active-change edits or deletions do not change this evidence.

- [Rust main](https://github.com/s116821/ReMarkableBuddies/tree/33db26add721cea6c0121ad769a54d06ae600b4e): canonical specs, archives, config, all OpenSpec and testing workflow assets.
- [Unfinished REM-9](https://github.com/s116821/ReMarkableBuddies/tree/da8838db9863d504b12b5e8b44a3015af9ded0cd/openspec/changes/responsive-reader): active responsive-reader snapshot and unchecked tasks, later rescoping owned by its task.

Source history/branches were not rewritten. Clone full Rust history and run `git log SOURCE_SHA -- SOURCE_PATH` or `git show SOURCE_SHA:SOURCE_PATH` for prior authorship and revisions. For offline validation, run `python scripts/check_docs.py` or `python scripts/provenance.py`: these verify the manifest's archive SHA-256, exact member inventory and every original Git blob hash without Git history or network access. Shallow clones and source ZIP downloads work. The former topic import commit is not required to remain reachable.

To retrieve original bytes, find the desired source path's `blob` value in the manifest, then run `python scripts/provenance.py BLOB NEW_OUTPUT_FILE`. The command validates evidence first and refuses to overwrite an existing output. Python's standard ZIP reader also opens the archive; its members are blob IDs, not executable workflow paths. Keep this archive/manifest immutable when current artifacts evolve.

**Current merge policy:** squash merge every PR, including the initial Docs migration, after authorized review and CI. This latest user instruction supersedes the withdrawn merge-commit-only proposal. No repository settings, permanent tags or special refs are needed to preserve provenance.

Historical archive wording is evidence, not current workflow authority. Follow [central workflow](../../openspec/README.md) and [roadmap](../roadmap.md). This migration syncs/archives only its completed central workflow scope; other active changes retain their owners and acceptance gates.
