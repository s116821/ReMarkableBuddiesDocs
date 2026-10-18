# Export prepared notes with stable destination correlation

## Why

Writer must create a note, find that same note after restart and update it on a
later export. The delivered historical Ledger already defines `[RMB:<UUID>]`
and `remarkable_buddies_export_id`, but has no destination transport. Its export
record also treats Completed as terminal and source_revision as immutable,
preventing ordinary re-export under the same correlation.

## What Changes

- Add a replaceable destination interface, a real Mem HTTP adapter and a bounded
  production command/library path accepting prepared Markdown and source facts.
- Retain stable correlation/backend/source scope in the existing Ledger while
  recording each export operation, exact content digest and prior remote version.
- Separate a newly committed preparation from historical retry acknowledgments;
  only the first invocation may dispatch its one external write.
- Resolve exact metadata/title markers, preserve externally edited notes through
  prior-body checks and version-conditional updates, and reconcile uncertainty.

## Capabilities

### New Capabilities
- `prepared-note-export`: prepared content create/find/update and Mem transport.

### Modified Capabilities
- `historical-conversation-ledger`: stable note association across distinct export
  operations/revisions, retaining historical receipts and expected-head checks.
- `shared-storage`: explicitly admit export-association domain version 2 in the
  existing format-one envelope and offline JSON contract, preserving other version refusals.

## Impact

Rust export orchestration, Ledger export transitions, one bounded command and
focused real-HTTP/local-Store fixtures. No new registry or Buddy network service.
Extraction, OCR, generation, gestures, native rendering, refinement UI and whole
Writer acceptance remain separate unfinished requirements. No live account write
is needed to implement or verify this increment.
