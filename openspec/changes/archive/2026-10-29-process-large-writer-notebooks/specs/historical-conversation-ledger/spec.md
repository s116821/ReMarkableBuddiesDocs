## MODIFIED Requirements

### Requirement: Retain complete source evidence and historical capture facts
The library SHALL retain every ordered source image and required native-parent
image with exact bytes, digest, dimensions, crop/transform and recorded observation
provenance. It SHALL also retain explicitly supplied normalized text as its own
immutable typed Source record with exact ordered text, locations, source and
normalized digests, and extractor revision; these SHALL NOT imply original-byte,
OCR or native qualification. It SHALL retain full image decoding and geometry
validation before publication, validate complete required content before
publication/readback, distinguish unavailable required committed content from
explicitly omitted imported media, and retain references after logical deletion.
Existing Source1 image/capture serialization SHALL remain unchanged; new
normalized-text Source records SHALL use explicit domain 2 with schema/shape
validation. Source: REM-37 all-screenshots/provenance/coordinates requirements;
accepted historical and SDK regressions; bounded REM-23 supplied-text consumer.

For explicit notebook processing, the library SHALL retain complete canonical
normalized-document JSON as required content-addressed media with a Source3
descriptor, exact typed envelope media and original source-turn linkage. Plan and
stage facts SHALL be separately typed non-visible Conversation3 records; they
SHALL NOT replace user history or become native Completed turns. Supported
historical reads/retained-media/whole owned backup and restore SHALL traverse the
complete required source and processing closure. JSON media SHALL retain its own
role without invented image dimensions or native capture qualification. Narrow
cleanup/native receiving SHALL explicitly refuse unsupported new data before
mutation/publication instead of silently ignoring references.

#### Scenario: Prepared image readback
- **WHEN** a valid ordered image request or synthetic SDK capture is persisted and reopened
- **THEN** original and parent bytes, ordering and historical facts read back exactly without recapture or a native effect.

#### Scenario: Corruption and omission
- **WHEN** image decoding/geometry is invalid, required committed content is corrupt, or imported coverage explicitly omits media
- **THEN** invalid publication or complete-context claims refuse, while declared omission remains distinguishable from corruption and retained historical text remains inspectable where permitted.

#### Scenario: Normalized text survives restart
- **WHEN** a Writer request with explicit normalized source text is persisted and reopened
- **THEN** exact supplied unit order, text, page/section locations and digest/revision facts remain available through its linked Source record without a synthetic image or native observation claim.


#### Scenario: Archived notebook after source file disappears
- **WHEN** a larger normalized input was committed, the input file disappears and its draft is refined after reopen
- **THEN** exact units, locations, digests and processing references read from committed archive media without recapture, cache fallback or changed-input substitution.

#### Scenario: Required archive or retained reference
- **WHEN** archive media is corrupt/missing, explicitly omitted on import, retained after logical deletion or shared by another retained revision
- **THEN** availability states stay distinct, complete-source/model/write claims refuse where required, and reference-safe retention never collects still-referenced bytes.

#### Scenario: Historical projection stays non-native
- **WHEN** an archive's document identity matches a native document UUID or later drafts reuse its original source
- **THEN** exact same-conversation origin linkage is required, later references remain valid without rewriting origin, and historical projection grants no native document ownership or receiving/execution permission.
