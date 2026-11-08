## ADDED Requirements

### Requirement: Circled-only retained-source generation
The existing stored-target Writer command SHALL resolve exact ready target/frame/media, derive the deterministic original-frame region mask, normalize it through the existing complete-image handwriting path with one frozen context, and retain RegionSource proof. Only regional source units SHALL constitute requested coverage. Refine SHALL retain the draft original target/version after later retarget.

#### Scenario: Missing or partial regional source
- **WHEN** promised original media is missing or region normalization is partial/unreadable/refused
- **THEN** no complete regional draft/model fallback is admitted.
