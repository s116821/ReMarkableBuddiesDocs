## Why

Saved subject-memory settings already enrich captured Reader answers and standalone
supplied-text Writer notes, but ordinary typed Reader follow-ups, routed Writer
Generate/Refine and notebook reduction omit that context. The local memory
constructor also refuses an already-ready notebook Store because it holds a
legacy-sync lifetime instead of the existing ordinary local-domain lifetime.

## What Changes

- Share the existing configured local Provider with ordinary receiving callers on
  their exact Ledger Store, preserving disabled behavior and selected-mode refusal.
- Admit local memory on an already-ready generation 4 Store through the existing
  ordinary mode/local-domain lifetime; retain legacy constructor and sync fences.
- Add bounded, separately labeled associative snapshots to typed Reader,
  routed Writer Generate/Refine and the existing notebook reducer. Keep exact
  requests, history, original source scope, image associations and draft identity.
- Freeze notebook memory before stage admission and bind it into existing reducer
  reservation/digests; preserve model-free replay and unchanged map inputs.
- Add focused real-Store/caller controls and a separately admitted, bounded enabled
  memory qualification using the existing shared-conversation simulator facilities.

## Capabilities

### New Capabilities

None. This composes the delivered memory and receiving capabilities.

### Modified Capabilities

- `subject-memory`: ordinary receiving callers and already-ready local notebook
  admission, bounded context, reducer binding and replay/failure behavior.
- `local-simulator`: same-path enabled/disabled memory controls and explicit live
  qualification with separate scripted, provider and native evidence.

## Impact

Rust changes are confined to existing local lifetime/memory admission, receiving
callers, notebook payload/preparation, focused tests and simulator documentation.
No new dependency, Store format, memory schema, Provider engine, sync worker,
service, Manager setting or native capability is introduced. Generation 4 is not
silently prepared or upgraded by memory admission. Existing captured Reader and
standalone supplied-text Writer behavior and selected receivers remain intact.

This proposal is based on delivered memory merge
`f6af5d1ce08c7ad518c0943d4a293e7c18688699` and inspected shared receiving source
`200d21733c1a402d3b68a93430f0e05e82e16ca2`. Implementation must reconcile the
eventual delivered shared-conversation successor before edits. This same active
Docs change/PR remains paired with its eventual Rust implementation through
verification, canonical sync and archival; this is not a completed planning
deliverable. Remote shared/isolated sync, native Writer input/effects and wider
memory lifecycle acceptance retain their existing requirements and owners.
