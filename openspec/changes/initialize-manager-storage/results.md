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

## Action-bound public admission correction

Independent source review found that a malformed host reply could present a
prepared result/current kind to policy-only Begin, a ready result to Cancel, or
an unrelated connection's unknown original to Begin. The genuine host was not
shown to emit those values, and no physical dispatch was established. The public
validator and shared controller needed to reject them independently.

Manager successor `deb513355c08efb0c4a10af9120f6235c62b6ec1`, tree
`8052e0fdfb91a91a7a9a32259b94ea29b5d44e69`, restricts ready to Begin, forbids
prepared/current on Begin, permits current only on Confirm/Refresh, and binds a
Begin unknown to the requested connection. It intentionally permits an older boot
for that connection-only historical block. Existing original-row lookup is reused
for the outcome/current-identity checks. The host producer/dispatch and old mode
parsers are unchanged.

All 28 focused cases pass at this successor: 16 host/raw/public, 11 controller,
and one supervised child case. New malformed public/controller variants have
genuine policy, original success, no-current replay/cancellation, older-boot
unknown and current-inspection positive controls. Lint passes. The earlier
935-case full suite and package/matrix receipts retain their earlier-head
attribution; they are not later-head qualification. The same central contract
clarifies action admission without changing the accepted requirements or delta.
Final-head hosted qualification and independent recheck remain required.

The first correction commit `3482ce6` passed focused tests/lint but exceeded the
unchanged production size ceiling by 96 bytes. The successor consolidates the
same admission conditions into the existing state/shape clauses; all 28 focused
cases and lint pass again. No whole package/peer matrix was repeated locally: the
wire, genuine host state machine, command dispatch and resource packaging are
unchanged, while focused genuine-result controls exercise their compatibility.
The production build is checked because the public validator enters the renderer
and the prior build was close to its existing size ceiling.

The consolidated intermediate `8ae8669` was still 9 bytes over the ceiling. Final
`deb5133` removes a duplicated early observation-status check: the existing final
observed/unconfigured branch continues to reject every non-observed current kind.
The full 28-case focused selection and lint pass at that final correction. Both
failed build receipts are retained separately from the final build result.

Production build at clean `deb5133` passes: initial total 649.99 kB under the
unchanged 650 kB error ceiling; the 400 kB warning remains. No package rebuild or
physical/provider execution was performed for this correction. Existing earlier
Linux package custody remains attributed to `8bce05b` through independent review.
Normal actual-main integration already completed at Manager `3740eea1` / Docs
`a668b211`, with complete tree equality to those original implementation inputs.
This correction follows those integrated heads on the same owned branches.

## Complete historical action and identity controls

The original action-boundary cases were independently rechecked as resolved at
`deb5133`/`bd2a67b`. Review then identified adjacent malformed replies: a no-current
Confirm replay or Refresh could select a prepared/unknown original with a foreign
connection/boot, and an unknown/current Refresh reply could be mislabeled Confirm.
No genuine host emission or physical dispatch was established.

Manager `1f258ce39f15127aef524167289815177a2b4e14`, tree
`f715b31464927e7c4d24e09481b6183722acaed3`, binds prepared/unknown originals to
both request identities for Confirm/Refresh, regardless of current presence.
Confirm/current additionally requires prepared. Begin's connection-only older-boot
unknown block and Cancel's no-current historical echoes remain valid. Genuine
unavailable wrong-session refusals keep their closed historical rows without
claiming an outcome or current authority for the refused request.

All 30 focused cases pass (17 host/raw/public, 12 controller, one child). One new
matrix checks all 48 combinations of two historical outcomes, four selecting
request actions, current/no-current and same/foreign-connection/foreign-boot rows.
Genuine retained reads and wrong-connection/boot Confirm/Refresh refusals are
positive controls. Controller mutations separately cover foreign no-current
Confirm/Refresh custody and unknown/current Confirm, preserving only the correct
local unknown history on refusal. Lint passes. Shared predicates replace repeated
checks; matching request identities plus existing observation identity checks
preserve the original/current relationship without a duplicate comparison.
Prior build/package/full-suite evidence retains its exact earlier source.

The coherent boundary also reserves state none for Retained. Additional malformed
non-Retained none variants are rejected, including a Confirm that would otherwise
discard local uncertainty. Genuine retained history, Begin/Cancel semantics and
all 48 historical combinations retain their controls. No new host dispatch or
state format is introduced. The 30-case selection passes again at the final
successor; earlier counts/builds remain separately attributed.

Production build at clean `1f258ce` passes at 649.90 kB under the unchanged
650 kB error ceiling; the 400 kB warning remains. No package/matrix reconstruction
or tablet/provider operation was performed. The original `8bce05b` Linux package
was retired after its independent review purpose ended; source, captures and logs
remain preserved. Corrected-head hosted packaging/qualification is separate.
