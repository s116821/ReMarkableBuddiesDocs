# Notebook archive maintenance results

Buddy candidate `69b8941ed683ad38b1b621d0f1ef56f69b052fd6` has tree
`871a4935722350d9abe115bac4c1f5128b10c674`. The local checks use the locked
dependency graph. Raw logs are retained in `work/rem52-notebook-archive-evidence`
alongside the worktrees.

The paired delivery is [Buddy #122](https://github.com/s116821/ReMarkableBuddies/pull/122)
and [Docs #133](https://github.com/s116821/ReMarkableBuddiesDocs/pull/133).
Independent review accepted the source and verified all 853 blobs in the
successful Linux source archive against the reviewed Git tree. The existing
Buddy CI runs on Linux; Windows archive evidence below comes from local host
execution. The Docs CI separately checks portability on Linux and Windows.

## Windows

- Five archive unit controls passed, covering the work and capacity limits,
  report custody, witness changes and no-clobber publication.
- The maintained maximum-size Writer test passed. It generated the notebook
  through the Store and verified archive export and detached readback.
- Seven archive CLI tests passed. They included the `LocalOnly` export and
  detached readback, refusal and compatibility controls, and Windows case alias
  refusal with byte-for-byte preservation of the owned tree.

The CLI scenario that reads an external Writer notebook asset runs on Linux.
Windows coverage uses the product Writer runner and exercises the archive CLI
separately. Windows power-loss durability remains unqualified.

## Linux

- Eight archive CLI tests passed, including the maintained scripted notebook
  scenario. The test checks the archived source, plan and stage records,
  original manifests and object bytes, detached readback, corruption and
  undeclared object refusal, and unchanged source data.
- Seven archive unit controls and the maintained maximum-size Writer test
  passed in the same run.
- The offline container ran from a Git archive of the candidate with LF
  checkout conversion pinned. The source archive SHA-256 was
  `b8861983c091c69e6e3b41ac11b22baba0550c9c05d365a7e76e54f0afa4eda0`.
  The run verified the maintained input asset hash before execution and used
  a supported local filesystem for the fixture.

## Preserved diagnostic runs

- An initial Windows build failed because the new command lacked the `Read`
  trait import. A separate maximum-size fixture run returned `Busy` while the
  fixture still owned the Store lease. The corrected fixture releases the
  result before export.
- The scripted scenario refused external input on Windows and on the first
  Linux run's overlay filesystem. On a supported local filesystem it refused
  the CRLF-converted asset because the scenario binds the original bytes. The
  final run verified the asset hash. Earlier refusals have separate logs.

## Independent review and hosted validation

Independent review accepted the corrected Windows canonical-alias admission and
the exact source/evidence pair. All 22 evidence entries and the 853 committed
blobs in the successful Linux source export were independently verified.

[Buddy CI 41855396934](https://github.com/s116821/ReMarkableBuddies/actions/runs/41855396934)
passed title, checks, build and integration at the exact candidate above. The
release job correctly skipped this PR run. Initial
[Docs CI 41855406173](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/41855406173)
passed at `dfebe666281000e735e35a8b77107b6982b185bd`; the final spec sync/archive
revision requires its own hosted Docs checks before merge.

The explicit ordinary archive requirement is synchronized into
`large-writer-notebooks` and this completed bounded change is archived in the
same paired delivery. Local tests exercise host archive behavior with fixtures
and scripted model replies; they do not establish native, restore or sync support.
