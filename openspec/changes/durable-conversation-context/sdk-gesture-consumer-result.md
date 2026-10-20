# Separate SDK gesture consumer result

Rust source `67c73e9c4a0a4a6ba5d4fb05eea8ef3d383629a6` is a direct successor of
`1f4b29134532f720dd4aba34a14549b295861ad7`. Precode
`f5f3f50c22e8abd686f256068e364af1365af3df` precedes implementation and starts at
Docs `bea05aba7191fd22ca1ad7bbc806e9d50a971140`.

Linked delivery: [Rust PR40](https://github.com/s116821/ReMarkableBuddies/pull/40)
and [Docs PR29](https://github.com/s116821/ReMarkableBuddiesDocs/pull/29). Merge
coordination remains with the ecosystem coordinator; neither parent nor this
delivery is merged by this result.

Eight changed files consume SDK
`5c0bc303bb9b22e8e01bce9b2bd2a7fe47c8010e` as specified in
[the integration contract](sdk-gesture-integration.md). Hardware diagnostics
change only explicit navigation orientation arguments. Pen changes and the
untracked pen tool remain excluded. Main rehashed all nine protected active
working files against the preservation snapshot before copying only the seven
mapping files; the original files were not modified or staged.

On the clean source, Main verified formatting, strict all-target/all-feature
Clippy (17.88 seconds), and six focused tests: three actual emitter controls,
unsupported source orientation/chrome refusal before dispatch, post-dispatch
orientation drift refusal without replay, and ordered-page orientation parsing.
All six passed. Compilation time is not a navigation latency measurement.
No complete navigation matrix or native device operation was rerun.

Sol independently inspected the committed eight-file source and assertions,
accepted both the precode scope and source agreement, and did not rerun these
tests. Copy/hash preservation is Main owner evidence. Required
[hosted source checks](https://github.com/s116821/ReMarkableBuddies/actions/runs/38434469227)
passed release policy, Linux build/lint and tests, including both tablet-target
crossbuilds. The title check passed. Hosted PR checks use the normal merge
checkout; these are associated with source67c73e9, not a claim of bare-head
execution or hardware qualification. Paired Docs checks passed Linux, Windows
and OpenSpec validation at d16a68f. Bounded task3.23 is complete; the full Reader
change remains active and unarchived.

The SDK produces a pure trajectory; Reader remains the event emitter. Persisted
portrait configuration is not active-page authority. One ordinary-error release
attempt is preserved, but process-crash release is unqualified. Unsupported
orientation/device profiles and the old unverified fallback refuse. Native
navigation/creation/bootstrap, landscape support, full Reader lifecycle, and
REM53 personalization remain outside this bounded delivery.

## Current-parent integration

Current source ff2bac2c1ce2ae9c630f154b1ef40417fe5afa7c normally integrates
original gesture branch 010aa6b and composed-memory parent 3ee307d. Its effective
child is the six original consumer/example source files, all byte-identical to
010aa6b. Cargo.toml and Cargo.lock remain exact current-parent bodies, retaining
SDK 32b86e4 rather than downgrading to the historical 5c0bc303 pin.

The cached current SDK gesture implementation was compared directly with the
original pinned version. Removing only three added provenance/license comment
lines makes the complete gesture.rs body identical. Types, supported profiles,
trajectory, timing and refusal behavior are unchanged. This is pure API/source
compatibility evidence, not a new SDK-native qualification or pin change.

Current Windows six focused controls pass: three fake-sink emitter controls,
unsupported source configuration/chrome refusal, post-dispatch orientation drift
refusal without replay, and fixture-only ordered-page/configuration parsing.
Strict all-target/all-feature Clippy with denied warnings, locked no-default
library, formatting and diff checks pass. Docs validation passes 39 items and
preserves 25 guidance files and 126 original source blobs. Original source/review
and hosted evidence remain separately attributed; no broad navigation matrix or
hardware diagnostic was executed.

Current exact-head hosted checks and independent integration review remain open.
Parent live-model/delivery, native completion, process-crash release, active-page
authority, other profiles and the full active Reader/MVP lifecycle remain open.
The tablet is owned by a separate human-directed effort and must not be contacted
until the human explicitly returns ownership. This preparation performs no SSH,
connection probe, device inspection, transfer, navigation, execution, service
change or cleanup. No permission follows from pure plans or fake-sink tests.
