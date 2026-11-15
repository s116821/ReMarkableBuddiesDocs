## ADDED Requirements

### Requirement: Combined ordinary local scenario
The simulator SHALL exercise the production dispatcher with scripted receiving models, one Ledger and simulated device effects.

It SHALL also offer a separate explicit opt-in combined receiving qualification
entry using the same production Dispatch/Writer/notebook paths. Its credential-free
control SHALL use the same sequence/assertions. Live execution SHALL be bounded to
seven non-retried provider requests,4000 output tokens per request,90s per request
and12min overall, preserve original payload/reply evidence and stop on error.
Scripted success SHALL NOT be reported as live or native qualification.

#### Scenario: Reader Writer Reader handoff
- **WHEN** a scenario switches receiving buddies and returns to Reader in one conversation
- **THEN** assertions cover exact text, ordered history, historical image evidence, preset separation, disabled modules, blank start, ambiguous export and stale or canceled effects.

#### Scenario: Synthetic boundary
- **WHEN** a simulated visit or aggregate revision invalidates admitted work
- **THEN** the scenario verifies suppression of the stale effect without granting native or selected-sync qualification.

#### Scenario: Reviewed receiving qualification
- **WHEN** an explicitly selected bounded live sequence follows credential-free payload/source review
- **THEN** actual returned Reader/Writer/notebook responses and image/source associations are retained for independent semantic assessment, with no external export or native effect and no optional memory route silently enabled.
