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

This is host CLI/domain/output-handoff evidence. It is not filesystem-immutable inspection, hard wall-clock cancellation, live sync/native/model evidence or completed Manager UI. Broader memory, privacy, personalization and native/parent gates are preserved.

## Hosted acceptance and own lifecycle

Independent source/spec reviews 5532769962 and 5532770107 were read in full at feeaf4752422b7a5ec3b68894f2eb7d6337f31ca and 4a0ecf0c89ca3688ecd87713e8aeffc82493f0d3, with no actionable findings. The accepted preceding privacy lifecycle 36afb775 was carried with provenance into Docs855a730f81311e59655d834f2bb05473ba0fd94d; all five own memory files remained byte-identical. Current inline review comments are empty.

[Source pipeline 38731346625](https://github.com/s116821/ReMarkableBuddies/actions/runs/38731346625) completed successfully at frozen head feeaf475. Actual job checkout was merge5a08f4a6a7384079b7651de835eef32e05621743 into mainb74395a1, not a later mutable PR merge ref. Hosted Linux Rust1.99 reported library311 passed/one inherited ignored; both actual CLI stdin tests passed within the subject-memory CLI group's16 passing tests. Other reported groups passed; nested child tests are not added again to totals. Raw unit/build/integration logs are retained separately from local Windows logs.

The build uploaded artifact11971174004,19191077-byte ZIP, SHA25691e3f767458f5f514c47f849b87c3cea618e70e10507381e32d87e87e714ef42. Integration downloaded that exact artifact ID/expected digest and exercised retained ARMv7/AArch64 version commands under pinned emulation images without rebuilding. Candidate0.3.0 is not an official release; publication was correctly skipped for the PR. This is retained-artifact emulation, not native tablet qualification.

[Docs pipeline 38733071788](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/38733071788) passed all three jobs at855a730f. Actual strict checkout5ab0c3538d26b62365c7748d5108c209177c0eff merged that head into879f5ec0 and reported27 passed/zero failed, distinct from local22. The completed one requirement/three scenarios are synchronized to the own canonical capability and only this change is archived. Final lifecycle preservation review/current Docs CI remain the coordinated delivery checks; no parent merge or whole REM24/42 completion follows.
