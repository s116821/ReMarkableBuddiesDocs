# Windows wired read-only observation

## Why

The accepted Linux observer and shared browser/Electron UI currently refuse native Windows. REM-41 requires a supported host transport without routing to wireless or trusting an IP alone. This slice extends read-only observation; installer and package authority remain unavailable.

## What Changes

- Add a Windows host adapter proving selected present USB PnP ancestry, adapter GUID/LUID/index, local source and on-link ordinary/constrained route.
- Bind/read back IP_UNICAST_IF before source bind/connect; preserve fixed peer, pinned host-key-before-auth and bounded reads.
- Validate protected Windows ACLs using maintained pywin32, with no renderer credentials or automatic enrollment.
- Register interface/route/address and selected device change notifications before dial, reject every invalidated generation, and retain deadline/cancellation.
- Exercise actual Windows APIs in hosted CI and request Main's actual Windows/tablet qualification separately.

## Capabilities

### New Capabilities
- `manager-windows-wired-observation`: Windows-specific protected read-only host adapter.

### Modified Capabilities
None; retain the accepted shared contract and Linux behavior.

## Impact

Manager host Python/Node dispatch, pinned Windows dependency, tests and public prerequisites. Central paired Docs/code delivery. No SDK, tablet install, firmware/account/service changes. Actual Windows USB/RM2 evidence belongs to Main, RM1 remains SCRAPPY-DOO.
