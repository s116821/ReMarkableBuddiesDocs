# Concrete shared editor design — implementation pending

The existing general inspector discards its private digest and cannot authorize
editing. A new explicit Begin pauses polling first, then privately inspects the
original file through the new fixed producer selector. It creates a120s ready grant.
One Save internally prepares and applies at most once under one13s overall budget;
it never pauses again, refreshes conditions or asks a second confirmation. Producer
owns exact full-file serialization; the host verifies original private hash/intent/
projection linkage, not a reconstruction of Config from three fields.

Three finite controls keep a dirty-field set; origins remain visible. No saved
override maps to clear only after an explicit gesture; an explicit remove control
handles declared-null even when the selector already appears unset. Untouched keys
remain absent from the patch. A no-change producer result preserves original bytes.
Saved readback is separate from restart/runtime; no service/provider buttons follow.

Private original prepare bytes and apply packet are integrity-protected in memory
before possible dispatch. One active slot and at most8unresolved records are bounded;
reserve before dispatch, never evict an unresolved original for a fresh Save. A new
Begin is distinct, not replay or implicit resolution. Read-only status uses the old
exact packet and original target, reports only desired-file observation, and later
invocation refusal cannot settle it. No host-restart recovery guarantee/persistence.

A host-memory-only retained action lists original opaque references/safe target IDs
for reload recovery without another inspection or automatic remote status. Local
snapshots cannot renew a ready grant. A cancel of an old reference cannot kill newer
work. Explicit status/remote work still requires verified current original identity.

Both before-I/O directions matter: wrapped public maintenance invalidates ready
editor/forget references, and direct forget prepare/confirm/receipt/cancel paths call
the shared hook too. Raw observer receiver stays original so internal run cancellation
does not invalidate the same Save. Unknown originals remain private/retained. Every
await and final public bridge checks host generation/target; navigation/refresh even
with unchanged IDs invalidates ready views. Existing queued cancel ordering remains.

contract.md is the exact proposed API/reduction/phase/cap/lifetime authority for this
consumer. Original accepted producer wire is immutable. Source implementation waits
for independent precode review. Verification consumes original45reports without a
producer rerun, separates synthetic faults from captured bytes, exercises real HTTP/
main-frame IPC and normal dev/retained browser/Electron across both OSes, then own
canonical sync/archive in the linked delivery. Source basis is actual delivered
f43627ba/5f2e7175 plus accepted82717f; all new design choices are proposals.

## Cross-operation ownership clarification
A host-private single-I/O ownership token spans each Begin, whole Save, editor
status or direct forget prepare/confirm/receipt. Busy acquisition does not cancel
an existing owner. Editor status is remote I/O: when it acquires the idle slot it
invalidates any ready editor before dispatch; while a newer Save owns the slot it
returns invocation-busy without changing that Save or the older unknown evidence.
Host-memory retained and forget status do not acquire remote I/O or invalidate ready.

Targeted cancellation checks lane/reference/token ownership in BOTH coordinators.
The old forget request(cancel) unconditional observer.cancel must be replaced in
this implementation: a nonowner returns only local old-state information, without
observer cancel or the cross-I/O hook. A token-conditional finally cannot release a
new owner. Existing deliberate global cancellation remains a separate operation.
Required real HTTP/main-frame IPC race controls cover old-forget cancel versus new
basic apply, old-basic status versus active new Save, and status invalidating a
merely ready grant; preserve original bytes and all installed public guards.
