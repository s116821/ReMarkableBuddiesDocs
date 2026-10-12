## ADDED Requirements

### Requirement: Read-only storage CLI route
Runtime SHALL provide `--inspect-owned-data` as an inspection-only route that
returns a versioned report before Store/runtime/provider/sync/device initialization.
It SHALL preserve normal Reader argument behavior, reject conflicting execution
overrides and never perform service or native-document operations for inspection.

#### Scenario: Inspection is distinct from Reader startup
- **WHEN** the real application is invoked for data inspection with missing provider credentials or an unavailable Store
- **THEN** it reports the inspection state without starting the Reader, creating data or resolving credentials, and preserves the existing normal startup behavior on later ordinary invocation.
