# Portable preference consumer verification

## Source and scope

Precode e0c3b838ff4dcb9c65455b8e6e36e0de0c675a7b was independently accepted
before source edits. Manager starts from delivered
3f14a0d268ef0b6824756ff503f213d40b41f978. Docs normally reconciles delivered
producer main53cbfe5be4b328a58781a6d2772b5172863b8c3b through merge
a07d8b51843f328b7ef7928658e4a0b5902b4d24; its canonical import specification
and archive are preserved without a duplicate importer. Initial Manager handoff source head is64f45ffffcea81239f94d240672ef9d19e3ba0bf;
review correction successor is a9bb5466fbea508ecd8a3beccb91ff1e3c4a956b.
The full exact revision is recorded in the paired delivery comment.
Exact paired Docs revision is recorded in the delivery comments.

The implementation is one shared file UI/controller, a closed private/public
protocol, fixed wired transport and operation-specific host using existing
MaintenanceIO and peer invalidation. The backend retains all Config overlay,
whole-document validation, family admission, publisher and Store/mode custody.
No direct Buddy API, Config writer, archive/sync engine, service control or native
operation is added. No installed capability is inferred from source delivery or
matching versions; an absent/unsupported producer refuses without fallback.

## Executed local checks

On Linux with Node24.21.0 and Electron44.4.5:

- npm run check: PASS, including ESLint, all1023 Node tests, development styles,
  production build and actual baseline browser/responsive/sandboxed Electron.
- python3 -B -m unittest discover -s tests/portable_configuration -v:4 PASS.
- The original check-json-digests.cjs: all3 Rust artifact byte spans equal Node
  recursively sorted compact bytes; all26 original cases verify.
- npm run package and npm run test:package: PASS for Linux x64.
- npm run test:portable-configuration-hosts and its --packaged mode: PASS through
  real guarded helper/IPC, actual file selection/Blob download and private host,
  including exact actual export bytes, confirm once, original-only Status,
  unknown/reload, Stop, stale cancel/status during a newer owner, frame/arity,
  malformed-file error redaction, packaged resource equality and390px layout.
- Rendered390px browser and1200px Electron views were visually inspected; final
  shared controls use existing primary/secondary styles and show no private values.

Local builds precede the final source commit and truthfully display
0.0.0-dev-3f14a0d268ef-dirty; these are tested working-tree contents, not a clean
release binary or hosted-CI result. Both OS jobs are wired to the new source and
packaged host checks; actual Windows and current hosted checks remain delivery
gates. No tablet, live provider, installed-runtime or native qualification follows.

Docs validation:12 tests PASS, guidance36/preserved126 PASS, and all123 active
OpenSpec items PASS strict validation after own canonical sync/archive.

## Original producer attribution

The immutable fixture directory tests/fixtures/portable-configuration-e5bf3b8
contains the original96-file/120637-byte packet. ZIP transfer44016bytes SHA256
d195a4ba05fa0e0ad9ad7bffc62ceb6005bfbb3f3266dc107b14ff7e5bcec9d1;
original file-manifest.json SHA256
4f69dfca80558fd52cfe56bc5fb6e878d7735f2209022fb849aa32c74a11d76c.
Every95 original manifest entry, raw stdin/stdout/stderr, all26 cases and all3
exact Rust compact artifact byte spans are checked. Inputs are synthetic data;
outputs are actual CLI/Store observations from source contents
e5bf3b8ad7f5681f3f90d7cfc097aee3cae53ca3 / Docs
2087f0cec22ceb405275bda30dcb4271a9a26789. Preserve their original Windows paths
and actual precommit dev.v0.73.0-dirty metadata. They are not relabeled as the
subsequent source merge or a release. The packet contains no producer executable,
cache or Store tree.

The pure phase parser accepts the actual original Windows Config digest as its
explicit test context. Production host transport still binds the single fixed
Linux tablet path. This tests compatibility without inventing Linux/native captures
or rewriting original hashes. Actual export bytes also cross the real host/UI
file boundary. Induced loss/identity/fault/owner cases use separately labeled
synthetic callbacks; no producer operation or Store setup is replayed here.

## Requirements and meaningful controls

Shared explicit workflow: file selection is cleared immediately; raw artifact
bytes go only to private input or the deliberate export save flow, never normal
state/HTML/logs/URLs/storage. Changed names/origins are redacted; no-change grants
no Apply. Whole raw JSON, numeric lexemes, duplicates, types, sizes and exact
private Inspect/Prepare/intent/artifact/Apply/Status correspondence refuse whole
frames. Parser/cyclic input errors are fixed and cannot leak excerpts into IPC.

Custody: one shared owner, original120s grant and eight non-evicted unknowns;
remaining deadlines, after-await identity/generation, old cancel/status versus a
newer same/other lane, retained forget receipt bytes, and no automatic replay.
Both actual host paths test file/UI lifetime. A final verified reply reserves its
original through the last bridge guard; invalidation before publication preserves
unknown. Unresolved followed by transport loss returns valid unknown rather than
an old observation with missing evidence. Status sends only original intent and
never imports again or proves historical publisher/runtime authority.

## Failures and measured budget decision

Git staging initially normalized one captured CRLF comparison log under the existing
text=auto policy. A normal successor adds a fixture-specific -text rule and restores
the original bytes; all95 staged entries plus the original manifest were rehashed
against the original pins before handoff. The captured CRLF comparison log also
uses the existing opaque-evidence diff convention; complete branch diff checks
pass without changing those bytes. No report or provenance was rewritten.
The earlier implementation commit remains in history, not amended into a claimed
original-byte success.

The first Python control expected an exception for multi-frame stdout. The existing
transport correctly returns a sanitized unavailable/null-stdout result. The test
was corrected to assert that refusal and owned channel closure; no production
acceptance was widened. Its initial4-tests/1-failure diagnostic was observed in the
author task; no separate raw log for that initial execution was retained.

The initial actual browser test passed export/import/layout but expected the old
basic editor wording “origins ready”; actual current wording is “Saved settings
ready to edit”. The exact expected label was corrected. The raw failed log and
subsequent pass remain distinct below. A later lint run found two unused fixture
imports; those test imports were removed without source behavior changes.

The original simple presentation compiled but failed650kB initial error budget at
669.82kB. Measured deferred-panel, controller-lazy and dynamic-component attempts
were678.80kB,657.86kB and686.02kB; framework costs did not meet that bound. The final
implementation keeps the existing simple pattern and explicitly changes only the
initial error allowance650→675kB (+25kB,3.85%), leaving400kB warning and all protocol/
privacy/custody bounds unchanged. Final initial assets are670.17kB,115.44kB estimated
transfer. Root independently accepted this measured allowance during review. The failed
budget diagnostics are retained in the author task/paired review record rather
than misreported as passes; there are no abandoned lazy UI/runtime files in source.

## Retained execution log identities

These logs are maintained with the source handoff, outside shipped artifacts:

- check-privacy-final.log: 119028 bytes; SHA256 b8f77802013c647c22858b117f5e6244e4ab1ed534f15affb525030b4f9a4fce
- python-final.log: 810 bytes; SHA256 9234c6c14c104c6e25992af211872f74a6c92f19c6d5a234430d0d8d6c9a82f4
- original-json-digests.log: 1033 bytes; SHA256 7acfc0cdb524d11aff9b0a36890aa792a86e30576d85788069e700fa7c7f82b1
- package-privacy-final.log: 151 bytes; SHA256 0f7d6b2c2fc47cdd3d0dea1bcc1086f18c636085d21737f933832a8cf6e79a1d
- package-smoke-final.log: 115 bytes; SHA256 92cea251f2c1ed0aa5608fe26b9e2f5f7f4a8693fa7881164a2344b0068b13c0
- hosts-source-final.log: 387 bytes; SHA256 ad8674d9a5f8dd15850983f3ac06765ba19e5252dee74f981f8ab0ea76ae1948
- hosts-packaged-final.log: 399 bytes; SHA256 49fec6a549c67078834ecb83e39ac87443128b8e4ccb38f1d2163832b27015a7
- hosts-initial.log: 3632 bytes; SHA256 bc01963c6c55875abeec7c43757983d363a3122bfe869cfaf78ab1d3867395c3
- hosts-label-corrected.log: 387 bytes; SHA256 ad8674d9a5f8dd15850983f3ac06765ba19e5252dee74f981f8ab0ea76ae1948

- package-committed-final.log: 151 bytes; SHA256 0f7d6b2c2fc47cdd3d0dea1bcc1086f18c636085d21737f933832a8cf6e79a1d

- hosts-packaged-committed-final.log: 399 bytes; SHA256 49fec6a549c67078834ecb83e39ac87443128b8e4ccb38f1d2163832b27015a7

- committed-corpus-check.json: 347 bytes; SHA256 d83589cade9f8cf0f8b9c3e64e86486b47bc0fd51c0fc247e09ecde4ab1246d5

- hygiene-closeout.json: 1218 bytes; SHA256 dd46bc7c27d6efc9397169bd7735e27f8f480a4da284098e0c11cab7dbce0fc3

- openspec-final.log: 4401 bytes; SHA256 61905fe36d9e88d753dee72a7dadada192102e49fcf75a6548ca273f4a9540f5

- docs-tests-final.log: 4708 bytes; SHA256 50e549cc2ca9cbd2966093a53279cbb8f6008ace9bdf32e8d3792fc362216ed2

- docs-guidance-final.log: 76 bytes; SHA256 d2b6e1f4de586d5149a23b208f27ee4b4f73b4061bb421ad79e9560aa706d4d6

After final packaged checks, only unused task-owned packaging outputs and the
duplicate extracted transfer packet were retired:301396939 logical file bytes.
Source/corpus, useful logs/screenshots, original small ZIP and active task-owned
review caches/browser outputs remain. Shared caches and protected inputs were
untouched. Logical sizes and separate free-space observations are in the receipt.

## Remaining delivery and limits

Independent implementation review must assess this exact pair and the measured
budget allowance. Current hosted Windows/Linux checks and feedback, coordinated
squash delivery and actual-main/release follow-through remain required. Local
source archive does not claim those checks or production publication passed.
Export is a browser/OS handoff, not proof of durable save/private permissions.
Saved Config readback is not running adoption. Wider installer, credential,
cloud/group/archive/native/tablet and final1.0 obligations remain outside scope.

## Review correction: receive completion, host allowlist and plain copy

Independent review reproduced premature acceptance when exit status arrived before
remote output completion. Five deterministic schedule controls first failed against
the initial collector (9 tests, 5 failures); the corrected collector passes all9.
It reads stdout and stderr nonblocking through actual empty receive results, with
fair bounded chunks and the unchanged aggregate deadline/output/diagnostic caps.
Delayed second-frame stdout refuses the whole result; late private stderr drains
without publication; oversized late diagnostics refuse; absent EOF times out;
valid completion preserves the exact original frame. Possible Apply loss retains
the existing original-only unknown outcome and never retries.

The hosted Ubuntu wired-host failure was a stale exact expected capability list;
portableConfiguration was added without weakening exact-key checking. Inspection
found no other maintained whole-host key inventory. UI copy now explains review,
saved-file observation versus running Buddy, and an import that did not start in
plain language, with exact state assertions and unchanged private outcomes.

Correction checks on Linux: ESLint PASS; all25 focused Node controls PASS; all9
Python transport controls PASS; development and production builds PASS; package
PASS; real wired-host source and packaged checks PASS; real portable file UI
source and packaged checks PASS (browser plus sandboxed Electron each). All8
390/1200px screenshots were refreshed; production browser390 and packaged
Electron1200 visually inspected, with readable copy and no overflow/private text.
Final initial assets670.14kB/115.55kB estimated transfer, within accepted675kB
allowance; unchanged400kB warning remains. Docs12 controls and strict OpenSpec123
items PASS. No tablet/provider operation or hosted Windows success is claimed.

The correction packet retains original failing/passing logs, screenshots, tested
source hashes and normal successor bundles against the published initial pair.
Its manifest/delivery comment identifies exact successor revisions. Earlier
execution evidence and producer corpus remain unchanged. Task-owned node_modules,
Angular cache, browser builds and rebuilt Linux package remain active pending
Root review of this correction; review that retention after integration. No
shared or held inputs were cleaned by this correction.
