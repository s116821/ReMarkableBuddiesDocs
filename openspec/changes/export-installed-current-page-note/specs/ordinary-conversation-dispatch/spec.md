## ADDED Requirements

### Requirement: The shared source submission can export a current-page note

The installed ordinary Writer receiver SHALL offer current-page note export on the same shared submission as Reader and draft-only Writer. It SHALL preserve the exact request and export only its fresh guarded draft through the configured note destination. It SHALL retain the existing stale, uncertain and retry behavior and use the Buddy page to report the result.

#### Scenario: A source request explicitly asks to save a note from the open page

- **WHEN** the user submits an unambiguous handwritten request to create and export a note from the open page
- **THEN** Writer SHALL generate from that page, submit through the configured destination, and display the draft and observed export result on the bound Buddy page
- **AND** a later request to save the same current-page note SHALL retain the source document and page correlation, including across gestures before a Buddy page is bound or after placement fails. The receiver SHALL retain an applicable earlier correlation on the owned conversation. An explicitly separate note SHALL have a distinct correlation.

#### Scenario: The draft and export outcome together exceed the native text limit

- **WHEN** the full Writer exchange cannot be typed on the applicable Buddy page
- **THEN** the receiver SHALL select a compact truthful result under the same page and text checks, retaining the complete draft and export association in Buddy history
- **AND** the presentation path SHALL make no additional destination write.

#### Scenario: A save or export request leaves the source or action ambiguous

- **WHEN** a handwritten save or export request lacks an unambiguous supported source or effect
- **THEN** Buddy SHALL save the literal request and clarification in the same conversation before presentation. The normal history reader SHALL include both turns. The receiver SHALL make zero destination calls.

#### Scenario: Ownership changes or the destination result is uncertain

- **WHEN** the source changes before dispatch or the destination cannot verify a possibly dispatched write
- **THEN** Buddy SHALL stop a stale attempt before the write or preserve the uncertain attempt for reconciliation, respectively.
