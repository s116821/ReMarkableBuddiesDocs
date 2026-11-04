# Stored historical feedback snapshot

## Why

The delivered static feedback catalog requires an already validated OutcomeFact. The current ordinary Ledger retains typed outcome facts across page unavailability, but has no receiving adapter that resolves one explicit stored fact into that catalog. Existing work leaves pre-page persistence and actual presentation unfinished. Reuse durable facts before introducing another queue or persistence schema.

## What Changes

Add one ordinary, read-only receiving API for an explicit conversation and outcome-fact identity. Validate a single current Conversation-namespace metadata snapshot using existing Ledger decoders/root/chronology checks, then describe the exact retained fact through the existing catalog. Return original historical identities and static text only. Only supported schema-one Failed/Canceled/ReconcileRequired facts produce a description; completed or unsafe records refuse explicitly.

## Scope

Stored, already-associated historical facts only. No new persistent records or queue, acknowledgment/dismissal state, automatic selection, CLI/service/runtime wiring, page rendering or native admission. Pre-attempt errors without durable conversation/turn identity, actual pending presentation and its receipts remain unfinished. A returned historical description cannot establish that it is current, unpresented or safe to render.

## Impact

Proposed Source scope: src/conversation/mod.rs (one child-module registration), new src/conversation/feedback.rs and tests/stored_feedback.rs. Preserve Ledger writers/types, storage/schema/mode implementation, Cargo/SDK pin, OpenAI, Orchestrator, Manager and every other path. Central change remains active until implementation, checks, review, canonical sync and archive in the paired delivery.
