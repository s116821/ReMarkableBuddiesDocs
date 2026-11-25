## ADDED Requirements

### Requirement: A source submission opens its conversation independently of the model

The ordinary lower-right hold on a supported open source page SHALL capture the submitted source and promptly open its conversation. Buddy SHALL start placement as soon as it has the source identity and required source pixels. Routing, handwriting recognition, answer generation, answer text size and optional pending feedback SHALL NOT gate page opening. If the source already has an associated adjacent Buddy page, Buddy SHALL open it. Otherwise it SHALL insert one adjacent conversation page while preserving the source and any ordinary neighbor. The captured source and the selected conversation SHALL remain associated with the same pending request.

#### Scenario: Model is still working on the first handwritten request

- **WHEN** a user submits from a one-page notebook and the service receives no model response yet
- **THEN** the adjacent Buddy conversation becomes visible with the source page intact
- **AND** a later Reader or Writer reply appears in that conversation using the original source capture.

#### Scenario: A conversation already exists beside the source

- **WHEN** the user submits again from the associated source and the provider reply is delayed
- **THEN** the existing conversation opens while the provider is still pending, preserves its previous turns, and the notebook page count stays the same.

#### Scenario: The user switches pages during the request

- **WHEN** the conversation opened and the user moves to a different page before publication
- **THEN** the newly selected page and its contents are preserved
- **AND** the outcome stays associated with the original conversation.
