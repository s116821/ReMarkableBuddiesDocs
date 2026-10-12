# Non-effectful Buddy acquisition decision seam: assessed precode contract

Main and the existing independent Sol reviewer accepted this five-file contract
delta on2026-10-12. Local implementation remains the next step; native and
installed Reader qualification remain unfinished.

This REM-25 increment implements a local decision model under
[buddy-page-reuse-contract.md](buddy-page-reuse-contract.md). It does not operate
a tablet, inspect another process, activate a payload, render, allocate a target,
create/navigate a native page, persist a binding or construct NativeCommitted.
Held8112 transfer/activation remains untouched. Model acceptance does not complete
the native, installed Reader, REM-37 binding or REM-38 delivery gates.

## Existing boundaries

Rust pins the public SDK to
`f6b7dc8954ba9f5a284d56568765e05c38483924`. Its PageObservation exposes page/order/
origin and full opaque equality; device/instance/session/visit/revision/input
fields remain private. NavigationReceipt exposes request and observed completion.
The local SDK development checkout has a later HEAD; inspect the exact pinned
Git objects or dependency source rather than attributing that HEAD to this API.
The605b native helper is a different source contract and is not used here.

Existing sdk_acquisition prepares only synthetic create/handoff/Next results.
Installed render_answer still inspects the successor before classification.
This increment adds no production wiring or authority to either route.

REM-37 owns the one existing Store, deterministic document/page binding key,
full-head CAS and qualified adoption/binding publication. Consume supplied
read-only association projections through a narrow interface. Do not implement
another registry, binding-key algorithm, storage format or receipt issuer; do not
copy or edit the separate REM-37 WIP. Public source reference:
[qualified binding design](https://github.com/s116821/ReMarkableBuddiesDocs/blob/1049375fc8d9e92342ef430e99696408e00a2202/openspec/changes/durable-conversation-context/design.md).

## Current-first decision

The first phase accepts the original SDK PageObservation, a fresh current
observation, desired conversation ID and supplied read-only association and
optional recognition witnesses. Require Synthetic origin, full original/fresh
equality, a nonempty unique order containing the current page exactly once, and
consistent document/page scope before lookup. No Debug parsing, invented session
IDs, bare current-qualified boolean or private SDK field access is permitted.

An association witness must bind the complete observation and exact logical
page/conversation it describes. Relevant unambiguous current association yields
SyntheticReuseCandidate immediately, with only the current lookup and no
successor inspection. It remains a candidate requiring later native qualification,
not renderer/binding permission.
Require explicit Synthetic origin for every supplied association/recognition
observation, receipt source/completion and fresh successor, even while the SDK
currently exposes only that origin. Mismatched observation, page or requested
conversation in any supplied witness refuses rather than being ignored or used
as a fallthrough. Consistent projection fields are modeled inputs, not proof
that they came from Store or establish current-device qualification.

Missing association is UNKNOWN. With no matching observation-bound recognition,
return RecognitionNeeded. Relevant unbound/legacy Buddy recognition returns
AdoptionRequired; it does not create a trusted association. Blank, unavailable
header cache, failed/unfamiliar/unknown recognition and another or unresolved
conversation's Buddy cannot authorize insertion. Conflicted, tombstoned or
unresolved historical/imported/stale claims remain explicit unresolved evidence.
In particular positive ordinary recognition cannot silently erase an existing
unresolved logical Buddy claim to permit another page's creation.

Only positive ordinary source recognition with no contradictory claim permits
continuation. At the exact synthetic end of the fresh unchanged order, return
a SyntheticInsertionPlan after the ORIGINAL source with no neighbor. Otherwise
return an immutable InspectImmediateSuccessor plan privately retaining the
original observation/order/conversation and the exact immediate neighbor key.
This is an evidence requirement, not a navigation dispatch or permission.

## Successor decision

The second phase accepts that private anchor, an SDK-created NavigationReceipt,
a fresh successor observation and supplied read-only association/recognition.
Require receipt.request.source equal to the complete original anchor, direction
Next, target equal to the original immediate neighbor, unchanged exact order and
document, and fresh successor equal to receipt.observed by full opaque equality.
Legitimate navigation changes the visit/page, so do not compare successor directly
to the original observation as if their visits were equal.

Resolve the exact successor's relevant association first. Relevant association
yields SyntheticReuseCandidate with zero creation. A missing association requires
matching recognition; stale/imported/historical/conflicted/tombstoned known claims
stay unresolved, and positive non-Buddy recognition cannot erase them. A stale or
mismatched recognition witness itself refuses. Legacy candidate adoption retains
the same conservative limits as the first phase.
Only positively confirmed non-Buddy successor evidence, with the original ordinary
source still bound by the validated receipt chain, produces an insertion plan
after ORIGINAL source and before that preserved neighbor. Wrong adjacency,
changed scope/order/opaque state, conflicting association or mismatched witness
refuses. Never rebase insertion onto the displayed inspected successor.

## Plans confer no effect authority

Decision functions accept no mutable Platform, DeviceBackend, renderer, persistence
or effect callback. A read-only projection is not a qualified production Store
adapter. All results are explicitly synthetic candidates, recognition/adoption
requirements, unresolved decisions or placement plans. Anchor/plan fields are
private; there is no conversion into CreationRequest, NativeCommitted, binding
receipt or write permission and no target allocation. Ordinary legacy Reader and
existing acquire_created_target behavior remain unchanged.

SDK CreationRequest requires a fresh current-source guard. After successor
inspection the original observation is stale: dispatching it refuses, while using
the inspected successor as source would insert in the wrong place. Future
effectful integration must obtain a supported qualified return-to-original
handoff and fresh source guard, or a separately reviewed anchored-placement API.
This increment only retains the original historical placement plan and does not
solve that native gate through a workaround.

## Verification

Use public MockPlatform observations and SDK-generated receipts for local fixtures;
the decision code itself performs no SDK effects. Verify current relevant reuse
with only current lookup; successor reuse; recognition fallback and adoption
without duplicate creation; blank/cache/unknown/conflicting/tombstoned/historical
claim refusal; positive ordinary source/non-Buddy neighbor original placement;
exact synthetic end; mismatched full observation/conversation/witness; stale or
foreign receipt, wrong direction/adjacency/order; and opaque input/session/visit
drift despite matching page IDs. Verify no target allocation, page mutation,
binding publication or rendering and preserve the existing acquisition controls.
SDK refusal of a stale original creation request after inspection is an API-limit
fixture only, not product dispatch behavior.

Source basis: current repository and exact Cargo-pinned public SDK source, current
REM-25 contract, REM-37 description/all37 accessible timestamped comments and
existing binding design. The new seam is assessed design; actual native behavior,
recognition and production Store integration remain unverified.
