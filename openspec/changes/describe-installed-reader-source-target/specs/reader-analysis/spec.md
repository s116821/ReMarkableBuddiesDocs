## ADDED Requirements

### Requirement: Installed Reader recognizes source subject separately

The ordinary installed Reader proposal SHALL request a short optional description of the selected source in its existing first provider request. The description SHALL be separate from the handwritten question, answer and normalized center. The independent transcription request SHALL continue to receive only its normal inputs. Subject availability SHALL NOT trigger another model request.

#### Scenario: Handwritten question refers to circled content

- **WHEN** a verified handwritten question refers to a visible circled or highlighted subject
- **THEN** Reader retains the question as written and accepts a single bounded description from the same proposal for the marked source

#### Scenario: Subject is unavailable

- **WHEN** the proposal omits the subject, explicitly abstains for the field, duplicates it or offers an invalid value
- **THEN** Reader omits the subject and applies its existing question verification and answer rules
- **AND** it does not substitute the question, answer, center or a later capture for the subject
