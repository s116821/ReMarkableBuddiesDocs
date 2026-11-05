## ADDED Requirements

### Requirement: Explicit protected same-actor notebook restoration
The backend SHALL expose notebook prepare/apply/status through the existing
protected restore maintenance family with explicit versioned selectors/intents.
It SHALL admit only a ready local notebook Store and a completely validated
same-actor format4 archive, preserving existing OS custody, config/path/mode and
media guards. Legacy restore SHALL NOT silently admit notebook layouts.

#### Scenario: Complete same-actor archive
- **WHEN** an idle ready local notebook Store prepares a supported complete same-actor archive
- **THEN** it returns an additive original intent bound to exact source/config/mode/base/target identity without changing CURRENT or applying configuration.

#### Scenario: Unsupported or changing input
- **WHEN** archive actor/schema/media, Store readiness/mode/ownership or original source/config/base conditions disagree
- **THEN** admission refuses without native/provider work or target activation, retaining original local state and archive bytes.

### Requirement: Conditional notebook publication and reconciliation
Apply SHALL reuse the existing notebook generation writer with the original
absent target and complete expected history, distinguishing known no-activation
from possibly attempted publication. It SHALL verify actual desired state before
reporting restored. Status SHALL observe only, without replay/repair or renewing
original authority. Staged configuration SHALL remain unapplied; native references
SHALL remain historical.

#### Scenario: Additive restore and exact readback
- **WHEN** original conditions still hold and generation publication/readback succeeds
- **THEN** all source and unrelated current records/media remain, the target is verified and runtime/native activation is not claimed.

#### Scenario: Lost acknowledgement or interrupted publication
- **WHEN** publication may have occurred or capability/readback completion is unknown
- **THEN** the original outcome remains unknown and later Status can report desired state without repeating Apply or claiming historical rollback/success.

#### Scenario: Legacy request
- **WHEN** a legacy selector or version1 intent encounters a notebook archive/generation
- **THEN** existing unsupported behavior remains unchanged rather than selecting the new path automatically.
