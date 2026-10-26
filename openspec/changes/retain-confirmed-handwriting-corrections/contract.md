# Proposed one-shot transport v1

Invoke --handwriting with the existing explicit configuration option and stdin.
Allow no unrelated command/runtime/device/model flags. This option returns before
normal runtime initialization. Input is one strict JSON object followed by EOF;
no file/URL fallback or line-delimited multiple mutations. handwriting_version
must equal1. Unknown versions produce Unsupported; malformed/unknown/duplicate
fields produce InvalidInput. Fixed sanitized error codes contain no input content.

Commands and their exact fields (required unless explicitly stated):

| command | Fields in addition to handwriting_version/command |
| --- | --- |
| confirm | profile, correction, operation, expected_heads, confirmation, original_text, corrected_text, confirmed_ms, provenance, sample_png_base64 |
| update | Same complete fields as confirm, with nonempty current expected_heads and immutable original/sample/source linkage |
| inspect | profile, correction |
| query | profile, query_text (string or null), max_matches, max_encoded_bytes |
| forget | profile, correction, operation, expected_heads (nonempty) |

All UUIDs are canonical lowercase hyphenated non-nil strings. expected_heads is a
unique array; its canonical fingerprint sorts by UUID text. confirmation is exactly
user-confirmed. confirmed_ms is a nonzero u64 asserted time. provenance has exactly
kind:"caller-confirmed-sample", description, source. source is null or an exact
three-UUID [conversation,turn,source_record] array; nil/partial triples refuse.
Samples and provenance do not qualify page identity or native authority. Definitions
and limits are in design.md; null query_text means all confirmed records in profile.

Reports are one bounded JSON object plus LF. Fields in order: handwriting_version,
command, status, failure, operation, transaction, record, historical, facts,
diagnostics. Nulls are explicit. status is Complete, CompleteEmpty, Partial, Busy,
Unavailable, Unsupported, InvalidInput, Conflict or Failed, serialized kebab-case.
failure is null on admitted successful/partial observations, otherwise one fixed
sanitized code. operation is the requested mutation ID or null. transaction is the
observed commit ID or null; record is the deterministic record ID or null.
historical is true only for a confirmed identical replay, not a dispatch grant.

facts contains bounded typed value/head observations and sample availability, not
PNG/base64 bytes. diagnostics contains counts for scanned, matched, omitted,
conflicted, unsupported and missing_media plus mutation_outcome. mutation_outcome
is not-requested/not-dispatched/observed/unknown. A failed stdout write cannot
prove rollback or produce a second report. Inspect reports exact current heads;
query reports only usable strict confirmed values, never conflicted winner guesses.
All encoding including complete diagnostics fits the caller query bound, or query
refuses with a fixed bounded report. Overall report ceiling is256 KiB plus LF;
inspect is at most16 heads and refuses excess without partial complete-inspect.

Library provider reports carry the same facts and owned guard lifetime; no public
boolean can release required mode/data ownership before actual handoff. This is
an ordinary local explicit command, not a remotely queryable Buddy service.
