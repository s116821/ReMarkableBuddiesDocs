# Keep Reader content out of routine diagnostics

## Why

The actual application defaults enable Debug for its own module. Provider parsing currently logs entire response JSON and arbitrary model/usage values; Reader orchestration logs analysis, question, independent transcription and answer; rendering logs the full text again. This routinely exposes user/document text and any personalization echoed by a provider. REM-53 requires avoiding routine full user-text logging.

## What Changes

- Replace full Reader/provider/rendered-content diagnostics with stage names and bounded numeric metadata.
- Retain only recognized numeric token usage fields; do not stringify arbitrary provider metadata into logs.
- Preserve exact requests, parsed answers, visible/persisted text, configured diagnostic levels and intentional private evidence/debug dumps.
- Add one real CLI/local HTTP regression with synthetic sensitive canaries: logs exclude content/metadata while the report and answer retain exact intended content.

## Scope

Provider response diagnostics, actual Reader orchestration and its render-text log only. No prompt/API request, model choice, transport, storage/schema, native operation or deliberate evidence-retention change. The reviewed Reader cancellation and personalization branches remain intact; their wider gates are unchanged.
