# Planned evidence matrix â€” unimplemented

The matrix below originated as planned precode. Historical observations are timestamped snapshots, not current acceptance. Executed observations and
remaining gaps are recorded separately below. Accepted older inventory/cleanup
corpora remain attributed to their original sources, never credited to this change.

- Strict input/parser: all four operations; raw dash aliases; held stdin early
  conflicts/non-Linux; missing/unknown/duplicate/nested keys; unsupported versions;
  canonical UUID/digest/integer/null rules;32768-byte closed output; no sentinels.
- Fixed service observer: exact argv/env/null stdin; inactive/dead/zero acceptance;
  active/activating/deactivating/failed/unknown/missing/duplicate/extra/stderr/nonzero;
  overflow/timeout kill+reap; no service mutation. Use only synthetic child fixtures.
- Existing-only admission: missing/foreign/unsafe/header/root/generation/mode;
  selected format/feature/history; held OS lock and held/named replacement;
  conservative whole-generation entry/byte budgets BEFORE content read/recovery;
  all failures preserve bytes/modes/mtime and stage files; no credentials payload.
- Eligible empty/settled unbound/bound history; shared retained source images and
  historical exports. Typed schema/chronology/source/binding validation; current
  conflicts, foreign binding, schema2 anywhere relevant, unfinished/uncertain
  turn/export refuse; original historical nonterminal revisions remain readable.
- Settled exchange: Interpreted User+later Completed Assistant passes with original
  user bytes unchanged; exact-exchange Failed/Canceled with required terminal facts;
  missing/duplicate/wrong-exchange/mismatched-mode assistant, missing/ambiguous
  same-manifest terminal proof, orphan/outdated/contradictory facts,
  pending/generated/uncertain current turn and ambiguous causality refuse.
- Admission headroom: each4096commit/8192object/manifest8MiB/record32MiB/object256MiB/
  target4096-envelope8MiB boundary before and after exact N envelopes+manifest;
  near-limit prepare/first apply refuses before writes, or reserved original status
  succeeds after reopen. Exercise every object/stage/BeforeCommit/AfterCommit/output
  failure phase, unchanged/partial/full publication; no second apply from partial.
- Cumulative recovery: one16MiB media object referenced by1000 valid manifests must
  refuse before512MiB read work or65536 visits; count every repeated media hash,
  record reread and dependency pass, including preflight and receipt reconciliation.
  Verify actual consumed bytes/visits never exceed the operation budget, no reset
  or unbudgeted fallback; legacy recovery remains unchanged.
- Deterministic original intent/vector and2or3-record atomic transaction; root plus
  binding publication or no visible partial transaction. Exact retry/changed-ID
  reuse, mutex races, changed heads/generation/mode/Config, local-only outcomes.
- Faults before publication vs during/after durable publication; unknown/lost
  stdout; explicit original status; historical receipt/current-state separation;
  matching tombstone without receipt unresolved; no retry/rollback/resurrection.
  After exact publication, append a later retained revision/conflict under a separate
  deliberate fixture action; original apply retry AND status still acknowledge the
  original receipt with current_state=changed without fresh live eligibility or
  current-history equality. Changed Config/mode/unsafe storage still refuses shared
  admission. Own deletion alone must never make original status exceed admission.
- Preservation: all original history/media/source/export records and original
  documents unchanged; existing Ledger::delete and frozen older CLI wires/vectors
  unchanged. Run current normal source/Docs checks and independent review.
- Actual CLI provenance separately: Linux missing/unavailable service refusal;
  Windows unsupported/parser only. Positive injected typed-service fixtures are
  library/model evidence, never actual inactive-unit/native qualification.

After accepted implementation, record exact source/Docs commits, original raw logs,
actual executable identity, separately attributed corpus hashes and only executed
case coverage. Canonical sync/archive/final paired review and actual main/publication
remain separate. No device or real provider/credential/native execution is planned.


## Initial draft implementation observation (not acceptance)
Source a562e6f0420f08e7e080c49fd03603228b3e7217 / tree
feef202a2a7a2817f2502696afb6bd5eee913bd5 implements the proposed producer in draft
Buddy84, paired with accepted precode d89. Fourteen own paths preserve429 other
baseline entries. No SDK/Cargo/lock/older protocol/vector changes occur.

Clean-current Windows fmt/strict all-target Clippy/16 modeled groups/7 binary
checks/3 actual CLI groups PASS. Two ignored synthetic child-helper entrypoints are
explicitly driven by the timeout/overflow wrapper; they are not native tests.
Model cases execute empty and interpreted+completed history, same-manifest terminal
failure, retained source-image bytes and historical binding, lost acknowledgment/
partial objects/original retry/status, later competing revision, commit-entry
headroom, output lock/failure and the16MiB/1000-manifest cumulative-work refusal.
This is Windows fixture logic, NOT Linux directory durability or inactive-unit
qualification. Original Linux Checks120362142320 on CI39937963089 now PASS; the remaining
Build/Integration delivery jobs are still separate.

windows-initial-cli-corpus.json retains19 actual refusal records,38 independently
verified stdout/stderr hashes and4 separately checked intended stdin digests.
Executable e58ce16b054d6f522a0a8c0f93c8feb3cf3f45f207d0cd682e783532e06585a2.
Original raw17008bytes/SHA2569d0cd70685475fc3247fd3b78d93a62af450eff3884a3c749e00bac6a1283927;
normalized15348bytes/SHA256254b5913ec43689f57803dabea4bf6d210f3851320d67d6c90c8b053b1cfd037.
The Linux-compatible actual executable controls intentionally stop at
selector/parser/missing-Config boundaries BEFORE the real service observer; no
actual unit query is run by this work. Positive OS state remains injected only.

### Remaining verification work
The planned matrix above remains a checklist, not a claim of full coverage.
Additional focused controls are still needed for all inventory/byte/target-history
boundary reservations, structural/selected/schema/adversarial ownership and target
variants, full process property/error cases, changed bindings/generation/mode,
receipt corruption and semantic-versus-exact byte matching. Independent static
implementation review and complete source/contract coverage mapping remain open.
Do not archive, synchronize canonical completion or mark delivery ready from these
initial results. Native/provider/consumer/whole-project gates remain separate.

Earlier uncommitted wire/model green runs do not qualify a562. Initial compile
iterator diagnostics and initial strict-Clippy fixture lint failure remain preserved
separately; current clean checks above are new executions after their corrections.


### Original a562 Linux Checks
Original job120362142320 passed445 library tests/3ignored (one preexisting plus two
synthetic subprocess helper entrypoints),7 binary tests,3 new CLI groups and all
maintained regressions/audits. Downloaded original raw job log is658122bytes/SHA256
4a7908b657271595ee97d395e5e3be4875b274d2b2c07d7ffceaf73cd4ce2e97.
Fetched actual clean tested8a6afabb67aa6b67e46afa292504cce47e29c828; its tree
feef202a2a7a2817f2502696afb6bd5eee913bd5 equals sourcea562 exactly.

linux-initial-cli-corpus.json preserves15 original records/30 independently checked
stdout-stderr hashes plus4 separate intended stdin hashes. Actual executable
c79e1981881a692eb81083ad133435000eba31a26ef9deeffa15715b4aa6ef9d;
normalized12626bytes/SHA2565da9b7b20287df1d0238e010e1658159d41b0b101b251f130605b3e49bf4d745.
Actual Linux CLI tests stop BEFORE the real service observer. Positive service/
transaction cases remain injected fixtures; no inactive-unit/native/provider
qualification follows. Initial source remains frozen for independent review;
known/remaining source and coverage gaps above are not cleared by green CI.


## Focused implementation successor367 (review still pending)
Read production review5627043028 and all four findings. Source
367eddeafd1cd4a9ffb68aa443237a89e2e5a38b/tree8a406ac7fddff6e966e759c43a75a4c66a3026a8
changes six paths overa562;437 other entries and frozen vector bytes are exact.
Original admitted header bytes now precede typed constructor reads and remain
bound across recovery and later checks. Raw deterministic manifest digests bind
historical receipt recognition. Every supported schema-one source variant has
bidirectional identity/link validation and summary accounting, without changing
original provenance. Config/storage checks bracket the observer; deadline timing
begins before process spawn. No actual unit query or device operation occurs.

Current CLEAN367 Windows fmt/strict all-target Clippy/22 modeled groups/7binary/
3actualCLI groups PASS. These executions are new, not relabeled a562 runs.
New models exercise five header classes during recovery and same-length/time-
restored content changes, both original operations after raw manifest formatting
rewrite, four source variants through existing synthetic producers and12 orphan/
foreign/changed-turn refusals, and final-observer Config changes before and after
publication. The Unix final-observer inode-replacement control remains for current
Linux CI39942259765. A missingCursor test-helper compile failure is retained
separately; it is not a passing result.

windows-current-cli-corpus.json retains19 current records/38 output hashes and4
intended stdin hashes. Clean executable
e3a0ff9dee80e958404d4c6abfc10e3d7a4e87a9a7dfaca01b067cab40e96254;
raw17008bytes/SHA256c3b2815a7e31206a51d5f88989e160cf3020a6d677e6b54709fbaf39dd937541;
normalized15348bytes/SHA256254b5913ec43689f57803dabea4bf6d210f3851320d67d6c90c8b053b1cfd037.
Equal normalized refusal records do not merge the two source/executable identities.
Originala562 CI39937963089 completed Title/Checks/Build/Integration PASS with PR
Release skipped; it does not qualify367. Broader boundary/coverage mapping,
independent successor acceptance and paired lifecycle remain unfinished.


## Focused367 acceptance and coverage successor
Independent source review5627336291 accepted the four production corrections at
367; its full normal run39942259765 subsequently passed Title, Checks, Build and
Integration (PR Release intentionally skipped). Original watcher79791 exited0.
The original Linux raw658843bytes/SHA256
f456930658879275e32ea09fd4edb36e1c65cce9fc183c9a5e6391df162e5b9b
and linux-current-cli-corpus.json preserve15records/30output hashes/4stdin hashes.
Tested42609ed093d6f260fba4998a0e48a8c6bb0bda64 has tree8a406ac equal367.
This closes the earlier focused367 review/Linux gaps, not the whole feature.

Successor8f865ff5ff19b527832edf6aed4089ffd9f7407e/tree
0105c5aab26e14779b23d4a6ae32cbe4b068fb06 adds five paths of change over367,
preserving439 other entries and both original vector bytes. Production changes
are limited to acknowledging only the complete original manifest/receipt while
allowing exact derived objects under another manifest to produce unresolved
partial-state observation, and refusing an already-used operation receipt ID at
preparation. The matching-tombstone/missing-original-receipt case was reproduced
red on367 (Conflict instead of required Unresolved), then corrected. It can never
acknowledge or dispatch another publication from partial state.

coverage.md maps contract areas to named actual-source controls and explicitly
distinguishes numeric capacity models from real-store/physical commit-boundary
execution. Added synthetic process, wire, structural/mode/schema, exchange/fact,
source/binding/export, receipt-corruption and publication/output controls preserve
original logs. The third expanded WIP run35PASS/1FAIL had an overly narrow test
expectation: corrupt original object refusal is Unsupported during safe admission.
No production correction resulted. The fourth WIP39PASS/2driven helper entrypoints
passed. The fifth WIP40PASS/1FAIL attempted a competing binding branch via ordinary
local commit, which correctly rejects stale parents; corrected fixture uses the
existing import path, and its focused test passed. Final WIP strict Clippy passed.
These failures remain failures; none qualifies the committed successor.

Clean-current8f865 fmt/strict all-target all-feature Clippy/model/bin/actualCLI
qualification and normal39968879386 CI are in progress. Independent implementation
and coverage acceptance, own canonical sync/archive and final paired delivery
review remain open. No a562/367 result qualifies8f865. No actual unit query,
tablet/provider/real credential or runtime/native qualification was performed.
