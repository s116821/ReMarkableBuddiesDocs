# Development focus ancestry consumer amendment

Status: source-only proposal awaiting Main review, before implementation. SDK
authority is `2313a3e2d93278f311d8f0f960da8103bc63cfa4`, specifically
`openspec/changes/establish-native-platform-contract/focus-ancestry-discovery.md`.
The SDK owns discovery, event guards and the internal retained-owner ticket; this
document owns Buddy decoding, refusal admission and preservation. Main and Sol
accepted the SDK proposal only. No wire rollout, artifact, nonce or trial follows.

## Selection and unchanged evidence

Accept the additional format only for an explicitly source/configuration/packet
bound `developmentFocusAncestry=true` selection with development capture enabled,
setup120000/facts5000 and main-dev-facts-120s. It is default off, never a fallback
after BFS refusal. A selected scope is not native qualification: ordinary-window
delivery and pre-receiver event-filter observation require exact runtime profile
evidence. Unknown subscene/filter behavior remains unsupported.

Historical version1 remains exact29 fields; version2 remains exact33 fields and
its unchanged finite topology matrix. Do not append fields, reinterpret counters
or modify their raw bytes. In particular e997's return site remains unknown and
9453 remains the actual cumulative queue-cap refusal. Keep callback4, capture
completion36 and facts23 fields unchanged. A decoded diagnostic never promotes
capture/facts/visual/native/render/UI acknowledgment or authorizes another action.

## Exact version3 format and scalar rules

Version3 has exactly the version2 field names plus `discovery_scope`, `chain_items`,
`chain_complete`, `chain_failure`: exactly37, case sensitive. Version is the JSON
integer3. Scope is exactly `window-focus-ancestry-v1`. All four version2 topology
fields are null in every version3 record, including ancestry depth refusal.

Apply the existing kind/profile/nonce/PID/start/root-device/inode binding, literal
false authority flags, accepted/failure/effective-deadline relationships and original
strict scalar rules. Nullable numeric fields are signed64 JSON integers, never
boolean, fraction, numeric string or out-of-range bigint. chain_items is null or
0..25; chain_complete is an actual boolean; chain_failure is null or exactly
anchor-unavailable, item-context, root-unreached, depth-bound, cycle,
observer-unavailable. Reject unknown names, enums, versions and mixed shapes.

Use the actual duplicate-key-aware parser, including escaped duplicate names,
strict UTF-8 and existing8192-byte limit. Preserve complete bounded matching raw
bytes exclusively before decoding. Invalid decoding is distinct from unknown
transport/copy/binding: do not discard a verified copy on later failure or let a
foreign copy borrow ownership. Existing before/copy/after metadata guards,
historical collector isolation and refusal-before-cleanup remain unchanged.

## Finite branch matrix

The following is an additional version3 matrix, not a relaxation of the v1/v2
decoder. Counters mean visited_items/receiver_candidates/scene_candidates/
matched_pairs. Pair detail means the existing first-pair triple. Observer detail
means the existing document/scene/receiver installation triple.

| Branch / result | chain_items / complete / failure | Other fields |
| --- | --- | --- |
| initial-progress / null | null / false / null | Original progress predicate; counters, pair, active-owner and observer detail all null |
| owner-discovery / open-focus-chain-refused | 0..25 / false / finite chain label | predicate/deadline operand, all counters, pair, active-owner and observer detail null |
| owner-discovery / open-context-lost before completion | 0..25 / false / null | Original progress predicate; counters, pair, active-owner and observer detail null |
| owner-discovery / original classification or matching refusal | 1..25 / true / null | Exact original branch rules with the tighter chain relations below |
| observer-install / open-owner-observed | 1..25 / true / null | Original finite observer role/member/failure tuple; predicate, counters, pair and active-owner detail null |
| owner-revalidation / open-owner-observed | 1..25 / true / null | Original finite revalidation predicate/active-owner relation; counters, pair and observer detail null |

No other branch or combination is accepted. Construction enters with chain_items0;
count only items passing pointer/thread/window/cycle checks. Observer failure
after append retains that count. complete becomes true only after retained root
and its observers pass. Complete never becomes false again. Classification begins
only afterward, so incomplete records cannot contain evaluated0 classification
counters. Scope is fixed even in initial-progress records.

Local chain refusal labels have these additional count relations:

| chain_failure | chain_items |
| --- | --- |
| anchor-unavailable | 0 |
| item-context | 0..25 |
| root-unreached | 1..25 |
| depth-bound | 25 |
| cycle | 1..25 |
| observer-unavailable | 0..25 |

These are consumer bounds, not claims all counts are reachable. Missing initial
window/root/leaf uses anchor-unavailable0; initial engine/thread or item-context
failure uses item-context0. Required observer failure before any retained item
uses observer-unavailable0. No pre-chain engine/window enum may masquerade as
completed classification. Concrete SDK return sites must agree before code is
accepted; this amendment selects no undocumented producer coercion.

Completed classification accepts only the existing open-context-lost,
open-item-lost, open-candidate-bound, open-owner-unavailable and
open-owner-ambiguous results. Never open-topology-bound, open-engine-thread or
open-current-window-unavailable. Preserve their existing type/null/predicate/
first-pair/active-owner matrix, with visited_items0..chain_items, role counts0..9
and each role count<=visited_items, matched_pairs0..2 only after pairing begins.
No matched_pairs value is allowed until visited_items=chain_items and both role
counts<=8. Pair ordinals0..7 must be less than their respective candidate counts
and refer to root-to-leaf enumeration. Candidate-bound requires at least one
role count9, null matching/pair/active-owner detail. Unavailable requires
visited_items=chain_items and matched_pairs0; ambiguity requires full classified
chain and matched_pairs2, with at least two candidate pairs. Preserve existing
first-rejected-pair semantics for unavailable and final active-owner rejection
only for open-context-lost with matched_pairs1. Do not infer owner absence from
partial classification or choose a first/nearest receiver.

## Original progress and sticky continuation

Original progress predicates remain context, live, invalidated, token, deadline,
in that order. Sticky focus/input/anchor/chain events map to captureInvalid_ and
the original epoch. Initial-progress remains separate. During construction,
post-operation progress wins before a sampled local chain label is committed:
progress refusal has chain_failure=null. An observed endpoint mismatch first
invalidates, so reports invalidated rather than a new chain label. Deadline
operand is non-null only when predicate=deadline, is >=effective_deadline and
<=failure time; earlier predicate failures leave it null. Nested first failure
is immutable. Completed-chain invalidation preserves complete=true and count,
then uses original progress or the existing later refusal stage. No replacement
diagnostic or reset clock is created during facts continuation.

## Retained-owner refusal admission

SDK ticket construction is private to FactsEntry, noncopyable and bound to exact
owner QPointers, weak entry/guard identity and generation. The consumer cannot
inject an owner, manufacture a ticket or decide its validity from a callback.
The original guarded owner must continue through unchanged visual-before-facts
admission; later facts must not rediscover, switch owner or use expected order
as observed order. Deferred entry/session teardown and original identity/order/
epoch/final-output checks remain SDK obligations.

Admit `facts-retained-owner-refused` only as an additional selected ancestry
reader_stage in the existing exact27-field version1 refusal.json. The SDK reader
allowlist must preserve that name instead of mapping it to unlisted-reader-stage;
reader_result_had_facts must be false. Entry stage and callback remain the existing
facts-entry-read-refused or facts-entry-delivery-refused, as appropriate. Keep the
callback exactly nonce, stage, application_thread, engine_thread with unchanged
identity/type/thread checks. Do not add SDK internal observed/outputPublished
fields to callback JSON. The internal result remains unsuccessful and the
consumer's facts/capture flags remain false. Unselected sessions refuse the new
reader stage; no outer callback enum is added. All27 refusal fields, original
clock/sample/entry relationships and literal false authority flags remain strict.
It establishes neither successful facts nor cleanup eligibility.
Unavailable/revoked/mismatched/reentrant ticket before or during helper entry
uses that stage, unless an earlier terminal result is already latched. Required
facts-observer metadata failures retain facts-metadata-or-context-refused;
ordinary helper conversion/mapping failures retain their original stages when
ticket validation passed. Entry final delivery/output binding failure retains
facts-entry-delivery-refused/facts-entry-output-unknown. No new callback fields,
automatic retry, second discovery or deadline extension follows. Missing entry
means no dereference/publication; independent restoration still controls cleanup.

## Acceptance before any artifact selection

Implement only after independent acceptance of this amendment and SDK contract.
Real decoder/collector/callback source tests with mocked transports must cover
every row/label and count boundary, null versus0, selected/unselected stage,
types/relations/duplicates/unknown versions, historical v1/v2 readback, partial/
foreign bytes and later binding loss. Preserve the current short-path and both-
collector isolation tests. Independently review concrete ticket API and source;
SDK exact vendor fixtures must exercise focus ABA before notifications, nested
validation/destruction, provisional success through publication, ambiguity, edge24
and no edge25, and same-owner facts without rediscovery. Host fixture success
does not establish native profile qualification. No artifact/packet/next trial,
canonical sync/archive or task4.11/native completion follows from this proposal.

Source basis: current SDK2313a3e contract, current strict Buddy decoder source,
and Main/Sol proposal acceptance messages. Private run evidence has no public
link and is not repeated as a new experiment here. Count-label refinements above
are proposed consumer requirements awaiting producer/consumer independent review.
