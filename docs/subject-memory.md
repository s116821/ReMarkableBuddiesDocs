# Optional local subject memory

The local memory domain stores explicit associative facts in the existing
SubjectMemory namespace. It supports store/update, bounded query, exact current
inspection and forgetting through `memory::Provider`, with `LocalMemory` as the
offline implementation. It does not automatically learn from answers, failed
transcriptions, cancellation or model guesses.

The implementation belongs to the active
[subject-memory change](../openspec/changes/subject-memory). Full Writer and
Manager integration, selected cross-device sync/recovery, live-model effectiveness
and native acceptance remain open.

## Optional configuration

Existing configurations default to disabled memory. An explicit portable profile
UUID is required to enable it; this identity is independent of a device actor:

```json
{
  "memory": {
    "enabled": true,
    "profile": "bfcf4324-d157-4d7f-b2fd-08f0fb60d73c"
  }
}
```

This is a fragment of the ordinary configuration, not a complete replacement.
Keep the chosen profile stable across the intended user scope. Configuration is
read at application startup; no live reload is claimed by this increment. Disable
memory without deleting stored records by setting `enabled` to false.

## One-shot offline maintenance

The existing Reader binary also supports explicit file-input operations:

```text
reader-buddy --memory-operation inspect --memory-input /absolute/path/key.json
reader-buddy --memory-operation query --memory-input /absolute/path/query.json
reader-buddy --memory-operation put --memory-input /absolute/path/mutation.json
reader-buddy --memory-operation forget --memory-input /absolute/path/forget.json
```

Select an existing configuration explicitly with `REMARKABLE_BUDDIES_CONFIG`.
It must contain the portable profile; the response-enrichment enabled flag may
remain false. Each JSON input uses the corresponding typed API structure described
below. The command reads at most 1 MiB from a safe regular input file, rejects
unknown/invalid fields and mismatched profiles, and routes before `.env`, provider,
logging, sync or device initialization. Provider/runtime flags conflict with it.

Only a valid creation put with empty expected parents may initialize absent/empty
owned storage. Reads, forgetting and updates cannot initialize missing state or
repair a partly owned nonempty root. Existing Store opening can still perform its
normal known metadata/recovery/staging cleanup under the lease; these are not the
nonmutating inventory commands. A busy Store returns a fixed busy report instead
of stopping/retrying a service or reading without a lease. Self-parent and other
invalid requests fail before startup writes.

The single compact JSON response has `report_version: 1`, operation, status,
incomplete indication and bounded data. Exit zero means a report was emitted;
check its status. `ok`, `partial`, `busy`, `unavailable`, `unsupported`, `conflict`
and `invalid-input` remain distinct. Conflicts return the complete bounded current
revision set for an explicit refresh; there is no automatic rebase. Total response
bytes, including the final newline, are capped at 8 MiB + 64 KiB. An over-limit
result returns unavailable/incomplete without partial refresh data.

Inspect/query deliberately print saved values on stdout to the requesting caller.
Failure reports do not echo request values, private parser data or filenames, and
routine logs do not receive those values. See the detailed
[maintenance contract](../openspec/changes/subject-memory/maintenance-cli.md)
for exact input/output limits and verified scope.

The local adapter conservatively refuses any Store with selected storage, even
if sync is now switched off. It holds the existing legacy-mode lease, preventing
selected publication while it lives. Active SubjectMemory sync plus enabled
local memory is refused. REM-52 must supply a qualified accepted-membership
adapter; no ordinary-head fallback or sync qualification follows from this API.

## Records and operations

`Key` identifies a portable profile, explicit global/document scope and independent
fact UUID. Document scope uses a stable document UUID; it does not grant document
access or native authority. Record IDs are deterministic UUIDv5 identities. Claim
keys normalize ASCII whitespace/case, preserve other Unicode bytes and remain
immutable with the logical key. Value, subject, tags, expiry and provenance change
only through explicit expected-head updates.

`Mutation` supplies the operation UUID, expected revision set and typed `Fact`.
`Forget` supplies an operation, expected revisions and key. Exact operation retries
are idempotent; changed intent reusing an operation refuses. Forgetting creates a
tombstone, retaining historical immutable evidence. It does not erase every backup.
Reinstatement requires explicit current tombstone parents and a new operation.

Provenance distinguishes user-confirmed assertions, source assertions and inferred
associations. Description and optional source/turn links are author assertions;
UUID presence is not proof of source ownership, native evidence or completion.
Confidence is an integer declared assessment in 0..10000 basis points, not a
calibrated probability. Multiline Unicode values are preserved.

Store-backed API callers explicitly open the normal Store under its existing
ownership/lease rules. Normal initialization may create or recover Store metadata;
this API is not the nonmutating inventory command. Explicit `inspect` uses the
already-open Store's bounded current-head snapshot and can return conflicts and
tombstones. No listener, account setup, second database or network operation is
needed for the memory operations themselves.

## Retrieval and Reader behavior

`Query` supplies exact query text, an optional explicit document, caller time,
bounded typed canonical-current claim keys, match count and encoded context budget.
No document supplied means global facts only. Current explicit/canonical keys suppress
matching stored claims; raw page/query text is never promoted into trusted keys.
Initial ranking uses lexical token overlap, declared confidence and stable UUID
ties. It does not claim semantic-embedding or handwriting-recognition effectiveness.

Expired facts are excluded at the expiry boundary. Conflicting current keys and
contradictory applicable claims are withheld, including same-claim duplicates of
conflicted keys. Same-value duplicates select the best existing relevant
representative without combining confidence. No retained ancestor fills a missing
or forgotten fact. Unavailable recovered commits cause retrieval to be unavailable
and mutation/inspection to refuse rather than resurrect an old value.

Results distinguish disabled, complete-empty, complete, partial and unavailable.
Count/byte omissions and conflicts remain explicit diagnostics. The scan shares
4096-head/8 MiB metadata limits. Up to 16 matches and 16384 exact encoded context
bytes are supported, including labels, provenance and JSON escaping. No half-fact
truncation or hidden empty success occurs at a limit.

Actual Reader recognition and independent transcription verification receive no
memory. After successful verification, the unchanged question is persisted; enabled
relevant global memory may then add one answer-enrichment call with the original
source images. Global-only retrieval is the installed Reader boundary until a
qualified document association exists. Disabled or complete-empty retrieval retains
the ordinary two-call path. Withheld-only partial or unavailable retrieval does not
silently become complete-empty; enrichment failure, abstention, malformed answer or
lost request progress prevents output and records failure. Enriched answers require
a bounded `ANSWER:` frame. Routine logs retain only memory status/count diagnostics,
not saved memory context or enriched answer text.

The shared receiving context interface is usable by future real Writer consumers;
this does not claim Writer implementation. Provider protocol fixtures verify
question/image bytes and labeled data assembly, not live model precedence or native
rendering. Consult the owning change for exact revisions and observed test evidence.
