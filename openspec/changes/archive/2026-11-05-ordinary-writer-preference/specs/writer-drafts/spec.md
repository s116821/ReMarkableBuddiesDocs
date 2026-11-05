## MODIFIED Requirements

### Requirement: Durable Writer drafts refine within one conversation
The Writer SHALL use the existing provider and conversation Ledger, retain exact
user requests and separate explicit guidance/source data, and store proposals as
Writer Generated drafts. Refinement SHALL name one unique current draft and use
its original source within the same conversation, without rewriting prior turns
or treating unrendered drafts as native-verified Completed history. Optional
personalization SHALL remain a preference, and subject memory SHALL NOT be
required. Explicit selected-draft export preparation SHALL return the existing
PreparedNote without sending an external note or operating the tablet.

The ordinary draft receiver SHALL include an effective saved preference once
as a separate prompt part. The preference SHALL yield to the current request
and fixed task/source-safety instructions and grant no action permission.
An absent, empty or disabled preference SHALL preserve existing prompt parts.
The preference SHALL remain outside the exact request/history/source data.

#### Scenario: Generate then refine after restart
- **WHEN** a saved Writer draft is selected with a new exact refinement request after Store reopen
- **THEN** a new draft in the same conversation preserves prior requests/source facts and the selected draft, and neither draft claims native completion.

#### Scenario: Prepare deliberate export
- **WHEN** a caller names a unique current draft/source and valid correlation/effect identities
- **THEN** preparation returns the exact selected content and provenance in PreparedNote with no Mem write, native capture or rendering.

#### Scenario: Regeneration retains logical export scope
- **WHEN** a new deliberate generation uses changed source content for the same document identity and explicit page/notebook selection
- **THEN** prepared export retains the same logical source scope and advances its content/draft revision, allowing the existing correlation to update the same note rather than being rejected as a different source scope.

#### Scenario: Conflicting preference during generation or refinement
- **WHEN** the ordinary draft receiver receives an effective preference and a current request
- **THEN** the receiving prompt explicitly prioritizes the current request and fixed task/source-safety instructions, and the preference remains separate from durable history.
