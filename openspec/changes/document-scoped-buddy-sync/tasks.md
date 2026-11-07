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
- [ ] Implement agreed immutable root/catalog/base/slot and durable original staging/attempt recovery through existing transport/file/outbox primitives.
- [ ] Enforce mode/current binding and actual domain-gated handoff; never hold Store mutex during network or rebase a stale losing candidate.
- [ ] Validate complete domain/media winner and apply one atomic winner-plus-local-unresolved closure; recover activation-before-withdraw without resend.
- [x] Implement and verify the bounded receiving-local memory genesis/catalog bridge in reviewed source `24c1bb6`, including original activation-before-checkpoint recovery and exact fact bytes; [the existing receipt](implementation-status.md#connected-core-source-increment) retains its attribution. Optional-domain and full parent coverage remain separate.
- [ ] Implement the reviewed selected notebook generation stage, exact Source3/NotebookPlan/NotebookStage validation and actual selected notebook producer within this same feature; preserve ordinary format4 routes and old-reader refusal.
- [ ] Define and implement required handwriting/portable-preference selected adapters with their domain owners; do not silently claim absent coverage or misuse another namespace.
- [ ] Publish bounded truthful mode/committed/applied/pending/media status from actual original receipts and explicit failure states.
- [ ] Exercise the REAL producer/Worker/adopter with two Stores and actual HTTP adapter fixtures: same-base winner, independent scopes, catalog races, lost ack/restart/stale mode, active operation/settlement, notebook stages/media and abrupt activation recovery.
- [ ] Extend relevant maintained simulator scenarios; keep local protocol, actual-provider and native evidence distinct.
- [ ] Independently qualify the selected disposable provider/account/application/client binding under provider-qualification-contract.md before production publication; no live resource operation follows from source tests.
- [ ] Obtain exact final source/spec review and applicable checks, reconcile domain shared-file ownership and paired delivery, sync only as-built requirements and archive only completed named scope in the SAME implementation pair; do not merge precode alone or archive unfinished parent requirements.


## Shared-worker successor r2 concrete corrections

- [x] Reconcile protocol review db02c677 and independent domain review 2e03d6af into a preserved successor design; no Rust implementation claimed.
- [x] Add agreed-binding GET-only observation reusing exact pointer/descriptor checks, typed absence/invalid, and candidate comparison only for an actual prepared candidate; source4063d49, 11 fixed-slot HTTP tests passed.
- [x] Implement explicit CreateGroup control on existing mode dispatch/checkpoint: current ordinary admission for allocation only, persisted IDs/body, release/revalidate original token, exact conditional shared choice and current shared lease before create. Source `8c97cc2` verifies the bounded control with real local HTTP and CLI checks; production qualification remains closed and catalog registration/new-scope admission remain unfinished.
- [ ] Recover never-submitted and uncertain original attempts by current admitted SAME-ID/bytes retry; stale selected attempts observe only, changed namespace admits no old network work.
- [x] Persist original passive receiving custody and reconcile exact Initialize/Activate receipts before checkpoint/health or outbound retirement in reviewed source `24c1bb6`; [existing local HTTP / restart evidence](implementation-status.md#connected-core-source-increment) does not imply full provider/domain qualification. Later catalog staging-boundary corrections retain their own evidence below.
- [ ] Gate every affected product/admission/send path on exact staged mixed-genesis registration; factor locked registration publication without recursive gate acquisition and resume the original receipt after crash.
- [ ] Validate active winner and exact retained manifests separately; derive local uncertainty only from verified local Commit/predecessor lineage, preserve foreign history without effect authority, and block ambiguous lineage.
- [ ] Keep own or competing winners containing an exact unresolved local receipt committed-not-applied; test exclusive-retention settlement separately without promising active-intent release.
- [ ] Apply notebook semantic closure checks at live selected writer/adopter and recovery, fence actual model handoff/result commit, and recover stale capabilities only through exact original preparation under existing-only custody.
- [ ] Run real Worker/two-Store branches for pull-only join/update, absent/invalid slots, first-root allocation/mode/root crashes, before-create restart, stale edit after preparation, passive activation-before-checkpoint, readiness windows, sibling retained/foreign receipts and overlap settlement.
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
- [ ] Add format5 portable namespace/typed owner, strict original-byte closure validation, explicit Inspect/Edit/Status selector, original receipt/no-op behavior and real Worker/second-Store adoption.
- [ ] Capture admitted raw+typed local configuration together and integrate the effective request overlay, selected or established-absence pin, actual Writer/notebook role/prompt gates and ordered handoff/result checks; preserve original recovery and excluded local values.
- [x] Integrate the disjoint Handwriting1 raw-byte validator/projection/typed preparation adapter through reviewed parent82e11f2; keep ordinary leases and null-original refusal unchanged. Actual selected command/consumer integration remains open below.
- [ ] Enforce Store-atomic local operation reuse checking across selected producers with bounded existing local transaction evidence, identical replay and imported-operation separation; test concurrent competing scopes/profiles/corrections.
- [ ] Connect the real confirmed command, correction catalog/genesis, original sample/tombstone/rollback semantics, fixed-slot winner, passive receipt and exact selected/retained/media validation across two real format5 Stores.
- [ ] Reconcile compatible existing Reader/Writer receiving interfaces and actual recognition ingress before claiming shared example consumption; Buddy105 remains an explicit separately owned source dependency, not fulfilled by data transfer or archived normalized notebook stages.
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

- [x] Add format5-only portable namespace/contract and legacy-family publication refusal, exact raw V1 record/chain projection, group-stable key/UUID and original-condition-bound pure preparation; source `8a50104`, independent review pending.
- [x] Verify declaration-based no-op versus null/empty/omitted fallback, duplicate raw JSON, foreign/conflicted history, real selected Store reopen and all four legacy-family refusal controls; pass 25 portable configuration and 195 storage cases with their stated non-additive attribution.
- [x] Execute the unmodified older format5 reader's old-contract positive control / new-contract nonmutating refusal; retain its exact source/binary/schema provenance and three default-ignored gate attribution. Pass strict Clippy, formatting and unchanged final input hashes after the test-only borrow cleanup.
- [ ] Complete fresh first-scope/current-selected admission, portable Worker registration/publication/adoption, original Status and effective product/Manager command integration; pure record helpers grant no live permit.

## Portable raw-parent correction

- [x] Preserve a valid single-parent positive and correctly rehashed original `[P, P]` failure through both projection and actual Store admission; share one raw portable check before typed set normalization, source `76095e7`.
- [x] Pass 26 portable configuration / 195 storage cases with 3 explicit default ignored gates, strict Clippy/formatting and unchanged three-file correction hashes; preserve independent Worker drafts outside the correction and keep prior old-reader evidence at its original source.
- [ ] Obtain the requested independent narrow re-review and coordinator publication; this correction changes no contract fingerprint or live admission rule.
