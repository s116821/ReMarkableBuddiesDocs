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
