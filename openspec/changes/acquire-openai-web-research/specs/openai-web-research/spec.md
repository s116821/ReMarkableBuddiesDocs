## ADDED Requirements

### Requirement: Explicit bounded concrete web research provider
The backend SHALL provide an independently selected OpenAI Responses web-search
Provider using existing frozen research input/result interfaces. It SHALL transmit
the complete exact captured context with explicit finite one-attempt tool/output/
request/response/time controls, caller-supplied credentials/model/endpoint and no
implicit fallback, retry, settings mutation or answering/runtime substitution.

#### Scenario: Admitted required research
- **WHEN** an admitted Required request reaches a compatible explicitly selected backend
- **THEN** one bounded POST carries the exact original context and requires web search, while Disabled/NoInternet through existing composition make no provider/network call.

#### Scenario: Unsupported selection or transport
- **WHEN** selection/capability/HTTP/redirect/deadline/size admission fails
- **THEN** the attempt refuses with sanitized failure without endpoint retargeting, credential disclosure, retry or offline/empty success.

### Requirement: Actual search witnesses and unverified correlated evidence
Successful acquisition SHALL require completed hosted search action/query and
consulted-source-URL witnesses plus strict per-source structured output correlated
to those URLs. It SHALL preserve request identity and original evidence strings,
reuse all existing complete evidence/wrapper bounds, and distinguish provider-
asserted source-attributed summaries from fetched quotations or verified truth.

#### Scenario: Complete nonempty or empty search
- **WHEN** completed actual search yields a valid bounded selected source set or no selected evidence
- **THEN** the provider returns distinct Complete/CompleteEmpty with actual reported queries and ProviderAsserted provenance, without inventing source dates, search terms or verified-source authority.

#### Scenario: Missing witnesses or invalid evidence
- **WHEN** search/query/source witnesses are absent, schema/URL association is invalid or the response is incomplete/refused/oversized
- **THEN** composition refuses without replacing missing queries, dropping invalid evidence, guessing citation index units or returning aggregate answer text as source quotations.

### Requirement: Owned cooperative transport cancellation and distinct qualification
The synchronous adapter SHALL retain one owned cancellable async request with
joined cleanup on every exit, progress before dispatch/during response waits/before
return and a finite monotonic deadline. Local and bounded hosted qualification
SHALL remain separately attributed and SHALL NOT imply native/runtime readiness.

#### Scenario: Witnessed withheld-response cancellation
- **WHEN** the exact request is received and its progress callback cancels while headers/body are withheld
- **THEN** local return is independent of that response, owned resources are joined and late completion cannot publish successful evidence or imply remote rollback.

#### Scenario: Real acquisition and unchanged context
- **WHEN** the actual configured hosted adapter is qualified with a public authored saved-context fixture
- **THEN** retained search/query/source/schema evidence establishes only that bounded provider invocation, exact original request/history remains unchanged and later installed runtime/native acceptance stays separate.
