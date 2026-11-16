## ADDED Requirements

### Requirement: Verified native and aggregate integration
Future unified native integration SHALL use verified input/page/currentness and
aggregate contracts from their existing owners, preserve exact transcript and
receiving semantics, and refuse unavailable capability instead of constructing
authority from simulated or saved facts. Enabled-memory receiving SHALL remain
with its separately reviewed caller change; the ordinary memory-disabled
qualification SHALL NOT be promoted to enabled-memory evidence.

#### Scenario: Missing real capability
- **WHEN** native composer/Submit/page effects or actual aggregate application lacks its verified owner contract
- **THEN** the unfinished operation remains unavailable and no native or remote acceptance is inferred from the host dispatcher.

#### Scenario: Separately delivered integration
- **WHEN** the existing owner supplies an independently reviewed selected capability
- **THEN** integration reuses its admission/lifetime/settlement and proves real source/currentness/stale-operation behavior before completion.

### Requirement: Durable native composer operations
The composer consumer SHALL reuse the existing resident transport and Store-owned
effect journal. Provision and clear SHALL reserve exact requests before dispatch,
retain original outcomes across restart, and refuse replay or continuation after
unresolved effects. Observation and key facts SHALL NOT imply current edit or
semantic Submit authority. The development capability SHALL remain unavailable
in ordinary release builds until its native integration is qualified.

#### Scenario: Lost mutation response
- **WHEN** a provision or clear may have been sent but its outcome is unknown
- **THEN** the original request remains consumed and no new effect for that conversation bypasses its unresolved state.

#### Scenario: Exact input retention before clear
- **WHEN** the consumer requests conditional clear
- **THEN** this submission has freshly committed a new durable User turn with exactly the submitted text to the same Store, and the native owner independently compares the selected range, genuine revision and text before editing.

#### Scenario: Historical or concurrent identical submission
- **WHEN** an append returns a historical receipt, a concurrent winner's receipt or a lost commit acknowledgment
- **THEN** the retained history remains available but that caller receives no new clear proof; identical text alone cannot authorize clearing another draft.

#### Scenario: Changed or malformed input
- **WHEN** input cannot be converted without loss, durable retention fails, or the live draft differs from the submitted selection
- **THEN** clear is refused and no success or discarded draft is inferred.

#### Scenario: Idle typing
- **WHEN** a key wait ends without a native attempt and the runtime owner admits a fresh connection
- **THEN** a new read-only wait may use the same still-valid native visit and range without provisioning again or replaying an effect.
