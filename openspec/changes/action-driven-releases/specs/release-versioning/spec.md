## MODIFIED Requirements

### Requirement: Semantic application releases
The release system SHALL compose maintained upstream Actions and declarative
configuration for path selection, semantic version calculation, immutable tagging
and publication. It SHALL NOT contain a custom release coordinator, path classifier,
bump algorithm or publication/retry engine in Python, JavaScript or shell. Each
admitted application squash merge SHALL receive a version derived from its tagged
ancestry and actual conventional history, independently of queue execution order.
Scoped feat SHALL bump minor, fix and recognized maintenance types SHALL bump patch,
and ! or BREAKING CHANGE footers SHALL bump major even at0.x. Existing tags SHALL
remain unchanged. Source: REM-30 and September26 REM-46 clarification.

#### Scenario: Feature followed by a fix
- **WHEN** application squash history contains feat(REM-9) then fix(REM-9), even if their jobs start in reverse order
- **THEN** the feature's own SHA receives its minor version and the fix's own SHA receives the following patch version, without tagging a newer docs commit instead.

#### Scenario: Breaking change
- **WHEN** an application commit uses conventional breaking syntax or a BREAKING CHANGE footer
- **THEN** upstream tooling calculates a major bump from the actual tagged base, while the explicit REM-35 gate still prevents premature major publication.

#### Scenario: Misclassified application change
- **WHEN** an application PR uses docs or an unsupported/nonconventional title
- **THEN** validation fails visibly before release handling rather than silently skipping the application change.

### Requirement: Documentation merge exclusion
Upstream Actions and version-tool configuration SHALL conservatively exclude only
explicit documentation paths. Pure documentation merges SHALL create no tag and
execute no application compilation in CI or release workflows. Unknown paths,
build/dependency changes, executable fixtures and mixed changes SHALL remain
application-relevant. Required PR checks SHALL finish for docs-only changes without
an app build. Source: REM-30/46.

#### Scenario: Documentation-only merge
- **WHEN** a docs PR changes only the explicit README/spec/documentation paths
- **THEN** it completes non-compiling checks and never invokes the publication workflow or advances the application version.

#### Scenario: Mixed and reverted changes
- **WHEN** separate queued application merges include an edit then its revert, alongside documentation merges
- **THEN** upstream history analysis retains both application commits rather than discarding their releases because a later net diff is empty.

#### Scenario: Executable fixtures or renamed code
- **WHEN** scripts/JSON fixtures under docs change or code is moved into a documentation path
- **THEN** the change remains relevant using both old and new paths; incomplete file/history observations fail visibly.

### Requirement: Immutable tag before exact-source build
Release tags SHALL identify the actual admitted merged main squash commit without
generated version commits. Remote tag creation or exact identity verification SHALL
precede official compilation. Distributed packages SHALL checkout that exact tag,
embed its version and report matching source/checksum provenance. Custom helpers
SHALL be limited to actual application build/packaging and directly necessary
source/version/artifact checks. Source: REM-30/46.

#### Scenario: Main CI ordering
- **WHEN** an application PR merges to main
- **THEN** main-push CI performs non-compiling checks, and the explicit release DAG tags the admitted SHA before any official app build; PR CI may compile dev builds.

#### Scenario: Main advances to documentation
- **WHEN** newer docs or application commits exist while a release waits
- **THEN** its tag and all artifacts still identify its original admitted SHA, not refreshed main.

#### Scenario: Tag push fails or conflicts
- **WHEN** the tag cannot be pushed or the fetched tag has a different target
- **THEN** publication fails before compilation, with no force update or replacement tag.

### Requirement: Recoverable serialized publication
Application publication SHALL use native Actions ordering/concurrency and upstream
draft/upload/release actions. Jobs SHALL preserve independently recoverable merge
identity without relying on FIFO or replacement of pending runs. Reruns and manual
existing-tag dispatch SHALL recover unfinished releases after main advances, without
allocating a new version, mutating completed releases or relying on GITHUB_TOKEN tag
events. A completed published release SHALL skip compilation and asset writes.
Source: REM-30's recovery requirements and REM-46 coordinator removal.

#### Scenario: Several queued merges
- **WHEN** several application PRs merge while another release runs
- **THEN** their release runs are retained within the supported queue bound and each exact source remains independently recoverable; a cancelled/overflowed run is visibly unfinished, not represented as released.

#### Scenario: Partial release retry
- **WHEN** a run fails after tagging or during builds/uploads
- **THEN** the immutable tag and recoverable draft remain; retry builds that same tag and publishes only after all package checks/uploads succeed.

#### Scenario: Documentation after failure
- **WHEN** only a documentation merge follows a failed application release
- **THEN** that merge remains build-free; the original run or explicit existing-tag dispatch recovers the unfinished release without another application merge.

#### Scenario: Completed release retry
- **WHEN** the same release is already published
- **THEN** the upstream observation and declarative skip prevent builds and asset replacement; its existing tag/assets remain untouched.

#### Scenario: Old unfinished draft
- **WHEN** the exact tag has an unfinished draft beyond the first two releases-list pages
- **THEN** upstream direct tag lookup or complete pagination discovers and reuses that same draft ID, with no duplicate create request or new tag.

#### Scenario: Failed release observation
- **WHEN** the release lookup returns a network, authentication, GraphQL or unexpected API failure, or a malformed identity/state observation
- **THEN** the run fails before draft changes or application builds; the error is never interpreted as a missing release.

#### Scenario: Unsupported draft asset inventory
- **WHEN** an existing draft exceeds the upstream uploader's verified complete asset-discovery bound
- **THEN** the run refuses before compilation or asset mutation and reports the unsupported inventory rather than overlooking an asset on another page.

#### Scenario: Upload interruption
- **WHEN** an artifact upload fails
- **THEN** the release remains draft, and no public release is claimed from the mere existence of a tag or partial asset set.
