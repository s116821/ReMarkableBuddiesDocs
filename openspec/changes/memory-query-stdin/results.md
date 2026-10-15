# Memory stdin query: local verification and consumer handoff

## Exact source and contract

Central precode2d0ecad was published before implementation. Source626c2f818ad335f6aa49e5a9e88a739267b270cb implements the actual CLI/common maintenance/validator path and focused controls. Current sourcefeeaf4752422b7a5ec3b68894f2eb7d6337f31ca adds only guide wording clarifying that local memory access is not an external provider call. Four source paths over reviewed logging11f6aac7: main, memory maintenance, existing CLI tests and public guide. No Cargo/SDK/schema/provider algorithm changes or remote staging writer.

The [public exact stdin guide](https://github.com/s116821/ReMarkableBuddies/blob/feeaf4752422b7a5ec3b68894f2eb7d6337f31ca/docs/memory-query-stdin.md) specifies query-only `--memory-input -`, existing Query fields/report1,1048576-byte limit/read at most+1, EOF/caller deadline semantics, supported numeric budgets and actual empty/status examples. Profile comes from existing configuration. Generic response bound remains8454144; a smaller Manager cap must refuse overflow honestly. Old readers reject relative dash before Store because existing file safety requires absolute paths; no /dev/stdin/staging fallback. SCRAPPY received the actual published contract for its existing Manager memory-search precode, not an invented endpoint.

## Actual Windows checks

Rust1.98.1, locked/offline/all-features/jobs1, isolated owned Stores and actual child CLI, no device/provider/service access:

- Two new actual CLI tests passed9.93s: exact file/stdin report parity for local and selected memory, retained Unicode/CRLF/provenance and relevant facts; inclusive valid1MiB input; malformed/invalid UTF8/trailing JSON/oversize/domain-invalid refusal before data/cache/credentials creation; valid query against missing Store remains unavailable without initialization. Configured fake API endpoint/key and invalid-unused runtime setting confirm this maintenance route does not enter model/device startup.
- Core maintenance module three tests passed1.14s: one new I/O failure/non-query no-read control; the updated selected writer control now decodes its query through stdin before exercising stale/forged/empty/currentness and partial-output failure; one existing error-classifier control is separately counted, not three new tests. No full legacy CLI/provider matrix rerun.
- Initial core test compile failedE0382 because the updated fixture borrowed identity after moving it into configuration. Original writer-r1 log remains; only the fixture reference was corrected to borrow the configured identity. Writer-r2 then passed. The earlier two actual CLI tests had already passed; no production defect was hidden.
- Final strict all-target/all-feature Clippy passed19.98s; formatting/diff passed. Raw CLI/writer-r1/writer-r2/lint logs remain in the task evidence directory.

This is host CLI/domain/output-handoff evidence. It is not filesystem-immutable inspection, hard wall-clock cancellation, live sync/native/model evidence or completed Manager UI. Required exact hosted CI, independent review/current feedback and own canonical/archive remain open. Broader memory, privacy, personalization and native/parent gates are preserved.
