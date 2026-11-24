## ADDED Requirements

### Requirement: Installed Reader role text and resident source target

Installed Reader SHALL store the verified interpreted question and generated answer as separate verbatim role texts and retain the normalized target on the original resident capture linked to those turns. The target SHALL identify the same captured document, page and overview used for analysis. Updating the capture to retain that target SHALL publish atomically with the interpreted user turn and SHALL preserve all original image descriptors and media. Ordinary continuation SHALL attach the existing historical images and expose the target on the matching overview association when available, under the existing turn eligibility and evidence checks.

#### Scenario: Reopen a conversation after an installed Reader question

- **WHEN** ordinary continuation reads a reopened conversation with a verified Reader interpretation and stored source target
- **THEN** eligible role text is presented without generated QA markers or duplicated question text, and the matching overview identifies the original capture, origin turn, source document and page, dimensions and normalized target.

#### Scenario: Open earlier history

- **WHEN** an earlier resident record lacks a structured target
- **THEN** its original text and image association remain readable and no target is synthesized from role text, a page heading or a new capture.
