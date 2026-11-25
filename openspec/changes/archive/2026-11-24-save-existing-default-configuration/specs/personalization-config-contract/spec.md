## ADDED Requirements

### Requirement: Explicit first saved configuration for an existing default installation

Buddy SHALL expose `check-existing-default` and `create-existing-default` on `--configuration-operation` with bounded version-1 reports and no stdin. An existing default installation SHALL require the ordinary Store lease and local-mode checks before creating the fixed canonical configuration. Existing Store data, credentials and recovery state SHALL be preserved. The clean and replacement flow SHALL retain its empty-root admission. Manager SHALL offer explicit review and confirmation for this action through the existing wired setup flow. Once a valid file exists, the existing saved-revision personalization editor SHALL apply.

#### Scenario: Check and create on an existing default installation

- **WHEN** the existing default Store is available and both known configuration files are absent
- **THEN** check returns missing without writes, and an explicit create may publish the built-in defaults at the canonical path using atomic no-clobber publication and verified readback.

#### Scenario: Earlier or incompatible config

- **WHEN** a valid canonical file already exists, the legacy config exists, or a config entry is unsafe, invalid or inaccessible
- **THEN** Buddy reports present for the valid canonical-only case and blocked otherwise, preserving all existing files.

#### Scenario: Concurrent or interrupted first save

- **WHEN** another writer creates a configuration first, or a possible publication cannot be verified
- **THEN** Buddy preserves the winner and never treats an uncertain response as a rollback. Manager can check the current disk state without replaying the original create.
