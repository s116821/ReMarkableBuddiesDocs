## MODIFIED Requirements

### Requirement: Independent semantic release policy
Manager SHALL follow the action-based release-versioning contract with independent
Git tags and release cadence. Maintained Actions SHALL own filtering, semantic
version calculation, tag creation and publication; no custom coordinator or policy
engine is permitted. Pure documentation merges SHALL create no tag or app build.
Manager releases SHALL never trigger Rust builds. Source: REM-21/30/46.

#### Scenario: Documentation-only merge
- **WHEN** only explicit documentation paths change
- **THEN** required PR checks finish and main skips application compilation, tags and publication.

#### Scenario: Relevant semantic change
- **WHEN** a scoped feat, fix, maintenance or breaking application squash is admitted
- **THEN** upstream tooling computes its version from its actual tagged ancestry, docs titles concealing code fail, and major1+ publication stays gated by REM-35.

### Requirement: Exact source and recoverable artifacts
Official browser and desktop packages SHALL compile only after the immutable remote
tag exists at the exact admitted SHA. Runtime metadata, package names and checksum
provenance SHALL agree. Local/PR builds SHALL identify themselves as development.
Custom code SHALL be restricted to actual application building/packaging and
directly necessary metadata/artifact verification. Source: REM-21/30/46.

#### Scenario: Release interruption and retry
- **WHEN** a build/upload fails after tagging and main advances
- **THEN** retry recovers that same tagged source, leaves completed releases untouched and keeps partial artifacts draft until all packages have been verified and uploaded.

#### Scenario: Browser and desktop agreement
- **WHEN** official browser, Windows desktop and Linux desktop packages are produced
- **THEN** all three embed the same tag/source, Linux executable modes are retained and none relies on an independently maintained package.json application version.
