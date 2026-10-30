## ADDED Requirements

### Requirement: Explicit host mode maintenance
The application SHALL expose one-shot initialize, inspect and choose operations over existing durable mode semantics without starting runtime, provider, service or native work. Only initialize SHALL allow normal owned Store creation/recovery. Inspect and choose SHALL require valid existing owned state and preserve Busy/unsupported/unavailable refusals without repair or service stopping.

#### Scenario: Existing selected state
- **WHEN** a valid selected Store is inspected or its mode is explicitly chosen
- **THEN** the supported maintenance path preserves selected records/media/history and uses existing validators; the legacy maintenance opener's selected-format refusal remains unchanged.

### Requirement: Original conditional intent and historical retry
Choose SHALL require the caller's original validated expected token and operation UUID, never substituting current state. Exact retry SHALL preserve the original receipt without changing later mode state; response SHALL separate original receipt from actual current snapshot and never label historical replay as current activation.

#### Scenario: Retry after a later choice
- **WHEN** an earlier original operation is retried after another mode is current
- **THEN** the original receipt remains historical, the current snapshot remains the later mode, and changed/stale/foreign requests refuse without implicit rebase.

### Requirement: Bounded guarded command output
Choose input SHALL be strict bounded JSON from an absolute regular file or exact-dash stdin, with an inclusive16KiB cap and caller-owned EOF/deadline/cancellation. Reports SHALL be one JSON line no larger than16KiB with sanitized truthful status and no activation claim. Store/current mode lifetimes SHALL remain held through the single consuming write; partial output SHALL NOT cause another report or mutation retry.

#### Scenario: Interrupted report
- **WHEN** a writer accepts a prefix and then fails
- **THEN** no second report is appended, any committed mutation remains uncertain until deliberate original-operation reconciliation, and held leases release after cleanup.

### Requirement: Ordinary startup respects chosen mode
Normal ordinary Reader startup SHALL admit only absent/LocalOnly mode with compatible legacy sync and nonselected data, using distinct ordinary-mode and legacy-data guards held through runtime lifetime. Unsupported mode/selected data SHALL refuse before model, device or domain runtime initialization; mode metadata SHALL NOT grant sync/provider/native authority.

#### Scenario: Shared choice precedes normal startup
- **WHEN** ordinary startup sees a shared/isolated mode or selected data
- **THEN** it refuses before model/device initialization and cannot silently continue as ordinary local history.

#### Scenario: Runtime owns ordinary lifetime
- **WHEN** an admitted ordinary runtime is alive
- **THEN** mode replacement/selected activation refuses until its mode and legacy-data guards are released, without using a snapshot-only permission check.
