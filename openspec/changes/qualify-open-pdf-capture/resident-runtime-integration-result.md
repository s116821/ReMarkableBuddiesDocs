# Resident runtime ownership result

Buddy `35e0f1d3a3cfc3a1295f4fe25fd64ce4ac07639c` implements the explicit
Linux child/admission/connection owner under
[resident-runtime-integration.md](resident-runtime-integration.md).
The owner copies and verifies approved artifact bytes into a fresh private
directory, clears inherited environment, publishes one synchronized admission,
authenticates one connection to its actual child, and retains the child and
connection for the session. Startup failure, shutdown and Drop close the
connection and attempt bounded termination/reaping of only that child.

Two recovery defects found during review are covered by regressions. A reply
publication failure now retains the original operation/digest uncertainty through
later calls and repeated close/shutdown, even after the SDK correlated the reply.
Journal reload still uses the actual stored outcome. If the activation directory
is renamed or replaced, runtime access refuses and cleanup diagnostics use the
retained directory descriptor. A replacement directory is never used for the
shutdown record; publication failure is reported in the shutdown result.

Independent design and implementation review accepted the final source. On
October 25, the final source passed:

- Linux `cargo test --offline --locked --lib workflow::resident_ -j 1 -- --test-threads=2`: 34 tests, none failed or ignored (26 client and 8 runtime tests).
- Linux `cargo clippy --offline --locked --all-targets --all-features -j 1 -- -D warnings`.
- `cargo fmt --all -- --check` and `git diff --check`.

The runtime tests launch a real owned Python process and use actual Unix sockets,
peer credentials, process metadata, admission files and Store journals. They cover
successful one-use admission, wrong artifact/loader environment, private-copy and
directory replacement, child exit, missing/late endpoint, missing/replaced
consumption, malformed Ready, original deadline bounds, shutdown/Drop, and reply
retention failure before and after outcome publication through journal reopen.

The earlier five-test run predates the recovery regressions. A later 33-test run
predates the directory replacement regression. Its strict lint found only an
oversized startup error value; boxing the optional shutdown report resolved the
source issue without suppressing the lint. Those runs are not credited as final
source verification. Local logs remain in `work/rem25-resident-local` as
`resident-runtime-linux-r1.log`, `resident-runtime-linux-r2.log` and
`resident-runtime-linux-r3.log`. The container has no Git executable, so its
build metadata warnings do not provide commit provenance; the source revision
above identifies the unchanged tested worktree contents.

This is an explicit runtime component, not installed activation. The test launch
removes LD_PRELOAD and uses a protocol fixture; it does not load proprietary code.
Actual bootstrap/preload and copied executable resources, stock-service handoff,
lazy first-gesture activation, heartbeat, crash-loop prevention, independent stock
recovery, Manager lifecycle, Reader handle reacquisition and capture/write/native
qualification remain required. No tablet action, service change, native capability
promotion, merge or archival occurred. Full hosted checks for this new source
remain pending; predecessor CI does not validate it.

Source basis: current implementation/spec files, independent source review and
directly observed Linux process/socket tests and compiler output. Product and
native acceptance remain separate.
