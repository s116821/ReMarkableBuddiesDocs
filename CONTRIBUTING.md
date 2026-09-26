# Contributing

Public GitHub issues/PRs and these requirements suffice. Route UI work to Manager, tablet behavior to Rust, and requirements/cross-component work to Docs using [manifest URLs](repositories.json). Use public issues for discussion. A task owner edits its named change and implementation; the maintainer reviews contracts and coordinates merges. Publish acceptance decisions without requiring private tools.

## Docs-only starting point

Install Git and Python 3.11+ using normal platform tools; no Python packages are needed.

```text
git clone https://github.com/s116821/RemarkableBuddiesDocs.git
cd RemarkableBuddiesDocs
python scripts/workspace.py
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

Windows may use `py -3` instead of `python`. Commands work in PowerShell, cmd, bash and zsh. Quote paths with spaces. No shell scripts, private integrations or tablet are required. Setup never installs packages or accesses hardware.

Select only what the task needs; default component destinations are siblings of Docs:

```text
python scripts/workspace.py rust --dry-run
python scripts/workspace.py rust
python scripts/workspace.py manager
python scripts/workspace.py --all
```

No arguments lists the directory without cloning. Docs tasks require no components. Rust tasks read its AGENTS.md and local-development guide, install Rust stable, then run manifest checks from Rust. Manager tasks read its AGENTS.md/README for supported Node, run `npm ci` then `npm run check` from Manager. Until a pending foundation PR merges, use its reviewed branch for new commands rather than assuming old main contains them.

## Existing clones, worktrees and forks

Default sibling roots are discovered automatically. Supply explicit paths for custom layouts and linked worktrees:

```text
python scripts/workspace.py rust --path "rust=C:/work/reader task"
python scripts/workspace.py manager --workspace "C:/work/companions"
python scripts/workspace.py rust --url rust=https://github.com/YOUR-NAME/ReMarkableBuddies.git
python scripts/workspace.py rust --path "rust=C:/work/my-fork" --url rust=https://github.com/YOUR-NAME/ReMarkableBuddies.git
```

Any remote matching canonical upstream or the explicit override permits reuse, including a fork with an `upstream` remote. Git detects linked worktrees with `.git` files. Setup never fetches, changes branches, resets, cleans or modifies existing work, including dirty clones. All selected paths are checked before cloning. Unrelated directories, nested repository paths, overlapping destinations and wrong remotes fail without overwriting anything. Network failure can leave an incomplete new clone; inspect it or use a new destination. Setup never deletes directories.

Manual equivalents are ordinary `git clone URL PATH`, `git remote add upstream CANONICAL_URL`, and `git worktree add -b TOPIC PATH BASE`. Select BASE explicitly from the intended reviewed branch; never overwrite a dirty checkout. Fork PRs and local checks require no canonical write access.

## Routing and linked delivery

| Task | Repositories | Central change |
| -- | -- | -- |
| Docs correction | Docs | Update guidance; behavioral changes need full proposal |
| Rust-only behavior | Docs + Rust | Relevant tablet/reader/platform capability |
| UI-only behavior | Docs + Manager | Manager capability and applicable install/management change |
| Cross-component contract | Docs + affected components | One agreed owner and linked PRs |

Read full task/comment chronology, then [propose in Docs](openspec/README.md) before implementation. Link one change ID from all PRs. Record exact spec/code SHAs, checks/results, remaining gates, owners, compatibility and merge order in comments. PR body is exactly `# Summary` plus concise bullets; scoped semantic titles follow component policies (`docs(REM-21): ...` for migration). Descriptive scopes work without private tickets.

Linked Docs and code PRs form one reviewed delivery, not a separately completed planning prerequisite. Verify implementation, sync canonical contracts, then archive only completed changes. Rebase dependent work and repeat affected integration checks. Migration order: additive Docs first, Rust removal second, Manager pointers after central paths exist. REM-35 alone authorizes the integrated 1.0 gate.

Current user policy is to **squash merge every PR**, including the initial Docs migration, until explicitly changed. [Preserved source evidence](docs/migration/README.md) is independent of topic-branch history and remains verifiable in a shallow clone after squash. Do not change repository settings to enforce or bypass this instruction.

Documentation changes need working examples/checks, not paid model or native runs. Use the shared [simulator checklist](.agents/skills/reader-simulator-testing/SKILL.md) and, only for authorized idle hardware, [tablet checklist](.agents/skills/reader-buddy-testing/SKILL.md) for relevant implementation changes. Label offline, live-model and native evidence separately; unavailable native checks remain maintainer gates. Preserve source documents and secrets. See [licensing](docs/licensing.md).
