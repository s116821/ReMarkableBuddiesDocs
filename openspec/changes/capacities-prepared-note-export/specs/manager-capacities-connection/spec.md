## ADDED Requirements

### Requirement: Capacities consent uses the existing settings workflow and verified public client

Manager SHALL provide Capacities connection controls beside the existing Reader/Writer destination setting in browser and Electron. It SHALL use a maintainer-registered public OAuth client, S256 and one-use state, exact registered loopback redirect, validated provider metadata and the required API resource/scopes. Ordinary users SHALL sign in with their own Capacities account without registering an application or supplying a personal API token. Missing registration SHALL leave consent unavailable without substituting another client's registration.

#### Scenario: Consent succeeds on either Manager host

- **WHEN** the user starts consent for the selected tablet and completes the provider's space selection
- **THEN** the host validates the original one-use callback and transfers code/verifier only through the identity-bound confidential tablet command.
- **AND** the application renderer receives only sanitized pending or connection state, never credentials or callback secrets.

#### Scenario: Callback is stale, duplicated, denied or malformed

- **WHEN** the original flow has expired, changed or been canceled, or callback identity and shape fail validation
- **THEN** no code exchange is authorized and the UI reports the corresponding bounded result.

### Requirement: The tablet exclusively owns OAuth lifecycle and uncertain handoff

The tablet SHALL be the sole token redeemer, credential store, refresh owner and revoker for its enrollment. Its bounded one-use exchange SHALL bind the original tablet, connection, boot, configuration revision, grant and operation. It SHALL durably record possible exchange before network dispatch, verify granted space and scope, publish credentials privately and commit the configuration pointer last. Unknown delivery SHALL reconcile only the original operation and SHALL NOT replay a code or infer success from a local acknowledgment.

#### Scenario: Exchange or configuration publication is interrupted

- **WHEN** the response or final install acknowledgment is lost
- **THEN** status distinguishes the exact committed grant/config pair, a verified staged grant awaiting the same local commit, and unresolved exchange.
- **AND** unresolved exchange does not replay OAuth or authorize export through an uncommitted enrollment.

#### Scenario: Refresh outcome is uncertain

- **WHEN** a rotating refresh may have been consumed without durable replacement token bytes
- **THEN** the grant remains fenced for reconnect and neither CLI nor daemon retries the old token or borrows another enrollment.

#### Scenario: Disconnect or replacement consent

- **WHEN** the user disconnects or reconnects
- **THEN** local-use disabling and remote revocation are reported separately; replacement consent receives a new grant identity.
- **AND** an unknown export retains its original provider/space/enrollment, and uncertain revocation is not reported as confirmed removal.
