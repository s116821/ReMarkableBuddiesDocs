# Historical notebook page-image normalization

## Purpose
Provide explicit bounded transcription of declared historical PNG page sets into
the existing Index and owned cache, retaining exact page mapping and visible
unverified OCR/profile origin. A model transcribed status does not independently
verify recognition accuracy. The complete [versioned normalization design](../../changes/archive/2026-10-25-normalize-notebook-page-images/design.md)
defines image-set identity, resource and response bounds, temporary engine
ownership, cooperative cancellation and separate local/hosted evidence. This
does not acquire native notebooks, activate installed Reader behavior or complete
handwriting reliability and native/runtime qualification.

## Requirements

### Requirement: Explicit bounded historical notebook image normalization
The notebook adapter SHALL consume only an explicit ordered bounded set of
caller-declared historical PNG pages through a caller-selected existing LLMEngine,
validate complete images before dispatch, perform at most one invocation and
admit only a strict complete page-correlated transcription. It SHALL preserve
model-declared blank/uncertainty distinctions, refuse any unreadable page without
partial success, bound complete encoded inputs/outputs and retain visible
unverified OCR/profile origin. It SHALL NOT imply native notebook acquisition,
freshness, completeness, independently verified transcription or runtime authority.

#### Scenario: Original image identity and changed material
- **WHEN** declared PNG bytes, reading order, page mapping, extraction profile or admitted normalized text changes
- **THEN** the applicable complete IndexKey changes, with the source digest explicitly identifying the versioned historical image set rather than native notebook-file bytes.

#### Scenario: Invalid or incomplete recognition
- **WHEN** image/container/decode/resource admission fails, response shape or page correlation is malformed, a page is unreadable or a complete byte budget cannot fit
- **THEN** normalization refuses without a successful partial document, cache write or source mutation, and errors do not expose content or provider bodies.

### Requirement: Scoped engine ownership and cooperative cancellation
The adapter SHALL own and clear temporary engine content before fallible work and
on every exit, pass exact original admitted PNGs with stable instructions and
ordered manifest, and latch progress failures before accepting a result. It SHALL
NOT claim hard preemption of arbitrary engines or physical/remote erasure.

#### Scenario: Cancellation and temporary content
- **WHEN** admission, execution, strict response handling, callback cancellation or unwinding ends an attempt
- **THEN** temporary text/images are cleared under the existing engine contract, no latched or late cancellation returns success and no hidden repair/retry is dispatched.

### Requirement: Actual index and owned-cache consumption retains OCR provenance
The maintained caller SHALL exercise the actual OCR-to-Index-to-owned-cache
reopen/query path using an independently retained exact key, preserving image-set
identity, unverified profile and exact original page/normalized UTF8 ranges. Local
controls and genuine historical handwriting model observations SHALL be recorded
separately with inspected accuracy limits, without upgrading either to native or
installed Reader qualification.

#### Scenario: Reopened retrieval and stale key
- **WHEN** a successful historical transcription is indexed, cached, reopened and queried, or its expected key becomes stale
- **THEN** exact-key retrieval retains declared page/range and visible unverified origin, while stale identity refuses and failed replacement preserves accepted material.

#### Scenario: Genuine handwriting evidence
- **WHEN** a fixed legally reusable genuine handwriting fixture is evaluated through the maintained model/Index/cache consumer
- **THEN** original/conversion bytes, attribution, independently inspected reference facts, actual returned text and page/range correlations are retained, with recognition errors and narrow qualification limits stated explicitly.
