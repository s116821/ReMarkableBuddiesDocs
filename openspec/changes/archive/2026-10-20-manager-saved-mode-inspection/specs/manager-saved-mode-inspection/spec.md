## ADDED Requirements

### Requirement: Shared explicit saved-mode inspection
Both browser and Electron Manager SHALL inspect saved mode through the existing identity-verified wired host adapters and only the fixed one-shot inspect command. Renderer input SHALL carry only current connection/boot identity. This capability SHALL NOT expose initialize/choose, arbitrary commands/paths, configuration or storage writes, service control, provider/native activation or a Buddy service API.

#### Scenario: Supported saved choice
- **WHEN** an admitted wired target supports the fixed inspection contract and returns a valid saved choice
- **THEN** both companions display the same saved mode and relevant Buddy device/group/backup metadata without activating or changing it.

#### Scenario: Unsupported or busy target
- **WHEN** the command or report version is unsupported, or existing Store ownership prevents inspection
- **THEN** the UI preserves unsupported or Busy status without a private-file fallback, service stop, automatic retry or invented LocalOnly result.

### Requirement: Bounded inspection and reduced host authority
The host SHALL accept only a bounded valid inspect report-v1 with activation_performed=false, known statuses and exact typed shapes. It SHALL consume snapshot data only from an ok complete report with null receipts, reject malformed/duplicate/oversized/partial output and validate existing mode identities. Conditional tokens, actors, binding/root details and receipts SHALL be discarded before any browser or Electron renderer response; the shared UI SHALL accept only the separately validated reduced view.

#### Scenario: Private fields are present in a valid backend report
- **WHEN** the producer returns its valid conditional token and stored binding/root metadata
- **THEN** the host validates them privately and returns only saved display metadata, with those private fields absent from both host bridges and renderer state.

#### Scenario: Refused or incomplete output
- **WHEN** output is oversized, truncated, nonzero-exit, malformed, unknown or not an ok complete snapshot
- **THEN** no healthy mode snapshot is displayed, truthful supported refusal status remains visible, and neither truncation nor missing data is converted into an unconfigured success.

### Requirement: Saved mode is distinct from runtime readiness
The UI SHALL distinguish unconfigured legacy policy, explicit LocalOnly, isolated backup and shared group. A saved choice or identity SHALL NOT imply current service/sync health, provider qualification, group bootstrap/membership, native authority or hardware identity. Inspecting unconfigured state SHALL NOT initialize or choose a mode.

#### Scenario: No explicit choice exists
- **WHEN** a valid complete inspect snapshot has null mode/device/epoch
- **THEN** both UIs show no explicit saved mode, without labeling it LocalOnly or claiming any worker is inactive.

#### Scenario: Shared or isolated metadata exists
- **WHEN** a valid snapshot identifies a shared group or isolated backup
- **THEN** its saved identity is displayed separately from unverified runtime/provider health and does not authorize another operation.

### Requirement: Inspection results belong to the current session
Inspection replacement, cancellation, disconnect and explicit tablet-state refresh SHALL clear the old view and invalidate pending results. Both host and controller SHALL verify matching connection/boot identity; late or mismatched results SHALL NOT repopulate a new session, including a refresh with unchanged IDs.

#### Scenario: Inspection completes after invalidation
- **WHEN** an old inspection completes after cancellation, replacement, refresh or connection/boot change
- **THEN** its snapshot is ignored and cannot restore stale mode metadata or authorize a follow-up action.

Source traceability: Manager main87ba4e7, producer Buddy67 source1a068730 and central operate-host-sync-mode precode d7479bf; exact ownership, bounds and evidence separation are recorded in design.md. These are planned consumer requirements until verified in the linked implementation delivery.
