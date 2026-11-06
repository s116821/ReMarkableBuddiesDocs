## Existing host boundary

The completed [host design](../archive/2026-11-06-own-host-exchange-history/design.md) and canonical owned-exchange-history requirement define exact latest-exchange eligibility and truthful modeled outcomes. The current sole PageBackend implementation is modeled; it is not a native range API. Reuse that controller rather than introduce another history registry.

## Unfinished native integration

Obtain an actual platform-issued current page/session/visit/content and owned-region capability, compare the complete original state at the native effect boundary, and verify operation-correlated completion plus fresh readback. Do not synthesize current ownership from saved layout, screenshots, coordinates or restored data. New user editing, page departure, replacement or any ownership loss invalidates eligibility.

Persist/reconcile interrupted native effects with conversation/presentation state without replaying an uncertain action or resurrecting stale responses. Unknown results stop effects and require explicit read-only reconciliation; do not compensate by broader deletion. Preserve older exchanges, draft/focus/status/header, source records and external exports. Native synchronization does not transfer an old live grant.

Qualify actual first/latest/repeated actions, user-edit races, page/visit changes, cancellation, replacement/restore and restart uncertainty, including legacy coexistence and newline/persistence findings. Measure actual ownership/latency and use verified completion rather than a fixed stall. These requirements remain unimplemented/unqualified; modeled host success does not close them.
