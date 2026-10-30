# Manager Google Drive authentication

## Purpose
Provide explicit Google Drive sign-in and protected credential lifecycle on the Manager host independently of a connected tablet. This bounded capability does not enable backup inspection, domain synchronization or tablet restore.

## Requirements

### Requirement: Explicit maintained Google Drive authorization independent of tablet
Both Manager distributions SHALL use a separately configured desktop client and maintained OAuth library for explicit external-browser S256/state/code flow, granted drive.appdata verification and actual account discovery. Host token/account/client identity SHALL be checked before reporting a fresh connection. No tablet connection or native/backup readiness SHALL be inferred.

#### Scenario: Sign in without a tablet
- **WHEN** the user starts sign-in and valid current consent/account/scope completes
- **THEN** the Manager commits the protected host grant and displays a fresh account connection independently of USB.

#### Scenario: Wrong, stale or failed consent
- **WHEN** callback state/shape/client/scope/account mismatches, expires or the network refuses
- **THEN** the grant is not replaced and status stays truthful without exposing callback/code/token diagnostics.

### Requirement: Bounded host-only credential custody and narrow shared actions
The host SHALL keep tokens/verifiers out of renderer/localStorage/argv/logs, enforce owner-only regular nonlink/reparse bounded storage and atomic guarded persistence, restrict IPC/helper to fixed authenticated actions, and bound listener/request duration and response bytes. Unavailable protected storage SHALL refuse without widening permissions or creating usable insecure grants.

#### Scenario: Successful protected host operation
- **WHEN** login/check runs through the helper or authorized Electron main frame
- **THEN** only sanitized status/account metadata or the fixed consent URL reaches the UI; token data stays under host custody.

#### Scenario: Unauthorized caller or insecure path
- **WHEN** caller origin/session/frame/action is invalid or storage ownership/ACL/path/size changes
- **THEN** the action refuses and no credential is echoed or persisted insecurely.

### Requirement: Cancellation and explicit credential lifecycle are truthful
The host SHALL prevent stale results after cancellation/replacement/disconnect, preserve a prior grant until a new fully verified guarded commit, distinguish cached from fresh provider state, and support local disconnect and separately confirmed provider revocation. Revocation errors SHALL NOT be labeled success. No Drive backup object or tablet setting SHALL be modified by this capability.

#### Scenario: Late completion after cancel or disconnect
- **WHEN** an earlier code/token/account response arrives after its flow is invalidated
- **THEN** it cannot commit/resurrect credentials or change the current UI account.

#### Scenario: Restart or revocation
- **WHEN** stored metadata is loaded after restart or a revocation request fails/has uncertain outcome
- **THEN** the UI reports cached/unverified or failed/uncertain state rather than claiming a fresh connection or revoked grant.
