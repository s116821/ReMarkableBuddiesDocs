# Ecosystem guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md), [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and each selected component's AGENTS.md. Use [the manifest](repositories.json) for routing and checks.

All OpenSpec artifacts and workflow assets live here exclusively. Follow [central workflow](openspec/README.md): proposal/design/tasks/deltas before code; linked Docs/code PRs with exact revisions and merge order; verify, sync and archive completed work only. Never archive another lane's unfinished change or label plans as implemented behavior.

Read complete public requirements and timestamped comments. Review private chronology only when available and publish material requirements. Private tools are optional. Preserve dirty clones and unfinished work; use isolated checkouts. Coordinate before creating workers or editing another lane's scope. Use the shared [development hygiene skill](.agents/skills/development-hygiene/SKILL.md) before heavy builds and at handoff/delivery on every development machine.

PR bodies are exactly `# Summary` plus concise bullets; detailed evidence, revision pairs, limits and bot responses go in comments. Use scoped semantic titles, inspect required CI and bug-bot feedback, and obtain coordinated independent review before merge. Docs never tags/builds applications; components release independently; REM-35 alone owns 1.0.

The coordinating agent owns delegated work through review, integration and verified delivery. A worker's completion report is a handoff, not closure. Follow [delivery ownership](CONTRIBUTING.md#delivery-ownership): reconcile task state with linked PRs at every handoff and checkpoint, deliver ready increments, and retain a named owner and specific next action for unfinished work.

Squash merge every PR under the current user instruction, including the initial Docs migration. Do not change repository settings; the immutable migration archive preserves source evidence independently of topic history.

OpenSpec skills are in `.codex/skills/`; equivalent manual steps remain supported. Shared testing checklists are in `.agents/skills/`; run component commands from that component checkout. No tablet permission follows from setup or simulator success. Never incidentally pair/sync personal accounts or upgrade firmware. Keep secrets out of tracked files, logs and evidence; protected ignored local/environment configuration remains allowed.

Follow [development validation](CONTRIBUTING.md#development-validation): use the authorized development tablet whenever it is available, with one coordinated operator. Build and run the changed software, exercise the actual workflow and relevant edge cases, and observe the result. Automated component/regression checks run in existing CI. Local simulators or emulators are for parallel development while the tablet is occupied, or contributors without authorized hardware; they are not a prerequisite for an available tablet. Feed hardware failures into CI fixtures without presenting modeled results as product completion. Preserve existing execution scopes and independent recovery.

Put reusable documentation under `docs/` in every repository. Central OpenSpec artifacts remain in their standard `openspec/` structure; conventional root entry files such as README, CONTRIBUTING, AGENTS and LICENSE remain appropriate exceptions.
