# writer-export-flow Specification

## Purpose
Compose deliberate supplied-text Writer stages with the existing exporter under fresh intent, exact selection and truthful uncertainty boundaries.

## Requirements

### Requirement: Deliberate Writer stages compose with the existing exporter
The component SHALL expose explicit bounded generate-and-export,
refine-and-export, selected-draft export and known-ID reconciliation through the
existing Writer command path, reusing the existing Writer, Ledger and replaceable
note destination with Mem first. Legacy generate/refine/prepare-export SHALL
retain their behavior and SHALL NOT send implicitly. Complete input, identities
and every required credential SHALL validate before durable admission or paid
generation. Subject memory SHALL remain optional; secret values SHALL NOT enter
arguments, reports or ordinary records.

#### Scenario: Direct then deliberate refined re-export
- **WHEN** a fresh direct request succeeds and a later explicit refinement/re-export uses the same correlation with a new effect identity after reopen
- **THEN** the exact generated/refined content is created then updated at the same verified destination note, retaining source scope and all prior attempts.

#### Scenario: Review before submission
- **WHEN** generation or refinement is requested without an explicit sending command
- **THEN** only a durable proposal is produced, and a later selected-draft export sends exactly the deliberately selected current content without another model call.

#### Scenario: Missing destination credential
- **WHEN** a direct sending request lacks required Mem credentials or has invalid input
- **THEN** it refuses before Store admission, model dispatch or destination polling without echoing sensitive input.

### Requirement: Fresh outer intent is distinct from generated or historical state
The joined flow SHALL require a positively fresh observed Ledger admission bound
to the complete outer request before automatic dispatch. Receipt replay, uncertain
admission and a HistoricalGenerated report SHALL NOT authorize model/destination
polling or continuation. The existing Ledger SHALL own this state without a
second registry. A new explicit selected-draft export intent MAY resume a
previously generated proposal, but an uncertain existing export SHALL require
reconciliation before another effect. Reports SHALL distinguish generated,
historical, no-send, uncertain and verified export outcomes.

#### Scenario: Interrupted outer flow
- **WHEN** the draft exists after restart but the outer admission is replayed and export preparation is absent
- **THEN** no model or destination call occurs, and the caller receives an honest interrupted/historical result requiring a new explicit export intent.

#### Scenario: Lost admission acknowledgment
- **WHEN** outer admission commits but its acknowledgment is lost, or its operation ID is reused for changed request content
- **THEN** no fresh grant is reconstructed from stored success and no automatic stage dispatch occurs.

#### Scenario: Uncertain earlier write
- **WHEN** an earlier effect may have been sent and a caller repeats or proposes another effect
- **THEN** existing known-ID reconciliation/no-write-retry rules remain authoritative; a new identity cannot bypass unresolved uncertainty.

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

### Requirement: Joined ownership composes with standalone entrypoints
One same-Store joined invocation SHALL span preparation, model waiting, guarded
export admission, destination waiting and result publication using the existing
Writer/export owner mechanisms in a fixed nonblocking order. Standalone paths
SHALL contend with those same owners. No Store index mutex SHALL span network
waits. Cancellation SHALL remain latched and command workers SHALL be joined;
existing model/export bounds and sanitized failures SHALL remain intact.

#### Scenario: Cross-entrypoint overlap
- **WHEN** joined, standalone Writer or standalone export operations overlap on the same Store
- **THEN** competing work reports Busy before unintended admission/provider cost and cannot exploit an independent ignored lock.

#### Scenario: Failed or late generation
- **WHEN** model output fails, is oversized, canceled or stale
- **THEN** no export starts, retained history remains truthful and releasing ownership cannot revive a late result.
