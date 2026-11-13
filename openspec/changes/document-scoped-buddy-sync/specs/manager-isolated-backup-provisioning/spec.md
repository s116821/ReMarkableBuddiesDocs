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
- **THEN** Manager verifies the stated currency against the actual current mode and original grant binding, rejects another Store actor, and preserves the original outcome independently of newer settings.

#### Scenario: No valid result is received
- **WHEN** output is lost, partial, malformed or supplies no valid root-result custody
- **THEN** Manager preserves uncertainty or the explicit early refusal without manufacturing success or retrying a new operation. A later inspect alone does not reconcile the original result.

#### Scenario: Explicit original retry is selected
- **WHEN** the owner deliberately retries an unresolved operation under a valid current connection and retained custody
- **THEN** the host submits only the exact original input, without rebasing its token, choosing another mode or allocating a replacement intent.
