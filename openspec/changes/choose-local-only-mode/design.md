## Context

The producer accepts a strict original `{operation,expected:{actor,sha256},choice:{kind:"local-only"}}` over fixed `choose --sync-mode-input -`. Inspect/choose require an existing valid owned Store. The response is report-v1, one UTF8 JSON line of at most16384 bytes including newline, with `activation_performed:false`. Initialize remains a separate administrative capability.

Current producer source and tests define exact retry, current versus historical receipts and post-commit failure. Sanitized consumer fixtures are derived synthetic data from separately reviewed Windows CLI output; they are not original bytes or integrity authority. No Linux/device/provider result follows from them. Source tests establish selected-history preservation and output/lease uncertainty; they are not new execution evidence.

## Goals / Non-Goals

Goals: deliberate Local-only choice in both companions, original host-private authority, one dispatch, retained uncertainty and separately labeled current metadata. Preserve the shipped read-only inspection API.

Non-goals: initialize/repair, isolated/shared selection, binding edits, configuration editing, token rebase, mutation replay, cloud/provider work, service control, data conversion, activation or process-restart recovery of in-memory host records.

## Decisions

### Separate capability and original private packet

Add `local-mode-choice` maintenance handling rather than widening `inspectSavedMode`. Public actions are begin with current connection/boot IDs, choose/cancel/refresh with an opaque reference, and local retained-history enumeration. The host obtains fresh inspect data, validates all mode/token shapes, creates a nonnil operation UUID and retains exact original request bytes plus hashes. The only choice is `{kind:"local-only"}`. Public requests cannot supply an operation, token, path, command, arbitrary choice or raw report.

Ready previews expire after120000ms. A host retains at most8 possible-dispatch operation records without silently evicting unresolved entries. Private records belong to this host-process lifetime; browser reload/session invalidation does not remove them. Process restart is not original-operation reconciliation. Raw report/request buffers are bounded and cleared after use; retained original authority stays private until coordinator disposal.

### One dispatch and truthful uncertainty

Confirmation consumes one ready reference. Acquire the shared MaintenanceIO owner and check generation, identity, deadline and original packet hashes before setting possible-dispatch and invoking the fixed writer. Repeated/queued confirmation never dispatches again. Busy cannot release another lane's invocation. Cancellation before this boundary invalidates the preview; after it, cancellation/timeouts/disconnects/late responses preserve unknown original outcome.

A valid complete successful receipt must match original operation, expected digest, request fingerprint and Local-only choice. Receipt current/historical classification requires epoch AND mode agreement with the actual snapshot. A later Local-only epoch is historical even when the kind is unchanged. New deliberate same-valued choice is a real new epoch, not no-change.

Malformed/lost/partial output, failed, unavailable or incomplete results after possible dispatch remain unknown. Unsupported is not universally pre-mutation: producer finish can return incomplete unsupported after commit. Only strict complete producer refusals proven before mutation may become refused; no status substring guesses or interpretation of current Local-only as proof of original success.

### Current observation is separate

Refresh executes only fixed inspect using retained target identity. It may attach a current reduced saved snapshot to an unknown record but never changes that record's original outcome or obtains a receipt. There is no original retry/receipt-check action: `choose` can mutate if the first call never arrived. An unknown original prevents another choice for that target within this host lifetime; inspecting it stays available. No automatic rebase, clear-uncertainty control or silent new operation replaces it.

### Bounds, identity and lifecycle

Reuse strict duplicate-key UTF8 parsing,16KiB remote input/output, bounded private base64 envelopes, fixed environment/Reader/configuration paths, Linux/Windows verified SSH callbacks and at most13s host/14s browser operation budgets. No renderer values enter a shell command. Hold Store/mode effects to producer semantics; transport EOF/cancellation never triggers a second write.

Both bridges share a single coordinator and MaintenanceIO with existing lanes. External observation/cancel, all competing maintenance operations, same-ID refresh, connection/boot changes, pagehide/hidden and disposal invalidate ready or in-flight authority. Host-issued response epochs and renderer generations reject stale results. Local retained-history views do not invalidate unrelated work or contact a device. Public state exposes only opaque references, target identity, reduced saved snapshot and sanitized original outcome/receipt metadata; no actor, token, operation UUID, expected/fingerprint digest, binding/root or raw receipt.

## Risks / Trade-offs

- Unknown records can intentionally block another choice. Recovery through explicit original mutation replay or durable host restart records is deferred; current inspection remains separate and cannot claim reconciliation.
- Local-only metadata does not make selected-format records readable by ordinary Reader, stop a worker, delete remote backups or establish service/provider readiness.
- A successful report is a saved historical receipt and a snapshot at observation time, not ongoing runtime truth.

## Verification and Delivery

Cover exact protocol/receipt relationships, all sanitized fixtures and synthetic malformed/uncertain controls; transport command/EOF/bounds/identity; shared ownership, cancellation/late delivery/expiry/capacity; original unknown with later current observation; all public-field reductions; both real companion UIs and retained packages. Preserve original inspect tests. Run appropriate production build/type/lint and full required CI. Publish coordinated Docs+Manager implementation PRs; sync only this completed capability and archive this change after qualification. No planning-only merge or device/provider qualification is implied.
