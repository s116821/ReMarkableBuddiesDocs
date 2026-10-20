# Proposed shared model-settings consumer contract

This is concrete unimplemented consumer precode against Manager8dfaf855 and
Docscc4cadf. It does not change the delivered producer contract or claim current
host support. Producer detail is fixed in the archived edit-saved-model-settings
contract; release equality alone never grants a write.

## Exact public boundary
Optional ManagerHost.modelSettings(request), fixed POST /manager-model-settings,
exact-arity main-frame IPC manager:modelSettings. Preserve current origin, Host,
session cookie, content-type, query, sender/frame/navigation and optional-capability
guards. No query/body transport path/argv/hash/UUID/private report is accepted.
Only this NEW request path permits at most16384UTF8bytes, including JSON escaping;
all existing path/request/output caps remain unchanged. Strict JSON objects, fatal
UTF8, duplicate/extra/version/type refusal and canonical bridge serialization apply.
IPC and host parser independently enforce the same scalar-string/byte/body bounds.

Requests are exactly:
- {action:'begin',connection_id,boot_id}
- {action:'save',connection_id,boot_id,reference,changes:CHANGES}
- {action:'status',connection_id,boot_id,reference}
- {action:'cancel',reference}
- {action:'retained'}

Identities use existing exact validators; references are fresh lowercase64hex host
opaque IDs, never a private digest reused as a bearer. CHANGES is nonempty, only
model/base_url, each exactly {action:'set',value:STRING} or {action:'clear'}.
STRING must be well-formed Unicode scalar text and nonblank under the PRODUCER's
Rust whitespace predicate; no trimming or rewriting. The whitespace set is
U+0009..000D,0020,0085,00A0,1680,2000..200A,2028,2029,202F,205F,3000; in particular
U+FEFF is not trimmed. Model <=256UTF8bytes; base_url <=2048UTF8bytes. Validate
exact field caps before serialization and complete request cap afterward. JSON
escaping can expand controls sixfold, so a basic1024-byte bridge must not be reused.
No URL parsing/scheme/userinfo/query/fragment/control/CRLF/trailing normalization,
provider validation, private endpoint probe or new global Config rule.

## Safe result and phase combinations
Exact outer {contract_version:1,status:OBSERVATION_STATUS,observation:SAMPLE|null,
model_settings:VIEW}, <=8192UTF8bytes. VIEW is exactly
{state,reference,current,report,retained}. current is null or exact FIELDS:
{model:FIELD,base_url:FIELD}, FIELD={origin:default|declared|declared-null,present:bool}.
Declared implies present:true; default/declared-null imply false. No raw strings,
lengths, hostnames, credential references, hashes, UUID, intent or raw errors appear
in output. report is null or only {operation,status,outcome,disk_readback_verified,
runtime_activation} from the producer's strict finite report table.

State is none|ready|invalidated|unsupported|unavailable|busy|capacity|not-dispatched|
no-change|verified|unknown|unresolved|desired-file-observed. Same ready/unknown and
invocation distinctions as basic, with explicitly MODEL-specific consistency:
- ready: reference, inspect/ok/read-only, exact2current fields.
- no-change: prepare/ok/no-change, current equals original projection, no apply.
- verified: apply/ok/verified, current equals prepared after, true/restart-required.
- desired-file-observed: status/ok/desired-file-observed, current equals prepared
  after, false/unverified; no historical publisher or runtime claim.
- unresolved: status/ok/unresolved with NULL current (producer data is null),
  false/unverified; original unknown is not a new edit grant.
- unknown: original reference and null current; no fabricated verified/readback.
- other refusal/local states cannot carry ready/current/verified authority.
Only a complete current identity-verified wire observation may carry outer observed/
sample. Host-memory retained/cancel/refusal uses unconfigured/null as appropriate.
Host-only retained returns none/null reference/current/report and no tablet I/O.
retained has <=8 unique exact {reference,connection_id,boot_id,state:unknown|unresolved}
records; never input text or apply packet. A status refusal is only invocation
failure and never resolves an original possibly published Save.

## Private hash/patch custody and one-shot Save
Begin reads fixed model inspect with no stdin, validates pure original base/path
hashes and presence projection, then creates a120000ms monotonic ready grant.
General/basic inspect cannot substitute. Save atomically claims same reference,
original target/boot/epoch and unexpired grant; duplicate claims cannot prepare or
apply twice. Generate private UUID. Prepare sends exactly original base/path and
snapshotted CHANGES. Recursive compact key-ordered UTF8 CHANGES under producer
urn:remarkable-buddies:model-settings-patch:v1: must match changes_sha256. Reject
lone surrogates; preserve exact decoded strings. Pin original independent vector
SHA2567b8b312e53ce731e251614648218ebf89f994b4d03b047e67278ae0b8ff2c226.

Strict prepare compares before to original presence, after to the finite patch's
presence transformation, original UUID/base/path/patch digests and new valid target
hash distinct from base. Full-file serialization/target truth remains producer-owned;
never derive it from hidden values. No-change must preserve original fields/base and
exact submitted patch digest, and dispatches no apply even if set text was already
saved. Untouched old Config values are not fetched or reconstructed by the host.

Before possible apply retain original exact hash-only prepare bytes, serialized
{intent} for status, integrity digests and before/after safe fields. Apply sends
EXACT {intent,changes} once, with original privately snapshotted patch. Validate
complete apply target/current/outcome/readback/activation before verified. Before
possible dispatch expiry/cancel/refusal is not-dispatched; after possible dispatch
missing/malformed/nonzero/late output remains unknown with the original hash-only
packet. No refresh/reprepare/automatic reapply/rollback/condition substitution.

Raw changes and serialized apply/base64 are transient Save-only data, not retained
record members, logs or diagnostic state. Drop request/patch/string references and
zero mutable owned buffers when their bounded send/Save lifetime ends; teardown
also covers prepare refusal/no-change, cancellation, deadline and exception paths.
Late callbacks cannot restore raw inputs or editor authority. Account explicitly
for HTTP/IPC/observer closures holding input until invocation completion; strip
safe identity/action/reference context for post-await validation rather than storing
whole Save requests. No claims of guaranteed JavaScript/IPC/OS memory erasure.

Status validates original reference/current verified target, sends ONLY original
{intent}, and never accepts or reconstructs changes. Exact target/hash/current match
may retire that diagnostic; nonmatch is unresolved/null current, later refusal
preserves prior unknown/unresolved. A same-target fresh Begin is a distinct edit,
not retry or implicit resolution. Terminal packets may retire; unresolved cannot
be evicted to admit a ninth model Save. Full host restart may lose recovery; no
persistence, restart guarantee or automatic status loop. Model8record bound is
separate from existing bounded basic/forget records, while actual I/O is shared.

## Shared I/O, budgets and late Stop
The SAME MaintenanceIO covers basic/model Begin, whole Save, remote original status
and direct forget prepare/confirm/receipt. Acquire before any hook/await; busy does
no raw run/cancel/invalidation. Owned model I/O invalidates basic/forget ready before
remote work; owned basic/forget and external wrapped observation/maintenance/raw run/
real navigation/global cancel invalidate model ready/pending generations. Preserve
all possibly dispatched originals. Host-local retained/forget status bypass I/O and
cannot invalidate or cancel a newer owner. Raw observer receiver stays original.
Construct all three coordinators around the SAME original observer and shared I/O.
The direct beforeIO hooks are explicit: model invalidates basic+forget, basic
invalidates model+forget, forget invalidates model+basic; the external wrapper
invalidates all three. Hooks never recursively call another wrapped observer.
Each targeted cancel checks exact lane/reference/token; old completions release
only their own token. All THREE coordinator directions must be tested.

Keep existing2/8/12/13/14s hierarchy. Save owns ONE13s total deadline, not one per
phase. Private budget_ms is integer1..12000, min(12000,floor(total remaining)); prepare
is also capped by original ready remaining. Supervisor timer clamps to it. Python
starts inherited monotonic deadline before config/auth; channel timeouts are
min(2s,remaining), command min(8s,remaining), identity/readback check remaining.
Original ready expiry is rechecked after prepare and before possible apply. Total
time is checked after every awaited reply, after parse and before final settlement,
even if timer callback has not run. Late possible apply stays unknown.
Host/editor epoch checks after await and final HTTP/IPC prevent late ready/verified
publication. Controller stop captures generation/reference/original and guards every
post-await mutation. Stopping host-only retained reads stays local; global queued
cancel applies only to a pending Begin without a published reference.

## Renderer private-text behavior
Two rows show Model / Endpoint and origin/presence only. Each offers Keep unchanged
(default), Replace, Remove override. Replace enables a plain-text multiline draft;
never prefill undisclosed old text. Treat text as text, never HTML/URL/link/network
input. Explain that replacement may contain sensitive data and saved changes need
restart; an effective endpoint/model/provider is unverified. No provider/test/restart
button, automatic credential manager discovery or value-reveal of saved text.
No-change Save remains valid because old opaque strings cannot be compared in UI.

Controller raw drafts are separate from safe status/diagnostic state, never app
storage/URL/history/logging/telemetry. Disable autocomplete/autocorrect/spellcheck/
autocapitalization; do not rely on browser/extension memory erasure. Save snapshots
exact field actions/strings then clears raw draft references and DOM values BEFORE
its first await. Failure/busy/capacity/verified/no-change never repopulates them.
Clear on Begin replacement, local refresh/navigation/disconnect/other-panel remote
maintenance, Stop, component destroy and120s local draft timer without edit renewal.
Host invalidation is immediate even if another client's UI cannot observe it until
its next response; no new push/polling channel. A late response cannot refill inputs.

Preserve pasted CRLF/trailing/control/Unicode exactly: prevent default paste, use
only that user event's plain clipboard text (no asynchronous clipboard permission),
keep scalar raw controller text and map textarea normalized LF selection offsets
back to raw CRLF boundaries when splicing. Display normalization is not submitted
source. Track beforeinput selection/input generation; ordinary edits preserve raw
unchanged spans and insert exact event text/new LF for a deliberate line break.
Reconcile composition/input against the same normalized/raw index map; if an edit
cannot be represented without silently losing existing raw characters, refuse Save
and ask for a fresh replacement rather than guessing. Test paste and later edits,
including leading/trailing CRLF, tabs, non-BMP text and the U+FEFF/U+0085 predicates.
No hidden .trim(), textarea/form roundtrip, URI parser or generic sanitization may
rewrite the raw snapshot. Routine screenshots use cleared synthetic drafts; the
application itself introduces no input-capture/screenshot/debug logging.

## Fixed transport, caps and public equivalents
Fixed prefix only: /usr/bin/env -i HOME=/home/root PATH=/opt/bin:/usr/bin:/bin
REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json
/opt/bin/reader-buddy --model-settings-operation OP. OP chosen internally as inspect,
prepare/apply for Save, status for original Check desired file. Inspect has no stdin
flag/data; others append --model-settings-input - and private bounded EOF JSON.
Never place values in argv/env, a path or error output. No file/service fallback.
Use existing POSIX/Windows identity-verified callbacks and known wired profile.

Config1048576, producer stdin/report16384(including LF/whitespace), stderr8192,
private request/child output envelope24576, public model request16384/output8192.
Base64 of a16384-byte private input plus fixed identity/budget/selector fits24576;
check inclusive complete bounds before spawning/parsing/forwarding. Other actions'
limits and existing release/version/dependency/job graph remain unchanged. Strict
private report shape refuses any old/new text/extra even in malformed producer
stdout before it reaches a public projection. Drain bounded stderr without echo.
Old/unsupported selectors refuse capability; optional bridge absence is supported.
Manual producer commands follow the archived contract with private stdin, fixed
config and no Buddy admin API; do not print/reuse example real replacement values.

## Evidence and lifecycle required before delivery
Verify original32Windows reports/60stdin+stdout hashes from90529byte corpus
SHA2561445676ff01ad2cfebbd94ed6a33845fccf63b5630848419f4fd15584408fcfe,
capturec785afe044fcd00d386ce9030cb06916245ba2c4/executable
2a624cfd80b87a945e3b0a8a7560100a0d0c92c3d4d62c386959ac57113b8fa6.
All reports cross actual typed model parser/coordinator/controller as applicable;
original status-after-verified is not induced transport loss. Label surrounding
synthetic replies/loss/faults separately and never replay producer execution.
Both actual protected HTTP and main-frame IPC hosts cover public abuse/arity/frame/
expiry/navigation, exact paste/edit/private-buffer cleanup, absent raw data from
retained/status/safe UI, no auto retry/status,8record bound, old stop/new Save and
all basic/model/forget ownership directions with original receipt bytes preserved.
Keep all original basic/general corpora and existing capability controls. Run normal
both OS source/development/retained browser/Electron checks with no local package
rebuild, inspect390/1280 captures, full implementation review, exact own canonical
sync/archive/final composition and normal linked Docs-first delivery. MainCI/actual
trees/tag/provenance and broad/native acceptance remain separately observed.
