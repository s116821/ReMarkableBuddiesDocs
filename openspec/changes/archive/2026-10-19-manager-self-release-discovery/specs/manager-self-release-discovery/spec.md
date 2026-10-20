## ADDED Requirements

### Requirement: Independent Manager stable metadata discovery
The shared Manager UI SHALL refresh its own official stable release metadata independently from Buddy's existing stream using fixed repository identities and the current compiled build identity.

#### Scenario: Stable release changes while the app runs
- **WHEN** Manager's upstream stable tag changes and a refresh or scheduled poll completes
- **THEN** both UI editions display the new Manager candidate without restarting or altering Buddy's state

#### Scenario: Repository or preview mismatch
- **WHEN** metadata belongs to the other repository, is draft/pre-release or lacks the expected Manager assets
- **THEN** Manager refuses identity or shows incomplete availability and grants no download/update authority

### Requirement: Honest and separate preview states
Manager SHALL keep stream failures/backoff/preferences separate and preserve current build and prior successful candidate with explicit stale/unknown status.

#### Scenario: One repository rate limits or fails
- **WHEN** a Manager request fails while Buddy succeeds
- **THEN** Manager's failure/stale state does not suppress or rewrite Buddy's state or stored source preference

#### Scenario: Development build or unverified assets
- **WHEN** current build is untagged development or only asset metadata is observed
- **THEN** the UI does not infer upgrade ordering, compatibility or completed installation and leaves updater/download qualification open
