## ADDED Requirements

### Requirement: Ordinary installed Reader retrieves the current original EPUB

With local EPUB research enabled, the ordinary installed Reader SHALL bind the current captured question to the original EPUB for the same document and retrieve relevant passages across its declared spine. The conversation SHALL retain the exact request, original source identity and each cited section. Rendered page numbers SHALL NOT be presented as EPUB section locations. Existing verified handwriting, research policy, memory, cancellation and placement behavior SHALL apply.

#### Scenario: A question needs another chapter

- **WHEN** the reader asks a handwritten question on an original rendered page of an EPUB and the relevant words appear in another section
- **THEN** the question can produce an answer using the other section and cite its EPUB location on the same conversation turn.

#### Scenario: A book changes between questions

- **WHEN** a later question uses the same original publication and a fresh current page table
- **THEN** Reader may reuse its verified normalized text and searches again with the new question. A replacement or edit to the book requires a fresh admission. A change while a request is underway prevents stale publication.

#### Scenario: Another workflow owns the page or the release

- **WHEN** EPUB retrieval is disabled, a handwritten page was inserted into the book, or Writer owns the source submission
- **THEN** the existing owning workflow handles the request. A PDF-only setting does not authorize acquisition of the EPUB text.
