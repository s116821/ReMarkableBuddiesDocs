# Buddy event-admission evidence

Product implementation6842037d229cab2b114c0b54dbac670b751929e3 changes only
Buddy ci.yml and its existing workflow.test.mjs. Structured jq reads the event
file and emits only a boolean. Exact body/from-string shape is recognized; base,
title, mixed, missing, malformed and unknown details remain normal events.
Normal stage names and budget remain unchanged. Existing title outputs and the
caller's explicit title/checks dependencies carry metadata classification;
main's skipped title remains admitted through existing explicit status guards.

Local eight focused controls pass with the real pinned expression evaluator and
the exact jq predicate extracted from YAML. Existing graph/budget/artifact gates
remain covered. Local jq1.8.1 Windows release bytes were verified against the
official release API SHA25623cb60a1354eed6bcc8d9b9735e8c7b388cd1fdcb75726b93bc299ef22dd9334;
this was task-local tooling, not a system install or new production dependency.

## Actual GitHub event sequence

All four controls use unchanged witness source1eba27dbf227930ed23a2ecade72354345ae4b9b.
That separate commit adds only a temporary early exit19 Checks step before
expensive suites; it is deliberately failing evidence, not a product defect.

- [Initial invalid-title run39375424148](https://github.com/s116821/ReMarkableBuddies/actions/runs/39375424148) fails the maintained title Action and starts no Checks runner.
- [Body edit while title remains invalid39375529335](https://github.com/s116821/ReMarkableBuddies/actions/runs/39375529335) preserves title failure and omits application work.
- [Correcting only the title39375575046](https://github.com/s116821/ReMarkableBuddies/actions/runs/39375575046): PR Title118472833884 passes and real normal Checks118472872609 fails only at the owned exit19 witness. No source push was needed for recovery.
- [Body-only edit39375669892](https://github.com/s116821/ReMarkableBuddies/actions/runs/39375669892) passes PR Title118473129461, creates no normal Checks or reusable application child contexts, and leaves real failed Checks118472872609 unchanged. Before/after native check APIs preserve its ID, head, failure conclusion and completed_at exactly. PR checks still reports that failure although the metadata-only workflow itself succeeds.

GitHub's skipped Checks API name is the literal conditional name expression,
not the evaluated metadata label predicted by expression-only controls. It is
distinct from the normal `Checks` context and does not replace it. The omitted
reusable caller resolves to `PR metadata (no artifact jobs)`. This observed
presentation distinction is retained rather than claiming an evaluated label.
Raw job/check-run snapshots and a machine-asserted before/after proof are held
privately; the public runs above expose native logs and context identities.

## Final candidate and remaining gates

Final sourcec3946d7a77279905e9b246dfc4963684a9ed7ca6 removes only the owned
witness in a new commit. Its entire tree7bb857c2d8cb850fea972a0cea667d1a6754654c
equals product6842037 exactly; no application-source/control fixture remains.
Original negative commits and failed runs remain preserved. Final ordinary
source CI, independent implementation review and postmerge stage proof remain
required; the metadata-only success is not passing application validation.

Manager and SDK are still with their existing owner and require their own
implementation/specification/evidence. SDK's flat graph must isolate every
omitted core context, including Release. No permissions, branch settings,
source concurrency, artifact bytes, publisher or version policy changes follow.
No provider, tablet, reverse-engineering or signing operation was performed.

Source basis: current immutable source diffs, actual local jq/expression outputs,
native GitHub run/job/check APIs and before/after identity assertions.
