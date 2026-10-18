# Prepared note export: Mem API and reuse boundaries

October 17, 2026. This is source research for the
[prepared export change](../../openspec/changes/archive/2026-10-18-export-prepared-notes/proposal.md),
not live destination qualification.

Mem's current [create endpoint](https://docs.mem.ai/api-reference/notes/create-note)
accepts a complete Markdown body and optional caller UUID. The first line becomes
the title; content is limited to 200,000 characters and UTF-8 bytes on create.
Do not infer an undocumented duplicate-POST/idempotency guarantee from that UUID.
The [read endpoint](https://docs.mem.ai/api-reference/notes/read-note) supplies
current content/version and trash state. The
[update endpoint](https://docs.mem.ai/api-reference/notes/update-note) requires
the exact version being updated and a complete desired body, not a partial patch.
These declared fields do not offer arbitrary custom correlation metadata, so the
existing `[RMB:<UUID>]` title token is the Mem adapter's portable path.

[Search](https://docs.mem.ai/api-reference/notes/search-notes) returns a bounded,
relevance-ranked window capped at 100 results. A search miss is not exhaustive
absence. [Listing](https://docs.mem.ai/api-reference/notes/list-notes) offers
chronological cursor pagination with at most 100 notes per page and requires
consistent filters/order across cursors. Bound local discovery and explicitly
report incomplete results; do not turn a cap into a missing-note claim.
[Error handling](https://docs.mem.ai/api-reference/overview/error-handling)
distinguishes authentication, invalid request, absence, quota and server failures.
A transport failure after dispatch remains an uncertain effect, not permission
to repeat it. Preserve useful prior-body/version facts to detect remote edits
before replacement instead of introducing a synchronization/conflict engine.

Narrow prior art: rMirror Cloud at
[`a1120fc85b774947ed0bcd5337803b55ca4db589`](https://github.com/gottino/rmirror-cloud/blob/a1120fc85b774947ed0bcd5337803b55ca4db589/backend/app/integrations/notion_sync.py)
separates backend sync operations and looks up an existing notebook UUID before
create/update. Its Notion-specific lookup also takes the first result and falls
back to a UUID prefix in a title. Those fallback semantics do not meet this
product's exact full-token/duplicate refusal contract and are not reused. No
source was copied; no OCR, ingestion or application architecture is inherited.

Source basis: current official Mem documentation and the pinned public reference
source above, inspected directly; current delivered Ledger implementation and
portable Writer requirements. Limits and reconciliation choices are engineering
inferences from those interfaces. No account credentials or live writes were used.
