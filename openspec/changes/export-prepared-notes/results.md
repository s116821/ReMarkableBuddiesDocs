# Prepared export verification record

Implementation `65481cda93eb095bb1e43200539a54354ec8817e` retains core
`5a1e0f88c0991d7d0dd0ad70098901b3c795597f` and is based on delivered
Buddy main `cc317ff53e1dd6f612b2e82707e5a5e4b50e0265`. This coordinated Docs
change starts at main `6f7f1d4cb33ff4ca9c0326b1bb248ddc8cfd139e`.

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

Design review accepted the bounded scope with no-send successor and live-owner
corrections, which are implemented and exercised. Exact final source/evidence
review, required hosted checks, coordinated spec sync/archival and linked PR
delivery remain pending in this record. No live Mem account write, live model,
installed Reader/Writer or tablet qualification is claimed. Extraction/OCR,
generation, refinement UI, gestures/native pages and whole Writer acceptance
remain unfinished outside this increment.

Source basis: committed implementation, actual local HTTP/Store/command outputs,
retained initial failures, current central design and directly inspected official
Mem documentation linked in the research note. Private review/logs have no public
transcript link. Verified-current is an observation of desired content, not an
external-call execution or native authority claim.
