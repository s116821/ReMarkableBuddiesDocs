# Proposed exact identity recipes, revision 1

These are new-path recipes under the accepted exact Source3/Conversation3 kind
reservations. Shared-path handoff and amended-contract review remain required;
allocation does not qualify an implementation.
The literal fixture identity-vectors.json pins examples independently of eventual
Rust implementation. The fixture is recipe evidence, not a model prompt or valid
large-notebook quality run. Do not regenerate expected values from the function
under test. Implementation must check literal values and one-field mutations.

## Serialization

C(x) means compact UTF-8 serde_json::to_vec(x), no BOM/trailing LF, escaping as
serde_json emits (Unicode remains UTF-8, control characters escaped), no Unicode,
line-ending or string normalization. Integers are unsigned decimal JSON numbers;
UUIDs are lowercase hyphenated strings; absence is null. All hash results are
64-character lowercase hexadecimal SHA-256. H(x) hashes bytes x. U(s) is UUIDv5
with UUID::NAMESPACE_URL and the exact UTF-8 name s. Arrays below have exact order;
their domain separator is their first string, included inside C. No object-key
sorting or arbitrary map serialization is allowed in identity input.

Canonical document bytes D are C(NormalizedDocument), retaining the existing
struct field order: document, format, source_sha256, extractor_revision, units.
Format is pdf/epub/notebook. Each SourceUnit has page, section, text in that order,
with null option fields retained. Units remain in original order. Strict parsing
rejects duplicate/unknown fields before canonicalization. The supplied extractor
source_sha256 spelling is preserved; validated expected raw input hash is lower
hex. Raw input includes its actual whitespace/LF, whereas D does not. The units
digest is H(C(document.units)). Do not substitute extraction digest for either.

Scope S is ["page",page] or ["supplied-notebook"]. The existing inline TextScope
object remains {"scope":"page","page":N} or {"scope":"supplied-notebook"}.
The exact JSON Media media_type constant is
application/vnd.remarkable-buddies.normalized-document+json;version=1.

## Archive and fixed request identities

Original user and final draft IDs preserve writer::stage:
U("urn:rmb:writer:v1:" + operation + ":user") and the same with ":draft".

A is the following ordered array (not a hash of an arbitrary Source3 struct):

```text
[conversation, original_user_turn, document.document, document.format,
 document.source_sha256, document.extractor_revision, H(C(document.units)),
 raw_input_sha256, raw_input_bytes, H(D), len(D), media_type, S, guidance]
```

source_identity_digest = H(C(["writer-notebook-source-v1", ...A])).
archive_id = U("urn:rmb:writer-notebook-source:v1:" + source_identity_digest).
Source3 has exactly id plus those facts; every semantic field is covered. The
expected raw digest/count refer to the original generation input even on refine;
refinement reuses archive_id, original user linkage and immutable media, and does
not replace original raw provenance with reserialized bytes. A new generation
has a new original user linkage; equal bytes alone do not alias conversations.

personalization_digest = H(C(["writer-notebook-personalization-v1",
snapshot.schema_version(), snapshot.effective_text()])). The snapshot itself is
not Serialize; these exact public effective inputs are frozen once. No credential
or unrelated configuration is included.

history_digest = H(C(["writer-notebook-history-v1", R, T])). R is null or
[start,end_exclusive]. T is the exact eligible ordered Turn vector from the
existing context-range contract, serialized with the unchanged Turn schema/field
order. Generated drafts are not eligible history and are forwarded separately.
Retain exact selected turn revisions as guards in addition to this content hash.
Any future Turn serialization change requires compatibility review/new recipe.

plan_id = U("urn:rmb:writer-notebook-plan:v1:" + operation).
Plan core digest is H(C(the following ordered array)):

```text
["writer-notebook-plan-v1", operation, archive_id, source_identity_digest,
 exact_request, guidance, personalization_digest, history_digest, prior,
 limits, chunks, "notebook-chunker-v1", "notebook-map-v1", "notebook-reduce-v1"]
```

prior is null or [draft_id, exact_draft_revision, H(exact prior UTF-8 text)].
limits has the following exact order/values; caller allowance is the final entry:

```text
[8388608,4194304,262144,256,8,9,32768,512,98304,4096,24576,95,600,64,256,
 caller_max_model_calls]
```

These mean canonical JSON bytes, document text bytes, selected text bytes/units,
map/total calls, authoritative chunk bytes, context bytes per side, encoded input
bytes, encoded map-reply bytes, final text bytes, per-stage/total cooperative
seconds, new heads/envelopes and caller allowance. chunks is the ordered map
vector. Each chunk is ["map",ordinal,authoritative,before_context,after_context];
each segment in those vectors is [original_unit_index,start_utf8_byte,end_exclusive].
Ordinals start at zero and have no gaps. Context includes selected units only,
is labeled separately and never counts as authoritative coverage. Reject any
non-deterministic/gapped partition. Reducer consumes all ordered map results.

Core excludes output results and actual reducer-input digest to avoid a cycle.
Plan retains all preconstructed map payload digests plus reducer fixed-prefix and
worst-case output reservation; actual reducer input is bound by its fresh prepare
after map results exist. Plan publication and later exact revisions are guarded
separately; historical equality never supplies a fresh grant.

## Stage and transition identities

Map stage_id = U("urn:rmb:writer-notebook-stage:v1:" + operation + ":map:" + n).
Reducer stage_id uses ":reduce:0". n is unsigned base-10 with no leading zeroes.
prepare/finish operation IDs = U("urn:rmb:writer-notebook-transition:v1:" +
stage_id + ":prepare") / the same with ":finish".
Final publication operation = U("urn:rmb:writer-notebook-transition:v1:" +
plan_id + ":finalize"). No timestamp/random actor/root revision changes these IDs.

Model input_digest = H(C(["writer-notebook-input-v1", prompt_revision, parts])).
parts is the exact ordered string vector actually sent via add_text_content,
including effective personalization, instructions and encoded payload; clear
engine content first and send no images. Use notebook-map-v1/notebook-reduce-v1
as appropriate. Any prompt change requires a prompt revision and updated tests.
Freeze one engine/config for the invocation. Provider endpoint/credentials are
not content identity and are never persisted in these inputs.

Fresh stage preparation fingerprint hashes C of:

```text
["prepare-writer-notebook-stage-v1", plan_id, core_digest, stage_id, kind, ordinal,
 archive_id, source_revision, input_digest, predecessors]
```

kind is map/reduce; source_revision is the exact pre-admission archive envelope
revision. predecessors is ordered [stage_id,result_revision,output_digest] triples,
empty for maps. Preparation additionally checks exact root/plan/history guards.
Those expected revisions are not refreshed after a conflict. Its returned cursor
uses exact post-publication revisions, per design.md.

Finish fingerprint hashes C of:

```text
["finish-writer-notebook-stage-v1", plan_id, stage_id, prepared_revision,
 outcome, invoked, output, observed_output_digest, observed_output_bytes, failure]
```

outcome is generated/failed/canceled/uncertain. invoked is a boolean observation,
not provider billing assurance. output is exact accepted text or null. Observed
output digest/count are null when no bytes were returned, otherwise hash/count of
the exact returned UTF-8 text, including rejected oversize text without retaining
its unbounded body. failure is null on generated, otherwise a fixed sanitized
code. Successful output is nonempty; its JSON string encoding fits 4096 bytes for
maps. Non-generated stages never authorize continuation. Receipt fingerprinting
is distinct from envelope revision identity and from an acknowledgment's freshness.

## Export and unchanged legacy recipes

Notebook source_revision = H(C(["writer-notebook-export-v1", archive_id,
source_identity_digest, core_digest, final_draft_id, exact_final_draft_text])).
Only a completed plan/final draft can supply this recipe. Exact envelope revisions
remain separate guards; a no-op revision cannot bless changes to selected facts.

Preserve old Source2 identity exactly: hash C([conversation,turn,document,
TextScope,guidance]), then U("urn:rmb:normalized-text:v1:" + hash).
Preserve old inline export revision exactly: H(C([NormalizedTextSource,
draft.id,draft.text.as_deref()])); there is no added domain separator. Source2
serialized order is id, conversation, turn, document, selection, guidance.

Both paths retain source_scope normalized-document:{document}:page:{page} or
normalized-document:{document}:supplied-notebook. Thus a new explicit generation
of an archive for the same logical document/selection can deliberately re-export
through an already confirmed correlation with new operation/effect identity,
updating the same verified backend note. Old Source2/draft/receipts remain intact;
old refine never silently converts into a multi-call operation. Same scope is
not permission to bypass unresolved effects, source lineage or version guards.

## Literal vectors and implementation checks

identity-vectors.json includes exact canonical/raw bytes and counts, units digest,
archive digest/UUID, empty-history/effective-personalization digests, plan core,
stage/transition IDs, example input/finish fingerprints and both legacy/new export
revisions for one Unicode unit. Raw input has a final LF; canonical media does not.
The legacy and new generations use different operation UUIDs but the same scope.
It also includes a page scope encoding and nonempty-guidance archive variation.
The example input strings are recipe vectors, not approved production prompts.

Future Rust tests must assert these fixed values, old inline preservation and
deliberate same-correlation inline-to-archive update through real Store/destination
paths. Add mutations for source/order/selection/guidance/history/prior/limits,
operation/ordinal/predecessor revisions and prompt text. Test map/reducer finish
acknowledgment loss separately from digest equality. Fixture provenance is this
central versioned file; copying literal test data is allowed, duplicating central
OpenSpec workflow/spec artifacts into a component is not.
