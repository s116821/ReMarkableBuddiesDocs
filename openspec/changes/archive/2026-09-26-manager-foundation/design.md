# Design

## Verified inputs

Read revised roadmap e00e720cfb68, REM-21, REM-41, REM-30 and every available
timestamped comment. Current explicit instructions centralize all OpenSpec in Docs.
Inspected Rust `.github/workflows/{ci,release,pr-title}.yml`, release-tools action,
`release/{policy,coordinator,test_release,test_github,test_workflows}.py`,
`cliff.toml` and release-it configuration at the revision in proposal.md.

## UI and host boundary

Angular 22.2.0, TypeScript 6.0.3, Node 24.21.0 and Electron 44.4.5 are pinned
from official current compatibility/releases and package registry metadata.
Angular has standalone components and one host abstraction. Browser uses an
unconfigured adapter; Electron exposes only immutable host identity through a
context-isolated sandboxed preload. No arbitrary IPC, Node renderer access,
remote content, shell commands or Buddy admin endpoint. Navigation/popups and
permission requests are denied. A later reviewed transport may implement SSH in
the desktop host and an authenticated companion helper for browsers.

The foundation screen clearly distinguishes Manager version from unknown tablet
version. It describes unavailable install/update/configuration features honestly.
Both hosts render exactly the same application, including responsive and keyboard
accessible layout. Browser static files also run from a subdirectory.

## Version and release adaptation

Retain Rust's conservative path allowlist, first-parent semantic squash policy,
git-cliff 2.14.2 decisions and release-it 19.0.6 annotated tags. Application paths
include dependencies, tests, packaging and workflow changes; only explicit docs
paths are excluded. Reject docs titles concealing application changes.

Manager is initially untagged: git-cliff's initial tag is v0.1.0, applied to the
first eligible application commit, never a generated bump commit. The initial
git-cliff range excludes the already-verified docs-only prefix (including a
non-conventional GitHub README initialization); application title validation
remains mandatory. Later feat
increments minor; fix/maintenance patch; breaking changes calculate major but
publication refuses major 1+ until REM-35 explicitly changes that gate.

A serialized release job refreshes main, recovers pending immutable tags first,
then handles each unreleased application squash commit in order. It verifies the
pushed tag before cloning exact source and compiling. No dependency on token tag
events. Docs-only main pushes never enter the release queue or application build.
PR required checks finish with an explicit success for docs-only diffs.

Package version stays non-authoritative (0.0.0); generated build metadata carries
exact tag/SHA for official builds and an explicit dev suffix for all local/PR
builds. Reject shallow/mismatched/dirty official source. Browser ZIP and Electron
portable Windows/Linux x64 ZIP artifacts contain the same UI and metadata, with
checksummed provenance. Portable foundation archives are not tablet installers.
macOS signing/notarization and desktop automatic updates remain REM-41 work.
Publish verified draft artifacts only after all required packages pass; retries
cannot silently overwrite completed releases. Do not publish any production tag
as an experiment in this lane.

## Verification

Real Angular build and ESLint checks; browser automation against built static
output; actual Electron renderer smoke with sandbox/Node absence assertions;
package and reopen the packaged desktop app. Optional native screenshots are
separate from mandatory rendered-content/runtime/isolation assertions because
headless compositors can reject hidden-surface capture. Run host checks on Windows locally
and Linux/Windows CI where supported. Deterministic temporary Git repositories
exercise initial release, feat/fix/breaking, mixed docs/code, docs-only no build,
reverts, renamed paths, stale queued merges, failed build/upload retries,
remote tag conflicts, shallow history and provenance integrity. Mock only the
GitHub publication boundary, not git-cliff/tag creation. Distinguish local/CI
host evidence from hardware and installed/update behavior not yet implemented.

## References

- https://angular.dev/reference/versions
- https://angular.dev/tools/cli/deployment
- https://nodejs.org/en/about/previous-releases
- https://releases.electronjs.org/release?channel=stable
- https://www.electronjs.org/docs/latest/tutorial/process-model
- https://www.electronjs.org/docs/latest/tutorial/security
- https://git-cliff.org/docs/configuration/bump/
