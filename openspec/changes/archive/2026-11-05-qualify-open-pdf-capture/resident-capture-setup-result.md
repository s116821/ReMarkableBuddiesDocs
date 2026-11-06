# Native capture setup source result

Buddy `f026bb6385a2c450fa4d79542fb57c097b98673f` implements
[resident-capture-setup.md](resident-capture-setup.md) in the existing
development-only controller/observer. It adds the version-2 expected-source plan,
candidate/runtime-bound durable setup barrier, separate fresh input admissions,
one explicit same-child reconnect and one CaptureSource. Version-1 candidates
retain single-Observe behavior. Source inventory comparison and stock-first
recovery remain unchanged. Both diagnostic examples require the development
feature and remain outside release packages.

Independent source review found that the SDK's 30-second idle retirement would
invalidate a connection retained through a longer setup. The corrected observer
calls the tested `capture_after_setup` helper: reconnect and capture share the
same original request deadline and progress checks, without Observe, automatic
retry or mutation. The actor publishes its final acknowledgement only after
receiving the observer's fresh-admission record, so a fast successful capture may
reap its child without racing another actor runtime-liveness requirement.
Review accepted the corrected source; native behavior is not qualified.

## Local evidence

- The full resident suite passed 150 tests after the reconnect correction. Its
  owned Python peer models idle retirement by closing the initial connection;
  the regression verifies exactly two total handshakes, unchanged child identity,
  exactly one CaptureSource opcode, no Observe/effect commands and no mutation
  journal. Input denial, expiry and denial after the new handshake send no capture.
- One additional actor-side refusal test was then added. All six setup tests
  passed on the final source, including both-participant guard release/acquisition,
  invalid identity/order, partial/stale/replaced/duplicate records, observer
  cancellation, actor acquisition error/contact and missing-peer timeout without
  releasing capture. Four protected-filesystem tests are explicitly ignored in
  ordinary unprivileged runs and were executed with `--include-ignored` in the
  owned root Linux container; no device service was involved.
- Final all-target/all-feature strict Clippy, formatting and whitespace checks
  passed. The diagnostic workflow regression confirms the required feature and
  exclusion from ordinary release inventory.
- Central guidance checking and all 88 strict OpenSpec items passed before this
  result record; final document validation is required at publication.

The initial compile failed on two error-conversion mistakes; those were fixed.
Logs `capture-setup-linux-r1` through `r4` retain that failure and the subsequent
checks. The evidence copy also retains the completed prior consumer CI watcher;
manifest SHA-256 is
`582898ea37c46c24dd24c6a037a664b90125efacc4fbd0988bbd98b36c700c5b`.
The container's unavailable Git metadata warning is retained; these local builds
are source/fixture evidence, not a native or release-artifact attestation.

## Remaining native and product gates

No new tablet transfer, input, service change or native execution occurred.
The exact new revision still needs hosted CI and its frozen ARM artifacts.
The source-opening preservation policy and setup driver must be qualified before
a new candidate is selected; the current controller continues to reject every
source byte change, including metadata. Preserve all prior spent candidates.
Actual native capture, installed first-gesture source admission, Reader/Writer/
blank-start creation and reuse, native lifecycle/preservation, simulator delivery,
review and coordinated spec sync/archive remain open.

Source basis: current code, independent source review, executed host tests and
retained local logs. The owned peer is a transport model, not a native Reader.
