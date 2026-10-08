## Why

The completed offline qualification covers a Linux source build, not the unchanged published ARM apk assets. Wired ownership observation needs actual tool-byte evidence before direct execution can be considered. Existing static QEMU runtimes allow bounded host qualification without tablet contact or global setup.

## What Changes

Extend the existing fixture runner with a separate pinned published-asset evidence mode and explicit verified emulator invocation. Reuse all 13 actual-tool observations for ARMv7 and AArch64; preserve the original source-build receipt and its 417-entry gate. Document asset/source attribution and emulation limits.

## Capabilities

### New Capabilities
- `manager-published-arm-apk`: Offline emulated qualification of exact published ARM tool bytes.

### Modified Capabilities

None; existing source-build behavior remains available.

## Impact

Manager Python fixture orchestration, guards and public guide; linked central Docs change. No UI/transport/installation/release workflow or shipped executable changes. Main owns independent review, coordinated delivery and canonical persistence.
