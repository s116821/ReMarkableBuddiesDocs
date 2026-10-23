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
- [x] Exercise Linux synthetic filesystem/CLI vectors and Windows early-unsupported no-read controls; retain failure and raw corpus provenance separately.
- [x] Verify complete before/after preservation, denied durable read/enumeration controls and uncertainty/output/locking cases.
- [x] Run exact-head fmt, strict Clippy, full tests and hosted Checks; read independent review and bot findings (full delivery CI remains a separate gate).

## 4. Linked delivery preparation
- [x] Sync only this completed canonical capability; archive only completed own implementation artifacts.
- [x] Prepare final composed review packet with current Docs/source checks and exact revisions.
- [x] Record normal Docs-first squash order and separate actual-tree/main/publication verification gates.
- [x] Document narrow producer scope and remaining Manager/runtime/integrated gates.

Final paired acceptance, normal merges and actual-main/publication receipts remain
explicit post-review gates in PR comments and canonical task tracking. Checked
implementation tasks never stand in for those later observed delivery results.
