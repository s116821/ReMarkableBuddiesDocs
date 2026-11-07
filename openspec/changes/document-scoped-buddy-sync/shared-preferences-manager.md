# Manager shared preferences

This is the Manager consumer for the existing format5 SharedGroup preference record. Saved-file editors and the portable file import/export selectors remain the local file path. The saved-mode view is a navigation hint. Shared Inspect is the authority for this editor and describes an inspection snapshot of the overlay available to the next admitted request. Running activation is unverified.

## Browser and Electron call

The loopback helper exposes POST /manager-shared-preferences. The Electron preload exposes one argument through manager:sharedPreferences. Both validate the same closed request and response using the existing host observation and MaintenanceIO owner. Same-origin, session-cookie, top-frame, connection, boot, deadline, navigation and cancellation checks follow the delivered private preference host.

| Action | Request fields beyond action |
| --- | --- |
| inspect | connection_id, boot_id, reveal_text (boolean) |
| edit | connection_id, boot_id, reference, patch (strict portable V1 artifact) |
| status | connection_id, boot_id, reference |
| retained | none |
| cancel | reference |

Inspect returns a host reference for a successful admitted view. Edit consumes it once after explicit confirmation. The editor submits only deliberate declarations, with omission, sparse objects and supported null preserved. It never round-trips effective defaults as declarations. Effective booleans, export and research enums, personalization presence and per-field origins can be displayed. Effective text is returned only for the explicitly requested private view and cleared with that view. Local file status remains separate.

The host privately retains the original Edit status query before possible dispatch, up to eight references. No patch/text is retained after dispatch lifetime. Status resolves the original operation. Refused/expired references do not allow another Edit. Cancellation, malformed output, timeout or identity change after possible dispatch retains unknown. A validated terminal disposition or known pre-dispatch refusal releases the original. Retention is process-local and same-observation-bound, with no automatic replay, persistent journal, text logs, service action or provider path.

## Buddy one-shot seam for joint verification

Proposed fixed selector is reader-buddy --shared-preferences-operation inspect|edit|status --shared-preferences-input - with the trusted installed Config path. Each input has shared_preferences_version 1. Inspect also has reveal_text. Edit has original operation UUID, the exact Inspect guard and the strict V1 patch. Status has only the original operation, guard and compact patch_sha256.

The private guard carries group, mode_epoch, binding_sha256, store_generation, local_config_sha256 and selection. Selection is either {kind: absent}, when absence is established, or {kind: selected, aggregate_generation, accepted_base_sha256, selection_sha256, revision}. The host treats the guard as opaque authority from Buddy and never returns it to the renderer. The accepted Worker owns actual admission and the Store CAS. Existing-only Store ownership can return busy. A missing command is unsupported, including older Buddy builds.

Inspect returns the authoritative shared disposition, private guard if editable, and the effective allowlisted view. Field names are reader_enabled, writer_enabled, export_destination, personalization_enabled, personalization_text_present and research_policy. Include personalization_text only as an exact disclosed string or null. The origins map has reader_enabled, writer_enabled, export_destination, personalization_enabled, personalization_text and research_policy, each shared, local or default. Joining/unresolved cannot mint an edit guard. Edit or Status returns the exact original operation, guard and compact patch digest for host correspondence. Status verifies the exact local original receipt without prompt text. An absent or unprovable receipt remains unknown. Remote applied or superseded is a separate verified disposition and local selected means pending upstream. Never infer success from matching effective values alone. An equal raw Edit can report no-change without a receipt.

Reuse 196608-byte renderer/host frame, 262144-byte decoded private request and 131072-byte one-shot report ceilings, strict duplicate-free JSON, bounded UTF-8, original remaining deadline and fixed stdin dispatch. The private transport uses the existing before/after observation and capability gates. No service API, auto-stop, Config rewrite, direct credential operation or second sync engine.

## Acceptance and ownership

Manager owns the shared Angular controller/panel and common private host, including browser/Electron guarded routing, sparse patch construction, unknown/recovery and privacy tests. Buddy owns mode, selection, atomic original receipts, truthful Worker status and the supported executable fixture. Test both hosts with the same request and bounds, including older unsupported Buddy, active Store busy, stale pins, lost output and original-only status. Source-level contract and guarded-path fixtures are provisional until real Buddy reports prove the same integration. Keep the Manager PR coordinated with Buddy139 and the active Docs change.
