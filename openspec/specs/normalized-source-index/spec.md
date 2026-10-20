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
