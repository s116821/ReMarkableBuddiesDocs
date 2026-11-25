## ADDED Requirements

### Requirement: A current ordinary Reader failure can use an existing Buddy page

When the ordinary installed Reader durably records a definite provider failure for an independently verified unmarked question, it SHALL use the original typed failure fact and its matching saved User turn. If the conversation has a safely associated existing Buddy page, Reader SHALL submit the verified question and the catalog's sanitized provider-failure message through the existing current-target output owner.

#### Scenario: A usable bound Buddy page is confirmed

- **WHEN** the original failure is current and resident placement confirms the conversation's existing bound Buddy page
- **THEN** Reader submits the verified question followed by the sanitized provider-failure text once
- **AND** the service returns the original provider failure and retains the owned failure fact. Source ink stays intact.

#### Scenario: No usable target or uncertain placement

- **WHEN** the Reader lacks a safe existing Buddy binding or placement cannot be confirmed
- **THEN** the owned failure fact stays available to the stored feedback receiver, without new page creation or source feedback
- **AND** an unverified write retains its actual disposition without replay or a fabricated success claim.

#### Scenario: Existing marked or canceled request

- **WHEN** the question follows the marked-question path, the request is canceled, or its source or stored failure changes
- **THEN** the unmarked provider-error placement does not run and the corresponding existing owner handles the outcome.
