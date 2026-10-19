# Design

## Existing contracts
Consume Store.paths.cache and storage::files ownership/path checks, bounded JSON,
atomic write/fsync/rename, directory sync and staging cleanup. The Store lease
must remain alive throughout use. Index::build already validates normalized
identity, source-unit limits, locations and controls, and computes the full key.
Cache normalized input rather than serializing private chunks or term indexes.

## Ownership and serialization
Use only cache/normalized-sources-v1, with a versioned domain owner marker bound
to the Store actor. Refuse a populated unmarked namespace, mismatched owner or
symlink/reparse path. A persistent namespace lock uses the existing File::try_lock
pattern and is held by the cache handle; a second handle refuses immediately.
Explicit unlock on drop follows the existing Store lease lifetime rule.

Open may create owned directories/marker/lock and, after ownership and locking,
clean only shared-helper .stage-UUID files. It is not filesystem-immutable
inspection. Unknown entries refuse instead of being deleted or adopted.

Each canonical document UUID names one JSON slot. Format 1 contains the complete
IndexKey and NormalizedDocument, with unknown fields refused. At most 16 document
slots and 32MiB complete encoded bytes per slot are admitted. Replacement needs
one additional bounded staging file before atomic publication. These are logical
byte/count bounds, not a hard process RAM/CPU deadline or disk quota for other
cache domains. No automatic eviction or broad cleanup is introduced.

## Operations
Install validates/builds first and bounds complete serialization before touching
the destination. Invalid input, capacity exhaustion or prepublication failure
must preserve the previous accepted slot. Atomic publication and durability
semantics remain those of the shared helper; a post-rename directory-sync failure
can report an error after publication and must not claim rollback.

Load requires an independently selected expected IndexKey. Bound the read,
decode the closed wrapper, rebuild the Index and require stored, rebuilt and
expected keys to agree. A missing slot is an honest miss; stale/corrupt/version-
unknown material refuses without returning an Index or echoing source text.
Never derive expected freshness from the cache's own untrusted key. Original
source digests remain adapter assertions, not current document/native authority.

Forget removes only one explicitly selected canonical document slot in the owned
namespace, after path/type checks, then syncs that directory. No source file,
durable Store record/media, other domain or unknown entry may be deleted. Cache
data is disposable and excluded from sync/restore; a cache miss requires caller
acquisition/rebuilding, not an invented document or silent unrelated-source use.

## Checks and delivery
Original temp-Store fixtures exercise restart/reuse through actual Index queries,
changed source/extractor/normalized keys, tampering and malformed versions,
invalid replacement preservation, capacity, targeted forget, lock lifetime,
owned staging recovery and protected/symlink refusal where supported. Filesystem
fault behavior already tested in shared primitives is not copied into a second
engine. No simulator/model/native test can be inferred from these local fixtures.
Deliver one coordinated source/Docs change; sync/archive only its completed scope.
