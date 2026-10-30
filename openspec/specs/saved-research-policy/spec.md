# Saved research policy

## Purpose
Persist deliberate research-policy declarations and capture an immutable typed
policy for the existing research API. The complete versioned
[producer wire contract](../../changes/archive/2026-10-25-save-research-policy/contract.md)
defines the request/report shapes, bindings, bounds and publication semantics.

## Requirements

### Requirement: Saved default-required research policy and immutable snapshot
Configuration SHALL support only an optional required/disabled saved declaration,
with absent/null resolving to Required and absent defaults preserving existing
serialization. A pure validated immutable typed snapshot SHALL feed the existing
research API without altering prior request/history or explicit NoInternet priority.
It SHALL NOT resolve environment/credentials, acquire research or imply file,
runtime, source or native authority.

#### Scenario: Saved policy enters actual research composition
- **WHEN** an actual temporary saved declaration is loaded and its snapshot is supplied to existing frozen-context research
- **THEN** Required attempts or refuses honestly, Disabled and explicit NoInternet make zero calls with distinct reasons, NoInternet dominates either saved policy and original request/history/context bytes remain exact.

#### Scenario: Declaration defaults and later changes
- **WHEN** the declaration is missing/null, explicitly set/cleared, invalid, or changed after a snapshot
- **THEN** supported defaults resolve to Required, invalid whole configuration refuses and the prior snapshot remains unchanged without an implicit reload or runtime claim.

### Requirement: Deliberate bounded saved-policy publication
The dedicated strict inspect/prepare/apply/status producer SHALL follow contract.md,
edit only the selected saved declaration and reuse existing checked-document,
Ordered target, conditional writer and custody/readback/receipt semantics.
It SHALL preserve no-op bytes and unrelated declarations, exact original
file/path/patch/target conditions and honest post-dispatch uncertainty.

#### Scenario: Conditional set and clear
- **WHEN** a supported explicit patch is prepared/applied to the same existing configuration under valid Store/mode custody
- **THEN** only the selected root declaration changes, no-op writes nothing and verified means exact target disk readback with runtime unverified.

#### Scenario: Invalid admission, conflict or uncertain output
- **WHEN** input/schema/size/path/patch/target/custody fails or publication/output may have occurred
- **THEN** the applicable bounded refusal/unknown result is retained without fallback, root retargeting, rollback or automatic retry.

### Requirement: Dedicated policy interface preserves existing boundaries
The new early exclusive CLI SHALL preserve old editor wires and the fixed broad
inspection v1 projection, expose only finite policy/origin/private workflow data
and keep inspection/prepare/status separate from Store/root/provider activation.
Manager/runtime/model/native consumption SHALL remain explicitly unqualified.

#### Scenario: Read-only inspection and reconciliation
- **WHEN** the policy is inspected or the original target is checked after an uncertain save
- **THEN** inspection consumes no stdin, neither operation opens Store/probes declared roots/initializes providers, and status proves only current desired bytes or unresolved, not authorship or earlier settlement.

#### Scenario: Existing editor and consumer compatibility
- **WHEN** valid policy declarations coexist with old settings or an old maintenance action/view is used
- **THEN** unrelated values/origins and existing wire shapes remain unchanged, old supported workflows preserve policy, and no new Manager or runtime capability is inferred.
