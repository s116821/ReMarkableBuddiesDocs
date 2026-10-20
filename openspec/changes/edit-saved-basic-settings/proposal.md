# Edit supported saved basic settings

## Why and scope
After saved-configuration inspection, both companions need deliberate edits to the existing trigger_corner, log_level and debug_dump declarations. Add only set/clear for these three current fields, preserving unrelated values and declaration origins, whole-file conflict detection and verified disk readback. One explicit Save authorizes internal preview plus at most one conditional write; no extra user confirmation loop is introduced.

Reuse the existing guarded configuration writer and wired host adapters. Do not add unsupported settings, a general JSON editor, credentials management, model/backend/path changes, mode/group changes, runtime activation or automatic service control. No provider question or REM57 device contact is needed for implementation.

## Authority and delivery
Selected under current REM42 chronology and source-backed assessment9a83563a, after producer actual181a0a1e9d6aec90e7c1778bc6c9b236ea46aaa6 / Docs7b30033b9e304c117ef6ac24dd5ce6f1414cc442 tree verification. Main owns producer/central contract, SCRAPPY the shared consumer, Root review. This active proposal is unimplemented and remains in one linked delivery through verification/sync/archive; no planning-only completion or new workflow gate is created.

## Source basis
Actual Config, config/personalization.rs, storage/recovery.rs::replace_config, storage/maintenance.rs and mode/selection custody at immutable181a0a1; existing Manager personalization/forget/saved-configuration patterns and current issue comments. Existing replace_config serializes typed defaults, while ordinary open_existing refuses selected formats. The following preservation/admission extensions are design decisions, not current capabilities. Historical Reader personalization PR49 and all held work stay untouched.
