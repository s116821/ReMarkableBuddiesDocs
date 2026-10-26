# Exact proposed report schema v1

All objects reject unknown/duplicate fields. Keys appear in the order below;
absent values use explicit null, never omitted fields. Integers are unsigned u64;
UUIDs are canonical lowercase non-nil strings. No raw payload, base64, image bytes,
OS error/path or unknown-domain text is returned. Explicit typed correction text
is allowed only in value. Limits from contract.md/design.md apply to all encoding.

## Outer object

```text
{
 handwriting_version: 1,
 command: null | "confirm" | "update" | "inspect" | "query" | "forget" | "status",
 status: "complete" | "complete-empty" | "partial" | "busy" | "unavailable" |
         "unsupported" | "invalid-input" | "conflict" | "failed",
 failure: null | FailureCode,
 operation: UUID | null,
 transaction: UUID | null,
 record: UUID | null,
 historical: boolean,
 facts: Fact[0..16],
 diagnostics: Diagnostics
}
```

command is null if strict command deserialization did not succeed; otherwise it
is the decoded command even on semantic refusal. operation is the validated
requested operation for confirm/update/forget/status, otherwise null. record is
the derived ID only after both key UUIDs validate (query has null). transaction
is non-null only for this invocation's positively observed successful commit;
all readback/replay/refusal/uncertain outcomes use null. historical is true only
when an accepted requested operation is found, whether via explicit replay or
status; false for inspect/query, new commits and absence/errors. It grants no
mutation or recognition authority.

## Fact

```text
{
 record: UUID,
 revision: UUID,
 parents: UUID[],
 head: boolean | null,
 conflicted: boolean | null,
 state: "value" | "tombstone" | "unsupported",
 value: ConfirmedCorrection | null,
 sample_availability: "available" | "unavailable" | "not-examined" | "not-applicable"
}
```

parents is the envelope's exact ordered parent vector. ConfirmedCorrection has
exactly the fields/order/types in design.md section2, including its exact Media
and provenance objects; there is no additional data wrapper or arbitrary map.
Value metadata is fully domain-validated before state:value. Unknown schema/kind/
identity/shape is state:unsupported, value:null; never echo its raw payload.
Tombstone is only a valid known-key null-payload/empty-media tombstone, value:null.

head/conflicted describe the captured head snapshot or successful commit point,
not a live currentness grant. Inspect facts have head:true and conflicted equal
to captured head-count>1 for that key, including unsupported members. Query facts
have head:true/conflicted:false and include only available supported values.
Observed mutation facts have head:true/conflicted:false. Status/historical-replay
facts are retained observations with both fields null; no extra current-head read
or false non-conflict claim is inferred. Each operation returns at most one retained
fact; an operation colliding with multiple retained revisions refuses as conflict.

Available requires actual hash/size/PNG/dimension validation in this invocation.
Unavailable means required content could not be verified (missing, declared import
omission, corruption or invalid image); it does not guess which cause from a generic
I/O error. Not-examined means no image verification was performed, including all
unsupported values; not-applicable is restricted to valid tombstones. Inspect and
status may expose supported value metadata with unavailable/not-examined state
but then must return partial; they never call it a complete usable example.
Query omits unavailable examples and returns partial. Omitted query metadata
matches have no Fact and no availability assertion. Mutation/replay of a value
must verify its sample; otherwise it refuses as unavailable, with historical:true
only if accepted operation identity was already established.

## Diagnostics

```text
{
 scanned: u64,
 matched: u64,
 omitted: u64,
 conflicted: u64,
 unsupported: u64,
 missing_media: u64,
 mutation_outcome: "not-requested" | "not-dispatched" | "observed" | "unknown"
}
```

scanned counts inspected envelope metadata (not pixels or all Store records).
matched counts supported single-head value keys matching requested profile/text
before output/media selection. omitted counts those matching keys excluded by the
result/output budget, excluding selected examples whose verification fails.
conflicted counts requested-profile keys with multiple captured current heads;
unknown-key/profile payloads instead increment unsupported. unsupported counts
uninterpretable examined handwriting envelopes, without asserting profile absence.
missing_media counts examined supported values whose required content verification
failed; it says nothing about unexamined/omitted content. No estimate is presented
as an exact count. Scanning exhaustion returns unavailable/refusal, not a guessed
matched total. Refusals before scanning have zero counters; known observed counts
may remain on later refusal. Omitted/conflicted/unsupported/missing_media>0 excludes
complete/complete-empty. All diagnostics and mandatory envelope fields count toward
the output budget. Query refusal due to the mandatory header exceeding its budget
uses a fixed bounded failure report under the256 KiB report ceiling, not a false
claim to fit the requested successful-result budget.

## Closed failure-code vocabulary

```text
invalid-json, invalid-version, invalid-identity, invalid-confirmation,
invalid-text, invalid-provenance, invalid-sample, input-limit, image-limit,
invalid-budget, output-limit, unsupported-mode, unsupported-record,
store-unavailable, ownership-busy, heads-conflict, operation-conflict,
immutable-change, media-unavailable, commit-unknown, storage-failure
```

All other internal errors map to storage-failure without diagnostic text. On
stdout failure, return a failing process outcome with fixed output-failure on
stderr and no second JSON; output-failure is not a fictitious delivered report.

## Command/outcome matrix

| Outcome | status / failure | transaction / historical | facts / mutation_outcome |
| --- | --- | --- | --- |
| New confirm/update/forget observed | complete / null | commit UUID / false | one value or tombstone / observed |
| Identical accepted mutation replay | complete / null | null / true | one retained verified value or tombstone / observed |
| Mutation refused before commit | invalid-input, unsupported, busy, unavailable or conflict / matching fixed code | null / false | empty / not-dispatched |
| Mutation commit acknowledgment unknown | failed / commit-unknown | null / false | empty / unknown |
| Status finds exact accepted operation | complete / null | null / true | one retained verified value or tombstone / observed |
| Status finds accepted value with unverifiable media | partial / null | null / true | one value with unavailable / observed |
| Status finds no accepted operation | complete-empty / null | null / false | empty / unknown |
| Status operation/key collision | conflict / operation-conflict | null / false | empty / unknown |
| Status incomplete/unsupported history | unavailable or unsupported / store-unavailable or unsupported-record | null / false | empty / unknown |
| Inspect supported head(s) | complete or partial / null | null / false | all captured heads, partial if conflicted/media unavailable / not-requested |
| Inspect absent key | complete-empty / null | null / false | empty / not-requested |
| Inspect mixed unsupported heads | partial / null | null / false | supported and unsupported head metadata / not-requested |
| Inspect only unsupported heads | unsupported / unsupported-record | null / false | unsupported head metadata / not-requested |
| Query usable subset | complete or partial / null | null / false | verified value facts, partial if any omitted/withheld/unavailable / not-requested |
| Query no matches, complete traversal | complete-empty / null | null / false | empty / not-requested |
| Query has only omitted/unsupported/conflicted/unavailable matches | partial / null | null / false | empty / not-requested |
| Any read output budget failure | unavailable / output-limit | null / false | empty / not-requested; status uses unknown |
| Invalid declared read budget | invalid-input / invalid-budget | null / false | empty / not-requested; status uses unknown |
| Accepted mutation replay missing media | unavailable / media-unavailable | null / true | empty / observed |

Invalid JSON/version/identity/input before an operation/key is established uses
invalid-input/its matching code (unsupported/invalid-version for unknown version),
empty facts, null IDs and historical:false. Busy/unsupported-mode/store-unavailable
before status can inspect history uses unknown; other read commands use
not-requested. A duplicate operation under changed action/heads/content is
conflict/operation-conflict, never historical success. A proved pre-commit CAS
refusal is conflict/heads-conflict, not-dispatched for this submission only;
it does not assert an earlier uncertain invocation was rolled back.

Status stages no blob and calls no commit. Store opening may still perform its
documented recovery writes. An absent status result supplies no permission to
resubmit. A later explicitly invoked mutation may submit exact CAS as specified
in design.md, but must not be called read-only reconciliation or an automatic
retry. Acceptance tests must assert these shapes/nulls/matrices, including status
after simulated lost acknowledgment, absence, later supersession and forget.
