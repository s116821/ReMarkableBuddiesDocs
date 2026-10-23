## ADDED Requirements

### Requirement: PDF text acquisition has an explicit supported profile and resource contract
The offline PDF adapter SHALL use maintained parsing code, bound original
acquisition before parsing and admitted content decoding before materialization,
and bound adapter traversal and normalized output. It SHALL distinguish these
controls from postparse eligibility checks and SHALL NOT claim hard process-wide
CPU, RAM or blocking-reader deadlines. Unsupported mappings/fonts/content,
encryption, malformed or exhausted input SHALL refuse the whole document without
external-resource access, text-skipping fallback or partial-success output.

#### Scenario: Unsupported or amplified font mapping
- **WHEN** a PDF contains unsupported font resources or an oversized declared ToUnicode range
- **THEN** the initial simple-font profile refuses before font-map expansion and does not return supported text from a partially accepted page.

#### Scenario: Malformed or exhausted source
- **WHEN** original bytes, admitted decoded content, page structure, content state or normalized text exceeds a declared limit, or strict parsing fails
- **THEN** normalization refuses without external fetching or publishing an incomplete normalized document.

### Requirement: PDF page text preserves original identity and ordered provenance
The adapter SHALL produce the existing normalized-source contract with exact
original-byte digest and a fixed extractor-profile revision, one ordered unit per
declared page and positive one-based page ordinals. It SHALL retain and report
textless pages, refuse entirely textless documents, preserve supported Unicode and
explicit lexical boundaries, and imply neither OCR/layout fidelity nor Reader or
native authority. Existing index/cache identity checks SHALL remain applicable.

#### Scenario: Ordered supported text and textless pages
- **WHEN** object order differs from page-tree order and supported text pages surround a blank or image-only page
- **THEN** actual index queries preserve declared page ordinals, the textless page remains represented, and supported Unicode and text boundaries remain searchable.

#### Scenario: Changed source and stale derived material
- **WHEN** original PDF bytes or extractor/normalized identity changes
- **THEN** the derived key changes and the existing index/cache refuses stale expected keys, independently of Reader/native freshness.
