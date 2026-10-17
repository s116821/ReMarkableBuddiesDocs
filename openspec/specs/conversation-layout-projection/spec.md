# conversation-layout-projection Specification

## Purpose
Define read-only normalized conversation presentation from chronological persisted context, preserving separate native rendering and current-admission gates.
## Requirements
### Requirement: Read-only unified conversation projection
The presentation planner SHALL project immutable chronological conversation context into newest-exchange-first history, with original user before assistant, exact turn/source identities and full original text, without changing ledger or draft or issuing model/native commands.

#### Scenario: Mixed chronological exchanges and long text
- **WHEN** valid Reader/Writer exchanges and a user-edited draft are supplied
- **THEN** only exchange presentation order reverses, user-before-answer and all text/source references/draft remain intact in disjoint normalized owned regions.

#### Scenario: Empty start
- **WHEN** bound historical presentation context has no turns
- **THEN** the plan contains ReMarkableBuddies title and input area with no fabricated question or model request.

### Requirement: Presentation identity and native boundary
Planning SHALL use persisted conversation identity independently of header pixels, typography, scale, scrolling or global caches; unknown/unbound/legacy identity and inconsistent turn/source context SHALL refuse. A plan SHALL NOT supply current native write, scroll, focus, erase or publication authority.

#### Scenario: Scrolled or differently styled header
- **WHEN** the same valid persisted presentation context is used across visual header differences
- **THEN** the plan remains identity-stable without consulting header pixels or changing native content.

#### Scenario: Unknown or inconsistent context
- **WHEN** presentation identity is missing or context has foreign, duplicate or causally misordered turn identities
- **THEN** planning refuses without changing the original ledger/draft or clearing user content.

