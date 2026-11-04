## MODIFIED Requirements

### Requirement: Selected Writer content remains bound through export admission
The joined flow SHALL capture the expected root before selected reads and bind
exact draft/source values and revision references into the same atomic
publication that admits the export attempt. Fresh producer completion SHALL
return a private committed snapshot rather than export permission inferred from
serialized Generated fields. Changed/deleted/conflicting root, draft or source
SHALL refuse admission. Checks after admission SHALL use the exact newly
published root/guard/association references returned by that transaction, never
pre-admission or refreshed heads. Outgoing content SHALL freeze at successful guarded
admission and SHALL never be replaced by later reads. Eligibility SHALL be checked
before first destination polling and after pending discovery before the first
write poll; pre-write cancellation/change SHALL yield known no-send. After the
first write poll, cancellation/failure SHALL use the existing truthful uncertainty
boundary and SHALL NOT claim reversal or authorize retry.

For notebook drafts, guarded admission SHALL also bind the exact source archive,
completed-plan lineage and required media identity. Media integrity/availability
SHALL be validated at source use and eligibility boundaries, without reloading a
newer body or inferring freshness from stored stage successes. Legacy inline
source-revision serialization SHALL remain unchanged; notebook revisions SHALL
use an explicit versioned recipe while retaining logical document/selection
scope and existing backend correlation. Prior uncertain exports SHALL refuse new
model stages before cost. Model cost SHALL remain separate from no-send claims.

#### Scenario: Admission publishes its own guard revisions
- **WHEN** guarded admission succeeds without an external change, or a later edit advances one of its returned references
- **THEN** its exact post-admission references permit the unchanged operation and detect the later edit without self-invalidating or refreshing to bless new heads.

#### Scenario: Selection changes before admission
- **WHEN** a selected draft/source/root changes after selection but before export preparation
- **THEN** atomic admission refuses without destination polling instead of accepting a newer root while sending old or substituted text.

#### Scenario: Generation-to-destination cancellation
- **WHEN** cancellation arrives after generation completion and before the first destination poll
- **THEN** the proposal remains historical data but no destination future is polled and no write authority is inferred from its Generated status.

#### Scenario: Change during discovery
- **WHEN** cancellation or selected-state change occurs while destination discovery/readback is pending
- **THEN** the frozen body is not substituted, no create/update is polled and the result preserves a known no-send/stale distinction.

#### Scenario: No-send recording cannot commit
- **WHEN** selected-root deletion/conflict during discovery prevents recording the observed zero-write-poll outcome
- **THEN** the report separates that invocation-local observation from the actual Refused/Storage persistence failure, retains unresolved attempt state and grants no later dispatch authority from the failed recording.

#### Scenario: Write already polled
- **WHEN** a write future was polled before cancellation, response loss or failure
- **THEN** the effect remains bound to its admitted frozen body and is verified/reconciled through the known destination identity without automatic resend or a false no-effect claim.


#### Scenario: Archived proposal and own admission revisions
- **WHEN** a fresh notebook proposal reaches export admission or an intervening archive/plan/draft/root revision changes
- **THEN** exact returned post-admission references allow the unchanged operation and reject changed lineage without self-invalidation or refreshing heads to bless it.

#### Scenario: Blob unavailable before write
- **WHEN** required source media disappears or changes before the first destination/write poll
- **THEN** writing is suppressed without restarting model stages or substituting source, and observed zero writes remain distinct from failed durable no-send recording.

#### Scenario: Final notebook acknowledgment is historical
- **WHEN** a final Generated notebook draft is saved but its current invocation lost acknowledgment
- **THEN** no automatic send grant is inferred; a later explicit selected-draft operation must validate the current exact source/media/plan closure before exporting.
