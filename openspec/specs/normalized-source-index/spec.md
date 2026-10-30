# Normalized source index

## Purpose

Provide bounded local passage retrieval with exact source provenance independently of extraction, installed Reader integration and native authority.

## Requirements

### Requirement: Bounded provenance-preserving normalized source index
The normalized-source retrieval library SHALL validate explicit document/format/original-content/extractor identity and bounded source units, preserve exact page/section/UTF8 passage ranges, search the full immutable index for each query, and bound complete serialized results including provenance. Its derived in-process cache SHALL refuse stale keys and preserve an existing valid index when replacement fails. The library SHALL NOT imply extraction fidelity, automatic Reader integration or native effect authority.

#### Scenario: Fresh queries and changed material
- **WHEN** a follow-up uses another query or original content, format, extractor revision or normalized material changes
- **THEN** retrieval searches the applicable full index anew, and incompatible keys cannot query a replacement index

#### Scenario: Exact bounded passages
- **WHEN** normalized material is queried with passage and complete serialized-byte budgets
- **THEN** selected passages retain exact UTF8 source-unit ranges, duplicate chunks are emitted once, neighbors stay in their source unit, omissions are explicit and inability to fit a direct match refuses rather than reporting empty success

#### Scenario: Invalid material and failed replacement
- **WHEN** identity, locations, controls, material bounds or cache capacity are invalid
- **THEN** installation refuses without echoing source content or replacing an existing valid index, while a valid query with no matches returns an honest empty result

### Requirement: Bounded corpus-aware lexical passage ranking
The existing normalized-source Index SHALL rank direct matches with its fixed
documented term-frequency, searchable-chunk-frequency and length-normalized BM25
formula, deduplicating normalized query terms and resolving exactly equal scores
in source order. It SHALL preserve source identity and exact passage provenance,
fresh full-index queries, same-unit neighbors, deduplication and complete serialized
result budgets. Derived ranking statistics SHALL be bounded by the admitted corpus
and rebuilt from normalized inputs without a durable cache schema change. Lexical
scores SHALL NOT imply semantic matching, confidence, source verification, model
quality, current native identity or effect authority.

#### Scenario: Useful lexical distinctions and stable controls
- **WHEN** authored normalized passages differ in query-term rarity, repetition or length, or contain exact-score ties, repeated query terms, Unicode or no searchable text
- **THEN** the documented finite scorer selects the expected authored contrasts over overlap-only ordering, exact ties retain source order, repeated query terms do not boost scores and no-match results remain honestly empty

#### Scenario: Ranking preserves provenance and output bounds
- **WHEN** ranked direct passages and optional neighbors compete for count and complete encoded-byte budgets
- **THEN** exact original ranges and source key remain unchanged, direct candidates precede same-unit neighbors, duplicates are omitted once, omissions are explicit and inability to fit any direct match refuses without partial text

#### Scenario: Fresh derived ranking and historical evidence
- **WHEN** a normalized cache is reopened, a follow-up asks another question or material changes after prior evidence was captured
- **THEN** statistics rebuild from admitted normalized units, each query searches the applicable whole index, incompatible source keys still refuse, and existing historical request/passage evidence is not rewritten by a new ranking policy
