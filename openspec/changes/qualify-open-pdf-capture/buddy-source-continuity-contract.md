# Pure synthetic return-to-source continuity: assessed precode contract

Main and the existing independent Sol reviewer accepted this five-file contract
delta on2026-10-12. Implementatione3b1d8c is locally verified and independently
reviewed in [buddy-source-continuity-result.md](buddy-source-continuity-result.md);
native and logical-claim refresh gates remain unfinished.

This local extension follows the decision modeld1b9f1d and public Rust SDK pin
f6b7dc8954ba9f5a284d56568765e05c38483924. It matches supplied historical placement
and SDK navigation evidence; it performs no device/process instrumentation,
navigation, creation, target allocation, Store mutation or rendering. Native8112
transfer/activation remains held and untouched. It is not a different executor
or surface for that operation.

## Gap and model data

After a positive ordinary source/non-Buddy successor decision, the stored original
SDK observation is stale because inspection changed the visit/current page. Using
it in CreationRequest refuses; using the displayed successor would shift insertion
to the wrong source. The existing placement plan correctly preserves the original
anchor but does not retain the actual completed successor observation needed to
match a supported Previous receipt later.

Add a private plan continuity variant: UninspectedEnd or InspectedSuccessor holding
the exact opaque completion already validated by complete_successor. Only those
existing decision paths construct it. Preserve original key/order/conversation and
neighbor, with no public setters, arbitrary continuity constructor or rebasing.

## Pure matching API

A function accepts a private PlacementPlan, supplied fresh source PageObservation
and optional SDK-created NavigationReceipt. It accepts no mutable Platform,
DeviceBackend, persistence, renderer or effect callback.

For an inspected successor, require a receipt with Synthetic request-source,
completion and fresh observation. Its request.source must equal the privately
retained actual successor completion by full opaque equality; direction must be
Previous and target must be the original source key. Completion must identify
that same original key/document, preserve the exact original order, and equal the
supplied fresh source by full opaque equality. Validate nonempty unique order and
the original immediately preceding the retained neighbor in the original exact
order. The retained successor must preserve that order/document, and both original
and retained observations must explicitly have Synthetic origin. Do not compare
the returned complete observation
to the historical original as though legitimate return could preserve its visit.

For a verified synthetic end plan, require no return receipt and full fresh-source
equality to the retained original observation, with Synthetic origin and unchanged
exact order. Require UninspectedEnd, neighbor=None and the original still last in
that exact order. An unexpected receipt does not turn the end path into a fallback.

Missing/foreign/stale/wrong-direction receipt, replaced plan context, nonadjacent
or wrong target, changed order/document or opaque input/session/visit/instance
state refuses. No receipt may be fabricated through Debug parsing, private SDK
field access or modeled current-qualified booleans.

## Exact meaning of the result

Return SyntheticSourceContinuity with private historical plan and matched fresh
source/conversation getters, or an explicit unresolved reason. It contains no
target allocation, CreationRequest conversion, native receipt, Store claim,
renderer token or live effect authority. SDK-created observations remain
Synthetic; all decisions and this matcher stay outside installed Reader behavior.

The result only matches SDK model continuity at the supplied observation point.
Pure equality cannot prove the caller collected that observation now rather than
passing an older clone. Positive fixtures use the actual MockPlatform observe_page
result after return; this API is not a native freshness oracle.
It does not refresh historical recognition, logical association or original
non-Buddy absence. REM-37 records can change independently while SDK observations
remain equal. A matching continuity result must never be described as revalidated
logical claims or permission to create. Future effectful integration must separately
refresh/reconcile association and recognition, require the current qualified SDK
source guard and durable original-source placement/journal checks immediately
before publication. These remain unfinished gates, not implemented by this step.

## Verification and scope

Use supported MockPlatform observations and SDK-generated Next/Previous receipts
only to arrange local fixtures. Verify positive return with changed visit but
same original key/order, fresh end with no receipt, original placement preservation,
and zero policy effects/target allocation. Refuse missing or unexpected receipt,
foreign scope, wrong direction/target, stale completion, changed order and opaque
input/session/visit/instance state despite matching IDs. A fixture changing only
the supplied logical projection while SDK state stays identical must demonstrate
that continuity conveys no association/recognition revalidation or effect authority.
Preserve all11 existing decision and5 acquisition controls, no dependency upgrade,
Store WIP change or installed Reader/native activation.

Source basis: current decision source, exact public SDK observations/receipts,
reviewed original-placement contract and local API assessment. No native result
or production Store/current-device qualification is claimed.
