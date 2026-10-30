# Shared public product-settings projection — review candidate

Reuse the delivered BasicSettingsHost/controller transaction envelope and common
MaintenanceIO queue, with component `product_settings` and the new three-field
current/dirty maps. Do not expose or reconstruct a parallel CAS engine in the UI.
Both browser helper and Electron expose one typed productSettings capability.

## Requests

Closed request shapes (maximum1024serialized UTF8bytes):

- `{action:"retained"}` reads safe host memory only.
- `{action:"cancel",reference}` targets only that opaque original/editor.
- `{action:"begin",connection_id,boot_id}` pauses observations before fresh inspect.
- `{action:"save",connection_id,boot_id,reference,changes}` submits original dirty choices once.
- `{action:"status",connection_id,boot_id,reference}` explicitly checks the original saved target.

Connection ID/reference are lowercase64hex; boot ID is canonical nonnil UUID.
Changes/current use contract.md; no raw path, hash, operation or intent is accepted.

## Results

Exactly `{contract_version:1,status,observation,product_settings}` using the existing
observation envelope. Maximum8192serialized UTF8bytes. Product view is exactly
`{state,reference,current,report,retained}`. States are none/ready/invalidated/
unsupported/unavailable/busy/capacity/not-dispatched/no-change/verified/unknown/
unresolved/desired-file-observed. Reference is null or opaque64hex; current is
null or the exact safe three-field declaration projection. Report is null or
only operation,status,outcome,disk_readback_verified,runtime_activation, validated
against the complete producer matrix. No producer data object crosses this boundary.

Ready pairs observed current with successful inspect/read-only; no-change pairs
successful prepare/no-change; verified pairs apply/verified; desired-file-observed
pairs status/desired-file-observed. Unresolved current, if present, requires its
successful status/unresolved report. Unknown has no current. None/invalidated/
unsupported/unavailable/busy/capacity/not-dispatched have no current. Positive
current is observation/identity-bound. Non-null references must match the captured
request. Retained is at most8 unique rows, each exactly reference/connection_id/
boot_id/state where state is unknown or unresolved; uncertain active rows must be
present. Retained read is none/unconfigured with null observation/reference/current/
report and performs no remote work. No private digest or raw report is copied.

Begin returns only ready/invalidated/unsupported/unavailable/busy. Save may return
verified/no-change/not-dispatched/unknown/capacity/unavailable/busy. Status may
return desired-file-observed/unresolved/unknown/unavailable/busy. Cancel returns
not-dispatched/unknown/unresolved/invalidated/unavailable; retained returns none.
The result remains bound to immutable captured action/identity/reference even
if another invocation or newer connection completes meanwhile.

## Fixed private transport and finite custody

Fixed existing clean environment/config path with only the dedicated selector;
non-inspect phases send bounded private JSON stdin and EOF, never shell arguments.
Transport envelope is at most24576bytes with selector/input_base64/budget_ms/
connection_id/boot_id. Report raw bytes at most16384; private response24576; stderr8192.
Canonical Base64, fatal UTF8, no BOM/extra JSON/duplicate members and exact phase/
identity/output validation apply. Budget is at most12000ms transport within one
13000ms host and14000ms UI wait; each lower phase gets only remaining time.
A ready editor is120000ms nonrenewing and is checked again before apply. At most8
uncertain original saves retain private intent for1800000ms from possible apply,
nonrenewing, with at most32executing original status calls. Expiry/capacity never
silently evicts safe rows or grants retry; expired originals erase private packets
and return unavailable to later status. These bounds supplement the reused public
envelope without changing any delivered editor.

One Save prepares privately then claims apply once; UI draft/signals/DOM clear
before waiting. Other maintenance and observation/identity/page lifetime clear
ready state. Stop permanently revokes an unconsumed ready reference, so a late Save
cannot dispatch after an arrival fence. Busy happens before peer hooks/I/O. Old
cancel cannot release a successor owner. After possible apply, cancellation/timeout
keeps unknown original history; status can cancel only its exact wait without
rewriting earlier disposition. No new save/status is reconstructed after host loss.

UI uses Reader enabled, Writer enabled and Export backend (Mem / Disabled), with
truthful declaration/default labels and deliberate changes. It states saved-file
verification separately from runtime activation and leaves account/workspace/
collection/credential setup and automatic Reader-to-Writer integration open.
