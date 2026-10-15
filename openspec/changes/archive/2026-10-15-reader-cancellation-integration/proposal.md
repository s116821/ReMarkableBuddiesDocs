# Integrate accepted provider cancellation into the current Reader

## Why

The accepted async provider cancellation repair exists in Buddy PR43, but the current Main Reader branch still uses the older blocking HTTP worker. Main's newer ordinary-mode lifetime and receiving context must coexist with that accepted repair. Transport-only cancellation controls do not establish the actual Reader's durable cancellation outcome or absence of later page mutations.

## What Changes

- Reuse only the accepted four-file PR43 commit2a510e825822d3683176fe5607efa6cf6f804e69, preserving its dependency graph and existing client policy.
- Exercise the actual Reader orchestrator, durable Ledger and modeled request ownership guard against an owned local HTTP server withholding its response.
- Cover request-ownership loss during recognition and after verified interpretation during contextual answer generation, preserving cancellation facts and zero page output.
- Correct a real integration defect if these focused controls expose one; do not build another cancellation engine or repeat the accepted transport matrices.

## Scope

Host Reader integration only. No native gesture/device experiment, actual-provider semantic claim, export rollback/billing guarantee, forced timeout reduction or whole REM-40 completion. Reviewed REM-53 PR49/Docs41 remain unchanged drafts with their separate real-provider gate. Unfinished parent delivery remains explicit.
