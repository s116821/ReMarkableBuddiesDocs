# Selected memory membership and receiving integration (proposal before code)

## Exact existing foundation

Current local source is `3f6258b898102d9e8bc91a276110ec90eb3997d3`. Accepted PR 31
source `423cb0b227856d3aa1fcc3e1e0b66865622e4fb7` is not its Git ancestor, but
selected/publication/portable/Drive/type files compare byte-identical. The
selected snapshot source blob is `de7a3f0c5be06480b2f67c290fc87996ca5cf816`,
including the accepted post-open lineage validation repair. Storage/mod differs
only by Main's bounded head/revision/media-reference helpers. Do not merge older
Cargo/config or overwrite protected WIP to recreate this already-present code.

The accepted storage contract remains [Docs PR 7](https://github.com/s116821/ReMarkableBuddiesDocs/pull/7)
at `7d4cb74fb2d620aeda3bdb172a5ab99d3f1bc92d`, a separate dependency rather than
an archived/copied change in this branch. Current REM-52 and all 34 timestamped
comments were read. Its fixed-ID transport does not mint domain membership,
qualify account/app visibility or authorize native work. Main owns the memory
domain; SCRAPPY owns genuinely missing generic primitives.

## Aggregate identity and catalog

Independent Sol focused review accepted this domain contract after the schema,
accepted-lineage and gate-discovery repairs. Domain implementation may proceed;
the generic cumulative pre-I/O/validated-lineage seam still requires its own
implementation and review before bounded selected runtime activation.

Keep existing Fact/Key/schema-1 identities unchanged. Global fact aggregation is
one stable SubjectMemory record identity per independent chain. Document-associated
facts participate in the common stable source-document aggregate; profile, title,
page, conversation, actor and timestamp do not split its conflict unit.

Frozen normative SHA-256 key bytes (implementation follows):

- Document: UTF-8 `urn:remarkable-buddies:source-document:v1:` plus canonical UUID.
- Global fact: UTF-8 `urn:remarkable-buddies:global-record:v1:subject-memory:` plus
  the existing canonical Fact record UUID.
- Memory catalog: UTF-8 `urn:remarkable-buddies:subject-memory-catalog:v1:` plus
  compact JSON in exactly the order `group`, `profile`, `binding_sha256`.
  UUID values use lowercase hyphenated canonical strings; the binding digest is
  exactly 64 lowercase hexadecimal characters. Binding contains no credentials.

Scope is the existing `(group, key_sha256, binding_sha256)` tuple. Reuse the exact
document recipe across conversation and memory domain membership;
an opaque caller hash in older fixtures is not a wire recipe. REM-52 owner review
confirms that this recipe belongs to the domain, not a missing generic Store API.

The catalog root record UUID is UUIDv5 under `Uuid::NAMESPACE_URL` over those
same prefixed catalog identity bytes. Registration record UUID is UUIDv5 under
that root UUID over UTF-8 `aggregate:` plus the canonical aggregate key digest.
Catalog envelopes use the already supported SubjectMemory domain schema 1;
existing Fact envelopes and identities remain unchanged. Strict tagged catalog payloads are `catalog-root` and
`aggregate-registration`. The root carries format 1, group, profile and binding
digest. A registration carries format 1, catalog root UUID, aggregate key digest,
typed owner (`document` plus document UUID, or `global-fact` plus complete Key),
and immutable genesis operation UUID plus selection digest. Catalog records have no mutable value,
tombstone or correction variants: each is one parentless immutable revision.
Their revision UUID uses the existing operation-derived memory revision recipe.
An operation is therefore one record creation, not a batch of unrelated roots.

Catalog payloads have a required top-level `kind` discriminator; existing Fact
payloads have no such field and strict Fact decoding rejects it. Decode according
to the registered scope, require the matching complete strict shape and reject
unknown variants/fields. Catalog records never enter fact ranking. This uses the
owner-reviewed existing schema allowance rather than broadening generic schema
acceptance merely to carry a new payload variant.

The genesis selection digest is the original raw-byte identity supplied by the
Store's validated accepted-lineage view for that scope's Initialize transaction.
Validate it against complete accepted
lineage, including after replacement; the genesis operation's transaction must
be Initialize for that exact scope and its original validated raw digest must
match, including noncanonical JSON bytes. Never reserialize transaction metadata
to invent this identity. A current token or supplied arbitrary hash
cannot substitute. Duplicate logical registration identity with different owner,
genesis or payload refuses. Identical membership can be acknowledged from the
current validated catalog, but that acknowledgment is distinct from an original
operation replay receipt. Adoption never publishes a losing fact/creation payload.
Document registrations exclude profile from the aggregate identity; different
profile catalogs may refer to the same document aggregate. A global registration
must carry this catalog's profile and its exact independent Fact record identity.

Represent the local selected memory catalog as a typed SubjectMemory root and
independent immutable registration records in the existing selected closure.
Registration is append-only: an aggregate key's genesis/membership identity cannot
be replaced or removed through catalog update, including after fact tombstones.
New registrations add records, not rewritten copies of all fact payloads. Bounded
current catalog closure is at most 4096 records/8 MiB; saturation refuses rather
than dropping membership. This is domain metadata, not another database, sync
worker or provider lock engine.

For every accepted catalog predecessor, its entire selected ObjectRef set must
be an exact subset of the current catalog set, with the same single root. This
also applies to activated catalog winners; generic closure validity alone cannot
prove append-only registration. Validate this from the already charged accepted
transaction lineage. Retained losing registrations are not predecessors and do
not become active membership. No unbudgeted receipt/history rereads are allowed
to validate genesis or this monotonicity rule.

Catalog registration contention is distinct from fact editing: a losing registration
may adopt the accepted existing key or explicitly register a still-absent key on
a fresh accepted catalog base, preserving every existing registration. A losing
fact/document edit may not republish/rebase its stale payload at a winner's
successor. Timestamps do not select either winner. Local catalog bootstrap requires
an explicit complete validated initializer; missing selection supplies no authority.

The initializer explicitly names the catalog identity, root operation and complete
registration set. Each registered aggregate must already have a validated complete
selection with matching owner and genesis. Publish aggregate creation before
catalog registration: a crash may leave an unregistered aggregate, never a catalog
advertising a half-created one. An orphan is not query membership; recovery must
explicitly validate and register it. A root-only initializer is the sole complete
empty catalog. No ordinary Store heads are automatically imported. Existing
document aggregates are adopted after complete owner validation, rather than
initialized again with memory-only references.

This phase defines local accepted membership and consuming paths. Remote group
root/catalog onboarding, immutable provider genesis-slot allocation, selected
publisher/outbox, OAuth and actual Drive contention remain separate unqualified
REM-52 work. Do not turn a local catalog or supplied provider ID into cloud authority.

## Projection and ownership

Read the complete Store-created selected snapshot and pair each parsed envelope
with the original ObjectRef at the same manifest position. Never reserialize an
envelope to invent its stored identity. Validate metadata and the existing hash-
linked accepted history through current Store primitives. Retained closures are
historical custody and never current query facts or implicit mutation parents.

Traverse full selected causal ancestry and derive one current head per logical key,
including explicit tombstones. Validate stable Fact key/claim invariants across
ancestors, schema, profile/scope and explicit aggregate ownership. Global aggregate
contains only its declared independent Fact chain. Document aggregate may contain
multiple facts/profiles and other domain records; every memory fact must name that
same document. A record/reference cannot claim two contradictory aggregate owners.
Preserve unrelated aggregates when applying one winner.

Mixed document closures preserve exact unrelated-domain references, namespace/media
and coverage. Reuse the existing conversation projector for its pinned subset and
require unambiguous historical document ownership. Unknown/unsupported/ambiguous
domains remain refusal; they are not ignored as permission to rewrite a mixed
closure. Handwriting and native evidence do not become memory or current effects.

The owner confirms `commit_selected` starts from the complete selected manifest
and preserves prior records, media, coverage and retained closures. Memory append
passes only new memory envelopes under the full aggregate token. It does not
reconstruct a manifest from a memory projection. This storage preservation does
not establish semantic ownership: validate the known conversation/source/export
subset using its existing pinned projector and require each conversation's
historical owner to equal the registered document. Unknown namespaces, missing or
ambiguous owners refuse this receiving adapter until a domain validator exists.
Do not use `activate_selected` with a memory-only replacement of a mixed closure.

Catalog membership and aggregate snapshots must form a bounded consistent read.
Missing catalog/root/registered aggregate, incompatible binding, incomplete closure
or stale token yields unavailable/refusal, not complete-empty or ordinary-head
fallback. An explicitly initialized complete empty catalog is distinguishable from
missing membership. Scope discovery never scans retained history as an active list.

One read has cumulative caps, not independent per-aggregate allowances: at most
64 registered aggregates, 4096 total historical transaction/reference work items,
8 MiB total metadata bytes read and 32 MiB total media bytes verified. Repeated
reads count again unless the Store can prove the same immutable verified pin is
reused. Catalog validation, excluded-scope ownership checks, retained/history
validation and current-token revalidation all consume the same budget. Context
ranking/output caps remain separate. Exceeding any cap yields unavailable before
the excess read/hash; no truncated catalog or partial authoritative ownership.

The published generic candidate `31116b03b6030bd0cde95ea5a5b84354f18f8441`
adds `selected_snapshot_with_budget` and its already validated raw accepted-lineage
view. Its independent review remains pending; the old `selected_snapshot(limit)`
alone cannot enforce a caller's cumulative cap after returning. Do not duplicate
private storage validation in memory code or
describe this media-verifying path as metadata-only inspection.

This cumulative cap covers receiving snapshot validation and token revalidation.
For mutations/setup, domain receiving validation uses that same allowance, while
the subsequent generic initialize/commit publication performs its own independently
bounded write validation. It is not one combined receiving-plus-publication I/O
cap. No combined mutation/setup latency or disk-work qualification is claimed.

## Actual Provider, Reader and commands

Implement a selected Provider using the same reviewed memory operations/query
ranking and the existing selected publication primitives. Local-only remains the
default and retains its legacy-mode lease. An explicit selected configuration must
choose a validated catalog/group/profile/binding; toggling sync or enrichment flags
cannot convert ordinary history into selected authority.

Selected updates use current selected heads plus live token/base at the actual
commit boundary; exact operation retry returns the original receipt and never
mints today's token. Applying a winner preserves losing branches as retained
history with no stale automatic republish. Memory records grant no native effect.

Integrate the selected Provider in the real Reader and existing one-shot commands,
not merely a detached projection helper. Pin query catalog/aggregate generations
and revalidate through receiving answer processing. Use the existing domain admission
gate/Store ordering for actual consuming publication or handoff; checking then
dispatching outside the guard is insufficient. No Store mutex is held over model
network I/O. Replacement during a model call prevents publishing an answer as
current; it does not retroactively claim a submitted effect never happened.
Reader continues global-only recall without a qualified document association.

Use the existing admission registry shared by Store pointer/group/aggregate key,
including replacement binding. Extend its reviewed internal seam to acquire a
set of gates in lexical aggregate-key order, deduplicated, with no reentrant
single-gate acquisition inside the callback. Catalog plus every queried aggregate
must belong to the same Store, group and binding. Read/revalidate all tokens under
that set before releasing for model I/O, then reacquire the same ordered set and
revalidate before the consuming Ledger Generated write. Hold admission across
the actual Generated write and output-pending journal transition/handoff where
applicable; never return an unguarded permission Boolean. All domain mutations,
catalog registration and selection activation must use this same registry.

Discovery is two-phase: pin/validate the catalog under its own gate, release that
gate, derive the sorted complete gate set, then acquire the set and verify the
catalog token is unchanged before reading or using any aggregate. Never hold
the catalog gate while acquiring another key that may sort earlier. Membership
replacement refuses this attempt; the adapter does not silently restart with a
new answer base. All validated/touched aggregates, including genesis ownership
checks, participate in that set and its pins. Every repeated validation consumes
the original cumulative budget; no per-retry reset is permitted. Final consumption
uses the same set and tokens, with no gate discovery after answer submission.
The first phase validates only catalog syntax and accepted catalog lineage and
discovers declared scopes; cross-aggregate genesis/current-owner validation
happens under the full set. Genesis semantics use its already charged validated
Initialize transaction, never a separate unbudgeted receipt read.

The existing ordinary Ledger journal records local processing only; this phase
does not turn its all-history heads into a selected conversation or native effect
authority. Selected memory can enrich that journal only under validated pins.
Selected-mode native rendering remains refused at its existing boundary. Failure
or stale pins after interpretation records the existing explicit failure/cancel
outcome with original question intact and creates no generated assistant draft.
Default LocalMemory behavior requires no selected pin and remains unchanged.

Pins also bind the exact returned status, diagnostics and context payload. Public
DTO fields are convenient data, not permission to alter facts while reusing a
valid pin. Changed payload refuses before the consuming callback; unchanged
clones share one consuming admission. Inspection has its own sealed envelope
payload and private admission anchor rather than exposing an unbound query pin.

The actual maintenance writer retains its Provider, pins and Store lease after
processing and guards the synchronous stdout write itself, including complete-
empty queries and inspection. Formatting bytes alone is not current handoff.
Changed/stale/exhausted admission emits fixed unavailable with no data before
any write attempt. A failed partial I/O write is not followed by a second report.
The original root ObjectRef must exist in every accepted catalog predecessor,
including Initialize; a later root cannot repair a rootless accepted genesis.

Exact memory retry compares media and complete coverage by unique hash-keyed
identity, including byte lengths and omission reasons. A normal Store append may
sort valid prior vectors; that order change does not change immutable media
identity or justify an operation collision. Historical raw references remain
unchanged and no reserialization invents an old reference or token.

Immutable Fact key/claim continuity requires accepted historical selected-envelope
custody, including facts first created after aggregate Initialize. A winning
closure cannot evade it by moving the original chain into retained history or
re-rooting the same record UUID. Use already parsed, charged accepted-history
envelopes, paired with their exact original references. Historical values provide
only identity/claim custody checks; current query heads still come exclusively
from the winning closure. Unaccepted retained losers are never creation authority.

Commands retain pre-runtime routing, explicit config, input/output caps, busy and
privacy behavior. Selected inspect/query/mutation are allowed only through the
validated domain path. A mixed/unknown selected Store cannot silently fall back
to LocalMemory. Default local commands and refusal tests remain intact.

## Required new evidence and open gates

Use real Store and receiving Reader/actual command paths: selected winner vs
retained ancestor/loser, tombstones, exact noncanonical references, unrelated
global/document preservation, catalog registration/current membership, wrong group/
binding/profile/owner, missing history/media, stale token, same-base competing edit,
replay and replacement around actual consumption. Reuse accepted generic coverage;
do not rerun its broad matrices merely because the domain adopts it.

Shared/isolated worker, live Drive/bootstrap, Manager, Writer, selected restore/
migration activation, native current-page/effect qualification and final release
remain open. Current native hold and protected WIP remain unchanged. This phase
must be independently reviewed before code/publication and cannot be archived as
full REM-24 acceptance from local fixtures alone.
