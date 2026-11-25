## ADDED Requirements

### Requirement: Research for an installed Reader question on a captured page

After Writer arbitration, an ordinary installed Reader with verified input scoped to the bound original page SHALL verify the handwritten question and web intent independently before applying the saved research policy. It SHALL retain the exact interpreted request, its historical page evidence, and eligible document and global subject memory without claiming indexed passages.

#### Scenario: Default research on a handwritten notebook question

- **WHEN** both readings agree on a question and report no restriction, and the saved policy is Required
- **THEN** Reader SHALL use the existing qualified web provider under the captured request and source guards before composing a cited answer.
- **AND** an unavailable required provider, invalid result or changed source SHALL prevent an answer from being generated or written.

#### Scenario: A handwritten follow-up is on a bound Buddy page

- **WHEN** the current capture is the conversation’s bound Buddy page
- **THEN** Reader SHALL use that capture to read and retain the new question while resolving any original research source and answer attachment from the retained capture of the bound page immediately to its left.
- **AND** an older conversation with no request source record SHALL reuse its retained, interpreted capture of the original page identified by the binding, when available.
- **AND** a blank-start conversation without an original SHALL stay source-less. A fresh question on its own original page SHALL use that fresh capture even when a Buddy page is already adjacent.

#### Scenario: A verified request skips internet research

- **WHEN** both readings agree on an explicit no-internet directive, or the saved policy is Disabled
- **THEN** Reader SHALL make no search call. Its answer may use the verified page image and eligible subject memory.
- **AND** an ambiguous or conflicting intent SHALL never authorize search.
