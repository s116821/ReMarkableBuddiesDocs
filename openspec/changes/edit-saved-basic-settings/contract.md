# Basic-settings maintenance wire v1 (proposed, unimplemented)

## Fixed operations and limits
New fixed CLI `reader-buddy --basic-settings-operation inspect|prepare|apply|status`. Existing REMARKABLE_BUDDIES_CONFIG selects an explicit absolute config. There is no --config option. All runtime/other maintenance selectors are mutually exclusive, including existing configuration inspection. Inspect takes no input and MUST NOT read stdin; supplied basic input refuses before I/O. Prepare/apply/status require exact `--basic-settings-input -`, consume bounded UTF8 JSON plus EOF, and reject file-path input before reading it. Unknown/old CLI is unsupported before apply dispatch; never fallback to files, services or automatic retry.

Config input remains inclusive1048576 bytes. Mutation/receipt stdin and complete single-LF report each cap16384 bytes; encode fully before the one writer, never truncate or emit a second error report after a prefix. Host stderr cap8192/private child envelope24576/public response8192/request1024; preserve existing2/8/12/13/14s hierarchy, never increase shared deadlines. All requests/reports deny recursive unknown/duplicate fields, malformed UTF8, trailing JSON, unsupported versions, nil IDs and invalid lowercase64hex digests. All counts/lengths remain safe integers. Explicit-path admission is bounded using existing file safety checks.

## Fields and exact patch
BASIC_FIELDS has exactly three flat keys trigger_corner, log_level, debug_dump, each `{origin:default|declared|declared-null,value}` using delivered version1 origins/types/default-null semantics. Trigger values UR/UL/LR/LL; log values off/error/warn/info/debug/trace; debug value boolean. Declared means nonnull supported value; default/declared-null mean null. This is saved-only, never effective environment or service state.

CHANGES is a strict object containing one to three of those keys. Each entry is exactly `{action:"set",value:FIELD_TYPED_VALUE}` or `{action:"clear"}`. Set never accepts null, unknown enum, extra fields, coercion or control text. Clear removes only that declaration. Absent patch keys are unchanged. No empty patch, arbitrary key/path/model/credential/personalization/memory/sync field or whole Config is accepted.

## Private request/intent shapes
Inspect has no stdin body. Successful private inspect data is `{schema_version:1,base_sha256:HASH,config_path_sha256:HASH,current:BASIC_FIELDS}`.

Prepare stdin is exactly `{basic_version:1,operation:NONNIL_UUID,base_sha256:HASH,config_path_sha256:HASH,changes:CHANGES}`. Both original hashes come from this editor's explicit inspection, not a caller-selected general view. A changed base/path refuses Conflict with no write. Compute the changed raw document using the design's deterministic recipe; validate supported Config/value constraints and byte cap. Real change returns `{before:BASIC_FIELDS,after:BASIC_FIELDS,intent:INTENT}`. A logical no-op returns `{current:BASIC_FIELDS,base_sha256:HASH}` with no intent and no write.

INTENT exact ordered fields are `{basic_version:1,operation:UUID,base_sha256:HASH,target_sha256:HASH,config_path_sha256:HASH,changes:CHANGES}`. Base/target must differ. Base/target hashes are SHA256 of exact file bytes; path hash is SHA256 of UTF8 `urn:remarkable-buddies:basic-settings-path:v1:` followed by the exact explicit absolute UTF8 path. Refuse non-UTF8 selection. No raw path/Config, credential reference/text or store identity is returned. Packet is private conditional evidence, not a bearer grant or proof of applied runtime state.

Apply/status stdin is exactly `{intent:INTENT}`. The host uses the exact original packet, not renderer-supplied hashes/revised patches. Apply rechecks path/base, recomputes exact target and compares its hash, validates unchanged owned roots and full Config admission, then uses current existing-store/mode custody and the SAME conditional atomic writer. Final base compare and target publication share its mutex/lease; no check-then-unguarded-write. No initialize/repair/retarget/replay. Current target bytes do not authorize repeating apply; use status. Success reads exact target bytes/config back under custody before reporting.

Status only reads the original selected config (no Store/credential-root probe or writer). Supported validated current bytes equal to target_sha256 yield desired-file-observed. Any other valid bytes yield unresolved. Missing/invalid/future file or status transport failure cannot prove original nonpublication. Status cannot write, reprepare, refresh conditions or imply historical/native/runtime success.

## Exact report and phases
Top-level required keys are `{report_version:1,operation:OP,status:STATUS,outcome:OUTCOME,disk_readback_verified:BOOL,runtime_activation:ACTIVATION,data:DATA_OR_NULL}`. No extras. STATUS exactly ok, invalid-input, unsupported, unavailable, busy, conflict, failed. OP exact inspect/prepare/apply/status.

| Complete successful operation | outcome | disk_readback_verified | runtime_activation | data |
| -- | -- | -- | -- | -- |
| inspect | read-only | false | unverified | private inspect shape |
| prepare with change | prepared | false | unverified | before/after/intent |
| prepare no-op | no-change | false | unverified | current/base hash; no intent |
| apply with exact readback | verified | true | restart-required | `{target_sha256:HASH,current:BASIC_FIELDS}` |
| status matching full target | desired-file-observed | false | unverified | `{observed_sha256:HASH,current:BASIC_FIELDS}` |
| status nonmatching valid file | unresolved | false | unverified | same status data |

Non-ok has data=null, false readback and unverified activation. Inspect/status refusal has outcome read-only; prepare refusal is not-dispatched. Apply validation/admission/Busy/known prepublication conflict is not-dispatched. Once atomic publication might have happened, any error/readback failure becomes failed/unknown, never rollback. Invalid/partial/nonzero/cancelled output after possible host apply dispatch is unknown. A later invocation's not-dispatched/read-only refusal does not settle an original unknown attempt. Routine diagnostics are fixed sanitized messages; no raw errors, input, private hashes or text.

Desired-file-observed proves only the complete prepared target file is currently read on the original target. It does not prove the original operation published it or that the runtime reloaded it. No automatic apply retry follows any outcome. An explicit fresh edit may start a DISTINCT intent from a fresh successful observation, while retaining the prior unknown diagnostic; do not silently refresh/reuse its original reference/conditions.

## Host/public boundary and lifecycle
Future shared consumer precode must use the same browser/Electron method shapes: identity-only begin editor; opaque host reference plus CHANGES for Save; opaque original reference plus identity for explicit status. It must validate private producer shapes and reduce to BASIC_FIELDS, safe outcome and opaque reference; never return/persist hashes or INTENT. No public arbitrary operation/argv/path/environment/revision. Existing protected HTTP/main-frame IPC and fixed trusted wired transport remain mandatory. The new consumer API/body implementation waits for its concrete precode review.

One Save invokes at most one prepare and one apply; record original intent privately BEFORE possible apply dispatch. Cancel before apply is not-dispatched; cancel/identity change after possible dispatch preserves unknown original packet. Ready references invalidate before other maintenance/refresh/navigation and every new editor read, including identical connection/boot IDs. Preserve existing original receiver/queued cancellation and after-await final bridge guards. Register new operations for before-I/O forget invalidation. Unknown forget bytes remain unaffected by basic-settings reads/writes; no config operation may settle a memory removal.

Retain at most one active editor/apply and eight unresolved original diagnostic contexts in memory. Completed/refused records may retire, but never silently evict/replay an unresolved record to admit another write; capacity refuses with no dispatch. Status can observe an old exact target, and a new explicit fresh intent may proceed without relabelling historical unknown as rollback. No persistence, automatic retry or cross-restart recovery guarantee. Separate consumer design must specify exact navigation/cancel/refusal races using real HTTP/IPC guards.

## Acceptance
Actual local Store/config/CLI fixtures must prove only selected keys/origins change; explicit null and missing unrelated fields, model/URL/reference/path/identity sentinels and exact multiline UTF8 personalization survive without output. Logical no-op keeps original bytes. Stale original/base/path/target, nested duplicate/extra fields, wrong enums/types, cap/EOF and mixed flags refuse. Inspect/status MustNotRead or write/Store guards and actual open-stdin control remain distinct from static call-graph evidence.

Exercise ordinary and valid selected generations/current modes, current owner Busy, corrupt/future/admission refusal and zero initialization/repair/restore/mode changes. Inject before/after atomic publication/readback/output-prefix failures and retain unknown originals without replay. Pin actual prepare/apply/status reports and capture executable digest at capture. Consumer tests exact bytes, original-versus-later refusal, same-ID/after-await/navigation/cancel and unknown forget interoperability in both hosts; retain actual narrow/wide UI evidence in existing jobs. No tablet/provider/native result is implied.
