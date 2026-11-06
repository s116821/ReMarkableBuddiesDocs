# Explicit selected Writer caller: contract and local evidence

Historical revision-specific record. Later implementation, live results and the
finite delivery disposition are in [delivery closeout](delivery-closeout.md).
Earlier pending statements below describe their recorded revision, not the final
status; no earlier failure or evidence attribution is overwritten.

Status: implemented and locally checked; Root independent review, current hosted
checks, coordinated delivery and separately pinned selected semantic run remain.
No live model, tablet, native output or export qualification is claimed.

Exact source candidate: `52595dc1941d4a2f57470c5b89065ee9018a94ec`, tree
`a8444f96c2c8db4993f58a42cd9eccdca3d4dbc3`, direct successor to16bb123.

## Caller contract

The existing `--conversation-operation` / `--conversation-input` family adds
`writer-inspect`, `writer-generate`, `writer-refine` and `writer-recover`.
Input can be a safe regular JSON file or bounded stdin (`-`), at most256KiB.
Unknown/duplicate fields, unsupported versions and selector/request mismatches
refuse; the selected adapter never falls into ordinary Writer or Reader runtime.
Ordinary `--writer-note` still refuses selected enrichment.

Inspect input is `{wire_version:1, scope:SelectionScope, conversation:Uuid}`.
It uses explicit group/document-key/binding and the saved Store SharedGroup mode,
not Reader selection or memory configuration. Missing, local-only, isolated or
foreign shared mode refuses. Writer must be enabled and legacy sync disabled.
The response's guarded `data.handles` contains exact expected selection evidence/
raw-head digest, root reference, normalized source references and generated draft
references, all retaining original ObjectRefs rather than reserialized guesses.

Generate/Refine/Recover use this closed envelope:

```text
{
  wire_version: 1,
  expected: {selection: IntentSelectionEvidence, raw_head_sha256: String},
  root: IntentRecordRef,
  refine: null | {source: IntentRecordRef, draft: IntentRecordRef},
  request: existing Writer Request::Generate | Request::Refine
}
```

Request identity remains in the existing Writer Request; root/conversation and
Refine draft references must agree with it. There is no second header operation
ID, serialized live SelectionToken or private fresh model permit. For subsequent
Refine, explicitly use current handles from the acknowledgment/re-inspection;
never silently substitute a newer selection for the caller's expected one.
The in-process library receiver remains available for actual Store-held handles.

The adapter first performs evidence-only historical recovery using the exact
operation/fingerprint, validated selected predecessor, original raw head and
deterministic records. It creates no new records, memory query or model permit.
Completed requests return Historical; prepared-without-finish returns
HistoricalPending; explicit recover with no receipt returns NotFound. Changed
input refuses. These outcomes precede credentials and current-winner admission,
so a later winner or lost acknowledgment cannot turn old work into a model retry.

Only a no-history fresh request compares actual current Store evidence/root/
source/draft/document scope and provider setup before credentials. It then calls
the selected receiver once, without an outer admission gate across model I/O.
Existing preparation gate/one-shot permit, same-Store ownership, exact payload
history byte/turn bounds and joined consuming memory publication remain.

## Report handoff

Reports are bounded complete frames with `native_authority:false`. Fresh current
handles are emitted under selected admission and saved-mode lease, checking the
exact original report payload/token/raw head. Replacement after commit preserves
the original durable draft/receipt/transaction as Historical with handles null;
it never rewrites that publication as an uncommitted failure. Failed/stale fresh
work does not claim a selectable draft or native/export capability.

An attempted partial output error propagates without appending an alternate frame,
retrying emission or invoking a model. The caller recovers the original operation
instead. Historical reports contain no current handles. Every next request still
validates exchanged evidence; current-at-emission is not future membership.

## Observed local checks

Final caller source passes39 Writer integration tests (the36 earlier Writer tests
plus three new caller tests) and three new report Store tests:42 distinct passes.
Subcases and child commands are not inflated. Actual separate CLI processes
perform inspect -> Generate -> exit -> re-inspect -> Refine with two owned
loopback POSTs. They deliberately configure an unrelated Reader selection while
the explicit Writer selection succeeds. Replayed/recovered requests after a later
winning root, pending preparation without finish, unknown operations and request
conflicts exercise no-credential/no-model recovery. Bad selection/raw-head/binding,
unknown/duplicate/oversized input, selector mismatch and competing command flags
refuse. Useful selected memory is present in both real fake-provider requests;
the library's existing full Writer suite retains stale joined-memory controls.

Three actual selected Store report controls prove replacement after publication
keeps the exact draft as Historical/no handles, partial BrokenPipe output does
not replay a commit or append a second frame, and tampered current payload refuses
before output. Existing source, bounds, cancellation, unavailable memory and
consumed-view/commit controls remain covered in the full Writer integration suite.

All-target Windows default-feature Clippy completes with only inherited three
library/nine library-test warnings (two duplicated), no new findings. It is not
a strict Linux/all-features execution receipt. Formatting/diff checks pass.
Evidence resides in `work/rem24-selected-writer-evidence`, final logs25/26/27.
The first compile failure (unneeded Debug derivation) is retained in19; the initial
CLI fixture self-deadlock is retained in20. That fixture held its capture mutex
while counting requests. The exact owned test process was verified/stopped/reaped,
the fixture lock was released before counting, and successor logs21/23 pass.
No product deadline widening or automatic retry was introduced.

Existing16bb123/367dba1 checks and earlier138-count/library/ordinary-live receipts
retain their own source identities; they do not automatically qualify this later
caller. No new cache, copied binary, live key/provider call or tablet operation.
Current exact heads and log hashes are recorded in the canonical handoff.

Remaining: Root exact-pair review/hosted delivery; separately reviewed two-call
selected Generate/Refine semantic plan on the accepted source; selected native/
export/notebook/recognition consumers and effect admission; sync/recovery,
survival and remaining full lifecycle/canonical sync/archive. Delivered Manager
inspect/forget is not reopened. This active subject-memory change stays open.
