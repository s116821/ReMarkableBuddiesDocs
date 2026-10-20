# Proposed narrow public host contract

This contract was published and independently accepted before code. The paired
implementation candidate now supplies this workflow; final CI/review/delivery
remain gates, recorded in results.md.
Producer protocol is pinned to Docs68 at64ff69baf2e066f203eadd587cb2d3864173b1a6,
including its exact matrix and envelope-golden.json. Root review5583470985 found
atomic-local-publication and historical-content gaps in the preceding packet;
corrected producer acceptance is recorded in review5583523433, and consumer
precode acceptance in review5583665573. Actual producer delivery remains a gate.

## Public entry and exact requests
One optional ManagerHost.memoryForget(request), one authenticated loopback POST
/manager-memory-forget and one authorized main-frame IPC manager:memoryForget,
with exact arity1. Every request is strict canonical JSON, <=2048 UTF8 bytes:

- status: {action:"status"}; host state only, no device command.
- prepare: {action:"prepare",connection_id:HEX64,boot_id:UUID,key:GLOBAL_KEY}.
- confirm/receipt/cancel: {action:ACTION,reference:HEX64}; no replacement fields.

Only canonical nonnil lowercase UUID global keys are initially supported. UI
preparation starts from one currently displayed supported single-value inspection,
then requests a NEW producer prepare for that key. Neither search nor inspection
mints permission. Exact valid prepare response, not old UI content, supplies the
confirmation preview. Caller paths, commands, operation UUIDs, expected heads,
private intent/pins/configuration and arbitrary target overrides always refuse.

status returns only the fixed reduced state below, including an existing uncertain
reference while original private bytes remain. It never returns an executable
prepared preview to a newly loaded renderer; navigation/refresh invalidates ready
confirmation first. A retained unknown slot may be recovered for explicit read-only
receipt lookup in the same host after original target/boot verification.

## Reduced response
Outer fields: {contract_version:1,status:OBSERVATION_STATUS,observation:SAMPLE_OR_NULL,
forget:{state,reference,preview,acknowledgement,report}}. status/observation retain
existing wired observation validation; host-only status has no fabricated sample.

state is none|preparing|prepared|confirming|checking-receipt|invalidated|busy|
unsupported|unavailable|not-dispatched|unknown|unresolved|acknowledged.
reference is null or a fresh opaque64lowercasehex reference. It is not a CLI intent,
write token or authority to choose a target. Only state prepared has nonnull preview:
{key,head:{record,revision,fact},scope:{kind:"local"|"selected",group:NULL_OR_UUID}}.
The full supported Fact is displayed unchanged; key/profile/derived record match.
Selected group comes from the same admitted private domain identity; local means
local memory, not proof an explicit LocalOnly mode was saved. Target is the original
verified outer observation/connection/boot, shown explicitly with the fact/effect.
No parents, content hashes, mode tokens, roots or accepted-generation pins enter
this projection. It is a single supported value; no conflicting head is filtered.

acknowledgement is null or {operation:UUID,transaction:UUID}, only in acknowledged
state and only after both exactly match the retained original operation/report.
It acknowledges a historical logical transaction, not that current data is deleted
or that every preparation field was historically consulted. No optimistic removal
or current-deleted label; current heads require separate deliberate inspection.

report is null or {selector,status,incomplete,outcome}. selector is prepare-forget|
forget|forget-receipt; status/incomplete/outcome preserve the exact producer matrix.
outcome is null|acknowledged|not-dispatched|unknown|unresolved. Never infer flags from
status alone. Prepare has null outcome; acknowledgement and failure shapes must
match their phase exactly. Unknown/unresolved retain original mutation uncertainty.
Local stale/caller/transport failure has report:null, never a fabricated CLI report.

A competing prepare returns busy for that call without replacing the global slot.
A stale/duplicate confirm refuses without resetting the retained state. Public
helpers/IPC and controller validate the reduced view and strip private fields.

## Single live-host slot and claim
One pending slot per actual helper/Electron main process, shared by all its tabs/
renderers. Reserve it synchronously before awaited prepare I/O. It contains one
immutable original intent UUID (host generated once), exact original report bytes,
fixed confirmation-input bytes, their digests, preview digest and verified target/
boot, host-instance identity and confirmation-observation epoch. Reference generation
uses existing maintained host crypto primitives, never a new signing/SSH identity.
No second preparation overwrites it; state preparing/prepared/confirming/unknown/
unresolved/checking-receipt is Busy to competing preparation.

A prepared preview expires after120000ms using host monotonic elapsed time. Check
reference, state, deadline, original host/observation epoch and original target/boot,
then synchronously claim prepared->confirming BEFORE any await or confirmation child
spawn. Claim is irreversible: cancel/error does not rearm it. Duplicates cannot
send a second CLI confirmation, even with the same reference or operation UUID.
Explicit cancellation before the claim is nonmutation and invalidates the reference.
After claim, any missing complete validated report/zero exit stays unknown unless
an exact complete matching producer row proves not-dispatched or acknowledgement.
No automatic resend/reprepare/new UUID/headset/mode or private-packet replacement.

The initial scope is per-host-process, not a cross-process registry. Separate hosts
cannot use another instance's reference; producer atomic conditional publication
must handle independent intents racing on the same target. No durable/global claim
is promised by a Node event-loop reservation.

## Invalidation, receipt and restart
External observe/tablet read, navigation/refresh, cancel/disconnect, known config or
connection/boot change and other maintenance invalidate ready confirmation, including
repeated IDs. After possible dispatch clear stale detail/preview but retain original
private bytes and unknown state in that live host; do not use renderer clear() to
erase host uncertainty. Controller generation checks suppress late view restoration.
A late exact acknowledgement may settle the host's retained historical record; it
cannot resurrect stale preview/current-data success in an invalidated renderer.

Receipt is a separate explicitly requested read-only action. It is available only
for a retained possible-dispatch intent, never as a confirm fallback. Same live host
identity/auth session plus reverified original wired target/boot is required; changed
identity/config/mode/domain pins conservatively remain unresolved. A new observation
epoch may allow receipt after same-target verification, but never rearm confirm or
replace any original binding. Producer receipt-only must not mutate when absent.

No localStorage, settings, credential store, database or durable journal stores the
private intent/reference. Full helper/app restart loses custody and old references
are unavailable. A surviving controller with previous possible-dispatch state keeps
an unresolved/unavailable notice when new host status is none; none means no retained
record, NOT no historical dispatch. A completely restarted UI cannot reconstruct
unknown history and always explains this limit. No durable recovery is implied.
An already retained historical acknowledgement can be returned for the same exact
receipt reference without another CLI dispatch; a cancel race never erases it.
A new pending preparation hides any older terminal public reference, so stopping
it invalidates that current reservation rather than targeting an old record.
Initial uncertain live-host slots permit receipt-only; they are not silently evicted
to make room. If custody is lost, a later deliberate fresh inspection and new user
preparation/confirmation is a NEW intent, not replay of uncertain work. No restart
or fresh inspection automatically generates it. A proved not-dispatched or historical
acknowledged terminal slot may be replaced only by a new explicit preparation.

## Bounds and private encoding
Existing fixed env-i HOME/PATH/configuration/Reader path and protected Linux/Windows
wired callbacks are reused. Fixed selectors only: prepare-forget, forget, and
forget-receipt, each --memory-input - and EOF; no arbitrary argv or remote staging.
Private CLI input <=131072 bytes; raw stdout <=262144 including LF, stderr discarded
and capped16384; private child request/response <=360448 (bounded base64 exact raw
bytes plus observation), public response <=65536. Use existing2/8/12/13/14-second
channel/collection/Python/Node/browser hierarchy. Exceeding a smaller host cap refuses
the complete operation/view. No partial report, retry or empty-success substitution.

Privileged Python rejects duplicate/unknown fields, invalid UTF8, multiple/trailing/
partial JSON before returning exact original stdout as bounded base64 privately.
The host decodes/strictly validates, retains exact original UTF8 bytes and constructs
fixed {intent:ORIGINAL_INTENT} confirmation-input bytes ONCE with unchanged values.
Those exact input bytes are reused for explicit receipt only; no rebuilt heads/pins.
No original private base64/packet is accepted from public requests or returned publicly.
Preview must roundtrip to the supported canonical Fact and match the producer's
exact typed Envelope canonical SHA, original operation/Key/revision and bindings.
Pin lists are bounded/sorted/unique and UUID/digest/version shapes exact. No live
SelectionToken is recreated or private root treated as authority. Preview numeric
values must be exact safe integers, not rounded. The config/pin hash interpretation
is producer owned; no alternate JavaScript JSON ordering is invented.
