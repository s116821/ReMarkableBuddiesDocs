## ADDED Requirements

### Requirement: New installed Reader exchanges show an About line

When an ordinary installed Reader question introduces a recognized source subject, the existing authorized page renderer SHALL put an `About:` line before Q&A within the resolved page's existing format. The line SHALL be emitted once for that exchange. The renderer SHALL preserve valid Q&A on its own when the optional line does not fit the existing output bounds. A plain typed continuation SHALL NOT add About from inherited source metadata.

#### Scenario: Render a fresh exchange on an installed conversation page

- **WHEN** the current authorized Reader exchange has a recognized subject and the renderer can present it
- **THEN** the page shows that subject on a single About line above the unchanged question and answer
- **AND** a newly created page keeps its configured title and a reused page adds no title

#### Scenario: Render a plain continuation

- **WHEN** an ordinary typed turn continues a conversation with a stored subject
- **THEN** only the continuation content is presented for that turn
