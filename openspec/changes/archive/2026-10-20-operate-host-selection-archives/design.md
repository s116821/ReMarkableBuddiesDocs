# Host selected archive maintenance

## Current source and ownership
Current REM52 description and full chronology were read for the preceding mode
delivery; subsequent review/consumer/merge comments were reconciled. Active nine
end-to-end requirements remain open. Current canonical selected archive custody,
shared-storage export and existing-maintenance contracts apply. Root confirmed
this preparation is independent of retained Reader ordinary-lifetime48/40; those
drafts stay open and unchanged.

Source95e0255 already owns Store::export_selected, inspect_backup and the complete
selected history/media validators. Export writes a new external destination and
publishes backup.json last; format2 excludes configuration and runtime/credential
trees. Inspection accepts supported format1/2 with bounded exact-object closure.
Store::restore still refuses format2. Ordinary Store::export includes a historical
config snapshot, so exposing it as portable exclusion-safe backup is not selected.
No archive codec, restore, namespace, selection or mode-setter logic is rebuilt.

## Command and strict input
Add --archive-operation inspect|export-selected and required --archive-input FILE|-
to the actual binary. Input is exactly {"path":"ABSOLUTE_PATH"}, unknown keys
refuse. An inclusive16KiB UTF8 JSON file or exact-dash stdin is accepted; regular
absolute input file and target path checks reuse storage::files. Stdin needs EOF
and the caller owns deadline/cancellation. Reject relative/nonregular/symlink
input and unsafe target paths before opening a Store or creating a destination.
Commands conflict with runtime/model/logging/simulation and other one-shot flags.
The route precedes dotenv and model/device/runtime construction.

Inspect does not load runtime configuration, open or initialize a Store, or write
the archive. It calls the existing whole-archive validator and returns only its
verified BackupInspection fields. This is historical custody from the validated
read, not a continuing freshness claim if another process later changes files.
Unknown, missing, corrupt, incomplete or incompatible archive input refuses;
missing input is not a valid empty archive.

Export-selected reads supported local configuration but refuses legacy sync
enabled. It opens only valid existing owned storage, without normal initialization,
repair, staging cleanup, service stop or lock bypass. Factor a second narrow
crate-private selected-aware existing opener over the existing private inner
validator; preserve public legacy and mode-specific opener behavior. Acquire the
current ordinary lease for absent/LocalOnly or exact explicit lease for shared/
isolated before export, retaining it and the Store/process lock through report
write/failure. Selected history can be archived as custody after a later mode
choice; no live domain readiness or matching remote membership is claimed.

Call export_selected exactly once. No ordinary fallback, restore, configuration
snapshot, current-generation replacement, mode mutation or automatic retry follows.
Existing destination or overlap with any data/cache/credential root refuses.
Partial failed output directories remain for deliberate inspection; never delete
or reuse them automatically. No successful response does not prove no complete
archive: the existing API can fail after marker publication. Inspect the original
destination to reconcile uncertainty; a new attempt requires explicit new intent.

## Report and custody
One <=16KiB JSON line, report_version1, operation, status, incomplete,
activation_performed=false and data=null or {inspection:BackupInspection}.
BackupInspection retains the existing format/manifests/objects/selected_scopes/
selection_receipts/complete_media/configuration_included field shapes. Status is
ok, invalid-input, unavailable, unsupported, busy or failed; no raw paths/errors,
credentials, record/media payload, current mode/selection token or restored claim
is serialized. Sanitized refusal must not become empty success. Partial media
is conveyed by complete_media=false, distinct from corrupt/missing promised data.

An export report owns Store/current-mode guards through a consuming single write.
Prefix-write failure appends no replacement JSON and never repeats export. Inspect
has no Store lifetime to acquire and cannot mint one. Library errors are mapped
conservatively; do not infer a category by substring or claim source/destination
immutability on uncertain I/O failure.

## Meaningful qualification
Actual CLI over temporary Store: export selected winner/retained historical media
and unrelated committed scopes, inspect that real destination, reopen source and
prove source inventory/selection unchanged. Configuration, credentials, cache and
runtime sentinels stay out. Cover format1/2 inspection, partial media, missing/
corrupt/unsupported archive, unknown/oversize/nonregular/relative input, bounded
file/stdin parity, missing/Busy/nonowned/partial Store, root overlap/existing
destination and no implicit ordinary fallback. Inspector must ignore poison config
and never create Store roots. Preserve legacy selected restore/export refusal.

Real module writer/fault controls: source mode/process ownership held inside the
writer and released after success/prefix failure, interruption before marker versus
after-commit uncertainty, deliberate inspect reconciliation and no second report/
automatic export retry. Unix FIFO refusal executes under hosted Linux. Reuse
existing fixtures/policies, avoid rerunning unchanged storage matrices manually.
Run affected routing/maintenance tests, strict lint/no-default and ordinary hosted
full pipeline; independent precode and final lifecycle review remain gates. No
live model/provider/native gate is manufactured for these host-only commands.
