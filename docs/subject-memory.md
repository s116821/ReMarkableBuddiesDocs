# Optional local subject memory

The local memory domain stores explicit associative facts in the existing
SubjectMemory namespace. It supports store/update, bounded query, exact current
inspection and forgetting through `memory::Provider`, with `LocalMemory` as the
default offline implementation. Explicit local selected membership uses
`SelectedMemory` over the same Store. It does not automatically learn from answers, failed
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

In default local mode, only a valid creation put with empty expected parents may initialize absent/empty
owned storage. Reads, forgetting and updates cannot initialize missing state or
repair a partly owned nonempty root. Existing Store opening can still perform its
normal known metadata/recovery/staging cleanup under the lease; these are not the
nonmutating inventory commands. A busy Store returns a fixed busy report instead
of stopping/retrying a service or reading without a lease. Pure input-validation
failures, including self-parent requests, fail before startup writes.

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
local memory is refused. The selected adapter described below uses reviewed
REM-52 primitives; remote workers/catalog onboarding, account visibility and
cross-device recovery remain unqualified. There is no ordinary-head fallback.

## Explicit local selected membership

Select this mode with a complete identity under `memory.selection`, matching the
ordinary portable profile. This example is a configuration fragment:

```json
{
  "memory": {
    "enabled": false,
    "profile": "bfcf4324-d157-4d7f-b2fd-08f0fb60d73c",
    "selection": {
      "group": "f3e8b68e-23f6-4b43-8d59-2ec542a768da",
      "profile": "bfcf4324-d157-4d7f-b2fd-08f0fb60d73c",
      "binding_sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    }
  },
  "sync": { "enabled": false }
}
```

These example identifiers/digest do not establish a cloud group or account
binding. Supply and preserve the explicit identity for your local selected setup.
The group and binding partition the selected Store; choosing their values grants
no provider visibility or native permission. Legacy sync must remain disabled in
this mode until its separate selected worker is qualified. The enrichment flag
may remain false for maintenance and can be enabled independently afterward.

The same binary adds explicit setup operations:

```text
reader-buddy --memory-operation initialize-aggregate --memory-input /absolute/path/aggregate.json
reader-buddy --memory-operation initialize-selection --memory-input /absolute/path/catalog.json
reader-buddy --memory-operation register-selection --memory-input /absolute/path/registration.json
```

`initialize-aggregate` takes `operation`, `accepted_base_sha256` and a complete
`fact`. It creates one new independent global chain or a new memory-only document
aggregate. `accepted_base_sha256` is an explicit lowercase 64-hex descriptor
digest, not a verified remote winner. An existing different initializer refuses;
an exact retry returns the original receipt. Document initialization does not
implicitly import legacy records or prove the native document exists. Existing
mixed documents must be adopted through their complete validated closure.

`initialize-selection` takes `operation`, `accepted_base_sha256` and a complete
`registrations` array. A registration is the exact `data.registration` returned
by aggregate initialization, containing the typed owner and immutable raw genesis
identity. Every referenced aggregate must already exist and validate. An empty
array explicitly creates a complete empty catalog. Only these two initializers
may create an absent/actually empty Store; partly owned nonempty state refuses.

`register-selection` takes `operation` and one `registration` for an existing
validated aggregate. Absent membership is appended; identical existing membership
returns `adopted` separately from an original `replayed` operation. Changed owner
or genesis refuses. Adoption never republishes a losing creation/fact payload.
Create aggregates before registering them: an interrupted sequence can leave an
orphan, which remains outside query membership until explicitly validated and
registered. Ordinary selected put/query/inspect/forget cannot bootstrap absence.

Document facts share the stable source-document conflict aggregate with its
conversations; profiles do not split it. Global fact chains remain independent.
The catalog keeps the same original root and append-only accepted registrations.
Current facts come only from complete winning closures. Historical selected
envelopes check immutable key/claim custody, including later-created facts and
re-rooted replacements, but never supply current values, parents or permissions.
Unknown/ambiguous mixed ownership and absent/corrupt/stale membership refuse.

One selected-snapshot receiving request shares 64 snapshot attempts, 4096 transaction/reference
work items, 8 MiB metadata reads and 32 MiB media verification. Catalog reads,
historical/retained verification and final rechecks consume the same allowance.
Attempts include absent scopes and repeated reads: an answer can exhaust this
budget before reaching 64 registrations. Exhaustion refuses, without a partial
authoritative catalog. Publication has separate existing Store limits; this is
not a combined read/write I/O cap or a wall-clock/native memory qualification.

Selected results bind their exact payload and Store-issued pins. API consumers
use `Provider::with_current` around the actual synchronous consuming write;
unchanged clones can consume once and altered payloads refuse. Plain `inspect`
is a historical read; `inspect_for_handoff` returns a sealed inspection for
guarded consumption. Maintenance keeps its Provider/Store lease through
`Report::write_to` and stdout, including empty queries. `Report::encoded` only
formats bytes. Stale/changed/exhausted admission writes fixed unavailable with
no data; a failed partial stdout write is never followed by a second report.

Selected memory can enrich the current Reader processing journal under those
guards, but its native output remains explicitly refused. That journal is not a
qualified selected conversation or native effect record. Shared/isolated Drive,
remote catalog/OAuth/publisher, Manager, Writer, restore/migration and native
qualification remain separate open gates.

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
