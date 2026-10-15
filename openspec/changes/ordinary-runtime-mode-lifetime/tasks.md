## Preparation
- [x] Read current REM-24 description and all 32 timestamped comments, current REM-39 scope and existing actual startup/mode consumer.
- [x] Preserve existing checkpoint branches and protected unfinished work; isolate the new Docs/Rust topics.
- [x] Record central proposal, design, requirements and verification before code.
- [x] Agree the exact narrow storage API and ownership with its current owner.

## Implementation and Verification
- [x] Implement the ordinary-mode guard using the existing mode transition fence.
- [x] Retain the guard through the actual ordinary Reader caller; preserve config and selected/historical behavior.
- [x] Verify affected real-Store and startup consumer cases, formatting and strict lint across all targets/features.
- [ ] Obtain independent source/spec review and inspect exact hosted CI and bot feedback.

## Delivery
- [ ] Publish linked code/Docs revisions with source-parent and evidence limits.
- [ ] Sync only the implemented requirements and archive this completed slice.
- [ ] Keep foundation merge, live mode UI/provider/native qualification and full REM-24/52 open.
