## ADDED Requirements

### Requirement: Explicit development tap with production echo observation
The helper SHALL expose tap-echo only through a nondefault development diagnostic
feature and SHALL reuse the production InputObserver, ContactFrames and owned-touch
watch unchanged for one existing tap. It SHALL reject unsupported scope and invalid
coordinates before contact and SHALL NOT grant product navigation authority.

#### Scenario: Positively observed contact
- **WHEN** the selected supported diagnostic completes both writes and every existing owned-touch observation check succeeds
- **THEN** it reports echo observed with UI acknowledgement and native navigation qualification false, without capture or another contact.

#### Scenario: Failed down or release
- **WHEN** a touch write fails after an owned window begins
- **THEN** release and finish observation are each attempted, and no success receipt or capture occurs.

#### Scenario: Missing or unsafe observation
- **WHEN** echo is absent, incomplete or unexpected, source identity or inventory changes, other input occurs, or an existing window limit fails
- **THEN** the diagnostic fails without retry or an inferred UI/kernel diagnosis.

#### Scenario: Default product build
- **WHEN** the development feature is disabled
- **THEN** the diagnostic entry and command are unavailable and existing product input behavior remains unchanged.
