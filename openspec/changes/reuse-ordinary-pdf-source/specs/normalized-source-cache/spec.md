## ADDED Requirements

### Requirement: Ordinary Reader reuses verified original PDF material

The installed ordinary Reader SHALL be able to reuse bounded source material from its most recently admitted original PDF while the process is running. It SHALL check the current original file contents and the document, format, extractor, page count and normalized identity before using that material. Each request SHALL perform a fresh retrieval for its own verified question with the normal source, conversation and publication checks.

#### Scenario: A second question needs a different page

- **WHEN** Reader receives a second question about the same unchanged original PDF and its verified material still fits in the cache
- **THEN** it can find passages anywhere in that PDF without extracting the original text again, and the new answer cites the new question's passages.

#### Scenario: The source changes

- **WHEN** the original file contents, document identity, page count or extractor changes between two requests
- **THEN** Reader discards the old match and uses freshly admitted material, or ends the request if acquisition fails.

#### Scenario: Retention is unavailable

- **WHEN** the service restarts, the cache is empty, or a supported original PDF exceeds the retention limit
- **THEN** normal cold acquisition and retrieval remain available within the ordinary source limits.
