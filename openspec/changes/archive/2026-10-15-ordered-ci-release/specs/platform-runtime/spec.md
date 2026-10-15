## MODIFIED Requirements

### Requirement: Git-derived application version
The CLI version SHALL derive from Git history through maintained semantic tooling
and vergen-gitcl, never an independently maintained Cargo package version.
A controlled candidate build SHALL require full clean history and exact frozen
candidate tag/version and source SHA; it MAY precede remote tag creation.
Its embedded value alone SHALL NOT grant official publication or native trust.
An existing published-tag build SHALL additionally verify the actual tag/SHA.
Only the final release job after all build/artifact integration gates SHALL create
the official tag and publish those exact already-tested bytes. Development or
unavailable metadata SHALL be explicit. Source: REM-56 superseding REM-30 order.

#### Scenario: Official tagged build
- **WHEN** an existing published-tag build checks out its verified release tag
- **THEN** --version and package provenance report that tag's semantic version and exact source SHA.

#### Scenario: Verified candidate before publication
- **WHEN** controlled CI builds a frozen clean candidate before the remote tag exists
- **THEN** both target artifacts report the frozen candidate version and integration consumes those bytes; only later successful final tag/release proof establishes publication eligibility.

#### Scenario: Missing or conflicting official metadata
- **WHEN** candidate/published metadata has shallow or missing history, dirty source, conflicting profiles/overrides or wrong source/tag identity
- **THEN** the build refuses instead of substituting a manifest version or misleading release identity.

#### Scenario: Development build
- **WHEN** a build has neither valid controlled candidate nor verified published-tag metadata
- **THEN** --version identifies development or unavailable Git state explicitly.
