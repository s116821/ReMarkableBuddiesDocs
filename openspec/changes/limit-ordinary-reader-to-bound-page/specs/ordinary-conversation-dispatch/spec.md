## ADDED Requirements

### Requirement: Ordinary Reader scope starts at the bound original page

Ordinary installed Reader SHALL use the original page immediately left of its Buddy page together with the current conversation and eligible memory. A new source-page question SHALL use its verified captured page. A typed continuation SHALL use the new request separately and SHALL attach an original page only when retained evidence matches the binding's original document and adjacent left page. A blank conversation without an eligible original SHALL stay source-less.

#### Scenario: Ordinary request with a mapped or archived document

- **WHEN** an ordinary request arrives with a mapped PDF or EPUB or a retained notebook transcription
- **THEN** Reader SHALL answer from the eligible bound page, conversation and relevant memory without acquiring, extracting or revalidating material from other pages to build or supply extra context, and without sending other pages for OCR.
- **AND** an optional lookup may use immediately available current text only when it is relevant, selective and quick. Such a lookup is not required; a mapping or archive alone does not qualify.

#### Scenario: Typed continuation on a bound Buddy page

- **WHEN** a new typed turn is submitted on a bound Buddy page
- **THEN** Reader SHALL preserve the exact turn and conversation history and include only a matching left-page capture as original evidence.
- **AND** an older indexed request SHALL grant no automatic document-wide scope to the new turn.

#### Scenario: A prior conversation turn links unrelated media

- **WHEN** a retained conversation turn points to an archived transcription or another page's image
- **THEN** ordinary Reader and shared intent routing SHALL preserve chronological turn text without reading or hashing the unrelated media. Reader SHALL still verify and attach its eligible original page.

#### Scenario: Typed continuation without an eligible original

- **WHEN** a blank-start conversation or a binding with no matching retained original capture receives a typed continuation
- **THEN** Reader SHALL use its request, conversation and eligible memory without substituting another page or a full-document source.
