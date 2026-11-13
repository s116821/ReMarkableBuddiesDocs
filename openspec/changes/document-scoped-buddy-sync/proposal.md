# Document-scoped Buddy backup and shared sync

Status: active, partially implemented; not provider-qualified. The coordinating maintainer owns continuation and independent review; the storage author owns the worker candidate. Existing domain/native drafts remain with their owners and the original generic API reviews retain their provenance. Ten completed API requirements are synchronized to the canonical specification; the nine unfinished end-to-end requirements remain in this active change. See [bounded delivery status](implementation-status.md). This linked delivery does not close the parent change or REM-52.

## Why

REM-36 provides immutable records, causal branches, recovery bundles and a bounded optional Drive worker. It does not provide the shared-sync policy now required: different source documents preserve both writers, while competing edits of the same accepted document revision select the first valid upstream commit and replace the losing local view. A filename, timestamp, local mutex or expiring lease alone cannot enforce this policy across tablets.

## Scope

- Explicit local-only, isolated device backup and selected shared-group modes, with distinct identities and namespaces. Manager-to-tablet control and restore use hardwired transport; internet access for optional cloud storage remains allowed.
- Buddy-owned durable history, bookkeeping, source references and export correlations grouped by logical source document; independent stable keys for subject memory, handwriting and portable configuration. Domain schemas remain owned by REM-37/24/26/53.
- Reuse REM-36 envelopes, content-addressed objects, media coverage, recovery validation, credentials and worker bounds. Add only the aggregate selection, conditional publication and local operation-fencing contracts needed for shared mode.
- Candidate Drive mechanism: immutable commit slots identified by provider-generated IDs known to all writers of the accepted base. A bounded metadata-only create pointing to a preverified immutable descriptor chooses the winner; no mutable shared head or distributed lease is proposed. Provider qualification remains a gate, with explicit fail-closed behavior if a claimed slot is incomplete or invalid.
- Versioned OS/file status and maintenance commands for REM-42. UI and transport implementation remain with Manager's owner.
- The [Manager isolated preparation consumer](manager-isolated-backup-provisioning.md) retains the original private command input and validates reduced root evidence before connecting the fixed wired action to both UI distributions.

Native reMarkable documents, rendered Buddy pages, ink and native file metadata are excluded. Turn screenshots and confirmed-learning samples are Buddy-owned media, with explicit inclusion/omission/completeness reporting. No pairing, firmware change, native mutation or personal-account sync follows from this proposal.

## Delivery and dependencies

Rust base: `s116821/ReMarkableBuddies` main `ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`. Docs base: main `8008389fa676d395401e6f28e049b47baa7b10ef`. REM-37 schema inspection: `673c5781cd5d89a89d712b9d8253433c920dc37c`, especially `src/conversation/types.rs`. This reference is an integration input, not permission to copy or modify its unfinished lane. Agree aggregate projection and operation fencing with that owner before domain integration; generic transport and storage work need not acquire native capability.

Review the proposal/design/scenarios together, implement the accepted contract in the owned Rust branch, verify the exact Docs/code pair, sync canonical contracts and archive only completed scope. Neither this draft nor host fixtures closes REM-52 or the ecosystem 1.0 gate.

## Read-only outbox recovery enumeration
Add bounded original-intent enumeration so recovery callers need not parse private journal files or already know operation UUIDs. This is custody only; provider/current/domain/native authority remains separately checked.


## Source-aligned shared worker integration continuation

At Buddy72ddbe5557222947f6a85167a7cb58c3601cb0e5 / Docsa1f446b8c4857e4f17726a0cb40ed62b8048b71a,
implement the real producer-to-worker-to-winner-adoption path using delivered
mode/outbox/fixed-slot/selected/admission primitives. The concrete precode and
interface conflicts are in [shared-worker integration](shared-worker-integration.md).
The coordinating maintainer owns independent review and integration; the storage author owns the
candidate, while existing domain/native drafts remain preserved.

This includes current notebook Source3/NotebookPlan/NotebookStage product data
through a reviewed identity-preserving selected-notebook compatibility stage and
actual selected producer. A legacy-only fixture is insufficient. Existing format4
maintenance and the deferred inspection-only observer are not reopened. Provider
resources/qualification remain unexecuted and publication unavailable until the
actual binding is approved. No planning-only merge or full-parent completion is
selected; implementation, verification, as-built sync and completed-scope archive
belong in the eventual paired delivery.


## Shared-worker successor r2 review corrections

The [integration design](shared-worker-integration.md) now specifies read-only
agreed-slot observation without a candidate; explicit CreateGroup allocation under
ordinary mode followed by exact conditional shared-mode selection; current-original
same-ID retry versus stale observe-only recovery; and passive first-join/pull
receiving custody with receipt-first crash reconciliation. No outbound attempt is
fabricated. It also makes staged mixed-scope readiness depend on exact local
registration across all product paths, separates active/retained causal projections
and imported history from verified local uncertainty, chooses committed-not-applied
for unresolved selected-receipt overlap, and requires notebook live/reopen validation
parity and original-only capability reconciliation. These are proposed corrections
after protocol/domain review, not implementation or runtime evidence.

Later provider qualification may use a suitable existing explicitly authorized
OAuth/account binding with isolated disposable app-data resources and exact cleanup;
a new account/project is not mandatory. No live credential/resource action or
production eligibility is selected. Original precode remains preserved; corrected
precode acceptance still precedes implementation and the eventual paired lifecycle.
