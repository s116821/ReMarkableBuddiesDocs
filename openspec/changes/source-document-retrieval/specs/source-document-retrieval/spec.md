## ADDED Requirements

### Requirement: Bounded source-associated passage retrieval
Reader document retrieval SHALL use the source document associated with the conversation turn, retain source content/extractor and page/section provenance, and enforce context budgets without injecting the whole document. Missing or blank-start source association SHALL NOT be fabricated from the visible Buddy page. Retrieval SHALL remain separate from native operation authority and the answering provider.

#### Scenario: Repeated and changed source queries
- **WHEN** a follow-up queries an indexed document or the source content/extractor changes
- **THEN** retrieval searches the applicable full document anew and invalidates reuse of incompatible derived indexes while retaining passage provenance

#### Scenario: Bounded normalized material
- **WHEN** explicitly normalized source material is indexed and queried
- **THEN** invalid identity or bounds refuse, selected UTF8 passages preserve exact source-unit ranges, and full serialized results obey requested limits without presenting truncation or source mismatch as empty success

### Requirement: Reader research and source evidence policy
The receiving Reader SHALL preserve the exact user request and turn-linked images, assemble relevant local document context and optional subject memory, research externally by default under configurable policy, honor explicit no-internet, and retain useful provenance while reconciling conflicting evidence. These data SHALL NOT grant native effects or change request transcription.

#### Scenario: Absent source and no internet
- **WHEN** a conversation has no associated source or explicitly forbids internet research
- **THEN** Reader preserves absent-source provenance and the no-internet restriction, using only available permitted context or requesting missing scope

#### Scenario: Actual receiving evidence
- **WHEN** retrieved passages or research influence an answer
- **THEN** their source/page/section/revision provenance remains associated with the turn, and currentness, cancellation and source safety are checked through the actual receiving path
