# Subject memory: local and selected receiving increments

## Exact source and contract

Rust revision `916dbbd089ec9f7e81b4af7c76e95cfa48b304c9` implements typed local
SubjectMemory operations, bounded query/inspection, optional configuration and the
actual receiving Reader's post-verification enrichment path. Preimplementation
contract `31cedb6f4fc886f73e615549ce47543a9258e82a` was independently accepted
before code; manual and scope clarification are in Docs
`a5acc08949bf6791e75bd3f5c8c7dd00710bf3e0`.

The source depends on unmerged Rust parent
`7b207ec8a42548c12960699854107236eb2bbd7f` / PR 30 and Docs parent
`60a8e0e7ec6ec181ed36652b9b7e33d222086a6c` / PR 6 for bounded Store snapshots
and typed conversation/source recording. The unrelated REM-42 inspector is not
in this topic base. All nine protected preexisting Rust inputs retained exact
hashes. No SDK consumer pin, device/service, account, firmware or held packet
operation occurred.

## Observed local evidence

Working-input checks passed 15 real Store controls, one actual loopback HTTP
provider protocol control and two actual Reader tests with synthetic device/model
responses. Additional negative Ledger transition control passed. They cover
Unicode restart, exact retries after forgetting, explicit CAS/tombstone
reinstatement, scoped/profile isolation, contradictory/expired facts, encoded
count/byte limits, bounded inspection, unsupported preserved payloads and actual
local-mode admission against selected storage.

The damaged-newer-tombstone control explicitly demonstrates that generic recovery
can expose an older surviving head while the memory domain refuses the incomplete
view. The imported-fork control proves an independent same-claim duplicate cannot
escape contradictory heads. The metadata-only relevance control proves duplicate
coalescing does not discard a relevant higher-UUID representative.

Reader controls preserve the exact verified question and source image bytes,
exclude memory from recognition/transcription and avoid fabricated visible turns.
Disabled/empty mode retains two calls; relevant enabled mode adds one receiving
answer call. Withheld-only, provider failure, abstention, malformed/non-ASCII answer
and lost progress prevent output. Exact failed/canceled user outcomes retain the
verified original; no assistant draft is created. Negative Ledger controls reject
reasonless/wrong-reason failure, changed interpretation, Generated/Completed and
mismatched cancellation rather than granting output authority.

The narrow Ledger fix permits Interpreted-to-Failed only with explicit
ProviderFailure/RequestFailed, or Interpreted-to-Canceled with Canceled, preserving
original interpreted text and existing root/turn CAS. Independent source/manual/
repair reviews accepted this bounded scope; the reviewer did not rerun the broad
suite or claim provider semantics/native effectiveness.

A normal Git archive exported with command-local `core.autocrlf=false` has SHA-256
`fbe1d2cb7fd7e1c1b8013338deabaa574c69a8acc0c26c63888cd7de60021986`.
Fourteen Cargo/source/test inputs matched exact raw Git blobs at the source commit.
The archive uses committed SDK
`d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`, not protected working-tree dependency
changes. Whole-tree formatting passed. Locked full all-feature testing completed
successfully on these exact inputs: 275 library checks passed, one existing test
remained ignored, and all binary/integration/compile-fail documentation checks
passed. The 15 memory Store controls, actual HTTP control, two Reader tests and
negative Ledger control are included in that run. Ordinary nonmock library/binary
checking passed. Required strict all-target/all-feature Clippy FAILED with the
same 24 existing unfinished-runtime dead-code errors (exit 101), unsuppressed and
unwaived. A diagnostic lint run does not replace that failed required gate.

The implementation is published as [draft Rust PR 33](https://github.com/s116821/ReMarkableBuddies/pull/33).

Central Docs 12 tests, guidance/provenance checker (19 files) and strict OpenSpec
validation (17 items) passed before this result append. This append and paired
drafts require their own current checks; no hosted result is claimed yet.

## One-shot maintenance successor

Source `3f6258b898102d9e8bc91a276110ec90eb3997d3` adds explicit bounded file-input
inspect/query/put/forget routes in the same Reader binary and draft PR. The focused
maintenance contract `5dda1872c093a870b4a6f572a727d95f0913f646` was reviewed and
committed before implementation. The existing domain/API operations are reused;
no app, listener, provider/runtime, service operation, dependency or sync engine
was introduced.

Working-input checks passed nine actual CLI controls plus the added self-parent
put/forget staging-preservation control, the real Store busy-classifier control,
two existing CLI controls and three binary argument/default/logging controls.
Independent source/test/manual review accepted the bounded maintenance increment.
Those earlier working results remain separate from the exact-source proof below.

The successor's normal LF Git archive SHA-256 is
`a30c4f7a2dc00d9d6165525e358f24b949ddc808881d9c8f44f3dea659e3aa0c`;
sixteen Cargo/source/test raw blobs matched the exact commit and committed SDK
remains `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`. Whole-tree formatting and ordinary
nonmock library/binary checks passed. Locked all-feature tests completed
successfully: 276 library checks, one existing ignored, all binary/integration and
compile-fail documentation tests, including ten actual Windows maintenance CLI
controls. Required strict Clippy FAILED on the same 24 existing dead-code errors
(exit 101), unsuppressed/unwaived. Earlier revision `916dbbd` proof remains valid
for that revision and is not promoted to this successor.

Hosted Ubuntu Test also passed in
[run 38296411740](https://github.com/s116821/ReMarkableBuddies/actions/runs/38296411740),
with 280 library checks/one existing ignored and eleven maintenance CLI checks.
The completed log explicitly records
`fifo_lock_is_refused_before_a_blocking_open_in_actual_cli ... ok`.
This is normal PR merge integration `25b52ca` of source `3f6258b` into base
`ff8ad75`; local archive checks above are the separate exact-head proof. Hosted
build/lint failed on the same 24 errors; tablet cross-build is not established by
these test results. Current published Docs `f1d0bab` Ubuntu/Windows/OpenSpec checks
passed; this final result append requires its own current Docs checks.

Maintenance intentionally prints bounded saved values for requested inspection/
query. Pure input failures, including self-parent identities, fail before startup;
well-formed stale/conflicting mutations can follow normal Store recovery writes.
Missing/partly owned state is not initialization permission; only creation put with
empty parents may initialize absent/empty storage. Busy and selected/refused states
never trigger service stop or unleased fallback. Exact total compact response
bytes include the newline; output limit never emits a partial conflict refresh or
retries a published mutation. See [maintenance contract](maintenance-cli.md).

## Selected receiving successor

Exact Rust source `ad6a70f29809972f23cd4370fdb0ab8f1f5a6bd5` implements the
selected Provider, typed append-only catalog, stable document/global aggregate
keys, original raw genesis and accepted key/claim custody. It connects actual
Reader processing and one-shot commands while keeping LocalMemory as the default.
Precode domain contract `04dc96c` and explicit setup contract `4cc3f3b` were
reviewed before their implementation; receiving/publication limits and final
handoff/custody clarifications are at Docs `abbb2e7`. Manual `b8ec9b3` was reviewed
against the repaired source. Full remote/native capability is not inferred.

The actual base already contained accepted REM-52 selected primitives byte-for-
byte despite non-ancestor Git history. Only the concrete generic budget delta
`31116b03` and custody delta `4884a256` were applied; protected Cargo/config/device
work was not imported or overwritten, and the separate historical archive API
was not introduced into live receiving. The generic increments were independently
accepted in [budget review](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5495556299)
and [custody review](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5495938187).
Custody spec content `94329b0` was fetched and reviewed; at this result preparation
the generic Docs PR 7 pointer still reported `c93adc7`. That owned publication
discrepancy remains separate from immutable content acceptance.

Queries read complete winning closures; retained/historical values never enter
ranking or supply missing facts. Accepted historical envelopes check only
immutable key/claim custody, including facts created after Initialize. Current
unknown/ambiguous mixed ownership, missing/corrupt/stale membership and exhausted
receiving budgets refuse. Mixed document edits preserve exact other-profile and
conversation/source references, media and complete coverage identities.

One receiving snapshot allowance covers catalog, all queried aggregates, history/
retained validation and final rechecks: 64 attempts, 4096 work items, 8 MiB
metadata and 32 MiB media verification. Repeated/absent attempts count. This does
not promise 64 usable registrations, total process memory or elapsed time.
Publication keeps separate Store validation limits, not a combined I/O cap.

The actual Reader holds shared ordered admission through its Generated/local
journal write. Returned payloads are sealed along with normalized tokens and raw
custody heads; changed payloads and reused consumed clones refuse. Selected-mode
native output remains explicitly refused. Maintenance retains Provider/pins/Store
lease through the actual stdout writer, including complete-empty queries and
sealed inspection. Stale/changed/exhausted admission emits fixed unavailable with
no data; a partial I/O failure never attempts a second report. Ordinary put cannot
mint absent selected membership. Three explicit setup operations support complete
initialization, orphan custody and distinct published/replayed/adopted receipts.

Independent Sol source review found consuming-output, mutable-result, root-lineage,
media-order retry and claim-continuity defects in the preserved intermediate
`7e10c59` candidate. The repaired exact `ad6a70f` source/assertions and central
manual were accepted after those controls were added. That reviewer did not
rerun the full exact archive suite; generic custody acceptance is separately
attributed above. No acceptance transfers to the intermediate candidate.

The normal LF archive has SHA-256
`7dd498d2b0d301821d8f5b87cfb90e702ef1416a3008ea14e3e16404655b7de6`.
Twenty-one Cargo/source/test blobs matched raw Git identities, including committed
SDK `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`. Locked/offline full all-feature
testing passed: 283 library checks/one existing ignored, all binary/integration
and compile-fail documentation tests. Included are eight real selected domain
controls, thirteen actual Windows maintenance CLI controls, the actual Reader
replacement test with three cases, and actual writer handoff test with five cases.
They are included in the suite, not additional unique counts. Earlier working-pin
checks remain separate from this exact committed proof.

Controls cover stale model/boundary replacement, payload forgery/clone reuse,
rootless genesis, accepted registration removal, normalized-token/raw-genesis
drift, original retry after tombstone, reversed media/coverage order, exact
noncanonical references and other-profile preservation, receiving budget
exhaustion, orphan registration/adoption and later-created claim custody with or
without retained copies. A legitimate same-claim winning fork remains usable.
The fail-once writer allows later writes and asserts exactly two calls plus only
the seven-byte prefix, so fallback append attempts are observable.

Whole-tree formatting and ordinary nonmock library/binary checking passed.
Required strict all-target/all-feature Clippy FAILED with the same 24 existing
unfinished-runtime dead-code errors (exit 101), unsuppressed and unwaived. Exact
diagnostic lint completed with those 24 and no additional warnings; it is not a
replacement for the failed strict gate. All nine protected input hashes remained
unchanged. The exact source is published in the existing draft PR 33; new-head
hosted CI, this result update's checks and final evidence review remain pending.

## Remaining capability boundaries

The actual Reader currently retrieves global memory only without a qualified
document association; explicit document queries are available to domain callers.
Provenance links and confidence are author assertions, not source/native authority.
Initial lexical relevance is not semantic embedding effectiveness. HTTP/synthetic
responses prove protocol assembly and control flow, not live model obedience.
Normal Store initialization/recovery is distinct from nonmutating inspection.

The local adapter holds the existing legacy-mode lease and conservatively refuses
any selected Store. Sync flag changes cannot admit historical/retained losers.
An explicit selected configuration now uses the implemented local accepted-
membership adapter described above. Remote shared/isolated worker, root/catalog
onboarding, account/app visibility, live contention, restore/migration activation
and clean/replacement-device recovery remain unqualified. Document facts share
the source-document conflict aggregate; global records keep independent chains.

Writer, Manager, selected shared/isolated Drive policy, migration/clean-device
recovery, representative live/native effectiveness and release/lifecycle gates
remain open. Required failures are not waived, the full REM-24 capability is not
complete, and no canonical sync/archive/merge/Done follows from this increment.
