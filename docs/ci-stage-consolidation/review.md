# Compact CI delivery and rollout evidence

The compact core is merged and actual-main publication is verified. All35 retained original feature PRs carry the corrected pipeline. Both obsolete CI drafts are closed with their source and failed evidence preserved. All 13 final Manager compatibility runs passed their five PR stages. The 21 older Buddy feature branches still need their own effective-main conflict resolution and hosted feature validation; the rollout stays active for those explicit delivery gates. No full feature, native gate or MVP completion is implied.

| Event | Buddy | Manager |
| --- | --- | --- |
| Pull request | PR Title → Checks → Build → Integration | PR Title → Checks → Build → Integration Linux/Windows |
| Main merge | Checks → Build → Integration → Release | Checks → Build → Integration Linux/Windows → Release |
| Running jobs | Four | Five, counting both platform legs |

Skipped event-only jobs allocate no runner. Title is a prerequisite of Checks on PRs. Common source, unit, release/workflow and dependency checks run once in Checks. Build owns candidate calculation, uploader audit/compilation and application compilation. Integration and Release consume retained artifacts without rebuilding. Applicable native Windows cases run only in existing Windows Integration; common suites are not repeated there.

## Core acceptance and actual publication

- Docs53 finalc0de65de was reviewed5541901340, CI38834925607 passed, merged d5da9cbae67339d3e041692fb647de4e06be3edc; actual main38835329598 passed.
- Buddy59 exact798cbe398b31d11a1f1fe6a562abe9846799f232 passed all four PR stages in38831146595, reviews5541792700/5541855786 accepted. Normal squash main6879efdc721db6dc598d4acdcdb33929c75756a2, actual [38835334603](https://github.com/s116821/ReMarkableBuddies/actions/runs/38835334603) all four stages passed; Title skipped.
- Manager23 exact678b6d406d23131c151e280ba40f56f2e38ec33c passed all five PR stages in38831149009, review5541792787 accepted. Normal squash mainb746c48ed0a11ca6dee7722ca7c08552f4985c21, actual [38835336589](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38835336589) all five stages passed; Title skipped.
- Buddy publicv0.3.3 release414445565: annotated tag79a1e7b8ecb80bc6fac316adbe66843e406afa8b resolves exact6879efdc. Artifact12019012358,16,050,301bytes, ZIP SHA256dff9e5fbad3f9786ec7dfd93ddcf286a86f60e48ae1b0cb5685b079aa830005a appears unchanged in Build, Integration and Release logs. All three public asset API digests match the parsed completion receipt; complete remote-byte verification precedes final publication PATCH.
- Manager publicv0.4.3 release414441908: annotated tag89265cbbb18c9e9a0d11939334734ed556a259b5 resolves exactb746c48. Artifact12019036670,280,534,728bytes, ZIP SHA2564891c770683e7a90559aab4381bf23ed23b4b17f5270777fe27603fad6701296 appears unchanged in Build, both Integration platforms and Release logs. All four public asset API digests match completion receipt, with complete remote-byte verification before publication.

## Branch-specific preservation and repairs

The [current inventory](open-pr-reconciliation.md) binds all delivered branch heads. Main independently compared complete candidate trees and each branch's source/runtime command set. Windows previews preserve three selected WindowsNative cases plus the Drive NTFS control where those source features exist. Root actually executed3+1 Windows cases; workflow guards passed7 controls per preview, including negative duplicate/wrong-platform cases. Earlier WSL Bash launch failures are preserved; successful execution explicitly used installed Git Bash.

Seven initial Manager compact branch runs8–12/21/22 passed. Six13–18 failed honestly in npm test because their fixture imported deleted coordinator.py. The repair reuses existing accepted PR21 commit973585003405e303cb555d91eca5a33c294e73ff: current hash-qualified pure identity helper, matching archive fixture, bounded runtime verifier and tampered-helper refusal. PR13–17 receive only six applicable files; PR18 receives all nine including already-present packaging/download assertions. Later download UI is not imported into earlier branches. Every unrelated tree entry remains exact.

Supported Node24.21/Python on Windows: the exact shared PR13–17 verifier/caller/fixture/test graph passes32 controls in a representative execution; PR18 passes33 including the existing shared-download case. No weakened checks or restored obsolete release engine. Earlier local test-log path error and missing Python launcher remained failed attempts; corrected runtime setup produced the recorded passes. Subsequent actual final-head hosted runs, linked per branch in the inventory, passed PR Title, Checks, Build and both Integration platforms for all 13 Manager branches; PR Release was correctly skipped.

Manager24 preserves useful draft2 maintenance: generated release fixtures' node_modules and .upstream distributions are excluded while maintained source stays linted. Actual ESLint5path assertions and full lint passed; source review5542072952 and all five PR stages38837100914 accepted before merge6b2b4d5. Branch propagation preserves each feature's ESLint browser-global list. A first whole-file equality assertion refused PR9; literal-only edits preserved its feature settings. An equivalent .gitignore append initially omitted main's explanatory comment, causing an actual merge conflict and no new CI. The final normal main integration copies the exact already-reviewed main .gitignore bytes; all remaining repaired tree entries are unchanged. Original failed runs and intermediate heads remain in Git history.

## Preserved earlier limitations

The initial local sandbox blocked localhost/Git-config Action controls and Windows Bash execution; those attempts are not passing evidence. Final hosted PR/main pipelines executed the required controls successfully. Actionlint1.7.12 reported the two preexisting concurrency.queue:max compatibility warnings, not a clean result. An early removed YAML helper was restored before the accepted exact source revisions. No denied run cancellation was rerouted; queues advanced normally. No repository settings or tablet state was changed.

Only ci-stage-consolidation's completed core is archived. ci-existing-pr-reconciliation remains active until current branch checks, refreshed inventory and its own acceptance/lifecycle finish. Broader REM-46 and feature work remain separate.

Source basis: direct human instructions, exact GitHub commits/reviews/Actions/release records, local source-tree comparisons and scoped actual checks. Historical tablet evidence supplies no CI or native acceptance here.
