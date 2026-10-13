# Manager owned-data inspection

## Why
REM-42 has a reviewed read-only Rust CLI report, but neither shared Manager host shows it. Users need observed sizes and explicit incomplete states before future maintenance.

## What Changes
- Extend the existing wired host adapters with one parameterless inspection action using the fixed installed CLI and normal nonsecret configuration.
- Validate report_version1 and render shared Angular/Tailwind categories, consequences and incomplete reference states in browser and Electron.
- Reject stale connection results, unsupported installed commands and unknown report schemas.

## Impact
Main retains Rust/CLI and inspect-owned-data ownership. This new Manager-owned change leaves cleanup, restore, settings, provider authentication, package provenance and whole REM-42 open. No Buddy listener, installation, native document access or live tablet operation is required for fixtures.
