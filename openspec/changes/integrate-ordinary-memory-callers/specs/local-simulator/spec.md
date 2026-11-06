## ADDED Requirements

### Requirement: Ordinary memory caller qualification
Maintained enabled/disabled memory fixtures SHALL exercise the actual ordinary
Dispatch Reader, Writer Generate/Refine and notebook map/reduce receiving paths
on real scratch Stores using the existing simulator facilities. Disabled defaults
and existing historical-image/replay/cancellation controls SHALL be preserved.
Scripted, loopback transport, real-provider and native evidence SHALL remain
separate. Source traceability: simulator/combined.rs,
simulator/combined/qualification.rs and the design's existing test mapping.

#### Scenario: Enabled same-path control
- **WHEN** the maintained enabled fixture executes without credentials
- **THEN** it SHALL assert actual exact histories, source/image associations, configured memory scope/query counts, retained drafts and reducer-only memory/digest binding through production receivers.

#### Scenario: Bounded live receiving evidence
- **WHEN** a maintainer separately selects one exact-source enabled-memory live sequence after source/build/config/fixture review
- **THEN** the existing entry SHALL permit at most seven non-retried requests, 4000 completion tokens and 90 seconds per request, and 12 minutes overall, stop on any error, and retain actual payloads/replies for independent source-fact and attribution review without native/export claims.

#### Scenario: Credential-free and failed evidence remains distinct
- **WHEN** scripted success or a partial/failed live attempt is recorded
- **THEN** it SHALL NOT be relabeled as complete live, handwriting, native, memory-causal or full-feature qualification, and a spent attempt SHALL NOT replay automatically.
