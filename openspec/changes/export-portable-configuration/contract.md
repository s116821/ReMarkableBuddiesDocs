# Portable configuration V1 wire contract

## Fixed selectors

`reader-buddy --export-portable-configuration ABSOLUTE_CONFIG_FILE`

`reader-buddy --inspect-portable-configuration ABSOLUTE_ARTIFACT_FILE`

These are exclusive clap selectors; no other runtime/configuration selector or argument is admitted. They dispatch before startup and read no stdin. The source configuration environment variable, dotenv, credential variables and default config are not consulted. File input reuses existing regular-file/reparse/symlink/parent-path refusal. This inherits the trusted/quiescent local-path model of files::read; it is not a hostile-filesystem race or stable live-file snapshot guarantee. FIFO refusal is before open for a quiescent named FIFO. The bytes actually retrieved are the validation/projection basis.

## Exact artifact

```json
{"portable_configuration_version":1,"settings":{"personalization":{"enabled":false,"text":"Sample preference"},"product_settings":{"reader_enabled":true},"research_policy":null}}
```

Root has exactly two required members; version is the JSON integer1 and settings is an object. Each allowlisted setting is optional. Product allows the existing schema_version/reader_enabled/writer_enabled/export_destination fields; personalization allows existing schema_version/enabled/text. Existing version1/type/text/value rules apply, including product map-only semantics and recursive duplicate rejection. Research policy is null, required or disabled as existing saved configuration supports. Product parent null is supported; personalization parent null is invalid. Empty settings and sparse objects are valid and retain omission. Export never inserts implicit defaults or schema fields into copied setting values.

Config fields absent from this artifact are outside V1 rather than reset commands. Null/absence are preserved data, not instructions to delete destination state. Settings cannot include config_schema_version or any excluded root field. Full artifact validation reconstructs only the allowlisted settings plus an internal config_schema_version1 for existing document validation; that internal field is not added to the artifact. No group, record key, causal revision, authority token or origin device is implied.

## Exact report

Every serialized report has exactly report_version, operation, status, runtime_activation, artifact and summary. report_version is1, operation is export or inspect, runtime_activation is always unverified.

On success, status is ok and summary is exactly {artifact_sha256:LOWERCASE_HEX64,declared_settings:INTEGER0_TO_3,personalization_included:BOOLEAN}. The count measures present top-level settings, not effective settings or changed destination fields. The boolean means the personalization member is present, even if its object is empty or text is disabled. Digest is SHA256 of compact serde_json serialization of the complete artifact value, excluding report/newline framing and input whitespace. It proves content correspondence only. Export includes the artifact; inspect sets artifact:null. Inspection of semantically identical whitespace/key-order variants therefore yields the same compact-artifact digest. Exact personalization string contents and declaration presence remain digest-significant.

Refusals set artifact:null and summary:null. Malformed/duplicate/unknown/type/invalid-value JSON is invalid-input; an unsupported configuration/preference/artifact version is unsupported; unavailable/unsafe/relative/special/oversized file input is unavailable. Overflow of the final output bound is a fixed output-failure without a JSON report. CLI syntax/conflict errors retain clap's ordinary exit behavior. A successfully serialized semantic refusal exits0; consumers must inspect status. No raw parsing/I/O error, source path, source-config digest, text excerpt or credential reference is reported.

## Bounds and output

Saved config input uses inclusive storage::MAX_RECORD (currently1MiB). Artifact input uses inclusive131072bytes. Report output uses inclusive131072bytes including its single trailing newline. Parse one complete JSON value; trailing whitespace is legal and trailing data is invalid. Source input is not reparsed from disk; digest/summary derive from the exact produced/validated artifact value. The report is constructed and bounded before any write, then consumed through write_all and flush. Partial write or flush error returns output-failure without a replacement report/retry. No persisted artifact or running reload is claimed. Caller selects private access/storage for the explicitly exported text; stdout redirection is outside the producer's write authority.

## Acceptance mapping

- Source parser reuse and exclusion: whole-valid config with unique endpoint/path/credential/selection sentinels; only allowlisted keys and declared values survive, including disabled multilingual text.
- Declaration truth: omitted parents, null product/research, sparse objects, empty settings, missing/explicit schema and every legal enum roundtrip unchanged.
- Complete refusal: duplicate top-level/nested/null members, arrays, excluded root/settings keys, unknown child/version, invalid Unicode/escape/NUL/text limit, invalid unrelated source value and trailing data refuse whole output.
- Actual CLI: export real synthetic config, save extracted artifact, inspect using only that file with invalid default config/env present; verify summary digest, redaction, byte-preserved source and zero created roots. No nonexistent root needs to exist for value validation.
- Limits/I/O: exact accepted artifact input length via padding and one-byte-over refusal, maximum text escaping fits report bound, relative/missing/directory/symlink/FIFO refusal, exclusive selectors, prefix and flush failure without second frame.
- Existing boundaries: old saved configuration inspection remains text-redacted; no Config/archive schema/writer changes and no native/provider/sync effects.
