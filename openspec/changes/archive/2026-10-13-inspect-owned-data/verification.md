# Named capability verification and scoped archive

October 13, 2026. Source0d440902 continues parentb085b368; the inspector patch is
unchanged from6b1b9fd. Exact corrected delta9ca1de7 was independently accepted
before canonical sync. This verifies only the bounded inspection capability.

| Verified requirement | Implementation and evidence |
| --- | --- |
| Nonmutating owned-data inspection | Existing read-only nonblocking lease, typed owner/format/current checks and path guards; actual busy/missing/foreign/changed/unsupported and nonmutation tests. |
| Honest bounded category and shared-byte accounting | Globally bounded known-path inventory, per-generation apparent path charges, nonadditive namespace references and explicit omitted/missing/uninspected/partial states; actual shared/retained/schema2/tombstone/limit/sentinel cases. |
| Inspection-only CLI admission | Early versioned JSON route before dotenv, credentials, Store/runtime/provider/sync/device; three real CLI cases and retained argument-interface tests. |
| Read-only storage CLI route | Same implemented early route and unavailable/busy/report semantics; no service/native operations. |
| Runtime startup and configuration | Corrected actual argument-parse/inspection-return/ordinary-dotenv order; all four existing scenarios preserved verbatim, ordinary precedence and simulation isolation retained. |
| Existing diagnostic flags | Exact current parser flag/conflict set includes inspection and no invented config flag; all three original diagnostic scenarios preserved verbatim. |

Bare-head Windows checks passed required strict all-target/all-feature lint,
formatting,16 filesystem inspection and3 actual CLI tests. Associated hosted CI
38419851583 passed Test, Check Build & Lint and Release policy using normal PR
merge067192c, with the Linux FIFO case and both target cross-builds. Cross-builds
are not native tablet qualification. The earlier same-head hosted run is not
counted as additional scenario coverage. Local and hosted evidence remains
separate from the reviewer's source/spec inspection; no review rerun is claimed.

Canonical sync creates three owned-data requirements, adds one runtime route and
replaces only two runtime requirement blocks in place. A scoped comparison asserts
every unrelated platform-runtime block is exactly preserved, requirement names
are unique and canonical files contain no delta-only markers. The eight named
implementation/verification tasks are complete. Only inspect-owned-data is moved
to this archive; durable-conversation-context remains active and unchanged by the
archive. The three original unchecked broader obligations are retained in
[external follow-ups](external-followups.md), not declared complete.

Final synced/archive source agreement, links and required Docs validation require
review in this same paired delivery. Root retains parent readiness and final
coordinated review/merge; no issue-wide REM42/Reader/native/release completion or
merge permission follows from this bounded archive.

Source basis: current source/Git and canonical merge comparison, actual owner
Windows outputs, hosted job evidence and independent precise capability/delta
review. Internal review has no public transcript link.
