# Ecosystem guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md), [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and each selected component's AGENTS.md. Use [the manifest](repositories.json) for routing and checks.

All OpenSpec artifacts and workflow assets live here exclusively. Follow [central workflow](openspec/README.md): proposal/design/tasks/deltas before code; linked Docs/code PRs with exact revisions and merge order; verify, sync and archive completed work only. Never archive another lane's unfinished change or label plans as implemented behavior.

Read complete public requirements and timestamped comments. Review private chronology only when available and publish material requirements. Private tools are optional. Preserve dirty clones and unfinished work; use isolated checkouts. Coordinate before creating workers or editing another lane's scope.

PR bodies are exactly `# Summary` plus concise bullets; detailed evidence, revision pairs, limits and bot responses go in comments. Use scoped semantic titles, inspect required CI and bug-bot feedback, and obtain coordinated independent review before merge. Docs never tags/builds applications; components release independently; REM-35 alone owns 1.0.

Squash merge every PR under the current user instruction, including the initial Docs migration. Do not change repository settings; the immutable migration archive preserves source evidence independently of topic history.

OpenSpec skills are in `.codex/skills/`; equivalent manual steps remain supported. Shared testing checklists are in `.agents/skills/`; run component commands from that component checkout. No tablet permission follows from setup or simulator success. Never incidentally pair/sync personal accounts or upgrade firmware. Keep secrets out of tracked files, logs and evidence; protected ignored local/environment configuration remains allowed.

Keep simulator and SDK fixtures improving in parallel with bounded, authorized native experiments. Incomplete modeled coverage does not block exploratory hardware observations. Resolve concrete defects threatening the exact run or independent rollback first, then freeze and isolate experimental inputs from continuing fixture work. Preserve unfinished coverage and feed hardware findings back into the model. Clearly mark exploratory evidence as unqualified; required source, native, merge and release verification remains in force. Ordinary repository files and CLI tools are sufficient for this workflow.
