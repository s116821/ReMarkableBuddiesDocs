## Preparation
- [x] Read the current user request, controller/renderer source, central workflow and REM-41 requirements/comment history.
- [x] Record the quiet-background presentation contract before source edits.

## Implementation and verification
- [ ] Preserve initial/manual pending while suppressing automatic pending display transitions.
- [ ] Verify deferred automatic success keeps prior status/details/timestamp until completion, and advances on success.
- [ ] Verify returned failure and identity change clear details and stop polling; disconnect during a pending automatic read defeats a late result.
- [ ] Run affected source checks and record exact revisions and supported/supplemental runtime limits.
- [ ] Obtain paired independent review and required CI without repeating completed physical cable tests.
- [ ] Sync only accepted requirements, archive this completed slice and merge linked delivery normally; leave wider REM-41 gates open.
