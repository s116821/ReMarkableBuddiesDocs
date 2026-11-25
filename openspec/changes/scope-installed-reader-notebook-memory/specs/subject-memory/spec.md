## ADDED Requirements

### Requirement: Notebook scope for an installed Reader source question

When subject memory is enabled and the ordinary installed Reader has a verified resident capture, it SHALL query the existing provider with the document ID from that capture and the independently transcribed question. Relevant global and matching document facts MAY enrich the answer under the existing profile, relevance and size limits. Facts scoped to other documents SHALL be excluded. The transcription requests SHALL receive no subject-memory facts.

#### Scenario: Same subject in two notebooks

- **WHEN** two notebooks have distinct facts on the same subject and the user asks a handwritten question in one of them
- **THEN** only that notebook's document facts and eligible global facts may reach the answer alongside the original question and images.

#### Scenario: Source identity is unavailable or independently selected

- **WHEN** the ordinary input lacks a verified notebook ID, or a selected Reader operation supplies its own ownership record
- **THEN** the existing unscoped or selected query rules apply respectively. Disabling subject memory preserves the original question and answer flow without a memory query.
