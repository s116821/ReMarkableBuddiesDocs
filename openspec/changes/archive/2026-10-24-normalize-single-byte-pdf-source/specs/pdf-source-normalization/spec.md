## MODIFIED Requirements

### Requirement: PDF text acquisition has an explicit supported profile and resource contract
The offline PDF adapter SHALL use maintained parsing code, bound original
acquisition before parsing and admitted content/map decoding before materialization,
and bound adapter traversal, declared mapping expansion and normalized output. It
SHALL distinguish these controls from postparse eligibility checks and SHALL NOT
claim hard process-wide CPU, RAM or blocking-reader deadlines. Unsupported maps/
fonts/content, encryption, malformed or exhausted input SHALL refuse the whole
document without external-resource access, guessed/replacement text, text-skipping
fallback or partial-success output. Explicit Type0 Identity-H/two-byte and simple
TrueType WinAnsiEncoding/one-byte profiles MAY supply bounded ToUnicode semantics
through the same maintained typed parser pipeline. Map source width SHALL match
its admitted font and immutable-reference cache entry; unadmitted eager mapping
constructors and font-program decoders SHALL NOT be used.

#### Scenario: Unsupported or amplified font mapping
- **WHEN** a PDF contains an unsupported font/map or a declared mapping range exceeding the remaining per-map/document allowance
- **THEN** the adapter refuses before that range is expanded and does not return text from a partially accepted page or silently fall back to a simple encoding.

#### Scenario: Malformed or exhausted source
- **WHEN** original bytes, admitted decoded content/maps, page/font/mapping structure, adapter work, content state or normalized text exceeds a declared limit, or strict parsing fails
- **THEN** normalization refuses without external fetching or publishing an incomplete normalized document.

#### Scenario: Declared Unicode and repeated resources
- **WHEN** an admitted font supplies complete unambiguous bounded UTF16-BE mappings for its fixed-width shown codes and repeats the same resource references across pages
- **THEN** Unicode text flows through the existing bounded text path, resource validation reuses immutable per-document references with the same source width, and unsupported/unknown/truncated codes refuse rather than becoming replacement characters.

#### Scenario: Single-byte font metadata and width ambiguity
- **WHEN** a simple TrueType font supplies explicit one-byte ToUnicode and bounded matching descriptor/character-width metadata, or shares a map with an incompatible two-byte font
- **THEN** the closed valid profile is searchable with existing page/range provenance, while invalid metadata, out-of-font-range entries and width conflicts refuse the whole document without fallback or duplicate map decoding.
