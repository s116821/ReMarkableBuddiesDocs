## Why

REM-4 requires reusable indexes to supply the relevant original document to each
Reader question. The owned disk cache already reloads exact-key normalized inputs,
while ordinary receiving consumes a retrieval Provider. There is no adapter between
these delivered local APIs, so each caller must perform its own load/query wiring.

## What Changes

- Implement the existing retrieval Provider for an already-open DiskCache.
- Load and validate the caller's complete independently selected key on each query,
  then use the existing rebuilt Index and unchanged query/budget semantics.
- Refuse absent cached material, preserving the distinction from a valid no-match.
- Qualify actual local cache/receiving integration across restart and replacement.

## Capabilities

### Modified Capabilities
- `normalized-source-cache`: direct exact-key Provider consumption by ordinary receiving.

## Impact

Rust retrieval/disk.rs, focused cache/receiving fixtures and reusable guidance.
No schema, dependencies, acquisition, installed workflow, SDK, model, network,
configuration, cleanup or native effects change. This is local data integration;
automatic Reader selection/ingestion and live acceptance remain unfinished.
