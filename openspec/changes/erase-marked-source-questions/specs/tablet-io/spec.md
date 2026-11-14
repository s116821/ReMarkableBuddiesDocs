## ADDED Requirements

### Requirement: A source-question erase is a guarded original effect

Before navigation loses the source visit, the ordinary Reader SHALL submit erasure only for the freshly acknowledged marked-question region while its original operation and source document, page, session and visit remain current in the captured viewport. The actual backend handoff SHALL revalidate the live owner and qualified effect mapping. The effective footprint SHALL affect only the admitted question ink and preserve underlying content, circles, highlights and neighboring notes. Unsupported or inactive guards, absent source or viewport authority, and ambiguous or overlapping footprints SHALL refuse the effect. Source: ordinary `RequestGuard`, the source capture owner and the bounded Reader erase effect.

#### Scenario: One eligible source-region effect

- **WHEN** the original source request, capture-bound viewport and qualified footprint remain current through submission
- **THEN** Reader consumes one original erase attempt before navigation and limits actual effect calls to the exact admitted question region
- **AND** the underlying source and surrounding editable ink remain intact

#### Scenario: Changed source or unsupported footprint

- **WHEN** an installed route lacks a qualified capture-to-viewport mapping or effect footprint, the original page/visit changes, or the footprint could hit a protected stroke
- **THEN** Reader makes no erase submission, with no broader or unguarded fallback

#### Scenario: Uncertain or partial erase

- **WHEN** a submitted erase may have taken effect and the operation cannot verify its original result
- **THEN** Reader reports an uncertain outcome and stops remaining erase work without automatic retry
- **AND** subsequent inspection may address only the original effect and cannot authorize another submission

#### Scenario: Installed qualification

- **WHEN** an installed implementation is qualified for a supported source kind
- **THEN** its evidence demonstrates current source and viewport admission, the real footprint, persisted source and neighbor preservation, and refusal or uncertainty after interruption
- **AND** scripted or simulated results alone do not qualify installed support
