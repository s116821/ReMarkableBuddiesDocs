## Why
Normalized retrieval accepts Notebook material, but has no adapter for notebook
page images. The existing PDF and EPUB adapters cannot supply handwritten text.
An explicit historical-image adapter makes this source class usable without
claiming access to a native notebook or changing installed Reader acquisition.

## What Changes
- Add bounded declared PNG page-image transcription through a caller-selected
  existing LLMEngine, retaining unverified OCR origin and extraction-profile identity.
- Define ordered image-set identity separately from native notebook-file identity;
  preserve page mapping through the existing Index and owned cache.
- Qualify an actual maintained OCR/index/cache-reopen/query caller with adversarial
  local controls and separately inspected genuine historical handwriting.

## Scope
Explicit ordinary backend ingestion only. No tablet access, native .rm parsing,
source acquisition, correction learning, selected/runtime integration, new model
settings, cache schema changes, SDK changes or dependency/framework addition.
This does not complete installed notebook support or the integrated product.
