## Context
The existing describe_stored query holds ordinary-mode custody, refuses incomplete stores, selects one bounded current-head Conversation metadata snapshot including explicit root/fact IDs and all selected heads, validates supported schema/identity/chronology, and returns a bounded static catalog description. The existing layout plan accepts already-validated historical context, preserving original borrowed turns and draft. Neither grants current native authority.

## Decisions
Expose conversation::feedback::plan_stored(ledger, identity, context, draft, geometry, fact_id). Derive the conversation only from a valid Persisted presentation identity; reject Unbound/Legacy/nil identity. The ordinary caller supplies a domain-validated ContextView, as required by the existing planner; this API does not claim to validate every unrelated context turn against storage.

Extract the current query body into one private callback helper. It retains its existing ordinary-mode lease through the callback, snapshot validation, exact selected fact and associated stored turn. The existing describe_stored API delegates with a description-only callback. The new API uses the same validator and exact static catalog result; it accepts no arbitrary caller description or raw fact.

The selected stored Turn must equal the matching supplied ContextView Turn in every existing field, including outcome, text, sources, correction and completion. Missing, duplicated, altered or stale selected context refuses. The original fact need not equal a later retained turn outcome: it remains explicitly historical. Run the existing planner unchanged to validate full layout identity/order/geometry. Return a new conversation_layout::HistoricalFeedbackPlan containing its PagePlan, original exchange UUID and FeedbackDescription. The consumer locates the description using its original turn ID in that exchange; no synthetic Turn or replacement text is inserted.

One explicit fact per call keeps failure atomic and attribution precise. Existing MAX_ITEMS/context and 1024-byte serialized description limits remain. No image/media reads or arbitrary errors enter descriptions. Refusals retain static privacy-safe diagnostics. No result implies undisplayed state, current operation state, successful presentation or write permission.

## Source compatibility and scope
Keep both existing public function signatures and original PagePlan/Exchange shapes unchanged. Only the three proposed source paths change. Existing 14 actual Store receiver tests remain intact. No Cargo/lock/SDK/domain/storage/workflow changes.

## Verification
Use actual temporary Store fixtures and the public composed API. Exercise all three catalog kinds, uncertainty dominance, older fact with later turn outcome, exact selected identity, missing/foreign/stale/mutated context, invalid geometry/unbound/legacy identity, existing snapshot conflict/tombstone/schema/mode refusals, catalog privacy, and borrowed turn/draft/source/region preservation. Reuse shared validation; existing receiver tests verify its full refusal matrix. No duplicate modeled catalog or native adapter is introduced. Run formatting and hosted exact-head Clippy/full tests/package integration; no local bulky build on C. Attribute PR and actual-main/release evidence separately.

## Remaining work
Pre-attempt/unassociated errors cannot be represented by existing OutcomeFact without a conversation/turn. Do not fabricate IDs or add a side journal. Durable retention needs its own reviewed domain/storage routing design. Live status, error-turn writing, cancellation gestures, display acknowledgment, native admission and whole feedback/layout completion remain separate open gates.
