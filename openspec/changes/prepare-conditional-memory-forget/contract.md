# Conditional one-fact forget protocol v1 - proposed

This accepted contract is implemented by unmerged Buddy70 77e92306. Delivered v0.17.0 does not support these new operations; current candidate/CI/review and delivery remain separate. Existing inspect/query reports, regular-file Forget and all unrelated APIs remain unchanged.

## Fixed transport and bounds
`reader-buddy --memory-operation prepare-forget|forget|forget-receipt --memory-input - --config ABSOLUTE_CONFIG` runs once, consumes EOF and emits at most one generic report-v1. Inclusive stdin cap1048576 bytes; encoded report cap8454144 including newline; caller deadlines/cancellation remain host-owned. No remote staging fallback or running Buddy API. New prepare/receipt selectors reject regular files; old forget files retain existing semantics. Put/all setup dash still refuse before config/input/Store. Earlier builds may reject the unknown selector/dash and are unsupported before mutation dispatch.

All new request/evidence structs deny duplicate/unknown fields recursively; enum variants are struct-shaped so global/local extra fields cannot slip through unit-variant decoding. UUIDs nonnil, digests64lowercasehex, exact versions1, sorted unique sets/lists validated before Store admission. Strict Key has profile, scope global{} or document{document}, fact and reuses unchanged domain/profile validation. Arrays are parsed without silently deduplicating caller input.

## Preparation request
`{"prepared_version":1,"operation":"INTENT_UUID","key":{"profile":"UUID","scope":{"kind":"global"},"fact":"UUID"}}`

The privileged host generates one intent UUID before preparation. Preparation needs an existing Store and authoritative profile, legacy sync disabled and correct current local/shared mode. Explicit maintenance remains allowed when automatic memory is disabled. It refuses unavailable/invalid whole views and anything except exactly one supported current value. Fact/Envelope schema and derived record ID must validate; asserted provenance stays asserted. There is no preview for an absent/tombstoned/conflicting/opaque key and no implicit initialization.

Preparation report operation is prepare-forget. Success status ok/incompletefalse, data:
`{"schema_version":1,"preview":ENVELOPE,"intent":PREPARED_INTENT}`.
The exact envelope and evidence originate from one admitted view; the consuming writer validates that view and full report bytes. Ordinary/local preparation requires a NEW Store-owned conditional heads/generation guard under its mutex through the consuming writer; existing unsealed ordinary Inspection alone is insufficient. Selected preparation reuses whole-view pins. Stale/forged/prefix controls must cover both modes. Stale/forged/oversized data refuses before output; a prefix I/O failure never appends replacement JSON. The host validates preview and exact Key before presenting explicit confirmation.

## Prepared intent
Top-level ordered fields: prepared_version, operation, key, expected, binding.
`expected` is a sorted nonempty list of `{revision,sha256}`, initially exactly one current value, pairing revision with SHA256 of its canonical typed Envelope serialization. The current stored/domain envelope must match that exact content, not UUID alone. This is distinct from selected raw transaction digests, which MUST use original accepted bytes.

Binding ordered fields:
- config_sha256: SHA256 of UTF8 `urn:remarkable-buddies:prepared-forget-config:v1:` followed by compact direct serialization of ordered `{config_schema_version,config_path,paths,memory,legacy_sync_enabled}`. config_path is the exact absolute explicit CLI path, paths is typed StorePaths data/cache/credentials, memory is typed Configuration enabled/profile/selection, legacy_sync_enabled is loaded sync.enabled. No credential value or credential contents are read; credential path is only a hashed ownership reference. Typed serialization/order is producer-owned, not arbitrary JSON-map ordering.
- mode: original typed `{actor,sha256}` from the SAME preparation Store snapshot, retained through its lease; confirmation acquires lease using that original token, never a fresh replacement.
- actor: exact Store actor UUID; store_generation: exact active Store generation UUID.
- domain: `{kind:"local"}` or `{kind:"selected",identity:IDENTITY,pins:[PIN...]}`. Identity is exact group/profile/binding_sha256. PIN ordered fields scope,store_generation,aggregate_generation,accepted_base_sha256,selection_sha256,head_sha256. Scope is group/key_sha256/binding_sha256; selection_sha256 is the fresh token digest and head_sha256 is ORIGINAL raw accepted-head transaction digest. Pins include catalog plus every admitted registered aggregate, sorted by scope key identity, unique and at most65 entries; existing charged read budget64aggregates/4096work_items/8MiBmetadata/32MiBmedia remains authoritative and may refuse earlier. Catalog/target identification is derived from Identity and Key/Owner, never caller-chosen.

No binding is a live capability or authority to open a requested root. Config selects actual paths/profile/identity, which must hash/match original. Store admission freshly mints live selected tokens and compares evidence under the existing gates. Unknown/colliding/foreign/missing evidence refuses. Full identity plus mode token alone is insufficient.

## Confirmation and receipt input
Both use `{"intent":PREPARED_INTENT}`. The host retains the exact packet privately with verified physical target/boot/session generation. Renderer receives only display/confirmation identifiers; confirmation cannot provide arbitrary replacement intent, path, operation, head or binding. Unknown outcomes retain original private intent; disconnect/clear never converts unknown to not-dispatched or creates a new operation.

Before first execution: validate strict request/config/profile/owned paths; open existing Store; match actor/generation; acquire original-token ordinary/shared lease and exact configured shared scope; admit current complete domain view. If an exact original receipt exists, acknowledge only after the historical checks below, with no second publication. Otherwise every original pin/content/expected head must match current under the gates before conditional publication. LOCAL FIRST PUBLICATION requires a NEW Store conditional entry point holding ONE mutex guard continuously through original generation/content/head comparison and publication; a precheck followed by unchanged LocalMemory::forget/Store::commit is prohibited because Store::restore can replace generation while an ordinary lease exists. A private already-locked helper may be factored without changing existing file behavior; no reentrant lock. Selected confirmation retains its existing gated expected-token CAS. One operation UUID describes this exact original deletion request; changed-input collision refuses.

Receipt-only NEVER falls through to mutation. A local receipt requires exact original envelope operation/actor/Key/parents/tombstone and a bounded uniquely matching accepted single-envelope/no-media manifest in the original generation (multiple matching manifest UUIDs remain unresolved, never an arbitrary choice); no call to commit/publish. Selected receipt requires existing original_receipt collision/intent rules plus the original commit DIRECT predecessor matching prepared target raw head digest, scope, store/aggregate generations, accepted base and selection identity. Current catalog and all non-target aggregate pins remain exact; target changes after the original commit are allowed only through validated lineage for historical lookup. Original mode/config/store/domain identity still must match. For BOTH modes, every expected revision/content SHA256 must also match its original accepted parent Envelope: local original generation history or selected original DIRECT predecessor selected records, never later current heads or tombstone parent IDs alone. Modified expected hashes refuse acknowledgement. Failure or no provable receipt remains unresolved, never proof no commit occurred. The logical historical identity is actor/Key/operation/parents/tombstone plus verified parent contents. Original selected predecessor proves that target acceptance context; present config/mode/catalog/other pins are conservative CURRENT admission checks, not proof those fields were consulted on original execution. There is no persisted full prepared-packet fingerprint, so receipt must not claim historical proof of all preparation fields or that an older file-origin logical operation used this new protocol.

## Report data and uncertainty
All new operation-specific data uses schema_version1; generic report framing remains version1. Success for forget/forget-receipt is statusok/incompletefalse with exactly `{schema_version:1,outcome:"acknowledged",operation:UUID,transaction:UUID}`. This is the historical original transaction acknowledgement; never current deleted/removed, current-state readback, or permission to perform another operation.

A complete refusal before any mutation attempt uses data `{schema_version:1,outcome:"not-dispatched"}` with non-ok status and the phase-specific incomplete flag in the exact matrix below. After a mutation may have committed, failure uses `{schema_version:1,outcome:"unknown"}` with unavailable/incompletetrue when a complete report can still be emitted. Receipt failure uses `{schema_version:1,outcome:"unresolved"}` with phase-specific status/incomplete from the exact matrix below; malformed receipt input alone has null data. If no complete validated report arrives, host state after possible dispatch is unknown regardless of exit status/timeout/cancel. InvalidInput/Busy/Unsupported from validation/admission are pre-attempt; implementations must not mislabel a possible commit with those statuses. Prepare failures are always nonmutation; existing report flags stay unchanged for old operations.

Clear stale detail after possible confirmation dispatch. No optimistic deletion, automatic resend, generated replacement UUID/heads/mode or empty-success substitution. After historical acknowledgement, display that original request was acknowledged and require a fresh deliberate inspection for current heads. Tombstone retains history/native documents and reclaims no bytes; selected local publication does not imply cloud propagation or start provider/worker/service.

## Required evidence before acceptance
Meaningful real local/selected prepare/confirm/receipt outputs; mode switch and re-entry; config/path/profile/identity change; same-Key/head-ID catalog/base/aggregate generation replacement; preview/confirmation stale/content changes; exact receipt after later value without a new tombstone; changed-input collision; receipt absence without dispatch; Busy/missing/no-init; raw nested duplicates/unknowns and all bounds; before/after commit and consuming writer prefix faults. Capture exact request/stdout bytes and hashes for independent consumer parsing. Browser/Electron host/IPC/unknown-state controls use explicit synthetic transport where appropriate and are not tablet proof. No device contact follows from source acceptance.

## Exact failure matrix

| Selector/phase | status | incomplete | data |
| -- | -- | -- | -- |
| prepare malformed/foreign request | invalid-input | false | null |
| prepare missing config/profile/Store | unavailable | false | null |
| prepare Store busy | busy | false | null |
| prepare wrong mode/legacy sync or non-confirmable empty/tombstone/conflict/opaque value | unsupported | false | null |
| prepare domain/currentness/budget refusal | unavailable | true | null |
| forget malformed input | invalid-input | false | schema_version1/outcome not-dispatched |
| forget missing config/profile/Store | unavailable | false | schema_version1/outcome not-dispatched |
| forget Store busy | busy | false | schema_version1/outcome not-dispatched |
| forget incompatible mode/legacy sync | unsupported | false | schema_version1/outcome not-dispatched |
| forget changed original binding/content/heads or intent collision, definitively before attempt | conflict | false | schema_version1/outcome not-dispatched |
| forget domain/budget refusal definitively before attempt | unavailable | true | schema_version1/outcome not-dispatched |
| forget any error after possible mutation attempt | unavailable | true | schema_version1/outcome unknown |
| receipt malformed request | invalid-input | false | null |
| receipt missing config/profile/Store | unavailable | false | schema_version1/outcome unresolved |
| receipt Store busy | busy | false | schema_version1/outcome unresolved |
| receipt incompatible current mode/legacy sync | unsupported | false | schema_version1/outcome unresolved |
| receipt no provable receipt, changed binding/content or domain/currentness/budget refusal | unavailable | true | schema_version1/outcome unresolved |

Success rows are exactly the prepare/acknowledgement shapes above. No Partial or
Failed status is introduced for these selectors. Writer prefix failure emits no
replacement row. Host accepts acknowledgement only from one complete validated
matching report and successful process exit; any nonzero/late/partial/unparseable
result after possible dispatch remains unknown. Preparation never dispatches a
mutation, regardless of its failure. Receipt failures never resolve the original
mutation outcome or fall through to confirmation.

## Consumer preview canonical-byte recipe

The expected content digest is NOT JSON.stringify of received report bytes or a
public projection. Reconstruct typed Envelope field order exactly:
envelope_version, namespace, domain_schema_version, record_id, revision_id,
parents, operation_id, actor_id, kind, payload, media_descriptors. UUID fields
serialize canonical lowercase hyphenated; parents sorted by UUID bytes and unique.
For this initial supported preview, kind is value, media_descriptors is empty,
and payload is a canonical supported Fact object whose nested JSON objects use
lexicographically sorted Unicode keys recursively (serde_json default Map order),
with arrays in original order. Require raw payload to equal typed Fact roundtrip
Value, including canonical UUID strings and no hidden legacy-global extras; reject
rather than normalize an unsupported payload. Subject/value/provenance strings
retain their exact Unicode content. Integers are nonnegative decimal; prepare
refuses observed_ms/expires_ms above9007199254740991 so both hosts can independently
validate without precision loss. Existing Fact/file APIs keep their wider u64 range.

Use compact JSON without whitespace or trailing newline, UTF8 without BOM. Escape
quote/backslash and controls using JSON short escapes for backspace/tab/newline/
formfeed/carriage-return, otherwise lowercase \u00xx. Do not escape slash, other
Unicode, U+2028/U+2029 or non-ASCII characters. Nested payload keys preserve their
actual canonical Value ordering; do not use typed Key's different direct field
order for that nested Value. SHA256 these exact bytes. The sibling golden vector
records actual existing-library serialization plus an independent byte/hash check;
it is a synthetic serialization diagnostic, not a Store/mutation/device run.

## Review reconciliation and evidence attribution

Full independent review5583470985 at34db7a58 was read. P1 is addressed in the
atomic local first-publication contract/design: one Store mutex guard covers
original generation/complete heads/content and actual publication, including the
restore interleaving; legacy file behavior remains unchanged. P2 explicitly
compares every expected hash with accepted original parent content before receipt,
adds tampered-hash/changed-parent controls, and distinguishes logical operation
identity/original target predecessor from conservative CURRENT admission. No full
prepared-packet historical fingerprint is claimed.

Consumer comment6288203027 was read. The new failure matrix, exact canonical-byte
recipe, safe-integer preview restriction and envelope-golden.json address its
producer framing/hash questions. Golden canonical body is913UTF8 bytes with
SHA256 a32d40a07ce867ec4d0d738e0f5317636f5d8bcd9c62dadbd342ffc7fbf1f75c.
A standalone scratch diagnostic linked the already existing library, validated
Envelope/Fact/derived ID and actual Rust serialization; independent Python
reconstruction matched all913bytes and hash. Initial helper compilation selected
an incompatible serde_json build artifact and failed; matched64ba artifact fixed
that helper only. No feature implementation, Store, tablet, new app build or broad
producer fixture replay occurred. Consumer private reference/retention details
remain in its coordinated precode; producer implementation began only after full corrected review5583523433 and
explicit exact consumer agreement6288406539. Consumer host/UI precode has its own
independent review and bounded in-memory custody/restart scope.
