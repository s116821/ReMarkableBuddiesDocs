# Storage preparation implementation evidence

## Source and scope

Manager implementation: `8bce05b905568ffeb69d4a2c6fc1a76a8f953261`,
tree `2761e5b54430601a77f220185e40cd68823c5027`.
Accepted Manager predecessor: `d7c12096ec9fbe91d832ed0c8d5cf412f8a1b7a3`.
Docs predecessor: `efde6b8e5eec493926d77f80b3f0760e9cad05ce`,
tree `e857e9414ff28f486d76c5d3f9b9c403ac5c792d`; precode imported in
`b226804`. The five contract/proposal/design/delta/config bodies are unchanged
from that pre-implementation commit; tasks and this results document track work.

This change adds no producer behavior. It consumes the existing fixed no-input
Initialize/inspect commands. Source equivalence of the mode module was verified
before implementation; its Git blob is
`80e9a21b9e1a7b2d447b830c6796f47ca32c97a0`. No physical tablet, account,
provider, firmware, native-page or filesystem qualification is inferred.

## Local qualification

On Linux with Node 24.21.0 and Electron 44.4.5:

- All 935 Node unit cases pass, including 14 initialization host/raw/public cases,
  nine controller cases and one supervised child case. They cover command-free
  review, one dispatch, retained original success/uncertainty, exact cancellation
  and early fences, late-output ownership,120s expiry,8record/32invocation limits,
  all four saved-mode kinds, raw/private/public size and lexical admission,
  private-field reduction and lost public delivery.
- Nine Python transport cases pass, including an actual local POSIX SSH peer for
  both fixed selectors, zero remote stdin, before/after identity checks,
  remaining channel budgets, output/stderr caps, nonzero/malformed reports and
  one-response deadline behavior. This is software SSH qualification, not USB or
  physical-tablet qualification. The local POSIX peer case is skipped on Windows.
- Both actual browser and Electron host factories exercise all 18 admitted
  maintenance predecessors:36 Busy directions and 33 preview invalidations each.
  Busy changes no raw-call/cancel counter. Pure policy review sends no producer
  command. Actual Local-only and initialization unknown histories survive peer
  actions in both directions.
- Development App checks exercise 53 incoming-action Busy guards/invalidations and
  18 outgoing controller clears. Actual queued observation tests cover a late
  reply, Stop before dispatch and14s expiry before dispatch. No late dispatch or
  global delayed cancellation is admitted.
- Real browser and Electron UI checks cover separate policy/confirmation,
  current-only inspection, Stop/pagehide/hidden/Read tablet state invalidation,
  retained uncertainty, disabled repeated initialization, narrow one-argument
  preload/main-frame IPC, guarded loopback routes, keyboard operation and 390/
 1280 px layouts. Packaged host resources match source bytes. Native Electron
  captures use actual window content geometry and capturePage.
- Lint, development/production builds,10 workflow fixtures,13 release fixtures,
 12 Docs unit cases, public guidance/source-blob validation and 109 strict OpenSpec
  items pass. The production size cap is unchanged. The initial candidate was
 290bytes too large; reduced repeated UI copy resolved the failure. Final initial
  bundle size is 649.92 kB, below the 650 kB error ceiling; the 400 kB warning remains.

The retained Linux package identifies the clean implementation source as
`0.0.0-dev-8bce05b90556`, `official:false`. It is a local validation artifact,
not an official release. Original failure logs, revision-specific passing logs,
screenshots, source bundles and payload hashes accompany the review handoff.

## Outstanding coordinated gates

Foundation smoke/style/wired and packaged smoke regressions pass. One source run
completed all assertions but returned 143; its log is retained. A repeat through
an explicit subprocess status collector completed every assertion and exited 0;
no source change or cause was established. The packaged initialization run also
exited 0. Windows source and downloaded-package CI, independent source
review, normal actual-main integration, final-head CI and canonical sync/archive
remain required in the same paired delivery. The central change stays active
until qualified; this is not a planning-only delivery or completion of broader
management, installer or release/MVP requirements.
