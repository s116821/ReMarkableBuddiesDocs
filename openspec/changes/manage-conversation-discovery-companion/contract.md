# Conversation-discovery companion contract (unimplemented precode)

## Authority and scope
[Canonical producer](../../specs/historical-conversation-inventory/spec.md) and [exact released producer contract](../archive/2026-10-23-inspect-historical-conversation-candidates/contract.md) are unchanged. This proposed consumer does not select a root, inspect deletion eligibility, mutate/configure/repair/recover a Store itself, stop/restart a service, make a native lookup or contact credentials/providers. The existing producer does read bounded owned payloads under ordinary existing-only recovery and fixed inactive-unit custody; do not describe discovery as metadata-only. Formats/modes/new namespaces it cannot admit remain refused, including any new feedback feature layout not qualified by that producer.

## Exact interfaces and fixed command
Optional public inspectConversations(request); POST /manager-conversation-inventory; IPC manager:inspectConversations; coordinator ConversationInventoryHost; private action/lane conversation-inventory; helper conversation_inventory_transport.py; raw key conversation_inventory_raw. Do not expose this raw action through general manager-host actions or renderer/preload/debug hooks.

Public request is exactly {connection_id:DIGEST,boot_id:UUID}, maximum256UTF8 encoded bytes. DIGEST is64lowercase hex; UUID is canonical lowercase hyphenated nonnil36-character UUID. Strict JSON/no duplicate members, no extra field/arity/array/coercion/BigInt/cycle or caller action/path/target/config/selector/filter/page/nonce/budget/cancel. Reject with static safe labels and no input echo.

Host-only helper request is exactly {connection_id,boot_id,budget_ms}, maximum256bytes; budget_ms is integer1..12000, never bool, inherited from the remaining original host deadline.

The sole fixed target command is:
`/usr/bin/env -i HOME=/home/root PATH=/opt/bin:/usr/bin:/bin REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json /opt/bin/reader-buddy --inspect-conversations`
Send zero stdin bytes, then EOF. No interpolation, fallback CLI/filesystem/admin query or version-threshold inference. Bound/discard stderr to8192bytes, never publish its text/exception.message/cause/traceback. Reuse existing Linux/win32 wired callbacks and before/after boot/session/host-key route verification unchanged. Local Windows support is separate from the producer's Linux-only target requirement. Nonzero exit2/126/127 with no admitted report maps unsupported, other unsuccessful/truncated/output-loss cases unavailable; a valid producer refusal at exit0 stays a reported refusal. No retry.

## Strict raw report
Require a single complete UTF8 JSON object of at most8192original bytes including exactly one terminalLF and no other literalLF. Whitespace counts; fatal UTF8/BOM/recursive duplicate-key/partial or multiple-frame errors reject. Do not coerce/round/truncate/sort/deduplicate. Validate the entire report before making a view.

Exactly13fields:
- report_version:1
- status:complete|too-large|unsupported|busy|unavailable|conflict
- scope:ordinary-current-root-candidates
- complete:boolean
- candidates:null|UUID-array
- candidate_count:null|integer0..16
- eligibility_evaluated:false
- mutation_authority:false
- native_authority:false
- runtime_unverified:true
- physical_reclamation:false
- local_only:true
- service_observation:inactive|unverified

Complete requires complete=true, candidate array0..16 of unique strictly ascending canonical nonnil UUID strings, count exactly matching array length and service_observation=inactive. Every refusal requires complete=false, null list/count and unverified observation. All fixed no-authority/privacy flags and scope must match in every status. Reject mismatched/null/count/bool/unsafe/nil/uppercase/future fields rather than normalizing them. Valid complete[]/0 is explicitly inspected-empty; a refusal is never an empty list. A positive safe-integer future report version is unsupported with no admitted data; invalid/noninteger/bool version syntax is unavailable; malformed current report is unavailable. No partial list or cached good snapshot fallback.

The raw internal response is exactly {contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,conversation_inventory_raw:{status:reported|unsupported|unavailable,stdout_base64:STRING_OR_NULL}}, cap16384encoded bytes. Validate strict envelope/observation/duplicates/base64/bounds first. Reported requires observed requested connection/boot and canonical base64 of the original report bytes; other raw statuses require null stdout. Fixed public errors never carry a raw field or parser object.

## Safe public result and protected surfaces
Exactly {contract_version:1,status:OBS_STATUS,observation:OBS_OR_NULL,conversation_inventory:{status:reported|unsupported|unavailable|busy,view:VIEW_OR_NULL}}, cap8192UTF8 bytes. Reported alone has observed matching request identity plus a fully validated view. All other wrapper statuses have unconfigured top status/null observation/null view. Wrapper Busy is shared-owner refusal before I/O, distinct from producer busy in a reported view.

VIEW has exactly11fields: status,complete,candidates,candidate_count,eligibility_evaluated,mutation_authority,native_authority,runtime_unverified,physical_reclamation,local_only,service_observation. Copy only from the fully validated report, preserving all combinations above; omit raw report_version/scope and every unknown field. No title/content/path/actor/config/intent/diagnostic/raw buffer enters public signals, preload, logs, telemetry or persistence. UUIDs are Buddy-owned root identifiers, not native page IDs. local_only denotes this nonremote read, not saved sync policy. Service inactivity is an observation within that snapshot, not continuing health or permission to resume/delete.

HTTP reuses exact loopback Host/origin/session/POST/no-query/content-type guards, strict bounded body reading and chunk wiping even on failure. Browser response cap8192 uses bounded stream/cancellation/reader release. IPC requires exactly one argument, authorized main frame/webContents and exact loaded fixed UI URL, isolation/sandbox and one added narrow preload method. Recheck token/epoch and current request/observed connection/boot before release/display. All inherited capabilities and arity/privacy restrictions stay closed.

## Eleven-owner custody and view lifetime
Use the same real MaintenanceIO in both factories for model/basic/forget/ordinary-export/research-settings/memory-settings/credential-reference/model-credential/source-cache-inventory/source-cache-cleanup/conversation-inventory. Acquire exact read token before beforeIO, cancellation, helper spawn or I/O. Busy changes no hooks/epoch/grants/originals/timers/cancel count. Use captured raw observer, never the externally-cancelling proxy that revokes its own operation.

Start one monotonic13000ms host deadline before hooks. Child budget is min12000/remaining; existing command stream ceiling8seconds and identity checks share the original child deadline, no budget renewal. Supervise never-resolving fake/IPC/child work too. Deadline/currentness checks surround async results and safe reduction. Old timeout/finally cancels only its own currently owned child/token/generation, never a successor. Clear mutable raw buffers/references on every exit; JS/IPC/SSH/OS immutable copies do not have a physical erasure guarantee. Release only the exact owned token after consuming validated output and final guard.

Admission invalidates idle grants/snapshots in all ten peers and they reciprocally invalidate discovery. Preserve every unknown/unresolved original operation, original private expiry/status availability and retained cleanup/export/forget/config/reference uncertainty; a new read must not settle/rebase/renew/retry them. A completed candidate list is no write grant. Preserve old90directed pairs and cover all110 in actual factories plus combined fixture.

Renderer known peer Busy checks precede private clearing. Accepted discovery synchronously clears all ten idle peer editor grants/views, actual private DOM/raw and cleanup selection/preview before the first pause/transport await, preserving unrelated query/Reader/Writer drafts and all original uncertainties. Existing28peer action boundaries plus separate forget receipt invalidate discovery immediately. A raced external Busy after local erasure does not restore text or change host Busy's no-side-effect rule.

## Observation quiescence, local Stop and UI
Reuse existing local observation pause/quiescence: advance observation generation, cancel scheduled poll locally, capture all in-flight/queued-before-host observation promises, wait for successful matching observed connection/boot results and existing connect cancellation. No adapter/global cancel is sent to create quiescence. Failure/timeout/abort/refusal or unresolved queued read is not a license to dispatch using a cached identity. Check request generation again after pause; Stop/expiry suppresses even later dispatch.

One renderer wait is bounded14000ms from invocation including quiescence. Local Stop immediately advances request epoch, clears view/timestamp/wait state and sends no public/global/helper cancellation or token release. Original host may remain Busy only until its original deadline. Old response/timer/finally cannot refill a stopped/newer view or erase a different editor. Disconnect, explicit state read, boot/cable change, pagehide/hidden, destruction and peer admission invalidate the view via existing semantics. No automatic re-observation/inspection/retry/poll/storage.

UI section Conversations, explicit Inspect conversation IDs and Stop waiting for conversation IDs. Initial/wait/stopped/unavailable/unsupported/busy/conflict/too-large labels are fixed and truthful. Display only count/sorted UUIDs and explicit snapshot time. Complete-empty says No current supported conversation IDs observed, not no history/no data. Copy explains owned persisted payloads were read, eligibility was not evaluated and native binding/runtime/reclaimable space remain unverified. No row button, auto-selection, deletion/prepare/confirm/resume/output/export/transfer or file-size total; later management needs a fresh separately admitted selected-target flow.

## Qualification boundaries
See acceptance.md and synthetic vectors.json. Precode checks test only text/vectors, never actual production/host/device behavior. Prior producer/manual/corpora keep their source/failure/executable attribution and are not silently rerun or called Manager qualification. Before delivery require exact current implementation/guard/helper/factory/shared-UI/source/development/retained Windows+Linux and current-main preservation evidence, independent review, own canonical/manual sync/archive and separate normal publication. No new library, jobs, resources/settings/auth retries, provider/model/SDK/RE or tablet operation follows.
