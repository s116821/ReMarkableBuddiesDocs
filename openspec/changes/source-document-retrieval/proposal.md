# Source-bound document retrieval

## Why

REM-4 requires relevant passages from the source document associated with a conversation turn, not the currently visible Buddy page or the whole document in every prompt. The current Reader supports optional subject memory but no document retrieval/index. The existing selected ownership projection supplies a stored document association; ordinary legacy captures explicitly have none. Neither association establishes current native authority.

## What changes

Implement a provider-independent normalized source-material index with bounded page/section passages, exact document/content/extractor provenance, deterministic lexical retrieval, neighboring passages and bounded serialized context. Reuse the index only for an identical content digest and extractor revision; replacement must not retain old passages. This first implementation boundary accepts explicitly normalized material and does not discover/extract a tablet document.

Follow with actual Reader receiving integration, source-format extraction, replaceable semantic/reranking providers where useful, configurable default external research/no-internet policy and durable turn-linked context evidence. These are required broader tasks, not implied by the first index API or its offline tests. The full change remains active until its acceptance gates are met.

## Scope and ownership

Main owns Reader retrieval/context and central Docs. Existing Store paths remain storage authority; indexes are derived cache, original turn images remain durable evidence. No second Store/sync engine, automatic source identity, tablet operation, new Manager writer or SDK change. Root's incremental SDK delivery proceeds independently. Current user reserve is one percent, superseding older issue wording.
