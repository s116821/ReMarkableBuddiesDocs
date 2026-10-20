# Selected executable startup and historical recovery result

This is a bounded REM-37 increment. Native Reader admission/effects, tokenizer
integration, full task 2.10 and the complete OpenSpec lifecycle remain unfinished.
The change is not merged, synced to canonical specs or archived.

## Exact implementation and delivery

- Rust: `4d539b80a743f5c5e515ff460f5c0d35fb73e161`,
  [draft PR34](https://github.com/s116821/ReMarkableBuddies/pull/34).
- Precode contract: Docs `3df4645d34bbf12ef68481dc4d50e6809cffba9b`;
  reviewed repair clarification: `28acd251907da9d0b33ac94e3f30dc52f8a35c95`,
  [paired draft PR16](https://github.com/s116821/ReMarkableBuddiesDocs/pull/16).
- Existing unmerged dependencies are Rust PR30 then PR33 and their coordinated
  Docs PR6 then PR15. This focused increment adds no independent merge permission;
  exact implementation/specification evidence must be reviewed together.
- Committed SDK remains `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1`. The protected
  working SDK/native changes are not staged or included in the qualification input.

The normal LF Git archive has ZIP SHA-256
`bb4a8fbb845cce61aef32cf9a5f0ae91eef61569a01dbdd848489d85d38064a0`.
Eleven raw Cargo/source/test blobs were compared with exact Git objects. This is a
build input, not a new checkout, worker or replacement for the preserved work.

## Implemented behavior

`reader.selection` explicitly chooses the existing selected Workflow/refusing
backend. Normal startup uses the final configuration after dotenv and routes
before model credential resolution, provider creation or ordinary RealDevice.
The default absent selector leaves ordinary startup routing unchanged. Legacy
sync cannot be enabled for the selected runtime.

Startup opens only safe existing owned Store state, uses shared selected admission
and the original receiving budget, rejects unavailable commits, and validates the
strict conversation projection and every owned conversation chronology. Only then
does it query pure typed backend availability and the committed unqualified SDK's
`NoNativeAdapter` result. It does not start a request or reinterpret a request-
guard error as capture status. Actual acquisition retains its request guard.

The existing executable now exposes `--conversation-operation inspect|context|
recover-pending` with required `--conversation-input FILE`. Strict bounded input
and explicit configuration precede dotenv, logging, provider, worker or device
setup; conflicting execution overrides are rejected. Inspection projects current
selected causal heads only. Ordinary and retained records cannot fill omissions.
Unknown mixed domain namespaces refuse instead of being silently discarded.

Current inspection seals its complete report, Store-issued token and original raw
custody identity. It retains the Store lease and shared admission through the
actual writer, consumes its seal once, and rechecks using the same cumulative
allowance. Stale, altered or exhausted admission emits fixed unavailable/no data
before output; partial output failure never triggers a second report.

Recovery validates the complete original request against the original historical
publication. Exact recovery returns named historical transaction/receipt/reference
data even after a later selected replacement. Changed original input returns typed
invalid-input, an absent operation returns not-found, and unavailable original
bytes return unavailable. It allocates no IDs, publishes no records, invokes no
source/backend/model effect, and returns no live token or ReaderContext.

There is no real provider tokenizer in this executable path. Context requests
validate their range/budget but return choice-needed with no model-ready data;
bytes, words and caller assertions are not invented token counts.

Input is bounded to 1 MiB and the whole compact response including newline to
8 MiB + 64 KiB. Selected validation shares 64 snapshot attempts, 4096 work items,
8 MiB metadata and 32 MiB verified media, including final writer rechecks. Normal
Store startup and historical recovery retain their separate existing bounds;
there is no combined command I/O, memory or latency qualification claim.

## Review and verification

Sol independently accepted the precode contract and identified two source defects:
startup accepted generic metadata without strict conversation validation, and its
acquisition call failed at the request guard before reaching the claimed boundary.
Both were repaired in Rust `4826cfc` and Docs `28acd25`. Exact repair re-review
accepted the source/docs and regression assertions with no remaining finding in
that delta. This is attributed internal read-only review, not a public approval or
an independent rerun of the owner's full matrix/archive hash. Sol also accepted
the exact `4826cfc` to `4d539b8` successor: it boxes the internal recovery request
and simplifies the typed SDK match, preserving request validation, schemas and
guards. These repairs resolve two new Clippy findings without suppressions.

Working-input focused passes cover ten actual executable tests: selected startup
and dotenv routing before private provider setup; generic-valid invalid schema and
chronology; unavailable ordinary commit despite surviving selection; current
inspection and no fabricated context tokens; busy/private input; once-only sealed
output and tampering; partial output/lease lifetime; oversized input/invalid range;
retained/ordinary isolation; and absent/foreign/busy recovery command routing.
Three library controls cover original recovery after replacement/changed/unknown/
missing bytes, current writer replacement/exhaustion/raw-custody guards, and default
routing/whole response bound. A fourth library control demonstrates typed startup
availability while preserving actual request-guard refusal. These controls are
included in full suites, not additional full-suite totals.

Final exact committed-SDK locked/offline all-feature tests pass, exit 0: Windows
Rust 1.98.1, 287 library tests passed/one existing ignored, plus all binary,
integration and compile-fail doc suites. All ten actual runtime executable tests
and four focused library controls are included in those totals. The ordinary
nonmock library/binary check and exact archive formatting pass, both exit 0.
Required strict
Clippy fails on 23 inherited dead-code errors, exit 101; the complete all-target
warning collection has exactly 23 inherited warnings and no new runtime/CLI
diagnostic. That collection uses a command-local warning cap to inspect all
targets, not to pass or waive the strict gate.

Hosted final source run `38318560160` at `4d539b8` has completed Test
`115040967892` successfully: Linux 291 library tests passed/one existing ignored,
plus all binary/integration/compile-fail doc suites and all ten runtime CLI tests.
Completed lint `115040967903` still fails on 23 inherited errors; the overall CI
run is unsuccessful. Release-policy and title checks pass. These are hosted
ordinary PR-merge inputs, distinct from the exact normal archive. Native cross
build qualification is not established because the earlier lint step fails.

Hosted Docs checks at `28acd25` pass on Ubuntu/Windows and strict OpenSpec. Local
pending result checks pass all 12 Docs tests, 19 guidance files/126 preserved
source blobs and all 17 strict OpenSpec items. The final result revision's hosted
checks at `397b0ca` also pass on Ubuntu/Windows and strict OpenSpec. Sol's final
bounded evidence review independently read completed local/hosted logs, parsed all
23 diagnostic warnings, and verified hosted Test success, lint failure, skipped
tablet builds and exact draft PR pointers. No new source/result finding remained.
Archive hash/blob verification and full-suite execution remain owner evidence;
the reviewer did not reproduce them. No whole-feature, merge or required-lint
acceptance follows. This final result/task amendment remains subject to its own
hosted Docs checks.

Prior candidate `6a140fd` full-suite
attempts failed build setup: a relative target path caused Windows LNK1104, then
shared cached dependencies lacked required rlib forms. Those logs are preserved;
they are not passing source qualification. The earlier `ac16229` candidate excludes
the reviewed startup repair and passed 286 library tests/one ignored plus all
other suites. Repaired `4826cfc` passed 287 library tests/one ignored plus all other
suites. Neither candidate qualifies the final `4d539b8` archive.

## Remaining gates and source basis

SDK d01 supplies no qualified native source admission. Selected fresh ReaderContext,
native capture/insertion/display/recovery, effect dispatch/settlement, development
collection bootstrap, selected trigger/status/history/idle undo, branch-dependent
rendering and full task 2.10 remain open. Applicable inherited strict lint failures
remain unsuppressed; this increment does not promise all 24 disappear.

All nine protected working files remain byte-identical. No device query/write,
model, firmware, pairing, account or service action occurred in this increment.
The held 8112 transfer/activation and equivalent replay remain untouched. A generic
platform flag does not establish a categorical ban on every unrelated observation;
future genuinely different permitted diagnostics require their own concrete
technical scope, sole-operator coordination, advance notice and recovery.

Source basis: exact repository blobs and actual owner test/build outputs; separately
attributed independent source/assertion review. Private local logs are not public
transcripts. No synthetic or historical evidence is promoted to native authority.

## Current-parent integration

Source8909dade30db044a1c69edd565b09144eefbf5a6 normally integrates existing
startup branch91cf92f with repaired memory parentd9aa2f3. The original accepted
startup/history source and result above remain historical evidence; they are
not relabeled current qualification. Subject-memory remains draft/live-gated,
and actual inspector release qualification is separately observed.

The effective child is12 source paths. The startup/history implementation,
ten actual CLI fixtures and refusing-backend implementation remain byte-identical
to91cf92f. Current Cargo.toml/lock, storage selection and the complete repaired
orchestrator remain byte-identical tod9aa2f3. Current SDK32b86e4 and release,
export, personalization, inspection and memory contracts are preserved. Only
the existing memory preflight and trusted Store-open classifier become crate-
visible for their real startup caller; no new admission/recovery engine appears.

Six conflicts compose configuration reader fields/defaults/validation, library
exports, all early one-shot routes, the shared preflight helpers, current outbox
and the repaired value-free Reader logs. History maintenance now also rejects
inspection, export and personalization, in addition to memory and runtime
selectors. The existing actual-process selector control adds eight orderings:
history against each other one-shot route in either order, no JSON dispatch and
unchanged fixture bytes. The source tree retains production refusing transport;
selected startup reports unsupported rather than falling through to RealDevice.

Current Windows23 distinct top-level checks pass: ten actual startup/history CLI,
four inspector CLI, five parser/logging, three runtime library and one exact
historical-recovery library control. The latter preserves original custody after
replacement and refuses changed/missing input. Strict all-target/all-feature
Clippy with denied warnings, locked no-default library, formatting and diff checks
pass. Earlier unresolved-merge parse output from a local text-encoding error is
retained; source was restored from authoritative Git blobs with explicit UTF-8
before these successful checks. No original full matrix was repeated.

The active platform delta preserves source-retention/service behavior while
correcting its old full-model-text logging permission and specifying the history
command pair and selector isolation. Strict Docs validation passes39 items;
manifest validation preserves25 guidance files and126 original source blobs.
No canonical requirement is synchronized or whole change archived here: current
hosted CI, independent full integration review, parent memory live evidence and
coordinated delivery remain required. Native/fresh ReaderContext, tokenizer,
selected effects, wider conversation requirements and full MVP gates stay open.
No model, tablet, service, account or remote-provider operation occurred.
