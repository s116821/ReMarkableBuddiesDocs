# Change: Assemble bounded source context for an existing Reader request

## Why
The delivered index, adapters and cache do not yet assemble retrieved passages
alongside an existing request and its exact historical context. A follow-up must
query its explicitly associated original document again rather than a visible
Buddy page or its previous hit list.

## What Changes
Add an ordinary historical Ledger receiving API that reads one existing snapshot,
preserves the interpreted Reader request and eligible history verbatim, validates
an explicit original turn/source-record reference against an independently supplied
complete IndexKey, and queries the existing local retrieval Provider. Return an
immutable typed/encoded frame with complete key, passage provenance, explicit
history selection and unavailable-media metadata under byte and caller-token limits.

## Boundaries
This is a read-only data seam, not automatic Reader/model dispatch, selected
history/effect admission, native identity, source discovery or a new registry.
Association selection and fresh expected keys remain caller inputs; inheritance
reuses an explicit original reference until the caller deliberately changes it.
No source record or capture-batch membership is rewritten. Durable passage
publication and runtime integration remain separate unfinished work. Preserve
Writer's pending normalized-text/generation workflow and all held lanes.
