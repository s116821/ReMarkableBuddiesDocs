# Acceptance and delivery checklist

Historical increment checkboxes are reconciled against their existing exact public
receipts and paired API delivery in [implementation status](implementation-status.md).
They are not new current-head test, provider, native or full-feature acceptance.
Unchecked compound requirements remain open where their end-to-end portion is
unproven; they do not reopen the individually accepted APIs below.

- [x] Read REM-52 and prerequisite/domain/Manager issue chronology; inspect REM-36 source and central contracts and active REM-37 record types.
- [x] Inspect provider documentation and maintained sync prior art; distinguish candidate mechanism from live-provider proof.
- [x] Propose modes, conditional publication, source-document projection, local fencing, media/restore/status contracts before implementation.
- [x] Obtain independent review at ebf8c72 accepting generic fixed-ID metadata create-or-read and transport fixtures only.
- [x] Obtain independent review accepting the admission/settlement/projector/application-matrix contract at 7e06d9; no implementation or live qualification follows from this acceptance.
- [x] Obtain Main's exact0830a9af owner review5442770097 and refreshed673c mapping; SCRAPPY owns storage, Main owns domain/journal/backend paths. Schema2 acceptance remains coordinated separately.
- [x] Obtain Main's efb8fd73 review accepting the coordinated proposal for an isolated selected-store/projector fixture slice; add history/bitmap admission coverage and propose the precise token/commit/activation/journal interfaces for owner agreement.
- [x] Complete the bounded interface/ownership agreement (`0830a9af` / accepted `7e06d9`) and disconnected opaque real-Store projection fixture in `a78d0ca`, preserved byte-exact in the independently accepted historical API delivery `0a258056` (blob `d37474a2`). See [provenance](implementation-status.md#source-and-review-provenance); no domain activation/admission or native authority was implemented by that fixture.
- [x] Read Main's exact0830a9af owner agreement (2026-10-07T13:09:56Z): SCRAPPY's selected storage implementation is unblocked; Main retains domain journal/projector/admission ownership.
- [x] Complete and review the bounded selected snapshot/guarded commit/atomic activation and original replay/fault-recovery increment. Historical API source `c8fe23c`, the [lineage receipt6072364455](https://github.com/s116821/ReMarkableBuddies/pull/31#issuecomment-6072364455), and the paired `0a258056` / `2f69e048` delivery establish this storage completion; full domain/worker acceptance remains open.
- [x] Implement and verify the bounded generic fixed-ID adapter slice without enabling shared-mode publication: original review `ebf8c72` and the historical API delivery recorded in [implementation status](implementation-status.md#source-and-review-provenance). This is local HTTP/source acceptance, not actual-provider qualification.
- [ ] Qualify or reject the candidate provider primitive using an explicitly authorized disposable app-data namespace; preserve reproducible evidence without secrets.
- [x] Implement the accepted generic scope/selection and conditional transport seam in historical API source `c8fe23c`, preserving domain-opaque storage/bounds; [the individually scoped receipts](implementation-status.md#source-and-review-provenance) and paired API delivery establish this increment only.
- [ ] Implement mode/binding isolation, bootstrap/catalog registration, outbox replay and first-winner replacement without stale auto-rebase.
- [ ] Integrate domain-owned aggregate projection and in-flight operation fence without duplicating REM-37/24/26/53 schemas or granting native authority.
- [ ] Implement versioned OS/file status, explicit portable configuration/media policy and validated selected-backup maintenance contract for REM-42.
- [ ] Verify two-client same-base winner, sequential A-to-B transfer, different-document/global preservation, clock skew, stale offline attempts, lost acknowledgement and interrupted publication.
- [ ] Verify clean/replacement tablet bootstrap, deletion/tombstones, corrupt/unknown-schema/interrupted restore, native page lag, active operation invalidation and intentional/incomplete media.
- [ ] Verify join/leave/switch/local-only and isolated backups cannot publish emptiness, merge namespaces, delete other backups or reuse device secrets.
- [ ] Run relevant Rust checks/simulator coverage and central Docs checks; distinguish host/provider/native evidence and remaining gates.
- [ ] Publish exact linked Docs/Rust revisions, inspect CI/bot feedback, obtain final independent review and coordinate merge order.
- [ ] Sync final as-built canonical contracts and archive completed scope only; retain unperformed provider/native qualification as explicit unresolved work rather than checking it off.

- [x] Independently review the bounded guarded commit/atomic activation increment, including history/replay/ancestor/fault/stale/media/unrelated-scope controls: the [lineage receipt6072364455](https://github.com/s116821/ReMarkableBuddies/pull/31#issuecomment-6072364455), [host qualification](qualification.md), and historical API delivery retain their exact-source attribution. No actual domain handoff or provider qualification follows.
- [ ] Implement portable selected backup/restore/migration policy before enabling these maintenance paths for selected stores; current explicit refusal prevents silent metadata loss.
- [x] Implement and locally verify the [portable selected archive/inspection candidate](portable-selected-maintenance.md), preserving original transaction/history/retained/media and unrelated data without minting portable live tokens; retain explicit restore/migration refusal until activation policy is implemented.
- [x] Independently review portable archive/inspection at source `423 -> 2ed` / Docs `7d -> 540`: [review5495568634](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5495568634). Exact paired publication/CI was subsequently reconciled by the bounded API delivery; broader restore remains separate.
- [x] Add and locally qualify read-only original-publication predecessor lookup for Main's historical selection-pin validation, without minting live tokens or changing current membership.
- [x] Independently review the bounded original predecessor lookup and its exact-source qualification, preserved in [receipt6072364455](https://github.com/s116821/ReMarkableBuddies/pull/31#issuecomment-6072364455) and historical API integration. This historical lookup grants no current token or native authority.

- [x] Implement the bounded selected snapshot/guarded commit/activation/replay candidate; checkpoint cca7ea9d passed hosted CI, with domain/native/provider integration still disabled.
- [x] Complete bounded retained-only publication and old-reader refusal review/qualification: [the accepted API provenance](implementation-status.md#source-and-review-provenance) and [unchanged-reader procedure/evidence](qualification.md#unchanged-older-reader) retain the original `7d1403c` format1 positive control / format2 refusal. This is historical generic storage proof, separate from format5 and actual domain settlement.
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
- [x] Reconcile historical DocsPR7 pointer and final successor CI in the bounded delivery: final Docs320122c -> actual main2f69e048, with source31/main0a258056 and actual-main checks recorded below; no broader sync gate is waived.

## Durable selected outbox preparation

- [x] Implement original-operation journal/replay, explicit local withdrawal and current-token/binding/object validation using existing Store/file/slot primitives.
- [x] Verify real Store restart/fault/replay/stale/binding/generation/media and unrelated-scope controls without network/native effects.
- [x] Publish and independently accept bounded outbox preparation via [staging-repair review5496789194](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5496789194), preserved in historical source `c8fe23c` and the paired API delivery. Mode/bootstrap/adjudication/worker/provider/domain/restore and full lifecycle retain their own gates.

## Accepted immutable increments

Independent archive read acceptance is review5495568634 at423->2ed/7d->540;
budget/lineage is5495556299 at2ed->311/540->c93; custody is5495938187 at311->488/c93->943.
These close their bounded independent-review portions only. At that historical
checkpoint DocsPR7 still advertisedc93 despite the correct owned943 branch. Its
linked-pointer/CI reconciliation was subsequently completed by the paired API
delivery recorded below; the full end-to-end parent lifecycle remains open.

## Outbox staging-residue recovery repair

- [x] Reproduce7e4 interruption residue before new intent and beside committed pending/withdrawn journal; reuse exact safe owned staging cleanup.
- [x] Verify preparation/withdrawal residue recovery, replay/current-token/descriptor/media preservation and unsupported foreign-entry refusal; deterministic residues are not actual process-kill evidence.
- [x] Publish and independently recheck the outbox staging-residue repair in [review5496789194](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5496789194); the original failed residue reproducer and historical API delivery remain the evidence. This closes the repair only.

## Explicit mode/binding control

- [x] Implement private mode actor/device/backup identities, current tokens, original-operation replay and mode leases with legacy worker exclusion.
- [x] Bind selected outbox to shared mode epoch and verify transition/restart/replay/lease/binding/leave-rejoin/refusal/unrelated data preservation through real Store fixtures.
- [x] Publish and independently accept the bounded mode API and repaired history through [review5496889027](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5496889027), historical source `a40503e` / `c8fe23c` and the paired API delivery. Actual worker/bootstrap/provider/domain/native qualification is separate.

## Read-only prepared-slot observation

- [x] Reuse exact provider metadata/descriptor validators for prepared GET-only observation and post-create observation.
- [x] Verify same/different pointer, account/app mismatch, absent/invalid/corrupt slot and no create/allocate/update/delete through host HTTP fixtures.
- [x] Publish and independently accept prepared-slot read-only observation in [review5496892636](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5496892636), preserved by the paired API delivery. Live provider/bootstrap/domain/native authority remains unqualified.

## Persisted mode identity repair

- [x] Reproduce persisted reused backup identity and same-binding identity discontinuity through actual Store reopening.
- [x] Enforce load-time continuity and first-use identity; verify snapshot/lease/replay refusal, valid restart/replay and root-only replacement outbox control.
- [x] Publish and independently accept persisted mode identity repair in [review5496889027](https://github.com/s116821/ReMarkableBuddies/pull/31#pullrequestreview-5496889027), preserved by the paired API delivery. This closes identity continuity only, not whole mode/worker acceptance.

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

## October 19 bounded delivery reconciliation

This parent change remains **active and unfinished**. The ten implemented API
requirements were synchronized verbatim into the canonical specification. The
nine end-to-end requirements remain in the active delta; no archive is manufactured
and no worker/provider/domain/status/restore or native task is waived. Historical
unchecked mixed-scope tasks above remain open wherever their broader integration
is unfinished. The exact accepted slices and pending candidate gates are recorded
in [bounded delivery status](implementation-status.md).

- [x] Reconcile existing source, repair, mode and fixture reviews without rerunning unchanged qualification.
- [x] Prepare actual-main integration preserving Conversation/schema2 and ExportAssociation/schema2 in both runtime validation and the offline contract.
- [x] Synchronize only the ten implemented and previously accepted API requirements; retain all nine unfinished end-to-end requirements as active.
- [x] Complete changed-candidate compatibility checks and exact-head hosted checks.
- [x] Obtain independent review of only the schema/contract resolution, main preservation and bounded lifecycle delta.
- [x] Coordinate the bounded API paired squash delivery and actual-main CI/publication: Buddy31 ->0a258056 / Docs7 ->2f69e048; source39359373842 and Docs39359368436 passed. This closes that historical delivery only; the end-to-end parent remains unfinished.
- [ ] Finish the remaining end-to-end requirements before final parent sync/archive.


## Bounded portable preference artifact

The separately owned finite [export-portable-configuration](../archive/2026-11-06-export-portable-configuration/proposal.md) exposes explicit private product/personalization/research preference export and offline inspection. It does not settle this parent's portable record-key policy, archive inclusion, import/application, model/memory preferences or actual synchronization. Parent tasks remain open.


## Selected publication/recovery and product winner adoption

- [x] Establish exact current source/spec bases, retained branch/worktree ownership and existing provider-binding contract; preserve other lanes.
- [x] Propose the connected worker/public producer/adoption footprint and concrete legacy-worker/local-genesis/notebook-format conflicts before code.
- [x] Obtain independent maintainer precode and domain-owner review of the r2 retention, portable/local genesis and selected notebook compatibility contract; accepted before implementation. Remaining domain coverage and implementation checks stay open below.
- [x] Route the existing Worker by actual mode/qualification before credentials and connect selected Writer/memory edits with Store wake in reviewed source `24c1bb6`; [the connected-core receipt](implementation-status.md#connected-core-source-increment) preserves actual two-Store/local HTTP evidence. Production qualification remains closed.
- [x] Implement agreed immutable root/catalog/base/slot and durable original staging/attempt recovery through existing transport/file/outbox primitives.
- [x] Enforce mode/current binding and actual domain-gated handoff; never hold Store mutex during network or rebase a stale losing candidate.
- [x] Validate supported memory, conversation, notebook and portable-preference winners and apply one atomic winner-plus-local-unresolved closure. Recover activation-before-withdraw from the original receipt.
- [x] Implement and verify the bounded receiving-local memory genesis/catalog bridge in reviewed source `24c1bb6`, including original activation-before-checkpoint recovery and exact fact bytes; [the existing receipt](implementation-status.md#connected-core-source-increment) retains its attribution. Optional-domain and full parent coverage remain separate.
- [x] Implement the reviewed selected notebook generation stage, exact Source3/NotebookPlan/NotebookStage validation and actual selected notebook producer within this same feature; preserve ordinary format4 routes and old-reader refusal.
- [ ] Define and implement required handwriting/portable-preference selected adapters with their domain owners; do not silently claim absent coverage or misuse another namespace.
- [x] Publish bounded truthful mode/committed/applied/pending/media status from actual original receipts and explicit failure states.
- [ ] Exercise the REAL producer/Worker/adopter with two Stores and actual HTTP adapter fixtures: same-base winner, independent scopes, catalog races, lost ack/restart/stale mode, active operation/settlement, notebook stages/media and abrupt activation recovery.
- [ ] Extend relevant maintained simulator scenarios; keep local protocol, actual-provider and native evidence distinct.
- [ ] Independently qualify the selected disposable provider/account/application/client binding under provider-qualification-contract.md before production publication; no live resource operation follows from source tests.
- [ ] Obtain exact final source/spec review and applicable checks, reconcile domain shared-file ownership and paired delivery, sync only as-built requirements and archive only completed named scope in the SAME implementation pair; do not merge precode alone or archive unfinished parent requirements.


## Shared-worker successor r2 concrete corrections

- [x] Reconcile protocol review db02c677 and independent domain review 2e03d6af into a preserved successor design; no Rust implementation claimed.
- [x] Add agreed-binding GET-only observation reusing exact pointer/descriptor checks, typed absence/invalid, and candidate comparison only for an actual prepared candidate; source4063d49, 11 fixed-slot HTTP tests passed.
- [x] Implement explicit CreateGroup control on existing mode dispatch/checkpoint: current ordinary admission for allocation only, persisted IDs/body, release/revalidate original token, exact conditional shared choice and current shared lease before create. Source `8c97cc2` verifies the bounded control with real local HTTP and CLI checks; production qualification remains closed and catalog registration/new-scope admission remain unfinished.
- [x] Recover never-submitted and uncertain original attempts by current admitted SAME-ID/bytes retry; stale selected attempts observe only, changed namespace admits no old network work.
- [x] Persist original passive receiving custody and reconcile exact Initialize/Activate receipts before checkpoint/health or outbound retirement in reviewed source `24c1bb6`; [existing local HTTP / restart evidence](implementation-status.md#connected-core-source-increment) does not imply full provider/domain qualification. Later catalog staging-boundary corrections retain their own evidence below.
- [x] Gate supported mixed conversation/memory, Reader, Writer and notebook paths on exact local registration and genesis. Publish receiving registration under the ordered catalog/scope gates and resume from the original activation receipt. Remaining optional domain gates stay with their adapter tasks.
- [x] Validate active winner and exact retained manifests separately; derive local uncertainty only from verified local Commit/predecessor lineage, preserve foreign history without effect authority, and block ambiguous lineage.
- [x] Keep own or competing winners containing an exact unresolved local receipt committed-not-applied; test exclusive-retention settlement separately without promising active-intent release.
- [x] Apply notebook semantic closure checks at live selected writer/adopter and recovery, fence actual model handoff/result commit, and recover stale capabilities only through exact original preparation under existing-only custody.
- [ ] Run real Worker/two-Store branches for pull-only join/update, absent/invalid slots, first-root allocation/mode/root crashes, before-create restart, stale edit after preparation, passive activation-before-checkpoint, readiness windows, sibling retained/foreign receipts and overlap settlement.

The bounded CreateGroup-to-first-fact regression is published in Buddy [`2be79fa`](https://github.com/s116821/ReMarkableBuddies/commit/2be79fa670cb22ebf94bf84499ec57db86dff030). It composes original control interruption/reopen, dynamic root/catalog creation, an actual selected-memory edit, Worker publication and passive adoption by a distinct Store without preseeded provider slots. Source review is complete, and the [hosted Checks job](https://github.com/s116821/ReMarkableBuddies/actions/runs/43570302977/job/132373055527) passed strict compilation/lint and this named regression; application build/integration remain pending. Both original Workers stop and join before the next phase or final assertions, and the receiving query contains the exact fact/revision. This finite composition case supplements the accepted standalone control, Worker and domain tests; it establishes no live-provider or tablet behavior.

- [ ] At later separately scoped provider selection, prefer suitable existing explicitly authorized OAuth/account with isolated disposable app-data resources and exact cleanup; reconcile the proposed contract before any execution.
- [x] Obtain successor acceptance before implementation; r2 accepted before source work. Final implementation/checks/spec sync/completed-scope archive remain required in the same paired delivery, not a planning-only PR.


## Initial reviewed-contract implementation progress

- [x] Enforce exact receiver-local catalog/genesis readiness across mixed current admission, selected Writer prepare/finish and selected Reader write; absent/corrupt receiving checkpoint grants no readiness.
- [x] Extend the actual mixed product regression with unregistered/checkpoint-corrupt refusal and exact-registration success; source61ed900 passed111 selected regressions with1 existing ignored test. These results do not cover the unimplemented connected worker or notebook stage.
- [x] Reconcile the provider resource proposal to permit a suitable existing explicitly authorized account/application with isolated disposable resources and exact cleanup, without authorizing execution.
- [ ] Complete the connected worker, original controls/receiving, domain retention/uncertainty, notebook format5/producer and their meaningful checks before final lifecycle/delivery.


## Accepted portable preference and confirmed handwriting integration

- [x] Record the reviewed portable/handwriting domain contracts in the active central change before real core/consumer integration; preserve delivered ordinary/import/Manager behavior.
- [x] Adopt the independently reviewed portable Artifact/LocalConfigSnapshot adapter through integrated parent458a4cd; this is not the completed selected producer/adopter/consumer route.
- [x] Add format5 portable namespace/typed owner, strict original-byte closure validation, explicit Inspect/Edit/Status selector, original receipt/no-op behavior and real Worker/second-Store adoption; bounded command/correction and real producer transfer are recorded at `b90b2a5` / `143eb62` / `23f7a70`. Production qualification and actual consumer/Manager gates stay open.
- [x] Capture admitted raw+typed local configuration together and integrate the selected Writer effective overlay, selected or established-absence pin, role/prompt gates and ordered handoff/result checks; preserve original recovery and excluded local values. Source `c249fa9` / Docs `a1af6c47` received independent review, publication and full exact-revision hosted CI; see implementation status.
- [ ] Finish composed notebook consumer qualification under the same configuration/role/prompt rules. Its original publication-lifetime correction is independently reviewed as `893c6912`; the dedicated notebook custody tasks below track the pending composed CI rather than reopening the accepted Writer increment.
- [x] Integrate the disjoint Handwriting1 raw-byte validator/projection/typed preparation adapter through reviewed parent82e11f2; keep ordinary leases and null-original refusal unchanged. Actual selected command/consumer integration remains open below.
- [x] Route handwriting through the existing format5 Store-atomic local operation check with bounded accepted transaction evidence. Exercise historical replay, concurrent competing correction scopes, and separation of imported envelopes from local receipts at `fd92de7`.
- [x] Connect the confirmed command, correction catalog/genesis, exact sample/tombstone/rollback, fixed-slot winner and passive receipt. Exercise retained alternatives, omitted or missing samples and two real format5 Stores at `fd92de7`.
- [ ] Verify remaining cross-profile and cross-producer collision cases in the combined delivery, including the separately owned inherited-base operation guard.
- [x] Route profile-wide Query through the verified selected catalog and exercise completeness, omission and response bounds across multiple correction scopes at `256e2d6`.
- [ ] Reconcile compatible existing Reader/Writer receiving interfaces and actual recognition ingress before claiming shared example consumption; Buddy105 remains an explicit separately owned source dependency, not fulfilled by data transfer or archived normalized notebook stages.
- [x] Complete the automatic selected Reader recognition path through actual submission and result publication, including metadata-first ranking, target exclusion and stale context refusal in the real Store fixture.
- [x] Connect the typed selected Writer image receiver to the existing guarded normalizer and selected Writer preparation. Preserve exact source/turn/media custody, separate single-use model stages, one deadline and read allowance, and original-only recovery.
- [x] Exercise the actual selected Writer image receiver with a real Store and scripted owned engine. Prove exact examples and target exclusion, complete-empty and partial-empty behavior, stale source/preference/correction refusal at submission and publication, and no duplicate normalization after historical or unacknowledged preparation.
- [ ] Exercise exact selected examples/coverage, target exclusion, bounded ranking/request budgets, stale handoff/result fencing and truthful unavailable/incomplete versus complete-empty behavior through the actual compatible receiving paths.
- [ ] Keep shared Manager effective-preference view/edit, ordinary promotion policy, broader schemas, isolated backup, live provider, model fidelity/native/device and full-parent qualification open unless independently delivered.

## Shared-preference Manager and backend command integration

- [ ] Integrate the Manager-owned [accepted detailed contract](shared-preferences-manager.md), guarded panel/controller and common browser/Electron host paths in the same coordinated Buddy/Docs/Manager delivery; preserve existing saved-file import/export.
- [ ] Implement the real versioned one-shot shared-preference Inspect/Edit/Status command with strict bounded duplicate-free input/output, explicit private text disclosure, effective field origins and exact local configuration identity in its original guard.
- [ ] Prove original-only Status correspondence from operation/guard/patch digest and exact existing transaction/result custody; retain unknown possible-dispatch outcomes without private patch retention, Edit replay, rebase or a second operation index.
- [ ] Exercise identical real guarded browser/Electron paths against the actual Buddy command for unsupported older Buddy, local/shared routing, established absence, selected readiness, sparse/null edits, no-change, stale pins, busy resident Store, post-dispatch unknown and original Status.
- [ ] Verify opaque-reference expiry/replacement/navigation/mode/connection/boot/deadline/cancellation behavior and bounded private frames, preserving unresolved originals and requiring fresh inspection plus deliberate confirmation after conflict; no automatic service Stop, saved-file fallback or provider access.
- [ ] Keep Edit unavailable until successful authoritative selected Inspect and exact backend correspondence; distinguish local pending/upstream applied/replaced state, effective inspection snapshot and unverified running activation.

## Connected core verified increment

- [x] Publish reviewed source24c1bb6 in the existing implementation draft: reuse the existing Worker loop, original attempt/receive custody, selected commit wake, domain byte validation and receiving-local registration; keep production qualification closed.
- [x] Exercise actual selected memory mutation and selected Writer model-entry/finish through the real local HTTP adapter and second Store, including first join/update, batch_items=1, Worker restart, lost create acknowledgement and activation-before-checkpoint original recovery; use a deterministic local engine and an already-created modeled root/catalog.
- [x] Preserve the exact-bound download failure, implement the bounded EOF probe without accepting oversized data, and verify exact/oversized/zero-bound behavior; pass163 storage regressions, strict all-target/all-feature Clippy and formatter checks with tested files unchanged by commit.
- [ ] Complete actual CreateGroup/catalog registration, broader uncertainty/retention, selected Source3/format5 producer, optional-domain consumers/CLI and applicable live/hosted qualification before final parent delivery; the connected fixture increment does not close those gates.

## Compound storage verified increment

- [x] Preserve the ordinary ready/incomplete notebook guarantee and correct the deterministic duplicated-preflight-descriptor busy race; keep actual Store reacquisition and new-owner exclusion assertions.
- [x] Implement original actor/source/target/operation/group/binding/mode-bound existing-only format5 staging, static contract/feature hashes, verified byte copying, one CURRENT switch and exact original capability reconciliation; refuse live selected-source re-rooting and missing published markers.
- [x] Verify controlled preparation interruptions and four actual subprocess deaths, real ordinary notebook Source3/plan/stage/media preservation, foreign-actor closure/local metadata and format5 Worker recovery; enforce Store-atomic operation reuse across real selected memory producers with exact replay.
- [x] Execute the separate trusted older-host-executable read-only compatibility gate, retain its format4 positive control and unchanged format5 metadata refusal, and pass175 storage plus17 Reader CLI cases, strict Clippy and formatting; keep default ignored witnesses and actual invocation evidence distinct.
- [ ] Complete the actual selected Source3 notebook producer/runner, group/catalog/new-scope controls and remaining domain/CLI/consumer/qualification obligations before syncing or archiving the unfinished parent.

## Additive catalog verified increment

- [x] Discover explicitly registered local memory/document scopes from exact current domain registration/genesis, retain original allocation/proposal in the existing checkpoint, and extend only the verified accepted catalog set under current mode and ordered gates; source `e1c170f`, independent review/hosted publication pending.
- [x] Preserve actual document-only ownership, losing explicit fact custody through reopen and original staging/outbox recovery; reproduce the preparation-write window and persist conservative intent before that write, with actual durable-write fault/reopen controls for present versus missing journals.
- [x] Verify all 8 catalog HTTP cases within 191 storage tests / 2 existing ignored gates, plus 74 conversation tests, strict Clippy, formatting and unchanged committed input hashes; keep the earlier pre-intent correction run and initial failures separate.
- [x] Reconcile thirteen obsolete historical increment tasks and three already reviewed connected-core implementation tasks against existing exact-source public receipts and paired delivery, without reopening qualification or closing broad parent work.
- [ ] Establish fresh provider-qualified first-scope product admission, preference/handwriting registrations and actual commands/consumers; complete selected notebook, uncertainty and final provider/native/delivery gates in this same active parent.

## Portable record verified increment

- [x] Add format5-only portable namespace/contract and legacy-family publication refusal, exact raw V1 record/chain projection, group-stable key/UUID and original-condition-bound pure preparation; source `8a50104`, accepted with the independently reviewed `76095e7` correction and published in the existing implementation draft.
- [x] Verify declaration-based no-op versus null/empty/omitted fallback, duplicate raw JSON, foreign/conflicted history, real selected Store reopen and all four legacy-family refusal controls; pass 25 portable configuration and 195 storage cases with their stated non-additive attribution.
- [x] Execute the unmodified older format5 reader's old-contract positive control / new-contract nonmutating refusal; retain its exact source/binary/schema provenance and three default-ignored gate attribution. Pass strict Clippy, formatting and unchanged final input hashes after the test-only borrow cleanup.
- [ ] Complete fresh first-scope/current-selected admission, portable Worker registration/publication/adoption, original Status and effective product/Manager command integration; pure record helpers grant no live permit.

## Portable raw-parent correction

- [x] Preserve a valid single-parent positive and correctly rehashed original `[P, P]` failure through both projection and actual Store admission; share one raw portable check before typed set normalization, source `76095e7`.
- [x] Pass 26 portable configuration / 195 storage cases with 3 explicit default ignored gates, strict Clippy/formatting and unchanged three-file correction hashes; preserve independent Worker drafts outside the correction and keep prior old-reader evidence at its original source.
- [x] Obtain the requested independent narrow re-review and coordinator publication at source `76095e7` / Docs `81667ed`; this correction changes no contract fingerprint or live admission rule.

## Portable Worker integration

- [x] Extend the existing additive catalog and selected publication/receiving route to the typed portable preference owner, preserving original genesis/proposal/receive custody and exact raw record bytes; do not create another Worker or silently seed an empty declaration.
- [x] Exercise explicit local edits and passive second-Store receiving, competing first declarations with losing-history retention, original activation-before-checkpoint recovery, and foreign-custody refusal at a known empty mapping through the actual Worker/local HTTP fixture.
- [x] Verify source `993236a` with 195 default-feature storage cases / 3 existing ignored gates, including all four Worker cases; pass strict all-target/all-feature Clippy, formatting and unchanged seven-file input hashes.
- [x] Obtain independent source review and coordinated publication of Worker `993236a` / Docs `01add2e`; hosted successor CI stays with the coordinator and is not implied by publication.
- [ ] Implement fresh qualified absence/current-selected Inspect/Edit admission, original-only Status and effective product/Manager consumers; the pure helper, local fixture producer and Worker registration do not supply these permits.

## Shared preference one-shot command increment

- [x] Implement strict fixed stdin Inspect/Edit/Status dispatch with existing-only Store custody, bounded private views and sealed production qualification before credentials.
- [x] Re-admit exact current mode/group/key/binding/epoch/generation/raw Config plus selected token or fresh qualified root/catalog absence under ordered gates; preserve established selected offline use and keep all provider publication/adoption in the existing Worker.
- [x] Prove historical local Initialize/Commit receipt, original predecessor and guard/patch/result-bound revision for Status without current mode/configuration admission, patch retention, a second index or Edit replay.
- [x] Validate unchanged source `b90b2a5`: 209 all-feature storage cases /3 existing ignored, including ten command cases; 26 portable configuration cases; 13 binary argument tests and 3 actual CLI cases; strict Clippy/formatting and nine frozen input hashes. Preserve earlier failures/pre-refinement evidence separately.
- [x] Obtain coordinator independent source/profile review of the bounded command and constructor correction; no full parent closure follows.
- [x] Complete coordinated publication of the bounded command/correction/test batch with green Buddy `23f7a70` / Docs `6f0ced3` / Manager `457d2278` hosted checks; these results exclude the effective consumer increment.
- [ ] Close the actual Buddy/Manager editable-command parity gate with the domain owner; source HTTP adapter cases and synthetic executable Status custody do not imply positive executable Inspect/Edit or live qualification.
- [ ] Complete effective Reader/Writer/memory preference consumers under the same ordered admission at actual handoff and result commit, alongside remaining handwriting/notebook/native/provider parent gates.

## Constructor checkpoint allowance correction

- [x] Reproduce the uncharged constructor checkpoint reread with a boundary that actually reaches four provider GETs on the uncorrected implementation before exhaustion.
- [x] Reserve that second bounded checkpoint read in the same original request allowance before credential opening in source `143eb62`; pass all eleven command cases, strict lint/formatting and unchanged two-file hashes, with the same boundary making no additional provider request.
- [x] Obtain the requested independent narrow review of the constructor correction; retain prior broad/executable evidence at its original source.
- [x] Complete coordinator publication of that accepted correction in the green `23f7a70` bounded batch.

## Actual producer to Worker transfer regression

- [x] Connect actual admitted first Edit to Worker publication, second-Store Joining/receive, offline reverse Edit and transfer back with exact membership, no passive POST and local-versus-imported original receipt proof, source `23f7a70`.
- [x] Pass all twelve command cases including the independent constructor boundary, strict lint/formatting and the unchanged single test-file hash; keep the two different earlier eleven-case runs separately attributed.
- [x] Obtain independent review and coordinator batched publication of this test-only increment, with successful hosted checks at Buddy `23f7a70`, Docs `6f0ced3` and Manager `457d2278`; effective consumer implementation is excluded from that finite batch.

## Effective selected Writer consumer increment

- [x] Factor current preference admission into a private typed request snapshot using exact raw Config and selected/qualified-absence pins; serialized guards and optional settings cannot create it.
- [x] Join Writer, preferences and optional selected memory at the existing owned model submission and result transaction, without nested gate acquisition or holding domain gates across the long model response wait.
- [x] Connect the actual selected Writer command before new-work policy/credentials while preserving original-only recovery and all local settings outside the portable allowlist.
- [x] Verify changed pins, disabled policy, delayed/lost/canceled model submission, original recovery and result refusal through the real adapters; report modeled versus live evidence and keep broader consumers/native/provider gates open.
- [x] Obtain coordinator independent final source review, coordinated publication and hosted checks for the Writer consumer increment. [Review](https://linear.app/magentumdragon/issue/REM-52#comment-1b3c1f43-c5d3-4c26-8013-f45dd6c90073) and [terminal CI](https://linear.app/magentumdragon/issue/REM-52#comment-6a62407f-12f2-43bf-afa7-3a83e57056d9).

## Installed resident Reader input

- [x] Independently review the [selected Reader precode](selected-reader-resident-input.md) and reconcile the final Writer submission API.
- [x] Verify received pure and mixed document custody, selected Prepared capture and receipt, and original-only recovery with local Store and Worker fixtures.
- [x] Exercise all three guarded Reader model stages through Generated using identical captured bytes, effective preference invalidation and joined selected memory in the local fixture.
- [ ] Verify the installed input-only constructor, effective admission at startup and each genuine release, repeat and interruption behavior, and ordinary LocalOnly behavior on the qualified runtime.
- [ ] Independently review the paired source and contract, reconcile current hosted evidence and complete the later Main-owned installed Reader qualification.

## Ordinary data snapshots for isolated backup

- [x] Reuse the format-1 archive collector, validation and writer under a same-Store current isolated lease. Skip empty history and publish the marker only after verified objects.
- [x] Round-trip committed history and exact screenshot bytes through the existing inspector and ordinary restore to a distinct actor. Local Windows fixtures at Buddy `9f5bfe0` cover media omission, missing/corrupt promised media, wrong-mode/Store/stale leases, empty input, owned-root overlap and exclusion of private configuration and credentials.
- [x] Obtain independent paired review and coordinator publication of the snapshot increment at Buddy `9f5bfe0`. Keep portable configuration inclusion, cloud binding/publication, Manager download and replacement restore open.

## Portable preferences in ordinary isolated backups

- [x] Review the [package composition and import policy](isolated-portable-configuration.md), including the exact artifact capture, marker schema and empty-history behavior, before editing runtime code.
- [x] Prepare and inspect a package from the same locked ordinary format-1 history and one exact saved declaration capture. Buddy `54fc5a2` Windows fixtures verify byte identity, exclusions, no-work, strict membership/version/hash/validation refusal, before-marker interruption, and original-marker observation after publication.
- [x] Exercise the verified components through existing ordinary data restore and independently confirmed portable import on a distinct destination actor. Buddy `54fc5a2` Windows fixtures verify stale/swap refusal, untouched destination-only declarations, and separate outcome reporting.
- [x] Independently reviewed the bounded `54fc5a2` package increment as composed in Buddy `95b7544`, with paired Docs `1606f475`; no findings. The exact Buddy [Linux Checks](https://github.com/s116821/ReMarkableBuddies/actions/runs/43558125345/job/132335556112) pass all four package tests, including the Unix-only lost rename-acknowledgment fault, original-marker recovery and replay refusal. Full source CI and paired Docs CI pass. Installed/provider/device and Manager transfer qualification remain separate.
- [ ] Keep additional archive generations, provider publication and the Manager replacement workflow open pending their own acceptance.

## Ordinary isolated backup publication

- [x] Review the [publisher proposal](isolated-backup-publication.md), namespace verification, original-attempt state, and ordinary runtime ownership.
- [x] Exercise the verified package through the existing Worker scheduler and Drive adapter with an injected, qualified fixture binding. Buddy `41dbeb4` Windows fixtures verify marker-last upload, exact package reconstruction, bounded exact-ID recovery, verified media coverage, a saved Config change during capture, and pending work after the frozen revision settles.
- [x] Admit ordinary format-1 startup to its isolated publisher gate without relying on legacy sync or selected-group admission. Buddy `41dbeb4` verifies offline startup and local-memory Dispatch with an absent Drive credential. Production publication requires supported root provisioning.
- [ ] Verify root/bootstrap and live provider eligibility independently. Keep remote retention, additional generations, and Manager download and explicit restore open.

## Ordinary isolated root provisioning

- [x] Review the [provisioning proposal](isolated-root-provisioning.md), public host command and Manager boundary, private reservation and checkpoint, epoch behavior, and Worker constructor.
- [x] Connect the versioned host control to an existing format-1 Store and trusted provider adapter. Buddy `00e45e6` localhost cases verify generated-ID persistence, exact readback, stale observation and a lost creation acknowledgment.
- [x] Verify current-epoch Worker admission through the existing scheduler, missing/corrupt custody refusal, unchanged inspect wire and a new root on leave/re-entry. Buddy `00e45e6` covers current/historical/unqualified mode reports and retains the format-1 offline runtime admission.
- [x] Recognize the fixed private isolated checkpoint layout in both offline storage inventory scanners. Buddy `ca5172b` includes the Linux successor and symlink fixtures for hosted execution.
- [x] Preserve ordinary local operation when an isolated checkpoint, lock, staging or session path is blocked. Verify the valid last marker stays visible in redacted recovery health.
- [x] Confirm the Linux-only successor inventory and no-follow fixtures in hosted CI for the composed source. Buddy `9d68e5c` passed full run `43526582411`; its host log records all three isolated inventory/layout/no-follow cases passing. Later Writer changes do not modify these scanner files; final composed CI remains separate.
- [ ] Qualify the installed application and protected grant separately against an authorized provider, with independently scoped execution and evidence. Keep production disabled until that qualification exists.

## Manager isolated backup preparation

- [x] Implement the host-private input and result validator against the accepted provisioning contract, preserving original identity, errors and historical currency. Focused fixtures include hashed original command-harness bytes plus synthetic adversarial cases; neither is provider or tablet qualification.
- [x] Reconcile original producer-emitted current, historical and unqualified frames without reserialization.
- [x] Independently review the [consumer contract](manager-isolated-backup-provisioning.md) and private validator. Manager `fdf8a8f` corrects typed-outcome, token/epoch continuity and redacted-parse-error findings; 13 focused tests include original Buddy frames.
- [x] Extend the existing fixed wired mode transport with provisioning-only deadlines, original-byte forwarding, identity/framing checks and cancellation. Independent review and 12 Python/3 Node child tests pass; no live command was run.
- [x] Connect the privileged host service with original request retention, bounded ownership and explicit original-only recovery. Manager `cef7f50` has independently reviewed service/storage and browser/Electron bridge source; 38 private, child, service and loopback tests pass. Actual shared UI and platform storage qualification remain separate.
- [x] Connect and independently review the shared browser/Electron review, prepare and original-recovery UI. Manager `eb0cc55` passes all 47 focused private/child/service/loopback/controller tests, scoped lint and TypeScript checks; completed backup and runtime health remain separate observations.
- [x] Manager `61f1887` passed the isolated-root provisioning UI fixture against development and production browser assets and source and packaged Electron on Windows and Linux, using synthetic replies. Windows also passed the actual broad NTFS grant refusal and isolated-writer lock release controls. The [Linux](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752711) and [Windows](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752749) jobs qualify these host fixtures, not live provider or wired execution.
- [ ] Complete coordinated source/Docs checks and separately scoped provider/wired qualification before release.

## Selected notebook publication custody

- [x] Review the existing producer's publication boundary and the bounded [correction](shared-worker-integration.md#notebook-publication-custody-correction). Reuse the accepted Source3/plan/stage producer and existing guarded commit API rather than reopening its completed implementation.
- [x] Retain a failing actual-producer regression after successful phase prechecks, then pass original phase reads and pure cancellation/cutoff checks through begin, prepare, result and final-draft commits. Independently reviewed source `549f05fb`, integrated as `893c6912`, retains both observed pre-fix failures and passes 9 actual notebook cases, 5 underlying guarded-Store checks and strict Clippy in the existing Linux cache.
- [x] Review exact source for late marker refusal, original read exhaustion, healthy multi-Map/Reduce within unchanged reservations, original-only recovery, memory/winner interlocks and lost acknowledgments. The callback runs inside the publication mutex; no forced contended wait or real elapsed timeout was tested.
- [x] Verify the composed source in hosted CI and publish this increment with the existing coordinated change. Published `958cacf2` contains the reviewed phase fence and passed full hosted CI `43544477417`; the separate predecessor-fixture failure and correction evidence remain preserved. This does not close native or wider feature acceptance.

## Manager disconnected isolated backup inspection

- [x] Reconcile the existing authentication, isolated V1 publisher and ordinary restore contracts; record the bounded [reader design](manager-isolated-backup-reader.md) before implementation.
- [x] Implement and independently review the private read-only reader and focused source/fixture checks. Both author and coordinator ran all 11 cases successfully; the fixtures are source-derived synthetic JSON, not retained Rust producer bytes or cross-language qualification.
- [x] Connect and independently review the existing protected auth read boundary and private asynchronous host. Manager `67045d0` preserves original protected digests, generation, expiry and operation references; 28 focused auth/host/reader cases pass, with the existing Linux-only permissions case skipped on Windows.
- [x] Implement and independently review the unbound six-method Drive read transport. Fixed GET routes/projections preserve original raw bytes and bounded object streaming; no redirect, retry, refresh or production factory activation. All 54 author transport/reader/coordinator/host cases pass; the coordinator independently reran all 11 new loopback transport cases, including request-close/abort and zero-byte controls.
- [x] Independently review the shared inspection/selection UI. Manager `f9b4bd7` passes seven coordinator controller tests, scoped lint and TypeScript no-emit; its source-derived fixture explicitly avoids tablet observation and checks its owned profile before cleanup.
- [x] Finish independent browser/Electron bridge review. SCRAPPY identified two lifecycle gaps in `c900c05`; correction `a4dc16e` binds incomplete HTTP bodies to the original document and invalidates Electron backup state on trusted main-document navigation. Root retained the failing full-helper regression, then passed all 16 focused checks; SCRAPPY independently accepted both corrections.
- [x] At Manager `61f1887`, both hosted Integration jobs passed disconnected inspection and selection in the source browser helper and Electron, and in the retained packaged Electron and browser-helper modes, using synthetic provider frames. Coverage includes Electron reload during a pending read and after selection. The [Linux](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752711) and [Windows](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752749) results leave provider/wired qualification and later reader/restore-owner quit changes separate.
- [ ] Complete qualified namespace visibility, selected package download/validation and guarded existing/clean/replacement target restore before claiming the full Manager backup workflow.

## Selected isolated backup download and existing oracle

- [x] Trace the existing marker, producer inventory, complete package oracle and ordinary restore/preferences seams; record the [bounded download contract](manager-isolated-backup-download.md) before implementation.
- [x] Expose the existing full package oracle through the narrow offline archive command and test actual exported producer bytes, corruption, extra membership and wrong-marker refusal without Store/network/runtime activity. The normal CLI additionally verifies stdin/file framing using real ordinary/portable exports with a fixture-assembled outer marker; it does not replace actual isolated-producer evidence or establish shipped host-verifier qualification.
- [x] Implemented the private selected-download coordinator with original selection and grant checks, bounded streams, private staging and a trusted verifier seam. The reviewed `826be13` composition and Manager `61f1887` [hosted Checks](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971) cover exact EOF, size and digest, stale authority, and checked retirement. The actual protected read binding and production enablement remain open below.
- [ ] Independently review and compose the actual protected read binding, staging and qualified verifier runner before enabling download in the shared UI; unavailable infrastructure must remain truthful.
- [x] Share one private backup composition between Electron and the packaged browser helper, preserving the original selection and joining inspection predecessors, protected guard opens/closes and download work before shutdown completes. Reviewed Manager `826be13` passes 30 focused composition/host/helper checks independently; the author's broader focused suite has 77 passes and one Windows-inapplicable permission case skipped. Production read factories remain unbound; the selected action source is tracked below.
- [x] Add the explicit selected Download and verify action, preserving original ownership, expiry and private staging through cancellation, navigation and late replies. The closed verified summary distinguishes omitted media from interruption; lost cancellation replies retain cleanup uncertainty only in the current view. Root independently passes 51 focused controller/composition/host/helper checks; the author's broader focused suite passes 78 plus TypeScript and scoped lint. Both hosts recheck caller/document authority after awaiting results. Production registration and installed/provider qualification remain open.
- [x] Connect one private verified-source handoff to the existing ordinary restore Prepare/Confirm/Status owner, preserving original digest, target and destination custody and joining cancelled work before stage retirement. Root independently passes 50 focused ordinary restore/composition/download checks; the author reports 80 focused passes and scoped lint. The destination stager is synthetic; production transfer, provider registration, preference preview and clean/replacement bootstrap remain separate.
- [x] Join the private restore owner's destination retirement in both existing host shutdown paths and carry its reduced cleanup uncertainty through the existing trusted close result and shutdown logs. Preserve the manual restore protocol and original uncertain Apply reconciliation. The author's 46 focused helper/composition/ordinary-restore tests pass; Root independently passes the same suites and scoped syntax/lint checks. Both restore owners, backup and active quarantine are held in source fixtures, including synchronous and asynchronous failure.
- [ ] Execute the retained packaged Electron and browser-helper quit fixtures against the current shipped bytes. The fixtures hold both original restore owners across repeated quit and then verify exit after retirement; source preparation alone does not qualify either host or activate the public cloud-to-restore consumer.
- [x] Expose bounded reads of the exact verified source inventory through the existing staging broker, preserving sealed file custody, original length/digest, deadline and joined cancellation. Root passes 38 composition/download cases and eight Windows staging cases, with three Linux-only skips; the author reports the same 46-pass aggregate and scoped lint. Independent review's refused/non-true close-acknowledgement finding is corrected and re-reviewed: only exact success confirms closure; otherwise the original broker is stopped and joined before reader ownership clears, with cleanup uncertainty retained. The fault fixtures reproduce the original failure and hold child exit to verify the fix. No new destination adapter, target-runtime dependency or production registration is introduced.
- [ ] Complete current-source Linux broker execution and retained Windows/Linux packaged checks for the reader. Remote completion and checked destination release remain separate; local source reading does not establish a wired uploader or target runtime.
- [x] Build and qualify the source-pinned normal host oracle on Windows/Linux, preserve its identity/hash/notices and package mode, and exercise retained Electron and browser-helper paths without a new Buddy release asset or runtime installer. Manager `61f1887` [full shipping-input CI](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971) passes Build and both native Integration jobs, including the Linux ZIP execute-mode correction from `61ff362`. Current reader/shutdown changes retain their separate checks above.
- [x] Close Windows original-resource custody with the narrow lock-only helper and actual loader/reparse/write/rename/cancel/timeout qualification. The guard from `5c40643` passes all three native Windows control groups in the [shipping-input Windows job](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752749). Product factory registration and installed/tablet evidence remain separate.
- [x] Correct Windows staging creation without weakening protected-storage admission. Independently reviewed Manager `35ae38f` supplies the existing explicit owner/protected DACL to directory creation and preserves original/cleanup failures separately. Four focused Python and two local Node checks passed; five platform-dependent Node cases were skipped in that original local run. Hosted `1c97d5f` failed staging before verifier execution; later shipping-input `61f1887` passes the Windows staging and retained-verifier controls. The original failure remains distinct.
- [x] Retain source-attributed synthetic actual-isolated-producer fixtures without manually assembled markers. Buddy author `efb05505` is published unchanged as `f4f1b9a`, with the same source tree; Manager `b072223` retains the two original package closures and unaltered reproduction/byte receipt.
- [x] Exercise the real retained oracle through Manager's verifier on both platforms. Original Manager `1c97d5f` [Linux job](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43550507976/job/132313086563) passed 14 archive tests and actual-producer controls. The later Windows run's 11 passes/one negative-path fixture failure remains historical evidence; Buddy `95b7544` fixes that fixture without relaxing the selector. Shipping-input Manager `61f1887` [Linux](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752711) and [Windows](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/43560801971/job/132353752749) now pass the precompiled native command, actual-producer verifier and original packaged-byte preservation checks; Windows reports 12 archive tests passed. These results do not establish current reader/shutdown composition or installed/tablet qualification.
- [x] Extend the existing bounded ZIP observer for embedded oracles, preserving pre-1.0 legacy downloads and accepting valid future dependency pins while enforcing trusted exact candidate inputs. Independently reviewed Manager `4c2643d` preserves the response, asset inventory and quarantine-only authority; its follow-up coverage appears below.
- [x] Bind original notice inventory and bytes through that same bounded reader and assembly readback. Reviewed Manager `9adc72b` preserves the ordinary runtime response. All 56 Python 3.12 observer fixtures and six altered/missing/extra notice cases passed locally; shipping-input `61f1887` also passes actual packaged-byte verification on both hosts.
- [x] Identify and independently verify the original SDK 10.0.10240 / setup 10.0.26624 license and third-party notice carrier for the separately selected Universal CRT. Add both distinct, hash-bound raw RTFs to the existing vendor notice mechanism; retain the publisher's static-library redistribution reference separately. Historical notice attribution and `61f1887` packaged-byte verification are accepted independently of legal or installed/tablet conclusions.
- [x] Move final host dependency compilation to the existing Build job with maintained cross-build tooling, complete matching notices and retained native test inputs; verify the original packaged bytes in both Integration jobs without adding jobs, assets or repeated common checks. Full shipping-input CI `43560801971` at `61f1887` passes; the PR run correctly skips Release.
- [x] Qualify the retained package UI/session/lifecycle path for the explicit browser-helper launch mode at shipping-input `61f1887`. Both Integration jobs pass the actual packaged Electron/Chromium and browser-helper fixtures; the original source increment was `a488de7`. Later restore-owner quit and source-reader changes remain open above, and installed verifier composition remains disabled pending its own qualification.
- [ ] Complete exact wired handoff, existing explicit restore/preferences flows, clean/replacement admission and provider/platform qualification before full workflow delivery.
