## ADDED Requirements

### Requirement: Existing pull request CI preservation
Every retained application PR SHALL carry the accepted compact CI and required feature-specific controls before merge. A branch update SHALL preserve unrelated unfinished source. Common suites SHALL run once in Checks, while native OS-specific controls SHALL run on their applicable existing Integration host. Rollout completion SHALL be supported by refreshed current heads and actual relevant validation rather than local previews alone.

#### Scenario: Existing PR delivery
- **WHEN** an existing or future PR is prepared for merge
- **THEN** it preserves the corrected job-count limits and required test coverage, and its effective merged workflow cannot restore the old administrative jobs.

#### Scenario: Windows-only feature control
- **WHEN** a feature contains a native Windows API or NTFS control that is skipped on Linux
- **THEN** its selected control runs in the existing Windows Integration job without repeating the common source suite or adding another job.

#### Scenario: Unrelated source conflict
- **WHEN** bringing a feature branch forward exposes a source conflict outside the CI wiring
- **THEN** the conflict is resolved explicitly with preservation evidence or retained as a visible gate; neither side's unfinished work is silently discarded.
