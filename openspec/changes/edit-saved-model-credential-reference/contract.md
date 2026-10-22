# Saved model credential reference protocol v1 (unimplemented)

## Fixed entry
Use `--credential-reference-operation inspect|prepare|apply|status`. Inspect accepts no input selector and never reads stdin. Other operations require exact `--credential-reference-input -` and EOF-delimited strict UTF8 JSON, never a file fallback. Refuse runtime/other-maintenance combinations before dotenv/logging/provider/runtime initialization. `REMARKABLE_BUDDIES_CONFIG` selects one explicit absolute existing regular file; no default or caller file/reference-path fallback. Existing basic/model/memory/file-credential/general wires are unchanged.

Request and single-LF report each cap16384 bytes including whitespace/LF. Config input and serialized desired file cap1048576 bytes. All request/intent/change records are exact objects with recursive unknown/duplicate refusal, no positional arrays/coercion. Unknown version is unsupported; operation UUID must be nonnil and hashes lowercase64hex. Empty tagged clear records MUST reject extra fields (use strict empty-record rather than permissive unit-variant decoding).

## One leaf and declaration semantics
CHANGE is exactly `{action:"set",value:STRING}` or `{action:"clear"}`. Only root `model_credential` is edited; no field/path selector or arbitrary Config object. Set uses existing credential_name validation:1..80 ASCII letters/digits/hyphen/underscore, with exact decoded spelling/case preserved. No trimming, new grammar, normalization or set-null. Clear removes the key. Missing/null are both typed None but distinct declarations: absent clear is an exact byte no-op; declared-null clear removes the declaration and creates a changed target. Same accepted string is a byte-identical no-op, including original whitespace/escape spelling elsewhere. A different accepted case is a real raw-value change.

Validate the complete original and target with current Config schema/value rules. Original invalid/unknown/duplicate/type/schema/value/cap refuses even if a patch could repair it. Changed targets use the existing explicit recursively string-key-ordered compact raw UTF8 serializer without file LF. Preserve unrelated decoded values, omission/null origins, paths, schema, memory/selection/mode, personalization and credential-like model/endpoint strings. No credential file or root is discovered/probed/created/read/renamed/deleted here; no environment/CLI credential selection, provider/worker/service activity or default change.

FIELDS is exactly `{model_credential:{origin:"default"|"declared-null"|"declared",present:BOOLEAN}}`. Missing gives default/false, null declared-null/false, valid string declared/true. Present means only a saved reference declaration, never file presence or credential validity. No old/new name, path, arbitrary text/error or credential bytes appears in any report. Names/new change and all digest context remain host-private; even an accepted name can be confidential. Do not log or expose intent/hashes as renderer data or authority.

## Fingerprints and prepare
Inspect DATA is exactly `{schema_version:1,base_sha256:HASH,config_path_sha256:HASH,current:FIELDS}` from one strict saved-file read, with no declared-root/Store/credential/provider probes. Path SHA256 covers UTF8 `urn:remarkable-buddies:credential-reference-path:v1:` plus exact absolute UTF8 selected Config path. Base/target hashes cover complete exact file bytes.

Prepare request is exactly `{credential_reference_version:1,operation:UUID,base_sha256:HASH,config_path_sha256:HASH,change:CHANGE}`. Compare original file/path hashes without refresh. Patch SHA256 covers UTF8 `urn:remarkable-buddies:credential-reference-patch:v1:` plus recursively key-sorted compact UTF8 CHANGE JSON without LF, preserving decoded string contents. Pin independent set/clear vectors and reordered/escaped-input equivalence against actual implementation.

Changed prepare DATA is exactly `{before:FIELDS,after:FIELDS,intent:INTENT}`. INTENT is exactly `{credential_reference_version:1,operation:UUID,base_sha256:HASH,target_sha256:HASH,config_path_sha256:HASH,changes_sha256:HASH}` with base!=target and no raw change/name. No-op DATA is `{current:FIELDS,base_sha256:HASH,changes_sha256:HASH}` with no intent or write. The original CHANGE remains private caller state for apply.

## Same writer and current custody
Apply request is exactly `{intent:INTENT,change:CHANGE}`. Validate version/shapes/path/base/canonical change/desired target before the SAME existing conditional Config writer, mutex/CAS and exact readback. Apply validates declared roots and opens only the current existing selected-aware configuration Store, obtaining unconfigured/local/shared/isolated custody as existing editors do. No initialization/repair/domain constructor, mode/group switch, credential-file operation or fallback. Current Store/mode custody lasts through consuming output; preparation did not freeze mode or authorize a file operation.

Whole-file changes, alternate path, modified original change or forged target refuse without refreshing/repreparing. Same writer publication/readback faults preserve uncertainty. A successful reference change is not a credential-file grant, including when it makes the separate file protocol's original Config binding stale. Never infer historical settlement from such a later refusal.

## Pure original status and report
Status request is exactly `{intent:INTENT}`; raw change is neither accepted nor required. Read only the original Config/path, compare complete target bytes and emit desired-file-observed or unresolved. No declared-root/Store/credential-file/provider probe or write, historical publisher/receipt claim, rearm or replay. No name echo is required to observe desired full bytes.

Exact report is `{report_version:1,operation:OP,status:STATUS,outcome:OUTCOME,disk_readback_verified:BOOLEAN,runtime_activation:"unverified",data:DATA_OR_NULL}`. STATUS is ok,invalid-input,unsupported,unavailable,busy,conflict,failed. Every operation keeps runtime unverified, including verified apply; no restart/next-request/authentication/revocation promise. Clear does not delete the old file or revoke an environment/CLI/active credential. Saved true presence does not prove a protected file exists, is private, is selected effectively or authenticates.

| Success | outcome | disk_readback_verified | DATA |
| -- | -- | -- | -- |
| inspect | read-only | false | {schema_version:1,base_sha256,config_path_sha256,current:FIELDS} |
| prepare changed | prepared | false | {before:FIELDS,after:FIELDS,intent:INTENT} |
| prepare no-op | no-change | false | {current:FIELDS,base_sha256,changes_sha256} |
| apply | verified | true | {target_sha256,current:FIELDS} |
| status desired | desired-file-observed | false | {observed_sha256,current:FIELDS} |
| status different valid bytes | unresolved | false | null |

Malformed/duplicate/unknown/type/hash/UUID/cap/change/target faults use invalid-input; unknown version/unsupported current admission uses unsupported; missing/unreadable Config/Store uses unavailable; owner conflict uses busy; original file/path mismatch uses conflict. Refusals have null DATA/false disk and read-only outcome for inspect/status, not-dispatched for prepare/apply. Possible atomic publication/readback failure uses failed/unknown/null/false. Encode/bound before one consuming write; partial/missing output stays unknown, with no second report, automatic retry/rollback/rebase or later-refusal settlement. Old files and unrelated data remain untouched.

## Verification and later consumer boundary
Verify exact set/clear/absent/null/no-op/case/grammar/opaque unrelated-value preservation; private no-echo/digest vector/original patch/CAS/path/target; strict nested objects/duplicates/empty clear extras/caps/EOF/flag inventory; Busy and all four ordinary/selected current modes; actual atomic/readback and consuming-prefix faults; pure read-only operations with held stdin/Store ownership/declared-root aliases; unchanged old editor/file-credential/resolver/archive behavior. Retain actual synthetic CLI bytes and clean build/executable provenance without real key files or provider/tablet contact. Different source/current observations retain their actual attribution.

Both-host API/UI/private buffers, cross-lane unknown retention and any multi-step credential setup/removal flow require separate concrete consumer precode/review. This source change alone does not authorize atomic two-file setup, file discovery/migration or effective authentication.
