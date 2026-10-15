# Design

## Existing contracts and source basis

REM-40's full current description and all twenty chronological accessible comments were read. The original measured native delay, accepted cooperative provider-only repair and later local TLS/size qualification remain distinct evidence. PR43's four authored files are reused, not reimplemented. The current Reader already records cancellation when its request guard fails; the integration must verify this through actual transport and durable calls.

## Decisions

1. Import the exact accepted backend commit on a separate topic over the current reviewed Reader source, not its unrelated layout/catalog ancestry. Preserve the protected original rust-rem37 checkout and prior branch refs. Resolve no dependency versions outside the accepted delta without a separately explained need.
2. A local server reads the actual immutable request and signals receipt before withholding a reply. A test wrapper observes that explicit receipt and introduces a modeled page/session ownership change before the production progress callback. This is controlled platform interference, not a native cancel gesture.
3. Record monotonic time when the actual callback rejects ownership and when the provider returns. Require return while the server still withholds its reply, with bounded cleanup even on assertion failure. Do not infer cancellation merely from eventual timeout or server release.
4. Run through actual Orchestrator and Ledger paths at recognition and contextual-answer boundaries. Assert retained source evidence, appropriate canceled facts, original interpreted question when one exists, no assistant output, no navigation/text and no extra dispatched request after loss.
5. Reuse existing client worker cancellation/join and workflow request guard. Preserve sticky input loss; no attempt to clear the guard to manufacture same-process readiness. Fresh provider-engine readiness is already covered by PR43 and is not retested here.

## Verification limits

Dummy auth and loopback responses are protocol/workflow proof, not external provider or physical input qualification. Cooperative async waiting remains distinct from hard preemption of synchronous setup/parsing. Run only new integration controls and necessary compile/lint checks locally; hosted required checks remain mandatory. Canonical synchronization/archive waits scoped implementation, verification and independent acceptance, and does not close native/parent/whole issue gates.
