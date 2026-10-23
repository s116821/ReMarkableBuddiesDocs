# Verification chronology and current candidate

This matrix originated as unimplemented precode. Source66d46ee/Docs0179557 establish
the baseline; the completed v0.29.0 deletion delivery stays separately attributed
and closed. Uncommitted source WIP began only after full483/1e423 precode acceptance.
The following initial sections retain their historical precode/WIP status. The
current-candidate section below records subsequent executions separately. No real
unit/provider/credential or tablet action has been executed for this change.

- Independent report vectors: exact13-field encoding, constants, empty/two IDs and
  too-large/unsupported refusals; independently recompute UTF8/newline hashes.
- Early CLI: every recognized conflicting execution/override selector, non-Linux
  held stdin without EOF, unexpected input/value, missing Config; actual Linux
  controls stop before the real fixed observer. Retain clean source/tree/executable
  identity and independently verify output/intended-input hashes per platform.
- Complete discovery: no roots, one/multiple roots, deterministic lexical order,
  singleton tombstoned/all-deleted history, >16 retained but <=16 current,
  exactly16/17 current roots and no truncated prefix. Root type reuse, current
  root conflict/value+tombstone branches, unsupported schema/identity/shape and
  malformed/corrupt owned files refuse without fabricated empty state.
- Eligibility boundary: valid root with pending or conflicted non-root turns may
  appear; existing fresh inspect/prepare still rejects ineligible selected history.
  Native bindings/source/export facts are not promoted or emitted.
- Existing-only: absent/foreign/unsafe/header/generation/format/mode, held/replaced
  lock, Config drift and final observer race. Preserve bytes/modes/mtime where
  examined, original documents, all history/media and stages; no repair or cleanup.
  Unknown orphan partial-deletion objects refuse this no-intent inventory while
  original deletion status retains its separate supported reconciliation.
- Work: one sticky content/visit budget across admission, all retained record/root/
  head visits and output validation; exhaust before typed decoding; no per-root
  reset or fallback. Check the independent Config maximum five-read straight-line
  schedule and existing1MiB per-read cap separately; never credit it to the Store
  meter. Likewise check at most two original mode loads, each8MiB plus EOF and
 4096 transitions, independently of the Session meter; no per-root/retry/final
  mode load. Global publication headroom is not required. No new I/O stress
  or native/power-loss qualification is implied by numerical models.
- Output: closed shape/caps, no text/path/native/private sentinel, final custody
  failure clears arrays/counts; partial stdout failure emits no second report and
  holds leases until failure returns.
- Compatibility: all previous vectors/reports/defaults remain exact. Exercise
  focused deletion admission/report/partial/receipt/custody cases if shared helpers
  are changed, plus normal maintained CI. Do not rerun closed release qualifications
  or credit older source executions to this change.

After precode acceptance, record only executed cases with exact current source/
Docs identities, original failures and separately captured CLI corpora. Independent
implementation review, canonical sync/archive, final paired review and actual
merge/main/tag/provenance observation remain unchecked. All live-unit, tablet,
provider/credentials, Manager consumer and native/runtime gates are separate.

## Focused precode budget clarification
Read full independent483 review5630742024. Its report/classification/custody design
is accepted; implementation has not begun. A subsequent source audit distinguishes
the released Store budget from Document::load/check's separately bounded Config
reads. The focused successor names the maximum five Config reads and leaves every
owned-storage/root-decoding limit, report field, vector and older wire unchanged.
Independent focused confirmation on the current successor remains required before
source edits; older483 validation/acceptance is not silently relabeled.

## Initial source WIP and ancillary mode clarification
Read full focused1e423 acceptance5630828999 before source edits. WIP implements a
separate opaque report, new metered root classification, inventory-only five-read
Config counter and a private custody setup helper preserving the old Doc/original
Plan-before-Store order. The first frozen-report unit group passed. Initial binary
run7PASS/1FAIL used an invalid generic log-level specimen and stopped at value
validation rather than the intended conflict; corrected the fixture to valid info.
Initial model run53PASS/1FAIL/2driven helper entrypoints failed because its Windows
fixture tried to read the held lock file while taking a preservation snapshot;
moved that comparison before/after the held interval. Both original failures are
retained, not relabeled. Current second model/bin executions are not yet qualified.

Further source audit identified the existing mode reader as another independently
bounded admission component outside Session::Budget. The focused wording names its
two fixed8MiB/4096-transition loads while preserving every Session/new-root work
bound, old mode behavior and report/vector. This attribution needs current focused
confirmation before implementation qualification. No new mode helper behavior,
mode setting, provider, candidate CLI or device execution follows.

## Frozen implementation and current Windows checks

Read full focused mode acceptance5631232663 at Docs167fc49 before qualification.
The source candidate is `4d4d9e7049eefa8c0cd7caf13abf352b810f8b22`, tree
`5d0d8c59868b9fc7af95cd6fd4d009d04ba148de`, paired source PR85 and Docs PR87.
Exactly eleven paths differ from actual66d46ee; all438 unaffected base entries
are identical. Cargo manifests/locks, SDK, credentials and older report vectors
remain exact. New report vector blob2c8d2583dc8807717724f1205449b3cf1dd1d657
equals accepted Docs167fc49. The source checkout stayed clean during qualification.

Current Windows results: fmt including the separately included test file, strict
all-target/all-feature Clippy,55 focused library groups (two driven helper
entrypoints ignored),8 binary groups and3 actual new CLI groups PASS. The binary
fixture iterates every existing argument for recognized conflicts. The new CLI
controls exercise missing Config/non-Linux boundary, eight recognized conflicts
and two ordinary parser errors, with stdin held open without EOF until process
exit. No Linux control reaches the fixed real observer.

`windows-early-cli.json` retains11 records/22 independently verified output hashes.
Executable SHA2567fc4e0c64cf7429b38ef8d1834fe48b838f7de204f419b23ed9a9b3ce9857ff4;
original log8411 bytes/SHA25683391b6610db78571dfb38359ca96e268bde2f0ee2924b74dcb6d926e084afce;
normalized6953 bytes/SHA256b06b7091e665dbdab6164163dabd720a082cb38c96b54f41692670c98f1f63c9.
There are no intended stdin bytes/hashes; the stdin property is held-open refusal.

Coverage in `inventory_tests.rs` maps to the matrix above: empty/sorted16/17 and
18-retained15-current/deleted roots; pending/conflicted descendants and separate
prepare refusal; other namespaces/untyped tombstones; root fork/mixed heads/type
reuse/schema2/malformed identity; byte/visit exhaustion before the real typed
decoder with a negative control;4096 stage-entry read-only admission without
publication headroom; original-document/stage/bytes/modes/mtime preservation;
orphan partial refusal versus original status reconciliation; existing-only held
owner/missing lock/bad owner/unsupported mode/feature/format; explicit LocalOnly,
oversized Config before observer, final Config/observer/named-lock races and
partial output failure holding custody on complete and discovery refusal.
Unix named-lock replacement remains a Linux execution obligation, not a Windows
pass. The explicit five-read counter is exhausted at final output and refuses
further checks; legacy Document paths retain their original unlimited schedule.
Mode admission's two fixed existing loads are checked by source call structure,
not credited as a new numerical stress execution or mode subsystem change.

All original WIP failures remain retained:7/1 binary invalid log-level specimen;
53/1 first model snapshot attempted to read a held Windows lock;53/1 second model
snapshot found initializer timestamp rewrites of contract-v1.json/capabilities.json
with unchanged bytes. The held-owner fixture now uses existing-only Store opening;
focused correction passed. Later WIP54-group/8-binary/Clippy and added namespace
group stay attributed to those executions rather than the frozen candidate.

Normal current source CI40009718330, original Linux corpus verification,
independent implementation/coverage review, canonical sync/archive and final
composed review/delivery remain pending. The old deletion CLI regression is run
separately at this source head because custody setup is shared. Existing deletion
Config matching/Plan construction still precede Store admission; no released
wire/default is extended. Native/runtime/installed UI/consumer behavior is unverified.
