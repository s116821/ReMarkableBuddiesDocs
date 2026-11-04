# Proposed opt-in partial transcription v2

Review-only proposal in the existing Buddy #105 and Docs #108 change. Baselines
are Buddy 846366943de69b70acd547835fa7bc0eba5af1c2 and Docs
e33a2703680730c63792f83635dc7d91dc70049a. The v1 contract and spec delta govern
until this option is accepted. The spent r2 recognition result remains NOT MET
with all eight calls spent.

## Request and model reply

Use the existing exclusive stdin operation. Select v2 only with
`"transcription_version":2,"policy":"partial-transcription"` in the same strict
envelope, keeping the original required nullable context. The v1 envelope
still rejects the extra key. A v2 envelope missing the policy, providing any
other value or containing extra or duplicate fields fails before image
admission, Store access or dispatch. Parse strict JSON once and decode the
specific envelope. Keep the original failure precedence and report bytes for
legacy and unrecognized envelopes. Once the complete v2 envelope and positive
page are accepted, emit v2 reports for all subsequent outcomes. No saved
preference, context selection or automatic caller can enable the policy.

The v2 prompt and its context addendum have separate immutable revision
strings. Do not append v2 instructions to the legacy prompt, whose base and
context suffix both demand whole-page abstention. Keep target last, examples
in exact requested order, content labeled as untrusted and only one provider
method entry. The v2 prompt asks for directly legible visible text in reading
order. It forbids completion from examples or background knowledge. It marks
each uncertain run explicitly and says to abstain if no text is reliably
legible. It never instructs the engine to force a partial result.

The v2 reply still has exactly one `pages` array entry with the exact positive
requested page. Decode a v2-only status-discriminated entry:

| Status | Exact entry fields | Meaning |
| --- | --- | --- |
| transcribed | page, status, text | Model proposes all visible text as legible |
| blank | page, status, text | No visible text and text is empty |
| unreadable | page, status, text | No reliably legible text and text is empty |
| partial | page, status, spans | Both reliably legible and uncertain text are present |

A partial entry has 2 to 64 ordered spans. Each span is exactly
`{"kind":"known","text":"<verbatim visible text>"}` or
`{"kind":"uncertain"}`. Require both kinds and reject adjacent uncertain spans
so one uncertain run has one marker. Known spans may preserve leading/trailing
whitespace but may not be whitespace-only. Preserve exact Unicode and spacing
within each span. The known text shares the existing aggregate 4096 UTF-8-byte
page ceiling and control-character policy. Uncertain spans carry no candidate
text, invented glyph count, confidence, coordinates or example provenance.
Reject wrong variants, page, type, null, unknown/duplicate fields, excess
length or malformed spans as invalid-response. No trimming, joining, repair or
partial salvage. All target, image, prompt, response and report bounds remain
unchanged. No new filesystem or credential input.

## Report, identity and boundaries

V2 uses the existing report fields with `transcription_version:2` and one
additional required nullable `partial` field. V1 serialization has no extra
field, even when null. Complete and blank v2 replies use the existing
normalized result shape with v2 identities and the existing unverified authority for the applicable context branch. Unreadable has neither result.
Partial emits `status:"partial", failure:null, provider_attempt:"called",
result:null, confirmed:false`. Its `partial` value has exactly `document`
(caller UUID), `page`, `source_sha256` (existing target-only image-set
digest), `profile`, `extractor_revision`, `authority`
(`unverified-historical-page-image-partial-ocr`), `prompt_sha256`,
`prompt_bytes`, `response_sha256` and the typed ordered `spans`.
The outer report continues to carry the exact target PNG digest and any
captured correction descriptors. Neither representation grants source ownership
or confirmation. A valid partial report exits zero for operation completion,
while callers must read the status to distinguish partial from normalized.
Report overflow clears both result slots and emits the same bounded output-limit
failure, preserving only already admitted descriptors and attempt facts. Stdout
failure retains ownership until write/flush/error/drop and emits no second report.

Proposed v2 identity pins are manifest `{"protocol":2,"pages":[PAGE]}`, profile
protocol 3 for both v2 context branches, prompt revisions
`transcribe-partial-v2` and `transcribe-partial-confirmed-examples-v2`, and
extractor prefix `notebook-ocr-partial-v2:` plus the existing canonical profile
hash. Keep the ordered selected-context descriptor recipe. Revision-only
selection changes extractor identity but cannot change an otherwise identical
payload digest. Target-only source and PNG hashes do not change when policy or
context changes. Review exact serialized identity vectors before code.

| Existing seam | Proposed boundary |
| --- | --- |
| `handwriting_transcription::Prepared::admit`, `Request`, `Report::new/fail/write_to` and `main`/command dispatch | Decode a version-specific envelope and report. Preserve v1 write bytes and pre-admission failure facts. Keep the ownership guard held through either report path. |
| `Prepared::capture/execute`, `ConfirmedContext`, `LocalCorrections` | Reuse the existing target/context admission and capture, without profile-wide lookup or fallback. Select v2 by the admitted request, not by the context. Map typed outcomes into mutually exclusive report fields. |
| `retrieval::notebook::normalize`, `normalize_admitted`, `normalize_inner`, `Response` and `Normalized` | Keep public normalizer and v1 prompt/profile/parser behavior exact. Use a private v2 entry and parser and reuse the bounded image/payload/dispatch/progress machinery where it leaves legacy bytes exact. Build a partial report type without constructing a `NotebookText`, `NormalizedDocument` or `SourceUnit` for partial. |
| Writer supplied normalized sources, `writer::Report::PreparedExport` and `note_export::PreparedNote` | There is no implicit partial adapter, source registration, draft, cache, indexing or export hook. `result:null` and the distinct partial type prevent a partial response from satisfying the normalized input contract. No text flattening or marker substitution. |
| `handwriting::ConfirmInput` and the existing explicit confirmation command | Captured examples stay read-only. No candidate can become a correction through this command, including partial, canceled or complete output. Existing deliberate user-confirmed sample admission remains separate. No record, schema, sync, learning or rollback change. |

## Qualification before delivery

1. Review the strict wire shapes, failure precedence, identity recipe and
   exact prompt/addendum before implementation. Freeze legacy request,
   report, prompt and profile vectors for no-context and selected-context and
   the default notebook normalizer. Freeze separate v2 vectors, including
   a revision-only/payload-stable control.
2. After approval, exercise real Store/CLI admission and bounded fake engine
   controls. Include v1 rejects partial, invalid v2 opts never call, v2 full,
   blank, unreadable and partial in both context modes, malformed variant and
   span combinations, foreign page, overflow, controls, attempt count,
   cancellation at every existing boundary, lost output, held ownership,
   no mutation and no export/confirmation consumption. Keep scripted
   protocol evidence separate from recognition.
3. Before requesting any fresh execution, separately freeze a method and
   independent ground truth tied to the already retained r2 targets and
   conditions. No changed fixture, model, easier replacement, budget or
   execution is authorized here. Compare v2 no-context and selected-context
   on identical targets. Score known-span facts within each span without
   concatenating across uncertain markers. For mathematics, the existing
   three literal logarithm facts must be legible and no known span may
   invent or repair unsupported text. On blank, require empty blank
   regardless of context. On the ambiguous Howe sample, report permitted
   abstention separately and reject contamination. Keep Hunter selected
   facts and all visible misreadings explicit, including prior date,
   terminal hyphen and printed initial observations. A partial label or
   all-unreadable result does not satisfy positive recognition. Review
   omissions, hallucinations, abstentions and degradation independently.
4. Retain any newly authorized run as separate policy-v2 evidence. It cannot
   pass or regrade r2, demonstrate adaptation from a same-page pair or
   substitute for real pen/native and broader Reader/Writer evidence.
   Reconcile and archive the existing paired change only after its required
   source and independently reviewed semantic gates are satisfied.
