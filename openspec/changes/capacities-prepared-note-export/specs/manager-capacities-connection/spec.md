## ADDED Requirements

### Requirement: Capacities consent uses the existing settings workflow and verified public client

Manager SHALL provide Capacities connection controls beside the existing Reader/Writer destination setting in browser and Electron. It SHALL use a maintainer-registered public OAuth client, S256 and one-use state, exact registered loopback redirect, validated provider metadata and the required API resource/scopes. Ordinary users SHALL sign in with their own Capacities account without registering an application or supplying a personal API token. Missing registration SHALL leave consent unavailable without substituting another client's registration.

#### Scenario: Consent succeeds on either Manager host

- **WHEN** the user starts consent for the selected tablet and completes the provider's space selection
- **THEN** the host validates the original one-use callback and transfers code/verifier only through the identity-bound confidential tablet command.
- **AND** the application renderer receives only sanitized pending or connection state and, in the browser, an opaque local launch ticket, never credentials, provider authorization parameters or callback secrets.

#### Scenario: Callback is stale, duplicated, denied or malformed

- **WHEN** the original flow has expired, changed or been canceled, or callback identity and shape fail validation
- **THEN** no code exchange is authorized and the UI reports the corresponding bounded result.

#### Scenario: Browser windows or cancellation overlap

- **WHEN** a delayed popup, status or cancellation belongs to an earlier browser launch
- **THEN** it cannot consume, confirm or cancel a newer launch; each owned request correlates to its original local ticket.
- **AND** closing the pending Begin response before it finishes cancels that pending host flow; after publication, cancellation uses only the original ticket.

#### Scenario: Connection belongs to another tablet or earlier Manager session

- **WHEN** a global connection status cannot be associated with the current observed tablet and the original consent attempt
- **THEN** Manager presents it as historical rather than claiming the selected tablet is configured.
- **AND** it preserves original uncertain exchanges and allows a distinct eligible tablet to start its own consent after earlier custody is settled.

### Requirement: Confidential handoff uses current existing tablet identity

The host SHALL capture the existing tablet actor, boot and durable saved configuration digest through a bounded read-only protected command without creating state, returning raw configuration or contacting the provider. Immediately before confidential handoff it SHALL validate that original identity and the fixed installed executable on the same wired transport. The code and verifier SHALL travel only through stdin, and the private host port SHALL allow at most one possible exchange for the original binding. Receipt parsing SHALL require settled streams and exact identity rather than a temporarily empty receive buffer.

#### Scenario: Tablet identity or available time changes before handoff

- **WHEN** the actor, boot, connection, configuration or executable no longer matches, or the original allowance cannot contain the full actor operation and postflight reserve
- **THEN** no confidential bytes are sent and the flow reports a bounded refusal.
- **AND** neither a currentness check nor a new phase clock renews the original consent lifetime.

#### Scenario: Existing tablet state cannot be captured

- **WHEN** compatible saved configuration or Store identity is absent or cannot be proven
- **THEN** capture reports unresolved without manufacturing a new actor or configuration.

### Requirement: The tablet exclusively owns OAuth lifecycle and uncertain handoff

The tablet SHALL be the sole token redeemer, credential store, refresh owner and revoker for its enrollment. Its bounded one-use exchange SHALL bind the original tablet, connection, boot, configuration revision, grant and operation. It SHALL durably record possible exchange before network dispatch, verify granted space and scope, publish credentials privately and commit the configuration pointer last. Unknown delivery SHALL reconcile only the original operation and SHALL NOT replay a code or infer success from a local acknowledgment.

#### Scenario: Exchange or configuration publication is interrupted

- **WHEN** the response or final install acknowledgment is lost
- **THEN** status distinguishes the exact committed grant/config pair, a verified staged grant awaiting the same local commit, and unresolved exchange.
- **AND** unresolved exchange does not replay OAuth or authorize export through an uncommitted enrollment.

#### Scenario: A later status sees no grant after an uncertain handoff

- **WHEN** confidential bytes may have been sent and the original invocation has no settled terminal receipt
- **THEN** a later absent-grant status does not clear uncertainty or authorize another exchange.
- **AND** the host retains the original binding because the original process may not yet have published its durable fence.

#### Scenario: Refresh outcome is uncertain

- **WHEN** a rotating refresh may have been consumed without durable replacement token bytes
- **THEN** the grant remains fenced for reconnect and neither CLI nor daemon retries the old token or borrows another enrollment.

#### Scenario: Disconnect or replacement consent

- **WHEN** the user disconnects or reconnects
- **THEN** local-use disabling and remote revocation are reported separately; replacement consent receives a new grant identity.
- **AND** an unknown export retains its original provider/space/enrollment, and uncertain revocation is not reported as confirmed removal.

#### Scenario: A connection changes after Manager checks it

- **WHEN** a user requests Disconnect using an earlier checked connection
- **THEN** the host consumes only that check's opaque reference and the tablet verifies the exact grant revision and original saved configuration before mutation.
- **AND** a stale or consumed reference cannot disable a replacement enrollment.

#### Scenario: Disconnect disables local access but provider removal is uncertain

- **WHEN** durable original pending-revocation evidence proves local disablement without proving provider removal
- **THEN** Manager reports those results separately and clears its earlier positive connected indication.
- **AND** subsequent Check reads only the recorded original operation, including after Manager restart, without replaying Disconnect.
