## 1. Concrete contract
- [x] Read current requirements, ownership and existing cache/inspection contracts.
- [x] Describe one-slot scope, noninitializing custody and uncertainty boundary.
- [x] Freeze exact canonical hash/identity encodings and synthetic golden vectors (filesystem qualification remains pending).
- [x] Obtain independent concrete precode review before Rust edits (accepted cfd133a; implementation review remains separate).

## 2. Producer
- [x] Add private header/lease custody with no Store/recover/durable reads and Linux one-slot unlink/sync primitive without changing legacy API behavior.
- [x] Add closed strict CLI and bounded inspect/prepare/apply/status reports with custody through output.
- [x] Document public manual equivalent and explicit unsupported integration/runtime domains.

## 3. Verification
- [ ] Exercise Linux synthetic filesystem/CLI vectors and Windows early-unsupported no-read controls; retain failure and raw corpus provenance separately.
- [ ] Verify complete before/after preservation, denied durable read/enumeration controls and uncertainty/output/locking cases.
- [ ] Run exact-head fmt, strict Clippy, full tests and current hosted CI; read independent review and bot findings.

## 4. Linked delivery
- [ ] Sync only this completed canonical capability; archive only completed own artifacts.
- [ ] Obtain paired final review and current Docs/source required checks.
- [ ] Normal Docs-first squash, verify actual trees/main runs and source publication.
- [ ] Close only this producer scope; keep Manager consumer and broad project gates explicit.
