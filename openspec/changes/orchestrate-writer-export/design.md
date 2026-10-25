# Design

## Authority and current paths

Read the current REM-23 description and complete timestamped discussion, current
owner/reviewer scope clarification, actual Writer/export code and simulator
contracts. Current actual main is Source1d1665f / Docs22773ea. The closed
generate-writer-drafts implementation, original two-call quality and all failed
heads remain historical evidence; they are not new joined-flow qualification.
The optional shared field-notes endpoint was advertised but returned tool-not-found;
the accessible issue chronology and source remain the authority, with no repeated
integration question.

Existing `writer::run` prepares/commits unrendered drafts; its command resolves
model configuration before opening the Store. `note_export::export` independently
admits a prepared artifact and owns Mem discovery/read/write/reconciliation.
Its later root capture does not fence an earlier Writer selection. That is valid
for its caller-supplied PreparedNote contract, but a joined flow must add its own
selection/intent boundary. Simulator scenario validation and documentation still
reject Writer/combined. Reuse these implementations; no OCR/export-mechanics
replacement or renewed commodity-backend survey is needed.

## Commands and compatibility

Extend the existing `--writer-note` dispatch with strict distinct command tags:

- `generate-and-export`: existing Generate request plus outer-operation,
  correlation and export-effect identities.
- `refine-and-export`: existing Refine request plus those identities.
- `export-draft`: explicit conversation/current-draft selection and fresh outer
  intent/correlation/effect identities; no model credential or model invocation.
- `reconcile-export`: explicit conversation/correlation using only existing
  known-ID reconciliation; no generation or create/update.

Use strict nested existing request types, reject unknown/duplicate fields and
invalid/colliding identities, retain the existing 256KiB command/40KiB source/
48KiB Source-record/24KiB draft bounds, and preserve legacy command JSON/output.
Keep the existing public legacy command entrypoint; main may use a compatible
dispatcher that serializes legacy reports unchanged and a distinct joined report.
There is no new daemon/admin API, automatic menu interaction or Manager surface.

Validate the complete request and resolve every required credential/configuration
before durable admission: model credentials for generation/refinement, MEM_API_KEY
for a sending/reconciliation command. Reuse existing precedence/resolvers and
fixed production Mem construction; no key argument, secret logging, account
search, new credential store or unreviewed endpoint override. Missing Mem
credentials must not cause a paid generation first. Tests use synthetic
credentials and injected loopback destinations through the production adapter.

## Fresh outer intent and interrupted phases

Persist the full outer request fingerprint under its distinct operation UUID
using existing Ledger receipt/publication machinery. No second registry and no
reuse of native admitted-intent records. The admission is an ordinary domain-one
receipt/root publication; existing schema/serialization remains intact.
Only a positively fresh observed commit yields a private invocation-bound grant.
Lost admission acknowledgment and receipt replay yield no grant and do not poll
either model or destination, even if a draft is already present.

Outer replay NEVER automatically continues from a historical Generated report.
It returns a truthful historical/interrupted or cached historical-export outcome,
without remote polling. To resume an interrupted draft-to-export gap, the caller
must issue a new explicit selected-draft export intent. A previous uncertain
export must first use existing reconciliation; a new effect ID cannot bypass it.
Deliberate re-export retains correlation and uses a distinct effect identity.
Reusing any operation ID for changed request/content refuses.

The report separates model outcome, selected draft and export disposition.
Generated means a durable proposal, never sent/verified/native-completed.
Legacy generate/refine remain review-first and cannot become sending commands.

## Exact selection and the freezing cutoff

The fresh producer returns a private committed draft/source snapshot, not a
permission reconstructed from serialized Report fields. Explicit export-draft
captures the conversation root before selected reads and obtains the exact
current draft/source values and immutable revision references from that view.
Do not recapture a newer root after body construction and silently accept it.

Carry the fresh outer grant and selected root/draft/source references into the
same atomic Ledger publication that admits the existing export attempt. Validate
their exact heads/content and add required no-op guard revisions to that batch.
An import, edit, deletion, conflict or append before admission refuses the joined
export; no destination future is polled. The ordinary PreparedNote-only export
API remains unchanged; its new internal guarded variant accepts the typed
selection/grant and cannot manufacture them from a Generated report.

The outgoing body is frozen ONLY at successful guarded export admission, using
the selected committed bytes and digest; later reads never substitute content.
Dispatch eligibility remains guarded before the first destination poll and
again after pending discovery/readback before the first create/update poll.
Cancellation or selected root/draft/source change during that pre-write interval
records a positively known no-send/stale outcome and performs no write.
The exporter must not turn a historical/lost-ack admission into another send.

The first actual write-future poll is the irreversible/uncertainty boundary.
After it, cancellation/failure cannot claim no remote effect or undo; preserve
existing exact known-ID readback/reconciliation and no automatic write retry.
An already-started effect stays bound to its frozen body; new content requires a
new deliberate effect after the existing uncertain attempt is resolved.

## Ownership, cancellation and bounds

Compose the existing same-Store Writer and exporter owners in one fixed order,
nonblocking, for the complete joined invocation. Reuse their actual counters/
private typed owner tokens so standalone entrypoints contend correctly. Do not
add an unrelated third lock ignored by those paths. Failure to acquire either
owner is Busy before admission or provider cost. No Store index lock spans HTTP.

Refactor private owned helpers without changing the model prompt or existing
export retry policy. The existing joined/owned blocking-worker command pattern
must retain cancellation from model wait through export completion, join work
and release ownership on every outcome. The model retains its existing
cooperative bound; export retains its45s budget/10s request bound. Synchronous
Store publication is not preemptible; do not invent a hard wall-time guarantee.
Cancellation is latched before constructing/polling destination work, including
the boundary immediately after generation completion. No new live Mem call is
authorized by this implementation task.

## Simulator impact

Use `--simulate` mode dispatch into strict Writer host scenarios that invoke the
same production flow, Ledger and scripted destination contract. Bound scenario
steps/replies, declare normalized source units/page selection, and support Store
reopen plus phase-indexed cancellation/state/transport faults. Scripted scenarios
require no credentials/network. Separate real loopback HTTP integration tests
exercise the unchanged model and Mem transports with synthetic values.

Preserve existing Reader device scenarios/reports. Writer reports retain exact
draft/selected export content, ordered stage/destination traces, model/write
counts, source preservation and assertions; they emit no invented tablet PNG,
navigation/rendering or native authority. Reader history may be seeded through
the actual Ledger to verify same-conversation preservation, but that is not a
production Reader→Writer native combined workflow. Combined/native gesture
routing stays explicitly unsupported and separately tracked. Correct stale
Writer-absent/lifecycle documentation in the affected guides.

## Required actual-path cases

1. Direct generation/export creates one note; reopen, refine and deliberately
   re-export the same correlation updates the same remote ID/version.
2. Review-first generate/refine produces no destination polls; explicit selected
   export sends the exact chosen current draft, with no model call at that stage.
3. Lost outer admission acknowledgment, changed outer payload, successful replay
   and model-complete/export-not-prepared restart never create a fresh automatic
   model/destination call; explicit new export intent is distinct.
4. Draft/source/root changes between selection and export admission refuse; new
   state is not silently guarded while old text is sent.
5. Cancel after model completion/before first destination poll sends nothing;
   cancel or selection change while discovery is pending causes no write.
6. Lost export-prepare acknowledgment retains existing no-resend behavior;
   cancel before first write poll is no-send; lost response after write poll is
   uncertain and explicit reconciliation only reads the known ID.
7. Overlap with standalone Writer/export is Busy before cost; duplicate or
   incomplete markers, external note edits, provider/transport failure and
   oversized input retain truthful outcomes without retries or source loss.
8. Legacy Writer/export/Reader cases and scripted Writer host scenarios pass;
   optional memory is absent, combined/native mode refuses honestly, and no
   gesture/menu/source feedback operation is invented.

Use events/barriers and real operation hooks, not sleeps as success. Preserve
failed artifacts. Review current-head code/spec/HTTP/simulator evidence, then
sync/archive only this completed scope in coordinated Docs-first delivery.
