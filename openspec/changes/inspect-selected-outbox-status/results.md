# Local implementation evidence

Buddy commit `7d173baae3278ae5176a4f4aba149ffe5ef15207`, tree
`88292442f0518b9a434ebcbd27e120d00a4f5e4d`, implements the accepted V1
contract. The precode is Docs `eb129326bda4a3a6c5cb95dccedcaa92a36420ed`.
Implementation acceptance is recorded in the REM-52 discussion.

The exclusive CLI dispatch runs before application startup. It opens existing
selected-aware maintenance custody, counts typed pending and withdrawn
records and retains the Store through one write and flush. The shared
inventory distinguishes missing directory from I/O failure and applies the
remaining aggregate byte limit to each read. Existing typed inventory and
attempt APIs remain available to callers.

The local Store tests use actual ordinary, selected and feedback generations.
They cover definitive absence, stale and withdrawn intent, corrupt metadata,
unsupported journal type, the exact 4,096-entry and 8 MiB limits and their
one-over refusals. A real notebook format 4 and an interrupted notebook
marker both refuse before the journal containing deliberately corrupt bytes
can affect the result. The output writer tests confirm Busy while a prefix
or flush is failing and successful lease reacquisition after the failure.
The first fixture run established that opening feedback custody alone
leaves format 1. The final fixture uses the explicit format 3 preparation
operation before asserting the version.

The local scope is Windows MSVC with Rust 1.98.1 and synthetic temporary
Stores. Linux hosted validation, independent source review, integration and
delivery remain separate. The broader document-scoped sync change remains
open. This check used no tablet, provider, native adapter or credential
contents.

## Test commands

| Windows command | Result |
| --- | --- |
| `cargo test --locked --offline --lib selected_outbox` | 13 passed, including held output and the entry/byte boundary controls |
| `cargo test --locked --offline --test selected_outbox_status_cli` | 1 passed. Actual executable exits with stdin open, refuses CLI peers without Store creation, and emits exact unavailable, cross-process busy and zero frames |
| `cargo test --locked --offline --bin reader-buddy` | 13 passed, including exact CLI inventory and exclusivity checks against every peer |
| `cargo fmt --all -- --check` | Passed |
| `openspec validate inspect-selected-outbox-status --strict` | Passed |

The library test build reported existing dead-code warnings in notebook writer
test helpers.
