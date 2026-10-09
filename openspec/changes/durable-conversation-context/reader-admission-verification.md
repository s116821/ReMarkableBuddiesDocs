# Reader admission checkpoint verification

This is partial implementation evidence for task 2.10. The change remains open;
no canonical spec sync, archive, native qualification or merge is implied.

## Source and review

- Rust implementation checkpoint: `b005b1beb9aec6dbeee89889561c4d4447eaf53c`.
- Rust repair checkpoint: `53b505803a1d4a8802d70198a8a9ab68e185b4fd`.
- Rust lint cleanup: `b8e176431d2824a5d7a1002e6ae56c9bfa0839fc`.
- Accepted API: [reader-admission-api.md](reader-admission-api.md).
- [Implementation evidence](https://github.com/s116821/ReMarkableBuddies/pull/30#issuecomment-6057359865).
- [Repair evidence](https://github.com/s116821/ReMarkableBuddies/pull/30#issuecomment-6057688438).
- [Independent repair closure](https://github.com/s116821/ReMarkableBuddies/pull/30#discussion_r4217717540).

## Implemented boundary

An immutable bounded Reader plan and separately sealed, owned source capability
are required for fresh Pending preparation. Original historical recovery runs
first and returns without minting output authority. Fresh construction publishes
through the canonical domain gate and retains the exact publication, source,
backend association and plan in a private context.

The selected backend facade owns its wrapped backend and exposes no unrestricted
DeviceBackend implementation or raw accessor. Actual Workflow dispatch validates
the matching context and consumes each ordinal before I/O. Errors, panics,
changed arguments and duplicate dispatch stop remaining work. Smart erase derives
its ordered rectangles from frozen image bytes using the shared Workflow geometry;
each lower call revalidates publication, uncertainty and source under the held
domain gate without holding a Store mutex over backend I/O.

Actual Attempt retains Fresh or Historical preparation tied to its Generated draft
and evidence. Historical preparation cannot dispatch. Legacy mutation methods
refuse once selected preparation is attached. The direct Attempt test supplies an
existing selected Store fixture and Generated draft; it does not model qualified
input acquisition.

The reviewed P2 repair excludes harmless unbound records from the uncertainty
ownership scan after full structural projection. Admitted Receipts and OutputPending
facts still require resolved ownership. A real unbound pending-fact negative control
continues to refuse.

## Verification provenance

Main executed ten context/facade tests at the repair checkpoint, including the
unchanged independent unbound-root reproducer and bound-only control, plus two
uncertainty tests. The independent reviewer rechecked these twelve focused tests
and closed the P2. Fixtures use actual temporary Store publications and recording
backends; they confer no production native authority.

A complete all-features serial regression passed before the final direct Attempt
test and P2 repair. Relevant SDK/legacy and persistence checks passed after the
direct Attempt addition. The subsequent [CI test job at the exact repair revision](https://github.com/s116821/ReMarkableBuddies/actions/runs/37762373501/job/113261712894)
passed in 7m37s. Its strict-lint job failed on 21 unused production-path errors,
large preparation variants and test-module placement.

The lint cleanup boxes both preparation variants and moves the unchanged test
module after the implementation. Main verified the moved module byte-for-byte
and reran all ten context tests successfully. Actual strict Clippy at this cleanup
revision reports only the 21 unused production-path errors; no lint allowance was
added. These paths remain unused until qualified production bootstrap exists.
Complete regression, strict lint and target builds at the final implementation
revision remain required gates.

## Remaining gates

- Production source capability and qualified acquisition ownership/bootstrap.
- Selected domain mutation and durable output settlement.
- Branch-bound qualified observations for selected render_answer; it currently
  refuses before effects. Selected history, setup and status acquisition also refuse.
- Full task 2.10 scenario verification, final regression, strict lint and target builds.
- Real evidence capture/persistence/restart validation and coordinated final review,
  spec sync, archive and squash delivery.

Source basis: linked repository source checkpoints, Main executed host checks and
the linked independent review. This document reports implementation and test
limits; it makes no hardware or production qualification claim.
