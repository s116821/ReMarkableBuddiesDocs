# Why
REM-53 requires a real portable personalization setting before the shared Manager editor can save it. Current schema-1 configuration rejects that field. This bounded increment provides the field, guarded maintenance CLI and verified disk reload contract without claiming Reader/Writer/provider or sync integration.

# What Changes
Add optional defaulted versioned personalization settings; preserve exact UTF-8 multiline text. Reuse REM-36 Store::replace_config, ownership preflight and stable exclusive lease for mutations. Add fixed inspect/set/disable/clear commands with bounded stdin and explicit configuration selection, revision comparison, sanitized failures and verified readback. Expose immutable validated snapshots for later receiving request consumers.

# Capabilities
## New Capabilities
- `personalization-config-contract`: portable setting and guarded local configuration maintenance.
## Modified Capabilities
- `platform-runtime`: align the existing startup and exclusive CLI requirements with fixed offline personalization maintenance while preserving normal startup and diagnostic behavior.

# Impact
Rust config/CLI and central public documentation only. Root owns coordinated review/delivery; Manager owns the editor and Main retains receiving-buddy/provider/domain/SDK work. No native or account operation, second backend writer, Buddy API or sync engine.
