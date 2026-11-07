# Installed resident input for selected Reader

Proposed precode for the existing [document-scoped Buddy sync change](proposal.md).
Source baseline is Buddy `23f7a70b0b324f28cab7e755357fb07f4fdd435c`, delivered
Buddy main `cf568ae05af6a585babf349c1df8507febcfce32`, Docs156
`6f0ced3dbf9b75901dc4ffc6bcdc89c76367f0a1` and the Buddy lockfile's SDK v0.2.0
`a0c6480be6785480c2e0da76a3c06697a18efae4`. This leaf is a proposal pending
independent review and reconciliation with the final selected Writer API.
The implementation and verification belong in the existing Docs156/Buddy139
delivery.

## Scope and decision

Connect one genuine installed Reader release to a fresh selected Prepared
request and the existing selected Reader consumer, ending at a durable
Generated draft. Start with an already registered, current local document
aggregate. Support both conversation-only closures and mixed conversation and
document-memory closures. A fresh unbound conversation can start inside that
aggregate. First-document registration, choosing or resuming a Buddy-page
binding, native output and separate researched-answer receiving remain open.

The SDK already supplies the private, bounded Observe and CaptureSource
protocol. HistoricalCapture proves the original document/page/full-order
samples, image integrity and bounded dimensions. Its two samples do not prove
continuous content freshness. The selected storage receiver needs no new SDK
primitive for this input. Public Platform acquisition remains unsupported on the
committed unqualified adapter. Current native content authority, effects,
binding and persistence still require their own qualified paths.

## Installed constructor and request owner

- Route the actual selected service startup in `main.rs` and
  `reader_runtime.rs` before ordinary model/device startup. Resolve the trusted
  installed Config path without loading model credentials. Open the existing
  ready format5 Store once. Require configured `reader.selection`, matching
  SharedGroup, current binding, existing registered document admission and the
  existing privately constructed `InstalledReaderSelection` plus supervised
  `ServiceHealth`. Keep the default selected refusing Workflow and its typed
  result for missing or unsupported native admission. Mode, registration and
  closure failures retain their own refusal classification.
- Build an input-only Workflow that combines the same Store's
  `SelectedBackendFacade` with `ResidentSourceOwner`. Reuse
  `RequestInput::wait_released_reader` with the actual Reader corner and
  blank-start disabled. Delegate the released guard to
  `ResidentSourceOwner::begin`, `InstalledFactory` and
  `Session::activate_selected_until`. Keep general device acquisition and
  effects refusing. Do not instantiate the ordinary RealDevice screenshot,
  pen, keyboard or touch writer merely to get its Reader release method.
- Preserve sealed installed profile/artifact, health, quiet-input, service,
  cgroup, activation and recovery checks. Where the admitted installed profile
  already selects preactivation, reuse its quiet startup handoff independently
  of output-backend construction. Retain that child and retire its initial
  connection. Preactivation creates no Reader request and consumes no gesture.
  The first genuine release opens the bounded acquisition for the current
  source. No automatic document reopening, replay of the first gesture, stock
  restoration bypass or alternate activation.
- On each admitted release, capture original request and mode custody before
  acquisition. Require the effective Reader gate before this request can
  publish Prepared or resolve model credentials. Own exactly one iteration
  and its finalization. Use the resident health/input guard throughout capture,
  derivation, Prepare, delivery and model work. Reuse the prepared receiver's
  inner entry so it does not begin a second iteration or replace the released
  input guard. After acquisition the existing owner retires the socket but
  retains the child and request guard. At first model handoff, its delivery
  check retires the acquisition subdeadline only. Failure, including a failure
  after possible takeover, follows the existing finalization and recovery
  owner. A distinct genuine release is required for a subsequent request.
  A lazy takeover that loses the initiating page cannot complete that
  request. The user may reopen the page in the stock UI and release again
  after the retained session is ready.

Ordinary LocalOnly startup, native output and ordinary Ledger behavior remain
on their delivered paths. No new command, data-only shortcut, runtime option
that bypasses admission, or fallback from explicit selected startup.

## Existing registered document admission

The configured scope is an exact group/key/binding pin, not a wildcard. Verify
the captured document UUID against the catalog owner and
`memory::catalog::document_key(document)`. Recheck Store actor/generation,
SharedGroup epoch and lease, binding, catalog root/mapping, exact receiver-local
registration and current selected token under canonical ordered gates. Hold
mode custody for the request and release it on finalization. Do not hold
domain mutexes during idle input, native socket wait, image derivation or
provider response. Discovery before ordered gates supplies only candidate
pins, which are revalidated inside the gates.

Both closure shapes require the same positive document registration proof.
Reuse the worker's protected accepted root/catalog and validated mapping for
the exact Document owner. A positive offline mapping requires no new network
read. Validate the local catalog projection, registration's exact owner/key
and the local original Initialize operation/hash in accepted lineage. A
missing registration or a received mapping without complete local custody
remains unavailable. For a locally created genesis, verify the agreed
root-and-key genesis base using the existing worker recipe. For a received
genesis, verify receiver-local registration and the accepted descriptor and
applied-base custody in the existing Worker chain. Do not compare a received
Initialize against the local-publication genesis-base recipe or accept a
foreign Initialize as local history. Later accepted activation and local
descendant commits retain their exact current base and token. The verifier is
read-only, bounded and takes the existing selected root/binding authority.
It neither constructs a Binding nor registers a new document.

Reuse the common `Catalog::project` and `Aggregate::project` validation used
by the worker's registration path. The latter already validates the
Conversation/Source/ExportAssociation partition of an exact document with or
without SubjectMemory. Pure conversation readiness must explicitly acquire the
document and matching catalog gates and run this proof. The existing
`with_ready_gate_set` discovery branch alone is insufficient because
`mixed_identity` skips a closure without SubjectMemory. Mixed readiness
additionally validates its complete memory partition and existing catalog
custody. Deduplicate overlapping document, catalog, preference and memory keys
in one ordered set and avoid nested acquisition. Reuse this positive readiness
proof at Prepare, actual submission and new result publication. Do not infer
readiness from selected membership alone, retained history or a configurable
qualification flag.

## Capture, Prepared publication and recovery

1. Under the original released-input acquisition deadline, use the resident
   Observe and CaptureSource exchange. Keep the exact source document/page/order,
   Observe/Capture operation IDs, runtime/activation/boot identity and original
   PNG. Prepare the Source domain schema2 ResidentCapture record using the
   existing historical encoder and validation from `conversation/resident_capture.rs`.
   Preserve the exact original PNG and ordered derived overview and three strips
   with dimensions, crop, DPR, descriptors and byte hashes. This transfer
   retains historical provenance. It supplies neither a current PageObservation
   nor native effect authority. An optional stronger contract for another
   identity sample would need a bounded same-child Observe, with no inference
   about content revision.
2. Freeze a single Prepare operation and its root/user/exchange/evidence/receipt
   identities and original input. Append to an explicitly admitted unbound
   root or create one inside this already registered aggregate. A captured
   page known to be a Buddy output page refuses this source-only route. At
   CAS recheck exact document and selected registration/token, root chronology and heads,
   current selected preference admission, and the original session/input guard.
   Derive media before the domain gates. Atomically call `Store::commit_selected`
   with the exact accepted token, root revision, Prepared Reader User turn,
   ResidentCapture envelope, original and derivative media and the original
   acknowledgment. Validate the candidate closure, preserve unrelated selected
   records/media and retain existing Store/Worker publication behavior.
   An ordinary Ledger root or capture publication cannot precede this CAS.
3. Verify the exact new acknowledgment and selected membership via
   `SelectedDomainProjection` and `SelectedAdmission::capture_images`.
   Reuse the current token and exact root/user/evidence references for
   `run_selected_prepared`. Only a fresh acknowledged Prepare enters the
   existing receiver. Missing, changed, corrupt or omitted media refuses
   without recapture or substitution. Current selected preference and owned
   capture delivery must still pass at the first actual model submission.
4. Freeze separate Interpret and Generate operations using the existing
   selected Reader text publication. A lost Prepare, Interpret or Generate
   acknowledgment can be reconciled only against the exact local original
   transaction, predecessor/input fingerprint, operation, closure and
   acknowledgment. Use existing selected receipts and bounded lineage. Provide
   historical-only recovery separately from the live admission branch so current
   preference or memory replacement cannot hide the original. Recovery cannot
   produce an active request, replace the active token, rerun a model, recapture
   or permit a fresh operation. Missing proof remains unresolved. Pending
   recovery retains its own existing contract. No separate journal or CLI is
   introduced.

## Effective policy and bounded multi-stage handoff

Use the final shared preference API once reconciled. Capture the trusted raw
Config identity and typed base, same Store generation/mode, exact current
preference token or established absence and admitted document token. Apply
the portable declaration overlay in memory, preserving excluded local
settings. Evaluate effective Reader enablement and selected memory compatibility
before credential-bearing dotenv loading, `Environment::current`, protected
model credential reads or engine creation. Do not use the saved Reader flag
as the selected authorization or fetch a replacement preference automatically.
An unresolved preference state refuses. Keep personalization out of both
recognition requests. Apply it through the existing optional enrichment path.

Use the existing proposal, independent verification against the exact same
persisted source images, then Interpret, optional memory/personalization
enrichment, and Generate. Under the ordered preference/document/catalog set,
revalidate exact pins at each actual owned model handoff and each new result
publication. For enrichment and Generate join the exact optional selected
memory result and its gates, including an observed empty result when it
determined no enrichment was needed. Preserve the original memory-pin lock
order and consume it only at its proper new publication boundary. Only a
fresh Interpret acknowledgment advances the Reader token. Release gates before
waiting and use bounded cheap progress cancellation, then repeat exact
revalidation before later dispatch and CAS. Unsupported model/provider
ownership refuses. No alternate recognition or model pipeline is required.

Proposed maximum parent deadline is 420 seconds from the genuine release.
Reserve up to the existing 90-second acquisition interval through first
handoff, up to three 90-second provider windows, and up to 60 seconds total
for between-call and final publication/readback work. Clamp all subdeadlines
to the original parent and preserve the existing tighter native limits.
An unused stage does not permit a fourth call or extend the parent. Reserve
one cumulative object/aggregate/byte allowance and a bounded progress
allowance before admission. Charge discovery, Config and selected reads,
source readback, submission, result verification and exact recovery performed
inside that lifetime. Reserve complete passes at the actual stage boundaries
and size the cheap progress allowance against the complete 420-second window
and actual cadence, including immediate handoff/final checks. Independent
historical inspection has its own bounded read operation with no authority
to resume. No callback may renew allowance, hold a domain lock across a
provider wait or adopt refreshed pins. Reconcile concrete budgets with the
frozen Writer API and the supported Reader payload bounds before coding.

A fresh Generated acknowledgment is a selected draft result. It does not
authorize Pending, native insertion/reuse, rendering or settlement. Preserve
the existing uncertainty fence and original operations. Stale/canceled results
retain only the truthful prior committed state. No ordinary failure publication
or native diagnostic is a substitute.

## Proposed spec deltas for the paired change

### MODIFIED platform-runtime · Explicit selected Reader startup and historical handling

An explicitly configured selected Reader runtime SHALL preserve the refusing
default unless current SharedGroup document readiness and the existing
installed resident source and health owners admit the Reader input route.
Selected input SHALL use the bounded released-request and resident capture
owner. Startup and every newly admitted request SHALL refuse absent or
contradictory authority before model credential resolution and SHALL preserve
ordinary LocalOnly routing, no legacy downgrade, existing-only Store custody
and independent historical handling.

#### Scenario: Qualified resident input without output

- **WHEN** an installed source and supervised health owner admit a genuine
  Reader release for the exact registered document
- **THEN** the same selected Store receives one bounded historical capture
  and one fresh Prepared acknowledgment through the selected route, without
  ordinary acquisition or native output authority.

Retain the existing unsupported, exact historical recovery, invalid metadata,
idle availability, persisted mode and historical report scenarios.

### ADDED reader-analysis · Installed selected Reader prepares exact historical input

The selected resident Reader SHALL admit both verified registered pure
Conversation and mixed document closures. It SHALL validate the exact captured
document and publish the root, Prepared turn, Source schema2 evidence, all
required media and original receipt in one conditional selected transaction.
Only a fresh exact readback SHALL feed the existing selected Reader receiver.
An uncertain or stale publication SHALL allow only original historical
recovery and SHALL NOT replay the capture, admission or model request.

#### Scenario: Pure and mixed registered custody

- **WHEN** the exact current registered document has either supported closure
  and the resident capture matches it
- **THEN** its complete original and derived media remain linked to the exact
  Prepared turn and any unrelated document memory remains unchanged.
- **AND** a missing, stale, foreign or unreceived registration refuses without
  ordinary publication, registration or a model call.

### MODIFIED reader-analysis · Selected request and draft publication

Selected interpretation and Generated publication SHALL retain the original
effective preference and canonical selected custody through every actual
submission and result publication, joining optional selected memory as
applicable. It SHALL use one cumulative bounded request across the distinct
analysis, verification and optional enrichment stages and preserve exact
original-only recovery independently of fresh admission. A selected Generated
draft SHALL stop before Pending, settlement or native output.

#### Scenario: Original request remains valid across multiple bounded calls

- **WHEN** the unchanged request takes more than a one-stage allowance while
  remaining within the original selected Reader deadline and reservations
- **THEN** the existing model stages may complete using the original pins,
  and exactly one selected Generated result publishes without a new budget,
  fallback, or device effect.

Retain the existing lost acknowledgment and preference drift cases. The
active shared preference and selected Worker requirements apply throughout.

## Implementation and verification tasks

- [ ] Root independently reviews this leaf, reconciles the current Writer
  preference/LLM/memory API and confirms the exact paired source bases before
  work starts.
- [ ] Reader lane implements startup, input-only Workflow, single iteration
  and finalization in `src/main.rs`, `src/reader_runtime.rs`,
  `src/workflow/{mod,orchestrator,resident_source,selected_backend}.rs` and
  the narrow input receiver. Keep ordinary and unqualified CLI controls.
- [ ] Factor historical capture construction in
  `src/conversation/resident_capture.rs`. Add selected Prepare and exact
  receipt verification alongside selected Reader publication. Coordinate
  the worker catalog/readiness hook with the owner of the shared modules.
  Avoid changing Writer, Manager, ordinary output or REM-26 recognition.
- [ ] Wire the reviewed effective consumer through
  `src/workflow/reader_attempt{.rs,/selected.rs}`,
  `src/conversation/selected_reader_write.rs` and the existing owned
  submission and memory interfaces after their API freezes.
- [ ] Exercise the actual constructor/refusal in `tests/reader_runtime_cli.rs`
  and the existing owned Linux resident peer for release → capture → selected
  CAS → readback. Cover pure and mixed registration, received versus
  locally created genesis, same-child second request, stale mode/head/catalog,
  foreign document, cancellation, missing/corrupt media, lost acknowledgment
  and no ordinary record, extra operation or effect command.
- [ ] Extend selected Reader persistence and composed-memory fixtures with
  guarded localhost model calls. Assert same source bytes in both recognition
  requests, independent verification payload, optional enrichment only after
  Interpret, a healthy delay across both former command/pulse limits and the
  one-stage lifetime, cumulative budget refusal, and mutations before each
  submission, during waits and immediately before CAS. Verify original-only
  recovery after drift and a truthful Generated acknowledgment.
- [ ] Main owns later evidence for the approved installed profile, genuine
  release and exact open-page capture after supervised activation, retained
  child, cancellation and independent stock recovery on RM2. Root owns
  source review, paired CI and eventual delivery. Production shared-provider
  Binding, provider qualification and broader Reader/native output remain
  separate gates. Do not archive the active change on precode or source-only
  evidence.
