# Proposed source-cache maintenance version1

This is precode review material, not implemented behavior.

## Platform capability
This new producer is Linux-only. On every non-Linux target, all four operations
return unsupported with runtime_unverified:true and possible_effect:false before
stdin reads, Config/root access, locks or mutation. Do not reuse the non-Unix
sync_dir no-op as proof of durability. Existing cache APIs remain unchanged.
Windows tests prove this early boundary, strict flag admission and encoding only;
they do not claim local preview, applied deletion or directory durability. Future
Manager browser/Electron consumers can both invoke the Linux tablet CLI through
existing host adapters; neither consumer is implemented by this delivery.
The frozen Windows identity vector is encoding-only reserved data, not a Windows
filesystem implementation or promise of maintenance support.

## Route and input
`reader-buddy --source-cache-operation inspect|prepare|apply|status --source-cache-input -`
with the existing explicit Config selector. All four operations require the raw
literal dash; equals-form aliases such as -/ refuse before any stdin read.
Incompatible execution modes refuse before Config, Store or provider startup.
A complete UTF8 JSON object plus EOF is required, maximum16384 bytes; unknown,
duplicate or missing fields, arrays in object positions, extra JSON, bad UTF8,
noncanonical/nil UUIDs and unsupported versions refuse without path access.
No input file path or arbitrary deletion path is accepted.

inspect: `{request_version:1,document:UUID}`.
prepare: `{request_version:1,operation:UUID,document:UUID}`.
apply/status: `{request_version:1,intent:INTENT}`.

All UUID strings use exact lowercase hyphenated canonical spelling. SHA256 values
use exactly64 lowercase hex digits. Request shapes are closed raw objects before
Serde conversion; custom value validation preserves exact spelling.

## Private intent
INTENT is a closed version1 object containing intent_version, operation, document,
config_path_sha256, config_bytes_sha256, roots_sha256, actor, generation,
store_owner_sha256, cache_owner_sha256, namespace_owner_sha256,
namespace_identity_sha256, entry_identity_sha256, entry_bytes and entry_sha256,
plus intent_sha256. All hashes bind canonical bytes, not human path display.
Identity encodings are fixed and portable at the wire level, but host-local
file identity values are opaque hashes: an intent is usable only on its original
filesystem and configuration, never transferred as cleanup authority to another
host/store. entry_bytes is an integer1..33554432; version1 cache entry validation
must pass before preparation. No normalized source text/title/location/key is
returned. Exact encodings and the intent digest domain are defined below and frozen in
digest-vectors.json; those vectors are synthetic, not filesystem qualification.

prepare performs no mutation and returns an intent only for a present valid
selected slot. inspect returns no reusable permission token. Missing selected
slot returns absent without an intent. apply/status reject a malformed or changed
intent before deletion; a matching public digest alone supplies no authorization.

## Admission/custody
Use a dedicated private header/lease custody type, never Store::open_existing,
Store::open, recover, DiskCache::open or an ordinary Store with an empty index.
Validate existing safe/disjoint configured roots, data/cache ownership headers,
actor, CURRENT and current ordinary format1 through known bounded file reads;
acquire the existing nonblocking Store lease.
Validate and acquire existing namespace cache.lock next; verify named/held file
identity. No initialize/recover/chmod/create/cleanup/publish call is permitted.
Only these known Store/header files may be read: data/identity.json (1024 bytes),
data/CURRENT (128), data/generations/<CURRENT>/format.json (64), cache/owner.json
(1024), and normalized-sources-v1/owner.json (1024). All JSON formats are strict
and supported; nil CURRENT/actor refuses. Config uses the existing bounded strict
Config reader. Existing store.lock/cache.lock are opened solely for custody and
identity checks. The selected entry is the sole cache payload read, capped32MiB.
Never enumerate generation directories, commits, objects, quarantine or sync;
never read durable payloads/indexes, recover history or publish capabilities.
Credentials root participates only in Config-root binding/safe-disjoint path
validation; no credential-root marker, filename discovery, contents or resolver.
Refuse selected-mode Store formats rather than adding another mode capability.
Check fixed namespace marker format1/actor/kind. Allow at most16 canonical UUID
slots and fixed owner/lock files; any unknown entry/type/staging/reparse refuses.
Recheck Config/roots/actor/generation/markers/lock and namespace identity before
and after selected read, and immediately before mutation. Hold both existing
leases through report emission/failure. Existing safe-file helper guarantees and
cooperating locks bound the threat model; do not promise protection from hostile
same-user directory replacement.

## Reports
Closed report_version1 object: report_version, operation (inspect/prepare/apply/status),
status, runtime_unverified:true, possible_effect:boolean, document (nullable UUID),
intent (nullable INTENT), entry_bytes (nullable bounded integer), entry_sha256
(nullable digest). No path, text, metadata excerpt, credential or error string.
At most16384 UTF8 bytes including newline. Exit0 means one complete bounded report,
including fixed refusals; exit1 means report/transport failure without JSON success.

Status enum: ready, prepared, applied, absent, unchanged, conflict, unknown,
invalid-input, unavailable, unsupported, busy.
inspect present =>ready; prepare present =>prepared with intent. apply unchanged
original =>one remove_file, directory sync, absent readback =>applied. Pre-mutation
changed binding =>conflict with possible_effect false. Pre-mutation unavailable,
unsupported or busy is explicitly nonmutating. Once remove is attempted, any
uncertain remove/sync/readback failure =>unknown, possible_effect true; no retry.
If selected slot is already absent at apply, return absent and do not mutate;
that is not proof this operation previously succeeded. status original exact file
=>unchanged; absent=>absent; present changed binding=>conflict. Status never removes,
rebuilds or repairs anything. Prepared intent is returned only for prepared;
other reports carry intent:null. possible_effect is true only for applied/unknown
apply results; status absence does not claim historical causation.

## Compatibility
This additive source producer does not advertise Manager/browser/Electron support,
new native/runtime readiness, generalized garbage collection or reclaimable byte
accounting. Existing wire contracts and all legacy cache API behavior remain
unchanged. Manual public CLI and independently versioned integration remain valid.

## Frozen digest encoding
`H(bytes)` is lowercase SHA256 of exact bytes. Owner/config/entry byte digests use
H directly, including all whitespace. `F(domain, parts)` hashes ASCII domain then
one NUL byte, followed by each part encoded as unsigned64 little-endian byte
length then exact bytes. String parts use UTF8, integers use canonical ASCII
unsigned decimal (zero is 0), and UUID/hash parts use their canonical ASCII form.
No JSON serializer, locale, case folding or Unicode normalization participates.

config_path_sha256 = F("buddy-cache-config-path-v1", [absolute canonical safe
Config path UTF8]). Refuse unrepresentable UTF8 paths. roots_sha256 =
F("buddy-cache-roots-v1", [canonical data path, cache path, credentials path]) in
that order. Paths are resolved from that Config, never from request bodies or
environment overrides. Store/cache/namespace owner digests hash exact respective
marker bytes. store_owner_sha256 covers identity.json; cache_owner_sha256 covers
cache/owner.json; namespace_owner_sha256 covers normalized-sources-v1/owner.json.

Filesystem identity = F("buddy-cache-file-identity-v1", [platform, volume,
file-id]). Unix platform is unix; volume=st_dev unsigned decimal, file-id=st_ino
unsigned decimal. Reserved encoding vector platform is windows; volume=GetFileInformationByHandle
volume serial DWORD unsigned decimal, file-id=high32<<32 | low32 unsigned decimal.
Only Linux filesystem identity is implemented in this delivery. Open existing
handles only, compare held and named identity, refuse unavailable
identity instead of substituting timestamps/length. Directory handles use the
platform existing-directory flag; no creation. Namespace and selected entry
identities are encoded the same way. Other platforms return unsupported before filesystem admission.

intent_sha256 = F("buddy-source-cache-cleanup-intent-v1", field values in this
exact order: intent_version, operation, document, config_path_sha256,
config_bytes_sha256, roots_sha256, actor, generation, store_owner_sha256,
cache_owner_sha256, namespace_owner_sha256, namespace_identity_sha256,
entry_identity_sha256, entry_bytes, entry_sha256). intent_sha256 itself is excluded.
INTENT has exactly those16 fields including its digest; reject extras/duplicates.
Digest vectors cover ASCII/nonASCII path parts, both identity platforms and the
whole intent plus one-field mutation. They freeze encoding only, not file access.
