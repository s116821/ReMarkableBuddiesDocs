# Portable preference import v1 contract

## Entry and bounds

Add exclusive `--portable-configuration-operation inspect|prepare|apply|status`. Destination is an existing absolute UTF8 Config path selected explicitly by REMARKABLE_BUDDIES_CONFIG; no default Config/dotenv fallback. Inspect rejects input and never reads stdin. Other operations require exact `--portable-configuration-input -`, one EOF-delimited strict duplicate-free JSON object and no input-file fallback. Dispatch precedes logger/runtime/credential/provider initialization. Existing export/inspect selectors and their no-environment contract remain unchanged.

Saved Config original/target each cap1048576bytes. Request cap262144bytes, including allowed trailing whitespace. The nested artifact must validate through the existing version1 closed validator and have compact serialized length at most131072bytes. These are separate inclusive bounds: the request framing is not permission to enlarge the artifact or destination. Output is one newline-inclusive frame of at most16384bytes. Invalid/duplicate/trailing-data/type/unknown-member input refuses; unsupported schema/version refuses as unsupported. Nil operations, malformed lowercase64-hex digests, equal base/target changed intents and impossible field combinations refuse.

## Prepare and target

Prepare request is exactly `{portable_import_version:1,operation:UUID,base_sha256:HEX64,config_path_sha256:HEX64,artifact:ARTIFACT}`. ARTIFACT retains the existing `{portable_configuration_version:1,settings:{...}}` schema and three-setting allowlist. The overlay rules in design.md apply at parent/child declaration level. Whole original and resulting target must validate; unrelated raw values and absent declarations remain unchanged. If the raw value tree is unchanged, return no-change and preserve original bytes. Otherwise serialize the complete raw target using existing compact serde_json ordering and enforce the Config bound.

Config path digest is SHA256 of UTF8 `remarkable-buddies-portable-import-path-v1\0` followed by the exact admitted absolute UTF8 path string, with no path rewriting. Original base digest hashes the exact retrieved Config bytes. Artifact digest uses the existing compact complete-artifact recipe, not raw whitespace. Target digest hashes exact target publication bytes. This establishes correspondence, not provenance/authenticity or a hostile live-filesystem snapshot.

Changed Prepare returns exactly this intent: `{portable_import_version:1,operation:UUID,base_sha256:HEX64,target_sha256:HEX64,config_path_sha256:HEX64,artifact_sha256:HEX64}`. It contains no artifact, preference values or path text. Preview metadata may contain only the fixed allowed setting names that change, declaration-presence counts and digests; it never echoes personalization text, excluded destination settings or parser/I/O errors. Unchanged Prepare returns no intent.

## Apply and Status

Apply request is exactly `{intent:INTENT,artifact:ARTIFACT}`. Require original path/base/artifact correspondence and recomputed target hash before Store admission. Apply validates the existing configured roots, admits only legacy1 or ready ordinary notebook4 through one original existing-only Store/mode custody, then uses Store::replace_config_document with original base and exact target. No fresh base, target rebase, default materialization or alternate file is substituted. Foreign/changed artifact, stale Config or path refuses without publication. No-op is settled by Prepare rather than a changed Apply intent.

Status request is exactly `{intent:INTENT}`. It reads the same explicit destination and checks path correspondence; exact desired full bytes mean desired-file-observed, otherwise unresolved. It needs no artifact, Store, roots or provider. Observation cannot identify the original publisher or settle historical uncertainty. A changed path is conflict/read-only. Status never invokes Apply.

## Reports and custody

Every report has exactly report_version1, operation, status, outcome, disk_readback_verified, runtime_activation and data. runtime_activation is always unverified. Inspect/Status refusals are read-only; Prepare/Apply refusals are not-dispatched except attempted publication uncertainty. Status categories reuse ok/invalid-input/unsupported/unavailable/busy/conflict/failed. Data is null on refusal; successful data is a closed operation-specific metadata object containing only the above admitted names/counts/digests/intent, never raw values/artifact/path/error. The entire transport is private because hashes can expose low-entropy text by offline comparison; do not add Debug/log rendering.

The literal report_version value is1; operation is the selected inspect/prepare/apply/status string. Outcomes are exactly read-only, prepared, no-change, verified, desired-file-observed, unresolved, not-dispatched or unknown. disk_readback_verified is true only for verified Apply. Successful data shapes are exactly:

- Inspect, ok/read-only: `{base_sha256:HEX64,config_path_sha256:HEX64,current:ORIGINS}`.
- Changed Prepare, ok/prepared: `{intent:INTENT,changed_settings:NAMES,before:ORIGINS,after:ORIGINS}`.
- Unchanged Prepare, ok/no-change: `{base_sha256:HEX64,artifact_sha256:HEX64,changed_settings:[]}`.
- Verified Apply, ok/verified: `{target_sha256:HEX64,changed_settings:NAMES}`.
- Status, ok/desired-file-observed or ok/unresolved: `{observed_sha256:HEX64}`.

ORIGINS has exactly product_settings, personalization and research_policy, each absent, declared-null or declared. NAMES is a nonempty lexically sorted unique subset of those three literal names whose complete raw parent value changed; it contains no child values. Origins do not describe effective defaults or authentication. No other success data keys are allowed.

Oversized request or compact embedded artifact and oversized computed target are invalid-input. Missing/unsafe/oversized original Config input is unavailable. Unsupported protocol/artifact/config/preference versions are unsupported; malformed versions/types are invalid-input. Final report serialization/bound/write failure returns fixed output-failure without a replacement frame; complete semantic reports retain the existing one-shot exit convention. CLI selector/input conflicts remain ordinary argument errors.

Apply maps existing ConfigPublication::Verified matching target to ok/verified with disk_readback_verified=true; Conflict to conflict/not-dispatched; Refused to failed/not-dispatched; Unknown or unexpected verified hash to failed/unknown. Do not infer that a publisher Refused result proves no owned temporary ever existed; preserve existing publisher/staging semantics. Once publication may have occurred, keep unknown without rollback, replay, automatic retry or a second report. Retain actual Store/mode custody through the single consuming write_all and release on success/error. Do not flush or replace a failed frame. Inspect/Prepare/no-op/Status acquire no Store. Prefix loss is caller uncertainty, never an automatic repeat.

## Non-effects

No reset/clear-all, credentials/reference/endpoint/model/memory/path/device/group/runtime settings, Store/data/media changes, archive import, cloud transfer, native authority, service restart, effective authentication or running activation is granted. Existing selectors/artifact bytes and other maintenance-family boundaries remain unchanged.
