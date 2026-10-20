# Saved memory-settings producer v1 — unimplemented precode

## Entry and bounds
Use --memory-settings-operation inspect|prepare|apply|status. Inspect has no input selector/stdin access; other operations require exact --memory-settings-input - with one EOF-delimited strict UTF8 JSON request. No file/default-path fallback or runtime/other-maintenance combination; entry precedes dotenv/provider/runtime initialization. REMARKABLE_BUDDIES_CONFIG selects one absolute existing file. Config cap1048576; input and complete single-LF report cap16384 bytes including whitespace/LF. Keep current host deadlines; no new polling/service/retry.

All request/intent/change records are exact objects with recursive unknown/duplicate refusal, not positional arrays. Supported version1, nonnil operation UUID and lowercase64hex hashes. General/basic/model/data-memory wire and validation/precedence remain unchanged.

## Fixed patch and parent semantics
CHANGES is a strict nonempty one-or-two-key object with only enabled/profile. Each selected key is exactly `{action:"set",value:VALUE}` or `{action:"clear"}`. Enabled VALUE is a JSON boolean, never null/string/number. Profile VALUE is an existing-decoder-accepted nonnil UUID string, never null/array/object, with exact decoded spelling preserved; no trimming, canonical reformatting or new UUID grammar. Clear removes the selected leaf. No whole memory object, selection/profile registry or arbitrary path patch.

If memory is absent, clear-only changes are exact no-ops and do not insert memory:{}. A set creates that missing object with only selected set children. An existing parent object remains present even when the final editable child is cleared; preserve memory:{} versus parent omission. Always preserve unrelated children including selection:null/object and original decoded text/origins elsewhere. Original memory:null/array and invalid whole files refuse, even if a patch could repair them. A logical raw-value no-op preserves exact original file bytes and performs no Store write.

Full current original and target Config/schema/value validation applies. Enabled omission/clear means typed false; explicit null is invalid. Profile omitted/null are both typed None but different declaration origins; clear removes a declared null. Enabled true requires profile; nil UUID, missing profile when enabled and selected identity/profile mismatch refuse. Existing legacy-sync constraints remain. Never clear/rebind selection, create/discover/migrate/delete a profile or facts, change mode/group/device/actor, resolve credentials or call a provider/runtime/Reader.

## View and original identity
FIELDS has exactly literal enabled/profile keys. Enabled field exact `{origin:"default"|"declared",value:BOOLEAN}`. Profile field exact `{origin:"default"|"declared"|"declared-null",present:BOOLEAN}`. Missing parent/leaf gives default; profile:null gives declared-null/present:false. No old/new profile UUID, arbitrary string, path, group/catalog identity, raw error or credential reference appears in any report, including intent. Hashes/context are private host data, not renderer authority.

Inspect DATA exact `{schema_version:1,base_sha256:HASH,config_path_sha256:HASH,current:FIELDS}` from one strict saved-file read, without validating/probing declared roots or Store/profile/provider state. Path hash is SHA256 of UTF8 `urn:remarkable-buddies:memory-settings-path:v1:` plus exact explicit absolute UTF8 config path. Base/target hashes cover complete exact file bytes.

## Prepare, digest-only intent and same writer
Prepare exact `{memory_settings_version:1,operation:UUID,base_sha256:HASH,config_path_sha256:HASH,changes:CHANGES}`. Refuse original file/path mismatch without refreshing. Apply changes only to the fixed nested leaves, preserve parent rules, use the existing explicit recursive string-key-ordered compact UTF8 raw target serializer with no file LF and full1MiB target cap. Unrelated values/absence/null survive semantically. No-op keeps original bytes.

Patch digest is SHA256 of UTF8 `urn:remarkable-buddies:memory-settings-patch:v1:` followed by recursively key-sorted compact UTF8 CHANGES JSON without LF, preserving string contents. Pin an independently calculated boolean/accepted UUID-spelling vector and reordered/escaped-input equivalence against actual implementation.

INTENT exact ordered6 fields `{memory_settings_version:1,operation:UUID,base_sha256:HASH,target_sha256:HASH,config_path_sha256:HASH,changes_sha256:HASH}`; base differs from target; no raw changes/UUID profile. Prepare changed DATA `{before:FIELDS,after:FIELDS,intent:INTENT}`. No-op DATA `{current:FIELDS,base_sha256:HASH,changes_sha256:HASH}` with no intent/write.

Apply exact `{intent:INTENT,changes:CHANGES}`. Verify original version/shapes/path/base/canonical-patch/desired target before the SAME conditional config writer/mutex/CAS/exact readback. Validate declared paths at apply and acquire current existing ordinary/selected Store plus unconfigured/local/shared/isolated configuration custody exactly as the existing basic/model writers. No initialization/repair, domain/profile constructors or refresh/fallback. This current file-write custody is not original mode continuity or selected domain permission. Store/mode remain through the single consuming report.

## Pure status and report
Status exact `{intent:INTENT}`; raw changes are forbidden/not required. Read only the original config, compare complete original desired bytes and emit desired-file-observed or unresolved. No Store/declared-root/credential/profile/catalog/provider probe or write, no historical publisher/apply proof, active memory/readiness claim or automatic retry. A later refusal cannot settle the original potentially dispatched unknown invocation.

Exact common report `{report_version:1,operation:OP,status:STATUS,outcome:OUTCOME,disk_readback_verified:BOOLEAN,runtime_activation:"unverified",data:DATA_OR_NULL}`. STATUS ok,invalid-input,unavailable,unsupported,busy,conflict,failed. Runtime activation stays unverified for EVERY operation, including verified apply. Saving false does not disable explicit maintenance; saving true/profile does not activate automatic Reader memory, current membership or a running profile. No restart-needed/next-request promise is inferred.

| Success | outcome | disk_readback_verified | DATA |
| -- | -- | -- | -- |
| inspect | read-only | false | {schema_version:1,base_sha256,config_path_sha256,current:FIELDS} |
| prepare changed | prepared | false | {before:FIELDS,after:FIELDS,intent:INTENT} |
| prepare no-op | no-change | false | {current:FIELDS,base_sha256,changes_sha256} |
| apply | verified | true | {target_sha256,current:FIELDS} |
| status exact target | desired-file-observed | false | {observed_sha256,current:FIELDS} |
| status different valid file | unresolved | false | null |

Known pre-publication refusals: null DATA/false disk/outcome not-dispatched (inspect/status refusal read-only). Possible atomic publication/readback failure: failed/unknown with null DATA/false disk. Encode/bound before one consuming write, with no second report after partial output. Missing/truncated output stays unknown; no rollback, automatic replay, profile/data reset or membership inference. Existing explicit memory query/selected/catalog contracts stay intact; future host UI/private patch lifetime/stale-view handling and runtime/native qualification remain separate.
