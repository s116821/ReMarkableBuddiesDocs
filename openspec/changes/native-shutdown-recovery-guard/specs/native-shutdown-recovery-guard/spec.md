## ADDED Requirements

### Requirement: Independent guarded one-attempt diagnostic
The development operator SHALL prearm an independent singleton recoveryactor and verify an exact owned runtimefailureguard before the first stockstop. It SHALL admit one fresh process/noncebound selected diagnostic attempt, survive hostloss, and retain one absolute recoverydeadline covering all mutations and final verification.

#### Scenario: Fresh diagnostic admission
- **WHEN** Main selects fresh reviewed packet/baseline and the actor verifies originalpolicy plus effective ownedguard
- **THEN** exactly one diagnostic activation is permitted, with no facts/request admission, getters, input, renderforcing or candidate retry; explicitly selected pretoken mode may install only its fenced setup cohort

#### Scenario: Vendor failure dependencies cannot be cleared by an empty drop-in
- **WHEN** original unit and vendor drop-in contain OnFailure dependencies
- **THEN** only exact-owned runtime full-unit and same-basename vendor shadows derived from pinned originals may remove the scoped dependency, and effective FragmentPath/DropInPaths/ExecStart plus empty OnFailure and guarded policy must be proved before STOP

#### Scenario: Partial guard installation or failed readback
- **WHEN** host loss interrupts installation or guard readback fails before STOP
- **THEN** scoped intent/creation claims and exact hashes authorize cleanup only of owned pieces, foreign/missing protection after admission refuses cleanup/start, and guard policy evidence remains separate from later stock proof

#### Scenario: Host loss or candidate failure
- **WHEN** the host disconnects, the candidate crashes, trace is uncertain or observation expires
- **THEN** the independent actor enters bounded restoration and preserves failure as distinct from healthy currentstock

### Requirement: Explicit pretoken cohort proof selection
Packet preparation SHALL select a distinct strict pretoken parser only for
diagnostic_kind=pretoken-facts-entry-v1, preserving legacy lifecycle-only parsing
for lifecycle-only-v1 and historical selections without a mode. Unknown or malformed
present modes SHALL refuse preparation before output creation. The selected parser
SHALL be bound in the existing packet manifest and identified in the receipt.

#### Scenario: Installation precedes qualifying render
- **WHEN** the selected pretoken snapshot contains exactly one entry-installed event after startup with startup TID, quit_seen=0, dropped=0 and frames=0, then a qualifying before-render with frames>=1 and quit_seen=0 for the same attempt PID/start
- **THEN** one STOP may be admitted under all existing bounded wire and recovery checks, while SDK source and fixtures separately prove the hard no-owner/getter/reader request fence

#### Scenario: Missing or invalid cohort proof
- **WHEN** installation is missing, render occurs only before installation, or installation is duplicated or has invalid scalar fields or TID
- **THEN** no STOP admission follows; missing evidence remains incomplete and invalid evidence is refused, without relaxing legacy wire limits or extending observation

#### Scenario: Installation contradicts prior rendering
- **WHEN** a normal before-render or after-render precedes entry-installed with frames=0, even if another qualifying render follows
- **THEN** the snapshot is invalid because installation cannot reset the actual frame counter, and STOP is not admitted

#### Scenario: Rendering begins after quit
- **WHEN** valid installation is followed only by normal before-render with quit_seen=1 and any late-before-render
- **THEN** the snapshot remains incomplete for the required pre-quit render and cannot admit STOP

#### Scenario: Shared root stimulates the watcher
- **WHEN** actor evidence creation in the existing shutdown root queues FactsEntry request callbacks
- **THEN** the SDK diagnostic fence must still prevent request admission and results are interpreted as a coarse setup/timing cohort rather than proof of an individual cause

### Requirement: Ordered stock restoration
The actor SHALL stop candidate under remainingguard, verify exact attempt PID/start and unitcgroup gone, remove only exactownedactivation/guard, reload, start stockonce and verify original effectivepolicy/hashes/services. Deadline, identity or cleanupfailure SHALL remain failure without retry or false success.

#### Scenario: Candidate gone and cleanup owned
- **WHEN** candidate termination and cgroupabsence are proved underguard
- **THEN** exactownedoverrides may be removed and one stockstart followed by originalpolicy/hash/service verification records restoration separately from diagnostic outcome

#### Scenario: Recovery proof fails
- **WHEN** deadline, process/cgroupidentity or ownedfile validation fails
- **THEN** no policyremoval or additionalstockstart is authorized and evidence remains preserved for Main recovery
