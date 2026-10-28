# Vendor companion integration checkpoint

The measured dependency gap is recorded in
[the native error-screen result](resident-error-screen-result.md). The selected
[two-process contract](resident-vendor-companion.md) retains direct-parent SDK
authentication and the existing activation-group recovery model. It requires an
explicitly owned companion; it does not start the original bound sync service
beside an inactive stock service.

## Verified launch inputs

Bounded read-only inspection verified the actual original unit, HOME drop-in,
executable hash/mode/size, current environment, working directory, Type=simple,
zero watchdog, nice level and dependency graph recorded in the contract. Broker
queries associated the current original sync process with `no.remarkable.sync`.
No pairing, account change, executable transfer, companion launch or new resident
activation occurred during this inspection.

An owned Linux host probe then exercised Rust `Command` against an open executable
descriptor through `/proc/self/fd`, retaining the original path as argv0. Both the
normal case and an intentional pathname replacement executed the admitted inode;
the executable descriptor was closed at exec. The probe used its own harmless
program and preserved both filesystem cases. It does not establish native rm-sync
compatibility, resource lookup, integrity during a writable-file race, readiness,
or companion shutdown behavior.

## First source increment

The fixed broker-observation module queries only the system broker. It checks name
presence, retains broker ID and unique connection owner, queries PID through that
unique name, and brackets owner and broker ID before returning the observation.
An absent name returns no owner; malformed output, changed evidence, cancellation
or expiry refuses. The caller must still compare this observed owner with its
owned companion incarnation. The module cannot activate a missing service.

The bounded subprocess runner now supports progress checks before spawn, in each
poll and before successful output delivery. Existing service calls retain their
previous no-op progress behavior. Cancellation still attempts bounded reaping of
the actually spawned helper and reports failure when that cannot be established.
Independent source review accepted the corrected broker and progress paths.

The expanded service suite passed 56 tests, explicitly including protected-filesystem
fixtures. The actual owned-child cancellation regression waits for the child to
publish a ready marker before canceling and checking its reaping. Broker tests cover
absent ownership, malformed/changed owner and broker replies, expiry, pre/post-query
cancellation and transport failure. A further delivery regression closes both child
pipes and allows one complete EOF-draining poll before releasing the child to exit;
cancellation after reaping therefore exercises the final delivery guard. Independent
review accepted this refinement. Its first execution exposed a test setup error
(creating the same private directory twice), corrected by retaining the created
path. The final three progress tests and strict all-target/all-feature Clippy passed
on Buddy `08809fc48f7b946656e610488bfa121f29bf50dc`; formatting and whitespace checks
also passed. The earlier 56-test run used the same production source but preceded
the deterministic delivery-test refinement. Linux host logs retain the build's
missing-Git-metadata warnings; this is source validation, not an ARM artifact or
native execution result.

## Still required

The broker primitive is not wired into resident startup or requests yet. Admitted
inode execution, two-child ownership, original companion stop/group admission,
ongoing integrity, shutdown accounting, versioned profile/candidate changes and
verified companion restoration remain unfinished. No installed capability or
native acceptance follows from this source increment. The full Reader/Writer/
blank-start creation/reuse, simulator, native and coordinated delivery gates
remain required.

Source basis: current source and independent review, owned host tests/probe and
read-only vendor process/unit/broker evidence. Architectural selection remains
distinct from native qualification.
