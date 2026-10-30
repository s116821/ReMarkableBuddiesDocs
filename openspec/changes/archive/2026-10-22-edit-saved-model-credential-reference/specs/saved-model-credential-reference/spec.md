## ADDED Requirements

### Requirement: Deliberate supported saved credential reference edits
The producer SHALL set/clear only saved model_credential under contract.md and existing name/full Config validation, preserving exact decoded spelling, unrelated declarations/origins and exact no-op bytes. It SHALL NOT discover/read/change credential files, retarget roots, resolve keys or change existing schema/precedence/wires. Inspect/prepare/status SHALL avoid declared-root probes; apply SHALL retain existing Config/Store root-and-ancestor path-safety metadata checks, including the credentials root, without credential-file content access or credentials-root mutation.

#### Scenario: Set, clear or retain declaration
- **WHEN** a supported name is set or a missing/null/present reference is cleared
- **THEN** exact grammar/case and raw declaration distinctions are preserved, missing clear creates nothing, declared-null clear changes origin, and logical no-op leaves original bytes untouched.

#### Scenario: Invalid original or patch
- **WHEN** whole original/target schema/value/shape/type/duplicate/cap or fixed change validation fails
- **THEN** the invocation refuses without repair, normalization, fallback, credential-file probe or disclosure of the original/new name.

### Requirement: Private original change and same conditional configuration custody
Fixed origin/presence reports SHALL disclose no reference text. Hash-only intent SHALL bind original file/path/private change/target, and apply SHALL separately verify the original change before the SAME existing writer/mutex/CAS/readback/current Store-mode custody through consuming output.

#### Scenario: Changed conditions or Busy
- **WHEN** original bytes/path/change/target differ or current ordinary/selected configuration custody is unavailable
- **THEN** bounded truthful refusal occurs without refresh/rebase, initialization, credential-file operation or new authority.

#### Scenario: Uncertain publication or output
- **WHEN** publication/readback/output may have occurred without a complete verified report
- **THEN** original uncertainty persists with no rollback/replay/second report, and custody ends only after consuming output or failure.

### Requirement: Saved reference is separate from credential readiness
Every operation SHALL keep runtime unverified. Pure original-intent status SHALL observe current desired full Config bytes only, without Store/root/credential/provider probes or historical settlement. Existing file operations and precedence SHALL remain unchanged.

#### Scenario: New reference or explicit clear
- **WHEN** saved reference change verifies
- **THEN** no file existence/private-mode/authentication/restart/revocation proof, file deletion or atomic two-file setup is inferred, and an older file invocation's unknown state is not settled by its now-stale Config binding.

#### Scenario: Explicit reconciliation
- **WHEN** original desired Config bytes are currently present or different
- **THEN** status returns desired-file-observed or unresolved without raw change/name, file authority, automatic retry or provider/runtime claim.
