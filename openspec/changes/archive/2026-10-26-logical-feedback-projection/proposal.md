## Why
The delivered stored-feedback query resolves an explicit historical outcome safely, and the delivered logical conversation planner preserves original turns and draft. Callers currently have no composed path that ties that stored description to the exact turn snapshot used by the plan. An ID-only join could attach historical feedback to stale or changed context.

## What Changes
- Add an explicit ordinary stored-feedback planning API which uses the existing single-snapshot validator and static catalog.
- Require exact stored-turn equality in the supplied chronological layout context, then return the unchanged page plan plus the original historical description and exchange identity.
- Preserve the existing describe_stored and layout plan APIs and all ordinary custody/privacy/refusal behavior.

## Capabilities
### New Capabilities
- None.
### Modified Capabilities
- sanitized-conversation-feedback: compose explicit stored feedback with historical logical layout.

## Impact
Buddy source envelope: src/conversation/feedback.rs, src/conversation_layout.rs, and new tests/stored_feedback_layout.rs only. No Ledger decoder, domain/storage schema, queue, namespace, persistence journal, runtime, CLI, Manager, model, SDK or tablet change. One linked Docs/source delivery will verify, sync and archive this change. Pre-attempt/unassociated error retention, live pending status, actual error-turn persistence, presentation receipts and native rendering remain open.
