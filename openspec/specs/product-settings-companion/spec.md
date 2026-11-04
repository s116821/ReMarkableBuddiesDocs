# Product settings companion

## Purpose

Provide supported Reader/Writer enablement and export-backend declaration editing
in both companions, with effect admission, original-file save custody and truthful
saved-versus-running limits.

## Requirements

### Requirement: Supported saved product declarations in both companions
Both browser and Electron companions SHALL inspect and deliberately edit only the
agreed producer's saved Reader/Writer and export-backend declarations, preserving
origins, defaults, independent clearing and unrelated configuration. Unknown or
unsupported fields/versions SHALL refuse without inventing values or raw editing.
Source: current REM-42 configuration-completeness requirement and producer review.

#### Scenario: Missing declarations retain compatible defaults
- **WHEN** supported settings are absent and the user inspects them
- **THEN** the UI distinguishes defaults from saved declarations, preserves the existing enabled/enabled/Mem behavior and writes no configuration merely to inspect it.

#### Scenario: Independent edit or capability refusal
- **WHEN** a user sets or clears a supported declaration, or the producer cannot support the requested schema
- **THEN** the former preserves sibling/unrelated declarations under the frozen contract and the latter refuses explicitly without a fallback write.

### Requirement: Disabled roles and export refuse new effects
The application SHALL enforce supported disabled Reader/Writer/new-export policy
at each affected entry before its credential, Store, device/model or provider
effects. Disabling SHALL not remove records or third-party notes. Maintenance
and original historical reconciliation SHALL retain their independent boundaries.
Source: REM-42 actual configuration behavior and preservation requirements.

#### Scenario: Re-enable without trapped maintenance
- **WHEN** Reader or Writer is disabled and an ordinary/new role action is attempted
- **THEN** it refuses before its effects while fixed settings maintenance stays available to inspect or re-enable it without model/Mem credential resolution.

#### Scenario: Disabled export with an uncertain original
- **WHEN** export is disabled after an earlier export becomes uncertain
- **THEN** new export dispatch refuses, while an explicit original historical check may remain available without granting another dispatch or inventing a replacement association.

### Requirement: Immutable save and truthful observation
Each deliberate save SHALL bind the original inspected configuration and private
patch to at most one apply, validate saved readback, and preserve unknown outcomes
separately from later desired-file observations. Saved success SHALL not claim
running activation, credential selection or provider/native readiness.
Source: REM-42 atomic configuration and safe failure acceptance.

#### Scenario: Stale conditions or lost reply
- **WHEN** the original file changes or an apply reply is unavailable after possible dispatch
- **THEN** a proved conflict stays distinct from unknown effect, with no automatic retry, refreshed base or rollback claim.

#### Scenario: Original desired file is observed
- **WHEN** an explicit original-only status observes the desired saved file
- **THEN** it reports only that observation, preserving historical uncertainty and runtime activation as separate facts.

### Requirement: Shared bounded maintenance and clear scope
Both companions SHALL use the fixed wired producer, exact response context,
shared maintenance ownership, finite nonrenewing custody and timely draft/DOM
clearing. A canceled unconsumed grant SHALL remain revoked after arrival fences.
Mem/backend preference SHALL not masquerade as account/destination provisioning.
Source: REM-42 host consistency, credential privacy and no service API constraints.

#### Scenario: Busy or stale cancellation
- **WHEN** another admitted maintenance operation owns I/O or an old cancel arrives
- **THEN** Busy preserves the owner before hooks/I/O and the cancel cannot revoke a newer action or preparation.

#### Scenario: Stop followed by delayed save
- **WHEN** Stop revokes an unconsumed preparation and its original save arrives after a short arrival fence
- **THEN** no apply dispatch occurs, while a genuine uncertain dispatched original stays historically unknown rather than rolled back.

#### Scenario: Backend preference without account setup
- **WHEN** the UI offers the existing Mem backend or disabled export
- **THEN** it labels that bounded preference and keeps account/workspace/collection, credentials and runtime/provider qualification explicitly separate.
