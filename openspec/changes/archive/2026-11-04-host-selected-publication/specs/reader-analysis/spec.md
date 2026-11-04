## ADDED Requirements

### Requirement: Development transport ownership
Development transport SHALL compile only for explicit tests and the opt-in
retained-store harness. The installed selected backend SHALL refuse requests
and effects without a qualified producer.

#### Scenario: Installed selected request refuses
- **WHEN** the installed refusing backend is asked to process acknowledged prepared input
- **THEN** it SHALL refuse before any model call, publication or device effect.

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
- **THEN** the changed selection SHALL refuse Generated publication. Configured subject memory SHALL refuse before the prepared path calls the model.
