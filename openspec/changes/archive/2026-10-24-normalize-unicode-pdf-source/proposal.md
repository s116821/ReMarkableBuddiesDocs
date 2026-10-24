# Extend the existing PDF adapter with declared Unicode text

## Why

The current PDF adapter refuses every Type0/CID/ToUnicode font. The explicit
simple Latin profile is useful but excludes PDFs with declared Unicode text maps.
The pinned library's general font helper cannot safely be enabled on arbitrary
input: its CMap constructor expands ranges into a reverse map, and convenience
decoding can substitute replacement characters.

## What changes

Extend the existing normalize API and parser pipeline with one closed horizontal
Type0 Identity-H/CIDFontType2 profile using explicit ToUnicode maps and fixed
two-byte shown codes. Reuse maintained strict typed operation parsing; validate
bounded mapping semantics before building a forward lookup. Preserve simple-font
behavior, page/content/output rules and whole-document refusal. Record a new fixed
extractor revision so old cache/index keys cannot masquerade as fresh extraction.

## Boundaries and delivery

No new parser dependency/tokenizer, generic extraction stack, rendering/font-program
decoder, OCR, external resource, model, tablet or runtime activation. Font metadata
and ToUnicode describe a text layer; they do not prove rendered glyphs or visibility.
Reader/Writer/model/native/selected gates remain open. Use authored offline PDFs,
actual Index/cache controls, paired Source/Docs review, own sync/archive, normal
Docs-first squash and separately observed actual-main/new publication outcomes.
