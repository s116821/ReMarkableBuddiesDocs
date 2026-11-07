# Explicit Writer enrollment after abstention

## Scope and admission

An explicit user action may supply a full transcription of an exact retained
Writer image after valid WholePage abstention. This is enrollment of a confirmed
sample with no original interpretation. WholePage, Generate, archive/source
provenance and the existing explicit partial and math policies keep their
current behavior. An unreadable model result is never a confirmation.

Extend the typed Writer receiving outcome to hand its admitted input owner an
opaque, operation-owned abstention value only for a successfully parsed
`Normalized::Unreadable`. Bind it to the original operation, same Store and
conversation, original user turn and revision, ImageUse and revision, ordinal,
page, source observation and admitted PNG digest. It contains no machine text
and publishes no normalized document. Parser failure, provider error, missing
media and cancellation do not produce this value. The owner keeps it in memory
for the corresponding correction interaction. Loss or invalidation of the
value ends eligibility for a new write. An existing write is reconciled by
operation status.

The input owner that presented this exact retained image and its abstention
must collect the user's explicit intent to save the supplied text as a
handwriting example. Plain editing, Refine, dismissal and retry convey no such
intent. The existing typed Dispatch owner boundary can accept this event and
enforce custody. No shipped native Writer owner currently supplies either
eligible image ingress or this event. The existing offline Handwriting1 CLI
owns explicit caller confirmation of submitted samples only. It does not own
a live Writer abstention or prove that supplied IDs refer to it. This increment
does not expose a CLI command that fabricates that authority. A fixture may
exercise the typed boundary and cannot qualify native UI.

Use the existing same-Store Dispatch admission, retained ImageUse resolver and
Handwriting1 publication. On explicit enrollment recheck active profile,
source observation, exact current source/turn heads, Writer user role and
association, ordinal, page, PNG digest, static PNG and the existing 512 KiB /
4096-byte limits. Reuse the existing profile-scoped image correction identity
and operation replay rules. Keep the original receiving operation and the
distinct user confirmation operation separate. Bind the frozen confirmation
input to source and turn revisions, exact media and expected correction heads.
An existing correction of the other provenance kind conflicts. A later
explicit edit of the same enrolled sample may use existing update CAS while
preserving absent-original provenance. Never silently switch lineages. Recheck
custody before publication. On stale heads or unknown outcome use existing
refusal/status behavior and never replay blindly.

## Stored values and consumers

Keep the existing Handwriting1 namespace, correction kind, field order,
envelope and IDs. Extend the stored original field from a required string to
a required string-or-null. Exactly one new provenance kind,
`caller-confirmed-after-abstention`, requires explicit null and the checked
three-ID runtime provenance assertion. Legacy `caller-confirmed-sample`
continues to require its existing nonempty original. Missing original,
empty original and kind/value mismatches fail closed. Do not rewrite legacy
records. Keep the existing public version-one confirm/update request parser
and legacy strings unchanged. Internally admit the new variant through the
same validation and publication implementation with a typed input that only
the custody-checked owner can construct. No registry or parallel publisher.

Preserve legacy serialization, operation fingerprints, value digests, and
context identities byte for byte. New records have explicit null in stored and
inspected original fields and in their original-text hash representation. Null
has its own identity and is never hashed as empty text. Treat provenance kind
and original state as immutable for updates. Query matches the supplied
confirmed text and matches original text only when present. Store selection
and capture still validate media and lineage and present the exact image with
user-confirmed text. Audit standalone context and ordinary Reader/Writer
payload builders independently. Keep all legacy-only payloads exact. With an
enrolled example, represent absence explicitly as null and use a distinct
context recipe revision with an instruction that null means no machine
reading exists. Do not send a fabricated original, the abstention token as
transcript, or evaluator text. Pin each affected profile, payload and identity
before source implementation.

New consumers accept both shapes. Older readers cannot interpret the new
variant and must refuse it through existing version/value validation. Before
implementation, establish whether older store, backup and restore consumers
refuse the new value before mutation. If this cannot be guaranteed with the
existing format and validators, require an independently reviewed capability
boundary before enabling publication. Cover inspection, status, forget,
backup/restore and sync/portable behavior through the existing scope and
guards. No new sync behavior or portability claim.

## Focused acceptance matrix

| Case | Required result |
| --- | --- |
| Valid unreadable plus explicit intent with current owned image | One confirmed record and exact PNG, null original, no Generate or normalized archive |
| Valid unreadable alone, ordinary edit, cancel, Refine or retry | No write and no example |
| Provider failure, malformed response, partial or structured outcome | No abstention capability and no enrollment |
| Foreign Store, profile, conversation, turn, image, ordinal or page | Refuse before publication |
| Changed observation, source or turn revision, missing or substituted bytes, ineligible PNG or oversize text | Refuse before publication and preserve existing records |
| Stale or conflicting correction heads, legacy-kind collision | No overwrite and no lineage conversion |
| Repeated operation, changed input under same ID, interrupted output or unknown result | Existing exact status and CAS semantics, no second publication |
| Legacy strings, digests, payloads and tests | Exact bytes and old behavior |
| New valid variant and missing/null/empty/mismatched variants | Only the explicit valid shape admits, with exact media and no synthetic original |
| Mixed context, query/inspect, update and forget | Correct nullable representation, truthful payload, stable identities and existing exclusion rules |
| Prior-version reader and current backup/restore round trip | Fail closed before mutation when unsupported, current version preserves exact record and media |
| Missing native owner | Source/API evidence only, native integration stays open |

This amendment is precode. Independent review must accept the ownership and
compatibility boundary before code. The consumed Barton and Lincoln outcomes,
frozen semantic criteria and coordinated delivery gates remain separate.

## Consumer trace on reconciled source

The older handwriting provider decodes the typed Correction in
handwriting/mod.rs. Null in its required String or the unknown provenance enum
fails decode. In provider.rs, fact reports unsupported, context capture cannot
admit it, and status and mutation traverse Self::lineage before returning a
successful result or committing. Confirm/update/forget cannot replace the
unsupported history through that path. Explicitly restrict the legacy public
input provenance to CallerConfirmedSample even if the shared enum grows.
Include provenance kind in same_original for internal mutations.

Storage mod.rs validate_objects_policy validates Envelope, object hash, sizes,
namespace and media coverage. It does not decode the handwriting payload.
Notebook backup validation calls that function and notebook_generation/records.rs
skips domain version one. Opaque object preservation through backup/restore
therefore does not itself require a new format. Verify this with exact old/new
record and media round-trip controls, including the common recovery path, before
publication. Keep payload interpretation and typed mutation refusal separate
from lossless backup behavior.

## Exact changed components for mixed context

See [mixed-context vectors](writer-abstention-mixed-vectors.json). The fixed
instruction is a separate text part immediately after the existing context
addendum, before the first example descriptor, only when at least one example
has no original. Keep example ordering and image placement unchanged.
The vectors pin the exact standalone and Reader descriptor strings, ordered
context identity bytes, four notebook Profile byte strings and extractors,
and both Reader diagnostic recipe names. The suffix applies only to contexts
containing a null original. No-context and legacy-only paths retain all current
protocols, addenda, recipes and hashes. The fixture identifiers and image hashes
are synthetic serialization inputs. They do not imply admission of any media.
