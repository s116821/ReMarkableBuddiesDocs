## Why
The released Linux conversation inventory can discover supported ordinary conversation root IDs, but neither Manager companion exposes it. Explicit read-only discovery fills this existing management gap without requiring users to obtain internal IDs manually or granting deletion/native authority.

## What Changes
- Add one optional identity-only inspectConversations capability and shared snapshot UI over the unchanged parameterless --inspect-conversations producer.
- Strictly distinguish complete-empty from complete candidates and every busy/unavailable/conflict/unsupported/too-large refusal; never truncate or infer eligibility.
- Integrate one eleventh bounded read owner with all ten existing maintenance owners, preserving originals, quiescence, private draft clearing and local Stop semantics.

## Capabilities
### New Capabilities
- `conversation-discovery-companion`: explicit bounded read-only conversation candidate discovery in both browser and Electron, with strict wire/identity and eleven-owner lifecycle.
### Modified Capabilities
None. Existing producer, aggregate report1/report2, storage, cleanup and operation wires remain unchanged.

## Impact
Central Docs plus Manager only. New small private parser/coordinator/helper, typed narrow host method, shared controller/UI/manual and meaningful existing-tool host/fixture coverage; no new dependency, jobs, transport, backend, installer or version source. See design.md for exact authored envelope and acceptance.md for gates. The full same-pair lifecycle continues through source implementation, verification, canonical sync and archive; this proposal is not a planning-only completed release. Device/provider/SDK/native/runtime operations remain outside scope.
