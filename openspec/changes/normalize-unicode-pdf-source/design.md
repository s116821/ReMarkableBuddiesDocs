# Bounded declared Unicode PDF profile

## Existing owner and parser

Extend retrieval::pdf, not a second normalizer. Keep normalize(document_uuid, Read),
PdfText, page units, original-byte SHA256 and normalized/index/cache schemas. Keep
the pinned lopdf0.46.0 dependency/features, strict loader, page tree, bounded stream
decoder and content-state machine. The existing simple Type1 branch and its trusted
literal OneByteEncoding getter remain unchanged in behavior. Its rejection of
ToUnicode/FontDescriptor/DescendantFonts/CharProcs remains valid.

The local pinned ToUnicodeCMap constructor eagerly enumerates ranges for a reverse
map; its convenience string decoder uses replacement fallbacks. Do not feed input
font dictionaries to get_font_encoding or invoke those CMap constructors. Reuse
Content::decode_strict for a bounded ToUnicode stream's typed Object/Operation AST,
then validate this closed grammar and build only the bounded forward lookup. No
PDF/PostScript lexer, interpreter or alternate parsing dependency is introduced.
AST eligibility follows maintained parsing; it is not a preallocation claim.
The authored parser-only probe preserves complete wrapper/metadata/mapping
operations and hexadecimal versus literal StringFormat, but it also demonstrates
normalization: odd hex digits are padded by the maintained parser (`<001>` and
`<0010>` both yield bytes0010), and duplicate raw dictionary keys collapse to the
last value. Source/target widths below refer to decoded bytes. This profile does
not claim raw hex-spelling or dictionary-key uniqueness that the typed AST has
lost; ordinary parsed dictionary semantics apply without a second raw lexer.

## Font/resource admission

Add a Type0 branch alongside the existing simple branch. A Type0 page font must
be an indirect dictionary with Type=Font, Subtype=Type0, Encoding=Identity-H,
nonempty BaseFont name (at most128 bytes), an indirect ToUnicode stream and exactly
one indirect DescendantFonts dictionary. Top-level keys are limited to Type,
Subtype, BaseFont, Encoding, DescendantFonts, ToUnicode and optional Name. Require
the descendant Type=Font, Subtype=CIDFontType2 and the same BaseFont name. Vertical
Identity-V, predefined/inherited CMaps, Type3/CFF and other font kinds refuse.

The descendant admits only Type/Subtype/BaseFont/CIDSystemInfo/FontDescriptor,
DW/W and CIDToGIDMap. CIDSystemInfo has bounded Registry/Ordering byte strings
(1..128), nonnegative integer Supplement, and no other keys. It is metadata, not
permission to resolve another character collection. FontDescriptor must have
Type=FontDescriptor and matching FontName. It may contain the ordinary bounded
family/stretch/weight/flags/bbox/italic/ascent/descent/leading/cap-height/x-height/
stem/width fields, FontFile2, CharSet and CIDSet. Other descriptor keys refuse.
Numeric values must be finite; Flags/Supplement are nonnegative integers, FontBBox
has exactly four finite numbers, metadata names/strings are at most512 bytes.
FontFile2/CIDSet and stream-valued CIDToGIDMap remain opaque input-owned streams:
validate references/types and reject external F/FFilter/FDecodeParms; do not decode
or interpret their programs/glyphs. CIDToGIDMap may alternatively be Name Identity.
Font programs may be absent; no system font lookup or render fallback follows.

DW is finite numeric. W is validated as bounded CID width-array/range metadata
with CID values0..65535 and finite widths; do not expand width ranges or use them
to claim layout. Per-font W has at most8192 array items; cumulative typed metadata
work is charged before each visited item and limited to65536/document. Nested
arbitrary structures refuse. W2/DW2/vertical fields are unsupported. These checks
establish the declared profile's structure, not valid TrueType programs or full
PDF/rendering validity.

Cache validated Type0 fonts by their input indirect reference and maps by their
ToUnicode reference within this one immutable parsed document only. Repeated page
aliases reuse these values, not repeated decompression/expansion. At most64 distinct
Type0 font references and64 distinct map references are admitted per document.
Reference-chain, page-resource, source-object and original-byte limits remain in
force. No durable/shared cache or external font/CMap lookup is added.

## Closed ToUnicode grammar

The map stream admits only no filter or one FlateDecode name with no DecodeParms,
using the existing bounded decoder. Use the maintained strict AST parser over
those bounded bytes, never the upstream eager mapping constructor.
Its dictionary admits only Length/Filter and optional Type=CMap, CMapName,
CIDSystemInfo and WMode=0. Optional name/system metadata must match the parsed
declarations. UseCMap and all other keys refuse, including dictionary-based
inheritance; external F/FFilter/FDecodeParms remain refused before decoding.

Accept the ordinary complete wrapper `/CIDInit /ProcSet findresource begin`, an
integer1..64 `dict begin`, `begincmap`, metadata definitions, mapping sections,
`endcmap CMapName currentdict /CMap defineresource pop end end`. Validate exact
operand types/counts and sequence; comments/whitespace handled by the maintained
parser are allowed. Required metadata: CMapType integer2, nonempty CMapName name
at most128 bytes, and CIDSystemInfo with the bounded fields above. Optional WMode
must be integer0; optional CMapVersion is finite numeric. Duplicate metadata definition operations,
unknown operators, execution extensions, usecmap, malformed or trailing content
refuse. No PostScript operation is executed.

Require one preceding codespacerange block containing1..16 nonoverlapping ranges,
each source endpoint exactly two hexadecimal bytes. Mapping blocks use declared
counts1..100 and matching end operators/operand counts. Support:

- bfchar: exact two-byte source and nonempty hexadecimal UTF16-BE target of at
  most16 bytes, with valid surrogate pairing and permitted text scalars.
- bfrange: inclusive two-byte source endpoints in the declared codespace, paired
  with either an explicit target-string array of exactly that range length or
  a single two-byte BMP target incremented without overflow/surrogate crossing.
  Multi-unit implicit destination increments are unsupported; explicit arrays
  or bfchar handle ligatures and supplementary Unicode.

Source ranges must be ordered internally and every entry covered by a codespace.
Duplicate/overlapping mapping entries refuse, including identical duplicates.
Validate all declared counts, range lengths and remaining mapping allowances
before expansion. No guessed/replacement glyph, implicit encoding or retained
partial map is accepted. Disallowed controls, malformed UTF16, empty targets,
unknown shown codes and odd/truncated shown strings fail the whole normalization.
Targets containing the replacement scalar U+FFFD are unsupported rather than
silently treating an unknown mapping as complete text. Existing permitted tab/
newline/carriage-return scalars retain the existing whitespace normalization.
Source shown strings use exact two-byte big-endian codes; append mapped scalars
through the existing Text bounds/whitespace/boundary path. Existing Tj/TJ/quotes,
Tf/BT/ET, graphics balance and unsupported content rules remain in force.

## Additional resource contract

| Stage | Limit and enforcement |
| --- | --- |
| Distinct Unicode fonts/maps |64 of each per document, reserve before new admission; reuse immutable reference caches |
| Decoded CMap |64KiB/map,1MiB/document; reserve remaining allowance before bounded decode |
| CMap typed AST |4096 operations/map,16384/document after strict AST materialization |
| Declared mappings |4096/map,65536/document; reserve the entire source range before expanding it |
| Target text |16 UTF16-BE bytes/entry and256KiB cumulative UTF8 map text/document, checked before table append |
| Typed font metadata |8192 W items/font and65536 visited metadata items/document, charged before visits |

Keep all existing acquisition/loader/content/text limits independently. Table
lookups add no output collector: each mapped scalar/boundary reserves existing
512KiB/page and4MiB/document UTF8 before append. Eager document/object parsing and
strict AST materialization still allocate internally before eligibility checks.
These are explicit acquisition/decode/adapter-work/output controls, not process-wide
RAM/CPU/deadline guarantees or a parser sandbox.

## Identity and verification

Set extractor revision `pdf-explicit-unicode-r2-lopdf-0.46.0` for every newly
normalized PDF, including simple-only input. Original/extractor/normalized changes
retain existing stale-key semantics; old r1 derived entries are not upgraded or
rewritten as fresh. Existing public API/output shapes stay unchanged.

Author PDFs through the maintained writer: mixed simple/Type0 text, compressed maps,
reordered pages, blank/image-only units, BMP/non-Latin/math, ligatures, supplementary
Unicode, range arrays and exact UTF8 Index passage provenance. Verify matching
cached references across pages/aliases, correct source/extractor key invalidation
and no new persistent schema. Preserve existing simple-font/refusal fixtures.
Negative controls cover huge declared ranges before expansion, exact/under map and
cumulative limits, duplicate/overlapping/out-of-codespace mappings, malformed UTF16,
odd/unknown codes, invalid font metadata/references, unsupported grammar/filter/
vertical/inherited profiles and later-page failure with no partial result. Do not
silently relax old whole-document/control/visibility/encryption refusals.

Run affected real parser/Index/cache fixtures, ordinary default library check,
required formatting/strict lint/current hosted checks/cross-target pipeline and
independent source/spec/lifecycle review. No live model/native test is required
for this data-only adapter; this does not release their separate integration gates.
