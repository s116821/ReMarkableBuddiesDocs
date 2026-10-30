## ADDED Requirements

### Requirement: Explicit shared verified Manager bundle download
Both distributions SHALL explicitly download a selected stable Manager tag through the existing fixed canonical consumer, preserving actual publication/digest/embedded identity qualification. Caller input SHALL contain only a bounded stable tag; host setup owns trusted interpreter and destination parent.

#### Scenario: Completed verified download
- **WHEN** the configured host completes an explicitly selected download and the existing consumer returns a valid successful receipt
- **THEN** the shared UI reports the downloaded tag/source and host-chosen folder, with update eligibility false and no extraction, payload execution or tablet action.

#### Scenario: Unconfigured or invalid caller
- **WHEN** host setup, origin/session/frame or request shape is invalid
- **THEN** no download starts and arbitrary caller paths/URLs/interpreters never reach the consumer.

### Requirement: Bounded owned download lifecycle
The host SHALL own at most one active attempt, expose bounded sanitized status and explicit cancellation, and preserve consumer receipt commit semantics without deleting partial or user-owned files.

#### Scenario: Cancel or concurrent start
- **WHEN** another start is attempted during active work or cancellation occurs before successful receipt issuance
- **THEN** no competing download starts, cancellation targets the owned attempt, and the UI never claims completed verification without its actual receipt.

#### Scenario: Late cancellation or malformed host response
- **WHEN** cancellation races an already committed successful receipt or a response is malformed/stale/unavailable
- **THEN** committed success is not silently undone and malformed/stale responses do not become current verified downloads.
