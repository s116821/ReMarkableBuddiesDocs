# Ordinary additive restore companion — concrete precode candidate

Status: accepted contract implemented in source; independent source review and retained-platform qualification remain pending. This contract consumes the unchanged [ordinary restore producer](https://github.com/s116821/ReMarkableBuddies/blob/68e42968b4c58b6f8ed1102078d78b40fad33ffc/src/restore_maintenance.rs) and [live ordinary-owned-restore specification](https://github.com/s116821/ReMarkableBuddiesDocs/blob/380229ec0f1db067733be2d21f0a00812d662761/openspec/specs/ordinary-owned-restore/spec.md). Exact source hashes and evidence limits are in source-proof.json. The source-selection exception below is specified explicitly; historical archives remain unchanged. No producer/device/provider execution follows from this design.

## Outcome and scope

Shared browser/Electron flow: explicitly enter one archive already on the tablet; prepare an additive restore into its existing ordinary local Store; show source/target impact; separately confirm once; explicitly check the original desired state after uncertainty. Source archives include private Buddy configuration/media; portable configuration is staged inactive, never activated. No transfer, cloud inspection, clean/replacement initialization, selected/shared/isolated/generation4 restore, native-page restoration, mode switch, service operation, writer replacement or recovery shortcut. These remain unfinished roadmap requirements.

## Closed public DTOs

Optional ManagerHost.ordinaryRestore(request); protected POST /manager-ordinary-restore; main-frame IPC manager:ordinaryRestore; private action ordinary-restore; helper ordinary_restore_transport.py; raw key ordinary_restore_raw; host OrdinaryRestoreHost. No raw/debug/general management API.

DIGEST is64lowercasehex; UUID is canonical lowercase nonnil hyphenated UUID. Exact objects, recursive duplicate refusal at JSON boundaries, no coercion/prototype/positional-array/extra keys. HTTP/IPC arity, authorized origin/session/frame/content-type/no-query and chunk-wiping rules remain unchanged.

Requests:
- Prepare: {action:'prepare',connection_id:DIGEST,boot_id:UUID,invocation:UUID,source:PATH}; complete encoded UTF8 object<=16384bytes.
- Confirm/Status/Cancel: {action:'confirm'|'status'|'cancel',connection_id:DIGEST,boot_id:UUID,invocation:UUID,reference:DIGEST}; complete encoded object<=512bytes. Cancel includes captured identity and the invocation being canceled, not a newly minted action invocation.
- Retained: {action:'retained'}, host-memory only, no target/helper access.

PATH is a well-formed Unicode scalar string of1..4096UTF8bytes, absolute POSIX, non-root, no NUL, no component exactly '.' or '..', no trailing slash. Do not trim, resolve, collapse separators, expand '~', substitute environment or change spelling. Host scalar/lexical validation is a proposed conservative input subset; producer remains authority for canonical filesystem safe-root/symlink/overlap/archive/Store checks. Path is an untrusted draft, never an authorization token. Request and full subsequent private packet/envelope bounds must all fit; reject rather than normalize/truncate.

Each executing Prepare/Confirm/Status uses a fresh invocation UUID recorded in that reference's32entry bounded ledger. Cancel instead names an existing or fenced prospective executing invocation; it does not allocate an unrelated UUID or dispatch a new producer action. Repeated Cancel is idempotent for that exact tuple and cannot consume another owner or target another invocation; reference is fresh random256bit host token, unrelated to producer operation/target generation. Initial Prepare has no reference; local Stop without a captured reference detaches UI only. The host operation UUID is separately minted after ownership admission. No renderer field accepts Config path, operation, intent, hash, actor/mode/base/target generation or budget. Confirm/Status/Cancel never accept source.

Result<=8192UTF8bytes, exactly:
{contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,ordinary_restore:VIEW}.
VIEW exactly {state,reference,preview,inspection,report,apply_outcome,retained}.
- reference is null for retained/newly refused Prepare; ready mints a reference. Other actions echo only their requested reference. It confers no authority after custody loss/expiry.
- SUMMARY exactly {manifests:COUNT,objects:COUNT,complete_media:BOOLEAN,configuration_included:BOOLEAN}; COUNT safe integer0..4096; no format field invented.
- PREVIEW exactly {source:SUMMARY,target:SUMMARY,additional_manifests:COUNT,additive:true,configuration_applied:false}. Only ready carries preview. additional_manifests<=source.manifests and<=target.manifests; source/target configuration_included equal. No assumption source.complete_media equals target.complete_media, or target.objects equals source.objects.
- inspection is SUMMARY only for restored/desired-generation-observed; otherwise null. It equals the complete original target SUMMARY, field by field.
- report is null without fully admitted current raw output; otherwise exactly {operation,status,outcome,disk_readback_verified,runtime_activation:'unverified'}. No report_version/raw data/intent/path/hash/UUID/diagnostic forwarded.
- apply_outcome is null before possible Apply; otherwise not-dispatched|not-activated|unknown|restored. It records the admitted original Apply evidence, not the last Status outcome. Desired-generation observation preserves unknown/not-activated rather than upgrading it to restored.
- retained<=8unique rows, each exactly {reference,connection_id,boot_id,state,apply_outcome,status_available}. state is unknown|not-activated|unresolved; apply_outcome is unknown|not-activated and remains fixed from admitted Apply evidence. status_available reflects retained original bytes/deadline/ledger capacity, not device health. Expired safe rows remain capacity-conserving until host lifetime ends; never silently evict/reissue an original.

Closed action/state relation:
| Action | States | Binding |
| -- | -- | -- |
| retained | none | unconfigured/null observation/reference/preview/inspection/report/apply_outcome; metadata rows only |
| prepare | ready,invalidated,capacity,busy,unsupported,unavailable | ready observed matching identity + prepared report + preview, new reference, null apply_outcome; other states null reference/preview/inspection/apply_outcome |
| confirm | restored,not-dispatched,not-activated,unknown,capacity,busy,unavailable | requested reference; no preview; restored has Apply restored/readback/inspection and no selected retained row; not-activated/unknown have same-identity selected row; known pre-dispatch local refusal has report null |
| status | desired-generation-observed,unresolved,capacity,busy,unsupported,unavailable | requested original reference; original apply_outcome never renewed/reclassified; desired carries exact original inspection and no selected retained row; unresolved has Status unresolved report and preceding original row; refusal/loss preserves preceding row |
| cancel | invalidated,not-dispatched,not-activated,unknown,unresolved,unavailable | requested identity/reference/invocation only; report/preview/inspection null; retained state and original Apply evidence survive where present |

Every report requires observed identity exactly matching captured request; local-only refusal is unconfigured/null report, never an observed success. Producer busy is an observed refusal with a report, unlike local ownership Busy. Cross-check action+state+report phase/outcome/readback, reference, apply_outcome, selected row identity and nullability independently at the public parser. Retained lists may contain unrelated originals from other identities; only selected row must match this request. Capacity/Busy cannot create speculation, evict rows, change deadlines or return a new ready reference. A fully parsed Apply refusal/not-dispatched consumes ready and drops its private grant; it never authorizes another Apply. A pre-launch shared-owner Busy preserves the original ready grant privately without renewing it.

## Exact private wire and custody

Private request exactly {connection_id,boot_id,selector,input_base64,budget_ms}<=24576encoded bytes. selector prepare|apply|status; budget_ms integer1..12000, clamped to remaining original13second action and grant/original deadline. Decoded canonical base64<=16384bytes strict UTF8 JSON, EOF:
- Prepare: {restore_version:1,operation:HOST_UUID,source:EXACT_PATH}.
- Apply and Status: {source:EXACT_ORIGINAL_PATH,intent:EXACT_ORIGINAL_INTENT}.

Command is fixed except closed selector:
/usr/bin/env -i HOME=/home/root PATH=/opt/bin:/usr/bin:/bin REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json /opt/bin/reader-buddy --restore-operation SELECTOR --restore-input -

Path is solely in bounded private stdin, never shell argv/env/URL/log/error/safe response. Existing wired trust/USB identity callbacks and exact boot before/after command remain.8second stream/12second child/13second host/14second renderer bounds remain; no inflation for larger archives. stdout16384bytes including one terminalLF; discarded stderr8192. Successful exit still needs full strict admission; exit2/126/127 without admitted report unsupported, other missing/lost report unavailable. After possible Apply, any missing/late/malformed/stale failure is unknown regardless of adapter label. No retry/fallback.

Private response exactly {contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,ordinary_restore_raw:{status:'reported'|'unsupported'|'unavailable',stdout_base64:STRING_OR_NULL}}<=24576bytes. Reported requires observed matching identity and canonical base64 of original bytes; other raw status has null stdout. No blanket cap increase for old capabilities.

Seven raw fields exactly: {report_version:1,operation,status,outcome,disk_readback_verified,runtime_activation:'unverified',data}. No BOM, malformed UTF8, recursive duplicate, trailing/multiple JSON, partial/multipleLF, unsupported keys or unsafe numeric shapes. Exactly one terminalLF, no other literalLF. Future positive safe report version is unsupported before Apply and uncertain after possible Apply; malformed reports unavailable before Apply and uncertain afterward.

INTENT has exactly fourteen ordered fields:
{restore_version:1,operation:UUID,config_path_sha256:DIGEST,config_sha256:DIGEST,source_path_sha256:DIGEST,archive_sha256:DIGEST,actor:UUID,mode_sha256:DIGEST,base_generation:UUID,base_history_sha256:DIGEST,target_generation:UUID,target_history_sha256:DIGEST,staged_configuration_sha256:DIGEST_OR_NULL,complete_media:BOOLEAN}.
All UUIDs nonnil; base!=target. No self-digest field exists. Prepare validates operation equals host operation; Config path SHA256 of UTF8 'urn:remarkable-buddies:ordinary-restore-config-path:v1:' plus exact fixed Config path; source path SHA256 of UTF8 'urn:remarkable-buddies:ordinary-restore-source-path:v1:' plus exact unnormalized PATH. These are distinct domains, neither bare-path hash nor export domains. complete_media equals preview.target.complete_media; staged_configuration_sha256 null iff both summaries configuration_included=false. Full original target SUMMARY is retained for later inspection equality.

config_sha256/archive_sha256/mode/base/target history are opaque valid producer-derived original conditions; Manager does not read files or reconstruct Store history to recalculate them. Producer revalidates raw config/archive bytes, same-mutex Store/current-mode custody, complete union/history/object integrity and exact target generation. Host verifies original report/input integrity and domain/context linkage independently; this does not authenticate arbitrary forged producer filesystem contents. Hashes/UUIDs do not establish physical tablet identity.

Before ready, serialize and bound both identical original Apply/Status packets and each envelope. Retain original strict prepared bytes, their SHA256, exact original packet bytes and SHA256, captured operation/identity/path/domain hashes, preview/target summary and fixed grant deadline. Confirm/Status rehash raw bytes and packet, strict-reparse original report against immutable captured context, revalidate all fourteen fields and target summary, and verify packet equals originally admitted source+intent; never synthesize from public DTOs/current state or silently replace a digest. Keep only bounded host-memory custody; wipe mutable temporary input/raw/chunk/base64 buffers on every exit. Immutable JS/IPC/SSH copies have no physical-erasure guarantee.

Closed raw matrix (all other tuples reject):
| selector | status/outcome | readback | data |
| -- | -- | -- | -- |
| prepare | ok/prepared | false | {preview:PREVIEW,intent:INTENT} |
| apply | ok/restored | true | {inspection:ORIGINAL_TARGET_SUMMARY,configuration_applied:false} |
| status | ok/desired-generation-observed | false | {inspection:ORIGINAL_TARGET_SUMMARY,configuration_applied:false} |
| status | ok/unresolved | false | null |
| any | invalid-input|unavailable|unsupported|busy|conflict|failed / not-dispatched | false | null |
| apply | failed/not-activated | false | null |
| apply | failed/unknown | false | null |

Status not-dispatched concerns only this read-only invocation and cannot settle earlier Apply. not-activated proves no CURRENT attempt by original Apply but staging may exist; retain that provenance/original, no automatic stage cleanup/reuse/reapply. Unknown includes publication attempt and output-loss uncertainty; no rollback claim. Desired-generation observation is exact intended current closure only, never a historical receipt/publisher proof/runtime activation. A restored reply proves the original Apply's exact disk readback, not running service readiness.

## State progression, cancellation and lifetime

Acquire thirteenth shared MaintenanceIO owner before hooks/invalidation/cancel/helper/I/O; failed Busy leaves all host state untouched. Capture raw observer, not cancelling proxy. Invalidate twelve idle peers reciprocally, retaining their uncertain originals/deadlines. All prior132directed relationships remain; total13*12=156. Re-enumerate actual incoming/outgoing UI boundaries against refreshed eventual base rather than hard-code proposed34/12 as fact.

Prepare mints operation/reference only after admission, validates current wired observation and calls producer once. At most one ready grant120000ms from accepted fresh prepare, no renewal. A genuinely new deliberate Prepare is allowed when the shared owner is free, any previous active action has settled under its existing lifetime rules, and fewer than8retained original rows exist. Allocate a new operation/reference even for the same target or a newly captured device identity. Preserve all older originals' exact bytes/hashes, identity, apply_outcome, deadlines, invocation ledgers and safe rows unchanged. This is a new restore, never refresh/retry/re-identification of an older grant. Expired custody metadata consumes its one existing row slot, not the entire capacity. Eight occupied slots refuse capacity without eviction. Earlier uncertain outcomes remain visible beside the new deliberate preview; no automatic confirmation.

Confirm consumes exact ready once; rechecks expiry/context/custody before possible dispatch. Arm one1800000ms original deadline and retain exact original before invoking Apply. Create no speculative renderer row until dispatch admission; if speculation is necessary for transport uncertainty, retire only its newly introduced row after fully parsed positive pre-dispatch Busy/capacity and no selected host row, preserving genuine originals. never renew ready on refusal. Known pre-launch failure=not-dispatched; after possible launch, loss/timeout/cancel/stale/malformed=unknown with original. Accepted not-dispatched Apply drops only that idle grant/original; not-activated/unknown retain original and its evidence; restored retires private custody after constructing safe result.

Status takes only retained opaque original/identity plus fresh invocation, reuses exact original bytes, never Prepare/Apply/path refresh. Unresolved changes current safe state while preserving apply_outcome. Desired observes current state then retires private custody, explicitly retaining historical apply_outcome in final result. Refusal/output loss keeps preceding row/deadline. Expiry wipes private bytes once and marks status_available=false; no recovery from public tokens, renderer reload, process restart or a new source draft. At most8originals/32executing-invocation ledger entries per reference. Later new restores may make an older desired closure no longer current; old Status then reports unresolved current-state evidence, never rollback or historical publisher proof. New admission must not alter an old original or renew its custody. No automatic polling of original status.

Cancel exactly binds original reference+captured connection/boot+the executing invocation being canceled. Ready cancellation targets the Prepare creator invocation; active Confirm/Status cancellation targets that active invocation. No unrelated new cancellation UUID can match or revoke it. An old cancel/finally/timer cannot kill/release a successor on same reference. Fence cancel-before-request in bounded ledger; duplicates do not dispatch. Idle ready cancel only with its creator invocation; active Apply cancellation cannot roll back and preserves possible outcome. Initial Prepare Stop without reference detaches local wait; host stays bounded Busy until finish. Recheck token/epoch/identity/deadline around every await, parse/reduction and surface return; cleanup owns only current child/token. No globalcancel to quiesce queued observations.

## Shared UI and source erasure

Label: Restore an archive already on this tablet. A blank protected source draft is explicit; no automatic path choice, directory scan, picker or registry. Show supported existing ordinary local Store and additive policy; disclose complete/omitted media, source/target manifest/object counts, additional manifests and inactive staged configuration. No native readiness/backup-transfer claim.

Check known peer Busy before clearing. On admitted Prepare, capture source into one temporary immutable value, synchronously clear signal draft AND actual textarea.value, then clear all twelve idle peer views/private DOM/grants before first observation/transport await; retain unrelated Reader/Writer/query drafts and all uncertain originals. Erase source/DOM on Stop, peer maintenance, reconnect/disconnect/boot change, reread, pagehide including bfcache, destroy, expiry and failed/rejected admitted Prepare. No localStorage/sessionStorage/disk/cache/telemetry/console/raw-error path persistence. A known local peer Busy refusal before admission preserves the existing draft/DOM under the established Busy rule; other submitted invalid drafts clear with a static local error. Failed admitted submission does not repopulate source; deliberate retry requires new input and original custody policy.

Preview renders no source path. Confirm is a separate deliberate button, never default form/Enter/autorefresh. Status is an explicit Check original desired state action, no automatic Apply/reprepare. Distinct labels cover staged but not activated, outcome unknown, desired state observed/historical outcome unproven and disk restore read back/runtime unverified. Safe retained discovery on reload is host-memory only and performs no remote status call. Both host adapters share this exact UI/controller/protocol, with manual fixed stdin equivalent and the same warnings/bounds.

## Delivery gates

Before implementation: verify current public source revisions and related in-flight work, include this candidate in one paired central OpenSpec change, explicitly modify live ordinary-owned-restore to allow only this untrusted Prepare path while preserving the historical archive, add the new consumer capability, obtain independent contract/vector review. No implementation-ready/merged-base claim yet.

Then source/private/helper/public/controller/owner/HTTP+IPC/UI tests, literal vectors independent of parser, full156directions preserving132, enumerated erasure/Busy/DOM lifetime/quiescence and once-only original behavior; retained Linux/Windows browser/Electron qualification; own canonical sync/parity/archive in same pair; independent review and normal coordinated delivery. No SemVer source constant; component tags remain authority; Docs is validation-only.
