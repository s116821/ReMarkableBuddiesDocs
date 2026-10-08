## Context

Complete proposed investigation/implementation design, not an accepted backend. research.md pins source evidence; qualification.md defines native gates. A missing exported API is not proof of impossibility. Creating a notebook, editing an offline file and inserting into an open annotated PDF are separate claims.

## Goals / Non-Goals

Create one native writable successor or reuse the exact bound conversation page, preserving source identity, ink, highlights, text, PDF bytes and unknown metadata. Share acquisition across Reader, Writer refinement and blank start. Preserve accepted REM-9 completion-driven responsiveness and cancellation.

No conversation renderer/history implementation, source-question erasure, marker switching, generic QML evaluator, remote command service, cloud sync, firmware recovery, Paper Pro or broader initial-trigger landscape work. No Buddy HTTP/RPC/admin API. Extension calls are private local integration; Manager uses SSH/OS/known files.

## Decisions

### Versioned historical topology evidence

Follow [the owning consumer plan](capture-owner-diagnostics-consumer-plan.md):
exact29-field version1 remains unchanged, exact33-field version2 adds only finite
original topology return-site scalars. Unknown/mixed formats preserve raw evidence
without decoding or admission. SDK4097736 and the consumer amendment require
coordinated review before code; artifact/packet/native qualification stays separate.

### Logical gesture navigation; direct opening deferred

The October 3 user decision selects permitted gestures exposed through SDK logical
Next/Previous with per-tablet implementations. Logical page order is distinct from
physical swipe direction and orientation. Direct native openPageKey is deferred,
not an MVP or release prerequisite. Its optional development restart/Myfiles setup
and guard experiments do not become prerequisites for the selected gesture route.
See [logical navigation contract](logical-navigation-contract.md) for the smallest
creation-to-write route and the exact boundary between existing behavior and work
still requiring implementation and qualification.

After a correlated insertion, freshly identify the active page. If it is the exact
new target, verify it without a gesture. If it is the exact source and the committed
order places the target immediately next, request one logical Next and verify the
intended target before binding/rendering. Unknown ownership, another active page,
nonadjacency, input, session replacement or unexplained order drift stops for
reconciliation. Actual insertion auto-selection is unqualified; persistence and a
later development reopen do not establish active-owner behavior before restoration.

Retain the current Reader's single-gesture completion and source/destination/input
guards. A legitimate insertion needs an explicit correlated structural handoff;
never relax the old order guard or silently repin a lost captured source. Per-tablet
gesture mappings, authoritative active-owner observation and runtime integration
remain open qualification work. No direct-opening-only gate carries into this route.

### Capability discovery before mutation

Prefer stable direct/native, IPC or maintainable coordinated service mechanisms using narrow SDK capabilities. Supervised lazy session-only XOVI is now an acceptable candidate for capabilities that cannot be reached robustly otherwise; it is not selected. The October 1 direction supersedes the earlier blanket production exclusion. Compare safety, maintainability and target-tablet compatibility rather than treating dependency avoidance as the goal. After dependency/review gates, observe exact active model, signatures, signals and serialization on the authorized RM2. Inspect legally available device resources locally; publish observed signatures/hashes, not proprietary firmware. Do not guess or invoke arbitrary methods during discovery.

Initially match exact model, architecture, firmware, xochitl build fingerprint, Qt ABI, extension/protocol version, document schema and qualified document kinds. Missing/conflicting/changed capability returns Unsupported before mutation. Recheck xochitl process generation and object lifetime at dispatch; restart invalidates handles. No historical memory offsets, menu coordinates or blanket firmware ranges inferred from one run.

### One guarded acquisition contract

Input: operation ID, conversation ID, intent (Reader/Writer-refine/blank-start), exact source document/page UUID, source content/order revision fingerprint, xochitl session generation and cancellation token. Page index is display data, not identity. REM-37 resolves canonical binding. A new selected source coordinate does not implicitly create another conversation.

Result: Created/Reused with exact target UUIDs, observed ordering and persistence receipt; otherwise Unsupported, Conflict, Cancelled or ReconcileRequired without render authorization. A FIFO reply, screenshot change or successful method call is not completion. Renew owner guard before REM-38 writes.

First insertion is immediately after source. An unrelated nonblank successor shifts; it is never overwritten. A verified prepared blank successor may be adopted. Reuse a bound page even when scrolled or edited. If moved, resolve by stable ID and navigate through a qualified route without silently reordering or duplicating it. Missing/deleted/mismatched/ambiguous binding requires reconciliation. Legacy header pixels do not establish ownership.

### Serialized transaction and recovery

Use REM-36 generic CAS/atomic storage and REM-37 canonical bindings, not a second identity registry. REM-36 coordination specifies envelope v1 (namespace/domain_schema_version/record_id/revision_id/operation_id/actor_id/parents/kind/payload/media_descriptors), expected full parent/head-set validation under exclusive OS lease plus mutex, immutable objects and atomic manifest-last commit. Its final implementation is still in progress; verify exact API before use.

Proposed **local-only native page-operation journal**, separate from syncable conversation records: operation_id, conversation_id, source IDs/revision, intended target ID when knowable, native session, phase, observed target ID and before/after order fingerprints. This new domain/namespace is not one of REM-36's five registered domains and requires coordinated registration before code. Default data root is /home/root/.local/share/remarkable-buddies; do not invent a parallel root. Native side-effect records MUST NOT be synced/restored as executable operations. Imported/restored logical bindings must be revalidated against this device and never initiate page creation by themselves.

Progression: capability/owner check -> durable Prepared -> bounded native dispatch -> observe native structural commit/save -> durable NativeCommitted -> binding CAS -> BindingCommitted -> renderer receipt. Native and ledger writes are not assumed atomic together. Replies include correlation and session; stale/out-of-order replies cannot satisfy requests. Serialize mutators; no generic shell/QML payloads. If broker transport is selected, audit actual pipe owner/mode and exclude unrelated writers/readers; 0660 alone is not authentication.

Retry first reconciles the same operation against exact native IDs. Lost reply or journal failure after insertion must not duplicate it. If API cannot preallocate/return or durably correlate the new ID, qualification must prove a uniquely attributable page-set delta under exclusive native mutation; otherwise that route fails safe retry qualification. Unknown outcomes stay ReconcileRequired, never automatic redispatch.

Cancel before dispatch causes no mutation. Cancel after possible dispatch stops rendering and retains uncertain native outcome; do not claim queued work was cancelled. External input/navigation/session changes stop output. No compensating global undo. An uncertain or user-edited new page is preserved. Only a separately qualified exact-page native removal with proof of unchanged blank/unreferenced ownership could roll back creation; otherwise preserve/report. Backup restoration is a coordinator fixture recovery action, never blind runtime overwrite.

### Metadata alternative

Compare native invokables/QML, an exact ABI hook if needed, and metadata with proven native flush/close/reload coordination. A filesystem lock does not lock xochitl. No writes behind an unaware open UI, unknown-field-dropping serialization or per-conversation restart. Offline archive modification aids fixtures but does not supply active-document coordination. Identity-replacing reimport is not successor insertion.

Preserve original PDF byte hash, native IDs, prior relative order, PDF redirection, CRDT/version/tombstone and unknown fields. Compare existing scenes bytewise; where native serialization necessarily changes representation, require explained semantic equality of all ink/highlight/text/style/positions and inspected visuals. Never waive PDF byte equality or unexplained mutation. Multi-file updates need tested recovery and cache handoff, not a single atomic rename.

### Manual fallback

Temporary unavailable capability produces honest preparation guidance and model-free exact-successor validation. Check full native content including off-screen text, layers and annotations; screenshot white-space is insufficient. Unknown blankness refuses adoption. Verified bound pages may contain edits and are not cleared. Preserve unrelated or legacy-unbound pages.

Choosing manual preparation as REM-25's delivered outcome requires completed candidate investigation, actual viable-route notebook AND open annotated-PDF tests, documented barriers/corrections and independent exhaustive-outcome review plus exercised fallback. Time spent, search misses, missing access or one failed prototype are insufficient. Bound experiments and checkpoint unresolved hypotheses rather than looping indefinitely or falsely declaring impossibility. REM-35 must accept the selected outcome.

### Extension lifecycle

If XOVI is selected, Buddy owns a tiny independent Supervisor process that can observe
the required trigger input without xochitl/XOVI. Supervisor and normal runtime remain
in the same Buddy repository, release artifact and one Manager installation; a vetted
minimal payload is an internal managed implementation detail. SDK owns hardware-facing
capabilities/adapter mechanics in its independent OpenSpec. No separate SDK installation
or user-managed XOVI prerequisite follows.

Cold boot runs stock xochitl with the Supervisor available and XOVI inactive. The first
recognized Buddy gesture of any supported kind may activate the session payload after
exact model/firmware/version/hash/capability checks. Allow at most a brief one-time
activation restart/rebind; subsequent gestures use the ready session without
per-conversation restart. Preserve the triggering intent where safe, but reacquire
and validate its current source, cancellation and fresh handles after restart.
No captured-source or pending-native-operation replay crosses the session boundary.

Require bounded readiness/startup checks and heartbeat, rapid crash/restart-loop
detection, automatic stock rollback on activation/health failure, UI-independent
disable/recovery and Manager-owned update/uninstall. Unknown compatibility refuses
activation. A cold reboot always restores the non-XOVI baseline; persistent xochitl or
systemd changes must not reproduce an injection crash loop across boot. Preserve
documents/data and unrelated user extensions. Restrict hooks to required semantic
capabilities rather than replacing the tablet shell or broad UI. These are planned
qualification requirements; no injection run or production selection is claimed.

If selected, package only needed ARM32 loader/modules and narrow adapter with pinned source/tag/SHA/hash, license/source notices, dependency graph and compatibility manifest. Audit Qt linkage and per-component terms. Do not enable webserver-remote, qt-command-executor or unrelated modules. Check hook conflicts and preserve independent user extension installations.

REM-41 owns browser/Electron staging, low-space/interrupted installation, activation verification, updates, rollback/removal and independent release discovery. A disclosed coordinated activation restart does not authorize per-request restarts. Use supported tethered/stock recovery, not boot modifications to root xochitl units. After reboot/inactivity report missing capability, not success based on files. Test stock return and preserve documents/config/data. Equivalent public manual CLI/file instructions remain available. No firmware upgrade, pairing or personal sync.

## Cross-lane migration

REM-36 owns storage primitives; REM-37 owns logical bindings/history; REM-38 owns template/typing/prepend/focus/overflow using a fresh owner receipt. Exercise contract fixtures for Reader, Writer and blank start without claiming downstream native integration before REM-37/38/39 exist. Blank start makes no empty model call. REM-35 later validates integrated native flows.

Coordinator approved this change and replacement of four reader-answer-pages blocks: successor identity/navigation, blank/bound classification, invalid successor recovery, reusable decisions. Rebased and reconciled against accepted REM-9 Docs e7fbdc44 and Rust 3df3b1e6. Retain its fresh bracketed native identity/pixels and positive settled chrome, monotonic deadlines, sticky request owner/cancellation, single-attempt recovery and non-ink diagnostics. Insertion legitimately changes order: only a proven, correlated owned structural transition may produce the new acquisition receipt; never relax the old order guard or silently repin the captured source after external input. A future native route must independently qualify replacement completion predicates before changing conservative REM-9 behavior. Pen/text tablet-io output remains Linux input; creation does not authorize direct scene rewriting.

## Gates and delivery

The next source-only combined discriminator is proposed in
[qt-input-observation-plan.md](qt-input-observation-plan.md), referencing SDK-owned
bounded filter, specialized end and separate GUI capture semantics. Consumer
publisher/collector evidence cannot create facts or native/render authority.
Coordinate both owning proposals before implementation; no device selection follows.

The prospective development collector correction is specified in
[facts-observation-continuation-plan.md](facts-observation-continuation-plan.md).
It permits only one fresh read-only callback-status observation after a returned
transport timeout within the unchanged original150s host clock, retaining full
live proof and restoration duties. No implementation or new device run is selected
by this plan; spent results and the held generic framework remain preserved.

Only Docs/OpenSpec checks now. No native/model result claimed. Implementation starts after REM-9 acceptance and exact plan acceptance by coordinator and independent reviewer. qualification.md and tasks.md remain open. Future linked Docs/Rust/required-Manager delivery identifies exact SHAs, passes code/spec checks, syncs/archives only completed behavior, uses Summary-only bodies and explained inline evidence, inspects CI/bot availability and is squash-merged by coordinator. REM-35 alone owns1.0.

## E0 host-owned lifecycle experiment

The coordinator authorized E0 only, coordinated with SDK contract
[e2b3ebbb8c4c630e46041896bc266498518de437](https://github.com/s116821/ReMarkableOpenSDK/tree/e2b3ebbb8c4c630e46041896bc266498518de437/openspec/changes/establish-native-platform-contract).
Original Buddy tooling models product activation policy with an injected monotonic
clock, then exercises independent fake Supervisor, recovery guard and stock/injected
child processes in unique owned temporary directories. It uses no network, tablet,
real service manager or production payload. It is experimental tooling, not an SDK
adapter or production Supervisor. Harmless Supervisor autostart is permitted only
with stock boot and a fresh authorized trigger; persistent injection-enabling changes
and cross-boot injection/crash-loop state remain forbidden.

Acceptance covers mismatch with zero activation; one healthy activation and duplicate
requests; nonce/generation/process-bound readiness and heartbeats; constructor failure,
missing readiness, stale heartbeat and crash-loop cutoff; Supervisor death before and
after arming, applying, awaiting readiness, Ready and rollback; guard-alone failure;
simultaneous loss with honest unprotected status and clean cold boot; interrupted
rollback without timeout-as-success; partial files and interrupted update/uninstall;
exact stock hashes and process start identities; removal of transaction-owned files
only. Deterministic events sequence tests. Host watchdog bounds are readiness5s,
heartbeat1s/stale3s, rollback5s and outer30s per real case; they prove no tablet timing.
No harness result authorizes E1 or qualifies any native semantic operation. Broad
implementation, real device, licensing, source handoff and full delivery remain open.
## Development capture observation integration

The pending [focus ancestry consumer amendment](focus-ancestry-consumer-plan.md)
adds a separately selected exact37-field diagnostic matrix and one reader refusal
stage in the unchanged27-field historical refusal format. SDK owns the guarded
chain/ticket; callback4/capture36/facts23 and all historical v1/v2 bytes remain
unchanged. Explicit native-profile qualification precedes selection.

The selected consumer integration follows
[capture-observation-consumer-plan.md](capture-observation-consumer-plan.md).
One distinct purpose-bound owner/image observation precedes the original facts
request. Exact copied PNG/completion/token bindings and Main's positive full-image
visual decision govern consumer admission. Sticky SDK owner invalidation remains
active through facts delivery. Capture success never resets original setup time or
grants native/render authority. The vendor grab may return held framebuffer pixels;
bounded owned copying protects byte ownership without establishing render freshness.
