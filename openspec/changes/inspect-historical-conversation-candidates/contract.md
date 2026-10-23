# Proposed conversation-root candidate inventory version1

UNIMPLEMENTED PRECODE. This packet grants no source/runtime/native qualification.

## Route and boundary
`reader-buddy --inspect-conversations` is a new parameterless Linux-only route.
Use the existing explicit absolute `REMARKABLE_BUDDIES_CONFIG` selector. No stdin,
input file, target/filter/path override, nonce or arbitrary command/unit is accepted.
Recognized conflicting execution/configuration-override flags refuse before normal
application startup without echoing their values. Ordinary clap syntax errors may
echo unexpected argv and remain exit2. Non-Linux emits unsupported before Config,
filesystem, service or input access. No dotenv, provider, Workflow or device startup.

## Shared existing-only admission
Reuse the released ordinary existing-only recovery and fixed inactive-unit observer
under unchanged conservative bounds. Config is a strict bounded safe existing file;
retain its exact path/bytes/roots and original actor/CURRENT/owner/format facts.
Legacy sync enabled refuses unavailable. Absent legacy mode or explicit LocalOnly
is admitted under the matching ordinary mode guard; other modes refuse unsupported.
Do not call Store::open, initialize, repair, chmod, create locks/markers, clean stage
files, or use a fallback recovery. Only known credentials/owner.json custody may be
read; no credentials discovery/content/resolver or provider operation.

Before content recovery, validate the ordinary current generation and all existing
safe identities:4096 commit entries,8192 object entries,8MiB aggregate manifest
lengths,1MiB each record,32MiB aggregate record lengths,256MiB aggregate object
lengths. Count bounded stages without reading/removing them; unknown or unclassified
objects refuse. There is no original deletion intent here, so deterministic orphan
objects cannot be adopted as known partials. The original deletion status route
retains its separate reconciliation rules. Selected generation/feature/history,
unsafe/reparse/symlink/hardlinked structural/payload entries and unavailable commits
refuse without candidate output or mutation.

The same sticky per-operation512MiB content-read/deserialize and65536-reference
work budget covers admission, every repeated record/head visit, root discovery and
final custody checks. Charge before work; reserve held object length before typed
payload decoding. No per-root reset, unmetered size serialization, reusable external
cache or unbudgeted Ledger/Store fallback. Reads retain bounded EOF sentinels.
This read-only operation does not reserve publication or reconciliation headroom,
construct a transaction Plan or acquire mutation permission.

Use only the existing `/bin/systemctl` observer with fixed read-only properties,
cleared environment, null stdin,4096-byte streams and3-second deadline, including
kill/reap on overflow/timeout. Only loaded/inactive/dead/MainPID0 is admitted;
other known well-formed state is busy; spawn/nonzero/stderr/unknown/malformed
observation is unavailable. Retain original Store and ordinary mode leases through all output
bytes/failure. Bracket final observation with exact Config/header/named-lock/file
fact validation; no service mutation or tablet/network operation.

## Complete bounded root discovery
Under one Store mutex, inspect every retained Conversation-namespace envelope in
the admitted generation. Require domain schema1 for values and tombstones. Decode
every value with the original supported domain decoder, preserving all identities
and historical authority. Unknown shape, wrong namespace/record/payload identity,
schema2/admitted/settlement or future schema refuses unsupported with no partial
list. The new route does not reinterpret root-like payloads in other namespaces.
Normal full owned-store envelope/reference/media verification still occurs.

Collect root record IDs from retained valid Record::Root values. A root record ID
must never have a retained value of a different record kind; such type reuse is
conflict. For each known root ID, require exactly one current head. A singleton
current value must be a valid schema1 Root with that ID and becomes one candidate.
A singleton current tombstone is excluded. Missing/multiple heads, mixed live/
tombstone heads or a non-Root current value under a known root ID refuses conflict.
No timestamp or file order chooses a winner. Tombstones that have no retained Root
value establish no current root candidate and grant no other claim.

Return unique canonical nonnil UUID strings sorted lexically, at most16 candidates.
Scan the complete bounded view before declaring complete, including deleted roots;
never truncate or expose the first16 of17. More than16 current candidates returns
too-large with null list/count. More than16 retained roots alone is not too-large
when at most16 current value roots remain and traversal fits the shared budgets.

A complete empty list means no current ordinary value-root candidates under these
rules, not an empty Store, absent history or reclaimable storage. Pending, terminal
or conflicting non-root descendants are not an eligibility decision here; valid
root presence can be listed while the separately selected preview later refuses.
Every selected target must still use a fresh existing conversation inspect/prepare
and explicit original intent. Candidates are not authorization or a native lookup.

## Closed report
Serialize these13 fields in order, UTF8 JSON plus one newline, at most8192bytes:
report_version:1, status, scope:"ordinary-current-root-candidates", complete:boolean,
candidates:null|UUID-array, candidate_count:null|integer0..16,
eligibility_evaluated:false, mutation_authority:false, native_authority:false,
runtime_unverified:true, physical_reclamation:false, local_only:true,
service_observation:"inactive"|"unverified".
Here local_only describes this nonremote operation, never an explicit saved mode.
No text/title/path/config/hash/actor/native-page/source/provider/credential/error
string is emitted. Root IDs are Buddy-owned IDs only. No new field/value is added
to any previously released report/operation.

status is complete, too-large, unsupported, busy, unavailable or conflict.
Complete alone has complete=true, array/count agreeing exactly and inactive
service observation. Every refusal has complete=false, null list/count and
unverified service observation, never a fabricated complete zero result.
Initial Config/read failure is unavailable; Store refusals preserve their existing
busy/unsupported/unavailable classification. Unclassified admission failures are
unavailable. Root count overflow is too-large; unknown/unsupported domain decoding
is unsupported; ambiguous root identity/head/type reuse is conflict; discovery
work exhaustion is unavailable. Final custody change is conflict; final observer
busy/unavailable maps directly, clears list/count and sets unverified.

Exit0 emits one complete bounded report including refusals. Exit1 is output failure;
never append a second report after a partial write. After fully safe admission,
retain custody even for discovery refusal and output failure. Report vectors freeze
the closed encoding only and grant no runtime or mutation authority.
