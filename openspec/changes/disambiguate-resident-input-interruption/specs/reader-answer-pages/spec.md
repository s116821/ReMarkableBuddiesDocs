## ADDED Requirements

### Requirement: Resident request input distinguishes passive packets from interruption

The active resident Reader guard SHALL disregard LED, sound and repeat-setting packets and the miscellaneous timestamp code. Genuine input and incomplete contact frames SHALL keep their existing cancellation behavior. A dropped frame or failed observer SHALL take the existing integrity-loss path. The guard SHALL log one fixed first-interruption category for an observed action, nonquiet contact or input loss, without raw events or user content.

#### Scenario: Passive packets arrive after observed page insertion

- **WHEN** the original insertion reply has been retained and only passive packets arrive during the next guarded observation
- **THEN** the request continues through the existing source and target checks and keeps the exact original insertion receipt.

#### Scenario: Genuine input or observer loss follows insertion

- **WHEN** a real input action, a held or incomplete contact, or an observer loss is first encountered
- **THEN** the existing cancellation or integrity path stops the request and records its first category
- **AND** the original insertion receipt remains available without a retry, automatic placement or a claim of visible output.
