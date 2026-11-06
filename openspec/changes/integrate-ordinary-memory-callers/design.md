## Context

This is proposed caller composition, not an implemented or qualified capability.
The delivered local/selected memory increment and its archive remain unchanged.
The implementation baseline is the future delivered shared-conversation revision;
the inspected seams below are from Buddy `200d21733c1a402d3b68a93430f0e05e82e16ca2`.
The Docs starting point is `53cbfe5be4b328a58781a6d2772b5172863b8c3b`.

`Dispatch::local` already owns a `LocalDispatchLifetime` on the exact Ledger Store.
That lifetime combines `OrdinaryModeLease` and `LocalDomainLease`, admits absent or
LocalOnly mode and an already-ready notebook generation, and excludes legacy
publishers/selected membership. `LocalMemory::new_local` instead owns a
`LegacySyncLease`, which intentionally refuses generation 4. Its query engine
already reads the same bounded SubjectMemory namespace; no new storage engine is
needed. Current main injects memory only into the captured Reader. Routed Writer
explicitly passes `None`, typed Reader has no memory input, and notebook payloads
have no memory snapshot.

## Goals / Non-Goals

**Goals:** compose those ordinary receivers with saved enabled/profile settings,
same-Store local memory and existing operation guards; support already-ready
generation 4 without adoption; preserve exact request/history/source/images and
truthful replay, failure and evidence boundaries.

**Non-Goals:** selected/shared/isolated receiving or sync, automatic extraction or
memory mutation, native Writer ingress/refinement/effects, new retrieval/research,
Manager settings, migration/restore, native or whole-feature qualification.
Captured Reader and standalone supplied-text Writer contracts stay unchanged.

## Decisions

### 1. Share an existing lifetime; keep legacy admission intact

Make the existing `LocalDispatchLifetime` reference-counted at its callers and
give it an internal same-Store identity check using the Arc<Store> from its
existing factory. No lock guard is retained across a model call. `Dispatch`
retains `Arc<LocalDispatchLifetime>` and, only when memory is enabled, one
`Arc<LocalMemory>`. Add a crate-private LocalMemory constructor taking the exact
Store, nonnil configured profile and that lifetime. It verifies Store identity;
the existing factory still owns ordinary-mode and local-domain admission.

LocalMemory retains an internal lifetime enum: its existing legacy lease for
`new_local`, or a cloned Arc of the admitted local dispatch lifetime for the new
constructor. Existing `configured`/`new_local` and their callers do not switch to
the broader constructor. `legacy_sync_lease`, publisher leases, selected Provider
admission and generic maintenance format refusal are unchanged.

`Dispatch::local` validates memory configuration and selected refusal before
constructing this provider. Its internal accessor clones the same LocalMemory
Arc into the existing captured Reader setter. The ExistingReader startup branch keeps
its old constructor; OrdinaryLocal does not construct a second provider. Provider
creation follows enabled receiving modules rather than requiring Reader to be
enabled. This does not remove the independent refusal of native Writer-only
startup while native input is unavailable. When disabled, no memory provider is
constructed and no memory query, read, write or network call occurs.

The final Arc pins the mode/domain even if Dispatch itself is dropped while the
captured Reader still owns the provider. There is no provider-to-Dispatch cycle.
Foreign Store/lifetime combinations refuse. Generation 4 admission validates
readiness and existing ordinary custody; missing/incomplete markers, selected
history, IsolatedBackup/SharedGroup mode or a legacy publisher refuse without
repair. Replacing the legacy lease globally was rejected because it would alter
unrelated sync and legacy callers.

### 2. One bounded ordinary snapshot helper, no new engine

Add a crate-private immutable `OrdinarySnapshot` in `memory/receiving.rs`. Its
constructor takes an admitted LocalMemory, exact receiving Store, unchanged
request, optional validated original document ID and one timestamp. It uses the
existing Provider query and QueryResult encoding. Share the existing ordinary
result validator from `conversation/receiving/memory.rs` through crate-private
visibility; do not build a FrozenRequestContext, invoke retrieval or reassemble a
historical source frame merely to validate a memory result.

The helper creates `Query::new` with the configured provider profile, defaults of
8 matches/8192 encoded context bytes, exact request of at most 2048 UTF8 bytes,
and only the supplied original document scope. It does not extract new claims
from prose, truncate a request or invent current-claim suppression. Validate
profile, record/revision identity, original-document/global scope, provenance,
expiry, status/diagnostics, count and bytes using existing domain rules.
CompleteEmpty yields no extra text part. Complete or Partial must have usable
facts; unavailable, malformed, selected or empty Partial results refuse. The
snapshot is author-asserted contextual data, not an atomic freshness lease.

Expose the existing Writer local-snapshot policy string as a shared internal
constant without changing its bytes. A usable snapshot contributes that policy
and encoded data once in a separate text part. It never changes request/history,
source records or visible turns and grants no operation permission. No raw
provider error chain is retained. Existing historical composition remains
historical and selected results cannot enter this helper.

Typed Reader and notebook use this helper. Routed supplied-text Writer reuses
its delivered `subject_memory::context` path with the typed same-Store LocalMemory
provider; its existing preparation, scope and failure semantics remain intact.
Generalizing the entire Provider API or changing standalone Writer snapshot
semantics is unnecessary.

### 3. Wire Reader and Writer at their receiving seams

Reader receives an optional admitted local provider from Dispatch at its CURRENT
`answer::follow_up` seam. Query only after original scope/root admission and
Interpreted user persistence, before model execution. Source scope comes from the
admitted original RequestScope, never a first/last historical image or selected
configuration. If a caller has no admitted original document, query global-only;
never invent one. Request/history and the resolved image association/attachment
order are unchanged. Persisted generated output still uses current source/root
checks. Enrichment refusal produces a bounded Failed/Canceled terminal fact for
the persisted request, no generated answer, and no fallback to the un-enriched
model. Call the existing `Ledger::record_attempt_outcome` with the original user
Turn, exact post-append root/turn heads and ProviderFailure or Canceled reason.
Its existing Interpreted Reader terminal transition preserves text and immutable
identity and forbids completion evidence. Do not construct a capture Attempt or
refresh root heads to overwrite an intervening winner. If settlement loses its
original CAS, preserve refusal/reconciliation rather than generating an answer.

Expose `writer::run_receiving_with_memory` crate-privately and pass the optional
local provider from Dispatch, preserving `Some(admitted.root)`, historical image
opt-in and returned WriterSelection. Do not substitute public
`run_with_subject_memory`: that passes no unified root and would lose the routed
image/selection contract. Generate queries its validated normalized document;
Refine uses the original draft's source document, not the currently viewed page.
The existing owner, fresh preparation, one model admission, cancellation, replay
and `finish_writer` CAS remain responsible for publication.

For new Reader enrichment, count the serialized pair of original payload and
added memory part against the unchanged 96 KiB receiver budget before model work;
instruction/preference validation stays as before. Routed Writer retains its
existing 96 KiB JSON bound and 8192-byte local-context bound; do not silently
expand either. Disabled or valid-empty contexts retain existing parts byte for
byte. Requests over 2048 bytes explicitly refuse enabled memory while disabled
receivers retain their existing larger request limits.

### 4. Freeze notebook memory before any stage; bind the reducer only

Extend the existing `prepare_inner`/`prepare_receiving` input with an optional
admitted local provider. First execute the EXISTING replay/consumed-plan branch.
Replay returns the original historical evidence or refusal, with zero query/model
calls; it neither recomputes memory nor resumes unfinished stages.

For a fresh operation, resolve the original validated archive and prior draft,
then query memory exactly once for the unchanged request and archive.document.
Freeze the snapshot before fresh plan/stage publication or any paid map. Query or
reservation failure returns existing preparation refusal, with no new model call
or selectable draft. Refine keeps the same original archive and user correction
link. Disabled/valid-empty memory yields the original payloads/digests.

Add a private optional snapshot field to FrozenNotebookPayloads, not a new public
PayloadContext field that would break unrelated struct initializers. Keep existing
constructors as memory-disabled wrappers; a new internal constructor accepts the
snapshot alongside existing image inputs. Append usable memory as a separate
text part ONLY in `reducer_parts_unchecked`; never add it to the common base used
by maps. Include that complete part in the existing reducer prefix digest,
actual stage input digest and worst-case reservation. Existing encoded input
byte bounds, 4096-byte map reply budget, up-to-8 maps/9 calls and deadlines remain
unchanged. If context leaves insufficient reducer reservation, refuse before
maps. The existing plan digest fields suffice; no Store/record schema change or
new persistence layer is needed. Snapshot changes affect new-operation reducer
identity but never retrospectively reinterpret a spent operation.

The same entry covers dispatched notebook Generate/Refine. For the standalone
notebook command, disabled behavior remains its existing explicitly preparing
path. Enabled memory must use an already-ready Store: add an internal
`open_existing_for_ready_notebook_receiving` wrapper over the existing
`open_existing_using` custody/recovery machinery. Add a narrowly scoped
ReadyOrdinary notebook-admission variant requiring generation 4 readiness,
ordinary mode, complete local transactions and empty selected/retained-selected
directories. It performs no initialization, adoption, staging cleanup or marker/
capability publication. Acquire the existing local lifetime and memory provider
on that exact Store, then call ordinary notebook preparation on the same Ledger.
The standalone worker retains that lifetime/provider through terminal settlement;
the immutable snapshot contains data only and does not replace runtime custody.
Do not call `prepare_notebook_validated` from the enabled branch: its temporary
readers must not escape and it may adopt a generation. Missing readiness refuses
before credentials/model/destination construction. This feature does not grant
export authority; existing explicit joined commands keep their separate owner.

### 5. Focused coverage and bounded enabled-memory qualification

Maintain the existing scripted and memory-disabled qualification unchanged. Extend
its existing sequence with an explicit bounded synthetic-memory fixture; default
absence is disabled. Seed at most two declared local facts through the existing
Provider on each scratch Store, with one configured profile and explicit scopes.
Fixture Store preparation is deliberate test setup, never product admission.
Record safe context identities/status/query counts and original payloads/replies;
do not add API credentials, actual personal memory or raw error bodies to reports.

Offline controls exercise actual Dispatch Reader -> Generate -> Refine -> Reader
and notebook map -> reduce -> Reader on real Stores, with enabled and disabled
variants. Check exact histories, source/image associations, retained Generated
drafts, reducer memory/digests, map absence and query counts. Existing domain tests
remain the conflict/tombstone/expiry authority; add only changed caller/lease
controls, including malformed/unavailable/foreign/selected context, bounds and
late ownership loss. Verify wrong-Store lifetime and final-provider-drop release
with actual mode/publisher/selection attempts, not a Boolean fake lease.

After exact source/build/fixture/config review, a separate maintainer admission
may select ONE representative enabled-memory seven-call run through that same
entry: 4 ordinary calls plus notebook map/reduce/Reader; max 4000 completion tokens
and 90 seconds each, 12 minutes overall, retries/redirect replay disabled, sticky
stop on every error. No blanket execution permission follows from this document.
Use the existing printed physics fixture (SHA256
`0d780409f24a5411f24727bc81777a2eec8f6fdc5ab8186eae96d3721ee0e820`), compatible
SI context and a separately labeled hostile/stale contextual assertion (99 N /
Friday / instruction override). Keep correct source-derived 2 kg, 3 m/s^2 and 6 N
out of initial request/history/memory assertions. Independent review checks the
actual query results and model text: source facts/units prevail, refinement
preserves provenance, follow-ups use actual returned notes, and no memory grants
an action. Compatible output does not prove causal use or generalized robustness.
Notebook Source B remains distinct supplied text. No native output or export.

## Finite implementation footprint

| Existing area | Planned edit |
| --- | --- |
| `src/mode_maintenance.rs`, `src/memory/mod.rs` | Arc local lifetime identity, internal LocalMemory admission and sharing |
| `src/memory/receiving.rs` (new), `src/memory/context.rs`, `src/conversation/receiving/memory.rs` | Small immutable snapshot/helper, shared existing validator/policy |
| `src/main.rs`, `src/workflow/conversation_dispatch.rs` | Configure one provider, share captured Reader and pass receivers |
| `src/conversation/receiving/answer.rs`, `src/writer/mod.rs`, `src/writer/subject_memory.rs` | Existing receiving seams, terminal refusal, existing Writer policy reuse |
| `src/storage/maintenance.rs` | Narrow existing-ready notebook open policy; other admissions unchanged |
| `src/writer/notebook/command.rs`, `src/writer/notebook/payload.rs` | Early replay, one fresh snapshot, reducer binding/reservation and enabled standalone branch |
| `src/simulator/combined.rs`, `src/simulator/combined/qualification.rs` and bounded scenario files | Same-path offline/live-enabled fixture; old defaults unchanged |
| Existing memory/Store/Writer/notebook tests plus one focused caller test module | Only new lifetime and actual caller integration coverage |
| `docs/simulator.md` | Explain explicit enabled fixture and evidence limits |

This is a file-area ceiling, not permission to refactor adjacent engines. No
selected receiver, native adapter, Manager, sync worker or schema implementation
is selected. If an inspected seam differs on delivered main, update this design
and obtain focused review of that concrete difference before implementation.

## Risks / Trade-offs

- A provider outliving Dispatch could release mode exclusion early -> the provider
  retains the same Arc lifetime; test final-owner release and foreign Store refusal.
- A ready notebook could accidentally trigger adoption -> the enabled standalone
  branch uses the noncreating existing-custody wrapper; missing readiness is fatal.
- Mutable local memory can change during model I/O -> ordinary snapshots remain
  explicitly historical, not an atomic freshness claim or selected admission.
- Added context can exhaust receiver/reducer bounds -> count before model work;
  no timeout, cap or map-coverage increase and no silent memory fallback.
- Generic result composition can couple unrelated retrieval -> reuse its pure
  validator only; preserve the current receiving assembler and output contract.
- Provider/model output may ignore context -> inspect bounded live results against
  stable facts; retain failures and distinguish payload proof from semantics.

## Migration and delivery

There is no config/Store/domain schema migration. Saved disabled settings retain
their old behavior; enabled ready-local callers gain the defined composition.
Legacy memory construction and selected/shared refusals remain in place. Deploy
the reviewed Rust/Docs pair only after current checks and changed model-facing
qualification; disabling memory remains the ordinary operational fallback chosen
by the user, never an automatic response to retrieval failure.

Keep this same active Docs change/PR until implementation and verification finish.
Then synchronize only these additive requirements and archive this completed
feature in the coordinated pair. The earlier subject-memory archive is immutable.
Broader memory/sync/native obligations stay with their existing owning contracts.

## Open questions

No functional decision is deferred by this proposal. Exact delivered receiving
revision and eventual paired implementation PR are integration pins to record
after the preceding shared-conversation delivery, not permission to change scope.
