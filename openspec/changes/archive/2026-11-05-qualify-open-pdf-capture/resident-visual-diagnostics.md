# Visual setup diagnostic precode

The spent native cc059b attempt reached matching observer-ended and actor-ended
records, but retained no before-image/ready, observation.json or observer.exit.
The actor failed a bounded service observation and independent recovery reported
success. These facts do not prove visual request dispatch or identify a cause.
Repeated synchronous service/broker admission is a source-level timing concern;
Qt initialization and sleep logs are not capture delivery evidence.

Add development-only, private, exclusively created visual diagnostic JSON files
under the existing control root. Each bounded record binds the complete existing
nonce/candidate/runtime binding, sequence, elapsed monotonic time, remaining
original deadline, selected visual stage and a finite phase/outcome. Sync each
record before its corresponding operation or next phase; cap output at 48 exclusively created records of at most 4096 bytes and
error text at 512 characters, preserve partial files as incomplete diagnostics, and grant no
completion, source identity or native authority. No per-poll logging is needed.

Trace actor-ended consumption, pre-capture progress, same-child reconnect
completion, capture API invocation/returned reply, PNG publication, whole capture
error and shutdown entry/result. The API entry is recorded inside with_connection after its initial companion
admission, immediately before invoking capture_visual_with_progress. Invocation
is not proof of actual socket write: the existing SDK API does not expose that boundary. Errors must be retained
before owned shutdown/Drop; diagnostic failure must never suppress shutdown.
All original deadlines, candidate/service/input guards, same-child ownership and
no-retry behavior remain unchanged. No protocol or installed capability change.

Exercise the real visual observer flow with delayed, expired and failing progress;
verify durable phase ordering and error retention before caller shutdown/next
actions, bounded output and refusal without image/ready/extra request. Preserve
all existing visual-stage admission and request-route controls. Native diagnostic
qualification requires a new reviewed artifact/candidate; cc059b remains spent.

The selected format is visual-diagnostic-NNN.json, separate from completion
markers. Normal full capture uses at most 32 diagnostic records (including both
reconnect/API pairs and shutdown), below the hard 48-record cap. A conservative 42-record ordinary controller/recovery inventory plus the hard
48 diagnostic records fits the existing 128-file bound; diagnostics add at most
192 KiB. Existing collection remains capped at 128 files/4 MiB; no limit is increased.
Failure to retain an entry refuses the following normal action, but shutdown
runs even after diagnostic initialization, record creation or count failure.

Anchor the observer setup120 deadline before diagnostic construction and outer
entry retention. Successful diagnostic result retention also rechecks that same
phase deadline after fsync; expiry records an error before onward action. A
returned record followed by error means the callback returned and its original
phase deadline had elapsed by retention completion, not successful delivery.
Those records alone do not attribute the consumed budget to callback execution
versus diagnostic retention. Shutdown remains
mandatory even when the deadline or diagnostic retention has failed.
