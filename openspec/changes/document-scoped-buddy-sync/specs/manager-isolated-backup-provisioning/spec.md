## ADDED Requirements

### Requirement: Manager retains the original isolated provisioning intent
The privileged Manager host SHALL prepare an isolated root operation only from a successful existing isolated-mode inspect report. It SHALL retain the original operation UUID, conditional input and snapshot privately before dispatching the fixed Buddy command. A renderer SHALL NOT supply credentials, conditional tokens, provider IDs, commands or paths.

#### Scenario: Existing isolated choice is reviewed
- **WHEN** Manager receives a complete supported inspect result for an isolated mode on its identity-verified wired tablet connection
- **THEN** it may prepare one original private provisioning intent for that device, backup, epoch and grant, without changing mode or treating desktop sign-in as a tablet grant.

#### Scenario: Input does not establish isolated mode
- **WHEN** inspection is unavailable, incomplete, unsupported, malformed or reports another mode
- **THEN** Manager does not prepare or dispatch provisioning.

### Requirement: Manager preserves root evidence and uncertainty
The privileged host SHALL validate the complete bounded provisioning report and correlate its result to the original operation and Store. It SHALL expose only reduced current-mode and root-result metadata. Root preparation SHALL NOT be represented as a completed backup, runtime activation or native readiness.

#### Scenario: Current or historical result is received
- **WHEN** a result identifies the original operation, device, backup and epoch
- **THEN** Manager verifies exact current token/epoch agreement, the persisted Store device and original backup grant continuity, rejects contradictory or unconfigured snapshots, and preserves valid historical outcomes independently of newer settings.

#### Scenario: No valid result is received
- **WHEN** output is lost, partial, malformed or supplies no valid root-result custody
- **THEN** Manager preserves uncertainty or the explicit early refusal without manufacturing success or retrying a new operation. Parsing failures expose only a fixed redacted refusal. A later inspect alone does not reconcile the original result.

#### Scenario: Explicit original retry is selected
- **WHEN** the owner deliberately retries an unresolved operation under a valid current connection and retained custody
- **THEN** the host submits only the exact original input, without rebasing its token, choosing another mode or allocating a replacement intent.

### Requirement: Host process restart preserves original custody
The host SHALL flush, replace and reread the exact private original before dispatch. Its fixed private version-1 file SHALL retain at most eight append-only originals with a 512-byte input, 2,048-byte record and 20,480-byte aggregate bound. The retention writer SHALL use an independent OS-held lock released on process exit and SHALL NOT change OAuth credential writer behavior. No original SHALL be silently replaced or evicted.

#### Scenario: Helper exits while holding its retention writer
- **WHEN** the storage helper is interrupted during a write
- **THEN** another process can acquire the retention lock after that process exits, validates the retained file before use, preserves unrelated credentials, and dispatches nothing unless the original is acknowledged and reread successfully.

#### Scenario: Restart recovers an unresolved original
- **WHEN** the host reloads a retained operation
- **THEN** it validates the exact input digest and snapshot agreement, displays unknown outcome independently of any later pending or refusal report, and permits only explicit same-input replay on the retained connection and boot. Only correlated root-verified evidence settles that original, and its actor/epoch reservation remains retained.

#### Scenario: Storage cannot establish custody
- **WHEN** the retained file is malformed, oversized, stale, full, or cannot be privately read and conditionally updated
- **THEN** Manager refuses dispatch with a fixed storage error. Process-restart evidence SHALL NOT be represented as system-crash, power-loss or storage-rollback qualification.
