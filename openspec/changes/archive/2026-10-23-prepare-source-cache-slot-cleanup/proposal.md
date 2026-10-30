# Prepared cleanup of one owned derived source-cache slot

## Why
The existing library can forget a selected normalized source, but the management
plane has no bounded preview/confirmation/readback CLI. Its ordinary open path
may initialize files and clean staging, which cannot implement a pure preview.
Selective cleanup must preserve original documents and all durable source history.

## What changes
Add a Linux-only version1 one-shot source-cache-maintenance CLI with inspect, prepare, apply
and status. Admit an existing ordinary Store and existing normalized-sources-v1
namespace without initialization, repair or staging cleanup. Bind one unchanged
canonical document slot to an original private intent and retain both leases
through consuming report output. Report deletion uncertainty honestly.

## Scope
Central Docs plus Rust producer only. Manager integration remains subsequent work
for both browser and Electron; neither distribution gains an implicit capability.
No cleanup of other domains, recursive deletion, source acquisition, cache
freshness claims, credentials/provider/runtime/native work or service controls.
Existing DiskCache open/install/load/forget callers keep their current behavior.

## Delivery
One linked Docs/Rust delivery, concrete contract review before source edits,
Linux synthetic operation qualification and Windows early-unsupported controls, canonical sync and completed archive,
Docs-first normal squash, then actual-main/publication verification. No hardware
or provider action is needed for this local storage contract.
