# PDF source normalization

## Purpose

Provide offline supported PDF text acquisition with explicit resource limits, whole-document refusal and ordered page provenance.

## Requirements

### Requirement: PDF text acquisition has an explicit supported profile and resource contract
The offline PDF adapter SHALL use maintained parsing code, bound original
acquisition before parsing and admitted content/map decoding before materialization,
and bound adapter traversal, declared mapping expansion and normalized output. It
SHALL distinguish these controls from postparse eligibility checks and SHALL NOT
claim hard process-wide CPU, RAM or blocking-reader deadlines. Unsupported maps/
fonts/content, encryption, malformed or exhausted input SHALL refuse the whole
document without external-resource access, guessed/replacement text, text-skipping
fallback or partial-success output. An explicit horizontal Type0 Identity-H profile
with fixed two-byte codes and bounded ToUnicode semantics MAY supplement the
existing simple-font profile through the same maintained typed parser pipeline;
unadmitted eager mapping constructors and font-program decoders SHALL NOT be used.

#### Scenario: Unsupported or amplified font mapping
- **WHEN** a PDF contains an unsupported font/map or a declared mapping range exceeding the remaining per-map/document allowance
- **THEN** the adapter refuses before that range is expanded and does not return text from a partially accepted page or silently fall back to a simple encoding.

#### Scenario: Malformed or exhausted source
- **WHEN** original bytes, admitted decoded content/maps, page/font/mapping structure, adapter work, content state or normalized text exceeds a declared limit, or strict parsing fails
- **THEN** normalization refuses without external fetching or publishing an incomplete normalized document.

#### Scenario: Declared Unicode and repeated resources
- **WHEN** an admitted Type0 font supplies complete unambiguous bounded UTF16-BE mappings for its fixed-width shown codes and repeats the same resource references across pages
- **THEN** Unicode text flows through the existing bounded text path, resource validation reuses the immutable per-document references, and unsupported/unknown/truncated codes refuse rather than becoming replacement characters.

### Requirement: PDF page text preserves original identity and ordered provenance
The adapter SHALL produce the existing normalized-source contract with exact
original-byte digest and a fixed extractor-profile revision, one ordered unit per
declared page and positive one-based page ordinals. It SHALL retain and report
textless pages, refuse entirely textless documents, preserve supported Unicode and
explicit lexical boundaries, and imply neither OCR/layout/visible-glyph fidelity
nor Reader/native authority. Existing index/cache identity checks SHALL remain
applicable. The Unicode profile SHALL use a new fixed extractor revision for fresh
normalization rather than relabeling old derived material.

#### Scenario: Ordered supported text and textless pages
- **WHEN** object order differs from page-tree order and supported simple/Unicode text pages surround a blank or image-only page
- **THEN** actual index queries preserve declared page ordinals and exact normalized UTF8 ranges, the textless page remains represented, and supported Unicode and text boundaries remain searchable without a rendering claim.

#### Scenario: Changed source and stale derived material
- **WHEN** original PDF bytes or extractor/normalized identity changes, including adoption of the declared Unicode profile
- **THEN** the derived key changes and existing index/cache refuses stale expected keys, independently of Reader/native freshness, without upgrading old derived entries in place.
