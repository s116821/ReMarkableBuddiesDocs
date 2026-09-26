## MODIFIED Requirements

### Requirement: Central specification ownership
The ecosystem SHALL keep all OpenSpec specifications, active changes, archives, config and workflow skills exclusively in the public Docs repository. Implementation repositories SHALL link to that authority. Migration SHALL preserve original source commit/blob provenance and incomplete change state. Preserved source bytes SHALL remain verifiable without topic-branch Git history, network access or unchanged live artifact paths, including after squash merges.

#### Scenario: Historical and unfinished migration
- **WHEN** Rust main and an unfinished branch are migrated
- **THEN** canonical/archive bytes and active branch artifacts are traceable to exact source blobs, and unfinished work remains active without checked-off tasks or canonical sync

#### Scenario: Squashed history and evolved live artifacts
- **WHEN** a contributor shallow-clones squashed Docs history after imported live guidance or changes have been edited or removed
- **THEN** the manifest and immutable compressed blob archive still verify every original source blob and support retrieving its exact bytes without the original import commit
