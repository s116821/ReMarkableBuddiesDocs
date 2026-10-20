# Manager self-release discovery

## Why
REM-41 requires independent Manager and Buddy release discovery. Current accepted UI polls only Buddy; current Manager build identity is displayed without its own upstream stable candidate. This metadata-only gap is independent of Main Reader/native and installer work.

## What Changes
- Reuse existing polling/cancellation/rate-limit discovery for two fixed official repositories.
- Show current compiled Manager identity and separate latest stable Manager candidate in both shared UIs.
- Reject wrong repository/previews/incomplete Manager asset metadata; retain truthful stale/error/missing states.

## Impact
No updater/download/install/compatibility authority, source version field, third-party dependency upgrade, tablet/provider operation or release engine change. Existing accepted parent heads remain stable; Main retains Rust/release-policy and physical qualification ownership.
