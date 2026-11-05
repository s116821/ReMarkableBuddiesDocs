# Durable selection integration

Buddy `deb863b9a2b8cd94893d7b04eac635ecb5472706` implements
[the selection contract](resident-selection-integration.md), retaining SDK pin
`9880766f5bb0bdb91445716132703b02587d372e`. Insertion and current/adjacent selection
now share the Store-owned journal, operation namespace and execution/retention
path. Format 1 remains insertion-only; successful writes advance to format 2
without rewriting original frame/digest/outcome fields.

Observed insertion or selection permits a fresh operation only for selection of
the same document/target. Reserved and Indeterminate outcomes block both effects.
Later known refusals cannot erase an earlier target restriction. Exact selection
reply correlation includes document, target and complete order. Read-only
reconciliation selects the latest or an explicitly named original operation and
dispatches the matching insertion/selection command without rewriting history.

Independent design review initially identified an ambiguous publication-error
contract. The accepted policy makes the actual valid stored outcome authoritative
after reopening: an error reported after storing an observed reply permits only a
fresh same-target selection, whereas a missing outcome stays reserved. Unknown
native effects never become known merely by reloading. Every later effect must
synchronize the entire journal plus its new reservation before bytes. Source
review accepted the implementation; its requested selection-specific generation
restore regression is included.

On October 25, all **26 Linux journal/socket tests passed** on this source with
`cargo test --offline --locked --lib workflow::resident_client -j 1 -- --test-threads=2`.
They exercise actual Store files and authenticated owned sockets: reservation
before bytes, current/adjacent success, both directions of cross-kind operation
reuse, exact typed response refusal, lost/partial/indeterminate responses,
concurrent mixed effects, restart/generation restoration, chronological target
restrictions, v1/v2 historical insertion preservation and format refusal,
typed original reconciliation, and publication errors before/after retained
outcomes followed by reopen. The existing journal capacity and malformed-history
checks also pass. This is owned host evidence, not tablet or physical power-loss
qualification. The container cannot embed Git provenance; hosted exact-commit
checks separately establish source correspondence.

The earlier Windows run passed 16 journal tests before the last two portable
regressions were added. Final-source Windows strict lint passes with
`cargo clippy --locked --all-targets --all-features -j 1 -- -D warnings`. Broader
[Buddy CI 40230580096](https://github.com/s116821/ReMarkableBuddies/actions/runs/40230580096)
is pending at this checkpoint. Earlier passes are not credited to that gate.

The SDK documentation closeout at `d5e53034de62925f2a4fd663dd041df4d7d1f895`
also passed all required checks/build/integration in
[SDK CI 40229268079](https://github.com/s116821/ReMarkableOpenSDK/actions/runs/40229268079).
That does not qualify native effects or replace the consumer's own CI.

This selection API requires a separately qualified Buddy-target decision. It is
not an exploratory neighbor-inspection API: a positive result deliberately pins
the conversation target. Product inspection/return-to-original composition still
needs its own integration without bypassing these restrictions. Installed Reader
wiring, current/adjacent recognition and binding, capture/write/persistence,
Supervisor recovery and native acceptance remain open. No tablet action or native
capability promotion occurred; the coordinated change stays active and draft.

Source basis: current implementation and specification files, independent review,
and directly observed local test output. Native handoff findings remain separate.
