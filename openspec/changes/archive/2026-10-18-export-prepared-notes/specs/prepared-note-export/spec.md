## ADDED Requirements

### Requirement: Prepared content uses portable exact correlation
The exporter SHALL accept explicitly prepared content and source provenance,
reuse the existing stable metadata key/title marker, and resolve only verified
native note identities. It SHALL expose missing, duplicate, malformed and
incomplete discovery rather than fuzzy-match or silently select a note. Mem
SHALL use the supported title path and bounded chronological discovery rather
than treating relevance-search absence as exhaustive. No second registry or
network-queryable Buddy service SHALL be introduced.

#### Scenario: Create then find and update
- **WHEN** a prepared note is exported, the service is reopened and a later source revision is deliberately exported under the same correlation
- **THEN** the same verified destination note is updated, the stable marker and useful source provenance survive, and each operation retains its historical result.

#### Scenario: Ambiguous or incomplete discovery
- **WHEN** exact discovery finds duplicates, malformed scope, missing markers or exceeds its bounds
- **THEN** it reports the explicit unresolved/conflict outcome without overwriting a note or assuming a search miss permits creation.

### Requirement: External writes preserve version and uncertainty boundaries
The exporter SHALL durably record a per-export attempt before one external write,
distinguish fresh local preparation from historical replay, verify prior exported
body and current destination version before replacement, and confirm exact result
identity/content before recording completion. Mem SHALL use documented complete
Markdown/version requests, bounded HTTPS transport and private credentials with
no automatic side-effect retry or redirect. Reconciliation SHALL read known IDs
and exact markers/content without resending an uncertain create/update.
The result SHALL describe observed desired content, not claim that readback proves
a particular HTTP call executed. Prepared Markdown and useful human-readable
provenance SHALL be preserved without a redundant machine-ID footer; per-effect
scope/revision/hash/version facts SHALL remain in the existing Ledger.
All same-Store export/reconciliation calls SHALL share a live invocation owner
through prepare, dispatch and result; overlapping calls SHALL return Busy rather
than observe an unfinished sender as a released operation. The Store commit
mutex SHALL NOT be held over HTTP.

#### Scenario: Lost response or cancellation after dispatch
- **WHEN** a write may have reached the destination but its acknowledgment is lost or cancellation arrives
- **THEN** the operation remains exported if confirmed or explicitly requires reconciliation, and neither retry nor restart blindly resends it or claims to undo the external effect.

#### Scenario: Remote edit or version conflict
- **WHEN** the destination body differs from the recorded previous export or its conditional update conflicts
- **THEN** export refuses replacement and preserves the remote edit for explicit refinement.

#### Scenario: Desired body is already current
- **WHEN** verified exact-ID/marker readback already contains the complete desired body with consistent version evidence
- **THEN** export records the verified-current result without a redundant PATCH or a claim that it performed a new remote mutation.

#### Scenario: Credential or transport failure
- **WHEN** credentials are absent or a bounded request fails
- **THEN** a sanitized typed outcome exposes whether dispatch may have happened without logging credentials or private note content.

#### Scenario: Cancellation before send permits deliberate later export
- **WHEN** cancellation positively occurs before dispatch and a later new effect UUID exports the same stable association
- **THEN** the new operation may proceed under current heads, the canceled operation is not replayed, and old receipts remain inspectable.
- **AND** cancellation winning before the non-effectful write future is first polled is recorded as no-send rather than stranding an unsent attempt as an uncertain external write.

#### Scenario: Retry overlaps a live sender
- **WHEN** a second same-Store export/reconciliation call arrives while its first sender still owns the invocation
- **THEN** it returns Busy and makes no second dispatch or successor cycle until the owner releases.
