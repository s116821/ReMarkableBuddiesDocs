# Private Reader diagnostics

## Purpose

Keep full Reader content and arbitrary provider response strings out of the bounded routine diagnostic paths while preserving exact user output and intentional private evidence. This is a stacked candidate contract, not an exhaustive audit of every third-party/error log or native/live-provider qualification.

## Requirements

### Requirement: Content-free routine Reader diagnostics
Routine provider-response, Reader interpretation and render-text diagnostics SHALL omit full response bodies, arbitrary provider metadata and user question/transcription/answer/rendered text, including under the application's existing default Debug policy. Useful stages, lengths and recognized unsigned token counters MAY be logged. Exact requests, answers and intentional persisted evidence SHALL remain unchanged. Source traceability: REM-53 user-text logging requirement and actual Reader/provider/default logger source.

#### Scenario: Default logging with content-bearing replies
- **WHEN** an actual CLI Reader run receives synthetic replies containing distinct question, answer and arbitrary provider-metadata canaries under the default log configuration
- **THEN** stdout and stderr omit those canaries while the output report and answer preserve the exact intended question and answer

#### Scenario: Invalid usage metadata
- **WHEN** recognized usage fields contain strings, objects or unsupported values
- **THEN** diagnostics treat those counters as absent without formatting the arbitrary metadata, and normal response parsing/output remains unchanged
