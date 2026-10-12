# Subject memory: bounded local increment

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

## Remaining capability boundaries

The actual Reader currently retrieves global memory only without a qualified
document association; explicit document queries are available to domain callers.
Provenance links and confidence are author assertions, not source/native authority.
Initial lexical relevance is not semantic embedding effectiveness. HTTP/synthetic
responses prove protocol assembly and control flow, not live model obedience.
Normal Store initialization/recovery is distinct from nonmutating inspection.

The local adapter holds the existing legacy-mode lease and conservatively refuses
any selected Store. Sync flag changes cannot admit historical/retained losers.
The REM-52 handoff is read and documented: local key compatibility is a reasoned
assessment; shared wire-schema/membership acceptance remains open. Document
facts share a source-document conflict aggregate while independent global records
have independent chains. Exact shared membership/catalog policy, accepted current
projector and restore activation remain unimplemented here. PR 31/7 successor
primitives are not silently assumed present in the REM-37 base.

Writer, Manager, selected shared/isolated Drive policy, migration/clean-device
recovery, representative live/native effectiveness and release/lifecycle gates
remain open. Required failures are not waived, the full REM-24 capability is not
complete, and no canonical sync/archive/merge/Done follows from this increment.
