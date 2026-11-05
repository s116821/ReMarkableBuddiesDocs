# Optional ordinary Writer memory: contract for review

Status: proposed, no implementation or new model/native qualification.

## Existing state and boundary

The owning pair is `epub-normalization_rust-rem25` at dd5b05d and
`epub-normalization_docs-rem25` at a2469b7. Writer has no subject-memory consumer.
Its ordinary receiver already preserves exact request/history/source JSON and
uses fresh WriterPreparation plus finish_writer CAS. Reader memory, selected
Provider seals, and REM-37 joined Reader admission exist; none supplies selected
Writer publication. Local Provider::with_current is a compatibility continuation,
not a local snapshot-currentness seal. Do not describe it as stronger protection.

Reconcile delivered ordinary Writer precedence before implementation. Root's
combined preference source is8dd025d with receiving/test blobs preserved from
live-qualified34fe4de. Do not regress that prefix, repurpose its live receipts,
change frozen notebook prompts/plans, or alter the pending REM-26 qualification.

## Proposed first receiving slice

Use existing memory Configuration/Provider/LocalMemory, QueryResult and Store.
Memory stays disabled by default. An absent/disabled configuration performs no
memory read and preserves existing model parts and behavior. PrepareExport
remains model-free and performs no memory query. Empty usable context adds no
part. Use a separate optional receiving entry/options seam, preserving existing
run/run_owned callers until they explicitly adopt this scope.

For explicitly enabled ordinary generation/refinement, query once after fresh
Writer preparation, scoped by its immutable normalized source document and the
exact new request. Do not query from or rewrite past turns. Keep Query's existing
2048-byte text bound; a larger enabled query refuses enrichment rather than
silently cutting the current request. Default to8 matches/8192 encoded bytes,
within existing domain maxima. Keep the existing96 KiB source/history payload
limit separately. Do not drop source/history to make room for memory.

Pass usable Complete or Partial facts only in a separately labeled, bounded
ASSOCIATIVE_MEMORY part with author-asserted provenance/revision metadata. A fixed
receiving policy gives current explicit request and current source precedence;
memory grants no actions or permission and cannot rewrite source, transcription,
export/module settings or conversation roles. It stays separate from the saved
preference and from the exact JSON payload. Do not auto-extract learned facts.

Unavailable/query/encoding/unsupported configuration failures refuse before model
dispatch. An enabled Partial result without usable facts fails explicitly;
Disabled/CompleteEmpty preserves the baseline. A failure after fresh preparation
records a truthful Failed result only while its exact Ledger guards remain valid.
Cancellation/stale ownership publishes no late Generated draft. Provider failure,
invalid output and interrupted/uncertain commit retain existing outcomes and
historical replay behavior; never retry a model request automatically.

## Selected admission and consuming publication

The proposed ordinary slice admits local memory only. Explicit selected-memory
configuration or a selected QueryResult refuses before provider use; it MUST NOT
fall back to LocalMemory or ordinary all-history interpretation/publication.
This is an explicit bounded cut, requiring Root review, not full Writer/selected
completion of task3.1.

The actual ordinary consuming operation remains Ledger::finish_writer under the
fresh preparation's root/source/selected-draft guards and same-Store Writer owner.
No preflight boolean or no-op callback replaces that CAS. The local context is a
labeled retrieval snapshot; this slice does not claim atomic revalidation of all
local memory changes across model I/O. If that stronger freshness is required,
review a typed local snapshot/conditional-publication seal before implementation.

A later selected Writer consumer must supply exact acknowledged Writer input and
selection pins, and join its consuming Writer publication with the memory catalog
and queried aggregate admissions in one canonical ordered set, following the
REM-37 joined publication primitive. Revalidate provider instance, payload/raw
heads/tokens, cumulative budgets and fresh Writer ownership at the actual write;
consume uncertainty once. Never wrap a gate-reacquiring Writer/Store callback in
Provider::with_current. This requires an explicit selected Writer domain write,
not changing the ordinary receiver into an implicit selected path.

## Focused acceptance controls

1. Actual receiver and command: absent/disabled/empty memory has byte-identical
   parts/results, including delivered personalization precedence; PrepareExport
   makes zero memory/model/destination calls.
2. Enabled Generate and Store-reopened Refine: exact labeled facts appear once,
   source/current request/history remain byte-exact, and the selected draft and
   original source retain their identities. Test distinct document/global scopes.
3. Bounds and failures: overlong query/encoded context, unavailable or empty
   Partial view and query failure make zero model calls; no memoryless fallback.
4. Current-source conflict: capturing engine sees fixed precedence and separate
   data. A later bounded real-model gate must independently score useful context
   and a conflicting/stale instruction; Reader live evidence is not a Writer pass.
5. During model wait/finish: cancellation, root/source/draft replacement, write
   failure, lost acknowledgment and repeated invocation cannot publish a late or
   duplicate Generated draft; preserve the failed evidence.
6. Selected catalog/configuration, foreign providers and restored/shared modes
   refuse before ordinary side effects. Keep selected ownership and recovery
   work open; add actual joined-gate tests only when that separate consumer exists.

Root review must confirm this local ordinary cut and the stated snapshot-freshness
boundary before code. Whole REM-24 sync/recovery/native/local-survival and lifecycle
remain open; delivered Manager inspect/forget work is not reopened here.
