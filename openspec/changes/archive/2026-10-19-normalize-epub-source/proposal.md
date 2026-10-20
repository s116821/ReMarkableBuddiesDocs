# Change: Normalize bounded EPUB text into the existing source index contract

## Why
The delivered normalized-source index requires caller-supplied text. EPUB ingestion
is still missing. Existing reference code iterates manifest items and collapses
parser errors to empty output, which cannot preserve reading order or completeness.

## What Changes
Add an offline Rust EPUB text adapter and development example producing the existing
NormalizedDocument plus explicit textless-section reporting. Use maintained ZIP
and namespace-aware streaming XML parsers, bounded before metadata/decompression,
follow the declared package/spine, retain original-byte digest and section paths,
and refuse unsupported or malformed inputs without returning partial success.

## Boundaries
No PDF/OCR/notebook extraction, installed Reader integration, model/research call,
native identity, disk cache, tablet operation or full REM4 completion is included.
The existing Writer draft and native research remain separate. This is a text-layer
adapter, not a browser/layout/visibility or whole-physical-document proof.
