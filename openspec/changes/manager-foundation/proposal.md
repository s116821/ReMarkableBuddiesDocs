# Manager foundation

## Why

REM-21 requires a public Angular browser and Electron foundation with independent,
Git-derived releases. REM-41 depends on this foundation but its installer/updater
is not delivered here. September 26 explicit resume and centralized OpenSpec
instructions supersede older holds and component-local specification instructions.

## What changes

- Share one Angular application between a static browser distribution and a
  sandboxed Electron desktop host. Explicitly show transport as not configured.
- Add reproducible dependency locks, lint, browser/desktop smoke and packaging checks.
- Adapt actual Rust release policy, git-cliff/release-it orchestration, immutable
  tags, recovery and provenance from Rust revision
  `33db26add721cea6c0121ad769a54d06ae600b4e` to Manager artifacts.
- Keep all OpenSpec and workflow assets here; Manager has central pointers only.
- Gate official builds after tagging, exclude docs-only merges, retain public/fork
  checks, and block major 1+ publication pending the separately reviewed REM-35 gate.

## Impact and exclusions

Capability: manager-foundation. Implementation: s116821/RemarkableBuddiesManager.
No Rust modifications or tablet operations. No working connection, release
discovery, installer, updater, configuration/data management, firmware changes,
account sync or page-extension claim. REM-41 and REM-42 remain open.
No hosting deployment; browser output is a portable static release archive.

## Delivery

Commit this complete plan before Manager code. Linked Docs and Manager PRs form
one delivery. Review exact revisions and CI, merge central migration first, then
Manager implementation, then the synchronized as-built Docs capability/archive.
Do not merge either foundation PR until the parent independently reviews it.
