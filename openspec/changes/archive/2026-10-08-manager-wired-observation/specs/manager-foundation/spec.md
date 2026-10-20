## MODIFIED Requirements

### Requirement: Restricted desktop boundary
Electron SHALL isolate and sandbox the renderer, disable Node integration, deny
unexpected navigation/popups/permissions, and expose foundation host identity plus
only separately specified narrow host capabilities. Arbitrary command IPC SHALL
remain unavailable. Neither distribution SHALL connect to a Buddy service API.

#### Scenario: Renderer inspects privileged capabilities
- **WHEN** the foundation screen executes in Electron
- **THEN** Node require/process and arbitrary command IPC are unavailable.
