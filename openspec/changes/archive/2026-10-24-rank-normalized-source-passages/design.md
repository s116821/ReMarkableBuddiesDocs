# Fixed corpus-aware lexical ranking

## Current mechanism and compatibility

Current actual Source4bdf34b uses a BTreeSet of lowercase alphanumeric terms for
each <=2048-byte chunk. Score is distinct query intersection count; source ordinal
breaks ties. Every query searches all chunks, then the existing result selector
admits direct candidates before immediate same-unit neighbors, with deduplication
and complete JSON count/byte limits. Keep that selector and all source validation.

Replace only per-chunk term sets with owned term-frequency maps plus token count,
and store an immutable corpus document-frequency map and searchable chunk count /
total token count on Index. A searchable chunk has at least one token; whitespace
or punctuation-only chunks do not affect corpus statistics or become direct
matches, but can still be requested neighbors. A term contributes once to corpus
frequency for each searchable chunk containing it. No extra source lookup occurs.

Keep the exact existing split on non-alphanumeric characters and str::to_lowercase
normalization. No stemming, stopword removal, synonym expansion or Unicode full
case folding is added. The crate-private terms() helper used elsewhere retains
its existing set behavior; internal token iteration may be shared without changing
that contract. Query duplicates remain one term, with existing 1..64 distinct and
2048-byte validation. A result requires positive exact normalized term overlap.

## Exact scoring contract

For each distinct query term t present in chunk d, compute in f64:

```
N = number of searchable chunks
df(t) = number of searchable chunks containing t
L(d) = token count of chunk d, including repetitions
avgL = total tokens / N
tf(t,d) = term occurrences in chunk d
k1 = 1.2; b = 0.75
idf(t) = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))
score(d) = sum_t idf(t) * tf(t,d) * (k1 + 1)
                         / (tf(t,d) + k1 * (1 - b + b * L(d) / avgL))
```

Sum in the existing sorted query-term order. Sort descending using f64::total_cmp,
then ascending immutable chunk ordinal for exactly equal scores. No score is
serialized or exposed as confidence. Zero searchable chunks yields ordinary empty
retrieval without division. All scored terms have 1<=df<=N<=8192, positive lengths
and frequencies; denominators are positive and scores finite. Integer counts use
checked additions during construction. Do not invent platform-independent bitwise
floating-point equivalence: ordering is deterministic for the same build/input;
near ties on different math implementations may differ. Exact-score ties retain
source order. Constants are fixed, not a new configuration or tuning surface.

## Bounds and durable compatibility

Existing limits remain:4MiB normalized source text,4096units,512KiB/unit,
8192chunks,2048bytes/chunk; queries64terms/2048bytes and results16passages/
16384complete JSON bytes. Token count cannot exceed original normalized text bytes;
statistics are derived from that admitted finite corpus. Per-query scoring visits
at most8192chunks*64queryterms and sorts at most8192positive candidates. Maps retain
bounded corpus terms; lowercasing/String/map allocation remains ordinary library
allocation, not a new hard process-memory/CPU/deadline promise. Already-allocated
input and existing serializer/refusal limits remain explicitly distinct.

IndexKey remains document/format/original digest/extractor/normalized digest:
ranking does not change source identity. DiskCache persists normalized units and
rebuilds Index, so no persisted index/statistics schema or cache migration changes.
Older captured request/passages remain unchanged historical data; a fresh query
may rank the same material differently after this software upgrade. Existing
retrieval Provider signature and receiving output validators remain unchanged.
Never mutate durable citation evidence or invalidate source keys to disguise a
ranking-policy change. No source/model/native currentness authority follows.

## Verification and review gates

Before code, independently review these exact artifacts and formula/bounds.
Author actual Index/Provider retrieval controls comparing old overlap order to
the new scorer on declared synthetic relevance cases: distinctive rare terms,
length normalization, repetition saturation and a multi-topic technical corpus.
State authored expectations as fixtures, not measured real-user effectiveness.
Verify exact ties/source order, repeated queries/query terms, Unicode lowercase,
punctuation-only material, all-identical/common terms and empty/no matches.
Exercise exact provenance/ranges, neighbors/deduplication, count/serialized-byte
limits including escaping and a higher-ranked passage that cannot fit, fresh
followups, wrong keys, unchanged key/disk-cache rebuilding, failed replacement and
actual frozen receiving context. Preserve all existing adapter/cache controls.
Check maximum admitted corpus/query bounds with useful assertions, not timing
benchmarks. No network/model/native simulator scenario is relevant to this pure
index ranking change; actual data fixtures cover its operation path.

Qualify exact successor with focused retrieval/receiving/disk/adapter integration,
full default library, strict all-target/all-feature Clippy, default library check,
format/diff, central strict/guidance and current hosted CI. Resolve findings and
retain initial/failing results separately. Then sync only the added requirement,
archive only this increment, obtain final paired review, guard normal Docs-first
delivery and separately observe actual main/new publication. No held integration
or whole-MVP acceptance is implied by this increment.
