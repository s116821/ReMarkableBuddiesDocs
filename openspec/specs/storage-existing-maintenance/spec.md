# storage-existing-maintenance

## Purpose

Define lease-protected maintenance of already owned local stores without initialization or structural repair.

## Requirements

### Requirement: Existing store maintenance retains ownership
The shared Store SHALL offer an existing-store-only opening path for maintenance,
independent of Reader or subject-memory modules. It SHALL acquire the stable OS
lease once and retain it through maintenance and readback. Before maintenance
writes, it SHALL validate the existing data identity, auxiliary ownership markers,
current non-nil generation, supported format and required directories. Missing,
unsupported or busy storage SHALL refuse without initializing a store or replacing
an ownership marker or generation. Every refusal and completed lifetime SHALL
release the lease. Normal startup initialization SHALL remain available separately.
Source: REM-53 bounded personalization contract; shared Store implementation.

#### Scenario: Incomplete or unsupported owned storage
- **WHEN** a maintenance request finds a missing identity, owner marker, current generation or required directory, or an unsupported format
- **THEN** it refuses without creating the missing state or changing the configuration

#### Scenario: Concurrent owner
- **WHEN** another Store instance holds the stable lease
- **THEN** maintenance reports busy without writing, and can succeed after that owner releases the lease

#### Scenario: Existing store success
- **WHEN** a valid existing store is opened for personalization maintenance
- **THEN** the existing atomic config writer and exact readback execute under its retained lease without initializing a replacement store
