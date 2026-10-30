## MODIFIED Requirements

### Requirement: Four-stage application CI
Application CI SHALL run four Buddy jobs and five Manager jobs per application PR or eligible main merge, counting matrix executions and excluding skipped jobs that allocate no runner. PRs SHALL run PR Title before Checks; main merges SHALL run Release after Integration. Common source, dependency and workflow checks SHALL run once in Checks before Build, and downstream jobs SHALL depend on that result rather than rerun those suites. Supported-platform runtime checks SHALL belong to Integration. Candidate selection SHALL remain a step rather than a standalone administrative job. Maintained upstream Actions SHALL be consumed directly at reviewed immutable revisions; application CI SHALL NOT rebuild, transfer or requalify their implementations. Ordinary command orchestration SHALL live in the workflow. Substantive project-specific packaging, source admission, artifact identity and recoverable publication checks MAY remain tested helpers. Required status contexts SHALL remain satisfiable without weakening the protected delivery gate.

#### Scenario: Application change
- **WHEN** a Buddy or Manager application change is checked
- **THEN** Checks gates Build, Build's exact artifacts feed Integration, and only successful eligible main runs enter Release; application-specific tests remain.

#### Scenario: Invalid PR title
- **WHEN** the maintained title Action rejects a PR title
- **THEN** the Checks job and all dependent application jobs do not run.

#### Scenario: Downstream prerequisite
- **WHEN** Build, Integration or Release requires a common source or dependency check already owned by Checks
- **THEN** it relies on the dependency instead of repeating that suite; fresh downloaded-byte integrity and publication-state checks remain scoped to their own boundary.

#### Scenario: Documentation-only change
- **WHEN** maintained filtering identifies a documentation-only change
- **THEN** metadata checks finish without application compilation or entering the application publication queue; executable examples under docs remain application-relevant.

#### Scenario: Earlier stage fails
- **WHEN** a required check, build or artifact integration fails or is canceled
- **THEN** dependent application stages do not publish any tag or release.

#### Scenario: Direct maintained uploader
- **WHEN** publication uses the pinned upstream upload Action
- **THEN** it uses that revision's distributed implementation without a project-built vendor bundle, while exact release identity, no-overwrite behavior and complete uploaded-byte verification remain application gates.
