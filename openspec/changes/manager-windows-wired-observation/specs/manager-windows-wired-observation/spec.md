## ADDED Requirements

### Requirement: Windows USB and socket proof
The Windows host SHALL require a selected present USB physical device ancestry correlated to adapter GUID/LUID/index/source and on-link ordinary and interface-constrained routes. It SHALL set IP_UNICAST_IF and verify the host-order readback before source bind and fixed tablet SSH connection. Missing, changed, ambiguous or unsupported proof SHALL refuse without fallback.

#### Scenario: Wireless route or option refusal
- **WHEN** the ordinary route uses another interface or Winsock cannot prove the requested binding
- **THEN** no tablet authentication or observation is published

### Requirement: Windows protected authentication and generation
The Windows host SHALL require current-user-owned protected local configuration and private-key handles, independently pinned host-key verification before authentication, and fixed bounded read-only operations. It SHALL register selected-device and network notifications before dial, invalidate any changed operation, close its socket and refuse stale publication even after reattachment.

#### Scenario: Removal during an authenticated read
- **WHEN** a selected device or network change occurs while reading
- **THEN** the owned operation is cancelled and its observations remain unavailable until explicit reconnect

### Requirement: Shared Windows delivery and evidence boundaries
Windows browser/helper and sandboxed Electron SHALL use the same existing read-only adapter/result contract and protected host configuration. Actual Windows API tests SHALL be distinguished from fixtures and physical tablet qualification; unperformed hardware gates SHALL remain explicit, with installation unavailable.

#### Scenario: Fixture success without physical qualification
- **WHEN** host CI passes synthetic observations and native OS API controls without a connected tablet
- **THEN** documentation records those checks without claiming supported tablet or cable-removal qualification
