## ADDED Requirements

### Requirement: Explicit feedback generation capability
Storage contract2 SHALL introduce UnassociatedFeedback schema1 only under an actor/generation-bound format3 feature, preserving contract1 and legacy1/2 bytes/behavior and existing schema2 domain restrictions. New namespace commit/import/recovery admission SHALL verify the required feature/format relationship. Unavailable-history parsing alone SHALL NOT be treated as a global old-writer fence. Source: existing closed namespace contract, lifetime lease and generic publication mechanisms.

#### Scenario: Valid new namespace versus legacy generation
- **WHEN** a valid new-domain record is published against prepared3 or attempted against1/2/missing/foreign feature metadata
- **THEN** only the correctly prepared record may commit and unsupported cases do not publish a new observation.

### Requirement: Unique-owner feature adoption
Adoption SHALL be explicit through a fresh uniquely owned Store under the retained exclusive lifetime lease before handles escape, never automatically on ordinary open or by upgrading a live shared Store. Feature marker/readback, format3 and first record ordering SHALL be proven across crashes. Already-open/in-flight custody, passive historical values and native authority SHALL be distinguished; the gate is not a blanket per-publish or native rollback guarantee. Source: open-time validation and owned-store lease order.

#### Scenario: Existing owner or interrupted preparation
- **WHEN** another owner retains the Store lease or preparation stops between feature/format/record publication
- **THEN** no unsupported record is committed under a legacy format and actual readback determines readiness/refusal without guessed waits or worker bypass.

### Requirement: Versioned archive and monotonic activated compatibility
Qualified ordinary format3 backup and a separately prepared additive restore SHALL preserve exact record/media bytes and current-plus-archive union/collision semantics, carry required same-actor version3 feature metadata, and bind staged structural features to the admitted owner/generation without rewriting original IDs or restoring native authority. Existing restore APIs/default eligibility SHALL remain unchanged for legacy state and refuse unsupported3. Selected backup2/current2 or selected metadata, and cross-owner archive3, SHALL be unsupported by the new route. Restoring legacy archive1 into activated3 SHALL retain3. Old archive readers/writers and unqualified maintenance SHALL be explicitly unsupported; no safe downgrade is inferred. Source: conflict-preserving recovery, versioned archives and separate selection/native qualification.

#### Scenario: Restore older history after adoption
- **WHEN** the separate prepared route additively merges an eligible archive with current ordinary history in activated3
- **THEN** original history bytes and identity/collision semantics are preserved, prior current is preserved on preactivation failure, and format3 compatibility is retained rather than exposing new data to an old writer.

#### Scenario: Selected history and unsupported consumer
- **WHEN** selected2 history coexists with feedback3, or an old/unknown reader or maintenance path is used
- **THEN** selected history remains historical with unchanged authority and no added selected-restore eligibility, and unsupported paths refuse without claiming a compatible downgrade or native rollback.

### Requirement: Monotonic generation and capability publication
Activated3 SHALL retain its validated feature and format across every admitted creation/CURRENT/recovery/import path or refuse. Compatible open SHALL publish contract2 and six-domain capabilities2 for3 without erasing support on reopen; unchanged legacy1/2 publication and contract1 bytes SHALL remain intact. Generic migration from/to3 SHALL refuse before staging until separately qualified. Source: existing format1 generation creator and per-open five-domain publication.

#### Scenario: Reopen or create next generation after activation
- **WHEN** activated3 is reopened or an admitted additive generation is staged
- **THEN** feature/format3 and truthful capabilities persist before admission, and no helper or unsupported migration downgrades state to1/2.
