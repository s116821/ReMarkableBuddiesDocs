# Development capture owner refusal consumer amendment

Status: Main accepted the consumer contract at `0aef35c`; source implemented and
tested at the checkpoints below. SDK source is independently accepted; Main independently accepted consumer source0860464; acceptance is source-only.
SDK authority is docs-only `fb32d57c1b623ef1ea233a3f2da9a49c6d78f368`
(with `4a374ceb272542d45f2452e062ed2c079e6d09d6`), specifically
`openspec/changes/establish-native-platform-contract/capture-owner-diagnostics.md`.
Previous implementation baseline is SDK `f0e6ff4ccb37b887f7f278b0b820a7d047de1559`
and Buddy `42e4b02f81a5433ce3d6b9503036761ae82a16a3`.
Main owns target operations and canonical persistence, Sol owns ordinary source
implementation, and Astra owns specification and independent source/native review.
No artifact, fresh nonce, device attempt, retry or native qualification is selected.

## Scope and original failure

Consume the one additive `capture-owner-refusal.json` only in default-off
developmentCaptureObservation, setup120000/facts5000. Preserve the existing
four-field callback, `capture-observation-owner-refused` stage, capture completion
version1 and ordinary facts/input behavior. The diagnostic is historical failure
evidence. It cannot set capture_verified, facts_verified, candidate qualification,
visual acceptance, native_authority, render_authority or ui_acknowledged true.

The spent10a attempt exercised owner refusal, produced no image/completion/facts,
and restored stock. Its original operator receipt remains cleanup_verified=false.
Main separately preserved the exact106-byte request and removed the owned Qt/helper
directories under reviewed historical recovery R2; the separate closeout records
cleanup success. These facts do not identify the original failed owner predicate.
Preserve both receipts and all spent evidence without rewriting them or replaying.

## Strict raw schema and original identity

Before value decoding, cap UTF-8 bytes at8192, require one JSON object, and reject
duplicate decoded top-level names ordinally, including JSON-escaped aliases. Do
not let ConvertFrom-Json collapse duplicate names. Require exactly these29 fields:

`kind`, `version`, `nonce`, `attempt_pid`, `attempt_start`, `root_device`,
`root_inode`, `setup_profile`, `capture_accepted_ms`, `failure_ms`,
`deadline_check_ms`, `effective_deadline_ms`, `branch`, `predicate`,
`discovery_result`, `visited_items`, `receiver_candidates`, `scene_candidates`,
`matched_pairs`, `first_pair_receiver`, `first_pair_scene`,
`first_pair_rejection`, `active_owner_rejection`, `observer_role`,
`observer_member`, `observer_failure`, `native_authority`, `render_authority`,
`ui_acknowledged`.

Require kind=development-capture-owner-refusal, integer version1, the exact selected
nonce/profile and original attempt/root tuple. Process/start/device/inode are
positive canonical decimal strings, at most20 digits and within uint64. Bind them
to independently retained original attempt/request/root evidence, never a newly
selected process or current stock PID. All three authority fields are actual
boolean false. Missing/extra fields, wrong types, unknown enums and inconsistent
combinations refuse diagnostic decoding, without erasing the original refusal.

Times are nonnegative Int64 JSON integers, not floats/strings/bools.
0 <= capture_accepted_ms <120000; effective_deadline_ms equals
min(120000,capture_accepted_ms+5000). Failure latch time is at least acceptance
and may be at/after the effective deadline: expired failure evidence is valid
historical evidence, without admission or additional execution budget.
If populated, deadline_check_ms is the original compared operand, between
acceptance and failure latch; it is populated only when the evaluated failed
progress/allowed predicate is deadline, and then is at least effective_deadline_ms.
Otherwise it is null. No later timestamp can reconstruct a skipped comparison.
Host150000, rollback180s and restoration240s and all original origins remain.

## Normative branch and nullable detail

The closed SDK enum registries at the authority above are normative. Decoder
constants enumerate them literally; runtime object names/signatures are never
accepted as additional enum members. Progress predicates are context/live/
invalidated/token/deadline. Allowed predicates are reentrant-check,
invalidated-before, context-before, lifetime-before, active-owner,
invalidated-after, context-after, lifetime-after, owner-pointers, owner-threads,
deadline. Discovery result uses the existing finite open-* result registry.

| branch | predicate | discovery_result | permitted detail |
| --- | --- | --- | --- |
| initial-progress | failed progress enum | null | all counters, pair, active-owner and observer fields null |
| owner-discovery | failed original progress enum or null | actual non-success discovery enum | original reached counters; first-pair tuple only for open-owner-unavailable; final active-owner rejection only for original final validation failure; observer fields null |
| observer-install | null | open-owner-observed | required fixed observer tuple; all counters, pair and active-owner fields null |
| owner-revalidation | failed allowed enum | open-owner-observed | active-owner rejection required only for active-owner predicate; counters, pair and observer fields null |

For discovery, a populated predicate implies open-context-lost. Pointer loss after
successful progress leaves predicate null; never infer a progress failure from
open-context-lost alone. A final active-owner rejection requires open-context-lost
and predicate null, rather than replacing the first rejected pair explanation.
Both reasons use the SDK's fixed grouped predicates, not arbitrary strings.

Counters are null when their existing local initialization was not reached;
otherwise integer visited0..4097, receiver/scene0..9, matched0..2. Zero is observed
zero, never an unevaluated marker. matched is null before its original initialization;
no new traversal allowances arise from accepting the one overflow observation.
Open-engine-thread/current-window-unavailable have all counters null. Unavailable/
ambiguous have evaluated counters and matched0/2 respectively.

The first-pair receiver/scene/rejection tuple is all null or all populated. Populated
ordinals are integers0..7 below their respective evaluated candidate counts and
occur only for open-owner-unavailable with matched0. No candidates means no pair.
It records only the first original rejected pair, with receiver-document or a
fixed original active-owner group. It does not attribute that reason to all pairs.

The observer tuple is required only for observer-install. Role=document/scene/
receiver determines the closed existing11/4/4 member registry. Failure is one of
object-missing/property-missing/notify-missing/signal-missing/slot-missing/
return-type/connect-failed, at the original metadata check. Do not add property
reads, observers or acceptance checks to diagnose metadata.

## Bounded collection, preservation and exact cleanup

Use a separate diagnostic collector/decoder, never a successful capture fallback.
Main supplies the existing bounded read/copy transports. Positive absence is a
separate state from complete collected bytes, decoded evidence and unknown output.
Do not stop historical diagnostic collection just because capture completion is
absent. Bind reads to the existing held owned root, owner nonce, original attempt
identity and expected root signature; after restoration use retained original
identity, verified stock restoration and attempted-process absence, not live
candidate qualification. Keep each transport bounded and no publication retry.

For present output, require regular no-follow0600/current owner and <=8192 bytes.
Record size/hash/name identity, copy to an exclusive local path, independently
hash exact bytes and recheck the same owned root/name/file metadata and hash.
Complete matching copies are preservation knowledge even if raw JSON is malformed,
partial JSON, extra-field or undecodable. The decoder flag stays false. A timed-out,
truncated, replaced or mismatched copy grants no preservation flag; retain exact
remote evidence and restoration duty. Save verified bytes/hash before decoding or
later guards, so a later refusal cannot erase preserved-copy knowledge. Do not
rewrite original operator receipts to add flags; a historical recovery receipt is
separate and cannot upgrade original admission flags.

Add exactly capture-owner-refusal.json to capture-mode stale refusal, known output
preservation and exact-name cleanup. Cleanup requires matching complete local
bytes/hash or positive absence for this file, alongside all existing outputs and
stock/owned-root guards. Unknown diagnostic evidence retains the stage. Malformed
but completely preserved bytes can be removed only under the same independent
restoration/ownership guards; malformed diagnostics never authorize capture/facts.
Never remove foreign/preexisting output. Quiet ownership/stock guards around a
strict single-row preservation response must not contaminate stdout with status
lines. Recovery has its existing bounded duty; no diagnostic publication/read can
delay or replace it, restart timers, alter deadlines or select another input.

## Source acceptance gates

Freeze this amendment for Main read before source implementation. Then implement
SDK and consumer with default-null sinks, exact original evaluation/call counts,
first-failure sticky latching and unchanged callback. Focused fixtures cover all
four branches, every finite registry, null vs0, overflow, pair/observer tuples,
deadline equality/expiry, producer loss without fabricated progress reason,
identical/escaped raw duplicates, absent/malformed/partial/replaced output,
complete malformed-copy preservation, unknown retention and callback compatibility.
Exercise actual source collection/cleanup guards with mocked transports, including
quiet/noisy stdout and copy knowledge surviving later refusal. Re-run affected
entry/capture fixtures; host passes are source evidence only.

Independent exact SDK/consumer source review, artifact build/provider review,
private packet review and Main-only actual native selection remain separate.
Task4.11 and SDK native owner/render qualification remain open.

## Independently accepted source checkpoints

### Proposed integrated historical request closeout

Main's prepared-packet review found that the accepted live capture collector
copies the request only after completion. Owner refusal with no PNG/completion
therefore correctly retains the stage because the request has no saved copy.
This does not reverse diagnostic source acceptance. The current prepared packet
is held from execution until the following narrow extension is reviewed.

After mandatory stock restoration, preserve exactly
`capture-observation-request` and `capture-observation-request.tmp`
independently of capture completion. Each read uses the retained pre-arm root
device/inode, owner nonce, original attempted PID/start and quiet restoration
guards before/after metadata. Require regular non-link mode600 files capped at
256 bytes; bind size, digest and file device/inode before/copy/after. Save each
returned file to a separate exclusive local path. An existing successful request
copy may be reused only when its original verified flag, digest and exact bytes
match; never overwrite a local or remote file.

Cleanup knowledge requires exact UTF-8 canonical tuple bytes:
`nonce PID start dev ino capture-observation 120000 main-dev-facts-120s` plus one
newline. Length is computed from that exact original tuple, not fixed to the
historical ten-a byte count. Malformed/partial complete copies are retained as
historical evidence but refuse closeout. Transport uncertainty, metadata
replacement or later binding loss also retain the stage; a known complete copy
is not discarded by later refusal. Positive absence is distinct from unknown.
The temporary request uses its own path/flag/digest, so different bytes cannot
borrow preservation knowledge from the consumed request.

This source-only extension does not alter SDK/publisher binaries, capture/facts
admission, callback, deadlines, recovery clocks or original receipts. Regressions
must execute the actual restored collection/cleanup path with mocked transports,
cover refusal without completion, both names, differing temporary bytes, absent,
copy/metadata uncertainty, partial/malformed data, replacement, noisy output and
foreign local paths. Independent source review and a newly frozen private packet
remain required before Main-only execution selection.

SDK `1d221d73c8e2a2a19bfb2d1b37c09bca41d554ed` implements the additive latch;
`117fd0e8ccc4954545b33d91900a6ff0d4eabf20` adds stronger fixtures without
changing the SDK headers. Vendor Qt 6.10.3 ARM/QEMU capture42 passed, including
17 diagnostic modes with full29-field/null expectations, discovery progress
versus final active-owner loss, queued/no-event reentrancy, candidate/topology
bounds and ambiguity. Entry32, refusal-format21, input17 and originalcapture25
also passed. Astra independently reproduced capture42 and accepted exact117fd0e after header-hash and full-delta review. Queued reentrant traversal is deliberately fixture-induced by direct execution while the acceptance queue remains pending; it is not evidence of two ordinary production traversals.

Buddy `99066932571ccaf6ab49b6b0689b5fadce7b0a33` implements independent
restored historical preservation, raw strict decoding and exact-name cleanup;
`28bc8ba3eaad8a8b4096fe39763bfd08285bd507` strengthens finite registry and
reached-counter tests/validation. Repair `08604646d686057686f6438dd7729e04ef56394c` rejects impossible post-traversal overflow and context-phase combinations found by Main independent review. Owner proof/collector292, captureproof156,
collector40 and actualsourceintegration18 passed with host/mocked transports.
Complete malformed/empty bytes remain preservation knowledge; unknown copies or
later binding loss refuse cleanup. No capture/facts flags are upgraded.

Main independently accepted exact Buddy0860464 after full source/matrix review and independent owner292/sourceintegration18, with prior proof156/collector40 unchanged. These are source-only checkpoints. Task4.17 is checked for completed source implementation and independent review. Artifact/provider/private-packet/native selection remains
separate, and task4.11 remains open.

Source basis: current SDK proposal/source read directly; current Main accepted
contract messages; independently read private10a actual raw/callback/operator and
historical recovery receipts, with no public links; current repository checkpoints
and local/QEMU test outputs. Current Main and Astra independent source acceptance messages; native qualification is still pending.
