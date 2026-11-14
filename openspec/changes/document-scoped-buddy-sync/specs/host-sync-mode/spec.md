## ADDED Requirements

### Requirement: Explicit isolated backup root provisioning
The host SHALL expose one bounded explicit provisioning command for a chosen ordinary format-1 isolated backup. It SHALL use an existing Store, an original conditional mode token and an original operation UUID. Normal mode inspection, choice and startup SHALL NOT create a provider root. The control SHALL respect Store Busy state without stopping the service.

#### Scenario: First provisioning for a chosen backup
- **WHEN** an explicit request matches current ordinary isolated mode and a qualified protected tablet grant
- **THEN** the command durably reserves the original for the device, backup and epoch, persists one provider-generated ID before create and records verification only after exact-ID app-data readback.

#### Scenario: Restoring the original after a lost result
- **WHEN** root creation or command output may have succeeded without an acknowledgment
- **THEN** an exact original request reconciles the recorded ID first, a current original may repeat only the same-ID create, and a stale original may only observe. Missing or corrupt reserved custody requires recovery without an alternate ID or fresh genesis.

#### Scenario: Leaving or advancing the epoch
- **WHEN** a mode transition retires the original epoch
- **THEN** a new backup identity requires its own root and old evidence remains historical. An unchanged backup identity may be explicitly readmitted only from its original verified root and settled package state with continuous mode history.

#### Scenario: Reporting a root outcome to the wired host
- **WHEN** the provision command reaches an outcome under valid local custody
- **THEN** it reports the original operation, device, backup, epoch, outcome and currency using the bounded consuming mode report. Credentials and private provider IDs stay outside the result. Status distinguishes verified root, unresolved outcome, authorization, retry, recovery and an unqualified binding. A root result grants no package, runtime or native authority.

#### Scenario: Inspecting private isolated root custody offline
- **WHEN** an offline owned-data inventory encounters the fixed private isolated publisher layout
- **THEN** it counts only recognized regular checkpoint, lock and staging files through the existing bounded no-follow traversal. It reports unexpected layout or unsafe entry conditions without disclosing checkpoint contents or granting provider authority.

## MODIFIED Requirements

### Requirement: Ordinary startup respects chosen mode
Normal ordinary Reader startup SHALL admit absent or LocalOnly mode with compatible legacy sync and nonselected data. It SHALL also admit ordinary format-1 isolated mode for local Reader and Writer when legacy sync and shared Reader and memory selection are absent. The admitted runtime SHALL hold its current mode and compatible Store data lifetimes through use. Unsupported mode or storage SHALL refuse before model, device or domain initialization. Mode metadata SHALL NOT grant sync, provider or native authority.

#### Scenario: Shared choice precedes normal startup
- **WHEN** the ordinary startup route encounters an explicit shared mode or selected data requiring a selected route
- **THEN** it refuses before model or device initialization and cannot continue as ordinary local history.

#### Scenario: Runtime owns ordinary lifetime
- **WHEN** an admitted ordinary runtime is alive
- **THEN** mode replacement or selected activation refuses until its mode and compatible data guards are released.

#### Scenario: Isolated mode starts without qualified backup
- **WHEN** ordinary format-1 isolated mode is admitted and the root, protected grant or provider is unavailable
- **THEN** local use remains available. Redacted isolated health describes available evidence. Unqualified applications refuse before credential access, and existing verified backup identity is preserved when valid local custody supplies it.

#### Scenario: A verified isolated root is available to the Worker
- **WHEN** the exact current admission, protected qualified grant, saved Config and recorded root can be verified
- **THEN** the existing Worker may publish the original format-1 package through the admitted binding. Startup and the Worker do not create or choose another root.
