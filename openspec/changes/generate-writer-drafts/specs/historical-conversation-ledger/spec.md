## MODIFIED Requirements

### Requirement: Retain complete source evidence and historical capture facts
The library SHALL retain every ordered source image and required native-parent
image with exact bytes, digest, dimensions, crop/transform and recorded observation
provenance. It SHALL also retain explicitly supplied normalized text as its own
immutable typed Source record with exact ordered text, locations, source and
normalized digests, and extractor revision; these SHALL NOT imply original-byte,
OCR or native qualification. It SHALL validate complete required content before
publication/readback, distinguish unavailable required committed content from
explicitly omitted imported media, and retain references after logical deletion.
Existing Source1 image/capture serialization SHALL remain unchanged; new
normalized-text Source records SHALL use explicit domain 2 with schema/shape
validation. Source: REM-37 all-screenshots/provenance/coordinates requirements;
accepted historical and SDK regressions; bounded REM-23 supplied-text consumer.

#### Scenario: Prepared image readback
- **WHEN** a valid ordered image request or synthetic SDK capture is persisted and reopened
- **THEN** original and parent bytes, ordering and historical facts read back exactly without recapture or a native effect.

#### Scenario: Corruption and omission
- **WHEN** image decoding/geometry is invalid, required committed content is corrupt, or imported coverage explicitly omits media
- **THEN** invalid publication or complete-context claims refuse, while declared omission remains distinguishable from corruption and retained historical text remains inspectable where permitted.

#### Scenario: Normalized text survives restart
- **WHEN** a Writer request with explicit normalized source text is persisted and reopened
- **THEN** exact supplied unit order, text, page/section locations and digest/revision facts remain available through its linked Source record without a synthetic image or native observation claim.
