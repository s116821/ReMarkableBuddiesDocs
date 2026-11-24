## ADDED Requirements

### Requirement: New installed Reader exchanges show an About line

When an ordinary installed Reader question introduces a recognized or explicitly uncertain source subject, the existing authorized page renderer SHALL put an `About:` line before Q&A within the resolved page's existing format. The line SHALL be emitted once for that exchange. The renderer SHALL preserve valid Q&A on its own when the optional line does not fit the existing output bounds. A plain typed continuation SHALL NOT add About from inherited source metadata.

#### Scenario: Render a fresh exchange on an installed conversation page

- **WHEN** the current authorized Reader exchange has a recognized subject and the renderer can present it
- **THEN** the page shows that subject on a single About line above the unchanged question and answer
- **AND** a newly created page keeps its configured title and a reused page adds no title

#### Scenario: Render an explicitly uncertain subject

- **WHEN** a fresh verified Reader exchange has explicit uncertainty about its selection and the renderer can present the line
- **THEN** the page shows a neutral About line stating the uncertainty above the unchanged Q&A
- **AND** no inferred subject text is stored for later turns

#### Scenario: Render a plain continuation

- **WHEN** an ordinary typed turn continues a conversation with a stored subject
- **THEN** only the continuation content is presented for that turn
