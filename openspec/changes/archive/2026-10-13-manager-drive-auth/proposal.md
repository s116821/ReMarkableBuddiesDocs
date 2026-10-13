# Why
REM42 requires cloud authentication without a connected tablet. The existing Drive transport accepts protected credentials but has no authorization/account-discovery UI. This independent Manager work need not wait for physical Windows or Rust parent integration.

# What Changes
Add explicit Google Drive installed-app sign-in in both shared browser/helper and Electron, actual granted scope/account discovery, protected host token persistence, cancellation/re-authentication/local disconnect and explicit grant revocation. Reuse Google's maintained OAuth client. Do not introduce a sync engine or infer backup/domain/tablet readiness.

# Capabilities
## New Capabilities
- `manager-drive-auth`: bounded host OAuth and shared UI independent of tablet connection.
## Modified Capabilities
None.

# Impact
Manager host, narrow helper/IPC, Angular/Tailwind view, credential-custody helper and required tests/dependency notices. Central paired Docs; starts from accepted Manager10263/Docs1788. Main Rust/provider/domain/settings/native source unchanged. No source project versions or production release/account setup.
