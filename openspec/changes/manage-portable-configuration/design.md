# Minimal portable preference consumer

## Baselines and reuse
Manager baseline is 3f14a0d268ef0b6824756ff503f213d40b41f978; Docs baseline is
1b26d39cd72442c373ad68c112d167c88ed52870. Export uses the delivered
[V1 contract](../archive/2026-11-06-export-portable-configuration/contract.md).
Import consumes the exact reviewed [producer precode](https://github.com/s116821/ReMarkableBuddiesDocs/blob/69f90bb771b4366bec72cbb78f4517ef6de16911/openspec/changes/import-portable-configuration/contract.md).
The producer is being implemented separately; capability refusal remains valid
until its exact implemented protocol and attributed reports are available.

Reuse MaintenanceIO, observer identity/generation, before-I/O peer invalidation,
fixed Python callbacks, strict JSON helpers and sandboxed browser/Electron guards.
Add one operation-specific controller/private host/protocol/transport, following
current settings/archive patterns without refactoring unrelated lanes. Register
it in peer invalidation and dispose lifecycle; preserve all old pending originals,
including memory-forget, Stop and recovery contracts. No remote arbitrary path,
command, source module, local file path or service API is accepted from the UI.

## User workflow
The shared Preferences file section explains the supported Reader/Writer,
personalization and research declarations in ordinary language. Export explicitly
reads saved preferences and offers a file named
remarkable-buddies-preferences.json. A short notice says it may contain personal
text and the user chooses a private save location. Choose file accepts one bounded
file, reads bytes without putting decoded JSON/text into Angular state, immediately
clears the file input and requests Review import. Ignore filename, MIME and source
path as authority. Display only changed setting names and before/after declaration
presence; omitted declarations are kept and supported null is a saved declaration.
No raw JSON editor, value preview, default/reset switch or implicit Apply exists.

After an actual changed Prepare, show a separate Confirm import. No-change needs
no confirmation or Store. A verified result says saved file verified; running
settings remain unverified. Check original desired file is an explicit read-only
reconciliation of an uncertain import, never Retry. Explain unavailable/unsupported
saved-state prerequisites without exposing parser text, commands or schema jargon.
Pause ordinary polling before remote work; same-ID refresh, navigation, another
maintenance action or identity change invalidates ready authority and late UI
responses. Local retained diagnostics are available without touching the tablet.

## File privacy and custody
The only raw outbound content permitted to the renderer is an explicitly requested
export file payload. A narrow download path consumes it immediately as a Blob,
uses a fixed filename, revokes its object URL after handoff and never puts it in
ordinary application state, HTML, logs, URLs, localStorage or diagnostics. The same
shared file flow is exercised in browser and sandboxed Electron; no general file
or download IPC is exposed. Only export may return this payload. Import file bytes
are private input and are never echoed into preview/status/results.

No artifact is staged on the tablet or in a host filesystem spool. The browser/OS
owns the chosen download destination and its permissions. Download handoff is not
proof of durable save, private ACLs, overwrite policy or future restoration. The UI
must not say file saved/backup verified based on a click or Blob creation. Manager
holds no file handle that could justify such a claim. A failed local download can
be deliberately exported again because export is read-only; this never retries an
import. Do not claim immutable JavaScript strings have been securely erased;
release references promptly and zero owned mutable buffers where practical.

Keep at most one ready private import packet for 120 seconds, bounded by one raw
128 KiB file. It retains the exact selected bytes, validated artifact and original
Inspect/Prepare responses plus original intent until Confirm dispatch. Once Apply
may have run, discard artifact/text after the request lifetime and retain only
original digest/intent and bounded metadata for Status, which needs no artifact.
No persisted recovery journal is added. Up to eight unknown originals are kept
without eviction; a new changed import refuses at capacity. Host exit loses those
private references and must not imply settlement.

## Original operation ownership
Review import uses Inspect then Prepare under one 13 second host budget; each
private phase receives only its remainder, at most 12 seconds. Confirm has one
13 second budget and must recheck the original ready deadline before dispatch.
The outer guarded client deadline remains 14 seconds. One shared active slot
serializes every phase. Claim an immutable owner token; stale cancel/status and
finally paths cannot cancel/release another lane or a newer reference. An old
Status refuses busy during active work; when it obtains the slot it invalidates
merely ready peers before remote I/O. Read-only local retained does neither.

Retain the exact original private Apply packet before its one possible dispatch.
Record unknown before launching Apply. Output loss, timeout, partial frame,
invalidation or cancellation after possible dispatch retain that original unknown
without replay, new base, rollback or a second report. Only a complete valid,
original-corresponding producer report can yield verified/not-dispatched. Later
Status uses only the original intent and same current wired identity. Desired
bytes currently observed do not identify the publisher or prove runtime adoption;
refusal or different bytes cannot prove historical rollback. A new deliberate
review does not settle older diagnostics.

## Qualification and delivery
Use small attributed actual producer stdout/stdin captures with exact source/head
and byte hashes for export and import phases. Keep these distinct from synthetic
faults. Cover original closed reports, Unicode/CRLF/control text, sparse/empty/null
and no-change, excluded secrets/paths and exact digest correspondence. Validate
original file bytes before any parse/reserialization can normalize malformed
numeric versions or repeated fields. Synthetic cases must cover all boundaries,
phase/intent mismatches, late identity/generation, expiry, capacity, token ownership,
unknown retention and no-replay.

Exercise real loopback browser guards and actual sandboxed Electron IPC, their
shared rendered file selection/download, navigation/cancel races and private
state. Cross-lane tests use a retained older unknown plus a newer import/other
operation; prove one owner and original evidence preservation through actual
hosts. Test partial/oversized/invalid UTF8 output and child EOF/deadline handling
without a tablet/provider. Responsive UI checks and both OS package jobs remain
required. Exact producer compatibility is a delivery dependency, not inferred
from fixtures or equal release numbers.

No heavy build is needed for precode. Before implementation builds, check current
free space and select a task-owned dependency/output directory; do not mutate
another active checkout/cache. Retain useful failures and source/corpus hashes.
Independent precode review precedes source edits. Implementation review, current
CI and coordinated Manager/Docs merge/release follow full same-pair sync/archive.
