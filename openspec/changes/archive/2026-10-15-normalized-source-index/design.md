# Normalized index design and wider Reader boundary

This capability is the independently complete local library described in the initial precode. The original full Reader plan remains preserved at ba291120 and in REM-4. The explicit incremental-delivery direction separates its acceptance from broader Reader integration; paragraphs below describing that future integration are constraints on later work, not implemented-library claims or a blanket merge gate.

## Requirements and current source

Current REM-4 description and all four comments were read in chronological order, no next page. September 26 source-turn binding and durable screenshot rules supersede visible-page/temporary-screenshot/triangle instructions. Default external research, explicit no-internet, source conflicts, follow-ups, PDF/EPUB/feasible indexed handwriting, cache invalidation and provenance remain acceptance requirements.

Buddy feeaf475 has no retrieval or research module. Selected Attempt::memory_document obtains current stored document ownership under selection admission; legacy/ordinary returns None. Historical UUIDs or stored SourceObservation are not native admission. The first normalized-material API takes an explicit document identity and expected content digest, never a path/title/current screen. An unavailable or mismatched document is not empty success.

## Initial implementation boundary

- An immutable normalized document carries a non-nil UUID, source SHA256, bounded extractor revision, format and ordered page/section units. Validate bounds and all identities before building an index. Source text is data, never instructions or an authority grant.
- Keep page/section identity and UTF8 byte ranges into the original unit text. Split at UTF8 boundaries without altering source bytes. Content hashes identify original source bytes as reported by the extracting adapter, not proof of extraction fidelity; normalized-content digest additionally detects stale/corrupt normalized data.
- Deterministic lexical scoring is an initial replaceable local retriever. Query the entire indexed document anew on every follow-up; do not restrict to previous hits. Stable ties follow source order. Deduplicate selected chunks, include immediate neighbors only within the same source unit, and enforce match and full serialized-context byte budgets. Do not truncate UTF8 or silently omit mandatory provenance. No relevant match is complete-empty; malformed/mismatched input refuses.
- Cache identity includes document, source digest, extractor revision and normalized-content digest. Installation/replacement rebuilds from immutable normalized material; no wall-clock freshness inference or cached result reuse after a different query/content identity. This increment does not add an on-disk cache before its ownership/atomic-read integration is specified.
- Public API is a narrow library boundary, with focused real input/index/query tests. No CLI endpoint, service or installed automatic extraction is claimed. Do not change prompts until receiving integration and its evidence recording are implemented.

## Later REM-4 integration outside this capability

The Reader must use turn-linked source association and original evidence, preserve exact recognized request/history, assemble local page then retrieved passages then optional memory and independently governed external research, and recheck currentness before consuming results. Missing source/blank-start cannot acquire a fabricated document. Configured extraction failure, incomplete index and no matches are distinct. The actual answer context must retain useful document/page/section/hash provenance with its turn. No source text in routine diagnostics.

External research defaults on, with explicit user/config no-internet overriding it. Treat document/memory/web text as untrusted data and reconcile conflicts rather than grant tools or native permission. Research/semantic/model providers and storage remain separately replaceable. Live semantic and native effects require their own actual evidence; offline ranking tests cannot substitute.

## Narrow prior art, pinned before implementation

- [remarkable-mcp extraction](https://github.com/praveensehgal/remarkable-mcp/blob/d385834dbc80ebef2f61b8fe898c84288fc605a1/remarkable_mcp/extract.py): inspected extraction/cache declarations, PDF fitz and EPUB ebooklib entry points. Its whole-document string/TTL approach is not sufficient source-revision or page provenance for this contract. No code copied.
- [reMark chunker](https://github.com/BGGBTAC/reMark/blob/d5d76e0d1b4c10de7aa85f445e454c7b76802b2c/src/search/chunker.py) and [query](https://github.com/BGGBTAC/reMark/blob/d5d76e0d1b4c10de7aa85f445e454c7b76802b2c/src/search/query.py): inspected heading/paragraph chunks with offsets and separate BM25/semantic/RRF retrieval. Preserve source-unit provenance and provider separation; no dependency or synthesis policy copied.
- [Smart Remarkable](https://github.com/yangg1224/smart_remarkable/blob/55cc1401aaaea26e4f9b516fdf1c5775b390af7d/README.md): inspected screen-trigger/selection/return workflow. That inspected description provides no source-document retrieval index or qualified active-document binding; no native extension adoption is authorized.
