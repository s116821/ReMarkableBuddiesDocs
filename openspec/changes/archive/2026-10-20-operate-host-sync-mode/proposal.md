# Operate persisted sync mode from the host

## Why
The delivered Store has durable explicit modes and lifetime guards, and selected
memory requires a matching chosen mode. There is no supported one-shot mode
command. Operators currently need a custom Rust harness to use this prerequisite.

## What changes
- Add explicit initialize, inspect and choose host commands over the existing Store mode API.
- Preserve the original expected token and operation UUID for conditional choice and exact retry; distinguish historical receipts from the actual current snapshot.
- Hold the existing process/mode lifetime through report output and fence ordinary Reader startup against unsupported modes or selected data.

## Boundaries
This records operator intent; it does not activate sync, verify/join/bootstrap a
remote group, select aggregate membership, restore data, start a service, contact a
tablet/provider or qualify Reader model/native integration. The existing unfinished
document-scoped sync change and frozen Reader drafts remain separate. One paired
Docs/source delivery includes implementation, tests, review, canonical sync/archive
and normal delivery; this is not a planning-only prerequisite PR.
