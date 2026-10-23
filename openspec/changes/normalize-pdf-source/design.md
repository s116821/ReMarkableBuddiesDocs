# Offline PDF supported profile

## Status and ownership
Proposed before implementation. Rust owns the adapter, authored fixtures and
development example; this central change owns its requirements. Independent
precode review precedes source changes. Source and Docs form one delivery, with
Docs first after implementation, verification, own spec sync and archive.

## Parser choice and research basis
Use lopdf =0.46.0, default features disabled: MIT, declared Rust1.88 (below the
application's1.96), pure Rust, without optional Rayon/clock/image/font embedding.
Installed package VCS is bbc5e4bfe2bdf53a1881ac357193b5160807dfcd.
[Upstream source](https://github.com/J-F-Liu/lopdf/tree/bbc5e4bfe2bdf53a1881ac357193b5160807dfcd)
provides strict loading, per-stream decode limits, maintained object/content
parsing and public simple encoding tables. Content::decode_strict checks full
consumption; ordinary decode and its operation iterator can stop at malformed
trailing content. Do not use lenient extract_text/font fallback paths.

Font ToUnicode parsing eagerly enumerates ranges to build a reverse map. Thus a
small bounded CMap can allocate a very large map. This profile rejects ToUnicode,
Type0/CID, Type3, custom Differences and embedded font programs before any font
decoder/CMap constructor. Do not add a second parser. adobe-cmap-parser0.4.1 AST
parsing has recursive structures and unchecked dictionary-key UTF8; its
get_unicode_map helper also expands ranges and can panic. pdf-extract0.12.1 uses
older lopdf0.42 without the selected loader controls; do not introduce it.

Required narrow references informed failure/provenance choices, not architecture:

- [remarkable-mcp extract.py](https://github.com/praveensehgal/remarkable-mcp/blob/d385834dbc80ebef2f61b8fe898c84288fc605a1/remarkable_mcp/extract.py)
  uses PyMuPDF and skips empty pages/collapses exceptions; neither behavior is
  adopted. Repository declares MIT; no code copied.
- [reMark indexer.py](https://github.com/BGGBTAC/reMark/blob/d5d76e0d1b4c10de7aa85f445e454c7b76802b2c/src/search/indexer.py)
  consumes already-structured text and embeds chunks. No parser reuse or license
  compatibility claim is needed; no code copied.
- [Smart Remarkable manifest](https://github.com/yangg1224/smart_remarkable/blob/4d93645a6a3069cbf7c1f0ff15b56eff141c4959/Cargo.toml)
  and inspected module inventory did not identify a selected offline PDF adapter.
  Repository declares MIT; no image/LLM/native architecture or code is adopted.

## API and identity
Expose retrieval::pdf::normalize(document_uuid, impl Read) -> Result<PdfText>.
PdfText contains document:NormalizedDocument and textless_pages:Vec<u32>.
Reject nil UUID before acquisition. SHA256 covers exact acquired PDF bytes,
including metadata/trailing bytes, not reserialized objects. Set SourceFormat::Pdf
and a fixed revision identifying this profile and pinned parser. Every declared
page produces exactly one SourceUnit in page-tree Kids order, page=Some(ordinal),
section=None. Ordinals start at1; printed labels/native current-page identity are
not inferred. Blank/image-only units stay present and are listed; an entirely
textless document refuses. Build/validate the existing Index before returning.
No partial document escapes after any later-page failure. Existing IndexKey and
DiskCache need no schema/activation changes; original/extractor/normalized changes
retain existing stale-key behavior.

## Resource guarantees and their limits

| Stage | Limit and enforcement |
| --- | --- |
| Acquisition |16MiB plus one sentinel byte, at most4096 Read calls, checked before parser entry; no deadline for a blocking caller-supplied Read |
| Eager loader | strict mode, no supplied password;1MiB decoded output per object/xref stream through LoadOptions; reject any declared encryption after load, including empty-password encryption the library may decode internally |
| Parsed eligibility | at most16384 retained objects; this is checked after parsing and is not a parser allocation bound |
| Page tree | at most256 pages,1024 nodes and32 levels; reserve visits before traversal; reject duplicate/cyclic/missing references, invalid parents or inconsistent Counts |
| Content acquisition | at most64 content streams/page; decoded page bytes at most1MiB, aggregate8MiB; pass remaining allowance into each maintained strict stream decoder before decoding/concatenating |
| Content AST | maintained strict full-input decoding of bounded page bytes; at most32768 operations/page,131072/document checked after AST allocation; no preallocation operation-count claim |
| Resources/state | at most64 font and64 XObject entries/page; indirect dereference chains at most32, graphics stack32; check before processing/growing adapter collections |
| Text |512KiB/page and4MiB/document UTF8, reserve each scalar/boundary before append; no arbitrary intermediate text collector or range expansion |

Input bytes and per-stream limits do NOT establish a hard process-wide RAM or CPU
bound: eager PDF/xref/object parsing and content AST materialization allocate
inside the library before postparse eligibility checks. Repeated eager streams
can cumulatively allocate more than one stream allowance. The adapter provides
the stated acquisition/decode/traversal/output controls, not a sandbox, hostile
process containment or an interruptible parser. No hard RAM/CPU/time claim.
The maintained loader may try an empty password internally for encrypted input;
this adapter neither supplies/discovers credentials nor accepts that document.

## Structural and encoding admission
Use maintained parsed objects; do not write a PDF tokenizer/parser. Validate the
Catalog Pages tree explicitly rather than relying on a lenient page iterator.
Resources inherit from the nearest Pages/Page dictionary as a complete value;
validate references, do not merge resource dictionaries across ancestors.
Contents may be absent/null, a stream reference or an array of stream references.
Reject external stream F/FFilter/FDecodeParms. Support only no Filter or a single
FlateDecode with absent DecodeParms; validate dictionary types before calling the
bounded decoder (its invalid-filter fallback must not become success).

Allow Type1 standard Latin BaseFonts: Courier/Helvetica/Times families and their
standard bold/italic variants. Require explicit StandardEncoding, WinAnsiEncoding
or MacRomanEncoding names; no font descriptor/program, ToUnicode or custom mapping.
Inspect all admitted page font resources before text extraction; do not call
get_font_encoding or extract_text. Map each shown byte through lopdf's selected
public table, require a defined valid Unicode scalar, refuse disallowed controls,
and reserve its UTF8 bytes before appending. This supports accented Unicode where
the admitted encoding defines it, not arbitrary scripts. Missing Tf/font/glyph is
an error, never a warning or silently discarded character.

XObjects must be image streams; Form and PostScript XObjects refuse, even if a
page also contains supported text. Images are never decoded/OCRed. Reject page
annotations, AcroForm, optional-content properties and resource ExtGState or
Properties in this initial profile, rather than implying their text is included.

## Content semantics
Use a closed operator profile with operand arity/type and balanced-state checks.
Accept BT/ET, Tf, Tj/TJ, T*, apostrophe/doublequote text operators and ordinary
numeric text state. Tm/Td/TD position the start of a text object only; subsequent
arbitrary positioning refuses to avoid silently joining separately positioned
words. T* and quote operations establish an explicit newline. A TJ negative
spacing adjustment of at least120 text units establishes a space; smaller
adjustments preserve a word. The policy is lexical approximation, not geometry
or reading-layout fidelity, and belongs in the extractor revision. Each ET is a
text boundary. Require Tf in each BT before shown text; q/Q and cm only outside
BT. A subsequent supported BT is a distinct text boundary. Whitespace boundaries
are normalized without dropping page locations.

Allow a finite validated set of nontext vector/color/graphics operators, q/Q,
cm and image Do. Reject inline images, marked content/ActualText, compatibility
sections, unknown operators, clipping/invisible text rendering modes and invalid
or unbalanced text/graphics state. Do not silently ignore a potentially text-
bearing operator. Document the exact whitelist in source and the public guide.
Success means all admitted page content was handled under this profile; it does
not mean rendered visibility, annotations, physical completeness or native proof.

## Verification and delivery
Author synthetic PDFs with lopdf's maintained writer, including compressed
content; do not rely on personal files, external tools or a tablet. Run actual
Index queries for reordered page objects, retained blank/image pages, Unicode,
inline word joins and explicit boundaries/TJ spacing. Exercise exact original
digest, changed bytes/extractor keys and existing DiskCache compatibility. Include
finite malformed/encrypted/unsupported-font/missing-font/unmapped-byte/Form/
ActualText/positioning/trailing-garbage fixtures and oversized declared CMap ranges
that must refuse without entering CMap expansion. Exercise acquisition sentinel,
bounded decoding, tree/state/content/output limits and later-page failure with no
partial success. Use ordinary default-feature library check independently of
all-feature test unification, affected fixtures, fmt and strict Clippy, then
normal maintained CI/cross-target build. No new CI structure/SDK pin or model,
service, credential or tablet operation. Review implementation and final own
canonical sync/archive independently, then normal coordinated squash and observe
actual-main CI/tag/small provenance separately. No app archive replay required.
