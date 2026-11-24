## ADDED Requirements

### Requirement: Installed Reader recognizes source subject separately

The ordinary installed Reader proposal SHALL request a short optional description of the selected source in its existing first provider request. The description SHALL be separate from the handwritten question, answer and normalized center. The independent transcription request SHALL continue to receive only its normal inputs. Subject availability SHALL NOT trigger another model request.

#### Scenario: Handwritten question refers to circled content

- **WHEN** a verified handwritten question refers to a visible circled or highlighted subject
- **THEN** Reader retains the question as written and accepts a single bounded description from the same proposal for the marked source

#### Scenario: Literal separator text in the proposal

- **WHEN** the optional subject line contains literal `---`
- **THEN** Reader keeps the literal characters in the subject and uses the first answer separator outside that field
- **AND** existing proposals without the field and literal markers in the answer keep their established meaning

#### Scenario: Subject is explicitly uncertain

- **WHEN** a structurally valid proposal returns a single explicit subject abstention and the handwritten question passes verification
- **THEN** Reader exposes a neutral uncertainty status to the fresh exchange renderer and retains no subject text

#### Scenario: Subject is unavailable

- **WHEN** the proposal omits or duplicates the subject field or offers an invalid value
- **THEN** Reader omits the subject and applies its existing question verification and answer rules
- **AND** it does not substitute the question, answer, center or a later capture for the subject
