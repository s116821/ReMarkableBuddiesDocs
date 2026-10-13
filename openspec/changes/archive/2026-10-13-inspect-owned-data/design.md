# Owned-data inspection design

## Scope and ownership

Main owns `src/storage/inspection.rs`, its export in storage/mod.rs, the CLI branch
in main.rs and focused storage/CLI integration tests. SCRAPPY retains Manager
UI/transport and REM-50; existing Sol performs read-only review. No changes to
protected native/Cargo WIP, generic mutation/recovery or the held native operation.

This increment produces a usable report, not complete REM-42 management. UI,
cleanup/export/restore, service quiescing, provider authentication, personalization,
package ownership and current native-page readiness remain separate obligations.

## Nonmutating admission

Accept validated configured StorePaths, not paths advertised by stored capability
files. Read existing identity and CURRENT using current bounded typed rules.
Never create directories, identity, generations, owner markers, locks or staging;
never chmod, recover, clean, publish, contact a provider or initialize a device.

Open the EXISTING stable store.lock read-only and attempt its nonblocking exclusive
OS lease. This changes only temporary OS lock state, never file bytes. Missing
lease/ownership/current files are unavailable; an active writer is busy; unsupported
format/ownership/paths or lock behavior is explicit. No service stop or lease-file
creation follows. Recheck identity/CURRENT before return and disclose drift rather
than claiming a consistent result. Normal writers/maintenance use this same lease;
out-of-contract external mutation is not an atomic filesystem snapshot guarantee.
The running Reader normally holds the lease throughout its lifetime; this command
may therefore return busy until the caller performs separately authorized
maintenance. It never retries with write access or stops that runtime. Unix file
identity can be bracketed by device/inode; stable Windows standard-library file-ID
access is unavailable at the declared compiler, so read-only handle/path metadata
brackets have an explicitly weaker identity guarantee. Read access may update
access timestamps; content/mtime preservation is distinct from immutable atime.

Use the existing pure selected-generation validation for format1/2 and matching
actor/generation feature marker. Do not use the stale embedded envelope schema's
domain const1 to reject current typed Conversation schema2. Unknown versions
defer rather than rewrite or initialize them.

## Bounded physical inventory and categories

Walk only documented data structure names and valid generation/manifest/object
identities under the owned roots; validate every visited path with existing
symlink/reparse/protected-path guards. Unknown entries are reported as incomplete,
not recursively adopted as owned. Cache requires its existing matching owner
marker. Credential content and native/legacy document paths are excluded.
Diagnostics lacking a current declared ownership contract remain not inspected.
Known ordinary commits are `commits/<UUID>.json`, objects are `objects/<SHA>`,
current selected pointers are `selections/<scopeSHA>.json` and selected history is
`selection-history/<transactionSHA>` without a suffix. Both selected and retained
manifests carry references. Read configured root aliases canonically to reject
overlap rather than double count case/short-name aliases on Windows.

Bound entry counts and parsed JSON bytes with existing MAX_ITEMS/MAX_RECORD/
MAX_METADATA GLOBALLY for the whole inspection, including every parsed JSON input;
per-file limits do not multiply the allowed aggregate. Refuse/truncate no silently exact total: missing, denied, malformed,
unsupported, unexpected or limit-exceeded input yields explicit issues and only
observed counts, with a complete total absent. Never report an unknown category as
zero. Declared empty included categories may report zero once inspection is complete.

Apparent stored bytes are file lengths, each owned relative file path charged once.
The same hash in another retained generation is a different stored file. This is
not allocated filesystem blocks, media integrity, logical liveness or reclaimable
space. Tombstones, old revisions, retained losers and orphan/staged objects remain
stored bytes; the report never suggests they may be deleted.
Different paths are apparent byte charges even if an external actor made them
hardlinks/reflinks; allocated block/inode deduplication is not claimed.

Use existing bounded Manifest/Envelope/SelectionTransaction validators to classify
record metadata by Conversation, Source, ExportAssociation, SubjectMemory and
Handwriting. Do not reconstruct a current causal index, parse displayed questions,
re-OCR images or infer current associations. Commit and selected history metadata
are accounting evidence, not native authorization or a new registry.
Do not call Store::validate_objects, selected_snapshot or Source::open: those
stream media content. Validate record namespace correspondence, descriptor/coverage
hash correspondence and included-size consistency using the pure typed validators
and bounded record JSON. Reference unions are deduplicated by generation/hash/
namespace; a stored selected pointer and its history copy have separate file-byte
charges but cannot multiply the referenced object totals.

Namespace media-reference totals are unique declared references within a category,
but NONADDITIVE across categories. Report present file lengths and declared missing/
omitted references separately. Shared media gets one physical charge and an explicit
cross-category reference count. Validate reference size consistency; read bounded
record metadata only, not bulk image or credential content. Matching filenames or
lengths do not verify media hashes. Incomplete metadata may leave objects unclassified;
do not invent an exclusive category assignment or exact total in that case.
Preserve Omitted coverage even when another manifest leaves the same file present.
Conflicting declared sizes or observed length mismatches are explicit partial
conditions. Fixed sanitized issue codes/counts never emit raw parser errors,
unexpected filenames, paths, metadata bodies or protected sentinel values.

## CLI and compatibility

The inspection flag conflicts with simulation/provider/input/output override flags.
Route before dotenv/credential resolution, Store startup, Workflow, sync and device
construction; only the explicitly selected or normal known nonsecret configuration
is read. Sanitize configuration and metadata failures rather than echoing private
values. Emit report_version1 JSON; successful report emission is not a healthy
Reader/native result. Manual callers and both future Manager host adapters use this
same route; no running Buddy API is introduced.

## Verification and delivery

Test real Store-created fixtures after releasing the writer; hash every durable
file before/after and verify no new roots/files, cleanup, recovery, config rewrite
or timestamp changes attributable to a write. Test busy writers and missing roots
without creating a lock. Exercise legacy/selected formats, schema2, tombstones and
retained/shared/omitted media; source-image payloads and secret files must not be
read or emitted. Check unknown/corrupt/version/owner/limit/path failures and a
real CLI subprocess with missing provider credentials and protected sentinel values.

Validate exact committed source separately from carried Cargo/native WIP, preserve
parent dependency/source revisions, run focused tests/formatting/ordinary build and
required checks, and record existing unrelated lint/native limitations. Independent
review, paired draft delivery and full requirements verification precede any canonical
sync/archive/merge. Broad incomplete REM-42 tasks remain open.

## Prior art

[RCU](https://www.davisr.me/projects/rcu/) documents local/offline management,
snapshots, scriptable CLI and explicit compatibility handling. Those concepts
motivate clear inventory/failure states, not its firmware/document-management scope.
Existing inspected [reManager package/connection source](https://github.com/rmitchellscott/reManager)
distinguishes actual installed state from cached catalog information and uses
management-plane execution; retain explicit state/provenance instead of inventing
a Buddy service API. No source implementation, framework, native utility or
licensing grant is copied into this increment.
