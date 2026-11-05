# Integrated handwriting qualification, November 5

The current source passes technical checks and the six original cursive and
negative-transfer controls. Mathematical recognition remains **NOT MET**.
This active change is not ready for canonical sync, archival or delivery.

## Revision and mechanism evidence

- Buddy: `5403ae1e524f89e2e198d6c39319b34d81203e10`, tree
  `244fbeef5fedb1ccd37ae4ebe8c5a9a7eb6bfefb`.
- Execution-time Docs: `4b445d860fce9af3bc5603d614cde925321b0462`, tree
  `dac5f75a4ed79bf5db106c1d0b20c57d02dc8715`.
- [Source CI](https://github.com/s116821/ReMarkableBuddies/actions/runs/42078381381)
  passed Title, Checks, Build and Integration at that exact source; PR Release
  was appropriately skipped. All three execution-time Docs checks passed.
- Local integrated controls passed 23 focused transcription tests and two actual
  CLI tests. Local Windows Clippy retained existing dead-code warnings; hosted
  strict Linux checks are distinct evidence, not a relabeling of that local run.

Both live packets used explicit Terra calls through the reviewed instrumented
transport and actual product admission, normalization and report paths. Each
request allowed at most 4,000 completion tokens and 90 seconds with no retries
or redirects. The four-cell and six-cell executions each completed once with
correct pinned identities, `finish_reason=stop`, unchanged Store, unconfirmed
results, zero stdout/stderr leakage and exit 0. Technical completion does not
establish recognition accuracy.

## Explicit mathematical layout comparison

Experiment `rem26-math-layout-5403ae1-terra-r1` used the original two
upstream-default MathWriting PNGs, unchanged strict rubric and selected context.
Only the previously reviewed explicit policy/prompt/profile changed. Independent
arm-blinded scoring and the separately frozen Root score agree: **0/4 strict
usable structure and 0/4 full fidelity**.

Both sample-A arms retain union/subscript layout but confidently substitute
equals for colon-equals and less-than-or-equal for membership. Both sample-B
arms return unreadable, preserving none of the required positive fraction,
radical and subscript structure. These are distinct wrong-assertion and safe
abstention failures. No identifiable unrelated technical text appears; this
does not establish generalized resistance to misleading context.

The prospective rubric and input references remain in
[math layout profile](math-layout-profile.md) and
[earlier MathWriting evidence](mathwriting-results.md).

| Evidence | SHA-256 |
| --- | --- |
| Exact packet | `143b173181d10f637af7a860ddd533046b749644ae267510b0edc475d40e53a0` |
| Technical collection | `d15e236e22b25591bd324ba125ac0948982fd166d55dc831868e6c8ff49a1b47` |
| Independent blind score | `e9f705efea0fd46a277d7f35131174f38709c51d62c1d50d77681aa04e44a92a` |
| Root frozen blind score | `f7c0344076dff3b7f1a771744f9d623ce439f61cc6aa11108c66eb24b3c6fd7c` |
| Unblinded result | `aac32b9485534701ab7eff6ace6285ac869ea594cf1a721891a1b55c1f6eb6c3` |

## Original cursive and negative-transfer regression

Experiment `rem26-six-regression-5403ae1-terra-r1` kept the original
`partial-transcription` policy and Hunter/blank/Howe target, context, model,
prompt, profile and HTTP-body bytes. Fresh invocation identities and six-call
bounds were used. Original rows 1, 2, 5, 6, 7, 8 became rows 1 through 6; their
relative execution order remained 3, 4, 1, 2, 6, 5. The original frozen criteria
from [the partial-policy results](results.md) were retained.

| Case, both arms | Observed result | Frozen criterion |
| --- | --- | --- |
| Hunter | Normalized; six facts, 1893 header distinct from June 1892, M. J. Sherman and final `work-` retained | PASS 2/2 |
| Blank | Exactly empty normalized page 1; no formula or unknown-text stand-in | PASS 2/2 |
| Howe | Known Julia Ward Howe and Cordially yours, real uncertain spans, no unrelated recipient/date/unseen beginning | PASS 2/2 |

The independent score was frozen before arm disclosure and agrees with Root's
6/6 assessment. Root's score was only partially blinded: inspection of report
06 while checking `confirmed=false` revealed one Howe arm before Root's freeze.
That limitation is preserved; the independent score remained arm-blinded.
After both freezes, every random sample ID was bound to the actual raw bytes and
product report. Both Hunter arms already recover Wyckoff, so no improvement due
to context is claimed. Printed layout flattening and ambiguous extra handwriting
are separate from the narrow required-fact criteria, not full-page fidelity.

| Evidence | SHA-256 |
| --- | --- |
| Exact packet | `d1424f501dde8242a2f61f86c9f0c4a99b253ffd06a8d998666346c099faa27c` |
| Technical collection | `5c5f80107ded08b3216b1a9b47629232d7a637c09a61e21f31d38746f2ea1455` |
| Independent blind score | `1d639c28978bb6547a302e1511f4c9e0631d8399ff77f227b0008b4cc4dba402` |
| Root partial-blind score | `cdfc95340bbfbe166741d6d40bdccd190c832a3e680da34e79632d512c45e40e` |
| Unblinded result | `655bfe54b02dbbe26f2f6a28973a70ed446bec896695cae8ac974946c3787407` |

## Preserved failures and remaining work

Preparation caught a stale driver row assertion and then an independent review
caught the supervisor's old four-row completion guard. Both unadmitted
predecessors and failures remain preserved. The corrected packet passed all
12 offline actual-binary scenarios and controls of the actual final completion
predicate before any live call. These harness repairs did not change product
code, inputs, criteria or the executable.

All prior math, rendering, Terra/Sol and historical outcomes remain attributed
to their own revisions and spent executions. No unchanged rerun, easier sample,
relaxed criterion or automatic consumer adoption follows from these results.
Positive mathematical recognition remains an unresolved delivery gate; broader
Reader/Writer hooks, confirmed learning, optional sync and native pen-input
integration remain unfinished under their existing contracts.

Raw local receipts are hash-addressed evidence retained by the coordinator, not
public transcript links. Source basis: exact source/CI output, actual bounded
product reports, independently frozen scores and direct retained-target review.
