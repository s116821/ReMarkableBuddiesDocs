# Deliver offline host memory

## Why
Delivered main lacks the memory backend required by the prepared Manager search consumer. Pending Reader memory contains a reusable offline core, but its live-model gate must remain separate.

## What changes
- Deliver inspect/query/put/forget and explicit selected aggregate/catalog setup as a one-shot host CLI using existing Store records and CAS.
- Support bounded query-only stdin and existing absolute-file inputs with report-v1 output.
- Hold the correct storage mode and selected currentness guards through actual report output.

## Scope
Reuse frozen d9aa2f3 memory core and its generic ordered admission helper; adapt accepted feeaf475 stdin seam. Exclude model context, Reader orchestration/publication, SDK changes, device contact, sync workers, account operations and later memory drafts. Related code and this Docs change form one delivery. Existing live-model/native gates remain open.
