# Saved model-settings producer contract v1

## Fixed entry and bounds
Use --model-settings-operation inspect|prepare|apply|status. Inspect has no input selector/stdin access; the other operations require exact --model-settings-input - and EOF-delimited strict UTF8 JSON, never a file fallback. Refuse any runtime/other-maintenance combination before dotenv/runtime/provider initialization. REMARKABLE_BUDDIES_CONFIG selects one explicit absolute existing file; no --config/default-file fallback.

Config cap1048576 bytes; mutation/status stdin and complete single-LF report each cap16384 bytes, including whitespace/LF. Preserve current host deadlines/private/public/stderr bounds; no additional service/polling/retry. All request/intent/change records are objects with exact keys and recursive unknown/duplicate refusal, not positional arrays. Supported version1, non-nil operation UUID, lowercase64hex hashes and safe counts only. General/basic wire and limits are unchanged.

## Fields and exact string semantics
Only root model and base_url are editable. CHANGES is a strict nonempty one-or-two-key object. Each selected key has exactly `{action:"set",value:STRING}` or `{action:"clear"}`; no null, extra field, coercion, nested setting or whole Config. Set requires !value.trim().is_empty() and UTF8 byte length at most256 for model/2048 for base_url. Trim is a validation check only; retain the exact provided text, including currently accepted Unicode/control/CRLF/trailing whitespace. No URL parsing, scheme validation, userinfo/query/fragment stripping or provider eligibility follows. Clear removes the key, including a present null; absent fields remain unchanged. Full original/result Config/schema/value validation is mandatory; invalid whole files are not repaired.

FIELD is exactly `{origin:ORIGIN,present:BOOLEAN}`; ORIGIN is default,declared,declared-null. Missing/null Option leaves have present:false but distinct origins. No effective default model string, endpoint value/host, credential reference/text, lengths, path, errors or arbitrary saved/new text appears in any report. FIELDS has exactly literal model and base_url keys.

## Original inspection and hash-only intent
Inspect returns private `{schema_version:1,base_sha256:HASH,config_path_sha256:HASH,current:FIELDS}` from one pure strict saved-file read, without declared-root/Store/credential/environment/provider probes. Path hash is SHA256 of UTF8 `urn:remarkable-buddies:model-settings-path:v1:` plus the exact explicit absolute UTF8 path. Base/target hashes cover complete exact file bytes. General/basic observation cannot be substituted as this operation's private context or a live capability.

Prepare input is exactly `{model_settings_version:1,operation:UUID,base_sha256:HASH,config_path_sha256:HASH,changes:CHANGES}`. Refuse original mismatch without refresh/write. Reuse the existing recursive string-key-ordered compact UTF8 Config serialization with no file LF and full1MiB target bound; do not depend on serde_json Map feature order. Unrelated values/origins survive semantically; no-op keeps original bytes.

Patch digest is SHA256 of UTF8 `urn:remarkable-buddies:model-settings-patch:v1:` followed by the exact ordered compact JSON bytes of CHANGES, recursively sorting object keys while preserving all string contents. Pin an independently calculated vector with Unicode/CRLF/URL credential/query/fragment/trailing text. The hash binds the original patch without returning it.

INTENT has exactly ordered fields `{model_settings_version:1,operation:UUID,base_sha256:HASH,target_sha256:HASH,config_path_sha256:HASH,changes_sha256:HASH}`. Base and target differ. It contains NO raw changes/strings. Prepare with a change returns `{before:FIELDS,after:FIELDS,intent:INTENT}`. No-op returns `{current:FIELDS,base_sha256:HASH,changes_sha256:HASH}` with no intent/write. The host retains the original raw patch separately, privately and unchanged; output hashes are not renderer data or bearer authority.

## Apply and status
Apply input is exactly `{intent:INTENT,changes:CHANGES}`. Check version/shapes/original path/base/patch digest, recompute exact target and compare its original hash before the SAME guarded conditional atomic writer. Current existing ordinary/selected Store and supported unconfigured/local/shared/isolated mode custody are validated, without weakening ordinary admission or changing mode. Hold original byte CAS/publication/readback under the existing mutex and Store/mode through consuming output. No initialization/repair, root retarget, secret/reference change, runtime reload, provider or service action.

Status input is exactly `{intent:INTENT}` and MUST NOT contain or require raw changes. It reads only the original saved file, compares complete original target bytes and reports desired-file-observed or unresolved; no Store/declared-root probe/write/source credential/provider access. It cannot prove which process published bytes, historical apply identity, active environment/runtime or rollback. Current target bytes do not permit repeating apply; original-base mismatch refuses and caller uses status. A later refused status invocation cannot settle the original possibly dispatched unknown attempt.

## One bounded report
Exact common fields are `{report_version:1,operation:OP,status:STATUS,outcome:OUTCOME,disk_readback_verified:BOOLEAN,runtime_activation:ACTIVATION,data:DATA_OR_NULL}`. STATUS is ok,invalid-input,unavailable,unsupported,busy,conflict,failed. ACTIVATION is unverified except verified apply restart-required. No arbitrary old/new strings or raw errors/logging are emitted; encode fully/bound before one consuming write and never emit a second error report after prefix failure.

| Successful operation | outcome | disk_readback_verified / activation | Exact data |
| -- | -- | -- | -- |
| inspect | read-only | false / unverified | {schema_version:1,base_sha256,config_path_sha256,current:FIELDS} |
| prepare with change | prepared | false / unverified | {before:FIELDS,after:FIELDS,intent:INTENT} |
| prepare no-op | no-change | false / unverified | {current:FIELDS,base_sha256,changes_sha256} |
| apply | verified | true / restart-required | {target_sha256,current:FIELDS} |
| status exact target | desired-file-observed | false / unverified | {observed_sha256,current:FIELDS} |
| status nonmatching file | unresolved | false / unverified | null |

Any refusal before possible publication has null data/false disk/unverified activation and outcome not-dispatched (inspect/status refusal read-only). Any possible atomic publication/readback failure is failed/unknown with null data/false disk/unverified activation. Missing/truncated output stays unknown; no automatic retry/reapply/rollback/cleanup. Consumer memory/cancel/navigation/unknown references and the private original-patch buffer require separate concrete host precode; no both-host API/UI implementation is claimed here.

## Preservation and verification
Existing basic/general output shapes, bytes/origins/limits and resolve/DEFAULT_MODEL/environment/credential precedence stay unchanged. Current model precedence is CLI→saved→default (no OPENAI_MODEL input in this resolver); endpoint is CLI→OPENAI_BASE_URL→saved. Saved-file success does not verify that any override is effective. Source tests use synthetic private values only, no actual provider request/credential hunt/tablet.

Verify exact no-op/pasted bytes/set/clear/null/missing/unrelated legacy values; no old/new value echo in all successful/refused/fault reports including hash-only intent; independently pinned patch bytes; forged patch/target/path/base and cross-kind refusal; ordinary/selected four-mode/Busy/current owner custody without data changes; before/after atomic/readback/prefix faults and original-versus-later status; strict shapes/caps/EOF/no inspect stdin and exact Args inventory. Retain native actual CLI bytes/executable provenance and old basic/general compatibility fixtures without replay for handoff. Source/CI/consumer/runtime/device qualification remain separate gates.
