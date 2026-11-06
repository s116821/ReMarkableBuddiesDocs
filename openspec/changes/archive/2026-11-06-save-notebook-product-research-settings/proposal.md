# Save product and research preferences on ordinary notebook storage

## Why
Existing product/research Inspect and Prepare read a valid saved configuration, but their conditional Apply uses legacy maintenance admission, which explicitly refuses generation4/notebook markers. Ready ordinary notebook storage is already used by the runtime and protected archive/restore paths. REM-42 requires usable Reader/Writer/export and research preference management for that supported local store.

## What Changes
Extend only the two existing nonsecret conditional writers with a scoped existing-store preference admission that admits ready ordinary local notebook storage under the same custody. Reuse existing target/CAS/publication/readback/report lifetimes. Preserve all prior legacy admission and the other callers' explicit notebook refusals. No new setting, CLI/wire family, credential-file publication, notebook adoption, configuration import, archive integration, service restart or runtime activation.
