## MODIFIED Requirements

### Requirement: Current-page answer proposal
Each iteration SHALL capture the current page and send an overview plus three detail strips with ANALYSIS_PROMPT. The prompt SHALL ask for one readable handwritten question associated with a closed outline or deliberate highlighted passage, distinguish handwriting from typeset text and user selection from printed shading, allow surrounding context/general knowledge, preserve paper-specific values, and request plain ASCII output. Highlights SHALL NOT require a surrounding closed outline. Missing selections or ambiguous question-to-selection association SHALL request abstention. SELECTION_CENTER SHALL replace OUTLINE_BOX and identify the approximate center of the selected outlined/highlighted content in the full-page overview's 768 by 1024 pixel coordinate frame, excluding question and detail-strip coordinates. Selection interpretation remains model-based rather than independently proven from pixels. Source: src/workflow/orchestrator.rs analyze_and_answer/ANALYSIS_PROMPT.

#### Scenario: No readable question
- **WHEN** the response begins with NONE ignoring case and outer whitespace
- **THEN** the proposal is declined and the workflow records a non-ink Selection diagnostic without navigating for an answer.

#### Scenario: Highlighted concept
- **WHEN** a readable handwritten question clearly refers to a deliberate highlighted passage without a closed outline
- **THEN** the prompt permits an answer about that selected concept using the same format and independent question verification as a circled selection.

#### Scenario: Closed-outline compatibility
- **WHEN** the question clearly refers to content within a closed outline
- **THEN** the existing selection remains accepted under the same question-verification and answer-placement rules.

#### Scenario: Absent or ambiguous selection
- **WHEN** the page has a question but no clear user highlight/closed outline, only printed gray shading or an X, or an unclear association among selected topics
- **THEN** the prompt requests NONE rather than inventing a selected concept.

#### Scenario: Highlight without readable question
- **WHEN** highlighted content has no question or essential handwritten words are illegible or ambiguous
- **THEN** the prompt requests NONE and does not substitute a passage summary for the missing question.

### Requirement: Independent transcription agreement
Before navigation or answer output, the system SHALL clear model content and request transcription from the same overview/detail images without the proposed question or answer. It SHALL require a nonempty TRANSCRIPTION: value that agrees after normalization; verification provider errors SHALL decline the proposal using the provider failure code, distinct from the transcription-disagreement code, while device/input cancellation errors SHALL propagate and prevent answer output. Source: src/workflow/orchestrator.rs verify_question/transcriptions_agree.

#### Scenario: Harmless variation
- **WHEN** case, question punctuation or spacing around operators differs
- **THEN** equivalent normalized text can agree.

#### Scenario: Meaningful disagreement
- **WHEN** operators, numeric separators, grouping or word boundaries differ, or transcription is NONE/missing
- **THEN** verification fails and a non-ink Transcription diagnostic is recorded without writing the proposed answer.
- **AND** agreement remains a comparison check rather than proof of semantic correctness.

#### Scenario: Device failure during verification
- **WHEN** a non-mutating input/cancellation callback fails during the independent verification wait
- **THEN** the iteration reports that error without source feedback rather than treating it as a successful question decline.

#### Scenario: Unavailable verification
- **WHEN** the verification provider fails or times out
- **THEN** no answer is written and a non-ink Provider diagnostic is recorded, rather than claiming transcription disagreement.
