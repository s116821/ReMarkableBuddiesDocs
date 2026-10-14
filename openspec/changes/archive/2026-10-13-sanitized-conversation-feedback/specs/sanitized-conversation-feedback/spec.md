## ADDED Requirements

### Requirement: Sanitized historical feedback description
The feedback catalog SHALL consume existing typed historical outcome facts and return only original identity plus deterministic static code/text. It SHALL NOT copy raw diagnostic, provider, auth, request or answer text into user-facing descriptions or grant current rendering permission.

#### Scenario: Malicious or secret-containing conversational text
- **WHEN** recorded request/output or diagnostic text contains sensitive data
- **THEN** catalog output remains typed static text with original fact identity and no source-text serialization or ledger mutation.

### Requirement: Truthful uncertainty and refusal
Uncertain reason or ReconcileRequired state SHALL produce reconciliation feedback rather than claiming canceled, undone or delivered output. Completed facts SHALL produce no error description; nil identities and unsupported non-feedback states SHALL refuse.

#### Scenario: Cancellation overlaps uncertain external action
- **WHEN** historical outcome or reason denotes uncertain submitted/device action
- **THEN** description requires checking and cannot claim rollback, cancellation completion or a new successful delivery.

#### Scenario: Unsupported or completed historical fact
- **WHEN** identities are missing, state is unsupported or a fact is already completed
- **THEN** invalid context refuses and completed context yields no new error or success receipt.
