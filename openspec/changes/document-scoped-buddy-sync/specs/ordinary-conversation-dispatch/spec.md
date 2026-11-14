## ADDED Requirements

### Requirement: Opt-in ordinary Reader follow-ups retain the declared source

An admitted ordinary Reader follow-up SHALL preserve its existing conversation,
exact request, bounded history and verified associated images. An opt-in
source choice SHALL name either an earlier request-evidence operation in that
conversation, an explicitly chosen original source with exact turn and record,
or explicit no-document. The current input visit SHALL remain a separate
ownership check. The dispatcher SHALL prepare one context through the existing
ordinary evidence capture. Inheritance SHALL require the same exact retained
source record and independently verified document, format and original-byte
digest. A matching source SHALL be queried once across its full index with the
new request, including when no passages match. No-document SHALL make zero
source queries. Memory scope SHALL use the admitted source or omit document
scope for no-document. Preserve eligible global memory, existing internet
behavior, the generic resolver and the dispatch without this opt-in. See the
[ordinary follow-up design](../../ordinary-reader-source-followups.md).

#### Scenario: Search another part of the inherited source

- **WHEN** an admitted follow-up names exact prior PDF evidence for a document distinct from the current Buddy input visit
- **THEN** one new whole-index query can retrieve a different original locator while the receiver keeps exact ledger history and verified image associations.
- **AND** a later follow-up can name this request's saved evidence and inherit the same original source.

#### Scenario: Accept an exact reindex and refuse changed original bytes

- **WHEN** the owner independently validates a different complete index key for the same original bytes
- **THEN** the new key is admitted and queried within the same bounds.

#### Scenario: Refuse missing or changed inherited source

- **WHEN** the named evidence is absent, conflicted or no longer matches the exact source record or original bytes
- **THEN** the follow-up refuses before querying or submitting to a model, without substituting another source.

#### Scenario: Deliberate retarget or explicit no-document

- **WHEN** the owner admits a different exact original or an explicit or inherited no-document choice
- **THEN** a retarget uses its own source and locator without rewriting prior evidence, while no-document performs no source query or document-scoped memory query.

### Requirement: Source-aware follow-up submission requires fresh evidence

The opt-in ordinary Reader SHALL use the one prepared frame for answer assembly
and persist it through the existing conditional evidence publication. It SHALL
proceed only from a definite fresh acknowledgment whose exact root is still
current. The original input visit, Store generation, root, user, evidence and
receipt, named anchor and admitted source SHALL remain pinned through actual
model handoff, result admission and Generated publication. Existing output
ownership and exact verified completion remain required. Historical or uncertain
publication SHALL allow only original receipt reconciliation, without a new
query, submission or output. See the
[ordinary follow-up design](../../ordinary-reader-source-followups.md).

#### Scenario: Currentness changes during preparation or answer

- **WHEN** the original visit, root, user, saved evidence, anchor or source becomes stale or conflicted before a guarded stage
- **THEN** later work refuses and a result from lost ownership cannot become a Generated draft or verified output.

#### Scenario: An evidence write may have committed

- **WHEN** publication returns an uncertain outcome or only a historical acknowledgment
- **THEN** the attempt stops without submitting a model request or authorizing output, and reconciliation is restricted to the original evidence operation.
