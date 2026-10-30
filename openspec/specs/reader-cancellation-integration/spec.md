# Reader cancellation integration

## Purpose

Describe the bounded host Reader integration of the accepted cooperative provider cancellation lifecycle. This contract does not establish native cancellation/readiness, real-provider semantics, remote billing or export rollback. The current delivery is the actual ordinary Reader regression control over the already-delivered async transport and personalization path. Selected Reader/Attempt composition remains in its independent unfinished stack.

## Requirements

### Requirement: Reader ownership loss cancels provider wait
The actual Reader SHALL use the accepted cooperative async provider cancellation lifecycle. When its existing request guard rejects an in-flight operation, the provider wait SHALL return after owned worker cancellation/join while a witnessed server response remains withheld, without publishing a preliminary or late answer. Source traceability: REM-40 cancellation acceptance and accepted Buddy PR43.

#### Scenario: Ownership loss during recognition
- **WHEN** an actual recognition HTTP request has been received and its response remains withheld, and the modeled request guard loses page/session ownership
- **THEN** the Reader records a canceled durable attempt, returns without awaiting the withheld reply, preserves source evidence and performs no page navigation or text output

#### Scenario: Ownership loss after verified interpretation
- **WHEN** recognition and independent transcription succeed but ownership is lost while a contextual answer HTTP response remains withheld
- **THEN** the exact interpreted question remains durable, cancellation is recorded and neither the preliminary answer nor the withheld answer is published or causes another provider request
