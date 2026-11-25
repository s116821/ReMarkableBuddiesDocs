## ADDED Requirements

### Requirement: Installed Writer-only gestures honor the enabled modules

An ordinary local Writer-only service SHALL listen on its qualified installed output profile. It SHALL admit a released blank-start gesture without calling a model. A corner release SHALL admit a queued refinement only for the current service activation, operation, draft, document and page. On installations that support generation from the current circled target, it SHALL also accept the selected generation request for that page. Each action SHALL apply at most once to the request selected by the release. A disabled Reader SHALL never receive a fallback request. A disabled Writer SHALL never receive either Writer action.

#### Scenario: Start a blank conversation with only Writer enabled

- **WHEN** the user completes the three-finger blank-start gesture on a qualified page
- **THEN** Buddy opens or reuses its blank conversation through the installed page owner without recording a fabricated turn

#### Scenario: The existing queued path finds no matching Writer request

- **WHEN** Reader is disabled and the existing queued input path finds no eligible Writer request on this page
- **THEN** the queue check claims no request, calls no model, and changes no page. A request for another page remains queued for its intended page. The ordinary installed service passes the unqueued submission to shared source intake for classification.

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

### Requirement: Shared source submission supports an explicit circled-only note

The ordinary installed Writer SHALL accept an explicit request for the circled scope from the shared lower-right submission. It SHALL bind validated geometry to that submission's captured source, preserve the exact handwritten request in one Writer turn, and use the masked region for recognition. Its draft SHALL carry the existing About and region provenance and use guarded placement on the adjacent Buddy page.

#### Scenario: First circled note in a one-page notebook

- **WHEN** the user circles part of a fresh source page and requests a note for that part using one lower-right submission
- **THEN** Writer generates from the masked region and places a draft in the adjacent Buddy conversation without a preloaded command or earlier Reader request.

#### Scenario: Missing or ambiguous circled selection

- **WHEN** the user requests a circled-only note and the submission has no unambiguous bounded region
- **THEN** Buddy does not fall back to a current-page note and invokes no destination.

#### Scenario: The circled source changes during the action

- **WHEN** the request is canceled or the source identity or order changes before generation or draft placement
- **THEN** Buddy stops the remaining work and submits no draft to a different page

### Requirement: Whole-notebook Writer requires complete ordered source coverage

The shared source submission SHALL retain the exact wording and whole-notebook scope of an explicit notebook note request. The service SHALL admit notebook Writer generation only with a supported acquisition result that covers every original source page in order for the same notebook, including blank pages, and distinguishes verified Buddy output pages. It SHALL require source-owner evidence that pairs the independently observed whole saved-source revision with the digest of the exact ordered images acquired from that revision.

The persisted notebook producer SHALL independently bind admitted native order and original page identities to exact saved scene bytes and the resolved layout and template inputs. It SHALL exclude a page from the source only with a matching Buddy ownership receipt. An absent scene SHALL produce unavailable unless a qualified source positively establishes that the original is blank. A saved-byte revision SHALL confer no permission to generate from incomplete rendering.

#### Scenario: A complete ordered acquisition is supplied

- **WHEN** the receiver has verified the notebook identity, original page order, full-page image for each original and the identities of Buddy output pages
- **THEN** it SHALL normalize the original images in native page order, retain empty transcriptions at their original page positions, and bind the normalized source to the observed order and image digests.
- **AND** it SHALL use the original request and the existing notebook runner with a fresh draft publication. A missing, reordered or unreadable original page SHALL stop generation.

#### Scenario: More originals are available than one OCR request can hold

- **WHEN** a supported whole notebook has more than four originals and fits the aggregate acquisition and notebook planning budgets
- **THEN** the service SHALL use successive bounded OCR requests while preserving every original's native position, including blanks and gaps occupied by verified Buddy output.
- **AND** the service SHALL pass the complete ordered transcript to one existing map/reduce plan. A failed later OCR request or an exceeded aggregate budget SHALL stop Writer generation without publishing a partial draft.

#### Scenario: An earlier acquisition is supplied after another original page is edited

- **WHEN** the current page and native page order are unchanged but another original page's saved scene or layout assets change
- **THEN** the receiver SHALL decline the earlier acquisition before OCR if the change is already observed and stop before draft publication if the change is observed during processing. A substitute image with the same page ID SHALL fail the sealed image digest check before OCR.
- **AND** content changes confined to pages already verified as Buddy output SHALL leave the saved-source revision unchanged. A change to native order remains subject to the order guard.

#### Scenario: The open page changes during notebook generation

- **WHEN** the live resident observation no longer matches the captured document, current page or order, even when all original scenes and paper assets have the same saved revision
- **THEN** the service SHALL decline further provider calls or draft publication at the next operation boundary. It SHALL consult the live visit and the saved revision independently.

#### Scenario: The supported handwriting contains a punctuation dot

- **WHEN** a black fineliner stroke is a single sample or repeated stationary samples within the supported canvas
- **THEN** the renderer SHALL preserve the dot on the complete page image.

#### Scenario: A saved page uses a feature outside the supported renderer

- **WHEN** any original page cannot be completely rendered within the bounded profile, including an unverified template, unsupported content or an extent that exceeds the budget
- **THEN** the notebook request SHALL stop before OCR or placement. A supported empty scene SHALL keep its original position as a blank source unit.

#### Scenario: Saved handwriting uses ordinary RM2 pens and colours

- **WHEN** an original on verified white paper contains stock pen, pencil, highlighter or brush strokes across visible flat layers
- **THEN** Writer SHALL render the recorded colours, paint order and full stroke extent into the original page's image, including pages saved with the standard RM2 portrait layout.
- **AND** an ambiguous layer or stroke order, an unrenderable edit or a stroke extending beyond the allowed canvas SHALL stop acquisition of the notebook before draft generation.

#### Scenario: An original uses a pinned patterned paper asset

- **WHEN** an original has a supported pinned stock-paper asset and a nominal portrait canvas
- **THEN** the saved-source revision SHALL bind the exact template bytes. Writer SHALL render the user's saved strokes at native scale on a plain canvas for OCR, without template headings, ruling, or other printed artwork.
- **AND** a verified empty scene SHALL keep its original slot as blank, and admitted white strokes on patterned paper SHALL be rendered with a contrasting plain canvas.
- **AND** malformed, unsupported or mismatched template variants and patterned pages requiring a larger canvas SHALL stop acquisition before OCR.

#### Scenario: The installed service has only the open window

- **WHEN** the handwritten request asks for a whole-notebook note and no complete ordered source is available
- **THEN** the service reports unavailable notebook coverage before generation. It performs no page navigation, draft placement, or destination action and does not substitute a page-only note.

#### Scenario: Original pages contain diagrams and writing

- **WHEN** a sealed original page contains a drawing or image region, with or without writing
- **THEN** ordinary notebook Writer SHALL pass useful visible observations with original page provenance into the existing note planner, separately from any verbatim user writing
- **AND** the planner SHALL preserve their unverified observational status in summaries and the draft

#### Scenario: Confirmed handwriting examples apply across a complete notebook

- **WHEN** the active handwriting profile supplies confirmed examples for a whole-notebook note
- **THEN** Writer SHALL use one selection for reading handwriting in every OCR batch, exclude examples with the same PNG digest as any original in the notebook, and distinguish the examples from the target pages and drawing evidence.
- **AND** only the original pages SHALL contribute content to the note. The normalized source SHALL identify the correction revisions used. A disabled profile or empty selection SHALL preserve the original OCR request and unpersonalized extractor identity.

#### Scenario: Blank or unreadable original

- **WHEN** a page is genuinely blank
- **THEN** the producer SHALL preserve its ordinal as an empty unit
- **AND** an unreadable page or an extraction that falsely declares a marked page blank SHALL stop before notebook planning

### Requirement: Explicit whole-notebook saves retain the draft and reuse the note

The ordinary installed Writer SHALL route an explicit request to save a note from the whole notebook through complete ordered notebook generation and the configured note destination. It SHALL publish the readable draft before export and use the existing guarded export selection and journal. A normal save SHALL use the notebook identity for correlation. An explicitly separate note SHALL use its own correlation. An unresolved earlier save or a changed destination for the same correlation SHALL prevent a new association. The live capture, saved originals and destination configuration SHALL be current before writing.

#### Scenario: Save the notebook to the configured destination

- **WHEN** a clear handwritten save requests the whole notebook and complete acquisition succeeds
- **THEN** Buddy saves from the entire ordered set of originals, excludes Buddy output pages, and reports the verified destination result with the retained draft.

#### Scenario: Retry or save a separate note

- **WHEN** the user issues an ordinary save again for the same notebook
- **THEN** Writer uses the original association, or reports unresolved ownership or delivery. An explicit request for a separate note uses a distinct association.

#### Scenario: The destination is unavailable or the write is uncertain

- **WHEN** the destination is disabled or unavailable, the guarded source or destination changes, or a possible write cannot be verified
- **THEN** Writer preserves the draft, blocks unsafe writes or retries and reports the appropriate result when the current page can still be used for guarded presentation.

#### Scenario: Draft only

- **WHEN** the notebook request asks for a draft without authorizing an external save
- **THEN** Writer generates and presents the draft without invoking the destination.
