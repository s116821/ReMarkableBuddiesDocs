## MODIFIED Requirements

### Requirement: Explicit shared saved-only configuration view
Both companions SHALL offer explicit bounded inspection through the exact producer
contract, show safe saved declarations and their origins, and keep runtime/provider/
root/credential validity unverified. Inspection SHALL NOT grant settings mutation,
active mode, reload or service authority; absent schema settings remain explicit gaps.
The report SHALL be available under Troubleshooting rather than duplicating normal
settings. Schema gaps and technical origins belong in that report; normal controls
must still distinguish saved state from effective runtime behavior.

#### Scenario: Deliberate saved snapshot
- **WHEN** an admitted observed target is explicitly inspected
- **THEN** both hosts show the same validated safe fields/origins and unverified-runtime/path explanation without automatic inspection or raw JSON.

#### Scenario: Unsupported setting or runtime override
- **WHEN** a setting is not represented by the saved schema or runtime/environment may override it
- **THEN** the view shows the explicit schema gap or saved-only value and never invents a false default, effective model or active service/provider state.
