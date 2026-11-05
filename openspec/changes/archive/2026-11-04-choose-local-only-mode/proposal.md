## Why

Both Manager companions can inspect saved storage mode, but cannot deliberately choose Local only for an existing Buddy-owned Store. The existing conditional producer supports this bounded action without introducing a sync engine or runtime activation.

## What Changes

- Add a separate Local-only choice panel and host coordinator using the existing fixed mode inspect/choose commands.
- Retain the original conditional request privately and dispatch it once after explicit confirmation.
- Distinguish a validated original receipt, current saved metadata, refusal and an uncertain original operation. Current-state refresh never resolves uncertainty or retries a choice.
- Preserve the existing identity-only read-only inspection capability and all unrelated configuration, storage, cloud and runtime behavior.

## Capabilities

### New Capabilities

- `manager-local-only-mode-choice`: deliberate conditional Local-only choice, bounded private custody, truthful results and both companion interfaces.

### Modified Capabilities

None. `manager-saved-mode-inspection` and `host-sync-mode` remain unchanged.

## Impact

Manager adds a strict public/private protocol, fixed-command wired transport, host coordinator, browser and Electron bridges, shared controller/UI and tests. Docs owns this complete specification lifecycle. Producer source is the existing `host-sync-mode` interface at Buddy `4eeaabef92245173ff136e9773c0416de2653466`; no Rust writer change or new runtime dependency is planned. This does not implement initialization, cloud selection, restore, service control or ordinary/selected runtime integration.
