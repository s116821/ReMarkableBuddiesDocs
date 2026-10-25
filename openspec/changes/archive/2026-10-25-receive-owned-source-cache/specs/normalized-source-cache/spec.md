## ADDED Requirements

### Requirement: Owned cache directly supplies exact-key retrieval
An already-open owned DiskCache SHALL implement the existing retrieval Provider
by loading and validating the caller's independently supplied complete IndexKey on
each query and querying that rebuilt immutable Index with unchanged arguments,
ranking, provenance, neighbors and encoded-result budgets. An absent slot SHALL
refuse rather than becoming empty or no-document success. This integration SHALL
NOT select or infer source identity, acquire inputs, mutate cache contents,
implicitly open a cache, change durable schemas or establish native/runtime
authority, independent freshness or a cache-currentness lease.

#### Scenario: Reopened cache supplies ordinary receiving
- **WHEN** ordinary declared receiving uses an already-open reopened cache Provider and the independently retained exact original key
- **THEN** the request receives exact source-bound passages through the existing receiving path, later questions reload and search the whole applicable index anew, and existing complete frame limits still apply.

#### Scenario: Missing, changed or corrupt material
- **WHEN** the selected slot is missing, stale, corrupt or mismatched, or query/result admission fails
- **THEN** the call refuses without fallback, partial source-less success or cache writes; valid exact-key material with no lexical matches still returns an honest source-bound empty result.

#### Scenario: Independent query snapshots
- **WHEN** cache material changes after one query's validated Index is rebuilt
- **THEN** that immutable observation is not rewritten, a later query validates its supplied key again, and neither observation implies the cache remained unchanged or changes existing durable receiving publication admission.
