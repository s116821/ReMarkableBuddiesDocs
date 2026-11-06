# Design

Exact frames/status/bounds and qualification mapping are in [contract.md](contract.md).

## Source and ownership
Pinned delivered source is Buddy4a75316e358a471a08ba28c0c9408d1c6eacff3f; Docs base9c64e47852f9cf8c4a9076a73f8bef5444a33873. Main owns the paired source/spec work, Root independent review/integration. Manager notebook restore, REM-43/39 and Native REM-61 ownership remain separate. No implementation precedes this contract.

## Reuse
Add config::portable rather than another Config parser or writer. Reuse config::inspection::document for whole typed validation, recursive duplicate rejection, map-only configuration checks and raw declaration access. This intentionally validates values without StorePaths admission, environment resolution, filesystem-root inspection or credential loading. Existing product/personalization/research validators remain authoritative. Source Config is valid as a whole; invalid excluded settings do not disappear before validation.

## Allowlist and declaration semantics
Artifact is exactly {portable_configuration_version:1,settings:{...}}. Settings is a map with only optional product_settings, personalization and research_policy. Copy the source raw values only after validation. Preserve absent parents, sparse child declarations, explicit supported null, disabled personalization text and exact Unicode/newlines. Do not serialize a defaulted Config into the artifact. Product fields/schema, personalization fields/schema and research enum reuse existing definitions. Validate an artifact's settings through the same strict Config document boundary, plus exact artifact/settings key allowlists. Require integer version1 (reject float1.0), object roots and recursive duplicate/unknown rejection. This version does not claim complete portable configuration coverage.

Exclude model/base_url/model_credential, paths, sync, memory, reader, log/debug/gesture settings and every other source key. No actor/device/group/selection identity, endpoint, credential reference or runtime binding is a portable setting. Product enable/export choices and research preference remain saved declarations; transporting them never grants execution/export or enables tools.

## CLI and artifact boundary
Two fixed mutually exclusive selectors: --export-portable-configuration CONFIG_FILE and --inspect-portable-configuration ARTIFACT_FILE. Both require an absolute existing regular file, reject '-' and never read stdin or default/environment config. Dispatch before dotenv/logger/provider/runtime initialization. Reuse files::read and its regular-file/path safety plus inclusive MAX_RECORD for saved config. Artifact input has inclusive128KiB bound. Source bytes are parsed once; output is a snapshot of those retrieved bytes, not a claim of a stable live config revision. No locking or Store admission is inferred.

Report is exactly report_version:1, operation:export|inspect, status:ok|invalid-input|unsupported|unavailable, runtime_activation:unverified, artifact (export success only, otherwise null), and summary (success only, otherwise null). Summary contains artifact_sha256, declared_settings count and personalization_included boolean; no paths, source-file hash, raw error, text preview or effective-state claim. Digest hashes compact serde_json serialization of the exact emitted/validated artifact, excluding report framing; it proves content correspondence, not authenticity or actor identity. Inspect never echoes artifact/text. Exit0 means the bounded report was written; semantic status remains in the frame. CLI argument errors retain ordinary clap behavior.

## Privacy and I/O
Explicit export is a private artifact containing the selected personalization text; routine reports/logs/Debug must not disclose it. Report/portable containers have no derived Debug that prints the artifact. Bound final newline-inclusive output to128KiB before one consuming write_all + flush. A prefix/flush error returns fixed output-failure and emits no replacement JSON, retry or cleanup. Export writes stdout only; caller owns artifact extraction/storage/access. Neither command writes files, imports configuration, modifies archive formats or admits cloud/native effects. Existing saved inspection remains text-redacted and unchanged.

## Verification
Real config fixtures with excluded sentinel endpoint/path/credential/selection values prove artifact exclusion. Use actual CLI export, extract artifact, save it, inspect offline and compare exact digest/declarations/text while source bytes remain unchanged. Exercise no-parent/sparse/null/disabled Unicode cases; invalid source values/duplicates/unknowns; strict artifact version/unknown/settings/null/type/extra/duplicate rejection; size boundary; missing/relative/symlink/FIFO input refusal; selectors conflicting with runtime options; output prefix/flush failure without replacement; inspect secret redaction and missing root paths with no created directories. No provider/tablet or artificial simulator workflow is required for an offline serialization boundary. Full current-head normal CI and independent final review are required before canonical sync/archive in the same paired PRs.

## Remaining integration
Selected archive configuration remains excluded. Existing full local snapshots are not reclassified or rewritten. Import/application, model/memory preference portability, selected stable-key publication, cross-actor/cloud/media/native qualification and whole REM-52 remain open. This finite utility is independently usable for explicit private preference export/validation.
