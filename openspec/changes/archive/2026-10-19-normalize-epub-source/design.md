# Design

## Existing evidence and selected mechanics
The current retrieval NormalizedDocument/SourceUnit contract already carries
format, original source digest, extractor revision and ordered page/section text.
It validates at most4MiB normalized text/512KiB per unit after allocation. The new
adapter must bound acquisition and parsing before constructing that DTO.

The pinned remarkable-mcp extraction source d385834d uses ebooklib manifest order
and catches errors as empty text. Those semantics are not adopted. W3C EPUB3.3
defines the package spine as reading order, including auxiliary linear=no items.
Use that order, including auxiliary items, without sorting filenames or scanning
unlisted content. Resolve the first declared OCF package as the default rendition.

Selected maintained libraries are zip9.0.5 (MIT, Rust1.88) with only its pure-Rust
Deflate reader feature, quick-xml0.42.0 (MIT, Rust1.86) without encoding/entity
extensions, and the existing locked percent-encoding2.3.2 for local href decoding.
ZIP parsing/decompression and XML tokenization remain upstream responsibilities.

## Closed supported profile and limits
Read at most16MiB+one sentinel original bytes, hash only the accepted complete
input, and parse a private in-memory copy. Wrap Read/Seek before ZipArchive::new:
metadata read budget2MiB and32768 I/O calls; total subsequent compressed reads64MiB
with the same total call cap. This bounds parser input/work admissions, not a hard
process RAM/CPU deadline. Reject more than4096 entries, duplicate/noncanonical or
symlink names, prefixed/overlapping archives, encrypted entries and encryption.xml.
Validate all local/central headers with the upstream consistency check before
iterating the deduplicated ZIP name index; otherwise duplicate central names
can disappear. Never extract files or resolve network/filesystem references.

Require exact mimetype and one declared container rootfiles sequence; use its first
application/oebps-package+xml rendition. Read container/package XML at most64KiB
each and each spine XHTML at most1MiB, with8MiB cumulative decoded XML. XML must be
well-formed XML1.0 UTF8 with bounded nesting64/events100000 per resource; reject DTD,
custom entities, invalid encodings and ambiguous structure. Manifest IDs and
spine idrefs must be unique, bounded and resolvable; at most512 spine units.
Only local application/xhtml+xml spine entries are supported. Unsupported SVG or
foreign/fallback documents refuse rather than silently disappearing.

Collect body text, CDATA and predefined/numeric entities; exclude head/script/style
content and separate block boundaries. This is normalized XML text, not CSS or
rendered-visibility semantics. Do not execute QML/HTML/JS or fetch external data.
Preserve each canonical archive section path with page=None; page numbers are not
invented. Keep textless units in order and report their paths separately. All-empty
text refuses. Bound normalized output to512KiB per unit/4MiB total, then validate
with the existing Index before returning the result. Errors discard the whole
candidate. Original digest/extractor revision do not become native authority.

## Delivery and checks
Keep acquisition API independent of model/Store/Reader, with a development-only
stdin/file example producing bounded JSON. Original owned EPUB fixtures cover
spine-vs-manifest order, Unicode/entities/inline and block text, auxiliary/textless
sections, query through the actual index, changed source identity and all relevant
bounds/refusals. Cross-target/host quality and dependency audit remain normal CI.
No PDF authoring or tablet/model gate is applicable to this text-only increment.
Sync/archive only this completed scope in the paired code/Docs delivery.

Sources: https://www.w3.org/TR/epub-33/#sec-spine ;
https://docs.rs/zip/9.0.5/zip/read/struct.ZipArchive.html ;
https://docs.rs/quick-xml/0.42.0/quick_xml/reader/struct.NsReader.html .
Library metadata was read with cargo info; limits/profile are application design.
