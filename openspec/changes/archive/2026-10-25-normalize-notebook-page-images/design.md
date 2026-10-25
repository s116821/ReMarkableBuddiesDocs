## Status and ownership
Unimplemented precode. Central Docs owns this contract; Rust owns an explicitly
invoked retrieval::notebook adapter and maintained example. Existing selected,
Reader cancellation, personalization and Manager drafts retain their owners.
Baseline ingestion is distinct from confirmed-correction learning. The public
roadmap requires indexed handwritten notebooks where feasible; normalized-source
index/cache contracts already preserve declared provenance without extraction
fidelity or native authority.

## Inputs and historical source identity
Accept a nonnil caller document UUID, an ordered borrowed list of PNG byte slices
with positive unique caller page numbers, a caller-declared nonempty model/profile
identifier (at most 128 UTF8 bytes, no controls), options, exclusive mutable
LLMEngine and fallible progress callback. Page numbers need not be contiguous or
sorted: list order is the declared reading order. No paths, device handles,
filenames, network download or native-file identity are accepted by the adapter.

source_sha256 is SHA256 over an unambiguous byte sequence: ASCII domain
`notebook-page-image-set-v1` followed by a zero byte, u32 big-endian page count,
then for every ordered page its u32 big-endian page number, u64 big-endian PNG
byte length and exact original PNG bytes. The document UUID remains a separate
key field. This identifies the provided historical image set and mapping, never
the original native notebook file, full notebook completeness or current device.
No image is silently cropped, resized or re-encoded by the adapter.

extractor_revision is `notebook-ocr-unverified-v1:` plus a lowercase SHA256 of
the deterministic serialized profile containing protocol version, fixed prompt
revision and exact caller model/profile identifier. The prefix visibly preserves
origin in existing IndexKey, DiskCache and Retrieved without a wire-schema change.
The model identifier is a caller assertion, not engine attestation. The returned
report also exposes that profile and each original image digest/location. A
NormalizedDocument uses format Notebook, the above source digest/profile, and one
SourceUnit per page with exact caller page and no fabricated native section.
normalized_sha256 continues to bind admitted model text through Index::build.
Changing bytes/order/page mapping, profile or normalized text invalidates the
applicable complete key. Existing independently selected exact-key checks remain.
Unverified origin is never upgraded by caching, retrieval or downstream citations.

## Admission and finite work
Use existing image/base64/serde/hash dependencies only. Admit all inputs before
the model: 1..4 pages, at most 8 MiB PNG per page and 16 MiB total; positive
dimensions no greater than 4096 per side, at most 8 million pixels per image and
16 million total decoded pixels. Require PNG format and actually decode every
image with explicit image decoder allocation limits (at most 64 MiB each), after
dimension checks. Reject corrupt data and unsupported animation rather than
quietly choosing one frame. Sequential decode drops each decoded image before
the next; encoded original bytes stay caller-owned. Check all arithmetic.

Options can lower, never increase fixed ceilings; zero or inconsistent positive
bounds refuse. Bound the complete deterministic ordered engine-content JSON
descriptor, including image base64 strings and fixed instructions/manifest, to
24 MiB. Expose its digest and exact encoded byte count. This is a byte budget,
not a model token/window/billing estimate or complete HTTP envelope. No generic
token count is invented for images. An existing engine may apply its own stricter
provider/response limits. Raw returned UTF8 is capped at 128 KiB, per-page text at
32 KiB, total text at 128 KiB and complete returned report at 256 KiB; all are
checked before success. Existing Index bounds still apply independently.

Exactly one engine invocation for the whole admitted set; no repair, retry,
fallback or per-page hidden continuation. Existing engine-internal behavior is
separate. Work is bounded by admitted images/bytes and one call, not a promise of
hard wall-clock interruption for arbitrary engines. The maintained existing
OpenAI caller selects a timeout of at most 90 seconds, with no adapter-owned
background worker. Provider max-completion-token truncation must refuse at strict
response admission; it is not partial success.

## Model boundary and refusal
Clear existing engine text/images before any fallible admission; scoped ownership
clears on success, refusal, error and unwinding, assuming clear_content itself
does not panic. No old prompt restoration or physical/remote erasure is claimed.
Send fixed transcription instructions, a deterministic page-ID manifest, then
each original PNG with its page association as ordered content parts. Existing
OpenAI uses PNG data URIs; JPEG input is refused instead of mislabeled.

Instructions treat visible image text as data, never commands; transcribe visible
printed and handwritten text without completing from background knowledge. Do
not pass an expected transcription, source title/URL, date, answer hint or query
to the model. Preserve reading order and uncertainty. Response is strict JSON
with exactly `pages`, an ordered array of objects with exactly `page`, `status`
and `text`. Status is `transcribed`, `blank` or `unreadable`. Page mapping/count
must exactly match the manifest; no duplicates/reordering/extra fields, duplicate
JSON keys, fences or partial JSON. Transcribed text must be nonempty and bounded;
blank/unreadable text must be empty. Blank is an explicit model assertion,
never independently established. Any unreadable page refuses the entire result;
no successful partial document or cache write. Reject unsupported text controls.
No confidence number is treated as proof of completeness or recognition fidelity.

Progress checkpoints occur before/after each decode, before dispatch, during the
existing engine's cooperative progress, after response and before return. Latch
callback failure even if an engine swallows it. No successful result follows a
latched or late cancellation. Arbitrary synchronous engines cannot be forcibly
preempted; the default execute_with_progress only checks before execute. The
adapter writes no source, durable evidence, cache, credential or temporary files.
Return errors without source/model text, paths, credentials or provider bodies.

## Actual maintained consumer and evidence
A maintained example takes explicitly supplied historical PNG paths/page mapping,
declared model identity and query, invokes the adapter with the existing engine,
builds Index, captures its exact key independently, installs normalized material
into a temporary owned Store/DiskCache, drops/reopens it, then queries by retained
key through the actual Provider. Record bounded original-image/profile/prompt/
response/normalized/key/result digests and exact page/range correlation. Retain
raw returned text only in an explicitly requested private create-new report;
default console is sanitized pass/fail. Require explicit live opt-in; credentials
remain in the already-approved protected current-directory environment. Never
retarget a configured nondefault endpoint/model silently. Local HTTP controls use
dummy keys, isolated env and joined servers; no external request in fixtures.

Candidate genuine fixture: [NPS manuscript asset](https://npgallery.nps.gov/AssetDetail/c922fc45-34de-492d-802e-2080de9b466d),
M. J. Sherman to Alice Mary Longfellow, 24 January 1900. The primary asset marks
Public domain; credit Courtesy of National Park Service, Longfellow
House-Washington's Headquarters National Historic Site; Archives Number
1007.001/002.003-001#085. Original JPEG SHA256
6c309acb4749bc3123e0a8cba1544f6229b5b24975e40c48ddab80a05572b53c;
1822x2324 RGB PNG SHA256
a4a5b635299491db594d2a69f9dacb731060f757f1c69573fe3e320fe2085f32
(3,147,147 bytes). Conversion decodes JPEG to RGB and losslessly encodes PNG,
without crop/resize/retouch or generated handwriting. Retain reproducible
preparation, attribution and fixed fixture bytes in Source. Main inspected the
scan itself: handwritten body plus printed letterhead. NPS transcription omits
printed header detail and is a reference, not exact full-page ground truth.

Before a hosted call, independently inspect expected body facts (Mattie Walden,
second year in Junior class, studies, Hampton) and define query/page/range checks.
The single bounded hosted observation must be read semantically, with errors and
uncertainty retained; mechanical keyword flags alone do not qualify recognition.
It is a narrow historical handwriting observation, not a general accuracy study,
proof of model nonmemorization, native notebook support or live Reader acceptance.
Synthetic controls remain separately labeled. No tablet action is required.

## Verification and coordinated delivery
Local adversarial controls cover image/container/decode limits, duplicate/invalid
locations, digest boundary/order/mapping collisions, profile changes, strict JSON,
all-page/unreadable/blank rules, engine cleanup across every exit/unwind,
cooperative/late/swallowed cancellation, complete input/output bounds, malicious
image instruction handling contract, exact Index/cache reopen/query, stale key and
failed replacement preservation. HTTP/example controls verify actual ordered PNG
wire parts, no hints/expected text, explicit opt-in/config, safe report creation,
provider/invalid/truncated responses, cancellation and successful full pipeline.
Model robustness against embedded instructions remains an observed behavior,
not proven by prompt-string assertions or synthetic transport tests.

Freeze exact paired revisions, run relevant strict lint/default/integration and
example checks, obtain independent implementation review, then sync only this
owned canonical capability and archive after completed qualification. Separate
final paired review precedes normal Docs-first squash, actual-main CI and new
official Source publication. No replay of closed observations, held-body edits,
new settings/resources or archive of another lane's work.
