## ADDED Requirements

### Requirement: Shared bounded global subject-memory query
Both browser and Electron Manager SHALL offer the same explicit global subject-memory search through the existing hard-wired host adapters and Main's qualified fixed one-shot query command. The backend SHALL choose its configured profile; the consumer SHALL preserve supported query/context limits, original fact identity and asserted provenance without a second store, arbitrary remote paths, a Buddy service API or domain mutation.

#### Scenario: Supported query returns bounded facts
- **WHEN** an identity-verified wired target supports the published stdin query contract and completes a valid explicit global search
- **THEN** both Manager distributions show only the bounded returned facts and diagnostics with original provenance and honest completeness, without implying exhaustive inventory or native authority.

### Requirement: Honest refusal and session-bound results
The consumer SHALL preserve disabled, empty, partial, busy, unavailable and unsupported distinctions; reject malformed/oversized/unknown reports; suppress private diagnostics; and invalidate pending/visible results after query replacement, cancellation or connection/boot change. Query-only semantics SHALL NOT be represented as a guarantee that normal backend Store recovery performs no writes.

#### Scenario: Unsupported or incomplete query
- **WHEN** the installed command is older/unsupported, memory is disabled, Store admission is busy, the result is partial/unavailable, or transport/report validation refuses
- **THEN** the Manager shows that specific supported state without fabricated empty success, service control, remote request staging or a mutation retry.

#### Scenario: Query loses its session
- **WHEN** a query is canceled/replaced or its wired connection/boot identity changes before completion
- **THEN** old facts are cleared and late completion cannot repopulate the current view or authorize another operation.
