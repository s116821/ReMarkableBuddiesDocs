# Product settings producer contract v1 — review candidate

Authority: one coordinated proposal from Main's current Buddy
`e1e79226b31fddb7339ca3c59038c88f048fc3a9`, reconciled with the delivered
Basic transaction recipe. This is the proposed freeze, not implemented behavior
or admission to code until coordinated review accepts this exact amendment.
Contract/schema revisions are not maintained application release versions.

## Saved object and projection

Existing top-level config schema remains1. Optional `product_settings` is an
object with only `schema_version`, `reader_enabled`, `writer_enabled`,
`export_destination`. Missing/null parent, empty or version-only object are valid.
Missing schema_version means1; explicit null/noninteger is invalid-input; another
integer is unsupported. Unknown/duplicate fields, arrays/positional structs,
null leaves and wrong types refuse. The two role leaves are booleans; destination
is exactly `mem` or `disabled`. Missing leaves resolve true/true/mem. No environment
override, URL/origin, account/workspace/collection/note ID, path or secret is added.

Current is exactly the sorted map export_destination/reader_enabled/writer_enabled.
Each value is exactly `{origin,value}` with origin default or declared. Default
origin requires the corresponding true/true/mem value; declared origin retains
its actual supported value. Missing/null parents and missing leaves have default
origin. Inspection never materializes defaults or exposes unrelated config.

Clear removes only its leaf. Under absent/null parent it is byte-identical no-op.
Set under absent/null parent materializes schema_version1 and only changed leaves.
Set under an existing object preserves omission/presence of schema_version.
Clear-last preserves parent and any schema member: version+reader false becomes
version-only; reader false without version becomes empty object. Siblings and
unrelated declarations survive. An unchanged patch preserves original exact bytes;
changed targets use recursively sorted compact UTF8 JSON, no added newline.

## CLI and input

Fixed dedicated `--product-settings-operation inspect|prepare|apply|status`.
Inspect has no input and does not read stdin. Other phases require exactly
`--product-settings-input -`, one bounded JSON object and EOF. Other input selectors
refuse before input/config I/O; selectors conflict with unrelated CLI operations.
Successful explicit response negotiates this capability; generic config_versions
stays[1]. Existing basic/model/research/memory/general-inspection wires stay frozen.

Prepare request has exactly product_settings_version:1, operation, base_sha256,
config_path_sha256, changes. Operation is canonical lowercase nonnil UUID; digests
are lowercase64hex. Changes is a nonempty closed dirty map of only the three
supported leaves. Each edit is exactly `{action:"clear"}` or
`{action:"set",value:SUPPORTED_VALUE}`. No Keep entry is sent.

Intent has exactly product_settings_version, operation, base_sha256, target_sha256,
config_path_sha256, changes, in that serialization order. It binds the unchanged
original request and reconstructed target, with base different from target.
Apply/status input is exactly `{intent:ORIGINAL_INTENT}`. No regenerated intent,
new base, operation substitution, fallback file or automatic retry is permitted.

Base/target hashes are SHA256 of exact file bytes. Path hash is SHA256 of UTF8
`urn:remarkable-buddies:product-settings-path:v1:{absolute_path}`, no newline.
Saved configuration bound is1MiB; requests and reports are at most16384bytes.
Defined objects reject duplicate/unknown members and invalid types; no coercion,
unit-enum array or numeric boolean/version spellings are accepted as other types.
Reports are exactly one compact UTF8 JSON object followed by one LF, without BOM,
extra document or raw multiline framing. Numeric version tokens are plain integers.

## Report matrix

Envelope has exactly report_version:1, operation, status, outcome,
disk_readback_verified, runtime_activation, data. Operations are the four above.
Statuses are ok/invalid-input/unsupported/unavailable/busy/conflict/failed.

| Successful operation/outcome | Exact data keys | Readback / activation |
| -- | -- | -- |
| inspect/read-only | schema_version:1,base_sha256,config_path_sha256,current | false/unverified |
| prepare/prepared | before,after,intent | false/unverified |
| prepare/no-change | current,base_sha256 | false/unverified |
| apply/verified | current,target_sha256 | true/restart-required |
| status/desired-file-observed | current,observed_sha256 equal original target | false/unverified |
| status/unresolved | current,observed_sha256 different from original target | false/unverified |

All non-ok data is null, readback false, activation unverified. Inspect/status
refusals are read-only. Prepare/apply pre-dispatch refusals are not-dispatched;
failed apply may additionally be unknown after possible publication. A well-shaped
wrong path is conflict; stale original base is conflict; wrong reconstructed target
is invalid-input. Structural malformed intent is invalid-input and future version
unsupported. Missing/unsafe selected files are unavailable; Busy and conflict stay
distinct. Atomic publication Refused is failed/not-dispatched; Unknown or unexpected
verified digest is failed/unknown. No status proves historical authorship/rollback.

Inspect/prepare/status do not open Store or resolve model/Mem credentials. Apply
uses the existing Store::replace_config_document and original CAS/filesystem/config
admission/mode custody, held through complete or failed report writing. No expanded
storage-generation eligibility, second writer/transaction engine or service RPC.

## Actual entry gates and compatibility

Maintenance is available with all three settings disabled and without resolving
model/Mem credentials. Reader-off ordinary startup exits nonzero, empty stdout and
fixed secret-free disabled-setting diagnostic before credential/Store/device/model
construction; Writer-on does not auto-start a Reader loop. Every actual new Writer
generation/refinement/local prepare/export route uses the shared Writer helper.
New external export additionally requires Mem backend. Local drafts/prepare-export
need Writer enabled but not Mem. Joined notebook/generate/refine-and-export gates
both policies before any model effect. Existing current Reader has no automatic
Reader-to-Writer delegation: do not invent or claim that integration here.

Explicit Writer/note-export reconciliation remains available regardless of roles
and backend. It uses only a recorded original effect/target and cannot create/update,
create a replacement association/target, replay, auto-retry or imply rollback.
Disabling never deletes owned data, local drafts, export history or third-party notes.

**Intentional error-order change:** after valid export request preflight, nonsecret
config/policy checks move before MEM_API_KEY resolution (current code reads the token
first). Malformed-config versus missing-token precedence changes deliberately.
Credential selection order and literal bytes, fixed Mem origin and existing valid
editor wires remain unchanged. No new credential key or environment override.

## Qualification limits

Saved readback/restart-required is not runtime activation. No OS restart/reload,
provider/account/model call, device/native capability or complete destination setup
is qualified here. Wider Reader/Writer integration and REM-42 acceptance remain
open. Literal fixture bytes are synthetic definitions, not producer executions.
