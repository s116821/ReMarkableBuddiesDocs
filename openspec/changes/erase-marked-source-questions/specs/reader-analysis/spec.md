## ADDED Requirements

### Requirement: A handwritten question mark permits question-only erasure

The ordinary source Reader SHALL use its existing capture and analysis to observe a visible handwritten question mark associated with a specific handwritten fragment. A mark may occur anywhere in that fragment. The mark itself SHALL suffice for erasure permission. Printed punctuation, unrelated ink, and absent or ambiguous mark association SHALL NOT grant permission. Reader SHALL keep the exact interpreted fragment and SHALL NOT add a confirmation, semantic permission test, native stroke-provenance permission test, or provider call. Answer abstention SHALL NOT determine erasure intent. Independent verification and selected-topic behavior SHALL continue governing answers. Typed and Writer routes SHALL keep their existing interpretation and submission behavior. Source: existing source capture and `Orchestrator::run_prepared`, `ANALYSIS_PROMPT`, `parse_analysis_response`, and `verify_question`.

#### Scenario: Mark inside a handwritten abbreviation

- **WHEN** the existing analysis sees a handwritten question mark within an associated readable shorthand fragment
- **THEN** Reader retains the fragment verbatim and may admit its checked region under the existing capture without another model call or confirmation
- **AND** a separate answer abstention does not veto a usable marked fragment

#### Scenario: No applicable handwritten mark

- **WHEN** the page contains only printed punctuation, unrelated marked ink or a fragment without an associated handwritten question mark
- **THEN** Reader makes no erase call and follows the existing answer behavior

#### Scenario: Distinct typed, Writer and correction paths

- **WHEN** a typed or Writer input is submitted, or the ordinary source Reader erases an admitted fragment
- **THEN** typed and Writer input retain their existing behavior and the erasure creates no handwriting correction record

### Requirement: Retain the exact question region before erasure

Reader SHALL use one checked question-only region in the exact acknowledged full-page overview. It SHALL reject missing, duplicate, malformed, overflowed or out-of-frame erase geometry. Before an erase effect it SHALL freshly acknowledge the exact interpreted question, observed original document/page, retained capture and region together through the same ordinary interpretation operation. The region SHALL describe the question separately from the selected topic and answer. Historical readback SHALL remain inspectable without effect authority. Source: `Attempt::prepare`, ordinary interpretation and receipt publication, and the checked Reader geometry in `conversation/reader_plan.rs`.

#### Scenario: Capture and interpretation precede effect

- **WHEN** the existing Reader admits a marked, bounded fragment and the source binding is current
- **THEN** its exact text, checked region and original source/capture association are durably acknowledged before any erase submission
- **AND** any answer that is subsequently presented uses the retained interpreted text under the existing rendering rules

#### Scenario: Unusable geometry or acknowledgment

- **WHEN** the region is unsafe, the persisted association conflicts, or the original interpretation acknowledgment is stale, historical or uncertain
- **THEN** Reader attempts no erase and retains only the original operation's evidence for inspection

#### Scenario: Installed Reader observes a marked fragment

- **WHEN** the ordinary installed source request recognizes a readable handwritten mark and tight question region in the captured overview
- **THEN** Reader SHALL acknowledge the exact user text and a receipt referencing the original installed capture, its observed page and session, the full captured overview and the checked region
- **AND** Reader SHALL keep the captured viewport as historical evidence. This receipt SHALL NOT grant a current viewport or erase capability.

#### Scenario: Old or incompatible receipt reader

- **WHEN** a reader encounters the new ordinary interpretation receipt on a route that cannot validate its schema or exact references
- **THEN** it refuses the unsupported history or operation without rewriting evidence or granting erase authority
- **AND** ordinary and selected receipts written without the marked-question association retain their prior encodings and admission rules

### Requirement: Make a marked question available for correction when answering abstains

Reader SHALL present the exact interpreted question and retained source association as the original user turn in the bound Buddy conversation even when answering abstains. Use the existing conversation presentation and explicit correction ownership. Preserve the composer and other turns. The operation SHALL persist the interpretation before erasure and carry it into the normal subsequent Buddy presentation; it SHALL NOT require an inactive-page write or a new source visit to authorize erasure. Source: `Ledger::presentation_context`, `conversation_layout::plan`, `workflow::exchange_history::project` and the unified-page presentation owner.

#### Scenario: Usable marked fragment without an answer

- **WHEN** answering abstains and the normal continuation presents the original persisted user-only exchange
- **THEN** the user can find that text with its original source for later correction, with no fabricated assistant turn or new correction record
- **AND** any erase remains subject to the original source guard

#### Scenario: The installed question has no answer

- **WHEN** a readable marked fragment is saved and answering abstains or the required provider is unavailable
- **THEN** Reader SHALL use the existing guarded resident Buddy placement to submit only the saved User text if currentness and placement permit it
- **AND** it SHALL keep the original ink and distinguish a submitted write from durable tablet readback.

#### Scenario: Presentation unavailable or uncertain

- **WHEN** the route is known to lack question-only presentation before an erase is submitted
- **THEN** Reader retains the interpretation and original ink and reports that unsupported route
- **AND** if a supported presentation later fails after an admitted erase, Reader retains the saved interpretation and reports that failure without replaying erasure
