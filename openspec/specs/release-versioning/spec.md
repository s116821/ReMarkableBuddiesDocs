# release-versioning

## Purpose

Define semantic Git-tag versioning and recoverable exact-source application publication.

## Requirements

### Requirement: Semantic application releases
The release system SHALL use maintained upstream tooling for semantic selection,
tagging and publication, with no private release coordinator or maintained source
version. Scoped feat SHALL bump minor, fix and recognized maintenance types SHALL
bump patch, and explicit breaking syntax/footer SHALL bump major even at 0.x.
Existing tags SHALL remain unchanged. A read-only candidate MAY be calculated
before build; only the final eligible release job SHALL create its official tag.
Source: October 15 REM-56 superseding REM-30/46 ordering.

#### Scenario: Feature followed by a fix
- **WHEN** successful eligible main merges contain a feature and then a fix
- **THEN** maintained semantic history selects the minor then patch versions on their exact source SHAs without version-bump commits.

#### Scenario: Breaking change
- **WHEN** application history contains conventional breaking syntax or footer
- **THEN** maintained tooling selects a major bump including 0.x, and the separate REM-35 gate refuses premature 1.0 publication.

#### Scenario: Misclassified application change
- **WHEN** an application path changes under docs or an unsupported/nonconventional PR title or actual admitted main commit message
- **THEN** checks fail visibly before build or tag rather than silently excluding code or borrowing a candidate bump from earlier untagged history.

### Requirement: Documentation merge exclusion
The workflows SHALL share conservative path classification with semantic release
analysis. Pure documentation pushes SHALL create no tag and execute no application
compilation. Unknown non-documentation paths, build/dependency changes and mixed
changes SHALL remain application-relevant. Required PR checks SHALL finish for
documentation-only changes. Canonical main pushes SHALL contain exactly one
first-parent commit in the known before/source range; ambiguous batches, initial
zero/unknown history and non-forward updates SHALL refuse visibly before build or
tag. Structural merge admission SHALL remain distinct from actual-source semantic
eligibility and final exact merged-PR proof.
Source: REM-56 superseding the earlier private touched-history/backfill classifier.

#### Scenario: Documentation-only merge
- **WHEN** one admitted docs commit modifies only excluded documentation paths
- **THEN** the push performs only non-compiling checks and never enters the application publication queue.

#### Scenario: Mixed and reverted changes
- **WHEN** a push contains multiple first-parent commits, including an application edit later reverted to a net-zero diff
- **THEN** admission refuses before build/tag rather than classifying the ambiguous batch as documentation-only.

#### Scenario: Executable fixtures within documentation directories
- **WHEN** simulator JSON or validation scripts under docs change
- **THEN** those paths remain application-relevant and receive tests/release handling rather than documentation-only exclusion.

### Requirement: Verified artifacts before official tagging
The earlier tag-before-build ordering is superseded. Official tags SHALL identify
the same main source SHA and candidate version as artifacts already built and
tested by the ordered workflow. Tag/release creation SHALL occur only in its final
dedicated release job after checks, build and required artifact integration pass.
Failures, cancellation or skipped required predecessors SHALL prevent new tags
and releases. Exact built bytes SHALL be published without a release-job rebuild.
Source: October 15 REM-56 human instruction.

#### Scenario: Main CI ordering
- **WHEN** an application commit reaches main
- **THEN** simple checks gate build, built-artifact integration gates the one release job, and no official tag/release exists before those gates pass.

#### Scenario: Main advances to documentation
- **WHEN** newer main commits exist after the admitted application source
- **THEN** the frozen candidate, build, integration, tag and release still refer to that exact admitted source and verified bytes.

#### Scenario: Tag push fails or conflicts
- **WHEN** final tag creation fails or the existing remote tag targets a different source
- **THEN** publication refuses without replacing the tag, changing the candidate or rebuilding substitute assets.

### Requirement: Recoverable serialized publication
Main release runs SHALL use maintained workflow serialization and bind exact
source/candidate/artifact identity. A failed earlier run SHALL remain untagged
unless its own preceding gates later pass; no bespoke history backfill may publish
it merely because a later run succeeds. Final-stage recovery SHALL retain the same
remote tag/draft identity and verified assets without overwrite or duplicate tags.
String metadata passed through maintained Actions SHALL preserve its exact text
under those Actions' declared input parsing rather than being interpreted as YAML
structure. Source: REM-56 and the observed final-input failure.

#### Scenario: Queued jobs are replaced
- **WHEN** main advances, a pending run is canceled or an older run resumes
- **THEN** no run substitutes current main for its admitted SHA or claims a canceled/failed predecessor passed; retry remains explicit and identity-bound.

#### Scenario: Partial release retry
- **WHEN** final publication fails after tagging or during upload
- **THEN** retry verifies the same built artifacts and retained assets, uploads only missing matching bytes and finalizes only after complete verification.

#### Scenario: Documentation after failure
- **WHEN** only documentation follows a failed application run
- **THEN** documentation remains build/tag/release free and does not silently publish the failed run.

#### Scenario: Multiline completion metadata
- **WHEN** final verified release notes contain newlines, colons, quotes or Unicode
- **THEN** maintained input serialization preserves the exact notes string in the final request body, without bypassing same-ID or complete-byte verification.

### Requirement: Build-consuming integration gates publication
Required integration jobs SHALL consume the outputs produced by the gated build,
verify exact inventory/source/version/digests and execute supported artifact
checks without rebuilding substitutes. Only a canonical main run with successful
required predecessors SHALL enter the one dedicated release job.

#### Scenario: Failed or substituted artifact
- **WHEN** a required gate fails/skips/cancels, or downloaded bytes/source/version differ from the build receipt
- **THEN** no tag/release is created and no replacement build is silently substituted.

#### Scenario: Documentation validation ordering
- **WHEN** the Docs repository runs validation
- **THEN** portable prerequisite checks gate strict specification validation with read-only permissions and no application release.

#### Scenario: Existing development configuration coverage
- **WHEN** Manager's existing development browser configuration is built alongside production artifacts
- **THEN** its separate CI-only retained output is exercised on both supported hosts without an integration rebuild or inclusion in production release assets.
