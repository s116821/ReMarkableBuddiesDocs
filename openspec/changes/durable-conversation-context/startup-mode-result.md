# Persisted-mode application admission result

This is a bounded REM-37 application increment. Live local mode switching, active
isolated/shared publishers, account/root/provider and native qualification remain
unfinished. No merge, canonical sync, archive or whole-feature completion follows.

## Exact source and dependencies

- Rust `62a5376f3e14d06a5666c61b96dc6ad1bd35aa87`,
  [draft PR35](https://github.com/s116821/ReMarkableBuddies/pull/35).
- Paired [Docs PR18](https://github.com/s116821/ReMarkableBuddiesDocs/pull/18):
  precode `48d748b`, frozen cases `a5da6b3`, all-root clarification
  `f51a5c88e2b272f43eaacf2452a8fcb6b4989460`.
- Bases are the reviewed runtime Rust `4d539b8` / Docs `4ef142c` in PR34/16,
  themselves dependent on unmerged PR30/33 and Docs6/15.
- Relevant generic source is independently accepted repaired mode
  `7987da337a78be32d4ed3a41524e3853e925abcf` / Docs `df7cb0e`.
  Mode module raw Git blob `88134fbb208b37692e5421cc818127962662634f` is exact.
  Adopted plumbing is 40 added/4 removed lines for Store mode/publisher counters,
  the composed legacy publisher lease and existing Drive ID validation visibility.
  No outbox, slot/transport, archive, Cargo/config or domain-schema merge occurred.

Final normal LF source archive ZIP SHA-256 is
`79cf2759b30029caf91703049225d1944d088b7a90b9871cacbed45076606782`.
Eleven raw Git Cargo/source/test blobs are verified, including the exact generic
mode module. Committed SDK remains `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`;
protected working SDK/native changes are not the qualification input.

## Actual behavior

The real startup decision returns an admitted ordinary ArcStore or the fixed
private report. Existing Store mode is checked before credentials/model/device;
the same admitted Store survives credential resolution into actual Ledger,
memory and Worker construction. A final ordinary check precedes device/model
creation; config/effective-source snapshots remain after credentials.

Unconfigured mode retains legacy compatibility and grants no shared authority.
LocalOnly permits ordinary local data with sync disabled, while an explicit reader
selector or contradictory old publisher is unsupported. Isolated startup is
unsupported until its matched implementation exists. Shared mode requires explicit
matching reader group/binding, and still returns the committed SDK's typed
NoNativeAdapter after strict conversation validation. Missing/mismatched selector
refuses without a legacy fallback; malformed mode is unavailable, contention busy.

Fresh ordinary deferral requires data, cache and credential roots be absent or
safe empty directories. Partial/non-owned/foreign auxiliary state refuses before
credentials and data creation. Deferred creation repeats fresh checks, preserving
foreign bytes if state changed. The existing maintenance initialization policy is
unchanged by this startup-only rule.

Configured shared inspect and no-data ChoiceNeeded context retain the real matched
mode lease alongside payload/token/raw-custody pins, domain/Store admission and
the same cumulative budget through the actual writer. The lease blocks mode
transition until it is dropped. It supplies no provider/root/catalog/native
authority. LocalOnly/None have no application read-mode lifetime lease; live
ordinary-loop epoch fencing remains open and is not inferred from a startup check.

Historical pending recovery bypasses current mode/epoch admission, including a
departed/rebound group or corrupt current mode file, while preserving independent
configuration scope/original request/Store custody checks. It grants no current
mode permission, publishes nothing and returns no live token. Pure invalid/foreign
input still wins before a held Store can produce Busy.

## Independent findings and focused evidence

Sol accepted the precode architecture and frozen routing/private-status/input/
context-lifetime/historical-bypass/Store-reuse cases. Source review found a P2 in
initial candidate `6025d95`: Fresh inspected only the data root and could resolve
credentials/create data before rejecting foreign auxiliary roots. Corrected
`62a5376` adds startup-only all-root validation and deferred revalidation. Sol's
exact repair re-review accepted the cumulative source and test assertions with
no remaining scoped source finding. This is read-only review, not an independent
rerun or archive-hash recreation; original candidate/finding evidence is preserved.

Working-input evidence passes all 14 actual runtime CLI controls (13 prior/current
plus the new fresh-auxiliary control), runtime unit controls and extended historical
recovery. New behavior includes mode matrices before poison credentials, wrong/
missing shared selector, corrupt mode/partial state, LocalOnly publisher conflict,
invalid-input-before-busy, shared ChoiceNeeded lease exclusion, admitted ArcStore
identity, and original recovery after mode departure/rebinding/corruption.
Fresh-auxiliary test contains 12 meaningful cases: absent/empty data times cache/
credentials file/nonempty/stale-owner states, with unchanged foreign bytes/no data
creation. Deferred unit covers safe-empty positive and changed-state refusal.
Counts are included in final suites, not additional full-suite totals.

Exact final archive formatting and ordinary nonmock library/binary check pass,
exit 0. The same-source jobs-two locked/offline all-feature retry passes Windows
Rust 1.98.1: 293 library tests/one existing ignored, all binary/integration/
compile-fail doc suites, including all 14 runtime CLI controls. Existing generic
mode fixtures are included with their separate source attribution. Required strict
Clippy fails on 23 inherited dead-code errors, exit 101, without suppression.
The complete all-target warning diagnostic has exactly 23 warnings, all dead_code,
with no new runtime/CLI diagnostic. Its command-local warning cap collects the
remaining target diagnostics; it does not waive or pass the strict failing gate.
The first
full local build failed Windows paging-file/mmap resource exhaustion (error 1455),
not a passing qualification; preserved same-source retry limits build jobs to two
without changing system settings. Earlier `6025d95` is not substituted for the
repaired final source.

Hosted source run `38324189476` Test `115059000752` passes Linux 297 library
tests/one existing ignored and all suites/runtime CLI14. It checks ordinary merge
`825a7428375981d23cc82c1001e6e5f20b282893` of `62a5376` into `ff8ad75`, distinct
from the exact normal archive. Completed lint `115059000853` fails on the same 23
inherited errors; overall CI is unsuccessful, policy/title pass and tablet builds
are not qualified after the failed earlier step.

Docs local 12 tests/checker 19 guidance+126 preserved blobs/strict 17 items and
hosted `f51a5c8` and result revision `928407c` Ubuntu/Windows/OpenSpec checks pass.
The independent reviewer accepted the bounded final source/result evidence after
reading the completed local and hosted logs, independently parsing all 23 warning
diagnostics and verifying hosted jobs and draft PR pointers. This was an evidence
review, not an independent full rerun or recreation of the archive hashes.
Scoped task 3.12 is complete; this final documentation amendment still requires
its own hosted checks and paired publication readback.

## Remaining authority and source basis

No mode setter, bootstrap/account work, sender/apply, IPC, provider/model or tablet
operation is enabled here. All nine protected hashes/pins remain exact. Held 8112
transfer/activation/equivalent replay is untouched. SDK-native source admission,
Reader effects, tokenizer/live effectiveness, real publisher/provider qualification,
live local mode switching and full task 2.10/lifecycle/MVP gates remain open.

Source basis: exact code/blobs and actual owner local/hosted outputs, independently
attributed source/assertion review and separately accepted generic primitives.
Private logs/review chat have no public transcript link. No stored or synthetic
data is promoted to native/current-provider permission.
