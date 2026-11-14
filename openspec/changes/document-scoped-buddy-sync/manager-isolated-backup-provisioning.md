# Manager consumer for isolated backup preparation

This work consumes [ordinary isolated root provisioning](isolated-root-provisioning.md)
through the existing privileged wired host. It does not create another publisher
or provider protocol. Root owns the Manager consumer; the Buddy producer remains
in its existing scope.

## First source increment

The host privately retains the complete successful inspect snapshot and the
original version-1 provisioning input. Preparation requires an existing isolated
choice. It never substitutes a LocalOnly/shared choice or invents a grant from
Manager sign-in. The exact operation UUID, conditional token, device, backup,
epoch and binding remain associated with the operation across output loss.

The private consumer accepts one bounded UTF-8 JSON line, checks the complete
producer envelope and the existing saved-mode snapshot grammar, and correlates
the result to the retained original. It preserves early errors without inventing
result custody. An absent isolated_root member is distinct from a null or
malformed member. It checks each outcome/status/incomplete combination and derives
current versus historical from the original token and immutable epoch choice.
A result-bearing report must retain the Store actor and persisted device and
report an explicit current mode. At the original epoch it must retain the full
original token, backup and grant. A later epoch requires a different token;
reusing the original backup also requires the original grant. A changed device,
unconfigured mode or contradictory token cannot be accepted as historical.
Malformed UTF-8/JSON is reduced to a fixed refusal without input excerpts, and
outcome values must be literal supported strings before enum lookup.

Only the reduced saved-mode view and result identifiers/outcome/currency may
leave this parser. Input tokens, grant digests, provider IDs, credentials,
operation UUIDs and raw output stay private. A verified root is preparation of
cloud storage, not evidence of a completed package, running publisher or native
page availability.

The focused tests combine explicitly synthetic contract frames with three
original Buddy command-harness report lines and their original request bytes.
Their hashes are checked before parsing current, historical and unqualified
outcomes. This validates the JavaScript consumer against Rust-emitted bytes; it
does not qualify a connected host action, real provider or tablet execution.

## Connected action

The transport, privately retained host service and shared browser/Electron UI
are implemented. Manager `eb0cc55` passes 47 private, transport-child, service,
loopback and controller tests, plus scoped lint and TypeScript checks. The new
browser/Electron distribution fixture and platform storage checks still require
hosted verification; live provider/wired qualification remains unfinished:

- The privileged host service uses the existing identity-verified wired
  maintenance transport, with shared ownership, deadline and cancellation rules.
  Commands, paths, original tokens and credentials stay outside the public IPC.
- Provide an explicit review and prepare action for an already selected isolated
  mode in the shared browser/Electron UI. Keep a lost response unresolved; a fresh
  inspect cannot stand in for the original provisioning result.
- Retain the original request for any explicit retry and use it byte-for-byte.
  Mode changes, account/grant replacement and connection or boot changes require
  refusal or separately reviewed reconciliation, never an automatic new root.
- Keep independent observations separate: saved mode, prepared provider root,
  latest verified package and current runtime status.
- Exercise the real host, transport fixtures, both UI distributions and current
  producer frames. Keep production qualification profiles unchanged.

The transport reuses `local_mode_choice_transport.py` and its fixed sync-mode
command prefix with the single additional selector `provision-isolated-backup`.
Only that selector accepts the original version-1 provisioning body and a total
budget up to 45 seconds, including identity checks. Its command phase is bounded
to 35 seconds to accommodate Buddy's existing 30-second provider window. The
observer has an independently configurable provisioning timeout, defaulting to
45 seconds; its existing ordinary timeout remains unchanged. Other selectors
retain their 12-second request and 8-second command bounds. Cancellation still
owns the child process, and lost or incomplete output is not an acknowledgment.
No transport retry, arbitrary command, path or endpoint is introduced.

### Host ownership and restart recovery

Retain dispatched originals in fixed `isolated-root-operations.json` through the
existing protected host storage helper. Reuse its checked directory, private
file access and conditional replacement; do not introduce a second credential
store, database, arbitrary filename or renderer-supplied path. Use a separate
fixed `.isolated-root-operations.lock` held by an OS file lock/exclusive handle
that releases when its process exits. The lock file may remain; its existence
is not ownership. Do not reuse the OAuth writer's exclusive-create sentinel or
alter the existing credential save/disconnect behavior.

The version-1 file contains at most eight append-only original records, each
with `reference`, `connection_id`, `boot_id`, `snapshot`, `input_base64` and
`input_sha256`. The input is the small host-generated compact V1 provisioning
body, at most 512 UTF-8 bytes. Each compact record is at most 2,048 bytes and the
whole file at most 20,480 bytes, below the existing private helper limits.
Validate the closed record and original snapshot, canonical Base64, input
digest and parsed input/snapshot agreement on every load. Preserve exact input
bytes; do not reserialize a recovered request. Actor/epoch and UI references
are unique, and append/CAS cannot replace an earlier record. No OAuth tokens or
duplicate credentials are stored.

The service must flush, replace and privately reread the exact original before sending it.
It releases the private storage writer before transport starts. If persistence
is uncertain, it does not dispatch. An existing original for that Store/epoch is
reused only through explicit original recovery, never replaced by a new UUID.
Retain all originals across lost output, cancellation and helper restart. A
reloaded original has an unknown result until an explicit original replay
receives root-verified evidence. A valid pending, authorization-required,
retry-later, recovery-required, unqualified or command-level refusal report does
not settle a previous uncertain dispatch. Display that report separately from
the retained uncertainty. Only root-verified settles this original's current or
historical evidence; it never releases the actor/epoch uniqueness claim.
An in-memory successful report is not invented after restart. No automatic retry
or silent eviction occurs when the bounded history is full. Changed connection
or boot identity refuses dispatch in this increment.

This increment guarantees original retention across host/helper process restart
after an acknowledged write, including interruption while holding the OS lock.
It does not qualify persistence through a system crash, power loss or storage
rollback. That stronger guarantee needs separately verified platform durable
replacement and recovery evidence. Storage uncertainty always refuses dispatch.

The public host request accepts only an action, observed connection/boot, an
opaque original reference and a fresh caller-generated `wait_id` UUID for each
begin/prepare/retry invocation. Cancellation carries that invocation's wait ID
and original reference; matching only the retained original cannot cancel a
later replay. The wait ID is transient cancellation metadata, not a Buddy
operation or retained-record identity. It exposes the reduced preview or captured report, and a
bounded list of retained references. Preparing a new operation uses the shared
maintenance owner; an invalidated ready preview cannot dispatch, and a stale
cancel cannot cancel another operation. A stale completion returns invalidated
without a captured report and cannot replace a later replay's evidence. A report
must match the retained row's connection and boot, as well as its original
device/backup/epoch; only prepare/retry can return one. One invocation has a single 45-second
deadline including storage and transport work; the undispatched review expires
after two minutes. Private storage or parsing failures produce fixed errors.
The host and public bridge implement these requirements. The shared UI uses a
fresh wait ID for each review, prepare or retry, rejects stale results, clears
reviews on peer actions or page lifetime changes, and requires explicit recovery
of an unresolved original on its original connection and boot. If Stop occurs
before a review has returned its reference, it abandons that local wait and
cancels a late ready preview by its original wait ID. It does not globally cancel
the observer for that action. Verified root evidence stays separate from package,
runtime and native-page qualification.

Tablet credential installation, choosing isolated mode from Manager sign-in,
provider namespace visibility, backup browsing/download and replacement restore
remain explicit following integration. They use this same preparation action and
the already accepted archive/restore contracts. No desktop authorization ID is
treated as a tablet credential or provider-root binding.

## Increment checklist

- [x] Review the private validator and reconcile exact producer-emitted frames.
- [x] Add the fixed wired command with separate bounded provisioning timeouts,
  original stdin/frame bytes and synthetic channel/child cancellation checks.
- [x] Connect host-owned original retention and explicit recovery to that command.
- [x] Connect and review the shared browser/Electron review, prepare and recovery UI.
- [ ] Verify actual host/transport/UI behavior and coordinated source/Docs CI.
- [ ] Complete separately scoped provider and wired runtime qualification.
