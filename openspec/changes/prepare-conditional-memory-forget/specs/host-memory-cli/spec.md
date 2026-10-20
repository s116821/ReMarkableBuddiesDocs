## ADDED Requirements

### Requirement: Prepared conditional one-fact forget
The host CLI SHALL provide bounded strict stdin preparation and explicitly confirmed one-fact forget with original configured profile/paths, Store actor/generation, mode token and admitted local/selected identity. Selected catalog/aggregate acceptance evidence SHALL be compared under existing gates independently of Key/head IDs. Existing regular-file APIs SHALL remain unchanged and unrelated mutations/setup SHALL retain early stdin refusal. Search/inspection alone SHALL NOT authorize mutation.

#### Scenario: Same-view deliberate preparation
- **WHEN** a host prepares one deliberate configured-profile fact and intent UUID
- **THEN** one guarded supported-value preview and immutable same-admission evidence are returned, while absent/tombstone/conflicting/opaque or unavailable views refuse without head selection or initialization.

#### Scenario: Changed original binding
- **WHEN** config, paths, profile, mode/re-entry or selected catalog/base/aggregate generations change despite identical Key/head IDs
- **THEN** confirmation refuses before mutation rather than refreshing original preconditions or switching namespace.

#### Scenario: Historical acknowledgement and receipt-only reconciliation
- **WHEN** the original exact request has a provable accepted receipt and the target later changes
- **THEN** a historical acknowledgement may be returned only after original namespace/predecessor checks, without another tombstone or current-deleted claim; receipt absence or unprovable evidence SHALL NOT dispatch a mutation.

#### Scenario: Unknown outcome remains explicit
- **WHEN** confirmation may have committed but output is lost, partial, cancelled or disconnected
- **THEN** the host retains the exact original intent and uncertainty, clears stale detail, never auto-retries or creates replacement intent, and requires fresh deliberate inspection for current state.

#### Scenario: Tombstone scope and compatibility
- **WHEN** a valid prepared forget commits locally or to admitted selected membership
- **THEN** history and original documents remain, no disk purge or immediate cloud propagation is claimed, and legacy file/unsupported-build behavior remains explicit without remote staging or service/provider startup.
