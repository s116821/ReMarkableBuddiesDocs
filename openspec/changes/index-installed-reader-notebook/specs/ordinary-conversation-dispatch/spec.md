## ADDED Requirements

### Requirement: Installed Reader retrieves verified local handwritten notebook passages

An ordinary installed Reader with an admitted original handwritten notebook source SHALL use eligible current local normalized notebook text for bounded passage retrieval where available. It SHALL open the Buddy page before provider work. The evidence SHALL exclude Buddy output and identify the original notebook and original page of each passage.

#### Scenario: The answer is on another original page

- **WHEN** the notebook has multiple original pages and local normalized material matches their independently admitted images and order
- **THEN** Reader SHALL retrieve relevant passages for the current verified question and retain their original page provenance in the request evidence.

#### Scenario: Another question or changed notebook

- **WHEN** the original saved revision and local index inputs still match
- **THEN** Reader MAY reuse the derived index for a fresh search.
- **AND** source drift after admission SHALL prevent publication from stale material.

#### Scenario: Captured-page handling remains available

- **WHEN** qualifying local material is missing, the original notebook is unsupported, or the source has one original page
- **THEN** Reader SHALL use its existing captured-page route without claiming indexed notebook passages.
- **AND** this workflow SHALL not send additional original notebook pages for OCR.
