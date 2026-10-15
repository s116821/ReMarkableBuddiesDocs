# Proposed subject-memory query integration seam

## Current source and prerequisite

Read-only source basis: Main PR49 `be95c29b0ab57806716a327d050adb92c921cd39`, memory/mod.rs Query190–230 and report/context types; maintenance.rs Report/write_to16–113, Input124–176 and query353–358; storage/files.rs240–280. Current code takes regular-file JSON only. Main owns its default-log privacy fix and subsequent minimal stdin successor. The proposed `reader-buddy --memory-operation query --memory-input -` is not supported until Main publishes qualified source and its central backend contract. Neither /dev/stdin nor a remote request-file writer substitutes for it.

## Request ownership

Manager's narrow renderer request carries validated current connection_id, boot_id and text only. These connection pins are host admission fields, not extra backend Query fields. Existing host-owned executable/config/environment and USB route/key/device checks remain fixed. The host constructs the exact existing Query:

```json
{"document":null,"text":"explicit user query","now_ms":0,"current_claims":[],"max_matches":8,"max_context_bytes":8192}
```

The example's zero timestamp is a schema illustration, not a production expiry value: the trusted host supplies current integer milliseconds for existing expiry semantics only. Text is nonblank, no NUL, <=2048 UTF-8 bytes. No profile field is added; Main chooses the configured memory profile. No arbitrary executable, path, shell, endpoint or command comes from the renderer. Encode one bounded JSON document to stdin and close write. Main's proposed overall input cap is existing MAX_RECORD1MiB; the Manager query is much smaller. Final byte/EOF/error behavior follows Main's published contract before code.

## Existing report preservation

Consume a bounded UTF-8 newline-terminated JSON Report with existing fields report_version, operation, status, incomplete and data. Version1/query are the currently published schema, not new version sources. For query data, preserve query_status, diagnostics and context; context retains kind, provenance_authority and original facts containing record, revision and fact. Fact keys/profile/scope, claim/value/subject, tags, asserted provenance, confidence and expiry remain backend data. Do not remint identities, infer current-document truth or treat the result as exhaustive inventory.

Query-status disabled, complete-empty, complete, partial and unavailable stay distinct. Outer report busy, unavailable, unsupported, conflict, invalid-input and failed remain meaningful; no service stop or automatic mutation retry follows busy. Main must publish actual CLI exit semantics so older flag support, nonzero failure and valid semantic reports are mapped from evidence. A missing/older Manager helper is unavailable; a proven older installed CLI is unsupported; unknown future report versions are unsupported; malformed/truncated/oversized/invalid UTF-8 is refused without empty success. No guessed minimum application version or fixed app version is stored in source.

Proposed backend-response cap is128KiB; trusted outer observation/envelope overhead needs its own explicit bounded allowance, as existing personalization transport does. Browser streaming, Python SSH stdout/stderr drain and Node child output each enforce their declared caps without retaining or displaying raw diagnostics. Final caps are aligned with the actual report and normal escaping before code. Existing backend Report.write_to currentness custody and no-second-report-after-prefix behavior must remain intact. This is a query-only domain action; normal documented Store admission/recovery writes are not falsely described as filesystem immutability. Invalid input must refuse before Store effects.

## Consumer cancellation and compatibility

Use existing observer generation/cancel and platform callback admission. Check requested connection/boot against current observation before dispatch and repeat observation after collection. Clear prior facts on new query, explicit cancel/disconnect, query replacement or tablet/boot/session change; late results cannot repopulate the current view. The host owns a deadline and closes the owned channel/process on cancellation; no assumption of remote rollback is made. Never persist the query/results as host settings, forward provider credentials or print private input/report diagnostics.

The centralized device profile permits a wired probe only; successful model/firmware observation does not assert that the installed CLI supports memory query or that physical/native behavior is qualified. Both shared Angular distributions expose the same search/status/provenance behavior. Standalone browser without its configured helper remains honestly unavailable; no separate Buddy API is introduced.

## Exact completion handoff

Main supplies central backend precode and immutable source for supported stdin, documented request/output limits and exit semantics, actual CLI positive/disabled/empty/busy or refused outcomes as applicable, and malformed/oversize pre-Store refusal evidence. No new profile-discovery, domain schema, Store, router or provider API is requested. Manager then records exact backend/Docs revisions, updates this plan to the supported contract and implements only its owned files.

Verify actual unchanged Main CLI output through the new stdin path against the strict parser, plus the actual fixed-command SSH peer with synthetic route/key/notice admission. Meaningful controls cover UTF-8/blank/NUL/oversize, unknown/duplicate fields, identity mismatch, output bounds/deadline, older CLI and unknown report, privacy, busy/disabled/empty/partial semantics, generation/cancel/disconnect and stale completion. Shared browser/helper and Electron authorized-call and packaged UI checks use explicitly synthetic semantic reports; actual parser/CLI/process checks remain separate. Use existing Linux/Windows jobs and package lifecycle, no duplicate backend/native/provider/compiler matrix or physical proof. Sync/archive this consumer only after implementation, supported checks and independent paired review.
