# Manager workflows

## Purpose
Organize the shared companion around requested user tasks while preserving supported capabilities and operation authority.

## Requirements

### Requirement: Task-oriented Manager navigation
Both browser and Electron SHALL provide Tablet, Settings, Data, and Backup & sync
destinations with secondary Troubleshooting. The first view in a fresh session SHALL prioritize
connection and current tablet state. A host protocol or archive generation SHALL
NOT become a primary navigation destination. Source: maintainer UX correction and
the public Manager outcomes in the revised roadmap.

#### Scenario: Open Manager without a tablet
- **WHEN** Manager starts in a fresh session without a current tablet observation
- **THEN** it shows a focused connection view, truthful availability and navigation to settings and account management rather than every editor at once.

#### Scenario: Navigate while an outcome is unresolved
- **WHEN** a user changes destination with an operation pending or uncertain
- **THEN** navigation does not dispatch or replay it, and its original status remains reachable with the existing lifetime guarantees.

#### Scenario: Hide an unused private editor
- **WHEN** navigation or a nested choice hides a private input or revealed value
- **THEN** its existing clearing policy applies, and a late result cannot re-enable a blank or invisible draft for saving; pending or uncertain original outcomes remain reachable.

### Requirement: Contextual configuration and maintenance
Related settings and maintenance operations SHALL share a user-task context.
Diagnostic settings, protected references, raw saved-state reports and legacy
format details SHALL be secondary controls. Normal language SHALL replace
implementation terminology while retaining saved/default/empty distinctions.
Source: existing Manager configuration and owned-data contracts.

#### Scenario: Configure the model connection
- **WHEN** the user opens model settings
- **THEN** model/backend and protected API-key controls are discoverable together, and credential-reference editing remains a deliberate separate operation within that context.

#### Scenario: Inspect and remove owned data
- **WHEN** the user selects a supported data category and maintenance action
- **THEN** the interface presents the corresponding inspect/preview/confirm flow without exposing unrelated inventories and protocol generations simultaneously.

### Requirement: Truthful and accessible presentation
The renderer SHALL remove obsolete placeholder cards and static status claims,
display supported capability states, remain usable with keyboard and narrow
viewports, and preserve browser/Electron behavior. Sign-in SHALL NOT imply tablet
provisioning or a verified backup. Source: existing host boundaries, Manager
accessibility requirements and the maintainer's Google onboarding clarification.

#### Scenario: Google account is signed in
- **WHEN** host sign-in succeeds but tablet backup setup is unfinished
- **THEN** Manager reports account sign-in separately and does not state that backup is enabled or verified.

#### Scenario: Narrow viewport
- **WHEN** Manager is used at a narrow supported viewport
- **THEN** navigation and the selected workflow remain operable without page-wide horizontal overflow, with visible keyboard focus and labelled controls.
