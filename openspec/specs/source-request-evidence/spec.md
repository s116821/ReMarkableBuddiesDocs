# Source request evidence

## Purpose

Persist inspectable ordinary historical request selections with exact source and
passage provenance, atomic stale-state admission and bounded original-reference
validation. These records do not confer current effect authority or prove model
consumption.

## Requirements

### Requirement: Ordinary evidence preserves the selected request context
The ordinary ledger SHALL explicitly persist a bounded immutable historical fact
for an existing interpreted Reader request using the validated receiving frame,
exact original record references, complete source/key/passage provenance and
reported admissions. It SHALL preserve explicit no-document, zero-match and
unavailable-media distinctions without changing capture batches, creating another
source registry or implying model consumption, current source freshness or native
authority. The existing read-only receiving API SHALL remain read-only.

#### Scenario: Bound selection and changed source
- **WHEN** a fresh local selection is recorded for a request or a deliberate new operation selects another valid original source
- **THEN** the exact frame and its original source/passage identities survive restart as distinct historical facts, without automatic inheritance or current-Buddy-page substitution.

#### Scenario: Explicit absence and zero matches
- **WHEN** preparation chooses no-document, returns a source-bound zero-match result or reports unavailable original media
- **THEN** no-document makes zero queries and fabricates no source, while persisted zero-match and unavailable evidence retain their distinct source/provenance meanings across readback.

### Requirement: Evidence publication is atomic and currentness checked
Fresh evidence publication SHALL bind the originating Store, captured generation
and exact relevant record heads across ordinary atomic root/fact/receipt commit.
It SHALL preserve original immutable object identity, reject a stale preparation,
honor stable operation/content retries and complete encoded/work bounds, and SHALL
NOT retry a query, truncate context or resurrect deleted state to produce success.

#### Scenario: Records change during preparation
- **WHEN** a relevant request/history/source revision, generation, conflict or tombstone changes after capture, including during callbacks
- **THEN** fresh publication refuses without attaching the stale frame or exposing a partial fact/root/receipt, while unrelated conversations remain independent.

#### Scenario: Retry and interrupted publication
- **WHEN** an operation is retried after a lost acknowledgment, concurrent winner or process restart, or reused with different evidence
- **THEN** identical committed content resolves to its original historical acknowledgment/fact without another query or write; changed content refuses, and precommit failure leaves only the prior complete logical state.

### Requirement: Historical evidence remains inspectable with exact references
Inspection and ordinary export/import/delete handling SHALL preserve the recorded
frame and qualification, validate exact bounded historical record references and
receipt relationships, and distinguish declared unavailable media from required
record corruption or unsupported data. Reading a fact SHALL NOT mint a writable
preparation, select a retained winner or grant current effect authority.

#### Scenario: Restart export and deletion
- **WHEN** complete or metadata-only ordinary history is reopened/imported or its conversation is logically deleted
- **THEN** valid evidence and original acknowledgment remain historical and inspectable with explicit media availability, and retries do not recreate the deleted root or replay an effect.

#### Scenario: Invalid or oversized references
- **WHEN** frame/ref/receipt identities are foreign, absent, contradictory, unsupported, corrupted or exceed complete admission bounds
- **THEN** domain interpretation/publication refuses without a partial validated result, preserves stored evidence, and never substitutes reserialized bytes for an original committed reference.
