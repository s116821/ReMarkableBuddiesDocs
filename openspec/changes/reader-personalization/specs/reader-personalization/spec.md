## ADDED Requirements

### Requirement: Verified Reader answer preferences
The Reader SHALL apply a validated enabled nonempty configuration preference once in its receiving answer context after independent question verification, separately from recognition, visible transcript and subject memory. The current explicit request and fixed operation, source and output contracts SHALL outrank the preference. Source traceability: REM-53 receiving context and precedence requirements; accepted configuration Rust PR39.

#### Scenario: Preference without subject memory
- **WHEN** a prepared Reader request passes independent question verification and has an enabled nonempty preference with memory absent or disabled, or after a successful complete-empty memory retrieval
- **THEN** one subsequent answer request includes the preference as separate configuration context and preserves the exact verified question and existing operation guards

#### Scenario: Configured memory retrieval refusal
- **WHEN** configured subject memory reports unavailable, fails retrieval or returns partial results without usable facts
- **THEN** the existing refusal remains in force and personalization does not bypass it or publish the preliminary answer

#### Scenario: Preference with subject memory
- **WHEN** a verified Reader request has both an enabled preference and usable subject memory
- **THEN** one answer regeneration contains both distinct contexts without duplicating preference or fabricating a conversation turn

#### Scenario: Recognition disagreement
- **WHEN** independent question verification disagrees or refuses the question
- **THEN** no personalized answer request or output is attempted

### Requirement: Immutable startup preference and default preservation
The Reader SHALL use the accepted validated startup snapshot for requests in that process. Disabled or empty preferences SHALL preserve the prior provider sequence. Disk maintenance SHALL retain restart-required semantics without claiming running activation. Source traceability: REM-53 next-request activation requirement, bounded here to startup only; accepted configuration and Manager activation distinction.

#### Scenario: Disabled or empty preference
- **WHEN** configuration has no enabled nonempty preference
- **THEN** the Reader follows its existing recognition and optional memory request sequence without an additional personalization request

#### Scenario: Saved edit during a running request
- **WHEN** configuration maintenance saves a different preference while an existing process has a startup snapshot
- **THEN** the in-flight request retains its snapshot and the save does not report the running process as activated

### Requirement: Ordinary runtime memory admission
The ordinary Reader receiving integration SHALL accept only actual local memory while preserving current-main verification and output guards. Enabled selected memory SHALL refuse before credentials/provider/device initialization or any Store/config mutation rather than fall back to global or unverified selected context. Disabled memory SHALL remain ineffective. Ordinary historical captures SHALL NOT fabricate document association or selected admission.

#### Scenario: Unsupported selected memory is explicit
- **WHEN** the ordinary runtime starts with enabled memory selecting a shared profile identity
- **THEN** it refuses after configuration validation but before credentials/provider/device initialization or any Store/config mutation, leaves records unchanged and grants no selected/native permission.

#### Scenario: Disabled selection does not become active
- **WHEN** memory is disabled but retained settings include a selected identity
- **THEN** no memory consumer is created and an otherwise valid preference follows the ordinary preference-only path.

#### Scenario: Helper cannot admit selected memory
- **WHEN** a caller supplies a selected QueryResult to the ordinary answer-context helper
- **THEN** the helper refuses before touching the engine rather than treating its presence as selected admission.
