# Report3 Manager consumer design

## Bases and ownership

The producer is frozen at Buddy `2d7d8e9bf9f73f4ba7db9a282b4d0920887564bd`.
This consumer extends this same active change and Docs125 history, normally merged
with delivered Docs `68ac03324a63cd25af69565e099874eefcfc25e7`. Manager starts from
`7d8faaa4e9db56570eba06aa4ccd104d12621a5e`. The delivered Local-only change stays
archived and unchanged. Producer contract/schema/vectors/design and producer
delta stay frozen; this document makes the consumer seams concrete for review.

This is precode, not implemented or qualified consumer behavior. The existing
report1/2 route and numeric types remain unchanged. No provider, native, runtime,
cleanup, restore or media-content authority is added.

## Disjoint public request and result

Expose one new capability, `inspectOwnedV3(request)`, with exactly one argument:

```json
{"connection_id":"64 lowercase hex","boot_id":"canonical nonnil UUID"}
```

The public request is at most256 UTF8 bytes. Neither path, command, selector,
filter, actor, arbitrary UUID, version choice nor raw report is renderer input.
The same closed parser admits both the authenticated same-origin browser route
`POST /manager-owned-data-v3` and authorized main-frame Electron IPC
`manager:inspectOwnedV3`; preload rejects wrong arity. The existing
`/manager-host` inspect-owned action and zero-argument inspectOwned API remain
unchanged. Update the exact closed preload API assertion explicitly.

The result is exactly `{contract_version,status,observation,owned_data_v3}` using
the existing ObservationResult envelope. `owned_data_v3` is exactly
`{status,view}`, with status reported/unsupported/unavailable/busy. Reported requires
observed outer status and the original matching connection/boot identity, and a
validated nonnull view. Other statuses require null view, unconfigured outer
status and null observation, matching the existing bounded inventory pattern.
Host Busy and unsupported CLI capability remain distinct from a valid report3
whose producer status is busy/unsupported. No refusal becomes an empty success.

## Raw admission and private reduction

Proposed separate files are `owned-data-v3-private.mjs`,
`owned-data-v3-protocol.mjs`/`.d.mts`, `owned-data-v3.mjs` and the shared
`src/owned-data-v3.ts`. Do not add report3 to parseOwnedReport or widen its
report1/2 enum, number handling or legacy raw framing.

Before a view is admitted, validate exact raw length at most32768 bytes including
one terminal LF, fatal UTF8 with BOM rejection, exactly one JSON frame, duplicate
members and closed fields. Use maintained standard JSON parsing, not a new JSON
grammar: the installed Node24.21.0 and Electron44.4.5/Node24.21.0 both preserve the
original numeric token via JSON.parse's reviver context.source. Check every numeric
token's original spelling is a canonical unsigned integer before admission;
reject fractions, exponents, signs and missing source context. Reuse strictJson's
duplicate/depth check without changing released callers. Counts remain strings,
validated with whole-string matching and BigInt range checks through u64::MAX.
The lexical report version/format checks cannot rely on already-coerced Number
values. Python also rejects duplicate keys and noncanonical numeric tokens while
preserving the original raw output for independent Node admission.

Apply all frozen contract relations after structural validation: storage file
sum equals observed_files and is at most4096; known physical-byte sums, shared
subsets and overflow/null/issue consistency; notebook Source and Conversation
subsets; complete key coverage, identity/custody, known totals and zero missing/
uninspected/mismatched/omitted references; partial requires issues and no complete
total; legacy-only complete scans have known-zero notebook counts. Retained4 may
justify notebook observations while current is legacy. Never infer completeness
from successful JSON parsing, clamp overflow or add nonadditive reference totals.

Construct a new closed21-key public view. Replace raw report_version with literal
public schema_version1; preserve status, current_generation_format,
retained_generation_formats, observed_files, observed_apparent_bytes,
complete_apparent_bytes, storage, observed_domains, observed_notebook_records,
domain_accounting_complete, cache_inspected, shared_media_files,
shared_media_apparent_bytes, issues and the six false flags
reference_totals_additive/notebook_record_totals_additive/media_content_verified/
logical_liveness_evaluated/credentials_inspected/native_documents_inspected.
Discard owner_actor/current_generation UUIDs and private byte_basis/
lease_identity_check/excluded_scopes after validating their required raw values.
Their fixed meaning remains explained in the public guide. Revalidate the closed
public shape, exact counts and applicable relationships in both bridges and the
renderer. No raw stdout, diagnostic text, paths, payloads or private identity
fields leave the host.

## Transport and explicit size budgets

Add `owned_data_v3_transport.py` and an independent `owned-data-v3` observer action.
Its private input is exactly connection_id/boot_id/budget_ms, at most256 bytes;
budget_ms is an integer1..12000. The sole remote command is the existing fixed
environment/configuration/Reader prefix followed by `--inspect-owned-data-v3`.
Send no remote stdin and close its write side; no caller-controlled arguments or
fallback filesystem scraping. Reuse verified Linux/Windows SSH callbacks and
connection/boot checks before and after the command. Both host OSes invoke the
Linux tablet CLI; native Windows producer refusal is not consumer qualification.

Remote stdout is capped at32768 bytes; stderr at8192 bytes and discarded. Preserve
stdout privately as canonical base64, never parse and reserialize away lexical
evidence. Only one output attempt, no retry on partial/nonzero/late output. Exit
2/126/127 is unsupported capability; other nonzero output is unavailable.

The private child envelope is exactly
`{contract_version,status,observation,owned_data_v3_raw}`; its raw payload is exactly
`{status,stdout_base64}`. Cap the envelope at49152 bytes (48KiB), independently of
the smaller cache and Local-only actions. A full32768-byte raw frame uses43692
base64 bytes; the maximum existing observation is692 serialized bytes, giving a
44502-byte conservative envelope. Public serialized result cap is16384 bytes.
The closed schema's deliberately overgenerous structural values serialize to5797
raw bytes and6233 reduced-envelope bytes; this is size analysis, not a semantically
valid or reachable filesystem fixture. Do not confuse it with product evidence.

Use inherited remaining budgets: at most2s channel operations,8s collection,
12s Python/observer invocation,13s total host operation and14s browser/controller
wait including observation quiescence. Streaming reads enforce caps before whole
buffer decoding. Timeout/finally clears private buffers and releases only the
original invocation; an old timer must not cancel/release a newer owner.

## Shared ownership and UI lifetime

OwnedDataV3Host acquires the existing MaintenanceIO token before beforeIO or child
dispatch. Busy returns without invalidation, cancellation or I/O. Use a private
request epoch, issued-result witness and assertCurrent check before either bridge
sends a reported view. Invalidating an old read must not release another owner's
token. Reuse the established bounded read-coordinator pattern, not its cache wire.

Wire reciprocal hooks with the actual current forget, basic/product/model settings,
ordinary export, research/memory settings, credential reference/model credential,
source-cache inventory/cleanup, conversation inventory/management, ordinary restore,
selected archive, handwriting records and Local-only coordinators. Include external
observe/cancel, legacy inventory/runtime/saved inspections, connection/boot change
and same-ID refresh in the observer proxy/controller fences. Enumerate and test
actual current entry points; no guessed matrix size is an acceptance criterion.
In particular, the new read never discards or resolves Local-only unknown records.

The shared controller quiesces queued observations using pauseObservation before
dispatch, preserving existing global cancellation ownership. Its generation fence
rejects late results. Stop waiting, hidden/pagehide and disposal clear the view and
invalidate local delivery; a stopped read may still finish within the host budget.
They do not issue a delayed global cancel that could kill a newer unrelated action.
Explicit observation/disconnect cancellation revokes the host read through existing
ownership hooks. A new action encountering the still-owned read receives Busy.

## Product presentation and compatibility

Use a separate explicit inspection for stored data including notebooks. Keep the
existing older-Buddy inspection available manually; no automatic v3 fallback or
version threshold inferred from application tags. Show plain Complete, Some data
could not be checked, Busy, Unavailable and Unsupported wording; wire/report terms
stay in technical details/docs. Missing categories are Not checked, null byte
aggregates are Unknown, and explicit zero remains an observed zero. Refusal/partial
results never claim a healthy empty Store.

Keep exact decimal counts as primary text, using BigInt/string formatting only.
Notebook archive/plan/stage metadata is already included in Source/Conversation
and physical totals; label its breakdown Included above and never sum it again.
Reference subtotals are also nonadditive. Current/retained format observations do
not prove runtime, upgrade/downgrade or restore compatibility. Record counts are
not model requests, generated turns, visible notebooks or feature activation.
Metadata can contain protected inline text; do not advertise the producer as
text-free. No source/media/credential/native content is displayed or exported.

## Verification and coordinated completion

Reuse the43 accepted raw vectors with exact hashes and their synthetic/arithmetic
classification. Cover malformed UTF8/BOM/duplicates/numeric spellings/framing,
every semantic relation, exact32768-byte boundary and separately validated public
reduction. Add actual read/peer/Local-only unknown, Stop/quiescence/late-response/
same-ID/ownership controls and both real bridge guards, without mirroring code.
Qualify plain responsive browser/Electron UI and source/retained Linux+Windows
packages, keeping lower fixture transport distinct from actual tablet evidence.
Run unchanged report1/2 compatibility tests. No new build is needed for precode.

After consumer acceptance, finish remaining tasks and verification in this same
Docs125 change plus Manager consumer PR and frozen Buddy116. Reconcile exact heads
and dependencies, sync only both named capabilities, archive the completed change
once producer and both consumers qualify, and use coordinated guarded delivery.
Actual-main/release observation stays separate. No producer-only or planning-only
merge is requested.

## Implementation budget note

The explicit new raw/public validation and shared UI measured approximately632.5kB of initial production assets. Manager retains its400kB warning and raises only the initial hard ceiling from625kB to650kB for this feature. The threshold change is part of the reviewable Manager diff; it does not disable the build gate or imply a responsiveness result.
