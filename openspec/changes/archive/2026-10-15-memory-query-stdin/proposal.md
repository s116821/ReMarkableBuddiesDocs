# Supported stdin for subject-memory queries

## Why

The existing memory maintenance command accepts only a validated absolute regular file. Manager's real subject-memory search consumer cannot safely stage arbitrary remote query files, and /dev/stdin is deliberately unsupported. Existing Query already obtains profile identity from configuration; a bounded stdin transport is the actual missing seam, not another retrieval/provider/profile API.

## What Changes

- Support `reader-buddy --memory-operation query --memory-input -` as an explicit stdin source for the existing typed Query JSON.
- Read at most the existing1MiB input bound plus one byte, validate UTF8/JSON/domain rules and preserve configuration, preflight, selected-current handoff and write_to semantics.
- Keep ordinary absolute-file input unchanged. The stdin marker is query-only; other operations refuse without reading stdin or opening Store.
- Publish exact fields, EOF/cancellation behavior and examples for Manager; prove actual CLI file/stdin parity, invalid-input refusal and selected handoff with focused controls.

## Scope

No memory schema/provider/store/search algorithm changes, temporary query-file writer, service listener, sync worker, credentials, model or device initialization. Domain-read-only queries can perform normal Store recovery; do not claim filesystem immutability. Existing Manager precode8c18074e owns its separate UI/transport integration after this contract is published.
