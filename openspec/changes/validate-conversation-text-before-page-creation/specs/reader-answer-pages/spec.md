## ADDED Requirements

### Requirement: Validate conversation text before page creation

When the installed Buddy needs a new conversation page, it SHALL check the fully formatted output against the existing keyboard repertoire and length limits before asking the tablet to insert a page. A rendering refusal SHALL preserve the original generated content and SHALL leave the insertion journal untouched. The renderer SHALL still check the text for the actual destination before typing.

#### Scenario: Reader cannot type the answer on a new page

- **WHEN** the exact question and answer together with the creation heading exceed a limit or need a character the keyboard cannot type
- **THEN** the saved answer remains in the conversation, output is unavailable, and Buddy does not request an insertion

#### Scenario: Optional About line would exceed the limit

- **WHEN** the optional source description cannot be rendered but the creation heading and exact Q&A fit
- **THEN** Buddy may create the page with the intact Q&A and omit the optional line

#### Scenario: Writer draft fits an existing page

- **WHEN** the plain draft fits the verified bound page, but adding the creation heading would exceed a limit
- **THEN** Writer may present the draft on that existing page without repeating the heading
- **AND** the same draft cannot cause an insertion if a new page would be required
