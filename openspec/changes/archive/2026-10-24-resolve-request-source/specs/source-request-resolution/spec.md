## ADDED Requirements

### Requirement: Source inheritance follows an explicit historical anchor
The ordinary ledger SHALL resolve an explicit source declaration or inheritance
from a caller-named earlier request-evidence operation for an existing interpreted
Reader request. It SHALL preserve explicit no-document and deliberate changes,
validate same-conversation original provenance against current ordinary records,
and SHALL NOT infer active intent, choose a timestamp winner, use a page binding
as a source registry or substitute the visible Buddy page.

#### Scenario: Named inheritance and deliberate change
- **WHEN** a caller names a valid earlier evidence operation or explicitly selects another valid original/no-document choice
- **THEN** the ordinary result carries that declared source, preserving prior no-document and exact original turn/source identities without changing any stored record.

#### Scenario: Missing anchor or invalid historical association
- **WHEN** the operation is omitted, multiple prior operations disagree, or a named dependency is absent, foreign, future, conflicted, corrupt or has changed source content
- **THEN** an omitted operation remains unresolved and invalid named dependencies refuse, while an explicitly named valid operation resolves independently of other operations without silently choosing another candidate.

### Requirement: Resolution preserves independent receiving admission
Resolution SHALL require a caller-supplied complete index key for original-source
results and no key for inherited no-document. It SHALL reuse bounded historical
readback/current association validation, return only ordinary historical data,
perform no retrieval or publication and preserve existing receiving/evidence
schemas and admission. Resolution SHALL NOT imply model consumption, source
freshness, selected/native authority or snapshot continuity into a later call.

#### Scenario: Reindexed or stale source key
- **WHEN** a named original choice is resolved with an independently supplied key
- **THEN** the resolver validates key shape/document identity without substituting the saved key, allows a valid independently reindexed same document, and leaves stale Provider/current snapshot refusal to subsequent receiving admission.

#### Scenario: Restart, bounds and absence of effects
- **WHEN** complete ordinary history is reopened or required metadata exceeds existing bounds or is unavailable
- **THEN** valid history resolves without queries/writes and unavailable or oversized dependencies refuse with sanitized errors, without retained-winner recovery or changing stored evidence.
