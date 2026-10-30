# Join deliberate Writer generation, refinement and export

## Why

Delivered Source1d1665f / Docs22773ea contain supplied-text Writer drafts and
the separate prepared-note exporter. A caller must manually compose them.
Generated-report success does not establish a fresh export request or prove
that a selected draft/source remained current. The maintained simulator still
rejects Writer and combined modes.

## What changes

- Add explicit generate-and-export, refine-and-export, selected-draft export and
  known-ID reconciliation to the existing bounded Writer command path.
- Bind a fresh outer request in the existing Ledger, then fence the exact
  draft/source selection into export admission. Keep stage outcomes distinct.
- Reuse the existing Writer model path, destination trait/Mem client, portable
  correlation and known-ID reconciliation; add no second export registry.
- Add maintained scripted host Writer scenarios through `--simulate`, using the
  production joined path. Preserve Reader scenarios and explicit unsupported
  combined/native routing; historical Reader fixtures are not combined proof.

## Scope

This closes a real supplied-text direct-export/re-export flow. Legacy generate,
refine, prepare-export and caller-supplied PreparedNote export remain compatible.
Review-first callers use those existing draft stages, then deliberately select
an export. Memory is optional. No ingestion/OCR, large-notebook reduction,
tablet rendering/gestures, shared native Writer routing or live Mem qualification
is implied. No new provider request is made to replay closed quality evidence.

Existing Source/Docs branches and old Reader/memory/native work remain preserved.
This change uses one coordinated Source/Docs delivery, including simulator
impact, canonical sync and its own scoped archive; no planning-only delivery.
