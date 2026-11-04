## ADDED Requirements

### Requirement: Local selected outbox status is a complete bounded read

The fixed exclusive no-input Buddy selector SHALL report versioned counts
of validated actor-owned pending and withdrawn local selected-attempt
journal records from an admitted existing Store. It SHALL reuse the
existing selected-aware maintenance custody and whole bounded inventory.
It SHALL expose no private journal fields or provider/operation identities.
Busy, unavailable, corrupt and unsupported reports SHALL carry null counts.
The selector SHALL refuse notebook format 4 or notebook marker custody
under V1, without claiming an empty journal. The selector SHALL retain the
Store lock through one output attempt and SHALL perform no mutation,
provider I/O, retry, restore, worker activation or native operation.

#### Scenario: Valid existing local journal

- **WHEN** an admitted Store has a complete validated selected-attempt inventory or definitively no journal
- **THEN** the report gives the exact historical local pending and withdrawn counts and grants no current publication or retry authority.

#### Scenario: Refused or incomplete custody

- **WHEN** the Store is busy, unavailable, incompatible or notebook-marked, or any present journal entry fails admission
- **THEN** the report gives the applicable refusal with null counts and neither repairs nor initializes state.

#### Scenario: Output failure

- **WHEN** the report writer fails after beginning the frame or at flush
- **THEN** existing custody lasts through the failed attempt and there is no second output, mutation or retry.
