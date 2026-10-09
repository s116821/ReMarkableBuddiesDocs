# Manager wired read-only observation

## Purpose

Describe the completed bounded Linux USB/SSH observation capability through shared
Angular browser/helper and Electron hosts. It does not qualify native Windows,
physical cable removal, RM2/Paper Pro, compatibility, package ownership or installation.

## Requirements

### Requirement: Authenticated wired read-only observation
The Manager SHALL offer explicit bounded read-only tablet observations through a versioned host adapter only after verifying selected USB parent/interface identity, on-link route, interface-bound socket and an independently configured SSH host key before authentication. Protected authentication SHALL remain host-owned; no Buddy admin API or arbitrary renderer commands SHALL be exposed.

#### Scenario: Observe configured USB tablet
- **WHEN** the user explicitly requests observation through a supported configured host
- **THEN** bounded known-file and OS reads return sanitized actual model/firmware/architecture/service observations, while unsupported installed-version/provenance remains unknown and installation stays disabled

#### Scenario: Unconfigured or untrusted connection
- **WHEN** host setup/authentication is missing, USB/route proof fails or the peer key differs
- **THEN** the Manager reports the appropriate setup/disconnected/untrusted state without authenticating an untrusted peer, switching targets or changing the tablet

### Requirement: Cancellation and identity invalidation
The Manager SHALL bound operations, invalidate old observations/results on cancellation, timeout, cable/route/interface or tablet boot change, and require explicit reconnection after failure rather than silently changing targets.

#### Scenario: Cable loss or stale result
- **WHEN** the selected connection changes, an operation times out or the user disconnects while a read is pending
- **THEN** the owned operation is cancelled and previous state cannot be presented as current or replaced by a late result

### Requirement: Shared UI with protected local host boundary
Browser and Electron SHALL use the same Angular observation UI and versioned adapter. Electron SHALL expose only narrow authorized observation/cancel calls. Browser transport SHALL have an explicit user-launched loopback helper and host-controlled setup, with origin/session validation; ordinary webpages SHALL not directly open SSH or discover arbitrary local hosts.

#### Scenario: Browser helper ownership
- **WHEN** the user opens the helper-served local UI with protected host configuration
- **THEN** the same observation path is available without renderer access to authentication or arbitrary commands, while remote origins and unsupported hosts fail closed and show their setup boundary
