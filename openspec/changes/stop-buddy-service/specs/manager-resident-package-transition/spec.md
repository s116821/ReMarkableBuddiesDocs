## ADDED Requirements

### Requirement: Resident package operations use one closed capability across both hosts
The Manager SHALL expose a distinct bounded residentPackage capability through the
shared browser/Electron host and UI, delegating only disable/remove/replace to the
existing private package helpers and preserving the separate serviceStop contract.

#### Scenario: No qualified production package binding
- **WHEN** a package review is requested with the production qualification bindings empty or without an eligible host-approved candidate
- **THEN** both hosts report unavailable or unsupported before opening configuration/SSH or submitting a service/package command, and the shared UI keeps confirmation disabled.

#### Scenario: Renderer attempts to choose private authority
- **WHEN** a request supplies a version, digest, path, activation, command, trust policy or unknown field instead of the closed public shape
- **THEN** both host routes refuse before peer invalidation or I/O.

### Requirement: Package transitions retain original ownership and unresolved outcomes
The Manager SHALL share MaintenanceIO and unresolved-submission fencing with Stop
and all current maintenance peers, using host-issued references, existing durable
private intents and one absolute deadline without replaying a possible submission.

#### Scenario: Another operation owns maintenance
- **WHEN** package review/confirm races with Stop or a current maintenance peer
- **THEN** only the admitted owner performs invalidation/I/O; Busy and stale cancellation/finally cannot affect it.

#### Scenario: Submission may have happened
- **WHEN** a package phase loses output, times out, is cancelled or its host process exits after possible submission
- **THEN** its original intent remains unknown, both package and standalone Stop refuse another submission for the connection, and only explicit read-only reconciliation of that original operation is offered until its phase is proven settled.

#### Scenario: Original context changes
- **WHEN** connection, boot, activation, profile, ownership, solver/candidate or ready lifetime differs at confirmation
- **THEN** confirmation refuses without dispatch or target substitution.

### Requirement: Wiring preserves existing engines and separate qualification gates
The package capability SHALL use the existing private prepare/recovery/disable/
removal/replacement functions and signature/ownership/lock checks without adding
an installer, Stop engine, generic workflow framework, trust enrollment or product
qualification based on source fixtures.

#### Scenario: Local shared-host and renderer checks pass
- **WHEN** small synthetic fixtures exercise the real browser/Electron routes and shared UI
- **THEN** production qualification registries remain empty and actual signed package/lifecycle/native qualification remains a separate requirement.

### Requirement: Proven intermediate outcomes permit explicit non-replaying continuation
The Manager SHALL bind each new public goal into its existing bounded durable Stop
intent and extend the existing finite Python coordinator to review and submit only
one proven unsubmitted next phase per new explicit continuation confirmation.
Intermediate Stop/disable proof SHALL NOT count as whole removal/replacement success.

#### Scenario: Recovery finishes after the original bounded invocation
- **WHEN** Check proves the original Stop recovered and no downstream phase was submitted, with the original writer positively settled
- **THEN** the host offers a new read-only remaining-step review and separate confirmation for disable only, never resubmitting Stop or renewing the original deadline.

#### Scenario: Disable is reconciled for a longer goal
- **WHEN** the full disabled/recovery/ownership proof is established for the original goal
- **THEN** disable completes, while remove/replace retain their reservation and require a fresh review/confirmation for their absent package phase only.

#### Scenario: Final package phase may have been submitted
- **WHEN** an original removal/replacement intent exists
- **THEN** only its exact terminal observer proof completes that goal; failing proof remains unknown and never permits a repeated package command.

#### Scenario: Host restarts between phases
- **WHEN** protected bounded discovery admits a validated version4 original goal and its phase chain after host restart
- **THEN** the new opaque reference starts fenced/unknown and the same explicit Check, prior-writer exclusion, current review and single-use confirmation rules apply; ambiguous legacy goals, changed candidate/context or contradictory records cannot authorize continuation.

#### Scenario: Continuation review is cancelled or becomes stale
- **WHEN** a remaining-step review is cancelled, expires or is confirmed more than once
- **THEN** no stale invocation dispatches, durable history and the original goal reservation remain, and only goal-specific terminal proof releases the shared fence.
