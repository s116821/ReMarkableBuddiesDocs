# Development pre-Enter consumer design

## Status, source and ownership

The precode was independently accepted in Docs PR 152 at
`a5e3dc16e437306197438474fc7e44ed74a60f5f`. The consumer implementation is
published in [Buddy PR 138](https://github.com/s116821/ReMarkableBuddies/pull/138)
at `9ee80d8d5c9e540ba6c06884da11f8ef511dcfcf`; independent source review and
local build validation passed. Hosted CI and coordinated delivery remain pending.
This increment contains no
provider call, installed artifact change or tablet action.

Reviewed delivered sources:

- Buddy `bafa5cc92c175b1319939265c6da5928315cd8bc`: `Cargo.toml`, `Cargo.lock`,
  `build.rs`, `src/workflow/resident_runtime/read_only.rs`,
  `src/workflow/resident_client.rs`, `.github/workflows/ci.yml`,
  `cicd/release/apk_source_build.py` and `apk_contract.py`.
- Central Docs `f98ff826aacdf63be373bd812c8eb8fdd102e3d5`: development-testing,
  platform-runtime and package-build-inputs canonical contracts.
- SDK wire/transport baseline `240df867147aa309ac35b74132f0b9fa22082b9b`,
  selected reviewed source `146d78c9eded3dcfbfe84d55ca2de353e1996dff`, and native
  variant/marker design `c85c466945bd81d3b96215ef279a97b1dc2d934d` in
  [the existing SDK change](https://github.com/s116821/ReMarkableOpenSDK/tree/c85c466945bd81d3b96215ef279a97b1dc2d934d/openspec/changes/capture-pre-enter-text-diagnostics).

SDK owns command/reply framing, Capture, Endpoint/RequestLease, private native
variant and marker implementation. This change owns only the Buddy consumer and
its central specification. An eventual execution coordinator owns fresh process,
route/trust, fixture, marker, input, containment and recovery admission. No source
plan transfers those authorities.

## Typed closed path

Add `ReadOnlyRequest::CapturePreEnter { offset: u32, count: u16 }` and its match
arm only under `cfg(buddy_development_native_pre_enter)`. Add the correspondingly
gated `ResidentConnection::capture_pre_enter_with_progress(operation, offset,
count, deadline, progress)`, analogous to `observe_with_progress`.

Use SDK `Client::execute_with_progress` with the specific
`Command::CapturePreEnter { offset, count }`, the existing no-mutation-journal
callback, progress error conversion and `transport_failure` mapping. Do not
expose an arbitrary Command, mutable connection or effect closure. Keep the
existing shared `Result<Reply>` admission boundary; the diagnostic caller must
narrow the result to the supported historical variants.

Invoke `request_read_only` with the caller's ORIGINAL `Instant`. Keep its
pre/post full admission, companion/child/owner checks, `before_api`, servicing
pulses and `after_api` retention, including error/retention precedence. Do not
use the separate fresh-capture-budget convenience path, add a new relative
budget, reconnect/retry automatically or discard evidence after a late boundary
failure. Endpoint and the native Capture receive their existing lease deadline
and retirement signal unchanged.

The SDK validates count <= 4096 and the checked half-open end
`u64(offset) + u64(count) < INT32_MAX`, including count zero. Preserve its exact
operation, sequence, request digest and reply type/count correlation. Any early
consumer validation must be equivalent and must happen before dispatch. The
initial proposed fixture is offset 0/count 12; this is not general permission to
read arbitrary documents or ranges.

`Reply::PreEnterText(Some(units))` preserves `Vec<u16>` unchanged.
`Some(empty)` is a successful zero-count copy, distinct from terminal
`PreEnterText(None)`, Unsupported and Capacity. Transport, wrong-kind/count,
stale, deadline and retention failures never become empty text or success. Do
not decode lossily, normalize Unicode, strip NUL, replace isolated surrogates or
turn a native paragraph separator into a different code point. If a bounded
private fixture report renders UTF-16BE hex, emit each original unit exactly;
keep diagnostic text out of generic/public logs.

NoPendingMutation describes effect-journal state, not permission to rearm an
already consumed native slot. A lost response must retain the original operation
outcome; no replacement ID, reconnect or replay is introduced.

## Build selection and official refusal

Ordinary normal/dev SDK declarations remain tag `v0.2.0`; ordinary Cargo.lock
remains at `a0c6480be6785480c2e0da76a3c06697a18efae4`. Ordinary CI retains
`cargo clippy --locked --all-targets --all-features` and
`cargo test --locked --all-features`. Do not add an ordinary Cargo feature that
makes those builds reference variants absent from the pinned SDK.

Register `cargo::rustc-check-cfg=cfg(buddy_development_native_pre_enter)` in
Buddy build.rs, but do not emit this cfg in ordinary builds. Explicit developer
compiler flags may select it only with the separately verified SDK override.
Registration alone does not enable it or change any runtime setting.

When that cfg is supplied, build.rs must reject BEFORE producing a diagnostic
Buddy artifact if ANY of `READER_BUDDY_RELEASE_TAG`, `READER_BUDDY_RELEASE_SHA`,
`READER_BUDDY_CANDIDATE_TAG`, or `READER_BUDDY_CANDIDATE_SHA` is present, including
empty, partial, mixed or malformed values. Check presence, not truthiness.
Observe the actual supplied cfg through Cargo's `CARGO_CFG_*` build-script input,
including a boolean cfg represented by an empty value; absence alone is false.
Do not rely on scanning only one possible RUSTFLAGS spelling.

Also reject a diagnostic build whose actual HEAD has an exact official semantic
release tag under the existing tag policy, even if official identity environment
variables are absent or the developer lock is dirty. Do not mint another tag or
substitute package versions. The selected developer source must instead identify
its reviewed untagged consumer revision and explicit developer lock delta. If
its required Git identity cannot be established, fail closed. Ordinary builds
without this cfg keep their current official/dev metadata behavior.

Use a fixed private-data-free build error; never print environment values. Add
appropriate rerun tracking for this selection and all four existing identity
channels so cached build-script output cannot evade a changed selection. The
SDK feature flag and native variant are independent gates, not substitutes for
this official-build rejection.

## Command-local developer dependency and lock

After implementation is separately reviewed, use an isolated task-owned Buddy
checkout/worktree, original source lock preserved, and a separate target/output
directory. Never modify another lane, the ordinary SDK cache, home Cargo config,
repository settings or the ordinary published lock. The developer checkout may
have only the explicitly recorded generated lock delta to its reviewed source.

Apply Cargo's maintained Git-source patch on EACH diagnostic Cargo invocation:

```toml
patch."https://github.com/s116821/ReMarkableOpenSDK".remarkable-open-sdk.path="/ABS/REVIEWED-SDK"
```

This is a `--config` argument, not a committed/global config change. The absolute
SDK directory must be the clean, reviewed immutable Git source providing the
paired command and Native's selected variant. The selected SDK source is
`146d78c9eded3dcfbfe84d55ca2de353e1996dff`, incorporating the reviewed wire and
variant/marker implementation. Bind its manifest/tree hashes and exact features;
no floating branch/default HEAD or unreviewed successor is accepted. Changing
this pin requires a new exact source review, not silently following SDK41.

Enable `development-resident-bootstrap` and dependency feature
`remarkable-open-sdk/development-native-pre-enter` explicitly only for diagnostic
commands, plus the compiler cfg above. Resolve the separate developer lock once
with this exact patch/features; retain original and generated lock bytes/hashes.
Then repeat every metadata/check/build with the SAME patch/features and
`--locked`; never update the lock silently while building. Use Cargo metadata's
full resolved graph to verify exactly one reachable SDK at the reviewed path,
manifest and source tree, including the actual feature set and dependency
identity shared by normal/dev declarations. Refuse a dirty/replaced SDK, unused
patch, ambiguous/duplicate SDK, unexpected feature or changed lock/graph. No new
resolver or dependency framework is needed.

The future command recipe is the existing Cargo/Cross diagnostic target with
command-local `--config`, exact features, recorded compiler cfg and independent
`--target-dir`. The actual target/toolchain command must be frozen before build;
this precode does not claim a runnable pre-Enter CLI or add runtime dispatch
configuration. Record exact Buddy revision/delta, both locks, SDK tree/manifest,
Cargo metadata/feature graph, toolchain, config/flags/argv, native variant/profile
and generated artifact hashes. No maintained semantic version or fake official
identity is introduced; keep existing Git-derived development build metadata.

Cargo references: [dependency overrides](https://doc.rust-lang.org/cargo/reference/overriding-dependencies.html),
[command-line config](https://doc.rust-lang.org/cargo/reference/config.html#command-line-overrides),
and [custom cfg registration](https://doc.rust-lang.org/cargo/reference/build-scripts.html#rustc-check-cfg).
The concrete Linux source recipe and full Cargo-metadata graph checks are in
the paired [Buddy guide](https://github.com/s116821/ReMarkableBuddies/blob/9ee80d8d5c9e540ba6c06884da11f8ef511dcfcf/docs/development-pre-enter.md).
It uses Rust/Cargo 1.98.1 and native x86_64-unknown-linux-gnu, with distinct
ordinary/developer locks and targets. No native shim is rebuilt.

The build script emits a private approval cfg only after effective selection
passes its guard. Both product crate roots include a compile-time refusal when
the diagnostic cfg lacks this approval. Consequently final-target-only
`cargo rustc -- --cfg buddy_development_native_pre_enter` cannot bypass admission
by withholding that cfg from the build script. The approval cfg is internal,
not an additional supported developer input.

## Existing release/package checks stay authoritative

Buddy's `cargo_identity` accepts one clean canonical Git SDK; it distinguishes
commit-pinned unqualified development from an independently proved stable SDK
tag. Its path-source refusal remains correct. `cargo_configuration` and official
build inputs constrain compiler overrides. The installed RM2 APK profile still
requires its existing SDK/bundle pin. A locally path-patched diagnostic must NOT
pass as ordinary source/APK input; no allow-patch, skip-proof or release exception
is added. Do not relabel this diagnostic as the installed resident package or
put it into distributed archives.

Only selected developer artifacts use the override. Ordinary tracked manifests,
locks, build commands, all-features coverage and release checks remain intact.
Removing a command-local patch is not a claim that an already resolved developer
lock reverted: ordinary builds use their independently retained original lock.
No byte-identical rebuilt ordinary binary is claimed by this precode.

## Native admission, input and limits

Use Native's distinct build-only profile, immutable manifest and real
handle-admission marker. The accepted manifest contract is 750 LF bytes with
SHA256 `3aff53ec9aa52ecc0ab61e1190dae6cd2dc8e0d78055473ff78a5b5be0d0f2d9`;
its private Qt/Dobby/compiler inputs and marker behavior remain SDK-owned. The
reviewed native candidate metadata SHA256 is
`23bd4f35ca6e298a35ce6ee5348f401b843c24337671c3c12eeed75ada5463fa`;
that identifies existing Native-owned evidence, not a binary copied into this
consumer handoff or a fresh device admission. Do
not copy those gates into a second owner or claim the manifest is a built/admitted
library. Ordinary StartupSelected stays false.

Ready, send completion or a fabricated consumer log is not an armed handle.
An execution observer must verify the actual bounded marker against its original
pending request/runtime/deadline and original device clock domain. Marker file
I/O still relies on outer containment; it is not a hard real-time guarantee.
Missing, partial, stale, late or mismatched marker means NO input step.

The eventual concrete ReadOnlyAdmission implementation must distinguish its ONE
specifically admitted Enter from an unrelated Reader-currentness lease while
retaining every applicable owner/health/deadline/retention check. Do not relax
unrelated edits, stale scope or lost recovery to make a fixture pass. A physical
folio Enter requires a human unless a separately verified, authorized mechanism
actually exists. No synthesized input or OSK event silently substitutes for it.

The copied result is historical, not semantic Submit, current draft authority,
edit revision, focus/clear lease or durable-save evidence. Source/offline checks
cannot prove the native edit occurred, independent visible-line-break evidence
or restoration. A later exact execution packet requires separate current fixture,
process/route/trust, ownership, input and recovery admission. No such operation
is selected here.

## Delivery and verification

Keep this central change open with its future affected Buddy PR; implementation,
verification, canonical sync and archival stay in the same coordinated delivery.
Do not merge/archive this as a completed planning prerequisite. Preserve ordinary
vs diagnostic evidence and all unresolved native gates separately. Focused tests
are listed in tasks; reuse unchanged SDK wire/retirement coverage rather than
repeat a broad native matrix. Neither handwriting integration nor SDK source
ownership transfers to this consumer change.
