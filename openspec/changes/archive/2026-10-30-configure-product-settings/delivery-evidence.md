# Scoped configuration delivery evidence

This closes the supported Reader/Writer enablement and Mem/Disabled export-backend
increment. It does not close all REM-42 requirements or qualify live native,
provider, account, running activation or automatic Reader-to-Writer behavior.

## Exact implementation and hosted qualification

The coordinating reviewer supplied the following final success receipt. Hosted
observation belongs to that reviewer; the SCRAPPY local tests are separately
attributed in consumer-evidence.md and source-proof.json.

- [Buddy PR114](https://github.com/s116821/ReMarkableBuddies/pull/114), exact
  `060d012ab60438d8bec933ff296afb3ff5fa05d8`:
  [full run41005995620](https://github.com/s116821/ReMarkableBuddies/actions/runs/41005995620)
  succeeded. The Linux regression
  `linux_reader_gate_precedes_notification_connect_and_keeps_trusted_predotenv_settings`
  explicitly passed. No tablet or actual service activation follows from it.
- [Manager PR51](https://github.com/s116821/ReMarkableBuddiesManager/pull/51), exact
  `eb3da3e47d8c9dafee00dc961b610358ab46bb76`:
  [full run41010792992](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/41010792992)
  succeeded: Checks123916018719, Build123916796844,
  Linux Integration123917208915 and Windows Integration123917208950.
  The PR Release job was normally skipped.
- [Independent successor review](https://github.com/s116821/ReMarkableBuddiesManager/pull/51#issuecomment-6516026570)
  accepted the test-only repair, native source identity, unchanged original
  assertions, actual queued-Begin regression and affected verification logs.

## Preserved failed predecessor and specific repair

The initial Manager `0e9a63ee194a9deeca7049d7652f5a33c69dd1d3`
[run41008003257](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/41008003257)
failed both integration jobs at `product-app-boundaries.mjs` for `beginModel`:
clear calls0 instead of1. Both240 ownership matrices had passed before that
failure; their success did not prove the subsequent App fixture setup was valid.

An actual App reproduction matched the failed object: the preceding DOM still
said ready while a new Begin was busy, its controller view/draft were empty,
the old select showed false and the peer correctly refused before clear hooks.
The old fixture waited only for ready text and could accept that preceding DOM.
This was investigated rather than dismissed as an unchanged-run flake.

Successor eb3 changes only `tests/fixtures/product-app-boundaries.mjs`. It binds
each idle setup to a fresh opaque reference, actual ready/not-busy/no-peer state,
and acknowledgement of the selected false value in the same reference's exact
draft/dirty map. A separate queued-Begin case verifies the correct Busy refusal.
The entire original46-boundary list and clear-count/DOM/draft assertion suffix
remain byte-identical. Production behavior, protocol and owner callbacks remain
unchanged.

Local affected checks passed on matching held application inputs: lint;46 actual
App cases with a250ms synthetic inspect delay; source browser/Electron240
invalidation and240 Busy directions each,46 incoming/15 outgoing App clears and
four held-observation cases per host; packaged browser/Electron240+240 matrices;
and source/packaged lifetime DOM checks for pagehide, hidden visibility,
observation refresh and120s expiry. Production debug seams remain absent, so
packaged matrix tests are not misrepresented as the development46-case execution.
The earlier cf7 App receipt is not automatically credited to later lifetime edits.

## Specification and evidence parity

Only product-settings-companion is synced:4 requirements and9 scenarios. The
canonical requirement body exactly equals the approved delta body (SHA256
`067da9446eba66bc7251e976f137a5b001e60bec1831c264eaf411279d1f8fe4`).
The129-definition corpus remains SHA256
`9f0f2b6e1f2e9c49323390f8038f93fc5a0cd6765dde9f2400e0215e08914152`;
its96 consumer cases,19 producer storage cases and14 lifecycle expectations are
kept distinct from actual behavior executions. The sanitized public producer
fixture remains SHA256
`1b46e345fa493c2d2dac516cf63a050aa995157ecb001d9e650a095329cd8ae8`.
It removes only the original capture's unnecessary fixture_root wrapper line;
all captured record/request/stdout strings remain unchanged.

## Completed local hygiene and remaining coordinator work

After the current verification use ended, bounded cleanup removed1,153,800,750
logical file bytes from ignored Manager package, dist, dependency/build caches
and reproducible test outputs. Measured free space increased1,186,029,568 bytes;
that allocation measurement is distinct from logical file sizes.

All404 useful test/failure/visual evidence files were first preserved in a local
verified evidence archive (SHA256
`4b429dd5c15b8bd92956f503c4d5fe2286f4fd55bbb1ee30d50884753c2f1e4e`).
Source worktrees, branches and native bundles were preserved. No active Manager
process or other owner needed the removed paths. Installed Node/OpenSpec/Xvfb
review tools and the existing Docs validation environment remain; no generated
Manager binary/package/cache hold is retained for a hypothetical future purpose.

The scoped specification is synced and this owned change archived in the same
[Docs PR123](https://github.com/s116821/ReMarkableBuddiesDocs/pull/123).
Final Docs successor review/CI, coordinated squash merges and actual-main release
verification remain coordinator-owned and are not claimed here. Broader runtime,
native/provider, account/destination and full REM-42 acceptance remain open.
