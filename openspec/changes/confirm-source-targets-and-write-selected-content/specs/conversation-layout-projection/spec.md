## ADDED Requirements

### Requirement: About follows persisted target use
Actual answer serialization and historical projection SHALL show distinguishable About for introduced/corrected/retargeted source turns using exact persisted target/use. Inherited turns SHALL omit repetition. Inline recipe/body hash SHALL prevent duplicate projection. Historical metadata SHALL grant no native currentness/output authority.

#### Scenario: Selected Generated projection
- **WHEN** a selected Reader generates target-associated content
- **THEN** About remains Generated/data projection without Pending/native rendering or a fabricated presentation binding.

#### Scenario: Writer presentation is separate from model context
- **WHEN** historical presentation reads a regional Writer exchange with a Generated draft
- **THEN** a bounded read-only presentation view includes the exact Writer body and validates its bound hash and Markdown About position before omitting duplicate metadata
- **AND** the existing model-context turn filter remains unchanged; neither the presentation view nor its logical page identity grants native output authority
- **AND** a changed body hash or misplaced About retains explicit target metadata rather than suppressing it by substring matching.
