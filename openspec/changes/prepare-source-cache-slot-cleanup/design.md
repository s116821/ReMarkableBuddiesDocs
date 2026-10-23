# Design

## Current evidence
Rust retrieval/disk.rs has a16-slot,32MiB-per-entry version1 owned namespace.
DiskCache::open borrows Store, validates ownership, can create/chmod/clean staging
and opens a namespace lease. forget unlinks exactly one UUID.json and syncs the
directory; sync failure can follow deletion. Existing owned-data inspection is
read-only and explicitly grants no cleanup permission. Store::open_existing is noninitializing but calls recover, enumerating durable
commits and validating object payloads. It also validates credential-root ownership
markers. It cannot provide this bounded header-only admission. Existing sync_dir
syncs only on Unix and returns success without syncing on Windows. Current ordinary
Store admission rejects selected-mode formats. These are source facts, not device qualification.

## Decisions
Use separate private existing-only header/lease custody with explicit known-file
read limits, no Store construction/recover/index and no durable tree enumeration
or payload reads. Reuse safe-path/owner/cap validation and the Linux one-slot
unlink+directory-sync semantics rather than wrapping mutating cache open. Keep
all legacy Store/cache APIs unchanged. Non-Linux returns unsupported before stdin
or any Config/root/lock access; no Windows no-op can yield applied. Both browser
and Electron future adapters may invoke the same Linux tablet producer; local
Windows producer execution remains explicitly unsupported. Require existing store.lock and cache.lock; never create
or chmod either. Acquire Store first, namespace second, nonblocking; hold both
until report write succeeds or fails. Linux fixtures must prove actual custody/admission and mutation. Windows fixtures
prove early unsupported without stdin/filesystem access, not local admission or
deletion. Preserve all seven encoding vectors, including reserved Windows data.

Scan only the fixed namespace, bounded by the existing slot/entry enumeration
limits. Unknown entries, unsafe/reparse paths and any staging files refuse this
maintenance operation rather than adopting, traversing or cleaning them. Validate
the selected bounded entry wrapper and normalized material using the existing
Index validation; its embedded key is never used as current-source authority.
Other valid UUID slots are counted but their contents are not read.

The intent binds the exact selected Config bytes/path, resolved owned roots,
actor, current ordinary generation, supported store/cache ownership markers,
namespace identity and original selected entry bytes. All exposed bindings are
hashes/UUIDs/fixed fields, never paths or normalized content. Apply revalidates
all bindings under custody. A hash is conflict detection, not authentication or
permission against an adversarial same-user process. Existing path safety and
cooperating OS leases are not a hostile-filesystem sandbox.

## Outcomes and limits
A successful remove followed by directory sync and absent readback yields
applied. Any failure after remove may have taken effect: report unknown with
possible_effect true; never retry or claim rollback. Readback disappearance only
proves present absence, never historical deleter identity. Reappearing different
bytes yield changed/conflict, not an instruction to delete again. Identical
recreated bytes cannot be distinguished from the original file without identity
binding; bind selected file identity as well as digest and recheck it.

No receipt file, tombstone, recovery journal, staging cleanup, persistent operation
registry or background worker. Consuming report output failure is caller-unknown;
return a transport failure and perform no retry/compensation. status uses the
original intent. runtime_unverified remains true for every report.

## Verification
Fresh synthetic owned directories only, complete before/after byte+preservation
metadata snapshots (excluding OS-managed access times) outside the selected deleted file,
explicit filesystem read/enumeration admission controls rejecting every durable
payload/tree access, poison payload directories that cannot be traversed, missing
and corrupt durable commits that do not affect valid header-only cache admission, NoWrite/no-create observations,
held writer/namespace locks, lock replacement, symlink/reparse/unknown/staging
refusals, selected entry bounds/schema, Config/actor/generation/owner/file changes,
post-unlink sync/readback/output failure injection and recovery status. Exercise
actual Linux CLI stdin/early routing and Windows no-read unsupported routing, original executable provenance,
all raw stdout/stderr hashes, and strict malformed/oversized/EOF controls. No
source freshness, native, installed runtime or real-provider result is claimed.
