# Proposed external input contract

This is a pre-implementation contract for new notebook command input and declared
Writer simulator assets. Existing Reader admission and owned Store-object reads
retain their contracts. Source data is not a credential: credential owner/mode/
single-link restrictions are not imposed merely to reuse safe-open code.

Generation requires document_file and document_sha256 (64 lowercase hexadecimal
characters). Every simulator asset requires its corresponding raw SHA-256. Resolve
assets relative to the scenario directory; reject absolute asset names, traversal
outside that directory and unsupported path aliases. Command paths may be absolute.
Reject symlink/reparse traversal, directories, sockets, FIFOs, character/block
devices, Windows device/pipe paths and alternate data streams. Admit only regular
local disk files. Reject an unsupported filesystem/platform safe-open contract
explicitly before Store admission, model use or scenario execution.

Linux admission uses component-aware no-follow directory traversal with retained
directory handles, then openat with O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_CLOEXEC.
O_NONBLOCK is required before the first fstat/read so a regular-file-to-FIFO race
cannot block open. fstat must establish a regular file before any read. Compare
the opened dev/ino, size, mtime and ctime with named no-follow metadata before and
after reading, resolving through retained directory handles. Refuse changed path
bindings, renamed/replaced components, truncation/growth or changed metadata; do
not reopen a pathname as a fallback. Parent binding checks reduce substitution;
the expected content hash, not metadata, binds accepted content under races.

Windows admission must use a disk-file handle with reparse-aware/no-follow
component validation, sharing that denies writes/deletes during admission, and
handle file-type/attribute validation before reading. Compare volume/file identity
from the opened handle with the named binding before/after read; size/time-only
fallback is insufficient. Reject reparse components and device/pipe/ADS aliases.
If the implementation cannot provide this contract on a target/filesystem, report
Unsupported; do not silently weaken it to File::open plus a size check.

Check observed length and stream at most 8 MiB plus one rejection byte. No unbounded
read_to_end, FIFO probe read or mmap. Require actual bytes read to match the admitted
length, no metadata/binding change, and SHA-256 of the exact observed raw buffer to
match the declared hash. Then require valid UTF-8, strict typed JSON (including
duplicate/unknown-field rejection), Index validation and all logical bounds. All
assets (32 MiB aggregate) and all plans/credentials must pass before execution.
Retain the validated buffer; parse/canonicalize from it without reopening the file.

The resulting buffer is immutable application input. It is not evidence that the
filesystem supplied an atomic snapshot during concurrent writes, nor a guarantee
of a hard filesystem wall-clock deadline. Expected digest matching establishes
the exact admitted content; ordinary metadata checks alone cannot do that. Direct
library callers may provide an already-owned immutable buffer with the same bounds,
hash and strict validation, without inventing a file path.

Retain raw digest/count and canonical media digest/count separately. Retain complete
logical normalized values/order; raw JSON formatting and original physical notebook
bytes are not retained. Never persist/forward the OS path, handle identity or raw
OS errors in model input, durable source facts or reports; use fixed error codes.

Required implementation tests use owned temporary fixtures and synchronization
barriers: regular file; one-over bound; invalid UTF-8/JSON/duplicate field/hash;
directory/symlink/socket/FIFO/device alias; regular-to-FIFO/symlink and parent-binding
replacement; concurrent growth/truncation/replacement; Windows reparse and file-ID
checks; unavailable safe-open support. A bounded child process proves FIFO refusal
without hanging the suite. Assert zero Store/model/destination effects on refusal,
no sensitive paths in reports, and no sleeps as success. Existing credential and
owned-object helpers may inform implementation, but their differing guarantees
must not be treated as proof that external input admission already works.
