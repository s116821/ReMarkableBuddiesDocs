# Simplify CI/CD maintenance and repository layout

## Why

Release and deployment helpers, examples and developer tools currently clutter
component roots. CI also rebuilds and requalifies maintained third-party Actions,
creating dependency locks, copied bundles, transfer checks and upstream test
fixtures that the project need not maintain.

## What Changes

- Place executable examples under `docs/examples/`, release/deployment inputs
  under `cicd/`, and development helpers under `scripts/`.
- Use maintained Actions directly at reviewed immutable revisions. Remove custom
  uploader builds, vendor locks, transfer artifacts and tests of upstream internals.
- Express ordinary build orchestration in the workflows; retain only concrete
  application packaging, identity, admission and recovery checks not supplied by
  the selected upstream tools.
- Update current commands and cross-repository references. Preserve historical
  evidence at its recorded revisions. Resynchronize open PRs after delivery.

## Scope

Buddy and Manager implementation PRs pair with this central change. SDK owns its
own corresponding specification lifecycle. Docs keeps its existing simple
validation workflow. This maintenance does not change device behavior, release
settings or the integrated 1.0 gate.

## Acceptance

Current commands resolve in the new layout; compiled examples remain Cargo
targets and application-relevant paths. Existing source, artifact integration and
publication guarantees remain enforced. Removed third-party qualification is
explicitly superseded, not reported as a successful audit of upstream internals.
Each open PR receives an ownership-aware resync and disposition audit so old paths
or completed work do not silently return.
