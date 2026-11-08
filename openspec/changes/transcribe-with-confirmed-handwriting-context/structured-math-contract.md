# Explicit structured mathematical transcription

Status: accepted source-design boundary, implemented with local controls;
independent source/hosted review and recognition qualification remain pending.

The current flat partial-text contract cannot preserve a visible fraction or
radical around an unknown child without inventing a complete text fragment.
Add one explicit version 3 request with policy `structured-math-transcription`.
This adds representational capacity. It does not resolve the observed wrong
assignment/membership symbols, prove source coverage or regrade any failed run.

## Admission and compatibility

Keep the existing raw request, duplicate-key, UUID, positive-page, required-null
context, PNG, context snapshot, credential and owned-output boundaries. Only exact
unsigned version 3 plus the exact new policy enters the new branch. Malformed
policy or typed admission retains the existing version 1 preadmission refusal.
After typed admission the report has version 3 and required nullable `partial`
and `structured_math` slots. Versions 1 and 2 keep their current field omission,
admission order, literals and identity bytes. No default or consumer is migrated.

## Bounded response data

One strict response object contains exactly one `pages` entry matching the target.
The existing transcribed, blank, unreadable and partial variants remain valid;
they keep their literal validation rules. Add `status: structured` with `page`
and ordered `spans`. Spans are exactly known text, opaque uncertainty, or a math
root. Require at least one math span; adjacent page-uncertain spans are invalid.

The new prompt must state all accepted legacy response rules itself; a reference
to "existing rules" is insufficient in an otherwise standalone prompt.
Transcribed text is nonempty. Blank and unreadable require empty text. Partial
requires 2..64 known/uncertain spans, at least one nonempty known text and one
uncertain span, and no adjacent uncertain spans. Known page text permits only
tab, CR and LF among controls. A reliably visible mathematical relationship
uses a structured math span even when some of its children are unknown.

Nodes use the following restricted Presentation MathML roles, with ordered
children. This JSON envelope and `unknown` marker are project rules, not MathML
conformance or a standardized recognition-confidence format.

| Node tag | Content |
| --- | --- |
| `unknown` | No payload; one opaque child expression |
| `mi`, `mn`, `mo`, `mtext` | One nonempty literal Unicode `text` token |
| `mrow` | 2..32 grouped children |
| `mfrac` | Numerator, denominator |
| `msqrt` | One radicand; group multiple terms with `mrow` |
| `mroot` | Radicand, index |
| `msub`, `msup` | Base, subscript or superscript |
| `msubsup` | Base, subscript, superscript |
| `munder`, `mover` | Base, underscript or overscript |
| `munderover` | Base, underscript, overscript |

Each math root contains a known token or a known structural node other than
`mrow`. An unknown root or groups containing only unknown leaves are not positive
structure. If attachment is unknown, use an unknown enclosing subtree rather
than choose a plausible attachment. Distinct known slots may have unknown
children. Preserve exact token bytes/order; never simplify, repair, normalize
Unicode, join across uncertainty, close implicit fences or flatten a tree into
a falsely complete text expression.

Use the existing serde/serde_json stack and a closed typed representation.
Reject unknown fields/tags, invalid arity, payload on unknown nodes, malformed
JSON and duplicate keys. Before typed tree deserialization, bound JSON container
depth to 64. Bound each response to 16,384 bytes, page spans to 64, total math
nodes across all spans to 128 and math depth to 8 with root depth 1. Each token
is at most 256 UTF-8 bytes and contains no Unicode control characters. Shared
known page-text/token bytes are at most 4,096. Existing prompt text, descriptor,
result and report limits remain; refuse rather than truncate.

## Identity, results and custody

The profile protocol is 4 with revisions `transcribe-structured-math-v1` and
`transcribe-structured-math-confirmed-examples-v1`. Its extractor prefix is
`notebook-ocr-structured-math-v1:` followed by the existing exact serialized
profile digest. The target manifest uses protocol 3. Use a dedicated prompt and
context literal; the old v2 context/addendum is incompatible with unknown-child
semantics. Keep descriptors/examples in their captured order and the target
image last. Preserve existing target-only source and response digest recipes.

Normalizer-owned provenance supplies document/page/source/profile, extractor,
prompt/response digest and prompt byte count. `structured_math` contains those
fields plus `authority: unverified-historical-page-image-structured-math-ocr`,
ordered spans and derived coverage. Coverage is `partial` if any unknown child
or page-uncertain span exists, otherwise `complete`. Complete means no declared
gap; it is not source coverage or accuracy proof.

The report status is `structured` only for this new branch, with nonnull
`structured_math` and null normalized/partial payloads. Every other success has
only its existing corresponding payload. Refusal, unreadable, failure,
cancellation and output-limit fallback clear all payloads. `confirmed` remains
false. Mechanical success includes a valid structured report, not recognition
acceptance. Keep the existing selected-context lease through actual output and
drop; null context opens no Store. No retry, salvage or automatic downgrade.

Serialize inert JSON only. No XML/TeX execution, renderer, entities, external URLs,
training, source/index allocation, export or native Reader/Writer adoption is
introduced. Older consumers must reject unsupported version 3.

## Acceptance

Production-path tests cover precise version/refusal precedence, legacy vectors,
both prompt identities, exact provenance and lossless structured round trips,
all shared limits, malformed/duplicate/deep replies, whole-page outcomes,
cancellation, output overflow and captured-context ownership. A six-node
fraction whose denominator is a subscripted radical can retain three unknown
children and zero invented glyphs. Wrong attachments and known relation glyphs
can still pass the parser; source-based recognition review must reject them.

Only a new independently reviewed live packet may evaluate recognition. Keep the
existing math failures and successful six-case legacy regression separately
attributed. The unchanged source glyph/attachment criteria still govern delivery.

Source basis: current exact transcription/normalizer source and recorded model
failures; independent reference review `879a5a69` (35 local reference controls,
not product tests); structural roles from [W3C MathML Core, June 2025](https://www.w3.org/TR/2025/CR-mathml-core-20250624/).
