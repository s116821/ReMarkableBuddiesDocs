# Atomic historical association input for SDK acquisition

The precode and implementation increment are independently accepted; its
[executed host results](historical-binding-projection-result.md) retain the
separate quality successor and open native/delivery gates.

This increment consumes the delivered historical ledger at Buddy
`cc317ff53e1dd6f612b2e82707e5a5e4b50e0265` and its current SDK pin
`32b86e4fef04844cbf2ec31129bf029cc1d9899a`. Reconcile that foundation into the
preserved REM-25 topic without replacing its history or frozen experiment
artifacts. The protected, unmerged selected-admission implementation is not an
implementation source for this increment. No second registry, binding key,
storage schema or current-effect receipt is introduced.

## One atomic historical read

Add a read-only Ledger association inspection for desired conversation and exact
document/page UUIDs. Use the existing `Ledger::binding_id`. Obtain the relevant
current heads and Store's unavailable-commit count under the same existing Store
mutex. Select the desired conversation closure plus the queried binding key, so
a binding owned by another conversation is not hidden by a conversation filter.
Keep the existing item/metadata bounds and conflict-head inclusion; do not truncate.
The existing general snapshot API keeps its previous behavior.

Validate the cloned snapshot without further Store queries. Reuse the historical
`inspect` chronology/record checks through a pure snapshot helper, and share the
existing `bind` receipt validation rather than inventing new evidence rules.
Unavailable commits, malformed records/receipts, invalid UUIDs or bounds refuse.
Missing, conflicting or tombstoned root/binding heads, unbound/differently bound
roots and another conversation's binding remain typed unresolved outcomes.
Never reinterpret those outcomes as native page absence.

A consistent root/binding pair returns an immutable historical candidate with
the original receipt and both observed head revision IDs. It has no public
constructor or mutable receipt access and no admission token, lease or effect
permission. A subsequent commit may make it stale; it remains historical even
when its logical IDs match an SDK observation. No source order, process, session
or device freshness is inferred from the stored receipt.

## Conservative existing decision integration

Add a concrete read-only Ledger-backed implementation of the existing
`ReadOnlyBindingLookup`. The current-first/neighbor decision functions retain
their Synthetic origin, complete observation and receipt-chain guards before
invoking lookup. Convert UUIDs through the public SDK API, never Debug output or
private field reconstruction. Use the existing Ledger instance; do not open a
new Store, take another ownership lease or publish any record.

A historical candidate maps only to `AssociationState::Historical`. Preserve
conflict, tombstone and other-conversation outcomes. Other unresolved or failed
stored inspection maps to one explicit unresolved-stored state. In particular,
do not map missing stored heads to the model's affirmative `Missing` input or to
`RelevantModelAssociation`. These inputs keep the existing decision unresolved,
even when positive ordinary/non-Buddy recognition is supplied. No result from
this adapter supplies native reuse, insertion, adoption, binding or rendering
authority. The installed Reader path is not wired or changed here.

## Focused verification and unchanged gates

Use the actual temporary Store/Ledger and public MockPlatform for the new path.
Verify atomic root/binding revision correspondence, unavailable-commit refusal,
historical positive lookup, missing/conflicting/tombstoned/other-conversation
states, malformed receipt refusal, and zero Store writes or SDK effects. Exercise
the actual current-first decision with this lookup so a saved match or unknown
stored state cannot produce a reuse candidate or insertion plan. Preserve the
existing synthetic model's explicitly supplied associations and refusal controls.
Run affected ledger/storage/decision checks and the ordinary library check; no
tablet or live-model test follows from this host-only change.

This does not finish native source/current identity, same-candidate creation,
gesture/capture/blank-display, independent recovery, adoption, installed Reader,
write/persistence or overall delivery. Held/spent operations, preserved fixture
pages and the exact existing helper artifact remain unchanged. Sync and archive
only when the existing whole change satisfies its acceptance gates.

Source basis: the delivered historical Store/Ledger APIs, existing current-first
decision contract and current REM-25 scope. This contract preceded implementation;
the linked result records the completed scoped host verification separately.
