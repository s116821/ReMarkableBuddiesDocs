## ADDED Requirements

### Requirement: Qualified bounded stdin memory query
The memory maintenance CLI SHALL accept the exact input marker `-` for query-only UTF8 JSON, bounded by MAX_RECORD1048576 bytes, through the existing Query validator/configured profile/admission/current handoff/report writer. Regular-file input SHALL retain its existing checks. This input transport SHALL reuse the existing local memory provider and SHALL NOT initialize an external model/provider, device or service or change the memory domain schema. Source traceability: REM24 Manager consumer clarifications e4a68788/951b1fec and existing maintenance/Query source.

#### Scenario: Equivalent file and stdin query
- **WHEN** the same valid Query is supplied by a supported absolute regular file and by stdin followed by EOF against the same configured Store
- **THEN** both routes preserve query scope/budgets/provenance/status and the existing selected-current stdout handoff semantics

#### Scenario: Invalid stdin refuses before Store
- **WHEN** stdin is invalid UTF8/JSON/domain input, encounters an I/O failure or exceeds the byte bound
- **THEN** the command emits a sanitized InvalidInput report without admitting/opening Store or echoing input

#### Scenario: Stdin is not mutation authority
- **WHEN** a non-query memory operation supplies the stdin marker
- **THEN** the command returns Unsupported without consuming stdin, loading configuration or opening Store; ordinary file-based operations remain unchanged
