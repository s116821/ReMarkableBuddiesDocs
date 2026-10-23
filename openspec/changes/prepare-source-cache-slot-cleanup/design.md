# Design

## Current evidence
Rust retrieval/disk.rs has a16-slot,32MiB-per-entry version1 owned namespace.
DiskCache::open borrows Store, validates ownership, can create/chmod/clean staging
and opens a namespace lease. forget unlinks exactly one UUID.json and syncs the
directory; sync failure can follow deletion. Existing owned-data inspection is
read-only and explicitly grants no cleanup permission. Store::open_existing is
noninitializing but validates credential-root ownership markers as well as data
and cache; it does not read credential contents. Current ordinary Store admission
rejects selected-mode formats. These are source facts, not device qualification.

## Decisions
Use a separate existing-only cache admission, reusing path/owner/cap validation
and the one-slot unlink+sync primitive rather than wrapping mutating open. Keep
legacy APIs unchanged. Require existing store.lock and cache.lock; never create
or chmod either. Acquire Store first, namespace second, nonblocking; hold both
until report write succeeds or fails. Support remains conditional on actual OS
locking behavior; fixtures must prove Windows and Linux admission/refusal.

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
Fresh synthetic owned directories only, complete before/after byte+metadata
snapshots outside the selected deleted file, NoWrite/no-create observations,
held writer/namespace locks, lock replacement, symlink/reparse/unknown/staging
refusals, selected entry bounds/schema, Config/actor/generation/owner/file changes,
post-unlink sync/readback/output failure injection and recovery status. Exercise
actual CLI stdin/early routing on both hosts, original executable provenance,
all raw stdout/stderr hashes, and strict malformed/oversized/EOF controls. No
source freshness, native, installed runtime or real-provider result is claimed.
