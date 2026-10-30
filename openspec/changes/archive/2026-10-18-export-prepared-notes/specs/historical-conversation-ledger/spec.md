## MODIFIED Requirements

### Requirement: Lightweight export correlation and historical authority boundary
The library SHALL retain lightweight stable export markers and associations,
resolve only an exact unique backend/scope/revision match, and expose ambiguity
or uncertainty. A stable association SHALL support distinct deliberate export
operations and changed source revisions after confirmed completion, retaining
each operation's immutable attempt facts, historical receipts and complete
expected-head checks. An uncertain attempt SHALL require reconciliation before
a new export cycle. A positively known no-send Canceled/Failed attempt MAY begin
a new deliberate effect UUID under current heads without replaying its old effect.
Older records SHALL remain readable without being promoted
into verified current remote-body or dispatch authority. Saved binding, capture,
completion, retry and export facts SHALL NOT confer current native observation,
effect permission or selected causal-view authority.
Source: REM-37 lightweight export and historical-not-live requirements; current roadmap and later chronology; prepared-note export increment.

#### Scenario: Ambiguous export discovery
- **WHEN** exact marker discovery finds conflicting native notes or incomplete scope/revision evidence
- **THEN** reconciliation reports conflict or uncertainty without creating a native note or selecting a winner.

#### Scenario: New revision preserves stable note identity
- **WHEN** a new export operation follows a confirmed completed attempt using current expected heads
- **THEN** it may advance source revision while retaining correlation/backend/source scope and verified native identity, and old operation retries still return their original historical acknowledgment.

#### Scenario: Prepared operation is replayed
- **WHEN** preparation is retried, won concurrently or committed with a lost acknowledgment
- **THEN** its historical result does not grant fresh dispatch, and the caller must reconcile the known external identity without resending the effect.
