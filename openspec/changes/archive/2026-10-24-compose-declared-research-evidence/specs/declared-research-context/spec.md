## ADDED Requirements

### Requirement: Explicit default-required research decision
Ordinary frozen source/memory composition SHALL support a transient research stage
whose default policy requires a Provider attempt and whose explicit no-internet
directive dominates that policy. Configured-disabled and request-no-internet
outcomes SHALL remain separately labeled with zero Provider calls. Required
provider absence/error/unavailability SHALL refuse rather than become offline or
empty success. The stage SHALL preserve exact prior request/history/context and
SHALL NOT imply installed policy resolution, performed network research, model
dispatch, durable evidence publication or native authority.

#### Scenario: Required research and explicit opt-out
- **WHEN** default-required research is composed, a provider is absent/unavailable, or an explicit no-internet/configured-disabled choice applies
- **THEN** Required makes at most one admitted Provider attempt or refuses honestly, NoInternet takes precedence with zero calls, and both disabled reasons remain distinct without fabricated query/evidence

#### Scenario: Complete immutable input
- **WHEN** a synthetic Provider receives a valid research request or reenters mutable local data
- **THEN** it receives the entire exact frozen context with a bound context digest/conversation/request/time, no request/history truncation or summary replaces that input and the retained prior context bytes remain unchanged

### Requirement: Bounded untrusted research evidence
The stage SHALL admit only identity-matching bounded query/citation data with
explicit synthetic/provider-asserted unverified provenance and distinct complete,
complete-empty and partial outcomes. Contradictory, unavailable, malformed,
duplicate or oversized results SHALL refuse without partial text or silent
fallback. Complete encoded evidence and wrapper/token limits SHALL include labels,
identity and escaping, with one final caller count and no token-monotonicity
assumption. The result SHALL remain historical data, separate from source truth,
currentness, configuration, runtime or effect admission.

#### Scenario: Honest evidence outcomes and correlation
- **WHEN** complete-empty, complete, partial, unavailable or foreign/invalid evidence is returned
- **THEN** admissible outcomes retain their exact queries/citations/basis and diagnostics, unavailable and invalid data refuse, and no synthetic or author-asserted observation is promoted into verified live research

#### Scenario: Exact complete-output limits
- **WHEN** escaped evidence, an oversized prior context or a failing/nonmonotonic token counter meets configured limits
- **THEN** byte preflight can prevent a Provider call, final limits cover the entire output, the counter runs once only on the final encoding and exhaustion/error refuses without rewriting or dropping prior context or research
