# Ecosystem guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md), [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and each selected component's AGENTS.md. Use [the manifest](repositories.json) for routing and checks.

All OpenSpec artifacts and workflow assets live here exclusively. Follow [central workflow](openspec/README.md): proposal/design/tasks/deltas before code; linked Docs/code PRs with exact revisions and merge order; verify, sync and archive completed work only. Never archive another lane's unfinished change or label plans as implemented behavior.

Read complete public requirements and timestamped comments. Review private chronology only when available and publish material requirements. Private tools are optional. Preserve dirty clones and unfinished work; use isolated checkouts. Coordinate before creating workers or editing another lane's scope.

PR bodies are exactly `# Summary` plus concise bullets; detailed evidence, revision pairs, limits and bot responses go in comments. Use scoped semantic titles, inspect required CI and bug-bot feedback, and obtain coordinated independent review before merge. Docs never tags/builds applications; components release independently; REM-35 alone owns 1.0.

OpenSpec skills are in `.codex/skills/`; equivalent manual steps remain supported. Shared testing checklists are in `.agents/skills/`; run component commands from that component checkout. No tablet permission follows from setup or simulator success. Never incidentally pair/sync personal accounts or upgrade firmware. Keep secrets out of tracked files, logs and evidence; protected ignored local/environment configuration remains allowed.
