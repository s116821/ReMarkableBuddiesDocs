# Manager foundation

The [Manager repository](https://github.com/s116821/RemarkableBuddiesManager)
contains one Angular application delivered as a static browser app and an
Electron desktop app. This is a **foundation preview**, not a completed tablet
installer or updater. The base foundation has an unconfigured connection and
unknown tablet version. The additive [wired observation slice](manager-wired-observation.md)
adds explicit Linux read-only transport while preserving the installer gates.

## Public setup and checks

Clone Manager normally or use the ecosystem's selective bootstrap. Use Node
24.21.0, npm and Git. Then run `npm ci` and `npm start` for the browser;
`npm run desktop` builds and opens Electron. No private tools, account or tablet
are required. GitHub forks can run the same read-only PR checks; official release
publication is restricted to the upstream repository.

Run `npx playwright install --with-deps chromium`, `npm run check`,
`npm run package`, then `npm run test:package`. Headless Linux requires
`xvfb-run -a npm run check` and `xvfb-run -a npm run test:package`.
`check` includes ESLint, version tests, Angular production build, responsive
browser checks and actual sandboxed Electron renderer checks. Optional desktop
screenshots use `MANAGER_CAPTURE=1`; required checks assert actual rendered content,
runtime identity and isolation independently of headless screenshot support. Package verification
launches the packaged desktop executable. Windows x64 and Linux x64 are the
foundation's portable desktop targets. macOS, signing/notarization and desktop
automatic updates remain later delivery; do not infer their support.

Release fixtures additionally require Python 3.12. Install the hash-locked
maintained tools with `python -m pip install --require-hashes -r release/python-tools.lock`,
then run `npm run test:release`. These fixtures use real local Git repositories
and Python Semantic Release; upstream Action controls use loopback API fixtures.
No experimental production tags or tablet operations are required.

## Architecture and scope

Angular 22.2.0 and TypeScript 6.0.3 compile shared components. Electron 44.4.5
loads the same static output with a sandboxed, context-isolated renderer and no
Node integration. The preload exposes host identity and the separately specified bounded
[wired observation/cancel capability](manager-wired-observation.md); arbitrary
command IPC remains unavailable. The main process denies unapproved navigation, popups and permissions.
The sole external link opens the public Docs hub in the system browser.

Browser output is `dist/manager/browser`, deployable under a static server's root
or subdirectory. No site hosting is provisioned. The bounded Linux wired observation path uses an explicit authenticated
loopback companion helper for browsers and controlled SSH/OS integration for Electron. Neither permits a queryable Rust Buddy service/API.

REM-41 still owns host transport, identity/authentication, separate Manager/Rust
release discovery, compatibility checks, install/update/rollback, page-extension
dependencies, service-state verification and preserve-data uninstall. REM-42 owns
configuration and owned-data management through both hosts. No capability here
claims these outcomes or RM2/Paper Pro validation.

## Version and release contract

Manager tags/releases are independent of the
[Rust application](https://github.com/s116821/ReMarkableBuddies/releases).
No maintained source version is authoritative. Development builds display
`0.0.0-dev-<commit>[-dirty]`. The [release contract](../openspec/specs/release-versioning/spec.md)
uses pinned Python Semantic Release 10.7.0 for a read-only semantic candidate
before build, and tag-only creation after every required gate passes. Scoped feat
increments minor, recognized maintenance increments patch, and breaking changes
calculate major even at 0.x. The separate REM-35 guard blocks premature 1.0.
There are no generated version-bump commits.

Explicit documentation-only paths skip tags and all main application builds.
Unknown paths, dependencies, tests and workflow changes are application relevant;
mixed code/docs changes release normally. Application changes cannot use a docs
PR title. Required PR checks still finish for docs-only changes.

The ordered application workflow runs checks, builds frozen candidate artifacts,
then exercises those downloaded artifacts on Windows and Linux without rebuilding.
Build produces `manager-browser.zip`, `manager-win32-x64.zip`,
`manager-linux-x64.zip` plus `provenance.json`; separate retained development
browser output preserves the existing development/Tailwind checks on both hosts.
Archives contain source/version metadata and verified SHA-256 digests. The
unchanged four-field build-info schema's `official:true` identifies the controlled
recipe; an unpublished CI candidate is not a trusted release or installer.

One final release job alone creates the official annotated tag and publishes the
same integration-tested bytes. It requires an exact merged-main source proof and
successful preceding gates. Single-first-parent push admission refuses ambiguous
batches; actual main commit semantics are checked independently of the PR title.
Failed sources are not backfilled by later successes. Maintained Actions serialize
publication, observe an exact draft ID and upload only missing verified assets
without overwrite. Explicit failed-job retries reuse retained artifacts for 14
days; conflicting tags/assets refuse. Outside writers are not covered by an
atomic immutability guarantee. These portable archives are not tablet installers.

## Central specifications and coordinated delivery

The central capability is `openspec/specs/manager-foundation`. Its complete plan
was committed under `openspec/changes/manager-foundation` before Manager code.
Keep all future specifications/workflow skills here, with pointers in Manager.
Review linked Docs and implementation PRs at exact revisions. Merge the central
migration first, verified Manager implementation next, and corresponding as-built
Docs synchronization/archive immediately after. Archive only the completed bounded
foundation; full REM-41/42 acceptance stays outstanding.

## Framework sources

- [Angular version compatibility](https://angular.dev/reference/versions)
- [Angular static deployment](https://angular.dev/tools/cli/deployment)
- [Node release schedule](https://nodejs.org/en/about/previous-releases)
- [Electron stable releases](https://releases.electronjs.org/release?channel=stable)
- [Electron process model](https://www.electronjs.org/docs/latest/tutorial/process-model)
- [Electron security](https://www.electronjs.org/docs/latest/tutorial/security)

## Shared styling conventions

The completed [shared Tailwind capability](../openspec/specs/manager-shared-tailwind/spec.md)
uses one theme and reusable accessible components across browser and Electron.
Follow the Manager [styling guide](https://github.com/s116821/RemarkableBuddiesManager/blob/main/docs/styling.md)
for literal utilities, semantic tokens and development/production host checks.
Native Linux and independent Windows evidence are separately attributed in the
[bounded verification archive](../openspec/changes/archive/2026-10-08-manager-shared-tailwind/verification.md).
Tablet transport and installer gates remain separate.
