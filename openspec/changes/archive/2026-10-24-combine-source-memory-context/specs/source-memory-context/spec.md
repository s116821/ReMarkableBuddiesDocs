## ADDED Requirements

### Requirement: Optional historical memory preserves the frozen source request
The ordinary receiving library SHALL combine an existing frozen source request
with optional separately labeled associative memory without rewriting its request,
history, source, passages or original encoded frame. Enabled query text and
document scope SHALL derive only from that captured frame; profile, time, canonical
current-claim assertions and limits SHALL be explicit. Disabled SHALL make no
memory query. The combined data SHALL NOT write records, repeat source retrieval,
invoke a model or confer selected/native/publication authority.

#### Scenario: Document scope and disabled memory
- **WHEN** a source-bound or explicit no-document frame receives optional memory
- **THEN** enabled queries preserve the exact request and use only its captured document or global scope, while disabled performs zero queries and keeps the original frame byte-identical.

#### Scenario: Source or memory changes during callbacks
- **WHEN** query/count callbacks change underlying records after source capture
- **THEN** the original frame remains unchanged and the combined result is labeled historical, without claiming an atomic snapshot or currentness lease.

### Requirement: Complete combined context has bounded and honest memory outcomes
The receiver SHALL validate enabled ordinary memory results against explicit
profile/scope/query bounds, identity, expiry, suppression, status and data labels;
preserve valid empty/partial diagnostics; and refuse unavailable, malformed or
selected results without empty fallback. It SHALL preflight minimum complete
encoded-byte lower-bound output before querying and cap/count complete final
encoding including both layers, query identity and diagnostics. Token admission
SHALL count the actual complete encoding only, without assuming monotonicity,
summing component counts or rejecting based on a placeholder count. Failures SHALL be sanitized and SHALL NOT
return truncated data, repeat a query or invent verified provenance.

#### Scenario: Conflicting, expired and unavailable memory
- **WHEN** the memory provider withholds conflicting/expired facts or returns unavailable, inconsistent or foreign data
- **THEN** valid empty/partial observations retain diagnostics, while unusable data refuses with no partial successful frame.

#### Scenario: Complete output budget
- **WHEN** the proven minimum encoded bytes or actual complete combined JSON/token count exceeds explicit known limits or final counting fails
- **THEN** assembly refuses at that boundary without rewriting source/history, dropping facts to hide exhaustion or returning empty success.
