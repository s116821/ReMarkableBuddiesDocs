# Answering frozen researched context

## Purpose
Consume complete historical source, memory and research context through an explicitly
selected answering engine while preserving original request/history and unverified
provenance. The complete [versioned answering design](../../changes/archive/2026-10-25-answer-researched-context/design.md)
defines prompt/output bounds, engine-content ownership, progress limits, strict
citation grammar and separate local/hosted qualification. This does not activate
the installed workflow or grant selected/native authority.

## Requirements

### Requirement: Explicit frozen-context answering preserves original input
The receiving buddy SHALL provide an explicitly invoked answering boundary using
the existing frozen source/memory/research context and caller-selected engine.
Stable instructions and the complete exact frozen JSON SHALL be separate text
parts without rewriting request/history, reacquiring evidence or implying separate
system roles. Complete declared input bounds and one whole-descriptor counter
SHALL precede one engine invocation, with no added retry/fallback or native/runtime
activation.

#### Scenario: Actual context consumer and complete prompt budget
- **WHEN** an admitted frozen request reaches the maintained caller
- **THEN** the actual selected engine receives stable instructions and byte-exact original context as two separate text parts, including all prior provenance, while byte/count/refusal failures invoke no model and never trim history.

#### Scenario: Source-free and policy opt-out answers
- **WHEN** an explicit no-source or disabled/no-internet researched frame is answered
- **THEN** its original labels remain unchanged, no new retrieval/memory/research/device call occurs, and absent evidence cannot acquire invented citation authority.

### Requirement: Temporary engine content and honest cooperative admission
The boundary SHALL own exclusive temporary engine content, clear prior text/images
at entry and clear again on success/refusal/error/unwind under the engine cleanup
contract. It SHALL latch progress failures, refuse late success and state the
selected engine's actual progress/transport limits without claiming generic hard
preemption, worker ownership or remote rollback.

#### Scenario: Engine reuse and failed attempts
- **WHEN** an engine has prior text/images or counting, execution, progress or output admission fails or panics
- **THEN** no later ordinary reuse inherits that prompt, no failed attempt returns a draft and cleanup follows the documented engine contract without changing stored conversation history.

#### Scenario: Existing-engine HTTP cancellation
- **WHEN** actual existing-engine HTTP is canceled after exact request/partial-write witnesses while response completion is withheld
- **THEN** no draft escapes, its actual transport/server cleanup is joined and measured local return is attributed to that engine rather than an arbitrary default progress implementation.

### Requirement: Bounded generated answers retain captured citation provenance
The boundary SHALL admit only bounded strict answered/clarification output with
known unique captured citation IDs and matching inline markers. It SHALL resolve
metadata only from captured source/memory/research arrays, preserve historical and
unverified provenance and refuse malformed/unknown/oversized output without
second-call repair. Structural admission SHALL NOT imply semantic truth, complete
fact attribution, currentness, durable publication or native authority.

#### Scenario: Disagreement and useful references
- **WHEN** the separately qualified actual model answers an authored source/memory/research discrepancy
- **THEN** the retained output demonstrates the checked expected facts and captured references for that invocation, with original unverified labels and exact context/history preserved.

#### Scenario: Strict output and citation refusal
- **WHEN** output is malformed, duplicated, oversized, uses unknown IDs or has mismatched markers
- **THEN** the call refuses with sanitized failure, no partial draft, invented URL/locator metadata or automatic retry, and later engine reuse starts empty.
