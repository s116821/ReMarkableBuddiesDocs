## ADDED Requirements

### Requirement: Storage-backed conversation regression evidence
Offline fixtures SHALL use the real shared Store and actual Reader orchestration seams to test restart, duplicate operations, full-head conflict, image byte identity, target changes, explicit context bounds, interrupted writes and reference-aware deletion. Mixed Reader/Writer API tests SHALL be labeled domain evidence rather than native Writer UI validation. Source: REM-37 acceptance and evidence separation.

#### Scenario: Provider boundary and reopen
- **WHEN** an offline Reader fixture records each supplied image and the Store is reopened
- **THEN** retrieved evidence matches every submitted byte sequence and a forced pre-dispatch storage failure yields zero provider calls and zero device mutations.

#### Scenario: Domain modes and native limitations
- **WHEN** mixed-mode, binding-receipt and export-marker fixtures pass
- **THEN** reports identify simulated interfaces and leave REM-25 native acquisition, external exports and REM-38/39 UI gates open.
