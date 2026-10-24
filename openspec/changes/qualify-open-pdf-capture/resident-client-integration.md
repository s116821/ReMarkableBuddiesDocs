# Resident SDK client and durable insertion journal

This continues the existing automatic acquisition delivery using SDK
`095f6c73777195b2bee56321a81857346a76ebde`. That revision provides the authenticated
Linux Client and resident dispatcher source; native activation/qualification is
still open. The SDK owns its adapter specifications. This document owns Buddy's
consumer behavior and does not replace the current-first/adjacent reuse contract.

## Durable attempt ownership

Keep a local native-attempt journal in the existing Store-owned data root, outside
generation replacement and synchronized conversation records. The Store's process
lease and shared mutex serialize access. This is an operation journal, not another
document/page binding registry. Existing Ledger bindings remain authoritative for
historical associations, with their independent current-device qualification.

Before any insertion request byte, reserve its conversation, original operation,
source, target, expected order, runtime/connection and complete canonical SDK frame
and digest. Persist the bounded strict-schema journal with file synchronization
and parent-directory synchronization on Linux. Windows fixtures do not establish
Linux power-loss durability. Initialization uses exclusive creation; replacement
uses the existing owned staging/atomic publication mechanism. Truncated, oversized,
unknown-schema or inconsistent records refuse access rather than resetting data.
The journal is bounded to 1,024 attempts and 8 MiB; reaching either limit refuses
new reservations without evicting original attempts.

Reject an already reserved unresolved/observed conversation or any reused operation,
including an identical request, a changed frame, a fresh operation or a replacement target. A reservation
survives caller failure, transport retirement, process restart and Store generation
changes. There is no automatic erase/retry API. A later reply is retained only as
historical correspondence; insertion observation is not durable native persistence,
current target selection or binding/rendering authority. Failure to retain a reply
leaves the original reservation unresolved. Only a durably recorded known refusal
before native mutation (or a client-proven failure before request admission) may
permit a new caller-selected operation for the conversation; the original operation
stays consumed, and the wrapper never performs an automatic retry. Read-only reconciliation uses that
same original source/target; target presence alone does not establish attribution.

## Connection boundary

The Linux consumer wrapper owns one SDK Client and the Store reference. It accepts
the Supervisor's independently verified runtime and retained activation-directory
descriptor, never fixture-echoed identity as production attestation. Observe and
Reconcile remain read-only. InsertAfter uses the durable reservation callback
before SDK pending admission/write. No automatic reconnect, mutation replay,
new-target fallback, runtime launch or restart is included in this increment.

The installed Reader's current synthetic acquisition seam is not converted into
native authority. Integrating current/adjacent Buddy recognition, target acquisition,
Supervisor activation/recovery, writing/capture and native acceptance remains open.
Historical SDK capture provenance stays unchanged.

## Verification

Exercise actual Store files and the consumer wrapper with owned Linux sockets:
successful reservation/reply, same/changed operation and conversation duplication,
lost replies, restart, malformed/partial/oversized files, failed journal publication,
concurrent callers and read-only reconciliation of the original target. Preserve
existing Ledger/decision and default simulator behavior. These are source/host
checks; native lifecycle, page preservation, writing and persistence require their
separately admitted device evidence.

Source basis: current SDK source and tests, existing Store primitives and Ledger
contracts, and the current REM-25/REM-57 handoff. The journal layout and wrapper
are this delivery's implementation design, not prior verified product behavior.
