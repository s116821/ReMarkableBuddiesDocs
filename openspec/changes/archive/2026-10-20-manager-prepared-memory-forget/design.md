# Consumer design and source feasibility

## Decisions and ownership
The original durable SQLite recommendation was optional design exploration. Initial
scope chooses one bounded IN-MEMORY live-host slot, with explicit restart limits;
no database or journal implementation. Main owns all Rust preparation/conditional
Store publication/receipt/canonical hash work. This lane owns only future consumer
host coordinator, private transport/parser, reduced bridges and shared UI/tests.
Own inspection29/67 is delivered at72a171a/8503aad and must remain untouched.

Read all five original producer artifacts4a17be2 and complete successors34db7a5 and
64ff69ba plus golden. Full Root source review5583470985 was read: original local
ordinary lease alone does not prevent restore generation replacement; local first
confirmation must atomically compare+publish under one Store mutex, and receipt
must verify original expected parent contents. Corrected producer review and actual
implementation/corpus remain gates, not inferred from precode promises.

Exact public requests/states, caps and retention are in contract.md. Preparation is
from a deliberately inspected single value, but always gets a separate producer
preview; old detail never acts as permission. Confirmation is explicit and bound
to the displayed immutable reference, original same-admission scope/group/target.
Absent/tombstone/conflicting/opaque/unsafe previews refuse instead of filtering.

## Resolve current shared-helper lifetimes
Current browser-helper.mjs has one process-level cookie and one observer, shared
across tabs. Current observer personalizationSnapshot is memory-only; current
MemoryInspectionController is read-only and renderer generation invalidation is
not a mutation registry. Add a narrow host-owned coordinator shared by all public
entrypoints, not one map per renderer. One reserved slot before async prepare and
one synchronous claim before confirm I/O prevent same-host replacement/double click.
Only exact reference+original epoch may claim; no caller target/packet substitutions.

Do not attach invalidation to WiredObserver.run's internal cancel() indiscriminately:
run currently cancels the preceding child for every action, including future own
prepare/confirm/receipt. Keep underlying internal child cancellation unchanged;
public external observe/cancel/other-maintenance entrypoints explicitly notify the
coordinator. Its separate host-instance identity/observation epoch distinguishes
public invalidation from internal operation mechanics. Both helper and Electron
main route through that single coordinator; actual IPC/origin/session guards stay.
Browser main-document navigation/GET /preview/ and Electron main-frame navigation
invalidate ready references, even if another tab initiated it. JS/CSS resource fetch
is not a document refresh. Receipt retains original host identity/bytes across a
new observation epoch and can run only after reverified original target/boot; it
never rearms confirmation. Pause ordinary polling before preparation, then check
that displayed inspection/observation generations still match before dispatch.

The controller clears stale fact detail once confirmation is claimed and preserves
an uncertain operation notice across its own clear/refresh/disconnect. Host status
allows a reloaded tab to discover a retained unknown reference for receipt only,
not an executable preview. A new host with no slot must not erase a surviving
controller's uncertainty. Full process/UI loss cannot be recovered by this scope;
document it without inventing durable remembered history. Unresolved live-host
intent blocks competing prepares; no automatic eviction. A deliberate new intent
after actual custody loss begins with fresh current-state inspection/confirmation.

## Canonical byte feasibility diagnostic
Main's envelope-golden.json uses the existing Rust library's typed Envelope order,
recursive payload Value ordering and exact JSON escaping. Independently reconstructed
913UTF8 bytes in Python and Node match every byte and SHA256
 a32d40a07ce867ec4d0d738e0f5317636f5d8bcd9c62dadbd342ffc7fbf1f75c.
The already delivered supported-Fact parser accepts the safe-integer boundary.
This is a synthetic serialization diagnostic, not preparation/Store/mutation/device
execution. Original failed helper compilation remains producer-owned historical
evidence. Keep the golden fixture attributed; do not relabel it actual feature output.
Private generation fields are UUIDs, so earlier u64-generation concerns do not apply;
Fact timestamps remain safe-integer constrained for this new preview only.

## Meaningful validation and lifecycle
Test two clients/tabs sharing actual helper auth, prepare reservation/Busy, expired/
stale/replaced references, duplicate claim and asynchronous cancel races. Keep real
Electron IPC arity/frame checks and public/private schema validation installed.
Exercise every exact phase/status/incomplete/outcome row and malformed/raw-private/
foreign packet, numeric/bounds/UTF8/EOF/exit/partial-output refusal. Use transport
fixtures for before/after possible-dispatch cases; they do not prove remote abort.
Actual producer corpus must include atomic local restore/publication race, selected
base/generation changes, expected-content tampering and historical receipt after
later value with no new commit. Consume those attributed original bytes without
rerunning producer cases. Distinguish no-confirmation-on-receipt-absence from a
healthy not-dispatched proof. Verify live-host refresh/disconnect uncertainty,
full restart custody loss and no automatic new intent/retry across both hosts.
Run current ordinary Linux/Windows dev/retained-package checks, inspect fixture UI
captures, independent source/contract review, own canonical sync/archive and final
composed delivery after qualified producer. Observe actual main/publication separately.
No tablet/provider/service operations or unqualified physical claims.
