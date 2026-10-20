# Saved memory declaration producer

## Purpose
Deliberately edit only the supported saved memory.enabled/profile declarations while preserving existing selection, explicit maintenance and runtime boundaries. The detailed [contract](../../changes/edit-saved-memory-settings/contract.md) fixes exact wire shapes, limits and fingerprint recipes. Profile setup, consumer UI, membership and automatic Reader/runtime/native qualification remain separate.

## Requirements

### Requirement: Deliberate supported nested memory declaration edits
The producer SHALL edit only saved memory.enabled/profile under contract.md and current full validation, preserve exact accepted decoded UUID spelling and unrelated selection/values/origins, and keep a no-op byte-identical. It SHALL NOT create/migrate/discover/delete profiles, facts or membership, change mode/provider/runtime or widen existing wire.

#### Scenario: Parent and leaf presence
- **WHEN** a selected leaf is explicitly set or cleared with an absent or existing memory object
- **THEN** clear-only absent edits create nothing, a set creates only selected children, an existing empty parent stays declared, profile null differs from missing, and unrelated children remain exact.

#### Scenario: Inconsistent configuration
- **WHEN** enabled/profile/selection, UUID/type/schema/shape/cap or whole original/target validation fails
- **THEN** the bounded invocation refuses without repair, normalization, fallback or profile/domain initialization.

### Requirement: Private original patch and same conditional writer
Inspect/preview/apply/status SHALL expose only fixed enabled/profile origin/presence views and private digests, never old/new profile UUID or arbitrary values. Digest-only intent SHALL bind the original file/path/patch/target, and apply SHALL separately verify the retained original patch before the SAME guarded writer/CAS/readback/current Store-mode custody.

#### Scenario: Changed original conditions or Busy
- **WHEN** original file/path/patch/target changes or current write custody is Busy/unsupported
- **THEN** no refreshed conditions, new writer, domain grant or fallback is used and only truthful phase-limited refusal/unknown output is emitted.

#### Scenario: Unknown or prefix-failed save
- **WHEN** publication/readback/output may have occurred without a complete verified report
- **THEN** original uncertainty persists, custody ends only after consuming output/failure, and no second report/retry/rollback/profile reset occurs.

### Requirement: Saved declarations are separate from memory authority
Verified apply SHALL mean exact saved disk bytes with runtime unverified. Pure status SHALL require only original intent/file and prove current desired bytes, never historical authorship, a running profile or membership. Existing manual query/selected/catalog behavior SHALL remain unchanged, including manual maintenance being independent of enabled.

#### Scenario: Explicit disable or new profile declaration
- **WHEN** a valid saved disable/clear/profile change verifies on disk
- **THEN** no record migration/deletion, manual-command disablement, automatic Reader activation, membership or restart/next-request promise is reported.

#### Scenario: Explicit read-only reconciliation
- **WHEN** original desired bytes are currently present or different
- **THEN** status returns desired-file-observed or unresolved without raw patch/Store/declared-root/profile/provider probes or settlement of an earlier unknown attempt.
