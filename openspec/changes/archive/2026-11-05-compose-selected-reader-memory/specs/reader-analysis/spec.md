## ADDED Requirements

### Requirement: Composed selected memory publication
Compatible selected subject memory and selected Reader draft publication SHALL use
one canonical ordered admission set, preserving original payload/token/raw-head
and budget seals. The writer SHALL NOT reacquire an already-held participating
gate. Unsupported or foreign providers SHALL refuse before model/publication.

#### Scenario: Memory and Reader share a document key
- **WHEN** the same selected document scope participates in both the memory view and Reader draft
- **THEN** its gate is held once with the complete ordered set, both inputs are revalidated, and the guarded draft publishes without duplicate gate acquisition or new native authority.

#### Scenario: Selected resident historical evidence
- **WHEN** the selected prepared request references a complete resident historical capture and compatible selected memory
- **THEN** the exact saved overview and detail images are reused, source ownership and required media are checked before text publication, and the enriched draft uses the shared admission without granting native output authority; replacement or failed writes publish no draft.

## MODIFIED Requirements

### Requirement: Selected request and draft publication
Selected interpretation and Generated drafts SHALL use canonical selected
admission, exact acknowledged root/user references and preserved evidence.
Failed publication SHALL stop without an ordinary write or later effect.
An acknowledged Generated draft SHALL leave Pending, settlement and native
output unavailable.

#### Scenario: Draft acknowledgment lost before retry
- **WHEN** the same operation and original input are retried after an acknowledged selected draft publication
- **THEN** the original receipt and pins SHALL be recovered before stale-head checks. The selected history SHALL contain one draft and no new live authority.

#### Scenario: Prepared preferences retain currentness
- **WHEN** a prepared request uses a personalization preference and the selected view changes during that model call
- **THEN** the changed selection SHALL refuse Generated publication. Unsupported or foreign subject-memory providers SHALL refuse before query or model work. An explicitly compatible selected Provider MAY enrich only through the sealed selected-memory path and joined publication; it SHALL NOT bypass currentness or grant native authority.
