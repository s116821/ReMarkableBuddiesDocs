## ADDED Requirements

### Requirement: Installed Writer-only gestures honor the enabled modules

An ordinary local Writer-only service SHALL listen on its qualified installed output profile. It SHALL admit a released blank-start gesture without calling a model. A corner release SHALL admit a queued refinement only for the current service activation, operation, draft, document and page. On installations that support generation from the current circled target, it SHALL also accept the selected generation request for that page. Each action SHALL apply at most once to the request selected by the release. A disabled Reader SHALL never receive a fallback request. A disabled Writer SHALL never receive either Writer action.

#### Scenario: Start a blank conversation with only Writer enabled

- **WHEN** the user completes the three-finger blank-start gesture on a qualified page
- **THEN** Buddy opens or reuses its blank conversation through the installed page owner without recording a fabricated turn

#### Scenario: The existing queued path finds no matching Writer request

- **WHEN** Reader is disabled and the existing queued input path finds no eligible Writer request on this page
- **THEN** Buddy stays available without a model call or a page mutation, and a request for another page remains available for its intended page

#### Scenario: Refine the current draft with only Writer enabled

- **WHEN** a pending refinement is selected by a corner release on its named page and still matches the activation, operation, draft and expiry at consumption
- **THEN** the existing Writer receiver processes the request once

#### Scenario: Generate a note from the current circled target

- **WHEN** the ordinary service supports generation from the current target, only Writer is enabled, and the corner release selects the queued generation for the open page
- **THEN** Writer generates its note from that target. If the request is replaced before Buddy claims it, the replacement stays queued for its own gesture.

#### Scenario: The page changes before a refinement is claimed

- **WHEN** the user changes the page or its order after Buddy selects a refinement and before it claims the request
- **THEN** Buddy leaves the refinement queued and makes no model call or subject-memory query for it

#### Scenario: Reader-only or unsupported installation

- **WHEN** Writer is disabled or the installed Writer input profile is unavailable
- **THEN** Buddy refuses Writer input and preserves the supported Reader behavior

### Requirement: The installed current-page Writer action uses its captured source

When Writer is enabled on the ordinary installed profile, an admitted current-page note action SHALL capture the open source page with the SDK and normalize its full source image. Writer SHALL generate a draft for that page through the existing Writer receiver, with its preset separate from the visible transcript. Buddy SHALL retain the document and page identity and submit the draft through the guarded placement owner for the bound conversation page. The action SHALL respect cancellation and refuse a changed source or page order before placement.

#### Scenario: Draft a note in combined or Writer-only mode

- **WHEN** a user in combined or Writer-only mode uses the lower-right hold with an explicit handwritten request for a note about the open page and the page contains readable notes
- **THEN** Writer generates from that captured page and places the draft in its Buddy conversation from the one submission. The source page ink is preserved and the ordinary path requires no queued request.

#### Scenario: The same source submission asks a reading question

- **WHEN** a user in combined mode uses the lower-right hold to ask a handwritten question about the circled content
- **THEN** Reader verifies and answers the question through its ordinary route without making a Writer draft.

#### Scenario: The source submission does not authorize creating a current-page draft

- **WHEN** a source submission is ambiguous, asks for a different note scope, or asks only to export
- **THEN** the current-page action creates no draft and invokes no destination.

#### Scenario: The source changes during the action

- **WHEN** the request is canceled or the source identity or order changes before generation or draft placement
- **THEN** Buddy stops the remaining work and submits no draft to a different page
