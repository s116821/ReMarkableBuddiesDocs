## Why
REM-4 requires default external research with a configurable alternative policy.
The delivered research stage accepts caller-supplied Required/Disabled policy and
NoInternet, but Config has no persisted policy. A deliberate saved-setting producer
and typed snapshot can close that independent configuration gap without claiming
that the held Reader runtime or a live provider consumes it.

## What Changes
- Add an optional research_policy declaration and a pure immutable typed snapshot.
- Add bounded dedicated saved-policy inspect/prepare/apply/status operations using
  the existing conditional configuration writer and custody.
- Feed a snapshot from actual saved configuration into the existing research API
  in real local integration tests, preserving request/history and opt-out priority.

## Capabilities
### New Capabilities
- `saved-research-policy`: deliberate saved policy and typed local consumption.

## Impact
Rust config/main early maintenance dispatch, focused fixtures and guidance; central
Docs only. No Manager files, runtime dispatch/prompt, provider acquisition, gesture,
SDK, dependency, configuration-schema bump or CI-graph change. Older builds may
refuse the new declaration/command; no unsupported cross-version claim follows.
