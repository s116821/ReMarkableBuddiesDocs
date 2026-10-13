## MODIFIED Requirements

### Requirement: Shared UI with protected local host boundary
Browser and Electron SHALL use the same Angular observation UI and versioned adapter. The observation interface SHALL expose only narrow authorized observation/cancel calls. Separately specified owned-data inspection, provider authorization, personalization, binary identity and verified Manager download capabilities SHALL expose their own narrow authorized fixed actions without allowing arbitrary renderer commands or weakening observation, trust, origin/session or main-frame boundaries. Browser transport SHALL have an explicit user-launched loopback helper and host-controlled setup, with origin/session validation; ordinary webpages SHALL not directly open SSH or discover arbitrary local hosts.

#### Scenario: Browser helper ownership
- **WHEN** the user opens the helper-served local UI with protected host configuration
- **THEN** the same observation path is available without renderer access to authentication or arbitrary commands, while remote origins and unsupported hosts fail closed and show their setup boundary
