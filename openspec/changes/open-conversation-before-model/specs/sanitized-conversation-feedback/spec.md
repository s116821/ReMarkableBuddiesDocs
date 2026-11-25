## ADDED Requirements

### Requirement: A failed open conversation shows a plain-language Buddy reply

After a source submission opens a conversation, an unsuccessful request SHALL produce a short, fixed, user-facing description of what failed in that conversation. Buddy SHALL reuse the existing sanitized outcome categories and preserve any request text it has already established. The reply SHALL omit technical diagnostics, provider payloads, account details and stack traces. If the conversation cannot currently be written, Buddy SHALL retain the outcome for presentation when that conversation can next be displayed.

#### Scenario: The model cannot answer after the page opens

- **WHEN** the user is on the newly opened conversation and recognition or the provider fails
- **THEN** Buddy shows a brief explanation as a conversation reply on that page without exposing technical details
- **AND** the request finishes with that failure without creating a second page or leaving a pending indicator active.

#### Scenario: A failed result becomes presentable later

- **WHEN** the destination is no longer current when the request fails
- **THEN** the user can see the retained explanation in the original conversation when it is next displayed
- **AND** Buddy leaves unrelated notebook pages untouched.

#### Scenario: A completed reply exceeds the page renderer's limit

- **WHEN** Buddy receives a complete reply that cannot be rendered in full
- **THEN** the generated text remains saved and the open conversation shows a short explanation by the normal feedback path
- **AND** the notebook keeps the single conversation page that was opened at submission.
