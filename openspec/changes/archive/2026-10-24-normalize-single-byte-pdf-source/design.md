# Closed fixed-width reuse

## Admission

Keep normalize/PdfText, strict loader/page/content paths, existing simple Type1
decoder and Type0 Identity-H/CIDFontType2 admission. Add only indirect simple fonts
with Type=Font, Subtype=TrueType, Encoding=WinAnsiEncoding (a name), nonempty
BaseFont<=128bytes, required FontDescriptor, FirstChar, LastChar, Widths and indirect
ToUnicode; optional Name<=128bytes. Top-level keys are restricted to exactly those
fields. Type1 ToUnicode, Type3/CFF, missing/other/dictionary encodings, descendants,
unknown fields and implicit mapping remain unsupported.

Resolve ordinary same-document metadata through existing bounded helpers.
FirstChar/LastChar are integers0..255 with first<=last. Widths is an array of exactly
last-first+1 finite numbers, hence at most256; charge its existing metadata budget,
never use it as a rendered-layout proof. Require every admitted map entry to lie
within that declared range; unmapped shown bytes refuse. Reuse the complete existing
FontDescriptor closed validation and matching FontName/BaseFont; forbid CIDSet in
this simple-font branch. FontFile2 remains optional opaque input-owned data with
external-file metadata refused; no new program decoding or font lookup is allowed.
Keep all other descriptor types, finite-number and string/reference rules.

## Map width and output

Give the existing private Map a closed One/Two source-width discriminator. Type0
requires Two; the new TrueType branch requires One. Thread expected width through
the same maintained strict CMap AST parser and decoded-hex code admission. For One,
codespace endpoints, bfchar codes and bfrange bounds are exactly one decoded byte;
for Two the existing two-byte checks remain unchanged. Mixed/variable-width codes
refuse. Keep the complete wrapper, direct CMap-body system metadata, operation and
target validation, bfchar/array/scalar-range semantics and range reservation before
expansion. Typed odd-hex/dictionary normalization remains as previously documented;
do not add a lexer or claim raw syntax information lost by maintained parsing.

Map forward keys remain u16. Decode shown bytes through the bound map width and
emit mapped Unicode scalars directly through the existing bounded Text::push path,
without allocating a decoded string/list. Type0 still rejects odd/truncated shown
strings; any byte count is integral for One. UTF16-BE targets remain2..16evenbytes,
with current pairing/control/U+FFFD refusal. No WinAnsi fallback is used when the
explicit map is present, including for ASCII-looking missing codes. This validates
declared Unicode, not whether the opaque font actually renders those glyphs.

Keep caches keyed solely by immutable input ObjectId. A cached map must match the
requested width or refuse, regardless of which font was visited first; never key by
(reference,width) to double-decode/count the same object. Font hits also retain their
bound width. Different map references may share CMapName and use different widths.
Aggregate64font/64map limits cover both Unicode branches; all prior per-map/document
decoded bytes, AST operations, mapping entries, target UTF8 bytes and65536metadata
visits remain unchanged. A One map has at most256distinct entries by its code space,
without relaxing any existing generic limit. Existing source/output/cache limits
remain distinct from library allocations or hard CPU/RAM/blocking-reader deadlines.

Use fixed fresh revision `pdf-fixed-width-unicode-r3-lopdf-0.46.0` for every newly
normalized PDF. Preserve r1/r2 entries without in-place relabeling; changed revision
means a different existing IndexKey. No normalized/index/disk schema change occurs.

## Evidence and lifecycle

Before source changes, review this exact profile. First add an authored expected-
success TrueType single-byte regression and observe its failure against the current
adapter; retain the red result, then implement and observe it passing. Reuse existing
authored Book/CMap helpers. Keep old14simple+16Type0 PDF cases; only the explicit
fresh revision expectation may advance. Test mixed simple/Type0/TrueType/blank pages,
Unicode/ligatures/supplementary targets, compressed maps, actual Index queries/ranges
and old-key/cache refusal. Test all256codes, repeated aliases/pages/map reuse,
same-reference width conflict in both orders, same-name distinct maps, aggregate
font/map/metadata bounds and genuine later-page whole-call refusal.
Width-conflict fixtures must map all bytes/pairs they show so refusal cannot be
credited to an unrelated missing-code error; fix page-local resources to control
which width is admitted first.

Negative controls cover missing/wrong encoding/descriptor/font name, first/last/width
shape/range/count/numeric/indirect fields, forbidden CIDSet/external program metadata,
out-of-font-range entries, unknown codes, literal/mixed/wrong-width CMap sources,
unsupported font kinds, malformed targets/wrappers and no fallback. Preserve prior
amplification/output/control cases through the unchanged decoder/budgets.

Qualify the exact successor with affected PDF/EPUB/cache/retrieval/receiving suites,
full default library, strict all-target/all-feature lint, default library check,
fmt/diff, central strict/guidance and current CI. Obtain implementation acceptance,
sync only the modified PDF requirement, archive own work, obtain final paired review,
then normal Docs-first delivery and separately observed actual-main/new publication.
Respect the1% usage reserve with a durable unfinished-work checkpoint if needed;
never relabel an unfinished increment or earlier evidence as complete.
