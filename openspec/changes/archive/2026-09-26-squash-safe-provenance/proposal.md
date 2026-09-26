# Squash-safe migration provenance

## Why

The user's latest instruction requires squash merging every PR until changed. The initial Docs migration must therefore retain verifiable original bytes without depending on the topic import commit remaining in main history. This supersedes the one-time merge-commit requirement.

## What Changes

- Retain one deterministic compressed archive of unique imported Git blobs, keyed by blob ID, with archive SHA-256 in the existing source provenance manifest.
- Verify those stored bytes without Git history, network or live imported files; keep exact source commit/path/blob records and a portable extraction command.
- Retract merge-commit-only guidance and test a fresh shallow clone of synthetic squash history, including absence of the old import commit.

## Capabilities

### Modified Capabilities
- `ecosystem-contribution`: provenance remains verifiable after squash and subsequent edits/removals of imported live artifacts.

## Impact

Docs verification/guidance only. No Rust changes, tags, repository settings or other active-change edits. All PRs use squash under current user direction. Historical source repositories remain unmodified.
