## ADDED Requirements

### Requirement: Independent guarded one-attempt diagnostic
The development operator SHALL prearm an independent singleton recoveryactor and verify an exact owned runtimefailureguard before the first stockstop. It SHALL admit one fresh process/noncebound lifecycle-only attempt, survive hostloss, and retain one absolute recoverydeadline covering all mutations and final verification.

#### Scenario: Fresh diagnostic admission
- **WHEN** Main selects fresh reviewed packet/baseline and the actor verifies originalpolicy plus effective ownedguard
- **THEN** exactly one diagnostic activation is permitted, with no facts/getters/input/renderforcing or candidate retry

#### Scenario: Vendor failure dependencies cannot be cleared by an empty drop-in
- **WHEN** original unit and vendor drop-in contain OnFailure dependencies
- **THEN** only exact-owned runtime full-unit and same-basename vendor shadows derived from pinned originals may remove the scoped dependency, and effective FragmentPath/DropInPaths/ExecStart plus empty OnFailure and guarded policy must be proved before STOP

#### Scenario: Partial guard installation or failed readback
- **WHEN** host loss interrupts installation or guard readback fails before STOP
- **THEN** scoped intent/creation claims and exact hashes authorize cleanup only of owned pieces, foreign/missing protection after admission refuses cleanup/start, and guard policy evidence remains separate from later stock proof

#### Scenario: Host loss or candidate failure
- **WHEN** the host disconnects, the candidate crashes, trace is uncertain or observation expires
- **THEN** the independent actor enters bounded restoration and preserves failure as distinct from healthy currentstock

### Requirement: Ordered stock restoration
The actor SHALL stop candidate under remainingguard, verify exact attempt PID/start and unitcgroup gone, remove only exactownedactivation/guard, reload, start stockonce and verify original effectivepolicy/hashes/services. Deadline, identity or cleanupfailure SHALL remain failure without retry or false success.

#### Scenario: Candidate gone and cleanup owned
- **WHEN** candidate termination and cgroupabsence are proved underguard
- **THEN** exactownedoverrides may be removed and one stockstart followed by originalpolicy/hash/service verification records restoration separately from diagnostic outcome

#### Scenario: Recovery proof fails
- **WHEN** deadline, process/cgroupidentity or ownedfile validation fails
- **THEN** no policyremoval or additionalstockstart is authorized and evidence remains preserved for Main recovery
