# Current basis and ownership

Original basis: delivered Source9be8862822e4ff0f110d91a0127b1af6db379e5c and
Docs11090c3a8f2cd1b1578798ab390cd757b315d0c3. This revision reconciles Docs
main6394f582101076e4df9770ba6a46051e2b65beab and the reviewed feedback Source
86d6c4f2fafa6c05534612bdb16b5ba93a0d59bb (delivered tree at
68e42968b4c58b6f8ed1102078d78b40fad33ffc). Relevant current code is
src/writer/mod.rs, src/conversation/writer.rs, src/conversation/writer_flow.rs,
src/writer_flow/mod.rs, src/note_export/run.rs, src/storage/types.rs and
src/storage/contract-v1.json, src/storage/contract-v2.json, src/retrieval.rs, src/conversation/selected.rs,
src/conversation/cleanup.rs and src/conversation/receiving.rs. The prior host-flow archive and closed
two-call quality observation are historical evidence, not new-run authorization.

Source/native shared-path handoff remains a pre-implementation gate. Source3 is
reserved for ArchivedNormalizedSource, Conversation3 for NotebookPlan/NotebookStage,
Kind::Value only, with exact record_kind strings in the adoption contract. Native
source f026bb6385a2c450fa4d79542fb57c097b98673f retains ExistingBinding schema2
and historical capture/evidence work; its older storage baseline lacks delivered
feedback contract-v2. Compose both after exact native-owner handoff, preserving
unfinished work. No native adapter, supervisor, service,
personal document, account pairing or firmware action is in this increment.

The revised [adoption contract](compatibility-adoption.md) is part of this
precode. Explicit in-place format adoption preserves the generation identity,
CURRENT and historical bytes; it does not copy retained media or require a new
generation UUID. The separately reserved unsupported format discriminator is the
old-writer fence. Envelope format1 and payload schema3 are independent of that
discriminator and feedback storage generation3. Contract1/2 remain immutable.
Generation4, ordinary same-actor backup4, contract3/contract-v3.json and
actor/generation-bound notebook-feature.json1 are reserved. Exclusive notebook
modules may proceed after review of this amended contract. Overlapping shared
edits still require a real native-owner acknowledgment at an exact revision;
allocation acceptance does not open that window.

# 1. Explicit commands and frozen input

Add generate-notebook and refine-notebook, plus
generate-notebook-and-export and refine-notebook-and-export, through --writer-note.
New requests require max_model_calls in 1..9. Generation declares a normalized
document_file with expected raw document_sha256, exact request, page/supplied-notebook selection and optional
separate guidance. Refinement selects a current notebook draft and its committed
archive; it does not reread the original input path. Existing inline commands
remain one-call paths with unchanged bounds, serialized reports and fingerprints.
Old refine does not silently turn into a multi-call operation on an archive.

New notebook requests may declare history_range using the existing strict
TurnRange shape (start/end_exclusive) and Ledger::context_range. Omission retains
the ordinary full eligible history; oversized history refuses for an explicit
selection rather than being summarized or truncated. The selected prior draft
is forwarded separately from eligible interpreted/completed history. Freeze the
exact chosen history and range in the plan; preserve all original turns in Store.

The command JSON limit remains 256 KiB. Only new generation reads the explicitly
named UTF-8 normalized JSON file, at most 8 MiB plus one rejection byte. Strict
deserialization, Index validation, complete planning, credential resolution and
all identity checks precede Store admission or model cost. Follow the regular-file,
opened-handle, bounded-read and expected-hash contract in [input admission](input-admission.md).
Freeze the validated observed byte buffer after hash verification; this is not a
claim of an atomic filesystem snapshot during concurrent edits. Later file changes
cannot substitute the admitted buffer.
File paths are command transport, not model input or durable source authority.
The admitted logical request binds resolved canonical bytes/digest, document
metadata, selection, guidance, exact request, history and planner revision.

Retain canonical JSON containing every supplied unit, text, location and metadata,
including units outside a page selection. JSON presentation/whitespace and original
notebook bytes are not claimed retained. The extractor's supplied source_sha256
keeps its existing meaning; it is distinct from canonical-JSON media SHA-256 and
normalized-unit SHA-256. Document IDs/page labels remain historical caller data,
never native document/page ownership.

# 2. Bounds and deterministic complete coverage

Initial new-path limits:

| Resource | Bound |
| --- | --- |
| Canonical normalized JSON | 8 MiB |
| Decoded document text | Existing Index 4 MiB bound |
| Selected text / selected units | 256 KiB / 256 units |
| Map calls / total calls | 8 / 9, additionally limited by caller allowance |
| Authoritative raw range per map | At most 32 KiB, split at UTF-8 boundaries |
| Optional adjacent context | At most 512 bytes per side, explicitly labeled |
| Each complete encoded model payload | 96 KiB |
| Each map reply as JSON string | 4 KiB encoded, nonempty, valid text |
| Final draft | Existing 24 KiB title/Markdown contract |
| Per-stage / aggregate cooperative budget | 95 / 600 seconds |
| New relevant heads / immutable envelopes per request | At most 64 / 256 |

Use Index::build for validation, not query relevance ranking to discard content.
The planner partitions selected units in original order. It prefers whole units
and paragraph boundaries, falling back to exact UTF-8 byte ranges. Authoritative
ranges have no gaps/overlap; optional context is separately marked and excluded
from coverage counts. Each range retains original unit ordinal/page/section and
byte offsets. Duplicate source text remains distinct supplied content.

Construct every map payload before the first model invocation. Bound source,
context, guidance, personalization and exact frozen history by actual encoded
bytes. Reserve the reducer's worst case before cost: at most eight 4 KiB encoded
summaries plus bounded stage-reference metadata. Its fixed encoded context must
fit the remaining budget. Valid maximum-size summaries must therefore fit; an
invalid/oversized summary fails instead of being trimmed. These are byte/work
bounds, not a tokenizer or provider-context guarantee. If planning, history,
storage reservation or caller allowance cannot fit, refuse before calls rather
than dropping units, using a different model or lowering coverage silently.

The aggregate budget is monotonic across stages; each stage also uses the existing
provider's cooperative deadline/cancellation. Owned workers and provider I/O are
joined. Synchronous file/Store work and non-cooperative alternative engines do
not acquire an invented hard outer wall-clock guarantee.

# 3. Typed durable source and stage records

Reuse Store::stage_blob(ObjectRef, reader) and the existing atomic manifest
publication. Staging is not source visibility. A new domain-specific validator
must bind fully validated canonical JSON to its Media descriptor before staging;
do not call JSON a screenshot merely because stage_image currently wraps the
same generic primitive. Source publication requires the complete blob.

Source3 ArchivedNormalizedSource holds conversation/original-user-turn identity,
document/index/digest metadata, selection/guidance and one required JSON Media
descriptor. Its identity includes exact logical source facts. Envelope descriptors
must equal the typed payload's required descriptors exactly. Source1 captures and
Source2 inline normalized sources preserve existing serialization and validation.

Conversation3 NotebookPlan/NotebookStage records are non-visible processing facts,
not turns, summaries substituted for user history, or native admitted intents.
The plan records exact coverage, algorithm revision, request/history digests,
work/output bounds and stable stage identities. Stage facts bind ordinal/kind,
source and plan revisions, exact input digest, predecessor result revisions,
sanitized outcome and bounded returned text/digest. Only the user request and final
Generated proposal allocate ordinary conversation chronology. Ordinary root/turn/
receipt formats remain unchanged; native Conversation2 intent/settlement and
Export2 attempts retain their existing meanings and fingerprints.

The exact serialization, domain separators, archive/plan/stage/transition IDs,
input digests and export revision are pinned in [identity recipes](identities.md)
and [literal fixed vectors](identity-vectors.json). Stable operation UUIDs derive
from the explicit generation operation and stage kind/ordinal. Reuse Ledger replay, expected heads and
publish_observed; no second job registry, native HistoricalIntent reuse or
selected-runtime execution permission. Every paid stage requires this invocation's
positively fresh durable preparation. Each successful stage returns a private
cursor containing the exact newly published root/guards/result references.
Subsequent stages consume that cursor without refreshing to bless intervening
changes or self-invalidating against pre-publication revisions.

Lost preparation or result acknowledgment ends automatic continuation, even when
a Generated stage is present after reopen. Replaying the original operation makes
zero additional model/destination calls. This increment does not implement partial
job auto-resume or infer a send grant from saved stages. A new explicit generation/
refinement operation can start new work within its declared budget; old partial
facts remain retained. Reports distinguish local invocation counts, confirmed
stage recording and unknown remote cost. Zero observed invocations and successful
durable no-call recording are separate facts if a root was deleted/conflicted.

# 4. Final proposal and export

Map and reduce requests forward the exact original user request and separate
guidance/personalization. Refinement also forwards the exact selected prior draft;
it replans/processes its original archive under the new explicit request. Map
instructions and processing facts are not inserted as invented user turns.
Semantic compression is model work; processed-byte coverage is not proof that
every fact was summarized correctly. Preserve failed outputs within declared
bounds and use a separate representative quality gate.

One actual Writer owner spans the whole run. A joined command acquires the actual
Writer then export owner in the existing nonblocking order and holds both through
all stages, final publication, destination waiting and outcome recording. Do not
hold the Store mutex over HTTP. An unresolved previous export refuses before new
model cost. Cancellation is latched; failures, changed source/history or late
replies stop subsequent stages and export without an automatic retry.

Only positively fresh final publication returns the private selected snapshot:
final draft, archive, completed-plan/source lineage and exact root revisions.
Existing prepare-export/export-draft remain deliberate read-only preparation or
explicit sending paths for supported selected sources; reconcile-export remains
known-ID read-only. Legacy inline source-revision bytes remain identical. Archive
revisions use the pinned distinct digest recipe; logical document/selection scope
and stable backend correlation remain compatible for deliberate re-export.

Extend guarded export admission to fence the exact final plan/archive/draft/root
and required media identity, using that publication's returned references. Check
required archive availability/integrity before model use and at the pre-destination/
pre-write eligibility boundaries; do not reload a newer body or source. Before
the first write poll, cancellation/change suppresses writing. Persisted no-send
failure remains distinct from observed zero writes. After a write poll, keep
existing uncertainty/read-only known-ID reconciliation, never restart models or
retry writes automatically. Model cost already incurred is not erased by no-send.

# 5. Consumer compatibility and reference closure

| Existing boundary | Required new-path behavior |
| --- | --- |
| Generic envelope/contract | Envelope format1 unchanged; exact Value-only Source3/Conversation3 shapes require adopted generation4 and contract3; contracts1/2 immutable |
| Ledger decode/inspect/context/retained_media | Exact descriptors, original source-turn linkage, required JSON bytes and truthful missing-media state; no fake dimensions, image role or visible intermediate turns |
| Writer source reads/refinement/export | Complete archive/ranges and immutable plan lineage; source changes/absence refuse; no fallback to cache or original input path |
| Historical selected projection | Explicit non-native source ownership and exact same-conversation origin linkage, analogous to Source2; never make document UUID into native ownership |
| Whole owned backup/restore | Ordinary same-actor backup4 preserves original record/media bytes, conflicts/tombstones, lineage and reference counts; selected/cross-actor notebook import refuses |
| Generic report1/2 | Truthful unsupported/null for generation4; no enum widening or complete-accounting claim; full accounting/companion handling remains required data-management/final-readiness integration |
| Narrow conversation cleanup | Preserve current Source1-oriented support/refusals; Source3/Conversation3 relevant data must produce explicit pre-mutation unsupported/refused results, not silent omission or deletion |
| Native receiving source_id/source_media and execution | Remain explicitly unsupported for the new host schema; no broadening of native receiving/admission, synthetic image conversion or runtime activation |
| Older consumers | Unsupported current format fences history recovery/publication; actual predecessor entrypoints need qualification; pending pre-format metadata may be ignored by old writers; supported historical bytes retain meaning |

Generic blob support alone is insufficient. Audit each typed media enumeration,
cleanup/receiving filter, selected closure, inspection, backup/restore and published
offline contract. Add refusal-only guards where an existing default could silently
skip the new kind. A complete supported consumer must follow all retained source,
plan/stage and media references; a narrow unsupported one must report that honestly
before mutation/publication. Garbage collection must not collect a blob still
referenced by any retained revision, including after logical deletion. Do not
expand this increment into native receiving or broad category-cleanup enablement.
Command/mode preflight must also refuse before admission/cost if its selected
projection, outbox or receiving path requires an unsupported new-record consumer;
successful generic Store opening does not grant sync or native execution support.

# 6. Verification and delivery

Maintained --simulate Writer scenarios use the production planner, stage runner,
Ledger and scripted destination, with declared normalized assets relative to the
scenario. Writer scenario JSON remains capped at 1 MiB; each new source asset is
bounded to 8 MiB and total declared source assets to 32 MiB before execution.
Every asset declares its expected raw SHA-256 and follows input-admission.md;
relative path resolution does not weaken special-file/reparse/race refusal.
Reader schemas/admissibility stay unchanged, including valid inputs above 1 MiB.
Keep reports as JSON, with exact source/range/stage/call/export facts and no tablet
PNGs or invented native transitions. Seeded Reader history remains fixture history.

Use real Store/reopen and actual localhost OpenAI/Mem adapters for boundary tests:
complete coverage, UTF-8/paragraph/context boundaries, maximum budgets and one-over,
per-stage before/after-commit acknowledgment loss, crash gaps, changed request under
old operation, cancellation/deadline/late or invalid reply, source/blob/history
changes, cross-entrypoint overlap, final publication acknowledgment loss and
export uncertainty. Verify whole backup/restore and supported/reference traversal,
plus explicit older/narrow-consumer refusals without lost bytes or native effects.

Because map/reduce changes model-facing behavior, prepare a new named original
quality plan after code/current-head qualification and independent pre-live review.
Use a new synthetic notebook above the old limits, boundary facts/equations/page
citations/guidance and a deliberate refinement; freeze input/plan first. Target
two maps plus reduction for each request, at most six total provider invocations
in one bounded attempt, using existing approved local configuration with process
precedence. Retain raw source/outputs, failures and Store graph for independent
semantic assessment. Do not replay the closed earlier two-call plan, substitute
easier inputs after failure, write to a live Mem account or operate a tablet.
Contributors without live configuration retain the missing gate for a maintainer.

Complete one coordinated Source/Docs implementation, current-head checks, review,
canonical sync/archive and ordinary Docs-first delivery. Full physical notebook
ingestion, handwriting/drawing recognition, native Writer/combined routing and
whole Writer/MVP acceptance remain open requirements, not this host increment's
completion claim.
