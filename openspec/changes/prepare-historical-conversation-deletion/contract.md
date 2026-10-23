# Proposed historical conversation deletion version1

UNIMPLEMENTED PRECODE. No source or native qualification follows from this packet.

## Route
`reader-buddy --conversation-operation inspect|prepare|apply|status --conversation-input -`
uses the existing explicit Config selector. Require raw literal dash; no input
files, arbitrary paths, filters, discovery or native lookup. Recognized conflicts
with api-key/model/simulate refuse before startup without echoing their values.
Ordinary clap syntax errors remain exit2 and may echo unexpected argv; accepted
request bodies and report errors never echo values. Preserve all legacy parsers.
Non-Linux returns fixed unsupported before stdin/Config/OS/Store access.

Linux input is one strict UTF8 JSON object plus EOF, <=16384 bytes. Reject duplicate,
unknown/missing keys, wrong object positions, trailing JSON, bad UTF8, unsupported
versions, noncanonical/nil UUIDs, noninteger bounds or invalid lowercase SHA256.
Parse and validate the whole request before Config/service/filesystem access.
inspect: {request_version:1,conversation:UUID}
prepare: {request_version:1,operation:UUID,conversation:UUID}
apply/status: {intent:INTENT}

## Existing-only custody and finite admission
Config is an explicit absolute safe existing bounded strict file. Bind exact path
bytes, exact file bytes and configured data/cache/credentials roots. Config sync
enabled refuses; missing/selected/shared/isolated modes are handled as follows:
absent legacy mode or explicit LocalOnly is admitted under its exact ordinary mode
lease; other modes refuse. Absence is never called an explicit saved LocalOnly.
Use only the already-owned store.lock, retaining its original OS handle through
output/failure. Validate held/named stable device/inode, Config bytes, actor,
CURRENT, ordinary generation and known owner headers before and after opening.
Never create a missing marker/lock/root or alter permissions. Refuse unknown or
selected generation format, any selected feature/selection/history metadata and
unsafe/symlink/reparse/hardlinked structural or payload entries.

Before Store recovery, while retaining that SAME lease, bound the entire current
ordinary generation conservatively: <=4096 commit-directory entries, <=8192 object-
directory entries, each manifest <=8MiB, each record object <=1MiB, all manifest
lengths combined <=8MiB, all record-object lengths combined <=32MiB and all object
lengths combined <=256MiB. Stage files count toward directory/byte limits and are
not read, removed or recovered as committed state. Root structure is exactly
format.json, commits, objects plus ignored bounded .stage-* entries; unknown entries
refuse. Count/check objects before content reads, reject foreign/unknown committed
object classification and all unavailable commits. Read admitted manifests first under the aggregate8MiB manifest budget to classify
record versus media references; before object contents, check all declared
lengths against held regular-file metadata and aggregate budgets. Existing recovery validates
record JSON/digests, manifest references and required media within those budgets;
this is full owned-store validation, NOT metadata-only inspection. No original
PDF/EPUB/notebook, native page, credential payload or remote object is accessed.
Existing known credentials/owner.json may be read solely to validate Store custody;
no credential filenames, resolver, secret values or provider is consulted.

## Inactive fixed unit
On Linux invoke ONLY /bin/systemctl with fixed argv:
`--no-pager --no-ask-password show reader-buddy.service --property=LoadState --property=ActiveState --property=SubState --property=MainPID`.
No shell, PATH lookup, configurable executable/unit or command text. Null stdin;
clear inherited environment, set LANG=C, LC_ALL=C, SYSTEMD_PAGER=cat and
SYSTEMD_COLORS=0. Bound stdout and stderr each4096bytes and wall time3seconds;
kill/reap the child on timeout/overflow, never emit its text. Missing executable,
nonzero exit, stderr, malformed/extra/duplicate/missing properties or unknown state
refuses unavailable. Exact LoadState=loaded, ActiveState=inactive, SubState=dead,
MainPID=0 is admitted. Other well-formed state refuses busy, not safe-by-inference.
Observe after strict request validation and before Store admission; repeat under
custody immediately before prepare/inspect output or first apply publication.
Status also requires fresh inactive observation/custody; unavailable is not absence.
The observation is not a durable service-state token. The Store lease supplies
writer exclusion if a cooperating runtime starts after observation. No service
mutation, D-Bus Buddy API, SSH or tablet operation is part of the producer.

## Target eligibility
Exactly one supported schema1 value root with matching conversation ID; at most
one live historical binding named by that root, also schema1 and belonging to the
same conversation. Reject foreign/missing/conflicted binding and extra live
bindings claiming the same conversation. Validate ordinary Ledger inspection and
all relevant retained records across Conversation, Source and ExportAssociation:
<=4096 envelopes/<=8MiB encoded metadata, supported shapes/namespaces/identities,
complete allocated chronology and no relevant current conflict. Reject ANY relevant
schema2/admitted-intent/settlement/export-attempt record, including retained records;
never promote historical source/binding facts to current native authority.
Current Turn outcomes must be completed/failed/canceled; other outcomes refuse.
Current Export associations must be completed; legacy failed/canceled lacks reliable
no-send qualification and refuses conservatively. Historical nonterminal revisions
of now-settled current records do not independently block deletion. Unresolved
current outcome facts refuse; source evidence remains retained and validated.
The prepared summary counts current turns, current source records and current
export associations. It never claims reclaimable bytes or complete native history.

## Intent and exact encoding
Closed INTENT fields in this serialization order: intent_version:1, operation,
conversation, config_path_sha256, config_bytes_sha256, roots_sha256, actor,
generation, mode_sha256, target_history_sha256, root, binding, summary,
intent_sha256. root is {revision,sha256}; binding is null or {id,revision,sha256};
summary is {turns,source_records,export_associations}, each integer0..4096.
Root/binding each represent the complete singleton original head and its canonical
Envelope SHA256. All UUIDs are canonical lowercase nonnil; digests are64lowerhex.
intent_sha256 is SHA256 of UTF8 domain `RMB-CONVERSATION-DELETE-V1\n` followed by
compact JSON of the preceding ordered fields, no trailing newline. Fields cannot
be omitted when null. The two synthetic digest-vectors.json cases freeze encoding.
roots_sha256 is SHA256 compact JSON array of exact configured path strings in
[data,cache,credentials] order. config_path_sha256 hashes exact absolute UTF8 path
bytes; non-UTF8 paths refuse. config_bytes_sha256 hashes exact original file bytes.
mode_sha256 is the existing current mode token digest, not a saved mode claim.
Do not reinterpret public input as a live token; acquire the matching ordinary
mode lease afresh. All derived operation/revision/transaction IDs must be distinct
from existing unrelated identities; any collision refuses without publication.
target_history_sha256 is SHA256 compact JSON array of ALL relevant retained
Envelope values sorted by (namespace,record_id,revision_id), excluding only this
operation's later deterministic receipt/tombstones during status reconciliation.
Namespace comparison is serialized kebab-case spelling. Envelope canonicalization
uses existing typed Envelope field order and sorted JSON object keys for payload;
parent UUID arrays are sorted lexically; semantic arrays such as acknowledgment
records retain their specified order. Hashes are preconditions, never permissions.

## Deterministic publication
For UUID derivation use UUIDv5/NAMESPACE_URL over UTF8
`urn:remarkable-buddies:conversation-cleanup:v1:{operation}:{role}`.
Roles: root-revision/root-operation, binding-revision/binding-operation,
receipt-revision/receipt-operation and transaction. Root/optional binding envelope:
existing format1/Conversation/schema1, original record ID, derived revision and
operation IDs, original singleton parent, original actor, tombstone, null payload,
empty media descriptors. Never tombstone any source/turn/export association.
Receipt record ID uses existing
`urn:remarkable-buddies:operation:v1:{operation}` UUIDv5 convention. Its value
payload is existing Record::Receipt with admitted_intent absent, acknowledgment
operation=original operation, conversation=target, records=[bindingID] or[],
applied_root_revision=derived root revision, binding=original bindingID ornull.
Receipt parents are empty. fingerprint is SHA256 compact JSON array
["prepared-conversation-delete-v1",intent_sha256]. Use one deterministic transaction
UUID and existing atomic LocalTransaction publication for exactly these2or3 records.
No media or coverage entries, no deletion/unlink or cleanup of retained files.

One Store mutex covers exact generation/actor/mode/target history/root/binding
revalidation, complete original-receipt absence and atomic publication. No gap may
admit an in-process append, bind/export, restore or changed selected history.
An existing exact original manifest/receipt is historical acknowledgment only,
not fresh permission. Reject ambiguous/partial/changed-content operation reuse,
foreign actor/generation/config/mode, stale or changed original target content.
Preserve existing Ledger::delete and all legacy operation fingerprints unchanged.

## Reports and outcomes
Closed report_version1 fields: report_version, operation, status,
runtime_unverified:true, local_only:true, physical_reclamation:false,
service_observation (inactive|unverified), possible_effect:boolean,
conversation (nullable UUID), intent (nullable INTENT), receipt (nullable object),
current_state (null|live-original|desired-tombstones|changed), summary (nullable).
Receipt fields: operation, transaction, root_revision, binding_revision(nullable).
No text/title/path/native identity/image/provider/credential/error-string output.
<=32768UTF8bytes including newline. Exit0 emits one complete report, including
refusals; exit1 is output/transport failure; do not append a second report after
partial output. Hold Store/mode custody through all bytes and failure.

Statuses: ready(inspect), prepared, acknowledged, unchanged(status without receipt
and exact original live state), unresolved(status without exact receipt but changed
or absent current state), invalid-input, unavailable, unsupported, busy, conflict,
unknown. Refusals have no intent/receipt/summary; original input conversation may
be included only after strict admission. possible_effect=false before dispatch;
true after publication attempt or acknowledged original receipt. Status without
receipt uses false but makes NO historical no-deletion claim. Current state is
separate from historical acknowledgment and can be changed after a valid receipt.

Prepare/inspect never publish. Apply first recognizes ONLY the exact original
manifest+receipt+deterministic envelopes, including retained originals matching
intent. Otherwise it revalidates original state and publishes once. Success
requires exact durable transaction/receipt readback; all errors after publication
attempt return unknown/possible_effect=true, no automatic write retry or rollback.
Explicit status of the SAME original intent observes exact receipt or unchanged/
unresolved current state, without writing. A matching root tombstone without exact
original receipt is unresolved, never acknowledgment. Exact historical receipt
may acknowledge even if current heads changed later; show current_state=changed.
Output loss never authorizes repeating with a fresh operation or re-preparing.
