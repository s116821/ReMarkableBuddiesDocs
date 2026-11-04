# Historical pre-implementation state

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


## Test-helper compilation correction

The ed1fe8d40356761700 run failed compilation under strict Clippy before tests: the new underlying snapshot overflow assertion called unwrap_err on Result<Vec<Envelope>>, requiring Debug for Envelope, which the existing type deliberately does not implement. Raw135615-byte log SHA25654cf126d4a6e845ff07dc8de508c7c63fdaca8dd91b426dcf11a6667a5487dd5 and complete metadata remain retained. No test result is credited to that head.

Source4524894c5ccee3f678030cd8d5febd4840a4c1b3 changes only the test helper to err().expect with the same overflow/classification assertions. Existing Envelope and production receiver remain unchanged. The exact452 source and all14 Store controls were independently reviewed with no additional source finding; preservation proofc32bd78978d6a1e1690fc1bda58ca4468daca654c6dd38e31efe1f7b8b187700 confirms532 unrelated base entries. This is source review, not executed test/full-CI acceptance. The sole current qualification is normal workflow40357531009; all earlier sections describe their historical checkpoint states.


## Current corrected qualification and verification

Exact Source4524894c5ccee3f678030cd8d5febd4840a4c1b3/tree4b834adb8ce9363461fcf8a8d5219e5eddf963b0 completed workflow40357531009 successfully: Title, Checks, Build and Integration passed; PRRelease correctly skipped. Actual checkoutac19ffb593b8e7502470dc4463141fa22d5b60b1 has parents016d78a+4524894 and exactly the reviewed tree. Full Checks raw742044-byte log SHA25669c30f976c1b634fce0e2c440195a05cc055f52fe5aae2a5334ad40026eb3b8e confirms548 library passes/three existing ignores,11 binary passes and all other executed suites passing.

All14 named stored-feedback controls individually passed,0failed/0ignored in4.05seconds. They cover real persistence/reopen/static identity and output bound, nil/missing/foreign/type reuse, explicit malformed/foreign fact capture, explicit tombstones/deleted turns, all selected heads including nonmatching foreign/null siblings, canonical completed/schema-two refusal, original fact-to-turn membership/chronology, stable older history, mode admission/release, metadata-only Source exclusion, unavailable committed storage, cumulative byte overflow and sanitized malformed-input diagnostics. The33 terminal outcome/reason cases inside the first control are parameterized inputs, not additional top-level passes. The existing eight live_simulator controls also pass on this corrected head; no failure is silently relabeled.

The canonical completed fixture serializes the typed enum and verifies the actual domain inspector reaches its invalid-attempt-outcome guard; schema-two refusal precedes decode. The exact metadata overflow cause is separately asserted before the receiver's sanitized refusal. Before/after owned-file fingerprints and repeated reads preserve original record identity without writes. In-call mode custody remains lexical RAII/existing lease-contract review; newly observed mode evidence covers admission/refusal/release only.

Independent immutable source reviewc32bd78978d6a1e1690fc1bda58ca4468daca654c6dd38e31efe1f7b8b187700 found no further issue in the accepted scope and preserves532 unrelated base entries. Full source qualification proof SHA256d8d2fda3488188897ab8cfe27cb33a87b6e054b710fe6380e6407b5f78ea0d52 pins current metadata, checkout and raw logs. Completed Integration43362-byte log SHA25610fe8c4f90457369ef776b6e5c7d9e27b043edcb15bed27c61c699a606fd6aa1 is retained; ARM package execution is emulation only. No local compile/install, provider/model call, tablet interaction, service change or retained executable overwrite was performed. New bulk evidence lives on the already permitted Z share because C is capacity constrained; existing C evidence remains intact.

Both original failures remain: f0af's unchanged earlier POST-fixture assertion, which prevented new Store tests running, and ed1's test-helper Debug-bound compilation error. A separate source-proven EOF path in the existing HTTP fixture is prepared for future bounded maintenance; it was not observed as a hang in this passing run and is not fixed or attributed as this run's cause. That proposal is outside this three-path receiver delivery.

## Scoped requirement and lifecycle verification

- Explicit stored ordinary feedback: the actual current Store tests and existing snapshot/domain decoders cover exact original root/fact/turn identity, pre-inspection selected-head/tombstone/schema refusal, complete chronology and metadata bounds. Existing pure catalog and writers remain unchanged.
- Historical/pending separation: actual older-fact-versus-later-turn and static/error-secrecy controls preserve historical identity and uncertainty without queue, presentation or current-state receipts. All supported catalog branches serialize within1024UTF8bytes. No image/native/provider call is added.

No unresolved implementation/scenario/design finding remains within this bounded library receiver. The accepted two requirements/six scenarios are synchronized into the existing sanitized-feedback capability, preserving its original two requirements/three scenarios. Only this change's five files are archived. Source remains452; only final Docs checks and exact paired archive/review/delivery observations follow. This does not complete pending presentation, unassociated pre-attempt retention, native/gesture/runtime/Manager work, general latency guarantees or whole REM-40. Source basis: actual hosted/current Git and native comparisons, retained failed and passing raw logs, exact executed controls and independent immutable source review.
