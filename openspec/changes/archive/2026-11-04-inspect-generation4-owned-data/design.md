# Decisions

## Separate selector and type

`--inspect-owned-data-v3` explicitly requests report3 for supported generation
formats1/2/3/4. `--inspect-owned-data` remains byte/schema compatible report1/2,
including its generation4 unsupported/null behavior. Reject both selectors
combined, all other one-shot/runtime/model/input selectors, operands and unknown
arguments before any effect. Report3 dispatch precedes normal Reader, Writer,
provider, sync and device construction. It accepts no stdin/path/filter/UUID.
Use the existing fixed nonsecret configuration selection; configuration failure
returns a small report3 unavailable result without raw diagnostics.

Prefer a new `storage/inspection_v3.rs` module and separate report types; reuse
reviewed low-level bounded helpers only after ownership review. Do not change
shared envelope/domain codecs or widen released report enums. The implementation
must demonstrate unchanged report1/2 fixtures, not merely source resemblance.

## Exact counters without JavaScript rounding

Report3 counts are canonical unsigned decimal strings in0..18446744073709551615.
Byte aggregates additionally allow null when checked arithmetic cannot represent
the observed aggregate. This is an explicit new version, not a changed meaning
for report1/2 numbers. Manager validates lexical form/range before conversion,
uses lossless formatting and never turns a large value into an IEEE754 number.
No exponents, fractions, signs, leading zeroes or whitespace are accepted.
Checked overflow records byte-count-overflow, makes the affected byte aggregate
null, keeps independently known counts and disallows a complete total. Saturating
u64::MAX is not an observed count. Complete requires an exhaustive supported
scan with no issues, a consistent final witness and known additive totals.

## Existing-file custody and bounds

The supported producer is Linux with verifiable existing-file/directory custody.
Other target/custody guarantees refuse with unsupported-platform or the existing
lock/unsafe-path codes. Both Manager host OSes invoke the Linux tablet CLI;
Windows native filesystem inspection is not claimed.

Open only validated disjoint data/cache roots and the existing regular store.lock.
Acquire its nonblocking OS lease; never create or repair it. Hold stable directory
and file handles with no-follow/nonblocking admission before reads; reject unsafe
components/reparse paths and changed bindings rather than reopening by path.
Retain lease through bounded serialization and final owner/CURRENT/lease/feature
witness. No Store constructor, recovery, service operation or cleanup is allowed.
Out-of-band changes may make inspection partial; this is not an atomic filesystem
snapshot, physical power-loss or Windows directory-sync claim.

Retain the existing4096entry,1MiB individual record and8MiB cumulative metadata
read budgets. Charge every validation reread and traversal, including contract,
feature and capability checks; no pure validator bypasses the budget. Source JSON
media is sized from metadata, not parsed/read as source content. Emit one compact
UTF-8 JSON object and one LF, at most32768bytes including LF; no stderr content or
private path is forwarded. Budget exhaustion is sticky and no complete total
survives. Host deadlines/framing remain bounded by the existing qualified host
contract; actual current adapter limits must be pinned before implementation.

## Generation and descriptor validation

Validate each current/retained generation independently, not only CURRENT.
Recognize notebook-feature.json, contract-v3.json and current capabilities3 through
budgeted read-only validation. Retained generation4 validates its own actor/
generation feature binding without requiring it to equal CURRENT. Invalid,
foreign, pending or incomplete feature state cannot produce a complete total.

Classify exact Value-only Source3 ArchivedNormalizedSource and Conversation3
NotebookPlan/NotebookStage metadata with the delivered typed decoders. Validate
record reference lengths/digests and exact media-descriptor/manifest coverage.
Do not call notebook mutation/recovery validators that load media or construct
Store/Index ownership merely to calculate sizes. Accounting completeness is
metadata coverage, not full notebook semantic/media integrity qualification.

Feedback schema1 remains supported within a validated generation4 feature
composition. The old inspector's literal format==3 feedback-envelope check cannot
be copied unchanged into the successor. Preserve older Source1/2 and native
Conversation2 contracts; unknown future payloads remain unclassified/partial,
not silently ignored. Namespace/category matching is explicit.

## Nonadditive references and notebook breakdown

Count actual stored files once per generation/path; identical content in another
generation is another stored file. Distinct references within a namespace are
nonadditive. A shared object is counted once physically and separately under each
referencing namespace, with shared-byte evidence explicit. Hard links retain the
stated apparent-file-length-per-owned-path basis, not allocated-byte accounting.

Notebook breakdown is a subset of Source/Conversation metadata, keyed by exact
archived-normalized-source/notebook-plan/notebook-stage. Deduplicate repeated
retained revision references by generation/hash. These are observed record files,
not live notebooks, pages, model calls, successful requests or visible turns.
A missing category is uninspected; complete scans may explicitly show zero.
Never add notebook subtotals to namespace/storage totals.

## Both Manager consumers

Add a disjoint report3 parser/type/request branch; preserve report1/2 branches.
The explicit notebook-inclusive inspection uses only the fixed v3 CLI on an
identity-verified wired target. The old inspection path remains available for
qualified older installations; unsupported v3 is shown honestly, without ordinary
Reader startup, alternate filesystem scraping or silent zero/fallback totals.

Both browser host helper and Electron main/preload factory must provide the same
reduced validated report3 semantics. No raw text/errors, paths, source content,
credentials or arbitrary renderer commands. Validate UTF-8/framing/duplicates/
closed keys and decimal strings before report admission; do not parse malformed
numeric text into healthy zero. Retain connection/boot/request epoch fences,
Busy-before-I/O, finite cancellation/late-result ownership and protected-view
clearing. Pin the actual current adapter and exclusion interfaces before implementation;
compute peer controls from tested source, never invent a matrix count.

# Alternatives

Widening report2's format enum or translating its unsupported result into report3
would invent support. Inferring model calls from NotebookStage record counts
would confuse preparation/results/replay. Loading archived notebook JSON to prove
media integrity expands the observer into a different contract. These are not
selected. A numeric JSON counter representation would require either an unsafe
JS conversion or a new safe-integer ceiling; the proposed decimal strings avoid
both and are an explicit precode decision for independent review.

# Delivery

Independently review concrete producer/schema/vectors and affected source scope
before implementation. Implement producer and both Manager consumers in
coordinated component PRs plus this same Docs PR. Keep compatibility and consumer
availability explicit. Reconcile reviews and meaningful exact-head qualification,
sync only these named canonical requirements, archive completed work and deliver
normally. Precode validation is not producer/host/native behavior qualification.
