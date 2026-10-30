# Copied-reader visual setup source result

Buddy revision `228f151151712a6b27c042e5e6a3e9649bb21775` adds an explicit
copied-reader binding to the developer screenshot example under
`development-resident-bootstrap`. The resident launcher uses a private executable
copy named `reader`; ordinary screenshot discovery continues to require `xochitl`.
The new mode requires boot ID, PID, start ticks, candidate nonce and executable
SHA-256, deriving the exact candidate-owned executable path from the nonce.

The helper retains the executable file handle, requires a regular root-owned
mode-0500 file with one link and a bounded length, and checks its path and metadata
through capture. Both opening and closing hashes read that same handle. Closing
verification occurs before returning pixels; failure discards the captured data.
Existing process, mapping, allocation-header and ambiguity checks remain in force.
The helper sends no signal or input and does not rename the process.

The first Linux regression run exposed a same-size executable write that could
share coarse timestamps. Metadata checks alone were insufficient. The corrected
implementation performs a closing digest verification with metadata checks around
the read. Preserve the first failed result alongside the corrected validation;
it is not a successful run on the final source.

Independent source review accepted the closing verification and explicit CLI
binding. The private operator setup driver now requires the resident flags and
refuses operation until a rebuilt helper hash is pinned. Any selected tap requires
a successful tap result and a retrieved, inspected after-image before completion.
A before-image may support completion only when no tap was selected. The driver
also derives one fixed operator deadline from the ready record, checks it before
each call, clamps transport timeouts, and reserves execution time before dispatch.
Monotonic time prevents a host clock rollback from extending a step. SSH timeout
does not prove remote termination; existing PID1/controller bounds retain that
responsibility. Independent review accepted this correction. All existing
controller/observer setup deadlines remain unchanged.

## Evidence and remaining gates

Final source validation passed:

- All 18 screenshot library tests, explicitly including the root-owned Linux
  executable-pin fixture, which exercises wrong hashes, permissions, replacement
  and same-size mutation refusal.
- All three screenshot CLI tests both with all features and with default features.
- All-target/all-feature strict Clippy, formatting and whitespace checks.
- Fifteen private capture/setup driver regressions, including delayed preflight
  refusing effect dispatch, deadline clamping and clock rollback, mandatory
  after-image inspection, mixed recovery refusal and source/image bindings.
- Central guidance checking and all 88 strict OpenSpec items.

Logs `copied-reader-visual-linux-r1.log`, `copied-reader-visual-linux-r2.log` and
`capture-driver-tests-r2.log` retain the initial failure and final checks. Local
container Git-metadata warnings remain visible. These are source/host results,
not release or native artifact attestations. No additional simulator behavior is
claimed for this developer-only visual helper; the discovered timestamp failure
is retained as a host regression.

The new helper needs a separately frozen ARM build. The already staged native
capture candidate retains its own earlier reviewed controller/observer source and
artifact identity. Do not relabel it as built from this helper revision. Neither
the copied-reader source checks nor earlier stock-library pixels prove actual
native capture, page identity, installed first-gesture acquisition, or automatic
Reader/Writer/blank-start creation and reuse. Those acceptance tasks remain open.

Source basis: current source, independent source review and executed host
regressions. No new device execution or copied-reader screenshot is asserted.
