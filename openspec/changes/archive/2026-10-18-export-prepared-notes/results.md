# Prepared export verification record

Implementation `65481cda93eb095bb1e43200539a54354ec8817e` retains core
`5a1e0f88c0991d7d0dd0ad70098901b3c795597f` and is based on delivered
Buddy main `cc317ff53e1dd6f612b2e82707e5a5e4b50e0265`. This coordinated Docs
change starts at main `6f7f1d4cb33ff4ca9c0326b1bb248ddc8cfd139e`.
Final Buddy `0b935880b88198a7c514bc827830f3148e9d5519` changes only the
reference link to this permanent canonical contract; production and tests remain
at the accepted revisions above.

## Implemented scope

The production library and bounded `--export-note` command consume explicitly
prepared Markdown. Mem uses the real bounded HTTP client, official v2 endpoints,
exact title correlation, verified native IDs and version-conditional updates.
The same body/marker already present yields verified-current without another
PATCH. Useful prepared content remains unchanged; there is no machine-ID footer.
Scope/revision/effect/digest facts stay in the existing Ledger association.

Schema-two attempts keep stable note identity across deliberate new export
operations, with expected-head checks, immutable stage receipts and bounded
retained-revision lookup for old operation retries. A shared same-Store owner
excludes overlapping senders/reconcilers without holding the index mutex over
HTTP. Positive no-send cancellation/failure permits a new deliberate operation;
unknown post-dispatch or crash states require known-ID reconciliation. First
future-poll observation separates positive pre-poll cancellation from possible
dispatch. A readback describes desired content, not proof that one HTTP call ran.

The format-one Store and offline JSON contract explicitly admit domain 2 only
for export associations. Other namespaces still refuse version 2. The Ledger
refuses schema-one attempt payloads and schema-two legacy shapes; old schema-one
records retain their original serialization. Older consumers must refuse the
new domain version rather than infer compatibility from envelope format 1.

## Executed evidence

Local Windows checks used rustc 1.98.1, locked dependencies and offline mode.
The HTTP cases use an actual loopback server and actual Mem transport, with
invented fixture content/credentials; Store cases use owned temporary roots.

| Check | Actual result |
| --- | --- |
| Focused prepared export suite | 12 passed, 0 failed, 0 ignored; final run 0.79 seconds |
| Existing historical Ledger regressions | 20 passed |
| Existing shared Store regressions | 15 passed; an internal subprocess result is included, not an additional test count |
| Affected binary command-interface unit tests | 5 passed after the independent review correction |
| Ordinary binary/library checks | Passed |
| Strict all-target/all-feature Clippy | Passed, no warning suppression |
| Formatting and diff checks | Passed |
| Targeted strict OpenSpec and documentation/provenance checks | Passed |

The focused cases exercise actual HTTP create/find/update and Store reopen,
two-page chronological discovery with reserved cursor characters, same-ID
re-export with changed source revision, no-write same-body completion, old
operation replay and changed-body refusal, metadata-capable alternate backend,
duplicate/missing markers, incomplete inventory, external edits and conditional
version races. Lost response and post-dispatch cancellation reconcile without
another write. Cancel-before-send and cancellation before the first write poll
permit a new deliberate operation; concurrent same-Store Ledger calls return
Busy. A lost local preparation acknowledgment cannot become fresh dispatch on
retry or restart. Cross-schema payloads, other-namespace version 2 and stale
expected heads refuse without an external effect. The real command's missing-key
path emits a sanitized report without starting Reader or echoing note content.

The initial suite recorded one pass/seven failures because the inherited generic
Store and JSON contract admitted only domain version 1. That result is retained;
the scoped domain admission/delta corrected the actual integration gap. Later
eight-, ten-, eleven- and final twelve-case runs are distinct records, not
relabeled predecessors. Earlier footer-bearing evidence does not stand in for
the final footer-free source. Private raw logs and source hashes are retained by
the owner without public download links.

Independent review caught the existing binary's exact-interface test still
expecting the old flag list. The initial hosted run at the core revision also
recorded that assertion failure (three passed/one failed). The test-only
`65481cd` correction includes the new flag/default and mutually exclusive modes,
with no credential echo. All five affected binary tests passed; the frozen
initial source/results remain retained. No production export code changed and
the HTTP/native matrices were not repeated for that interface-only repair.

## Remaining delivery and product boundaries

Independent review accepted the bounded source at core `5a1e0f88` plus test-only
`65481cda`, verified every frozen file against its hash/Git blob and inspected the
actual result logs. The binary assertion finding is closed. The
[public source review](https://github.com/s116821/ReMarkableBuddies/pull/61#pullrequestreview-5561571620)
records that scoped acceptance; this is owner execution and reviewer inspection,
not a reviewer test rerun. The coordinator subsequently inspected final Docs
`14f56007e7e854c6363d7afbf2aa9630c2ffa17b` canonical/archive correspondence and
the Buddy link-only change without another finding. Buddy
[run39101748006](https://github.com/s116821/ReMarkableBuddies/actions/runs/39101748006)
at `0b935880` passed Title, Checks, application Build and Integration; Release
was skipped. Docs
[run39101751778](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/39101751778)
at `14f5600` passed Ubuntu, Windows and all31 strict OpenSpec items. Raw hosted
logs were retained and inspected, not inferred from a prior source revision.
No unresolved PR review-comment finding surfaced at final inspection. This last
results/tasks-only update requires its own Docs checks before normal coordinated
squash. The paired PRs are
[Buddy61](https://github.com/s116821/ReMarkableBuddies/pull/61) and
[Docs57](https://github.com/s116821/ReMarkableBuddiesDocs/pull/57).
Coordinated squash delivery remains pending in this record; the canonical
sync/archive is in the same paired PR and is not itself a merged delivery claim.
No live Mem account write, live model,
installed Reader/Writer or tablet qualification is claimed. Extraction/OCR,
generation, refinement UI, gestures/native pages and whole Writer acceptance
remain unfinished outside this increment.

Source basis: committed implementation, actual local HTTP/Store/command outputs,
retained initial failures, current central design and directly inspected official
Mem documentation linked in the research note. Private review/logs have no public
transcript link. Verified-current is an observation of desired content, not an
external-call execution or native authority claim.
