## ADDED Requirements

### Requirement: Durable target inheritance and closure
The conversation SHALL preserve exact introducing/correcting/retargeting target revisions, original frame/media and one current TargetState. Ordinary follow-ups SHALL inherit exact target use without repeated About. New unresolved targets SHALL not fall back. Selected document closure, deletion, retention and restore SHALL follow all retained target references without ordinary-head substitution.

#### Scenario: Correction and retarget across reopen
- **WHEN** a subject correction or different region/page is explicitly submitted
- **THEN** correction retains subject scope without handwriting learning, retarget creates a new target identity, and both histories/media remain recoverable.
