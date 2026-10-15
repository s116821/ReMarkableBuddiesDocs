## MODIFIED Requirements

### Requirement: Exact source and recoverable artifacts
Manager SHALL freeze a read-only candidate version and source SHA, build its
browser/desktop artifacts, and test those exact bytes before final tagging or
publication. Its one final main-only release job SHALL reuse their verified
inventory/digests. Recovery SHALL not replace tags, overwrite differing assets,
rebuild substitutes or convert a failed/skipped predecessor into a successful gate.
Source: REM-56 superseding earlier tag-before-build ordering.

#### Scenario: Release interruption and retry
- **WHEN** build, integration or final upload is interrupted
- **THEN** failed predecessors create no new official tag/release; final-job recovery verifies the exact candidate/source/artifacts and retained matching bytes before publication.
