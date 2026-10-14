# Acceptance and delivery checklist

- [x] Read REM-52 and prerequisite/domain/Manager issue chronology; inspect REM-36 source and central contracts and active REM-37 record types.
- [x] Inspect provider documentation and maintained sync prior art; distinguish candidate mechanism from live-provider proof.
- [x] Propose modes, conditional publication, source-document projection, local fencing, media/restore/status contracts before implementation.
- [x] Obtain independent review at ebf8c72 accepting generic fixed-ID metadata create-or-read and transport fixtures only.
- [x] Obtain independent review accepting the admission/settlement/projector/application-matrix contract at 7e06d9; no implementation or live qualification follows from this acceptance.
- [x] Obtain Main's exact0830a9af owner review5442770097 and refreshed673c mapping; SCRAPPY owns storage, Main owns domain/journal/backend paths. Schema2 acceptance remains coordinated separately.
- [x] Obtain Main's efb8fd73 review accepting the coordinated proposal for an isolated selected-store/projector fixture slice; add history/bitmap admission coverage and propose the precise token/commit/activation/journal interfaces for owner agreement.
- [ ] Review the precise interfaces/journal extension with Main before shared domain/workflow edits; verify and independently review the disconnected real-store projection fixtures without claiming activation/admission implementation.
- [x] Read Main's exact0830a9af owner agreement (2026-10-07T13:09:56Z): SCRAPPY's selected storage implementation is unblocked; Main retains domain journal/projector/admission ownership.
- [ ] Complete and review the selected snapshot read-path increment, then implement guarded commit and one durable winner-plus-retained activation with original-selection replay and fault recovery. Interface agreement is no longer a blocker for this storage work.
- [ ] Implement and verify the accepted generic adapter slice without enabling shared-mode publication.
- [ ] Qualify or reject the candidate provider primitive using an explicitly authorized disposable app-data namespace; preserve reproducible evidence without secrets.
- [ ] Implement accepted generic scope/selection and conditional transport seam, reusing REM-36 domain-opaque storage and bounds.
- [ ] Implement mode/binding isolation, bootstrap/catalog registration, outbox replay and first-winner replacement without stale auto-rebase.
- [ ] Integrate domain-owned aggregate projection and in-flight operation fence without duplicating REM-37/24/26/53 schemas or granting native authority.
- [ ] Implement versioned OS/file status, explicit portable configuration/media policy and validated selected-backup maintenance contract for REM-42.
- [ ] Verify two-client same-base winner, sequential A-to-B transfer, different-document/global preservation, clock skew, stale offline attempts, lost acknowledgement and interrupted publication.
- [ ] Verify clean/replacement tablet bootstrap, deletion/tombstones, corrupt/unknown-schema/interrupted restore, native page lag, active operation invalidation and intentional/incomplete media.
- [ ] Verify join/leave/switch/local-only and isolated backups cannot publish emptiness, merge namespaces, delete other backups or reuse device secrets.
- [ ] Run relevant Rust checks/simulator coverage and central Docs checks; distinguish host/provider/native evidence and remaining gates.
- [ ] Publish exact linked Docs/Rust revisions, inspect CI/bot feedback, obtain final independent review and coordinate merge order.
- [ ] Sync final as-built canonical contracts and archive completed scope only; retain unperformed provider/native qualification as explicit unresolved work rather than checking it off.

- [ ] Independently review the guarded commit/atomic activation increment: bounded hash-linked accepted history, original-selection replay, shared ancestor context, abrupt process-exit recovery, stale token/causal conflicts, media refusal and unrelated scopes.
- [ ] Implement portable selected backup/restore/migration policy before enabling these maintenance paths for selected stores; current explicit refusal prevents silent metadata loss.
- [x] Implement and locally verify the [portable selected archive/inspection candidate](portable-selected-maintenance.md), preserving original transaction/history/retained/media and unrelated data without minting portable live tokens; retain explicit restore/migration refusal until activation policy is implemented.
- [ ] Independently review the linked portable archive/inspection candidate and verify its exact published source/Docs revisions and CI before integration.
- [x] Add and locally qualify read-only original-publication predecessor lookup for Main's historical selection-pin validation, without minting live tokens or changing current membership.
- [ ] Independently review the linked predecessor lookup and its exact published qualification before domain integration.

- [x] Implement the bounded selected snapshot/guarded commit/activation/replay candidate; checkpoint cca7ea9d passed hosted CI, with domain/native/provider integration still disabled.
- [ ] Independently review retained-only settlement linkage and generation-feature old-reader refusal with exact linked source/Docs revisions; qualify source against the unchanged older reader.
- [x] Qualify retained-only publication with actual abrupt child-process exit before/after activation, original receipt/media reopen, unrelated-scope preservation and competing activation using one captured token; these are host storage fixtures, not domain/native/provider qualification.
- [x] Publish a reproducible [host qualification procedure](qualification.md) using the unchanged older test binary, an ordinary-open positive control, selected-format refusal and current-reader reopen; retain the separate domain/native/provider limits.
- [x] Verify exact noncanonical object/reference preservation and snapshot reference order for Main's immutable ancestor lookup; domain projection must not recompute object identity from parsed JSON. This is storage evidence only; Main's domain fix/review remains separate.

- [x] Repair and independently review post-open complete selected snapshot lineage refusal, including missing/corrupt parent metadata and parent-only required record/media; preserve exact-source prior review evidence.
- [x] Locally reproduce the post-open lineage read failure on the prior source, repair it with existing history/closure validators, and pass four corruption/restoration cases plus the affected selected-storage suite; this is host evidence, not independent successor approval.

## October 12 evidence reconciliation

The accepted repair checkbox above refers only to Buddy423cb0b / Docsc9f3ce7
and [independent five-case Windows receipt](https://github.com/s116821/ReMarkableBuddies/pull/31#issuecomment-6072364455).
It does not close generic modes/worker/provider/domain/native/maintenance or
whole REM52 acceptance. Earlier predecessor/archive acceptance retains its
original scope. No new Rust, provider/device operation or test matrix follows
from this Docs-only correction.

Main owns REM24 local memory domain/provider/context on its existing REM37
parents. The current generic contract is Namespace::SubjectMemory/schema1 with
record UUID identity, parent CAS and tombstones. The proposed portable memory
identity is profile UUID + Global|Document(stable UUID) + independent fact UUID
with a domain-frozen canonical UUIDv5 recipe. Main's local-only adapter refuses
selected stores; shared aggregate/catalog key, exact selected reference closure
and domain restoration/admission remain explicitly unimplemented. Per-record
CAS does not automatically establish a remote fact slot when membership shares
a document aggregate. Preserve unrelated document/global scopes and retained
evidence; do not create a second sync engine or change generic Store semantics
as a shortcut. Source: current domain-owner handoff and accepted storage/design;
this paragraph records coordination, not a new implemented wire schema.

## Archived selection domain-validation seam

- [x] Implement token-free historical selected-backup inspection with exact head/reference order and included media handles; reuse full archive validation and retain restore/migration refusal.
- [x] Verify real Store export/inspection, mixed namespaces, noncanonical references, retained media, absent/invalid scope, bounds, corruption of another scope and unchanged source/destination state.
- [x] Publish exact linked archive successor and obtain bounded independent review at2ed/540; no domain restore/provider/native qualification.

## Cumulative selected receiving read budget

- [x] Implement caller-owned budgeted selected snapshots with pre-I/O charging across heads/history/record verification/parsing/media and sticky exhaustion; retain full lineage and existing API semantics.
- [x] Verify real Store cumulative multi-scope exhaustion, historical/media/metadata limits before I/O, exact-bound positives, absence and unchanged tokens/source state.
- [x] Publish exact budget successor311/c93 and coordinate Main receiving caps with bounded independent review; no metadata-only or live-provider claim.

## Historical selected-envelope custody

- [x] Return already parsed historical selected envelopes in original reference order within the budgeted accepted lineage, without additional validation I/O or live tokens.
- [x] Verify actual Store re-rooted identity with and without retained old chains, facts introduced after Initialize, exact noncanonical reference order, unchanged budget usage and current-view separation.
- [x] Obtain bounded independent custody review of immutable488/943 content and Source488 CI; preserve prior accepted revisions.
- [ ] Reconcile advertised DocsPR7 pointer and exact successor Docs CI before linked delivery closure.

## Durable selected outbox preparation

- [x] Implement original-operation journal/replay, explicit local withdrawal and current-token/binding/object validation using existing Store/file/slot primitives.
- [x] Verify real Store restart/fault/replay/stale/binding/generation/media and unrelated-scope controls without network/native effects.
- [ ] Publish exact paired revisions and independent review; preserve unfinished mode/bootstrap/adjudication/worker/provider/domain/restore/lifecycle gates.

## Accepted immutable increments

Independent archive read acceptance is review5495568634 at423->2ed/7d->540;
budget/lineage is5495556299 at2ed->311/540->c93; custody is5495938187 at311->488/c93->943.
These close their bounded independent-review portions only. The advertised DocsPR7
pointer remainsc93 despite correct owned943 branch, so current linked-PR/CI
reconciliation and whole-delivery lifecycle remain unchecked.

## Outbox staging-residue recovery repair

- [x] Reproduce7e4 interruption residue before new intent and beside committed pending/withdrawn journal; reuse exact safe owned staging cleanup.
- [x] Verify preparation/withdrawal residue recovery, replay/current-token/descriptor/media preservation and unsupported foreign-entry refusal; deterministic residues are not actual process-kill evidence.
- [ ] Publish exact paired successor and same-reviewer P2 recheck before claiming outbox incremental acceptance; mode/binding proposal stays separate.

## Explicit mode/binding control

- [x] Implement private mode actor/device/backup identities, current tokens, original-operation replay and mode leases with legacy worker exclusion.
- [x] Bind selected outbox to shared mode epoch and verify transition/restart/replay/lease/binding/leave-rejoin/refusal/unrelated data preservation through real Store fixtures.
- [ ] Publish exact paired mode successor and independent review; keep actual worker/bootstrap/provider/domain/native qualification open.

## Read-only prepared-slot observation

- [x] Reuse exact provider metadata/descriptor validators for prepared GET-only observation and post-create observation.
- [x] Verify same/different pointer, account/app mismatch, absent/invalid/corrupt slot and no create/allocate/update/delete through host HTTP fixtures.
- [ ] Publish exact paired successor and independent review; live provider/bootstrap/domain/native authority remains unqualified.

## Persisted mode identity repair

- [x] Reproduce persisted reused backup identity and same-binding identity discontinuity through actual Store reopening.
- [x] Enforce load-time continuity and first-use identity; verify snapshot/lease/replay refusal, valid restart/replay and root-only replacement outbox control.
- [ ] Publish exact linked repair and independent recheck without claiming whole mode/worker acceptance.

## Read-only outbox inventory
- [x] Identify missing recovery enumeration and document bounded custody-only contract before code.
- [x] Implement existing strict inventory reuse without journal mutation or current permission.
- [x] Verify restart/multiple scopes/stale/withdrawn/mode departure and corrupt/foreign whole-read refusal with exact-byte preservation.
- [x] Publish paired source/Docs, inspect hosted checks and obtain bounded independent review; preserve broader unfinished gates.

## Accepted outbox inventory receipt

Buddy8fc5d6cc/Docsdfdf4317 accepted only additive inventory in independent reviews [5511621272](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5511621272) and [5511622231](https://github.com/s116821/ReMarkableBuddiesDocs/pull/7#pullrequestreview-5511622231), fully read. Exact aggregate hosted source38488792072 and Docs38488778757 completed SUCCESS. Reviewer inspected source/logs without execution. Hosted Rust1.99.0 full tests/formatting/strictClippy/ARMv7+AArch64 compilation differ from owner localRust1.98.1 ten affected tests. HostedDocs21strictitems/12Windows tests/19guidance+126preserved differ from local16/18counts. No transfer to liveDrive/native/worker/domain/restore/status or wholeparent lifecycle; existing change stays active.

## Disposable provider qualification resource contract
- [x] Prepare concrete account/application/operator/namespace/budget/evidence/cleanup decisions and primary API basis without live resources.
- [ ] Obtain coordinator review and explicitly owned disposable binding before executing the live-provider gate.
- [ ] Execute bounded actual adapter contention/acknowledgement/client visibility checks and retain failures; do not infer native/domain/production acceptance.
