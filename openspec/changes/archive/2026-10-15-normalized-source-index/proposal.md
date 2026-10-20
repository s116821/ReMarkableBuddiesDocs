# Bounded normalized source index

## Why

REM-4 needs a replaceable retrieval backend with exact source provenance and bounded context. An immutable normalized-material index is useful independently of tablet identity, extraction and answering-provider integration. Those broader Reader requirements remain in REM-4; this change does not implement or archive them.

## What changes

Add the public Index/Cache/Provider library seam with validated document/format/content/extractor identity, exact page/section/UTF8 source ranges, deterministic lexical retrieval across the full document, optional same-unit neighbors, deduplication and full serialized-result budgets. Refuse changed keys and invalid material, and preserve a valid index if replacement fails.

## Precode and delivery boundary

The contract and required prior-art examination were published before implementation in [ba291120](https://github.com/s116821/ReMarkableBuddiesDocs/tree/ba29112029e765b81052ee1b4a539af7126eb87a/openspec/changes/source-document-retrieval). The subsequent explicit incremental-delivery instruction narrows this independently complete capability; it does not retroactively claim the broader plan was implemented. Original full plan and stacked source refs are preserved. This delivery carries only the index implementation onto current main, with no unrelated draft ancestry.

No extraction adapter, automatic Reader source association, native authority, answering prompt, external research, disk cache, new storage engine or SDK dependency is introduced. Main owns this library and central Docs; other lanes continue independently.
