# Pre-implementation state

This is proposed behavior only. No source/API implementation, new provider/model call, device action, deployment or qualification is claimed. Source016d78a and Docs mainb66d1b9 contain the separately accepted Reader delivery. Original Reader, native, selected, pending feedback and held failed/spent handwriting work remain preserved.

Current source inspection finds a static catalog with an explicit caller-validation/pending-persistence boundary, ordinary Ledger current-head decoding and existing Store/mode snapshots. The proposed receiver uses stored associated facts rather than inventing another pending record domain. Its limitation is explicit: it does not establish unpresented state or retain a failure before any durable fact exists.

Source basis: current REM-40 description/all32 comments, delivered canonical feedback/layout/ledger contracts and direct current source inspection. The optional advertised Linear field-notes operation returned ToolNotFound; no external field notes were assumed. Scope and implementation remain pending independent review.


## Precode review correction

Independent review found the original completed/no-error promise unreachable: Ledger::decode permits Completed OutcomeFact only with schema two plus VerifiedSubmitted settlement, while this receiver excludes schema two. The corrected proposed API returns Result<FeedbackDescription> and refuses unsupported completed records, preserving the existing decoder and separate pure-catalog behavior. No source/test behavior has been implemented or qualified.

Snapshot matching now explicitly includes original root/fact record IDs even with malformed/foreign metadata and retains every selected head. Pre-validation rejects selected tombstones, duplicate/conflicting heads and unsupported/schema-two envelopes before inspect_snapshot can skip tombstones. Original fact-to-turn membership does not require outcome equality to a later turn. Success serialization has an explicit1024-byte UTF-8 bound and all-branch test requirement. The original866fd2b precode/review evidence remains preserved in history.


## Initial implementation candidate

Corrected precode5a29d7e was independently accepted in exact review5654894702 before implementation. [Source PR106](https://github.com/s116821/ReMarkableBuddies/pull/106) candidatef0af858f500db70bb7e96ae1c27577a8d9cacb7d adds exactly three paths: one module registration, the stored receiver and13 actual Store/Ledger test controls. All532 other main source entries remain exact and all ten held refs/earlier Reader branches remain preserved. No storage/type/decoder/catalog/writer/Cargo/SDK/Orchestrator or installed runtime behavior changed.

Local formatting and staged diff checks passed. No local compilation/test run is credited: the normal existing hosted40355159302 pipeline owns actual compilation/test qualification, avoiding large C builds or overwriting retained frozen Windows executables. Its current compilation/strict lint passed and test execution is in progress; no successful test or full-pipeline result is claimed yet. No provider/model/native/tablet operation occurred. Source/test and refusal/privacy review continues before final independent implementation acceptance.

The13 controls cover actual persisted terminal branches/reopen/exact static identities and1024-byte output, nil/missing/foreign/type-reused IDs, explicit malformed/foreign payload capture, tombstones/deleted required turns, all matching record heads including foreign/null siblings, excluded completed/schema-two records, fact/turn membership/chronology, older fact versus later turn outcome, mode admission/release, metadata-only Source exclusion, unavailable committed objects and cumulative metadata overflow. Input fixtures and generic malformed Store records are explicitly test data, not qualified selected/native history.


## Completion-fixture and refusal-privacy correction

Preliminary source review of immutablef0af858 found that its completed-record fixture used noncanonical capitalized enum text, so that particular check could fail parsing instead of reaching the intended domain restriction. Source successored1fe8d72140fcc0ba3f1d9fec64004127ae320e uses typed Outcome serialization and independently asserts the actual Ledger inspector reaches `invalid attempt outcome fact` for schema-one completed input; schema-two records are explicitly refused before decoding. The old candidate and its original CI outcome remain retained and do not qualify this corrected branch.

Source review also identified that a raw domain/JSON error could echo a malicious stored variant value through diagnostic formatting. The successor maps mode, storage/snapshot and domain failures to static receiver messages without retaining raw causes, and adds a14th actual Store canary asserting both Display and Debug omit the stored secret-looking value. The metadata control separately asserts the actual underlying byte-bound failure and then the receiver's sanitized refusal. These retain the same three-path boundary and do not change existing Store/decoder/catalog behavior.

Mode tests observe admitted/refused choices and custody release after return. Custody held during the receiver call is lexical RAII plus the existing Store lease contract/source-review evidence; no newly observed concurrent mode-transition measurement is claimed. Current-head tests/full hosted qualification and independent final implementation acceptance remain pending. No model/native or further Reader qualification replay occurred.


## Original hosted failure retained

Originalf0af workflow40355159302 failed in an unchanged earlier live_simulator fixture before the stored-feedback integration group ran. Format/strict all-target Clippy passed, then548 library tests passed with three existing ignores and11 binary tests passed. The existing `pending_http_ticks_on_caller_thread_and_callback_failure_stops_ticks` failed its server's POST request-line assertion and subsequent join; that group had7 passes/1 failure. The13 new Store tests were not executed and receive no qualification credit. Build/Integration skipped. Raw482571-byte Checks log SHA2561bac08bd87395f8d8583375ea9eca90a1f0462d9004db3df93eba653ccef17a2 and complete run metadata remain retained. The actual timing/request-line cause is not established; no blanket flaky-test waiver or relaxed assertion is claimed.

The already-published ed1fe8d successor separately requires current-head full qualification for its canonical completion fixture and refusal-privacy changes. The existing HTTP test, production client, Cargo graph and all532 unrelated source entries remain unchanged. No unchanged-source rerun or out-of-scope HTTP edit was performed.
