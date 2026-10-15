## Why
REM-42 requires useful subject-memory inspection in both Manager distributions. The existing Rust query already selects its configured profile and returns bounded global facts with keys, revisions and asserted provenance. Manager need not discover private profile settings or implement another memory provider. Its precise missing transport is a supported bounded stdin request in Main's existing one-shot memory command.

## What Changes
- Add a shared Angular global subject-memory search and strict host request/report boundary using the existing wired observation adapters in browser/helper and Electron.
- Reuse Main's fixed query CLI after its actual stdin contract is published and qualified. Preserve older-build unsupported, busy, disabled, partial and unavailable outcomes.
- Preserve query-only domain semantics, connection/boot identity, bounded input/output, selected current handoff, cancellation and independent component versions.

## Delivery
SCRAPPY owns Manager and this central consumer change. Main owns the Rust CLI/domain input contract; no duplicate backend, remote staging writer or service listener. This active proposal is not a completed feature or separately completed prerequisite PR. Linked implementation and Docs are reviewed/verified/synced/archived together. Full REM-24/42/52, foundation deployment, service control, provider and native gates remain separate.
