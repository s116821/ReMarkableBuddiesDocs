# Saved research-policy producer v1

This is a dedicated saved-declaration interface. It grants no runtime, research
acquisition, model, service, native or Manager capability.

## Configuration and snapshot
Optional root research_policy is null, "required" or "disabled". Missing/null
resolves to Required. Config default remains absent when serialized; supported
explicit enum values serialize normally. Clear removes the key; set accepts only
the two exact strings, never null. Existing raw null remains distinguishable.
Config schema stays 1 with this additive supported declaration; older binaries
can refuse it. Unknown/new schema or invalid whole-file declarations refuse.
The pure typed snapshot validates values without Config::validate filesystem
traversal, captures only resolved policy and exposes no mutable field. It is
caller-supplied validated data, not saved-file/readback attestation.

## Selection and bounds
The fixed explicit absolute existing regular config is selected through the
existing REMARKABLE_BUDDIES_CONFIG mechanism; no --config flag/default-file lookup.
Use existing strict config/checked-document rules and 1048576-byte file cap.
Request and single newline-terminated report caps are 16384 bytes each.
Inspect has no input and never consumes stdin. Other operations require explicit
--research-settings-input -; any file/absent input refuses without reading it.
The selector is --research-settings-operation inspect|prepare|apply|status.
It returns before ordinary runtime/provider/credential startup and is exclusive
with all existing maintenance/simulator/runtime selectors.

## Input
Objects are strict, including nested change actions and intent. Duplicate fields,
unknowns, arrays in object positions, trailing JSON, invalid UTF8, enum/type/nil
identity/digest/version or bound failures refuse without repair.
Prepare:
```json
{"research_settings_version":1,"operation":"NONNIL_UUID","base_sha256":"LOWER_HEX64","config_path_sha256":"LOWER_HEX64","changes":{"research_policy":{"action":"set","value":"disabled"}}}
```
The only alternative patch is {"research_policy":{"action":"clear"}}.
A patch must be nonempty and contain only research_policy. No other field/path,
provider options, query, request opt-out, enabled flag or schema edit is admitted.
Apply is {"intent":INTENT,"changes":ORIGINAL_PATCH}; status is {"intent":INTENT}.
INTENT contains exactly research_settings_version:1, operation, base_sha256,
target_sha256, config_path_sha256 and changes_sha256. Base differs from target.
It is private local workflow data, not authorization from a search/inspection.

## Binding and publication
base_sha256 and target_sha256 hash the exact respective complete file bytes.
config_path_sha256 hashes UTF8
urn:remarkable-buddies:research-settings-path:v1:
followed immediately by the exact absolute path's UTF8 spelling, without path
normalization or resolving a different file. A non-UTF8 selected path refuses.
changes_sha256 is SHA256 of the UTF8 prefix
urn:remarkable-buddies:research-settings-patch:v1:
followed immediately by the existing recursively Ordered compact JSON patch.
Original request bytes are not a substitute for that canonical patch fingerprint.
The target is existing Ordered full JSON after only the admitted root set/remove.
No-op returns current fields/base/patch hash without an intent or write.

Apply must match current original file/path, retained patch digest and deterministic
target before the SAME conditional writer. Reuse current full-root validation,
open-existing-for-config and ordinary/explicit selected-aware mode custody. Never
initialize/retarget/repair a Store, migrate data, read provider credentials or
change mode. A changed condition is not refreshed into a new attempt. A verified
readback proves exact target disk bytes only. Existing unknown/post-publication and
output-prefix failures remain uncertain; no fabricated rollback/second report.
Status reads only the selected file/original intent, compares complete target bytes,
and does not open Store/probe declared roots, replay apply or prove authorship.

## Output
Exactly one bounded JSON report plus newline. Outer fields:
report_version:1, operation, status, outcome, disk_readback_verified,
runtime_activation:"unverified", data. The only current field is research_policy:
{"origin":"default|declared|declared-null","value":"required|disabled"}.
value is the resolved SAVED policy; raw null has declared-null origin and required
value. This is not an effective environment/CLI/runtime claim.

Status uses the existing basic Status set: ok, invalid-input, unsupported,
unavailable, busy, conflict, failed. Data shapes match the existing saved-editor
pattern: inspection {schema_version:1,base_sha256,config_path_sha256,current};
prepared {before,after,intent}; no-change {current,base_sha256,changes_sha256};
applied {target_sha256,current}; observed {observed_sha256,current}. No extra kind
tag or arbitrary config/paths/text/credential value is exposed.
Outcomes are read-only, prepared, no-change, verified, desired-file-observed,
unresolved, not-dispatched or unknown under the existing phase semantics.
A refusal has null data; apply refusal before possible dispatch is not-dispatched,
while possible publication cannot become that claim. Only verified exact readback
sets disk_readback_verified. Pure status can prove desired-file-observed or
unresolved, never historical publication or settlement of an earlier unknown.
Complete refusal reports do not require a failing exit status; malformed CLI or
output-write failures retain the existing CLI failure behavior.

The phase matrix is fixed: successful inspect is ok/read-only with inspection
data; prepare is ok/prepared or ok/no-change; exact apply is ok/verified with true
disk_readback_verified and applied data. Pre-dispatch prepare/apply refusals use
their applicable non-ok status, not-dispatched and null data. Possible publication
uses failed/unknown, false readback and null data. Status with current exact target
is ok/desired-file-observed with observed data; a different file is ok/unresolved
with null data. Inspection/status admission refusals use the applicable non-ok
status, read-only and null data. All other rows have false readback. A later such
row never settles an earlier possibly dispatched attempt.

## Compatibility and limits
The broad saved-configuration v1 DTO and all previous editor wires remain unchanged.
Their unsupported research-policy view entry stays literal; dedicated producer
support does not authorize adding a Manager consumer or making that view editable.
No automatic restart, next-request adoption, live provider availability, source
freshness, model effectiveness or whole-project acceptance is claimed.
