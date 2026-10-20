# Change: Reuse validated normalized sources across local process restarts

## Why
The delivered source index has a bounded in-process cache only. Reopening the
application currently loses reusable extracted text. Derived source material
belongs in the existing owned cache root, separately from durable evidence and
sync records.

## What Changes
Add a small Store-borrowing local disk-cache API for normalized source inputs.
Rebuild the existing Index on load and require the caller's complete expected
IndexKey. Reuse shared ownership/path, atomic-publication, staging recovery and
bounded-read primitives; do not create another persistence or conflict engine.

## Boundaries
No source discovery/extraction, Reader receiving context, provider/model calls,
native identification, cloud cache sync or complete REM-4 acceptance is included.
The independently reviewed EPUB adapter remains a separate delivery.
