# Local subject-memory design

The next selected receiving phase is specified in
[selected membership](selected-membership.md). Its exact identity, cumulative
read-budget and consuming-admission candidates require focused review before
implementation; the completed local phase below remains the default.

## Records, identity and persistence

Use Namespace::SubjectMemory with domain schema 1, existing immutable envelopes,
CAS parents, revisions/operation/actor identities and tombstones. A portable
profile UUID identifies the user independently of a device actor. Each fact has
an independent stable logical key; global user/subject scope and stable native
document UUID scope are explicit. A document conflict cannot erase other facts.
Keys and selected membership must agree with REM-52 before cross-device writes.

REM-52 owner handoff was read in full (REM-24 comments
`4bb49e47-f92e-489a-8d40-0ea128934e79` and
`b6c934b0-4cc6-47f8-af5a-37e3a22830c8`). Its accepted generic baseline is
Buddy `423cb0b227856d3aa1fcc3e1e0b66865622e4fb7` / Docs
`c9f3ce718ec638913567f4fb16ece118bc1d5288`, paired PRs 31/7. Those successors
are not assumed to be present in this change's REM-37 parent base. Local key
compatibility is a reasoned assessment, not shared wire-schema acceptance.

Before shared publication, the domain must freeze aggregate/catalog membership:
document-associated facts participate in the source-document conflict aggregate;
independent global logical facts have independent chains. Local per-fact CAS does
not imply separate remote fact slots within one document aggregate. Use exact
original references and selected/retained closures, exclusive aggregate ownership,
accepted base and live Store-created selection tokens; applying one winner must
preserve unrelated scopes. A fixed-ID Drive slot does not establish membership or
native authority. Catalog/OAuth, shared runtime and selected restore activation
remain open. This local delivery publishes no shared memory wire state.

The immutable logical identity is `(profile UUID, Global | Document(document UUID),
fact UUID)`. Its record UUID is UUIDv5 over canonical serialized identity using a
versioned application namespace. The caller supplies the stable fact UUID;
creating another UUID does not silently replace an existing claim. Claim keys are
also immutable on update. Canonical claim keys trim/collapse ASCII whitespace and
fold ASCII case; Unicode bytes otherwise remain unchanged. Subject/tags/value may
change only through explicit CAS updates. Moving a fact requires explicit forget
and independent creation, never changing identity through update.

Exact local recipe: serialize `Key` as compact UTF-8 JSON in the field order
`profile`, `scope`, `fact`. UUIDs use canonical lowercase hyphenated strings;
scope is `{"kind":"global"}` or `{"kind":"document","document":"UUID"}`.
Prefix those bytes with `urn:remarkable-buddies:subject-memory:v1:` and apply
UUIDv5 under `Uuid::NAMESPACE_URL`. Revision identity uses UUIDv5 under the
operation UUID with `remarkable-buddies:subject-memory:revision:v1` bytes.
The recipe does not use titles, provider IDs, actor/device identity or timestamps.

Typed payloads contain a bounded claim key, value, subject/tags, scope, provenance,
observed timestamp, optional expiry and confidence in integer basis points with
an explicit basis. Confidence is a declared assessment, not calibrated model
probability. Source/turn references are explicit optional UUID links; memory never
promotes a canceled answer or uncertain transcription into a confirmed fact.
No automatic learning or source-media copying is part of the local API.

Freeze initial UTF-8 bounds: claim key and subject 128 bytes each, value 4096 bytes,
up to 16 tags of 64 bytes each, and provenance description 512 bytes. Query text
is at most 2048 bytes, at most 16 matches and at most 16384 encoded context bytes.
The current-head scan shares Store MAX_ITEMS (4096) and MAX_METADATA (8 MiB);
oversized snapshots are explicit unavailable results, not truncated zero-memory
success. Confidence is 0..10000 basis points; timestamps are nonnegative Unix
milliseconds and expiry, when supplied, must follow observation. Nil profile,
document, fact, operation or explicit source/turn references are invalid.

Store/update requires explicit expected heads and stable operation identity.
Forget publishes a tombstone through the same engine; it does not promise physical
erasure of immutable backups. Inspection can expose exact revisions/provenance to
an explicitly requesting caller. Routine logs omit saved values. Unsupported
payload/schema, malformed references, unavailable inputs and concurrent heads
remain explicit rather than selecting an arbitrary timestamp winner.

Revision identity is deterministically derived from the supplied operation UUID.
An exact operation/envelope retry is recognized before a stale CAS check, through
the existing Store operation identity. Reusing an operation with a changed payload,
key, parent set or intended deletion refuses. Forget requires explicit expected
heads; a tombstoned key cannot be recreated with empty parents. Reinstatement, if
requested, requires explicit tombstone parents and a distinct operation; it never
revives an ancestor. Read-before-write validation checks immutable identity/claim,
and the Store's atomic parent comparison closes the write race.

## Query and context

Read one bounded current-head snapshot using existing Store APIs; never retrieve
ancestors or retained losers as current facts. Selected-sync consumers must use
their accepted membership and fail explicitly on absent/stale selection rather
than falling back to ordinary all-history heads. Local-only mode is explicitly
separate. Disabled memory returns no data and performs no memory read/write or
network call.

The local adapter holds the existing Store legacy-mode lease: construction refuses
any already-selected storage, and the lease blocks selected publication while
the adapter lives. Turning a sync flag off does not convert selected/retained
history into a local current-head view. An unavailable recovered transaction makes
query unavailable and inspection/mutation refuse; never resurrect an earlier
value after a damaged correction or tombstone. Reuse existing Store diagnostics
and admission rather than creating another recovery engine.

Query is profile/scope restricted with bounded UTF-8 input, count and encoded
context-byte budgets. Rebuild lexical ranking from current records; no additional
database or persisted index is needed initially. Use claim/value/subject/tag token
overlap, reject irrelevant matches and expired facts, and omit contradictory
values for the same applicable claim. Current explicit/canonical facts suppress
stored claims with the same key. Diagnostics distinguish conflict, unsupported,
expired and incomplete input; no unlimited history dump or silent truncation.

Applicable claims include global facts plus facts for an explicitly supplied
document, never another document or profile. No known document means global facts
only. Concurrent value/value or value/tombstone heads invalidate that logical key.
Across independent keys, different values for the same canonical claim invalidate
the whole applicable claim, even across global/document scope; confidence or time
cannot resolve it. Same-value duplicate claims coalesce deterministically without
adding confidence. Rank positive token overlap, then declared confidence, then
record UUID bytes as a stable tie-break. Source evidence remains independent.

Current/canonical suppression uses a caller-supplied typed list of at most 64
canonical claim keys (128 bytes each). Arbitrary query or source text is never
parsed into trusted suppression claims. Query uses an explicit caller timestamp;
expiry equal to that timestamp is expired. Return structured status and counts:
CompleteEmpty, Complete, Partial (including withheld conflicts or budget omissions),
Unavailable or Disabled. Count/byte caps produce explicit omission counts. The
budget covers exact serialized context including labels, provenance and JSON
escaping; never emit half a fact or call truncation complete-empty. Oversized
global head/metadata snapshots are unavailable rather than partial unbounded scans.

The receiving-buddy interface exposes memory as labeled associative data with
provenance/confidence. Current request and document evidence remain distinct and
outrank memory. Memory text grants no tool, erase, export, binding or module
authority. Do not insert fabricated visible conversation turns or rewrite history.

Existing Reader first proposes question/answer, then independently verifies the
question. Keep recognition/verification free of associative memory. When enabled
and relevant memory exists, perform a bounded answer enrichment call only after
successful verification, preserving exact recognized question and original source
images. Disabled/empty retrieval preserves the existing two-call path. Failed
enrichment cannot silently publish a memory-enriched success. Provider fixtures
verify actual request assembly; they do not prove model obedience or recognition.
Writer receives the same optional interface when its real integration exists.

Reader policy: complete-empty/disabled uses the existing answer path; partial with
valid nonconflicting relevant facts may enrich while retaining diagnostics.
Unavailable/unsupported retrieval does not become empty success: fail the optional
memory-enrichment attempt with an explicit non-output failure. Enrichment provider
failure, timeout, malformed/empty/abstaining answer or cancellation similarly
prevents output; do not publish the earlier proposal as enriched success. Check
request progress before/after retrieval and throughout the extra provider call.
The exact verified question and captured source images remain unchanged. Routine
logs do not dump memory context or full enriched answers. Provenance links are
explicit caller assertions until separately resolved against the typed source/
turn records; a UUID alone proves neither ownership nor successful completion.

## Acceptance and boundaries

Use real temporary Stores, restart/CAS/conflict/tombstone and namespace/scope
isolation tests. Exercise the actual receiving Reader and HTTP provider boundary
with disabled/enabled/irrelevant/conflicting/expired memory. Preserve source and
transcript bytes, fail on invalid budgets, and make local/protocol/live-provider/
native evidence distinct. Default operation does not require a cloud provider.

Generic export/restore/sync stays REM-36/REM-52-owned; verify domain payloads through
those existing interfaces rather than implement a second engine. Schema migration,
two-device selected membership/deletion, clean-device restore, Manager UI, Writer
and live/native effectiveness remain open until their real gates are verified.
This change must not be canonically synced or archived as complete prematurely.
