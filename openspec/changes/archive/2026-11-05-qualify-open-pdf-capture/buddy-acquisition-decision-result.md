# Local Buddy acquisition decision model result

Implementation
[d1b9f1db6ae4a5c5aef519540f32079ef7f80833](https://github.com/s116821/ReMarkableBuddies/commit/d1b9f1db6ae4a5c5aef519540f32079ef7f80833)
follows the independently reviewed Docs precode contract862b5ad. It changes only
the new workflow/sdk_buddy_decision module and its workflow export. Installed
Reader, existing acquisition seam, SDK dependency, Store, native tools and held
8112 transfer/activation are unchanged.

The pure two-phase API resolves the relevant current candidate before successor
lookup. Missing association requires recognition, unbound Buddy recognition
requires adoption, and stale/imported/historical/conflicted/tombstoned or other
conversation claims cannot become duplicate insertion permission. Supplied
witnesses bind the exact opaque observation, logical page and desired conversation;
positive ordinary/other-Buddy recognition contradicting a relevant association
refuses. Candidate results retain private observation/conversation context.

Successor evidence must use the SDK-created Next receipt tied to the private
original anchor, immediate neighbor, unchanged order and fresh completed opaque
observation. Positive ordinary source/non-Buddy neighbor yields an after-original/
before-neighbor historical placement plan. Exact synthetic end yields a no-neighbor
plan. There is no target allocation, CreationRequest conversion, native receipt,
Store claim, renderer permission or effect dispatch in this module.

## Executed checks and review

Sixteen focused locked/offline tests passed:11 new decision controls and5 unchanged
SDK acquisition controls. They use actual public SDK MockPlatform observations
and SDK-generated navigation receipts. Fixture setup may perform simulated
navigation; policy calls preserve page/gesture counts and perform no SDK effects.
Cases cover current-only lookup, successor reuse, unknown/adoption outcomes,
historical claims, contradictory classification, original placement/end, full
opaque input/session/visit/order drift, witness page/conversation mismatch,
foreign/wrong-direction/stale receipt and nonadjacent request refusal. A stale
original CreationRequest is rejected in a controlled SDK API-limit fixture only;
the policy never constructs or dispatches it.

The ordinary locked/offline library check passed without the SDK mock feature.
Formatting and diff checks passed. Development builds emitted expected unavailable
Git metadata warnings from the read-only mounted source; they are development
test/check evidence, not official release artifacts. Main independently inspected
the source, exact API guards and complete supplied test cases; no remaining
actionable finding was identified in this bounded slice.

The lookup interface is an audited read-only contract, not a Rust sandbox for an
arbitrary implementer. Supplied consistent fields are modeled input, not proof
that a production Store/current-device association is qualified.

## Unfinished integration

Model results do not qualify native acquisition/current-page reuse, recognition,
adoption, durable binding, installed Reader or REM-38 delivery. Future creation
after successor inspection still requires supported return-to-original evidence
and a fresh source guard; the old original observation is stale and the displayed
neighbor must not become the insertion anchor. REM-37 owns the existing Store
binding/CAS, and this seam does not duplicate or modify that work.

Native8112 remains local-only and held after the platform reported a possible
cybersecurity risk without a specific offending command. No attempt was made to
replay the held operation through another executor, model, worker, surface or
weaker control. This independently permissible source/model work is not native
execution or a workaround for that safeguard.

Source basis: frozen contract, exact Cargo-pinned public SDK API, committed source,
local tool/test output and independent source review. No new tablet evidence is
claimed.
