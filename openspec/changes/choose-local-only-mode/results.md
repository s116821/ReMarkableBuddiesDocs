# Qualification checkpoint

This change remains active. Independent review, required hosted qualification,
canonical sync/archive and coordinated delivery are pending.

## Exact implementation

Manager `f9b30c164638c5ef47671f11f0a7eb48a258d3a2`, tree
`a5c353db5b304aa44254bf4942207a3f923eef3d`, parent
`3d0e746807c7296c32d95ce684f2005233045d07`. The26-file change adds a separate
coordinator/protocol/transport/controller/UI and integration checks. Original
`host/saved-mode.mjs`, `host/saved_mode_transport.py` and `src/saved-mode.ts` remain
byte-identical to the parent. Existing inspect wire and canonical contracts remain
unchanged. Proposal/design/delta are at Docs `27e08552559fb8f991f5e3fb7503f82419b5eafa`.

## Local evidence

- Exact clean source production build/package, lint and full Node850 tests pass.
  The production initial bundle reports617.38kB against the existing400kB warning
  budget; budgets were not changed. Local package is development identity
  `0.0.0-dev-f9b30c164638`, official:false, not an official release.
- 22 focused host/controller tests cover strict fixtures/receipts/fingerprints,
  malformed output, incomplete unsupported/failed uncertainty, one dispatch,
  known pre-mutation refusal, expiry/cancel/late reply, unrelated owner custody,
  same-ID/foreign session, capacity and current inspection preserving uncertainty.
  The never-resolving observer control returns within its injected25ms budget.
  Actual product/local coordinator interlocks are covered separately.
- Seven Python mock-channel/subprocess controls pass: strict requests/bounds,
  fixed inspect/choose commands, one stdin send plus EOF, no resend on send failure,
  before/after boot checks, exact output cap, framing/duplicates/UTF8/nonzero exit,
  remaining deadlines/stderr cap and sanitized invalid-input output.
- Actual development browser and source Electron UI pass deliberate choice/new
  same-valued epoch, failed-afterpossible unknown, reload with retained originals,
  separate current inspect, privacy, main-frame/arity guards, pagehide/hidden,
  unchanged-ID refresh and120s preview expiry. The development App matrix passes49
  peer Busy guards,49 incoming invalidations and16 outgoing peer clears.
- Production browser and retained Linux Electron package pass the same user flow
  and lifecycle checks; package tests compare the three new host runtime resources
  to source and exercise sanitized invalid input.390/1280px screenshots were read;
  content wraps and the explicit confirmation is visible.
- Existing product-maintenance regression passes both browser and Electron:
  240 invalidation/240 Busy directions with predecessor210 preserved, the original
  46 incoming/15 outgoing product App assertions, queued-Begin and four held
  observation/quiescence cases. Hosted Windows qualification remains pending.

## Preserved findings

The first App matrix exposed a missing Local-only clear in product editor entry
points that preserve their own controller. Explicit local invalidation was added
to begin/save/check; the unchanged49-direction assertion matrix then passed.
An initial preview-expiry fixture installed the fake clock after a real timer
already existed. Creating a fresh preview after clock installation fixed the
fixture; the120s bound and disappearance assertion were preserved. Early fixture
extraction omitted its assert import, producing unavailable synthetic responses;
the import was restored before final850-test qualification. Failure logs remain
with compact implementation evidence.

## Evidence limits and remaining work

The twelve producer report fixtures are consistently sanitized synthetic
derivatives, not original receipt bytes or integrity authority. The fixed lower
transport/producer is synthetic in host/UI controls. Current producer source/tests
define selected preservation and post-commit/prefix uncertainty; these were read,
not executed again. No physical tablet, provider/cloud, service control, native
runtime or installed-release compatibility was exercised. Windows source/package
qualification and required CI remain hosted gates; final review and both actual
main/release outcomes remain separate coordinated work.
