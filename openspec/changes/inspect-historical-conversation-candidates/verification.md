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

## Compiler compatibility successor

Original source4d4 current Linux CI40009718330 failed strict Clippy before tests:
the newer runner compiler deprecates the newly introduced atomic fetch_update
method. Local Rust1.98.1 passed; the manifest MSRV is1.96. Original full Checks
120606739524 log127329 bytes/SHA2568762f19018d4ef5640748963c6638480b88df7203f36d5eb25436ea39997b0a4
is preserved unchanged. There is no Linux test/corpus/build qualification from
that failed run, and it was not rerun at the failed head.

Successor `c81403c5e45c45e0229c5537f15ab0288149f674`, tree
`d139b62bfebdc26c00687b1e7160007b7ccf925b`, changes only engine.rs7+/1-;
448 other predecessor entries remain exact. The counter uses load/checked_sub
and one strong compare_exchange. Exhaustion/contention returns before file I/O,
with no retry, zero wraparound or fallback. Five maximum reads and legacy None
behavior remain unchanged. No compiler/manifest/lock/settings update is needed.
Fresh successor qualification and normal CI40010340559 remain required. Earlier
4d4 Windows corpus and all WIP results keep their original source attribution.

## Independent output-classification finding and correction

Independent review5633370821 found discovery work exhaustion was correctly
classified unavailable internally, but the final generic custody check mapped
the same sticky exhausted budget to conflict. The original discovery-only test
did not exercise emitted output. This was a confirmed coverage gap, not a new
requirement or an actual Store change. Original red end-to-end test emitted
conflict instead of unavailable and is retained unchanged; the first byte case
failed before its visit loop case ran.

Frozen successor `7257defa50961d57e8737ec2e7ca0b68228a0089`, tree
`ae4febb694706aaa1b6abcb3f87dd8d2b2548617`, changes four paths116+/4- overc814.
Budget errors now carry a private typed WorkExhausted marker, keeping original
messages and sticky limits. Existing deletion custody/error classification stays
unchanged. Inventory-only initial/final custody maps this marker to unavailable;
real Config/named-lock changes still map conflict. The meter is never reset,
validation is never bypassed and custody stays held. A private admission helper
has a production no-op and a test-only pre-discovery limit hook.

Corrected WIP end-to-end byte/visit exhaustion test passes and checks held Store
lease inside the actual writer. Current successor adds real Config changes after
both exhausted-discovery cases and Unix named-lock replacement after both cases;
these must remain conflict. Fresh frozen-source checks, normal CI and focused
independent correction acceptance remain required; the prior green WIP does not
qualify7257 or its additional controls.

c814 separately passed clean Windows fmt/strictClippy/55 library/8bin/new3CLI and
old4CLI groups. Its11 new inventory records/22 hashes are independently verified
in `windows-c814-early-cli.json`, retaining executable2f340ff26d852b39a4c6b1ad852e8d2609265457c7cc55d3372b12d7fc957366.
The combined original new/old CLI log46488 bytes/SHA25603a22ad0938566dbd7e425692c9f3fc32f9feea70db50b38fc5bd51341b230ae
is distinct from4d4's log; normalized inventory bytes6953/b06b7091 remain equal.
Those executions remain c814 evidence only. No tablet/real-unit/provider action.

## Current7257 Windows qualification

Clean frozen7257 now passes fmt/included-file formatting, strict all-target/
all-feature Clippy,57 focused library groups/two driven ignored helpers,8 binary
groups,3 new actual inventory CLI groups and4 old deletion CLI regression groups.
Both byte/visit discovery-exhaustion cases emit unavailable through the actual
writer with custody held; both real Config-change controls remain conflict.
Unix replacement controls remain pending Linux execution. Original red1377bytes/
SHA256e6475c151533b3a7fb6a9c1a931a4eb88d53e07822446863010be331053e6624
and corrected WIP green621bytes/SHA25684bc66bfb9599d9818477cf0c36aa34591fd952dd7dd0e23a65181a52fc5128e
remain separately retained; neither is relabeled as a frozen-current execution.

`windows-7257-early-cli.json` contains11 records/22 independently verified output
hashes, source/tree7257/ae4f as above, executable779180d4495f13d233e22f7e84fd4c7054696ea752d6a59aae0301e490bad65c.
The original combined new/old CLI log46488bytes/SHA2567918091277fbb7d501c30220ff2bf6d1eecc453f6f8ea11e11db005aa7037730
is retained; normalized inventory6953bytes/SHA256b06b7091e665dbdab6164163dabd720a082cb38c96b54f41692670c98f1f63c9.
All source files remained clean. No actual Linux control invokes the real observer.
Current normalCI40011265841 has passed newer-compiler Clippy and is executing its
maintained full test suite; current Linux evidence and full CI remain pending.
Focused independent implementation/coverage acceptance, own canonical sync/archive
and final composed delivery remain subsequent gates. No native/runtime claim.

## Current Linux checks and retained execution proof

Source7257 CI40011265841 Checks120612016387 passed fmt, strict newer-compiler
Clippy,489 library tests/three existing driven ignored helpers,8 binary tests,
all maintained suites including3 new inventory CLI/4 old deletion CLI groups,
and normal release-tool/fixture checks. Both Unix named-lock replacement controls
passed, including replacement after byte/visit discovery exhaustion; the emitted
unavailable and real Config-change controls passed too. This is controlled OS/
Store fixture evidence, not a real service/tablet execution.

Original full Checks log695222 bytes/SHA2560ec422b2235092adcf97a16f7f777783e8413f88cc9e8e1ae81850b20d0aa25f
is retained unchanged. `linux-7257-early-cli.json` has11 records/22 independently
verified output hashes, executablee6a5dfec005717270dad7551095ef6f7126474f5b59b814f9ca66ed6b95b9eac.
The actual clean CI checkout is mergef942c51b506beded3a2decf0132c5277a8ccf3f1;
its fetched commit treeae4febb694706aaa1b6abcb3f87dd8d2b2548617 exactly equals
reviewed7257. Parents are actual66d46ee and reviewed7257. Normalized corpus6913
bytes/SHA2566aea9617a5143c4ac0a59ec3f023efd82378fe0ed05567a4b04c2a6d16d672c0.
The held-open-stdin early refusals never reach the production service observer.

Independent implementation/scoped coverage acceptance5633465661 and paired Docs
evidence acceptance5633488580 were read in full. The original finding was replied
to and its thread resolved after correction acceptance. Earlier4d4/c814/WIP
executions remain separately attributed. Historical c814 Checks passed486 library
tests/three ignored; its original694995-byte log/SHA2560241de1bae50b3e496cd3665179383bde673faa09fee3934b31dc2baa201e66f
and11-record/22-hash Linux capture remain separately private, not7257 evidence.

Current7257 normal Build/Integration remain pending, so full CI and own canonical
sync/archive are not yet complete. No new producer execution, package download,
tablet/provider/credential action or runtime/native/Manager claim was added by
these saved-byte/hash/tree verifications.
