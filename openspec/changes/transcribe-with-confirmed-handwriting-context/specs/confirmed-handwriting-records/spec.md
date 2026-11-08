## MODIFIED Requirements

### Requirement: Explicit confirmed samples remain distinct from inference

The component SHALL offer an explicitly invoked offline typed correction provider
and one-shot transport, retaining exact bounded sample PNG bytes, original text,
confirmed replacement and asserted provenance in the existing Handwriting domain.
Only explicit caller confirmation SHALL create/update a correction. The transport
SHALL validate strict bounded JSON/base64/image data before admission, preserve
Unicode text and distinguish caller-asserted source links from verified ownership.
No canceled/uncertain model output, refinement or export SHALL imply confirmation.
The custody-checked typed Writer enrollment path SHALL allow an explicit user
transcription after valid WholePage abstention to retain null original text and
distinct abstention provenance. The version-one public request SHALL continue
to require a nonempty original and legacy provenance.

#### Scenario: Confirmed Unicode correction
- **WHEN** a caller explicitly confirms a valid bounded sample/text pair and later reopens the Store
- **THEN** the exact original bytes, texts and asserted provenance remain readable without recapture, model training or fabricated native authority.

#### Scenario: Unconfirmed or malformed input
- **WHEN** confirmation is absent, data is malformed/duplicated/oversized or image decoding exceeds admitted format/dimension/pixel bounds
- **THEN** the command refuses before correction admission without model/device startup, path fallback or a learned-example claim.

#### Scenario: Custody-checked enrollment after abstention
- **WHEN** the typed Writer owner submits explicit user confirmation bound to valid abstention and the exact current retained image
- **THEN** the existing correction publisher retains the confirmed text and image with null original and distinct provenance, preserving immutable lineage and replay.
