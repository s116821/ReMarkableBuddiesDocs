## Why

REM-46 implements the September 26 clarification: established Actions should own
release filtering, version selection, tagging and publication in both components.
Rust already uses canonical tags and post-tag builds, but its Python coordinator
also implements history replay, recovery and publication. Manager copied that
coordinator. Replacing this machinery must preserve the functional REM-30 contract.

## What Changes

- Compose pinned upstream Actions and declarative workflow/configuration for both
  repositories; delete the Python policy/coordinator and unused release-it/git-cliff
  installation/configuration. Do not translate that coordinator into another language.
- Filter each merged application PR, derive its version from tagged ancestry and
  conventional squash messages, create an immutable tag on its exact merged SHA,
  then build verified packages and publish only after all uploads succeed.
- Use ordinary Actions reruns and explicit existing-tag recovery, with recoverable
  drafts and no modification of completed releases. Preserve independent component
  versions, documentation exclusions and the separate REM-35 major-release gate.
- Retain custom code only for actual application builds, packaging and directly
  necessary source/version/artifact checks. Test orchestration is not production
  release machinery.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `release-versioning`: upstream Actions, ancestry-based per-merge versioning and
  explicit retry/recovery replace the custom replay coordinator.
- `manager-foundation`: apply the same action-based lifecycle to the independent
  Angular/browser/Electron release, without changing UI or transport behavior.

## Impact

Linked Docs/Rust/Manager PRs are one delivery. No production tag, asset, settings or
tablet mutation is authorized merely by this plan. Existing tags/assets remain
immutable; no Cargo/package release-version commits are introduced. Full fixtures,
independent review, CI, canonical sync and archive precede coordinated squash merges.
