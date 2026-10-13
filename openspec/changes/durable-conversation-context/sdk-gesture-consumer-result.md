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
tests. Copy/hash preservation is Main owner evidence. Hosted platform checks
are pending at this result checkpoint and are not inferred from Windows lint.

The SDK produces a pure trajectory; Reader remains the event emitter. Persisted
portrait configuration is not active-page authority. One ordinary-error release
attempt is preserved, but process-crash release is unqualified. Unsupported
orientation/device profiles and the old unverified fallback refuse. Native
navigation/creation/bootstrap, landscape support, full Reader lifecycle, and
REM53 personalization remain outside this bounded delivery.
