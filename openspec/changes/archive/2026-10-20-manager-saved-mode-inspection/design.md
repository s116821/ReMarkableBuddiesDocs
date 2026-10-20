## Context

Base Manager main is `87ba4e798025e37608093641596390fea4aa006c`; Docs main is
`b0eb7c74117bce7ec40bd9b3b94c16e1d5834e9b`. Both browser and Electron already
share identity-verified Linux/Windows wired callbacks and bounded one-shot
inspection/query capabilities. No overlapping Manager mode-inspection topic was
found in the current branches or open PRs.

The producer contract is published in Buddy draft67 at
`1a06873074e0ca382b022d0524b0fbf673b4aa94`:
[`docs/host-sync-mode.md`](https://github.com/s116821/ReMarkableBuddies/blob/1a06873074e0ca382b022d0524b0fbf673b4aa94/docs/host-sync-mode.md),
`src/mode_maintenance.rs`, `src/storage/sync/mode.rs`, and the existing
`src/storage/drive.rs::id` validator were read directly. Main owns that source
and central `operate-host-sync-mode` precode. This is a published implementation
contract, not a claim its final review, main delivery or publication has passed.

## Goals / Non-Goals

**Goals:** Explicitly inspect saved mode in both companions; preserve unconfigured,
LocalOnly, isolated and shared meanings; show truthful refusals; bind results to
the current wired session; expose a reduced display view.

**Non-Goals:** Initialize/choose modes, write configuration/storage, activate sync,
verify provider/group/bootstrap readiness, restore data, stop services, access a
Buddy API, run native operations or contact a development tablet. Main retains
all backend, ordinary-runtime and Store lease changes. No SDK, dependency,
version-authority or release-policy change is needed.

## Decisions

### One fixed inspect command

Add only `inspectSavedMode({connection_id,boot_id})` to the existing narrow host
surface. The Python adapter uses the same protected configured interpreter,
USB-only Linux/Windows route/trust callbacks and fixed Reader/configuration paths.
Its sole remote operation is `--sync-mode-operation inspect`, with no input marker,
query, path, arbitrary command or conditional token from the renderer. Close the
remote stdin immediately. Compare connection/boot identity before and after the
command; retain existing identity admission and cancellation behavior.

A capability probe does not establish an installed version threshold. Older CLI
or report versions remain unsupported; no private mode-file fallback, staging
writer, Wi-Fi fallback or running-service request is added.

### Validate privately and return a reduced view

The backend produces one UTF8 JSON line of at most16384 bytes including newline.
Reject duplicate keys, invalid UTF8, extra documents, truncated/oversized output,
nonzero exit and malformed structures before accepting a snapshot. Require exact
report keys, report_version1, operation inspect, activation_performed=false and a
boolean incomplete. Preserve the seven published statuses. Healthy display data
requires status ok, incomplete=false, exact data/current_snapshot keys and null
receipt/receipt_status. Non-ok inspect reports have null data and retain their
status without a fabricated snapshot; incomplete need not map to one fixed value
for every error (the producer can return unsupported with incomplete=true).

Snapshot fields are device/epoch/mode/token. Token actor is a nonnil UUID and its
digest is64 lowercase hex. Mode null requires null device/epoch. A chosen mode
requires nonnil device/epoch and the exact existing tagged shape: local-only;
isolated-backup with nonnil backup and binding digest; or shared-group with nonnil
group, binding digest and root_id. Root ID is1–256 ASCII alphanumeric, underscore
or hyphen, matching the producer's existing validator. Validate known fields and
refuse unknown variants/keys rather than guessing compatibility.

The privileged Node host maps the private report into a fresh `SavedModeView`
containing only status, incomplete and a nullable snapshot. Snapshot fields are
kind/device/epoch/group/backup; kind can additionally be unconfigured and absent
identities are null. Conditional token/actor, binding digest, root ID and receipts
are discarded before browser HTTP or Electron IPC serialization. Validate this
reduced shape again at the shared controller. Never return or log the raw report.
This preserves a useful UI without creating a renderer precondition/mutation API.

### Bound every host layer

The two-field host request is capped at256 bytes. The SSH channel caps backend
stdout and discarded stderr at16384 bytes each, with the existing2s I/O timeout,
8s collection deadline and12s Python guard. Node retains its13s child deadline and
a32768-byte private envelope cap, including the existing observation. The browser
retains14s and a16384-byte reduced-result cap. Reject overflow rather than truncate
to a healthy result. Same-origin/session, content-type, route/method/query refusal,
exact IPC arity, configured interpreter and packaged resources remain enforced.
No timeout or malformed response causes a retry, initialize, choose or service stop.

### Saved intent and session-bound UI

An explicit Saved storage mode action is available only after the existing wired
admission and host capability check. Unconfigured means no explicit saved choice;
it is not LocalOnly, shared membership or proof of an inactive worker. Show saved
mode, group/backup identity and Buddy data-device identity; epoch can be an
expandable detail. These are local metadata, not hardware serial identity or
current sync/service/provider/native health. Existing modes and capabilities are
not silently enabled by this panel.

Use the shared controller's generation pattern. Starting/replacing inspection,
cancellation, disconnect or an explicit tablet-state refresh clears its prior
view and invalidates late responses, including refreshes with the same IDs.
Retain truthful Busy/unavailable/unsupported/conflict/failure states. Busy offers
later retry without stopping or unlocking a service. Render typed text through
Angular and existing accessible Tailwind components; never interpret returned
metadata as HTML, a URL or a command.

### Owned implementation and evidence

New Manager files: host saved-mode parser/types and Python transport, shared
controller, guide, focused Node/Python/host fixtures and tests. Existing narrow
edits: observer, browser helper, Electron main/preload, host interface, app/profile,
package scripts, lint host-test list and exact preload-surface checks. Add the
affected Python suite to existing Checks and the new development/retained-package
host test commands inside existing Linux/Windows Integration jobs. Preserve the
metadata classifier, job graph, permissions, current safety commands, release
helpers, locks and artifact custody. No new stage or repeated common-check suite.
The existing whole-host packaging recipe should include the helper; change it
only if a focused package-resource check demonstrates a missing resource.

Verify meaningful parser positives/refusals and token/binding/root canaries absent
from both public host responses; actual fixed-command/EOF/deadline behavior on an
owned SSH peer; controller late-result/cancellation/reconnect behavior; and both
renderers in development and retained packages. Feed producer-owner actual CLI
reports through the real parser when supplied, preserving their immutable source
and owner attribution. Label synthetic transport/semantic UI reports separately.
Run affected checks and ordinary exact-head CI; do not replay historical native,
provider, compiler or unrelated feature matrices for this increment.

## Risks / Trade-offs

- Backend draft can change → keep its exact contract/review provenance, reconcile changed fields, and require actual qualified backend delivery before consumer merge.
- A busy ordinary Store can prevent inspection → show Busy without bypassing ownership or promising continuous status.
- A saved shared/isolated choice can be unusable at runtime → label saved intent and preserve unknown health rather than invent readiness.
- Private backend fields could leak through a generic envelope → reconstruct and strictly validate the reduced public view; assert canaries at both bridges and in renderer state.

## Migration Plan

This is additive and needs no data migration. One linked Docs/Manager change keeps
precode, implementation, verification, canonical sync, own archival and final
review together. Require qualified actual producer delivery and exact final CI
before normal coordinated squash delivery. Observe actual merged trees and main
release separately. Preserve all other active/archived work and physical gates.
Rollback of this UI leaves the stored choice and all Buddy-owned data untouched.

## Open Questions

Producer-owner representative actual report fixtures and its final qualified
revision remain evidence/delivery dependencies. The inspect-only wire fields above
are concrete enough for this consumer precode and focused implementation; they do
not require waiting for the producer's full publication merely to draft code.
