# Manager foundation

The [Manager repository](https://github.com/s116821/RemarkableBuddiesManager)
contains one Angular application delivered as a static browser app and an
Electron desktop app. This is a **foundation preview**, not a completed tablet
installer or updater. Both hosts show an unconfigured connection and unknown
tablet version. They perform no tablet or Buddy-service calls.

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

Release fixtures additionally require Python 3.12 and git-cliff 2.14.2 on PATH.
Run `npm ci --prefix release`, then `npm run test:release`. These fixtures use real
local Git repositories, git-cliff and release-it; GitHub publication is simulated.
No experimental production tags or tablet operations are required.

## Architecture and scope

Angular 22.2.0 and TypeScript 6.0.3 compile shared components. Electron 44.4.5
loads the same static output with a sandboxed, context-isolated renderer and no
Node integration. The preload exposes host identity only; no command IPC is
available. The main process denies unapproved navigation, popups and permissions.
The sole external link opens the public Docs hub in the system browser.

Browser output is `dist/manager/browser`, deployable under a static server's root
or subdirectory. No site hosting is provisioned. Future browser tablet transport
may use an authenticated companion helper; Electron may use controlled SSH/OS
integration. Neither permits a queryable Rust Buddy service/API.

REM-41 still owns host transport, identity/authentication, separate Manager/Rust
release discovery, compatibility checks, install/update/rollback, page-extension
dependencies, service-state verification and preserve-data uninstall. REM-42 owns
configuration and owned-data management through both hosts. No capability here
claims these outcomes or RM2/Paper Pro validation.

October 1 adds an unselected supervised lazy XOVI candidate to REM-25/41. If qualified,
the Buddy artifact contains both its independent Supervisor and normal runtime plus
any vetted internal payload; Manager owns the single install/update/disable/uninstall
and preservation/recovery lifecycle. It does not install a separate SDK runtime or
require users to manage XOVI. Cold boot remains stock with injection inactive;
activation belongs to the first supported Buddy gesture of the session, with bounded
health checks, automatic stock rollback and UI-independent recovery. Foundation
delivery does not claim this lifecycle is implemented or choose XOVI.

## Version and release contract

Manager tags/releases are independent of the
[Rust application](https://github.com/s116821/ReMarkableBuddies/releases).
The package manifest version 0.0.0 is a non-authoritative tooling placeholder.
Development builds display `0.0.0-dev-<commit>[-dirty]`. Official builds contain
the exact semantic tag version and commit in both UI and package metadata.

The release policy is adapted from actual Rust revision
`33db26add721cea6c0121ad769a54d06ae600b4e`: git-cliff 2.14.2 computes versions;
release-it 19.0.6 creates immutable annotated tags on application squash commits.
There are no generated version-bump commits. For a new repository, the initial
calculation excludes its verified docs-only history prefix so a non-semantic
GitHub README initialization cannot block the first application release. An initially untagged Manager starts
at v0.1.0; feat increments minor, fix/maintenance increments patch, and breaking
changes calculate major. A publication guard blocks major 1+ until a reviewed
REM-35 change enables the completed ecosystem's release.

Explicit documentation-only paths skip tags and all main application builds.
Unknown paths, dependencies, tests and workflow changes are application relevant;
mixed code/docs changes release normally. Application changes cannot use a docs
PR title. Required PR checks still finish for docs-only changes.

One lock covers refresh, recovery, tagging, building and draft publication.
After verifying the remote tag, the release job clones the exact source and builds
`manager-browser.zip`, `manager-win32-x64.zip`, `manager-linux-x64.zip` plus
`provenance.json`. Archives contain tag/SHA metadata and verified SHA-256 digests.
Cross-packaged Linux archives preserve executable permissions. Windows and Linux
PR CI exercise their native packaged host; the official Windows release runner
executes the Windows package and cross-packages Linux. These portable archives are
not tablet installers. Pending tags recover before newer application commits;
verified published assets are immutable and partial drafts remain retryable.

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
