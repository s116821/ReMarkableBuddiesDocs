## ADDED Requirements

### Requirement: Witnessed inclusive application response bound
The existing application client SHALL accept a valid answer at its10MiB response bound and refuse declared or streamed bodies exceeding that bound. Qualification SHALL use the actual unchanged client, isolated owned TLS resources and exact child/request/response witnesses; only the existing static bound error SHALL count as size refusal.

#### Scenario: Inclusive exact-size answer
- **WHEN** a trusted owned origin sends valid answer JSON padded with whitespace to exactly10MiB
- **THEN** the actual client returns the exact synthetic answer and all owned resources are reaped and removed.

#### Scenario: Oversized declared or streamed response
- **WHEN** the owned origin declares10MiB+1 without sending a body or streams10MiB+1 with unknown Content-Length
- **THEN** the client refuses with the exact existing static bound classification, the server witnesses closure, no parse/timeout/network error is called a size pass and the declared-length case sends zero body bytes.
