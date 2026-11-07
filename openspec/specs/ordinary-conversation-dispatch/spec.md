# Ordinary conversation dispatch

## Purpose

Implemented ordinary-local dispatcher and bounded Reader/Writer/notebook receiving APIs. Typed input and completion/effect facts must be supplied by their verified owners; this contract does not claim native composer/page integration or enabled subject memory. See the [finite delivery](../../changes/archive/2026-11-06-unify-ordinary-conversation-dispatch/verification.md) and [unfinished integration](../../changes/unify-ordinary-conversation-dispatch/proposal.md).

## Requirements

### Requirement: Shared ordinary local dispatch
The ordinary local application SHALL route through a shared coordinator using the existing module settings and Ledger. The coordinator SHALL preserve exact request and eligible history, route only admitted intents, and retain one active operation. It SHALL exclude background nonlocal activation from this path.

#### Scenario: Switch receiving buddies
- **WHEN** a request is admitted to a different enabled buddy in the current conversation
- **THEN** the receiver gets the unchanged request and ordered Ledger history, with bounded verified associated media and separate preset and personalization content.

#### Scenario: Verified Writer visibility
- **WHEN** the page owner confirms the exact Writer response for its current draft, operation and visit
- **THEN** subsequent receivers see the exact response as a completed turn in the same exchange, while the original draft remains available for refinement and export.

#### Scenario: Shared historical image bytes
- **WHEN** multiple historical sources use identical verified PNG bytes
- **THEN** the receiving payload carries one attachment and retains each ordered source and ordinal association with its dimensions, attachment index and content digest.

#### Scenario: Bounded notebook receiving
- **WHEN** a fresh notebook generation or refinement is admitted against an existing ready local notebook Store
- **THEN** the existing stage runner processes the exact selected source and history, and the reducer receives digest-bound historical image attachments within the receiving budget.

#### Scenario: Refuse unresolved intent
- **WHEN** the module, page authority, required media or requested capability is unavailable, or export intent is ambiguous
- **THEN** dispatch refuses or requests clarification without a destination effect.

### Requirement: Guarded operation effects
The coordinator SHALL preserve release and invalidation semantics, reject duplicate and stale operations and revalidate ownership under the effect gate. Blank start SHALL call the admitted page owner with no model call.

#### Scenario: Cancel or replace before effect
- **WHEN** cancellation or a newer admitted revision invalidates an active request before effect dispatch
- **THEN** the old operation cannot render or export.

#### Scenario: Uncertain export settlement
- **WHEN** the existing destination owner cannot verify an attempted effect
- **THEN** reconciliation is required and the coordinator does not repeat dispatch.
