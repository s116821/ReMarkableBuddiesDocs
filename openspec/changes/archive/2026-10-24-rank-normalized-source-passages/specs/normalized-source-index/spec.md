## ADDED Requirements

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
