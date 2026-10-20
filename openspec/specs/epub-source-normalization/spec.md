# EPUB source normalization

## Purpose

Provide bounded offline EPUB text acquisition with explicit reading order, provenance and unsupported-input refusal.

## Requirements

### Requirement: EPUB text acquisition is bounded before normalization
The offline adapter SHALL bound original acquisition, ZIP metadata reads and I/O,
decompression, XML depth/events and normalized output before accepting a source.
It SHALL use maintained parsers, avoid extraction/network access and return no
partial document after malformed, unsupported or exhausted input.

#### Scenario: Oversized or ambiguous archive
- **WHEN** an archive exceeds a declared bound or contains duplicate/unsafe/encrypted/unsupported structure
- **THEN** normalization refuses without reading external content or publishing a partial normalized source.

### Requirement: Declared reading order and source identity remain explicit
The adapter SHALL follow the default OCF package and its complete declared spine,
including auxiliary items, preserve canonical section locations and original-byte
digest, and report textless units without inventing page, OCR or native authority.

#### Scenario: Manifest and spine differ
- **WHEN** supported XHTML entries have a declared spine order different from manifest or filename order
- **THEN** normalized units and actual index passages preserve spine order and exact section provenance.

#### Scenario: Textless or changed source
- **WHEN** a section has no extracted body text or original EPUB bytes change
- **THEN** the section is explicitly reported and the source identity changes; an entirely textless input refuses and no image/layout/native claim is inferred.
