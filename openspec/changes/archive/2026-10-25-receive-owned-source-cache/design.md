## Context

The current DiskCache holds its existing Store and namespace lease. load(expected)
serializes local operations, checks owned slots, validates a bounded entry and
rebuilds Index before returning it. Existing receiving takes a retrieval Provider.
The independently obtained key remains required; cache content cannot select it.

## Decision

Implement retrieval::Provider for DiskCache with the exact existing query
signature. Call load(expected) once; convert None to a fixed source-unavailable
error; call Index::query with the unchanged key, question, passage/byte budgets and
neighbors flag. Do not select another slot, infer a key, return empty for missing
material, install/forget anything or retain a process cache.

load's operation guard ends before Index::query. A concurrent install/forget after
the snapshot may change the cache but cannot alter the already rebuilt Index.
The result is an immutable observation of validated cached material, not a lease
over current cache state or independently verified source freshness. Every later
query reloads independently. Existing durable receiving publication admission is
unchanged and does not gain a disk-cache currentness guarantee.

Existing load, install and forget behavior stays intact. Query errors remain the
existing Index errors. There is no new retry, fallback, partial result or public
serialization/schema. DiskCache::open still has its documented initialization and
staging cleanup behavior; the Provider implementation does not open it implicitly.

## Verification

Use actual temporary owned Store/DiskCache and declared receiving. Reopen the
cache, supply an independently retained original key and query distinct pages on
successive user requests. Replace material: the old key refuses and a fresh key
queries changed text. Missing/corrupt material must refuse; valid unmatched text
returns a bound empty result. Compare direct Index and cache Provider results for
complete encoded budgets, neighbors and exact provenance, including refusal.
Check query leaves existing cache file bytes unchanged. Explicit no-document must
still perform no cache query; do not open the cache as an incidental fallback.
Retain all old cache/receiving fixtures. No artificial native simulator model,
tablet call or live provider is required for this local data seam.

## Limits

Rebuilding for each query has existing bounded work but is not a latency/CPU/RAM
guarantee. Loading cached data does not prove original bytes or native identity.
Automatic runtime consumption and live-model qualification are separate work.
