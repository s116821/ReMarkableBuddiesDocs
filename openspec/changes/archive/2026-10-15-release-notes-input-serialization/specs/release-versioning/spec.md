## MODIFIED Requirements

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
