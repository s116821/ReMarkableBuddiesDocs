# Resident historical capture consumer result

Buddy `af265bdba34d9b12c5fccef3152a70bd711dfbb8` pins SDK
`80b29ebec3a46b6976e5288d2e8d65fbeccca816` and adds CaptureSource to the existing
Session request dispatcher and ResidentConnection. Original input, health,
runtime and deadline checks surround transport and final delivery. The reply
remains HistoricalCapture, with no conversion to PageObservation or writing
authority. Capture does not reserve or finish an effect-journal record.

Owned Linux request tests decode every pixel of a 192-by-128 PNG larger than
64 KiB, deliver two captures across explicit reconnection to the same child,
and reject corrupted images, changed source and truncated transport. Cancellation
and deadline tests withhold image delivery and retain the child. Both uncertain
insertion and selection tests capture successfully after reconnect, verify
unchanged journal bytes, refuse another conversation's effect and preserve the
original lost operation through shutdown.

Original v2 insertion/request/response and selection fixtures match the SDK's
retained hashes. They and existing v1 fixtures survive restart and v3 append
without re-encoding original records. Mutation-journal bounds remain unchanged.

## Executed local checks

- Windows all-feature library suite: 568 passed, 3 intentionally ignored.
  Strict all-target/all-feature Clippy passed.
- Linux resident suite: 130 passed on the same compiled binary using an executable
  tmpfs fixture directory and an init process. Binary SHA256:
  `b3610189e7e265fb8506d816f9e9680bd0cf8e1b8e97da35ac00e0d343ca5416`.
  This exercises production policy with owned peers, not native Reader state
  or power-loss durability. Linux strict all-target/all-feature Clippy passed.
  The local container lacked usable Git metadata for vergen; its test/check
  artifacts are not release artifacts or native build-source attestations.
- Docs: 12 tests, documentation checks and 88 strict OpenSpec items passed.
- Independent source review accepted the dispatcher, journal compatibility and
  unchanged uncertainty boundaries. It also verified the observation-only
  example's new profile/library pins against the retained revision-3 artifacts.

The first ordinary-container Linux run retained 129 passes and one existing
startup timing assertion failure. Its isolated rebuild/retry expired before
spawn. No production or test deadline was changed. A direct-binary harness first
refused PID1 admission, then refused execution on Docker's default no-exec tmpfs;
both are retained as harness failures. With an init process and explicit exec
mount, the unchanged six-case startup test passed, then the complete resident
suite passed. A separate synchronized-copy sample measured about 224 ms on the
normal container filesystem and 5 ms on tmpfs. This supports investigating host
I/O delay, but does not prove the cause of either earlier timing failure.

Original logs are retained under buddy-capture-linux-r1, buddy-capture-startup-r2,
buddy-capture-startup-tmpfs-r3/r4/r5 and buddy-capture-linux-final-r1. Earlier
failures are not relabeled as passes.

## Remaining delivery

SDK CI40715054528 passed at the pinned revision. Buddy
[CI40721613058](https://github.com/s116821/ReMarkableBuddies/actions/runs/40721613058)
subsequently passed at `af265bdba34d9b12c5fccef3152a70bd711dfbb8`, including
the build/integration jobs. That evidence belongs to this consumer revision,
not later capture-setup changes. At this revision the development observer sends
only one Observe; no new native candidate was executed or old candidate replayed.
Actual native capture, installed first-gesture source acquisition, Reader/Writer/
blank-start creation and reuse, native lifecycle/preservation acceptance and
coordinated sync/archive remain open.

Source basis: current source, independently checked fixture/artifact hashes,
executed local tests and GitHub CI. Native qualification is absent.
