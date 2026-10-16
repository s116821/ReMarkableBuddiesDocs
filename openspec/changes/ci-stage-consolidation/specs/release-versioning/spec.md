## ADDED Requirements

### Requirement: Four-stage application CI
Application CI SHALL run at most four jobs for a PR and at most five jobs for an eligible main merge, counting matrix executions. It SHALL expose Checks, Build, Integration and Release stages. All existing source checks SHALL finish before application compilation, including Manager's Linux prechecks at the start of Build. Path/title checks, candidate selection and tool qualification SHALL be steps of those stages rather than independent administrative jobs. Duplicate standalone title workflows SHALL be removed from main PR runs only after their checks are preserved. Required status contexts SHALL remain satisfiable without weakening the protected delivery gate.

#### Scenario: Application change
- **WHEN** a Buddy or Manager application change is checked
- **THEN** Checks gates Build, Build's exact artifacts feed Integration, and only successful eligible main runs enter Release; existing tests remain.

#### Scenario: Documentation-only change
- **WHEN** maintained filtering identifies a documentation-only change
- **THEN** metadata checks finish without application compilation or entering the application publication queue.

#### Scenario: Earlier stage fails
- **WHEN** a required check, build or artifact integration fails or is canceled
- **THEN** dependent application stages do not publish any tag or release.

#### Scenario: Existing PR delivery
- **WHEN** an existing or future PR is prepared for merge
- **THEN** it preserves the corrected job-count limits and required test coverage, and its effective merged workflow cannot restore the old administrative jobs.
