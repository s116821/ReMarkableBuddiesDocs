# Shared Tailwind UI foundation

## Why
Manager already imports pinned Tailwind through Angular PostCSS, but shared shell rules target bare elements, states are inconsistent, and only production utility generation has been checked. Establish explicit reusable conventions for current and future browser/Electron screens (REM-54) without changing release discovery or tablet behavior.

## What Changes
- Keep supported Angular/PostCSS integration and reproducible existing dependency pins.
- Centralize semantic theme tokens and small reusable panel/control/status conventions; migrate the current shell and release preview consistently.
- Verify generated development/production CSS, responsive shared browser and packaged Electron rendering, visible keyboard focus, errors, and disabled controls.
- Document public contribution conventions in Manager docs.

## Capabilities
### New Capabilities
- `manager-shared-tailwind`: shared styling integration, conventions and host verification.
### Modified Capabilities
None. Existing release-source and installation boundaries remain intact.

## Impact
Manager styles/template, Angular development configuration, host checks and contribution docs. One linked Docs/Manager delivery. No tablet, Buddy API, release-engine change or new source-held application version.
