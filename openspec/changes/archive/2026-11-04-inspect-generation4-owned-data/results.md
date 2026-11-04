# Precode checkpoint

Static source analysis and the proposed closed report3 contract are prepared.
Implementation, actual counter/CLI behavior, both-host/UI execution and product
qualification are absent. The central change remains active; it must not be
archived or merged as a completed planning-only feature. Independent contract and
literal-case review precedes implementation.

The initial arithmetic examples placed enormous values in referenced media,
contradicting the actual256MiB Media descriptor bound. Preserved draft definitions
were corrected to explicitly synthetic opaque-cache aggregates; the overflow
case now sums multiple file lengths rather than claiming one file overflowed.
Whole-string counter checks explicitly reject trailing LF/whitespace. Complete
report reference counters must all be zero. These are precode corrections, not
changed producer/consumer execution results.

Source basis: merged producer6fd4082/Docs2024b375 and immutable Managerb6ca2305
parser/types/controller/manual. Proposed behavior is not attributed to those
existing revisions. Byte provenance and literal definitions are recorded in
source-proof.json and vectors.json.
