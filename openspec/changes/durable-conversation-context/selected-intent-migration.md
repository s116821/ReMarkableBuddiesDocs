# Selected intent and historical settlement migration

Status: proposed domain implementation increment; no selected effects enabled.
Main owns domain/projector/Attempt integration. SCRAPPY owns generic storage and
its selected publication/activation primitives. Accepted interface decisions are
[the REM-52 owner review](https://github.com/s116821/ReMarkableBuddiesDocs/pull/7#pullrequestreview-5442770097)
and [the version decision](https://github.com/s116821/ReMarkableBuddiesDocs/pull/7#issuecomment-6038732257).
Source basis: Buddy REM-37 `673c5781cd5d89a89d712b9d8253433c920dc37c`,
REM-52 selected publication implementation `cca7ea9d6a1942ccdfed70d76aab615fd2dca5d4`,
and the current REM-52 requirements. Plans are not implemented behavior.

## Version boundary

Keep `Envelope.domain_schema_version=1` for historical and ordinary records.
Version 2 is restricted to Conversation namespace Receipt/OutcomeFact records
carrying the new admitted-intent/settlement extensions. Version 1 rejects a
nonempty extension; version 2 rejects another variant, missing required extension,
invalid pins or an unsupported future version. Do not rewrite immutable history.
An old reader refuses version 2. A new reader retains version-1 inspection and
existing local-only operation, without upgrading an old receipt into admission.

SCRAPPY and Main coordinate storage validation before integration: generic
Envelope validation admits only versions 1 and Conversation version 2; Main's
domain decoder validates the exact variant and fields. No blanket acceptance of
future versions and no storage interpretation of domain payloads. Version-1
selected-storage fixtures remain independent of this increment.

## Extend the existing records

Receipt gains optional `admitted_intent`; OutcomeFact gains optional
`settlement`. Neither introduces another Record variant or operation journal.
The existing OutputPending transaction commits the assistant Turn revision,
Root revision and Receipt together before the first selected external effect.

An admitted intent retains the original operation/request ID, exact request
payload fingerprint, conversation/turn IDs, exact new root and turn revision
references, and the original qualified source/capture/evidence/media references.
Each immutable record reference includes namespace, record ID, revision ID and
serialized-object digest/size. Referenced media retains digest/size/type. All
references are bounded and checked against the pinned selected closure; source
qualification is checked by its domain/SDK owner rather than inferred from IDs.
Legacy identity-free captures and the current unqualified SDK synthetic model
cannot arm a shared native effect.

Selection evidence retains the accepted storage scope fields (`group`,
`key_sha256`, `binding_sha256`), store generation, aggregate generation,
accepted-base digest and selection digest. These are original publication pins,
not a serialized SelectionToken. Only Store can mint a live token. A transaction
may change the selection digest; post-commit effect admission must therefore use
the current store-minted token, require equality with the accepted intent publication token/generation, and verify that its selected closure contains the
exact admitted intent and causal revisions, rather than reuse precommit pins as
a live capability. Presence of the same intent in a later replacement is insufficient. Every guarded append changes aggregate generation and selection digest; historical replay returns its original possibly stale token, while selected_receipt is restart evidence only. A foreign, replaced, conflicted, missing or incomplete closure
refuses admission. Restart reconstructs facts and uncertainty, never an effect
queue or automatic replay.

Before allocating prepared envelope/revision UUIDs or computing a retry fingerprint, look up the stable operation in the accepted selected publication and Receipt. Validate the supplied logical request and original pins against that evidence and recover the exact original serialized envelope/revision references. Never reconstruct a committed batch with fresh UUIDs after a lost acknowledgment. Historical lookup neither refreshes current admission nor repeats an effect.

The existing immutable request fingerprint covers every intent field and its
original pins. An identical retry returns the original historical receipt before
ordinary current-head checks, without another append or effect. Changed payload,
pins or references under the same operation ID conflict. Returning historical
acknowledgment does not authorize replacement membership.

Settlement references the exact original Receipt and admitted Root/Turn revisions,
request identity/fingerprint, result state and bounded verification evidence.
Evidence identifies its procedure/origin and immutable records/media; timestamps
are descriptive. Unknown/unverified outcomes remain uncertain. A verified result
can settle that original intent only after the appropriate backend verification.
It cannot advance replacement Turn/Root heads, enqueue output, adopt imported
authority or infer native completion from a callback.

## Selected projection and effect admission

The domain projector reads only immutable `SelectedSnapshot.selected_records`
for current state. It validates unique root/turn/source/binding membership and
reference closure. The selected snapshot contains full ancestor closure, including earlier Root/Turn revisions. Derive causal heads for each (namespace, record_id) only inside those pinned envelopes, require exactly one head for current projection, and retain exact revision/digest ancestor lookup for intent and evidence. Multiple revisions in a chain are valid; a true fork refuses. All-history heads are not current selected heads. Explicit
retained records support historical settlement/inspection and unresolved intent
closure, without entering current context or ordinary append membership.

Project every supported Record variant through its existing conversation/source/
binding references to one unambiguous `SourceObservation.document` aggregate.
Root IDs, titles and page positions never supply a missing document identity.
Nil, absent, ambiguous or multiple document owners remain visibly deferred from
shared document publication while preserving their isolated backups. Unknown
schemas/variants and broken chronology or reference closure refuse projection;
no unsupported record is silently dropped. Preserve unrelated document and global
record scopes. A restored native binding remains historical/waiting until current
exact document/page verification; missing vendor files do not imply deletion or
authorize recreation, output, export or undo replay.

All Ledger/workflow/activation handles share one canonical Store-and-aggregate
admission guard. Lock order is domain admission then Store; the Store mutex is
not held over external I/O. Activation uses the same guard. Keep admission from
final validation through actual submission; for the current synchronous backend
this means the entire backend call. Every subsequent navigation, mode, text,
history/undo/redo and bitmap handoff validates current admission again. An
earlier successful check is not permission for a later handoff.

Historical settlement and durable uncertainty-latch transition commit in one
retained-only selected metadata transaction referencing both winner and retained unresolved
closure. Do not reuse commit_selected for late settlement: it extends active membership. The retained-only primitive preserves winner references and original accepted publication/intent linkage. Crash recovery sees old or complete new state. Uncertainty keeps the
latch; only explicit verified settlement can change it. Sync success, elapsed
time, imported receipts or provider upload cannot clear it. Domain validation
checks the original intent closure before reconstructing the latch. Unrelated
document/global scopes stay intact.

## Implementation and evidence

Implement codec validation and legacy migration first, then selected projector,
guarded intent publication and retained settlement, then actual Attempt/backend
admission. Coordinate the storage validator and exact primitive revisions with
SCRAPPY; do not copy storage selection structures or relax opaque token ownership.

Focused regressions cover old/new decoding and old-reader refusal, wrong
namespace/variant, missing/foreign pins and evidence, selected versus all-history
membership, multi-revision causal chains and true forks, stale publication despite matching parents or retained intent membership, lost acknowledgment with exact recovered prepared identities,
replacement during handoff, late verified/uncertain settlement against retained
revisions, crash/latch reconstruction and multiple handles. Exercise navigation,
mode, text, history/undo/redo and bitmap through the real guarded path. Synthetic
fixtures test domain mechanics only. Live provider and qualified native gates
remain their owning deliveries; no shared worker or production effect is enabled
by schema acceptance. Keep the complete OpenSpec delivery unarchived until its
implementation and all applicable verification gates pass.
