## Implementation

- [x] Reuse accepted PR39 configuration commit in the existing Main checkout, preserving ordinary-mode lifetime changes and unrelated unfinished work.
- [x] Connect startup snapshot to actual prepared Reader requests and shared receiving answer context.
- [x] Preserve no-preference behavior, transcription isolation, single assembly, memory refusal policy and operation guards.
- [x] Update maintained simulator inputs and outgoing-request assertions for this behavior.

## Verification and delivery

- [x] Run focused source/simulator regressions and formatting/lint checks appropriate to changed paths.
- [ ] Run representative authorized live-provider checks; distinguish actual semantics from scripted policy checks.
- [x] Publish linked implementation/Docs PRs with exact source/spec revisions and separately attributed results.
- [ ] Resolve independent review, required hosted checks and current bot/issue feedback.
- [ ] Sync only this completed capability into canonical specs and archive this change; retain wider REM-53 and runtime/native gates.
