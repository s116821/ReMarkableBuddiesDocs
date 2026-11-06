## ADDED Requirements

### Requirement: Explicit notebook restore family
Manager SHALL expose the delivered same-actor ordinary notebook restore as an
explicit capability using only version2 notebook selectors. Existing legacy
restore SHALL retain its original version1 admission. Family choice SHALL remain
fixed through preview, original intent custody, apply, status and cancellation.
Notebook-positive source/target previews, original intents and observed
inspections SHALL require complete media, without narrowing valid legacy cases.

#### Scenario: Prepare and confirm a notebook archive
- **WHEN** a user explicitly selects notebook restore for an archive already on the tablet
- **THEN** Manager invokes prepare-notebook, retains the original version2 intent privately and requires a separate confirmation before apply-notebook

#### Scenario: Wrong family or unavailable producer
- **WHEN** a response/intent belongs to another version or selector family, a reference belongs to another host instance, or the installed producer lacks notebook restore
- **THEN** Manager refuses without translating the intent or dispatching a legacy fallback

#### Scenario: Consistent but incomplete notebook media claim
- **WHEN** a notebook response or original intent declares incomplete media even if all other fields agree
- **THEN** Manager refuses that notebook-positive frame while preserving existing valid incomplete-media legacy admission

### Requirement: Reused bounded restore lifecycle
The notebook capability SHALL reuse existing maintenance ownership and finite
restore lifecycle semantics. Both application surfaces SHALL preserve private
inputs, captured cancellation, observation quiescence, expiry and original uncertain
outcomes without granting runtime, native, settings or retry authority.

#### Scenario: Uncertain apply followed by a desired-state observation
- **WHEN** apply-notebook has an unknown original result and an explicit status-notebook later observes the desired data
- **THEN** Manager reports that later observation without changing the earlier outcome or replaying Apply

#### Scenario: Concurrent maintenance, stopped wait or disconnected tablet
- **WHEN** another maintenance owner is active, the captured wait is canceled, or current tablet identity is lost
- **THEN** the common ownership/cancellation boundaries prevent stale or cross-family dispatch and preserve any already-possible mutation as uncertain

#### Scenario: Browser and Electron use the new capability
- **WHEN** either shared Angular surface performs notebook preview, confirmation, cancellation or retained-status inspection
- **THEN** the actual narrow host bridge applies the same family and lifecycle checks and excludes original paths/full intents from the safe view
