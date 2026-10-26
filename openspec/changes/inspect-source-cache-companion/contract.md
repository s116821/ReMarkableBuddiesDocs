# Source-cache inventory companion contract (unimplemented precode)

## Authority and exclusions
Unchanged [canonical producer](../../specs/source-cache-inventory/spec.md) and [exact producer contract](../archive/2026-10-23-inspect-source-cache-metadata/contract.md) own the Linux observer, limits and existing-only custody. Existing aggregate accounting and selected cleanup contracts stay closed. This is a new consumer design, not source/API implementation or independent acceptance. No cleanup/prepare/apply/status-for-write, selected UUID, discovery beyond this namespace, payload/title/text/hash access, original-document lookup, Store recovery/creation, permission/root repair, config/reference mutation, provider/runtime/service action, SDK/RE or tablet operation is authorized.

## Exact interfaces
Optional public method `inspectSourceCache(request)`; HTTP POST `/manager-source-cache-inventory`; IPC `manager:inspectSourceCache`; host coordinator SourceCacheInventoryHost; helper `source_cache_inventory_transport.py`; raw internal action/lane `source-cache-inventory`; private raw key `source_cache_inventory_raw`. General `/manager-host`/observer raw APIs remain unchanged and unexposed.

One exact public request `{connection_id:DIGEST,boot_id:UUID}` required. DIGEST is64 lowercase hex; UUID is canonical lowercase hyphenated36-character nonnil UUID. Bound canonical public UTF8 JSON to256 bytes. No action/selector/UUID-of-slot/path/Config/command/query/filter/paging/budget/cancel/reference is caller-admitted. Wrong arity/unknown/duplicate/type/array/coercion/cyclic/BigInt/malformed UTF8/oversize input refuses through fixed errors with no value echo.

Host-only helper request is exactly `{connection_id:DIGEST,boot_id:UUID,budget_ms:INTEGER}`, cap256 encoded bytes; budget_ms is1..12000, not bool. It inherits the remaining original host deadline. No selector or stdin_base64 field exists because this is one fixed no-input command.

Fixed target command:
`/usr/bin/env -i HOME=/home/root PATH=/opt/bin:/usr/bin:/bin REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json /opt/bin/reader-buddy --inspect-source-cache`
Only this literal command; no arguments/environment interpolation from caller or installed-version fallback. Send no stdin bytes and close write side. Bound/discard stderr; never display it, .message/.cause, traceback or command diagnostics. Nonzero/old/missing capability refuses without any alternate CLI/filesystem/Buddy API. Ordinary producer parser errors are not globally sanitized; the fixed consumer supplies no private argv and does not widen that guarantee.

## Raw report: strict host-only validation
Require one complete strict UTF8 JSON object with exactly one final LF/no other literal LF, recursively no duplicate object members, max8192 original bytes including framing. JSON whitespace still counts toward the cap. Decode with fatal UTF8 and preserve/reject a BOM rather than silently stripping it. Decode/reject before reducing; escaped equivalent JSON spelling does not change semantic validation. No truncation, clipping, integer coercion/rounding, sorting or deduplication repair.

Exactly13 fields:
- report_version:1;
- operation:"inspect-source-cache";
- status:"ok"|"unavailable"|"unsupported"|"busy"|"conflict";
- runtime_unverified:true;
- cleanup_authority:false;
- entry_payloads_read:false;
- entry_payloads_validated:false;
- source_freshness_verified:false;
- byte_basis:"apparent-file-length-per-owned-slot; no-allocated-or-reclaimable-claim";
- actor:UUID on ok, null otherwise;
- generation:UUID on ok, null otherwise;
- entries:ARRAY on ok, null otherwise;
- total_apparent_bytes:INTEGER on ok, null otherwise.

Each entry exactly `{document:UUID,apparent_bytes:INTEGER}`. ARRAY has0..16 entries, strictly increasing canonical document ASCII string order, no duplicates/nil/uppercase/noncanonical spellings. Each length is a nonnegative safe integer<=33554432, total is exact checked sum<=536870912; reject bool/nonfinite/fractional/unsafe/negative/out-of-bound/mismatching values. Empty ok[]/0 remains distinct from every refusal's nulls. Every fixed boolean/literal must match, even for refusals; do not downgrade a true authority/read/freshness claim to false and display it. Future version is unsupported without admitting its data; malformed current report is unavailable. No partial candidate list or old good snapshot is a fallback.

Private helper response exactly `{contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,source_cache_inventory_raw:{status:"reported"|"unsupported"|"unavailable",stdout_base64:STRING_OR_NULL}}`, max16384 encoded bytes, existing strict observation shape/identity. Reported requires observed matching requested connection/boot and canonical base64 of original strict8192-byte report; other statuses require null stdout. Validate recursive duplicates/UTF8/envelope/framing/base64 shape and identity before any safe view. A Linux producer's valid unsupported report is a reported refusal, different from transport missing/old capability; neither grants inventory or mutation authority. Non-Linux target early unsupported never implies local Windows Manager unsupported.

## Safe public result
Exactly `{contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,source_cache_inventory:{status:"reported"|"unsupported"|"unavailable"|"busy",view:VIEW_OR_NULL}}`, cap8192 UTF8 JSON bytes. Reported requires observed same requested identity and validated VIEW; all other wrapper statuses have null view, unconfigured top status and null observation. Wrapper busy means shared host owner refused before I/O, not a fabricated producer report. Existing observation validator is reused and every result is rechecked against request/token/generation before release.

VIEW exactly nine fields: `{status,entries,total_apparent_bytes,runtime_unverified,cleanup_authority,entry_payloads_read,entry_payloads_validated,source_freshness_verified,byte_basis}`, all copied only from the completely validated report. Same status/bounds/null/flags/literal rules apply. Omit actor/generation and every raw wrapper/report, path, header/metadata/digest/intent/binding/error/diagnostic field. No extra arbitrary text. Public candidates are IDs/apparent lengths only. No code can receive private parser objects through renderer imports/preload/general actions/debug hooks. Library exceptions are caught/replaced with static safe labels before public/log/error/telemetry output.

## HTTP, IPC and physical identity
Reuse strict loopback Host/exact same-origin/session cookie/content-type/POST/no-query guards, bounded body/stream reads and mutable chunk wiping on success AND oversize/refusal. Request JSON is canonical; malformed/duplicate fields reject before admission. No response caching. Browser safe-result stream capped8192, incomplete streams cancelled and reader released.

IPC requires exactly one arg, the authorized webContents/main frame and exact loaded fixed UI URL, context isolation/sandbox and narrow optional preload capability. Keep the exact exposed-capability allowlist current by adding only inspectSourceCache and test its arity/path/selector denial. No renderer Node/raw transport exposure.

Both Manager host OSes retain existing hard-wired route/cable/host-key and before/after boot identity checks. Raw result identity, request identity and current observation must agree; late previous boot/session/refused/cancelled generation yields no current view. No native USB/provider/installed compatibility inference follows from a fixture or a successful report on a source snapshot.

## Nine real owners and lifetime
The real shared MaintenanceIO covers model/basic/forget/ordinary-export/research-settings/memory-settings/credential-reference/model-credential/source-cache-inventory in both actual factories and combined fixtures. Acquire the read token before beforeIO hooks, observer cancel/helper launch or remote I/O. Host Busy returns wrapper busy/null and changes no epoch, grant, original, timer, hook or current owner. Do not route an admitted read through the externally cancelling observer proxy that revokes its own token. Use the captured raw observer through the dedicated coordinator as existing writers do.

Admission starts one monotonic13000ms host deadline before hooks; child budget min12000ms/remaining deadline, one attempt, no renewal. Host timer/late return/final generation check invalidates only the captured operation, releases only its exact token, and may cancel its owned child only while that token and generation still belong to it. No old timer/finally can cancel or release a newer owner. Use bounded promise/child supervision even if a fake/IPC/observer never resolves. No raw buffers/references persist past bounded operation cleanup; mutable buffers are cleared on completion/refusal/cancellation, immutable JS/Python/IPC/SSH/OS copies have no physical erasure guarantee.

Reciprocal beforeIO hooks invalidate idle grants/views across all nine owners; never resolve/evict/rebase a peer unknown/unresolved original or renew its private expiry. Preserve the original56-case submatrix and qualify all72 directed owner pairs. For a successful read, release custody only after complete validated output has been consumed/finally guarded. A list is not an idle write grant; reciprocal starts clear its snapshot.

Renderer known peer Busy checks run before private draft/actual-input clearing. On an admitted local action, synchronously clear all eight idle editor grants/private actual DOM/raw before the first pause/transport await, preserving unrelated query/Reader/Writer drafts and every original uncertainty. If a racing external request makes host Busy after local erasure, do not restore erased text; this does not change host Busy's no-side-effect guarantee. Both the private-file/reference/model/memory editor clears and inventory-view invalidation must be explicit; ConnectionController.pause alone emits no UI update.

## Read-only UI and local Stop
Section “Source-cache slot inventory”; explicit “Inspect source-cache slots” and “Stop waiting for cache inventory”. Initial not-inspected, waiting, wait-stopped, invalidated and unavailable/unsupported/busy/conflict are fixed local labels, not producer reports. Show a report only on matching admitted response; ok-empty gets its own inspected-empty message, refused/null is never zero. Show sorted IDs/apparent lengths/total with unread/unvalidated/freshness/runtime/no-cleanup limitations. Do not add this namespace's total to aggregate category totals or label it allocated/reclaimable. No row cleanup/prepare/select-to-write action, title/payload view, automatic polling/retry, browser persistence, version-threshold capability claim or inspection on connect/reload.

One renderer request wait is bounded14000ms from invocation. Stop waiting synchronously advances request generation and clears current view/wait controls; it sends no capability/global cancel request, releases no host token and performs no follow-up inspection. It is local detachment from a bounded read, not remote cancellation. Original host may still finish within its existing deadline, so a new peer/request may receive Busy until then. Late old result/timeout must never refill a stopped/newer snapshot or clear another editor. Disconnect, explicit global observation, pagehide/hiding, peer starts and destruction clear the view through existing external generation/cancellation semantics; no automatic re-observation. A completed list is labelled an explicit snapshot, not continuing source freshness.

## Planned qualification and delivery
See acceptance.md and explicitly synthetic vectors.json. These are not executed Manager qualification. Original12 Linux/7 current Windows records and older corpora keep source/executable/failure attribution and may be read statically only; no source cache/cleanup producer replay. Current both-host guarded source/development/retained/packaged qualification plus independent precode/implementation/final current-main and artifact-byte reviews precede own canonical/manual sync/archive and normal paired delivery. Root owns publication/current-main composition. The prior protected-file release is closed independently and is not a dependency. No new resources/settings/auth retry or tablet/provider/SDK/RE action follows from this proposal.
