## Why

The companions already edit several saved declarations, but Reader/Writer role
enablement and note-export backend preference lack a supported producer/editor.
A missing field cannot be presented as a false value or edited through raw JSON.
This increment adds one coordinated capability with actual application admission,
using the existing settings safety model in both browser and Electron.

## What Changes

- Add a dedicated versioned product-settings producer and matching shared editor;
  preserve the delivered basic-v1 and other settings/credential capabilities.
- Support deliberate supported Reader/Writer declarations and the existing Mem
  export backend versus explicitly disabled export, with truthful default/origin
  display and original-file atomic prepare/apply/readback/status semantics.
- Enforce disabled roles/new export before their ordinary side effects, retaining
  maintenance re-enablement and historical uncertain export reconciliation.
- Preserve exact unknown outcomes, original-only status, finite host custody,
  targeted cancellation and shared maintenance ownership across both hosts.
- Publish precise limits: Mem/backend choice is not account/workspace/collection
  setup, arbitrary endpoints, credential installation, live runtime activation,
  installed-service restart, native/provider qualification or all REM-42 delivery.

## Capabilities

### New Capabilities

- `product-settings-companion`: supported declaration editing and application
  admission semantics through the fixed offline producer in both companions.

### Modified Capabilities

None. Older wire contracts remain frozen; the dedicated capability negotiates
its own support.

## Impact

Central Docs and linked Buddy/Manager changes form one delivery. No new runtime
dependency, repository, service API, application version field or product WLAN
management path. Schema/contract revisions are independent of Git-tag releases.
Main owns producer implementation; the matching consumer uses one frozen shared
contract. The shared contract is accepted; final producer/consumer qualification and
coordinated delivery remain pending: see contract-review.md.
