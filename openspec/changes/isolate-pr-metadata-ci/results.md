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
[source CI39375790559](https://github.com/s116821/ReMarkableBuddies/actions/runs/39375790559)
passes Title, Checks, Build and Integration, with PR Release skipped. Independent
source/active-contract reviews5581166797/5581167003 accept this exact candidate.
Postmerge stage proof and coordinated lifecycle remain required; metadata-only
success was not substituted for passing application validation.

## Qualified owner implementations

Manager27 eda507ec535ee1ca556eaba5ed03bf9e26e6eb15 is independently accepted
by review5581318529. It preserves all135 other delivered download-UI main783a91b
entries including pipeline.yml, adds only the existing-title classifier and
distinct omitted Checks/caller names, and preserves explicit failure/main guards.
Its unchanged witness1d6c1dbc has actual invalid-title39377303958, corrected-title
39377414358 and body-only39377542326 runs. The corrected title executes normal
Checks118478604130 and fails at early exit19; body-only leaves that exact failed
normal check authoritative with no application children. Final ordinary
run39378103739 passes Title, Checks, Build and both Linux/Windows Integration;
PR Release is skipped. This completes its ordinary current-source PR validation.

SDK29 7ce5910bd525304704c743db868e7cb9ae9a0219 is independently accepted
by review5581318413. Its four-file precode11265ffd precedes implementation.
Only ci.yml, reusable pr-title.yml and the existing fixture implement admission;
all203 other delivered entries remain exact. Classification crosses both reusable
output levels and direct title edges; all five omitted flat core contexts are
distinct. Unchanged witness82a6f5bd has invalid-title39377147522, corrected-title
39377298105 and body-only39377412636. Normal Checks(Linux)118478239212 fails at
exit19 after correction; body-only retains that exact failure and omits all five
core contexts under observed literal names. Final ordinary39378129041 passes
nested Title, Linux Checks, Windows staging, Build and Integration; PR Release
is skipped. The SDK owner retains its own canonical specification/lifecycle.

Both final sources remove exactly their owned four-line witness. Original failures
remain preserved; neither owner's evidence is inferred from Buddy. All three
ordinary final source pipelines pass. Central canonical sync/archive follows
those qualified results; final Docs checks/lifecycle review and normal coordinated
delivery remain merge gates. Postmerge receipts are separate from PR qualification.

The central Docs topic normally merges actual delivered main b9a859d before its
own canonical addition; all unrelated delivered work is preserved. The one added
requirement has four scenarios and retains observed literal skipped names. The
source owners retain their accepted exact heads; this lifecycle does not request
repeating their completed ordinary matrices or changing artifact/release policy.
No permissions, branch settings,
source concurrency, artifact bytes, publisher or version policy changes follow.
No provider, tablet, reverse-engineering or signing operation was performed.

Source basis: current immutable source diffs, actual local jq/expression outputs,
native GitHub run/job/check APIs and before/after identity assertions.
