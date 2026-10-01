# Ecosystem guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md), [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and each selected component's AGENTS.md. Use [the manifest](repositories.json) for routing and checks.

Buddy/Manager OpenSpec artifacts and workflow assets live here. ReMarkableOpenSDK is independent and owns its own OpenSpec; cross-boundary changes coordinate exact owning revisions without duplicating SDK contracts. Follow [central workflow](openspec/README.md): proposal/design/tasks/deltas before code; linked Docs/code PRs with exact revisions and merge order; verify, sync and archive completed work only. Never archive another lane's unfinished change or label plans as implemented behavior.

The October 1 supervised lazy XOVI direction supersedes earlier categorical production bans. It is an unselected candidate: native/direct mechanisms remain preferred where robust. If required and qualified, a tiny independent Buddy Supervisor and normal runtime ship in the same Buddy repository/release/Manager installation. Stock cold boot has no injection; the first supported Buddy gesture may activate a compatibility-gated session payload with bounded health checks, crash-loop detection and automatic stock rollback. Require UI-independent disable/recovery, Manager-owned update/uninstall, and reboot to stock. After restart, discard stale handles and reacquire/validate the action's source before continuing. Never infer injection permission from read-only research or replace broad stock UI. See [active lifecycle plan](openspec/changes/native-buddy-page-creation/design.md).

Read complete public requirements and timestamped comments. Review private chronology only when available and publish material requirements. Private tools are optional. Preserve dirty clones and unfinished work; use isolated checkouts. Coordinate before creating workers or editing another lane's scope.

PR bodies are exactly `# Summary` plus concise bullets; detailed evidence, revision pairs, limits and bot responses go in comments. Use scoped semantic titles, inspect required CI and bug-bot feedback, and obtain coordinated independent review before merge. Docs never tags/builds applications; components release independently; REM-35 alone owns 1.0.

Squash merge every PR under the current user instruction, including the initial Docs migration. Do not change repository settings; the immutable migration archive preserves source evidence independently of topic history.

OpenSpec skills are in `.codex/skills/`; equivalent manual steps remain supported. Shared testing checklists are in `.agents/skills/`; run component commands from that component checkout. No tablet permission follows from setup or simulator success. Never incidentally pair/sync personal accounts or upgrade firmware. Keep secrets out of tracked files, logs and evidence; protected ignored local/environment configuration remains allowed.
