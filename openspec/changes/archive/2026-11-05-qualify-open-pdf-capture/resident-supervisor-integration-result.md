# Supervisor ownership and service-observation integration

Buddy `ac7c04042a16b1bc3b7984eef522812d967d4e06` adds Linux
`workflow::resident_supervisor` and its read-only `service` module under the existing
coordinated PR60. Final local tests and strict lint pass. Exact-commit hosted
validation remains unverified at this checkpoint.

The ownership component captures the actual parent incarnation/membership,
boot/namespaces, exact cgroup2 mount and original group identity. It distinguishes
populated, unchanged-empty and original-absent observations without granting
recovery authority. Exclusive synchronized lease publication retains the original
stock baseline, Buddy invocation and exact systemd start timestamp, profile and
adapter hashes. Current caller membership is checked before and after publication;
a late mismatch leaves the record occupied. Each live Lease pins the inode it
opened and rejects replacement during that handle's lifetime. Reopen strictly
validates retained bytes, metadata and boot; it does not establish original-inode
continuity across separate helper lifetimes. Partial/stale/malformed records are
rejected rather than repaired or overwritten.

The service observer invokes a fixed `systemctl` with explicit properties, cleared
environment and an option terminator before the unit. Nonblocking bounded pipes,
one operation deadline, and bounded child cleanup avoid unbounded wait/join paths.
Its recovery observation brackets the group read with two matching terminal
service snapshots and returns the exact group, terminal-identity and policy facts.
It distinguishes retained original metadata from the stricter fully-cleared
inactive/dead case. It still requires independently verified installed policy,
the common activation latch, qualified deletion semantics and helper context.
It cannot start stock or activate native code.

Independent source review covered the design and implementation. Findings fixed
before final validation included mandatory Buddy invocation and systemd timestamp,
identity file kinds, same-byte lease replacement, caller membership around
publication, preserving the bracketed group outcome, checking the deadline after
final lease reads, command option separation, forced-restart policy and fault
tests that assert the actual expected failure cause. The EOF regression records
that both pipes closed while the child remained alive, then requires timeout and
successful reaping.

## Validation chronology

- `resident-supervisor-linux-r1.log`: initial fixture setup failed because its
  synthetic invocation contained 31 hex characters. Validation correctly refused
  it; the fixture was corrected.
- `resident-supervisor-linux-r2.log`: 47 intermediate-source resident tests and
  strict all-target/all-feature Clippy passed. Later fixes superseded that source.
- `resident-supervisor-linux-r3.log`: 50 tests passed and the runtime fault test
  failed before its child launched. The old assertion discarded the underlying
  error. Its 800 ms budget included copying/hashing/synchronizing the interpreter;
  timing pressure is plausible, not established as the historical failure cause.
- The runtime fixture now reports mode/full failure details, still requires the
  child to have launched, gives its post-spawn fault cases a three-second operation
  budget, and requires completion within six seconds. The deliberately delayed
  fixture still waits ten seconds. Production deadlines are unchanged. A separate
  already-expired-deadline test requires refusal without a run directory or child.
- `resident-supervisor-linux-r4.log`: all 58 preceding-source tests passed in
  52.08 seconds; this does not validate the later service review fixes.
- `resident-supervisor-linux-r5.log`: final-source resident suite passed all 59
  tests in 65.09 seconds (26 client, 10 runtime, 16 ownership and 7 service tests).
  Strict all-target/all-feature Clippy completed successfully in 7m32s. Formatting,
  diff checks, shell syntax, Docs provenance and all 82 OpenSpec items also pass.

Final Linux commands were `cargo test --offline --locked --lib workflow::resident_
-j 1 -- --test-threads=2` and `cargo clippy --offline --locked --all-targets
--all-features -j 1 -- -D warnings`. No production source changed between that run
and the Buddy commit above. The fixture script is separately frozen and verified
by its source hash in the device result.

The files above remain in the local `work/rem25-resident-local` evidence directory.
Tests use actual Linux files, owned children, sockets and proc metadata, with
explicit fake cgroup/service snapshots for refusal logic. They do not emulate the
vendor cgroup filesystem or establish native authority. The container's missing-Git
build metadata warnings do not identify its source revision.

## Device evidence and remaining delivery

[The fixture result](resident-supervisor-fixture-result.md) preserves the earlier
five recovery cases, the later metadata-clearing observation and a fresh directly
populated-group deletion refusal followed by PID1 removal. All temporary units
and exact archived remote files were cleaned up, with unchanged real service
snapshots. A separate read-only sample confirmed the exact 26-property command
contract; installed Buddy still lacks the proposed recovery policy.

Implement the actual bounded recovery/stock verification helper and fixed common
activation latch, then installed service definitions, main-loop heartbeat,
first-gesture handoff and Manager lifecycle. Qualify shutdown cancellation and
native bootstrap before enabling effects. Reader/Writer acquisition, reuse,
binding/capture/write composition, persistence, preservation and cancellation
acceptance remain open. No merge, archive or native capability promotion follows
from these support tests or fake-service observations.

Source basis: current source/spec files, independent source review, direct Linux
test/compiler output and retained target command archives. Proposed installed
behavior is explicitly distinguished from implemented support.
