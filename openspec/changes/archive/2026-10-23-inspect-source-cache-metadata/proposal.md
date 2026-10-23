# Bounded metadata inventory of owned source-cache slots

## Why
Aggregate owned-data inspection reports cache counts/bytes without document IDs.
Prepared one-slot cleanup requires an explicit canonical document UUID. A future
companion needs a bounded way to discover candidates without arbitrary filesystem
commands, source-text reads or implicit cleanup authority.

## What changes
Add a separate parameterless --inspect-source-cache CLI/report_version1. On Linux,
use existing-only header/Store-and-namespace lease custody to list at most16
canonical IDs and apparent lengths from metadata, with explicit unread/unvalidated
payload and freshness flags. Preserve all existing closed reports and operations.

## Scope and delivery
Docs plus Buddy producer only; future browser/Electron consumers can both call the
Linux executable through host adapters. No Manager/Docs83 changes, mutation,
source titles/text/native lookup, content hashing, Store recovery, credentials,
provider/runtime/tablet or other cache domains. One coordinated Docs/source PR
pair; concrete review before source edits, current synthetic/CLI evidence,
canonical sync/archive and normal Docs-first delivery with actual publication.
