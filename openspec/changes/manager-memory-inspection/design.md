# Selected-fact inspection consumer

## Evidence and ownership
Precode refers to producer Docs66 at8636fc4f02e0d0090cf919d4bf8d690a229c2cdd,
openspec/changes/inspect-memory-fact-over-stdin/contract.md. All five producer
precode artifacts were read. The new stdin implementation and actual corpus are
pending, so examples are illustrative. Current source Manager main isd4574f7;
Docs main is8c0ae5d. Public source/manual requirements and current project
coordination authorize a read-only consumer; existing search is not an inventory.

Main owns all Rust memory/Store/configuration work. This lane owns new consumer
parser/types, fixed Python transport, shared controller/view, observer/helper/
Electron bridges, focused controls and public manual guidance. Reuse the existing
checkouts and protected wired callbacks. Preserve existing search/saved-mode/
provider/personalization behavior, releases/dependencies/lockfiles/SDK and graph
fixtures. Only add focused commands within existing CI jobs if needed.

## Fixed transport
Use /opt/bin/reader-buddy --memory-operation inspect --memory-input - with the
existing fixed env-i HOME/PATH/absolute normal configuration. No caller command,
path or environment. The sole domain input is the exact selected global Key
{profile,scope:{kind:"global"},fact}; the configured profile remains authoritative.
Include opaque connection/boot identities in the host request, never operation,
expected-head or mutation fields. Host request cap1024 UTF8 bytes; raw CLI report
cap262144 bytes inclusive of newline; private child envelope cap278528; public
HTTP/IPC envelope cap270336. These smaller limits refuse the complete view, never
truncate it. Discard/cap stderr at16384. Require one UTF8 JSON report, reject raw
duplicate keys, malformed/trailing/partial/oversize output or nonzero exit.
Use existing2s channel I/O/8s collection/12s Python/13s Node/14s renderer deadlines,
EOF and cancellation. No temporary remote file or query fallback.

The protected Node host constructs a fresh reduced public report with the exact
status/incomplete and supported complete heads. Only ok/false/array is detail.
Non-ok or alternate shapes remain refused/unavailable without a successful array;
keep the actual incomplete flag rather than deriving it from status. Unsupported
versions, numeric ranges or raw schemas refuse the entire view. No raw-private
report acceptance is added to public IPC. HTTP/IPC and controller revalidate the
reduced public shape and request identity. Missing capability on older installed
builds reports unsupported/unavailable, never an empty successful fact.

## Identity and all heads
Parse only envelope-v1/subject-memory/domain-v1 with exact fields, nonnil UUIDs,
distinct revision IDs, distinct parents (<=4096, no self-parent), kind value or
tombstone, and empty media. Compute requested record UUIDv5 using standard host
crypto/Web Crypto SHA-1 primitives and URL namespace per producer contract;
construct the canonical Key in profile,scope,fact order and normalize UUIDs.
Validate EVERY record ID, including tombstones. Do not mistake fact UUID for record
UUID. Value payload Key must match selected profile/global scope/fact exactly.
Reuse exact Fact/provenance validation rules, with JS safe nonnegative integers
only and expiry strictly later than observation; reject wider u64s without rounding.
The canonical claim uses ASCII whitespace normalization/lowercasing and no control
characters, matching producer. Unsupported/opaque payload, media or one foreign
head refuses the whole report; filtering must never collapse conflicts.

The fresh public view preserves all supported heads' revision/parent/operation/
actor identities, kind and exact supported Fact or null tombstone. These are domain
metadata, not private selected pins or write tokens. Renderer displays head count,
conflict when more than one, each value/provenance and each tombstone, with identity
details expandable. No ordering, timestamp or confidence selects a winner. Empty
means no current heads for THIS key in the admitted view; it does not prove no
history, no orphan records or a globally empty store. Author-asserted provenance
never becomes verified source/native evidence.

## UI lifetime
Only an explicit action on a currently displayed search result selects its key.
Show prior search context separately from a new detail inspection, not as fresh
until successful. A new search, explicit tablet read, refresh, cancellation,
disconnect or any connection/boot/session/request generation change clears detail,
including repeated IDs; late completion cannot restore it. Pause ordinary polling
during the bounded operation using the same observation brackets as existing
capabilities. Selection/detail is never stored in settings/localStorage/logs and
never grants future edit/delete authority. Both browser and desktop use the same
controller with host-specific adapters.

## Verification and lifecycle
Check the producer's UUIDv5 example and independently generated Python uuid.uuid5
cases, exact all-head/tombstone/empty/refusal meanings, foreign IDs, malformed raw
and unsupported values, safe-number limits and late responses. Use an actual owned
SSH peer with public test keys and synthetic route/report fixtures, preserving the
real transport/channel/EOF checks. Consume attributed actual local/selected producer
stdin specimens when Main supplies them, including competing heads and tombstones;
do not relabel illustrated JSON or synthetic UI reports as producer evidence.
Exercise actual browser/Electron IPC guards and development plus retained production
packages in existing Linux/Windows integration. No local repackaging or replay of
unrelated physical qualification. Review source and central lifecycle, sync only
this capability and archive only completed own artifacts, merge the reviewed pair
normally after producer delivery, and observe actual-main/publication separately.
