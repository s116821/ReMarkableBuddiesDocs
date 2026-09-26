## 0. Planning and dependency gates
- [x] 0.1 Read full REM-36 and timestamped comments, revised roadmap, central guidance and source baseline; record public source research and scoped ownership.
- [x] 0.2 Obtain independent review of full proposal/design/tasks/deltas; resolve storage, migration, transport and failure-boundary findings before code. Independent review accepted revision `889355c2a0eeb96aac9f1e7cc78f14329e45e4b2`; implementation remains gated by 0.3.
- [x] 0.3 Coordinator confirms REM-21 Manager acceptance; rebase isolated Docs/Rust lanes to accepted public mains and reconcile REM-9 integration points. Docs rebased onto `78303fb`; Rust starts at `6fc7f9e`. Coordinator explicitly assigned scoped main.rs/lib.rs wiring; final REM-9 integration rebase remains in 5.4.

## 1. Local store and owned layout
- [ ] 1.1 Implement validated owned roots, ownership marker, versioned capability/location descriptors and platform permission/path safeguards; test non-owned/system/xochitl/overlapping/symlink refusal.
- [ ] 1.2 Implement independent domain envelope API, stable record/revision/operation/actor IDs, exact idempotency checks, explicit parents/tombstones and bounded parsing; keep opaque fixture schemas distinct from domain completion.
- [ ] 1.3 Implement staged content-addressed objects and atomic commit manifests with appropriate file/directory sync; test failures before write, before/after rename, before index refresh and disk-full/corrupt/missing content.
- [ ] 1.4 Implement recovery/index rebuild and retained conflict heads; test arrival permutations, edit/edit, edit/delete, stale resolution and explicit all-head resolution without clock ordering.
- [ ] 1.5 Implement process-lifetime stable OS lease plus in-process transaction serialization; test two competing processes, crash/release, stale status/PID, disconnected maintenance and unsupported lock interop.

## 2. Configuration and maintenance contracts
- [ ] 2.1 Implement versioned nonsecret config and redacted source descriptors; preserve explicit CLI, existing env/.env, model/corner defaults and lean CLI; test each precedence and invalid/blank case.
- [ ] 2.2 Implement restricted credentials/provider abstraction and safe refresh-state writes; test no secret/token/session URL leakage in diagnostics, exports, errors or Debug output.
- [ ] 2.3 Publish exact offline JSON schemas, capability versions, layouts and stop-confirm-lock-stage-commit-restart maintenance contract in docs/storage-contract.md; no running-service API or assumed stock-tool availability.
- [ ] 2.4 Integrate minimal production startup and shared Store handle without implicit simulator/network I/O; run existing CLI and offline simulator regressions after REM-9 rebase.

## 3. Recovery, migrations and survival
- [ ] 3.1 Implement verified export to new destination and additive staged restore with traversal/symlink/schema/size/hash checks; exclude tokens/caches/binaries and rotate restored actor identity for new edits.
- [ ] 3.2 Implement explicit migration registration and generation activation with retained rollback; test synthetic v1-to-v2 migration failures before/after activation and unsupported actual-version refusal.
- [ ] 3.3 Test offline/empty-device restoration of values, retained media, tombstones and conflicts, corrupted/partial backups and repeat restore idempotency.
- [ ] 3.4 Verify app replacement/reinstall fixture preserves roots; publish source-backed firmware/reset uncertainty and independent backup requirement without tablet/update/reset operations.

## 4. Optional Drive implementation
- [ ] 4.1 Implement off-by-default independent domain policies, explicit collection/account binding and history/media retention/completeness reporting; ensure no network on default/local-only path.
- [ ] 4.2 Implement real HTTPS Drive v3 transport behind hermetic injectable interface, scoped credential acquisition/refresh provider, bounded request parsing and sanitized errors; never use actual user credentials in this lane.
- [ ] 4.3 Implement generated-ID journal, immutable record/media creation, verified 409/ambiguous completion, durable outbox and commit-manifest publication after complete uploads.
- [ ] 4.4 Implement resumable-media session checkpoint/status/expiry handling, backoff/jitter/Retry-After/cancellation and batch bounds; test partial/resumed/expired uploads and quota/auth pauses.
- [ ] 4.5 Implement full collection discovery, initial start-token race handling, pagination/checkpoints, staged imports and empty-device restore; test interrupted pages, duplicate replay, out-of-order dependencies and unknown/cyclic schemas.
- [ ] 4.6 Verify transport removals/lost access never synthesize tombstones; explicit deletion/reconciliation retains concurrent local edits; appData removal/revocation preserves local data and requires deliberate rebinding.
- [ ] 4.7 Wire the enabled production worker with startup discovery, durable-outbox/local-commit wake, periodic remote polling, short store-lock sections and bounded cancellation/shutdown; test remote-only arrivals, lost wakes, slow requests with foreground writes, restart replay and disabled/simulator zero-network behavior.
- [ ] 4.8 Implement policy-neutral media descriptors, exhaustive manifest coverage and supplemental availability commits; test history-only restore, size deferral, later arrival, policy toggles, unchanged revision/head identity, missing required objects and honest export completeness.
- [ ] 4.9 Implement distinct selected-record transport projections for mixed-namespace local commits; verify excluded records and their identifiers are absent from projection metadata, selected opaque payload associations are neither scrubbed nor recursively synchronized, parent closure stays within selected records, later enablement is idempotent and recovery never claims original cross-domain transaction completeness.
- [ ] 4.10 Verify bidirectional namespace/media selection, envelope-to-reference namespace integrity, deferred-policy replay and fair dependency scheduling across batches/restarts; optional corrupt/stale sync state must pause sync without preventing local Reader startup.

## 5. Acceptance and linked delivery
- [ ] 5.1 Run hermetic two-device matrix: local-only, offline edits in both orders, conflicts/resolution, delete/edit, new/empty restore, retries/409, partial uploads, cursor replay and interrupted migrations; keep fixtures public and synthetic.
- [ ] 5.2 Run config/CLI regressions, meaningful store/sync tests, strict clippy, existing offline simulator suite and both ARM target builds; record source SHA and host/simulated evidence limits.
- [ ] 5.3 Independent review checks issue coverage, unsupported-survival/CAS claims, ownership, credential redaction, no Buddy API, real adapter versus mock-only behavior, and remaining native/live-account gates.
- [ ] 5.4 Rebase against accepted ecosystem heads, run affected integration checks and open linked Docs/Rust PRs with Summary-only bodies, exact revision pairs and detailed evidence comments; inspect CI and bug-bot feedback or independent review.
- [ ] 5.5 Sync only verified shared-storage/optional-drive-sync and the two scoped platform-runtime blocks; archive this completed change in the paired delivery. Parent alone squash-merges; keep REM-37/24/26/41/42 and 1.0 claims separate.
