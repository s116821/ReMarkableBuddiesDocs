## ADDED Requirements

### Requirement: Installed Writer-only gestures honor the enabled modules

An ordinary local Writer-only service SHALL listen on its qualified installed output profile. It SHALL admit a released blank-start gesture without calling a model. A corner release SHALL only run Writer when a pending refinement for the same service activation, operation, draft, document and page remains eligible. A disabled Reader SHALL never receive a fallback request. A disabled Writer SHALL never receive a refinement.

#### Scenario: Start a blank conversation with only Writer enabled

- **WHEN** the user completes the three-finger blank-start gesture on a qualified page
- **THEN** Buddy opens or reuses its blank conversation through the installed page owner without recording a fabricated turn

#### Scenario: Corner hold without a matching Writer request

- **WHEN** Reader is disabled and the released corner hold has no eligible refinement on this page
- **THEN** Buddy stays available without a model call or a page mutation, and a request for another page remains available for its intended page

#### Scenario: Refine the current draft with only Writer enabled

- **WHEN** a pending refinement is selected by a corner release on its named page and still matches the activation, operation, draft and expiry at consumption
- **THEN** the existing Writer receiver processes the request once

#### Scenario: Reader-only or unsupported installation

- **WHEN** Writer is disabled or the installed Writer input profile is unavailable
- **THEN** Buddy refuses Writer input and preserves the supported Reader behavior
