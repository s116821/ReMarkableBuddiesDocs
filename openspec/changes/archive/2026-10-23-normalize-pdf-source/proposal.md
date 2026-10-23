# Change: Normalize a supported PDF text layer into the existing source index

## Why
The normalized index accepts caller-supplied PDF text but does not acquire it.
An offline adapter must retain original-byte identity and page order without
silently dropping unsupported text, skipping blank pages or treating errors as
empty success.

## What Changes
Add a pure Rust, offline PDF adapter using pinned maintained lopdf parsing and
strict content decoding. Its first supported profile covers standard Latin Type1
fonts with explicit simple encodings, ordinary text operations and image/vector
pages. Return the existing NormalizedDocument plus ordered textless page numbers.
Refuse unsupported fonts, mappings, text-bearing operations and malformed or
exhausted input for the entire document.

## Boundaries
No OCR, rendering/layout fidelity, arbitrary Unicode font support, annotations or
form-field text, external-resource fetching, source discovery, Reader integration,
model/research call or native authority. Existing EPUB/index/cache behavior stays
intact. This increment does not complete the broader retrieval feature.
