# Design

## Baseline and boundaries

Buddy main `cc317ff53e1dd6f612b2e82707e5a5e4b50e0265` and Docs main
`6f7f1d4cb33ff4ca9c0326b1bb248ddc8cfd139e` supply the delivered historical
Ledger. The native investigation and protected selected-admission work are not
dependencies or copied inputs. This increment consumes explicitly prepared note
content; it does not infer handwriting, choose a page, call a language model or
export anything merely because the service starts.

## Stable association and per-export attempt

Keep one ExportAssociation record per stable correlation. Conversation, backend
and source scope remain immutable. Add an optional, backwards-readable attempt
payload: effect operation UUID, action, exact desired-body digest, candidate or
verified destination ID, and previous exported-body/version facts when updating.
Old records without that payload retain their historical semantics; an unknown
prior body does not become permission to overwrite a remote note.

Attempt-bearing export envelopes use export domain schema 2; existing schema 1
records keep their original shape/meaning. Decode schema 2 only for a validated
attempt-bearing Export record, and reject cross-schema shapes. Generic Store
format remains 1. Older consumers refuse the unknown domain version rather than
silently treating a new attempt as an old terminal association.
The delivered Store validator and offline JSON schema currently admit only domain
version 1. Extend both explicitly to version 2 only in ExportAssociation; all
other namespaces remain version 1. Store keeps the payload opaque; the Ledger
enforces the schema-two Export shape. Older consumers/companions must refuse this
unknown domain version rather than claim compatibility from envelope format 1.

Store transition command IDs are distinct from the external effect operation.
Derive preparation/completion/reconciliation/cancellation command IDs from the
effect UUID and fixed stage names. Retain all old Store operation receipts.
Completed may start a new Prepared cycle only with a distinct effect UUID,
expected current root/export heads and the previous verified note identity/body
facts. Source revision may change only at this new-cycle boundary. Within a
cycle, its scope/revision/action/content/baseline are immutable. A terminal
Canceled/Failed attempt may start a fresh deliberate UUID only when the attempt
positively records no dispatch; this is distinct from every post-dispatch or
crash-uncertain state. Retain its old receipts. An uncertain cycle cannot be
silently replaced by another operation.

The existing commit/replay implementation always returns a historical receipt,
including after a fresh commit. Add export-specific fresh-commit disposition at
that boundary without changing historical acknowledgments. Only a successful
new local preparation commit permits the current invocation's single dispatch.
A replay, concurrent identical winner or committed-but-lost acknowledgment must
reconcile instead. This disposition is neither native permission nor a durable
lease that can be replayed after restart. Store CAS still rejects stale heads.
Ledger envelopes carry freshly generated revision/operation IDs for each commit;
do not generalize Store's generic identical-transaction Ok replay into dispatch
authority. Derived stage-command fingerprints remain immutable. Read-only
unresolved reconciliation need not overwrite a stage receipt with new observations.

One narrow in-memory export owner shared by all Ledger instances of the same
Store covers the complete prepare/dispatch/result or reconciliation invocation.
Use a nonblocking atomic guard, released on every exit; a concurrent invocation
returns Busy with no dispatch. Conservatively serialize exports within that Store
rather than add a per-note worker registry. This owner is separate from the Store
index/commit mutex, which is never held over HTTP. The OS lease still excludes
other Store processes; no owner state is reused after process restart.

## Destination contract and identity

Use a small replaceable interface for discovery, read and one create/update.
Destination capability selects the existing metadata key when actually supported
or the existing exact title token otherwise. No fuzzy title/prefix matching or
second registry. Every selected note must have the exact correlation token;
malformed or duplicate markers refuse. The verified native ID and exact full-body
digest bind readback to the immutable local attempt's conversation/source scope
and revision. Keep machine identities/per-effect facts in the Ledger without a
redundant visible JSON footer or assumed remote metadata fields. Preserve prepared
Markdown and its useful human-readable source/page/coordinate provenance.
User-provided title/body remain content, never destination selection instructions.

Discovery returns Unique, Missing, Duplicate or Incomplete explicitly. Mem uses
bounded cursor listing with the same filters/order, exact token checks and
verification by native ID. Search's relevance-ranked 100-result window cannot
prove absence. Cap exhaustion, repeated cursors, malformed rows, trash, identity
changes or failed reads refuse a unique/absence claim. A stored ID is a lookup
aid; verify its marker and current body before using it. Listing is an observed
bounded discovery, not an atomic account-wide uniqueness guarantee.

For a first create, persist a new candidate UUID and exact body digest before
one POST. A caller-provided UUID is not an assumed duplicate-POST guarantee.
For an update, GET the verified ID and require the remote body to match the last
confirmed exported body before PATCH with the exact returned version. A changed
remote body/version is an explicit conflict requiring deliberate refinement;
do not merge unrelated edits or overwrite them as a synchronization fallback.
The full desired body is submitted because Mem does not accept a markdown patch.
If the exact desired body is already present at the verified ID/marker with a
consistent version, record a verified-current result without another PATCH.
Completion means the destination was observed to contain the desired content;
readback does not prove that a particular HTTP call executed. Changed desired
content requires a version above the previous baseline; identical content may
retain the baseline version. No mutation is inferred from that equality.
Successful responses/readback must match the intended ID, correlation, body and
valid version before persisting Completed. Never select an arbitrary duplicate.

## Uncertain effects, restart and cancellation

Durably prepare before calling the transport. A timeout, lost/malformed response,
conflict response, cancellation after dispatch, or failed completion commit leaves
an explicit reconciliation outcome. Reopen reads the known candidate/native ID;
matching marker and exact intended body may confirm completion without another
write. Missing or differently edited state stays unresolved/conflicted. It never
licenses automatic replay of the write, including a duplicate create POST.
An identical completed operation returns its historical result; a new deliberate
export operation may start the next revision only from confirmed state.

Cancellation observed before dispatch records a no-effect cancellation. Once
dispatch may have happened, cancellation cannot claim to undo it. Confirmed
success remains exported; otherwise report reconciliation required. Use the
existing original operation bounds and responsive cancellation signal; never
renew a request clock or retry a side effect automatically.
Before-send cancellation is not a permanent terminal trap: a later deliberate
new UUID may export the same stable association under current heads, without
replaying the canceled effect. If a prior attempt was Prepared when the process
died, lack of a sent flag is not positive no-send evidence; reconciliation remains
mandatory.
Write-future construction is non-effectful by the destination contract. Track
the first poll separately so cancellation/expiry winning before that poll is
positive no-send evidence; entering the first poll is only a conservative
may-have-dispatched boundary, not proof that the network request executed.

## Real Mem adapter and limits

Use current documented `/v2/notes`: first Markdown line is title; POST accepts
an optional UUID; GET returns current body/version/trash; PATCH submits full
content plus exact version. No arbitrary metadata field is declared, so Mem uses
the title-token path. Bearer credentials come from a private environment/config
reference, never stdin reports, command-line arguments or logs. Production uses
the official HTTPS origin; local test HTTP is an explicit fixture constructor.
Disable redirects and automatic request retries. Bound request time, each body,
response bytes, cursor length and page count; incomplete discovery refuses.
Apply Mem's 200,000-byte create ceiling to the complete generated content.
Expose typed, sanitized outcomes without leaking private note bodies or tokens.

Initial bounds: 256 KiB command input; 256-byte single-line title; 1024 bytes each
for source scope/revision; 1 MiB per HTTP response; 4096-byte cursor; at most 20
listing pages of 100 rows. One export has a fixed 45-second monotonic deadline;
individual requests use at most 10 seconds and the unchanged remaining budget.
Synchronous Store I/O is not preemptible by this cooperative admission deadline.
Known verified IDs use direct reads; an unknown correlation needs the complete
bounded discovery before creation. A larger account that exceeds the listing
bound returns Incomplete rather than pretending the note is absent. These are
initial product limits, not measured Mem latency or account snapshot guarantees.

## Verification and simulator impact

Use a local HTTP fixture through the actual Mem client and actual temporary Store:
create/find/update, reopened Store with changed source revision and same marker,
exact metadata capability on a small alternate destination, duplicate/missing
markers, version/external-edit conflict, lost write acknowledgment and cancellation
after dispatch. Check one external write per effect UUID and historical receipt
retention. Do not build an unrelated model/device matrix. This prepared-content
path also verifies cancel-before-send followed by deliberate re-export, and one
live sender/concurrent retry through the real path returning Busy/no second
dispatch until the first owner releases. This prepared-content
path has no model or device effect; HTTP/Store fixtures cover its boundary.
Live Mem, OCR/refinement, installed tablet and whole Writer acceptance remain
unverified. Coordinate focused Docs/code review, CI, canonical sync and archival
only for this implemented increment, preserving wider roadmap work.

## Source basis

The current issue and all five comments supply the portable-correlation and
repeat-export requirements; they are internal planning context, not a public
transcript. Those requirements are reproduced above for public contributors.
The delivered Ledger source establishes the current transition gap. Current
official API facts and narrow prior art are linked in the reusable
[export research note](../../../../docs/research/prepared-note-export.md).
The attempt/disposition and conservative reconciliation design are engineering
choices; no live account write or native proof is claimed.
