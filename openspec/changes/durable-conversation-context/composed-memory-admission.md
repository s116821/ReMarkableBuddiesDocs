# Composed subject memory and selected Reader admission

## Concrete requirement and existing dependency

REM-24 requires optional associative context after verified transcription, with
current source/request precedence. REM-37 requires acknowledged selected drafts
without ordinary fallback. Existing memory Pins retain catalog/all aggregate
admissions, original tokens/raw heads, cumulative budget, provider instance,
payload identity and consumed state. Reader owns its actual selected write and
mode lease. These contracts are ready; qualified native acquisition is not a
prerequisite for this data-only integration.

Current prepared-data entry refuses Some(memory) because memory.with_current's
callback around Attempt.generated would reacquire an already-held Reader gate
when document keys overlap, or invert independently acquired locks. Replace that
refusal only for an actually compatible selected memory provider and one combined
ordered publication path. Do not add a transport, registry or SDK DTO/facade.

## Controlled combined publication

Add an actual Provider capability for selected Reader compatibility and selected
text publication using existing QueryResult, SelectedAdmission, SelectionToken
and SelectedReaderWrite/Publication. Default providers refuse; SelectedMemory
checks same Store handle, group and binding. A compatibility check is setup
validation, never current authority. Unsupported/foreign providers continue to
refuse before query/model/state installation.

SelectedMemory verifies original instance and sealed result payload, then passes
its actual catalog/aggregate admission handles to a crate-private controlled
Reader publisher. That publisher joins its own admission with the existing set
through SelectedAdmission.with_gates, which deduplicates equal keys and locks in
one canonical order. It owns the entire lock set and invokes the extracted
existing selected writer body under that set, never the public locking writer
from inside a callback. No raw backend or caller-created lock permission is exposed.

Under the combined set, validate memory tokens AND raw heads against the same
remaining receiving budget, completeness and payload/consumed seal. Then validate
the Reader's current token, root/user/source/media and mode, and publish the
existing selected draft/receipt transaction. Preserve all input invariants and
exact user capture ownership. Hold the actual shared mode lease through the
operation; no local/None lifetime lease is invented.

Recover an exact original Reader operation before current memory/Reader refusal,
returning Historical only and performing no new consumption/publication/native
effect. This is original text acknowledgment, not current memory usefulness or
fresh permission. A new operation cannot consume an altered/foreign/used/stale
memory view. Mark the receiving view consumed before the actual new handoff, with
sticky failure/panic semantics; no output or acknowledgment retry republishes.
Actual Attempt freezes its write IDs/time/text/original pins once and installs
state only from Published. Historical replay cannot initialize current state.

## Actual application route

Keep recognition and independent transcription verification unchanged and reuse
exact acknowledged selected image bytes. Interpretation publishes first; memory
query/enrichment then uses the interpreted current state. Selected Generated
publication goes through Provider's combined method, not memory.with_current
around the ordinary publisher. Ordinary Reader behavior retains its existing
path. Disabled/unsupported memory is explicit; empty/partial/budget refusals stay
faithful to existing memory policy. Preserve result identity and current Reader
progress checks during provider work. No source pixels, question, machine prompts
or stored transcript are silently changed by memory retrieval.

This enables data-only draft publication. Qualified Source/Binding/Pending/native
dispatch/settlement, installed acquisition, live-model effectiveness, SDK source
semantics and full lifecycle remain open. Remove the current Some(memory) refusal
only where the actual selected provider compatibility path is implemented.

## Verification and delivery

Independently review before code. Use actual combined publication and Orchestrator
controls for same-key and distinct-key sets, reversed construction order, opposite
concurrent operations, replacement of Reader/catalog/fact scope, mutated/foreign/
consumed result, budget exhaustion, source ownership and exact image order,
BeforeCommit/lost acknowledgment/historical retry, disabled/empty/unsupported
providers and zero publication on refusal. Bound deadlock controls with existing
test subprocess/deadline tools; a timeout fails instead of hanging the suite.
Verify other document/profile records and unbound Reader behavior are preserved.
No native/device/provider call is qualified by recording fixtures. Run affected
exact committed-SDK checks, required strict lint without suppression and scoped
independent evidence review. Keep the twenty native diagnostics and larger gates
honest; no repeated unrelated matrix or premature merge/archive.

Source basis: current REM-24 description/newest timestamped comments, existing
selected memory Pins and Reader publisher, canonical shared gate implementation
and Root's current dependency-order instruction. This is precode, not delivered
composed behavior or native qualification.
