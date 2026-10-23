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
record JSON/digests, manifest references and required media within the cumulative budgets below;
this is full owned-store validation, NOT metadata-only inspection. No original
PDF/EPUB/notebook, native page, credential payload or remote object is accessed.
Existing known credentials/owner.json may be read solely to validate Store custody;
no credential filenames, resolver, secret values or provider is consulted.

## Cumulative content and reference work
Unique disk lengths are NOT a cumulative read-work bound. This NEW admission must
use a shared per-operation recovery budget, leaving legacy callers unchanged.
Cap all manifest/object content reads at512MiB cumulative and all reference visits
at65536 cumulative. Charge BEFORE every read/hash/deserialize reread and before
every manifest/object/parent edge visit, including preflight, repeated shared-media
references, second record reads, retrying dependency passes and original-receipt
verification. A read must be limited to its reserved byte allowance (including any
EOF sentinel); growing files cannot consume unreserved bytes. Overflow or exhausted
budget refuses before the next read/visit. No resetting the budget per manifest,
object, pass or receipt branch. No fallback to unbudgeted recover/Source::open.
Verified reuse is allowed only inside this admission for the same validated object
identity/reference under retained custody; charge its verification once and every
reuse reference visit. No reusable cache or changed legacy verification semantics.

## Publication and reconciliation headroom
The caps above remain absolute for shared safe admission, including original status.
Before returning a prepared intent or attempting its first publication, compute the
exact deterministic2or3 envelope bytes R and manifest bytes M. Reserve conservatively
2 commit entries, N+1 object entries (N=2or3), 2*M manifest-directory bytes and2*R
object-directory bytes, charging2*R also as record-directory bytes. Include the
actual encoded
N-envelope union in the4096-envelope/8MiB target-history cap, including JSON array
separators when applicable. Existing stages count first; do not erase them to fit.
The reservation covers final files AND a single interrupted atomic-write staging
file at each publication phase, even though the normal writer is sequential.
If any prospective final or partial-publication inventory exceeds a cap, refuse
BEFORE preparing/dispatching. inspect does not reserve a nonce-specific transaction
and grants no guarantee that a subsequent prepare will fit.

Also budget the prospective bounded recovery/receipt-validation schedule with the
new deterministic manifest/envelopes included. Use the same deterministic traversal
and charging rules as actual admission, accounting for repeated dependency work;
reserve its cumulative bytes/visits BEFORE publication, or refuse before dispatch.
This must keep original-intent reconciliation admissible after this operation's
own final/partial files, without increasing or bypassing any global cap. Later
unrelated growth can still exceed a cap and yield unavailable, never false absence.

For apply/status with an original valid intent, shared admission may recognize its
exact deterministic object hashes/lengths as known uncommitted objects when the
manifest is absent. Bound and verify those bytes within the SAME read/work budget;
all other unclassified nonstage objects still refuse. Bounded .stage-* files remain
unread/untouched and consume reserved inventory bytes/entries. Exact original
partial objects without a complete receipt yield unresolved/possible_effect=true,
current_state=live-original or changed as observed; apply MUST NOT publish again.
No partial object/stage is cleaned, adopted as a receipt or used to relax a cap.
This is a single original publication attempt, not unlimited retry headroom.

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

## Fresh target eligibility (inspect/prepare and FIRST publication only)
Exactly one supported schema1 value root with matching conversation ID; at most
one live historical binding named by that root, also schema1 and belonging to the
same conversation. Reject foreign/missing/conflicted binding and extra live
bindings claiming the same conversation. Validate ordinary Ledger inspection and
all relevant retained records across Conversation, Source and ExportAssociation:
<=4096 envelopes/<=8MiB encoded metadata, supported shapes/namespaces/identities,
complete allocated chronology and no relevant current conflict. Reject ANY relevant
schema2/admitted-intent/settlement/export-attempt record, including retained records;
never promote historical source/binding facts to current native authority.
For current turns, group by the exact persisted exchange UUID, without title/text
matching. Require each exchange to have exactly one current User turn; that turn
may be Interpreted only when exactly one later-sequence current Assistant turn in
the SAME exchange is Completed with valid existing completion evidence, or Failed/
Canceled with valid existing outcome facts. User Failed/Canceled is admitted only
with zero assistant or one later terminal assistant. Assistant-only exchanges,
multiple current users/assistants, invalid role/sequence, missing terminal proof,
or any Prepared/Generated/ReconcileRequired turn refuse. A user's Interpreted
outcome is preserved unchanged; it never has to become Completed.
For Failed/Canceled terminal turns, require exactly one valid schema1 matching-
terminal OutcomeFact in the SAME
committed manifest as that current turn revision (same conversation/turn/outcome),
with no contradictory co-transaction fact. That is the applicable terminal proof;
facts have no sequence field and no timestamp is used to choose one. Older facts
may coexist only when their manifests contain an ancestor revision of that same
turn and validated ancestry/transition leads to the admitted current terminal
state under existing transition rules. Missing/ambiguous manifest membership,
contradictory terminal proofs or unassignable facts refuse. Require the terminal
assistant's mode to match its sole user request. No clock selects a winner.
Interpreted+Completed uses completion evidence on the assistant,
not an invented completion fact on the user. Empty conversations are eligible.
Current Export associations must be completed; legacy failed/canceled lacks reliable
no-send qualification and refuses conservatively. Historical nonterminal revisions
of now-settled current records do not independently block deletion. Immutable old
OutcomeFact records are historical; determine applicable current settlement by
validated turn revision ancestry/transition, not merely that a fact remains a head.
A contradictory, orphan or causally unassignable settlement fact refuses. No source
evidence is deleted or promoted to live authority.
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
Envelope values sorted by (namespace,record_id,revision_id) at fresh preparation.
It is mandatory exact revalidation before FIRST publication, not a requirement
that later history equal the old snapshot for historical receipt acknowledgment.
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
foreign actor/generation/config/mode. Stale or changed original target content
refuses FIRST publication; the historical receipt branch below has separate rules.
Preserve existing Ledger::delete and all legacy operation fingerprints unchanged.

## Branch order and historical receipt recognition
After strict input and SHARED safe service/Config/ownership/ordinary-mode/budget
admission, apply/status FIRST look for the exact original deterministic transaction
and receipt. This branch does NOT require a live root, settled current exchanges,
fresh whole-target eligibility, or current history equality with the old digest.
Verify exact manifest membership and bytes, derived identities, receipt payload/
fingerprint, and retained original root/optional binding envelope digests/identities
and expected parent relationships. The receipt fingerprint binds the complete
original intent, including its original target-history digest. Do not reconstruct
that old history by hashing arbitrary later retained revisions. Later target schema,
heads or settlement changes do not invalidate an otherwise exact original receipt
when shared storage is still safely readable within bounds.

Assess current state separately using only current root/binding head identity:
exact original live heads=live-original; exactly the derived original tombstones
and matching original binding state=desired-tombstones; all other/absent/conflicted
heads=changed. Historical acknowledgment may therefore accompany changed state;
no write or resurrection follows. If no exact receipt exists, status is read-only
and never invokes fresh-live Ledger inspection as a condition of returning an
unresolved observation. First-publication apply alone must pass ALL fresh target
eligibility, history/head equality and prospective headroom checks. Partial original
objects, changed/absent/tombstoned current roots or malformed/ambiguous receipt
state never authorize first publication or a second attempt.

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
and exact original live state), unresolved(status without exact receipt but changed, absent or partial-publication state), invalid-input, unavailable, unsupported, busy, conflict,
unknown. Refusals have no intent/receipt/summary; original input conversation may
be included only after strict admission. possible_effect=false before dispatch;
true after publication attempt, acknowledged original receipt or exact original
partial-object evidence. Status without receipt OR original partial-object evidence
uses false but makes NO historical no-deletion claim. Current state is
separate from historical acknowledgment and can be changed after a valid receipt.

Prepare/inspect never publish. Apply first recognizes ONLY the exact original
manifest+receipt+deterministic envelopes, including the retained original
root/binding matching intent. Later history equality
is NOT an acknowledgment precondition. Without receipt and without partial original
objects, apply may first-publish only after complete fresh original-state and
reserved-headroom validation. Success
requires exact durable transaction/receipt readback; all errors after publication
attempt return unknown/possible_effect=true, no automatic write retry or rollback.
Explicit status of the SAME original intent observes exact receipt or unchanged/
unresolved current state, without writing. A matching root tombstone without exact
original receipt is unresolved, never acknowledgment. Exact historical receipt
may acknowledge even if current heads changed later; show current_state=changed.
Output loss never authorizes repeating with a fresh operation or re-preparing.
