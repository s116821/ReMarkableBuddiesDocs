## ADDED Requirements

### Requirement: Explicit modes and namespace isolation
The application SHALL expose local-only, isolated device backup and explicitly selected shared-group modes with distinct persistent bindings. A mode transition SHALL preserve local data and pending-work provenance without merging backups or deleting remote namespaces.

#### Scenario: Empty replacement and group join
- WHEN a replacement tablet with no local Buddy data selects an existing verified group
- THEN it pulls committed state before any publication, creates its own device/actor identity, and cannot upload an empty replacement or reuse another device's secrets.

#### Scenario: Leave or switch during pending work
- WHEN pending work belongs to the old backup/group binding and the device switches mode
- THEN the old publisher stops, the pending work cannot enter the new namespace, local data remains recoverable, and no other backup/group is deleted.

#### Scenario: Ordinary publication loses its acknowledgment
- WHEN an isolated publisher may have finished writing a backup marker
- THEN it reconciles the original provider ID and complete referenced package under the original binding before publishing another revision or reporting the backup as recoverable.

#### Scenario: Ordinary publication encounters a namespace or capacity refusal
- WHEN the isolated publisher cannot verify its binding, reaches an existing supported bound, or has no committed records to publish
- THEN local use remains available, status explains the refusal or no work, and previously committed backups remain available under their original identities.

### Requirement: Document aggregate and independent global keys
Shared adjudication SHALL group related Buddy records by stable logical source-document identity across conversations, pages and operations. Domain-owned projectors SHALL supply membership without duplicating domain schemas. Global subject memory, handwriting and portable configuration SHALL use independent stable keys.

#### Scenario: Different documents and global records
- WHEN two clients edit different documents and independent global records
- THEN all accepted scopes remain present; applying one scope cannot replace or delete the others.

#### Scenario: Unknown source identity
- WHEN a record lacks an unambiguous stable source-document identity
- THEN isolated backup may preserve it but shared document publication is visibly deferred, without deriving identity from a title, page position or conversation ID.

### Requirement: First valid upstream commit wins the same accepted base
Shared mode SHALL use a provider-qualified exclusive commit primitive. All contenders for a base SHALL address the same commit location; success/uncertainty SHALL resolve by verified committed content. A losing stale local aggregate SHALL be replaced by the accepted upstream aggregate and SHALL NOT be republished against a later base.

#### Scenario: Concurrent same-base edits
- WHEN A and B create different candidates for the same document/base/commit slot
- THEN exactly one valid upstream commit wins, both clients apply that winner, and the loser retires its old attempt without acquiring a new slot for that payload.

#### Scenario: Lost acknowledgement and old process retry
- WHEN A loses the response after creation and an old process later retries
- THEN it reads/retries the exact same pinned slot; identical operation/digest is acknowledged once, a competing valid winner is adopted, and no successor publication follows without a new edit from the applied base.

#### Scenario: Clock skew and interrupted ownership
- WHEN clocks differ or a process stops during publication
- THEN winner selection does not depend on timestamps, expiry or sleeps; uncertainty remains explicit until the exact commit location is verified, and an invalid/incomplete occupied slot causes recovery-required rather than deletion or alternate-slot bypass.

### Requirement: Unique explicit bootstrap and registration
A group SHALL be selected by verified immutable root identity, not filename. Registration SHALL preserve all existing key-to-genesis mappings and allow only one mapping per stable aggregate key.

#### Scenario: Competing initial registration
- WHEN clients concurrently register the same key
- THEN they converge on the winning catalog's one genesis slot before content publication; a losing different-key registration may retry against the accepted catalog while preserving its existing entries.

#### Scenario: Duplicate group names
- WHEN distinct group roots have the same display label
- THEN joining requires explicit root selection and cannot silently merge them or infer uniqueness from listing order.

### Requirement: Atomic selected view and operation invalidation
Applying an aggregate SHALL verify and stage its complete selected view before one durable local activation boundary. Reader/Writer durable writes SHALL atomically revalidate generation/base with commit. Stored historical branches SHALL NOT resurrect as active shared heads on recovery.

#### Scenario: Pull during an active operation
- WHEN a winning upstream revision replaces a generation used by an in-flight operation
- THEN stale completion cannot append active history, claim success or dispatch native effects; unrelated aggregates remain unchanged.

#### Scenario: Crash around activation
- WHEN a crash occurs before or after activation
- THEN recovery exposes either the prior complete selection or the new complete selection, with no partial mixture or automatic loser re-enqueue.

### Requirement: Serialized native admission and historical settlement
Reader/Writer operations SHALL serialize actual native handoff with selection activation through a domain-owned admission guard. Already-admitted uncertain effects SHALL retain reconciliation guards and prevent conflicting admissions until settled; replacement SHALL NOT retroactively cancel them or infer success.

#### Scenario: Selection races native admission
- WHEN selection activation occurs between a preliminary generation check and attempted native dispatch
- THEN the serialized admission guard refuses stale dispatch, or records admission before activation and requires guarded settlement; the OS process lease alone is insufficient.

#### Scenario: Already-admitted uncertain effect
- WHEN selection changes while an admitted external effect lacks verified completion
- THEN it remains reconciliation-required, conflicting admissions are blocked, and late completion cannot attach stale history to the new selection.

#### Scenario: Undo and drawing handoff invalidation
- WHEN activation invalidates an operation before history mutation or bitmap drawing, or either already-admitted effect returns a late uncertain result
- THEN stale dispatch is refused and uncertain original effects retain historical reconciliation without repeated undo/redo or fallback drawing; imported history/receipts cannot authorize these effects.

### Requirement: Buddy data coverage and native authority separation
Backup/sync SHALL include selected Buddy-owned history, bookkeeping, references, export correlation and portable domain records; screenshot/confirmed-sample media SHALL have explicit coverage. It SHALL exclude native documents/pages/ink/file metadata and device secrets/runtime state. Imported native references SHALL remain historical/unbound until separately verified against current native state.

#### Scenario: Native pages arrive later
- WHEN Buddy history arrives before native cloud pages
- THEN references remain waiting/unbound; no missing-page deletion, recreation, erase, export or undo replay is inferred.

#### Scenario: Large media omitted or missing
- WHEN remote policy intentionally omits a large sample or an included sample is unavailable
- THEN status distinguishes intentional omission from incomplete promised media, retains required local media, and never reports a complete restore for missing included content.

#### Scenario: Preparing an ordinary isolated backup snapshot
- WHEN the ordinary Store prepares a snapshot under its current isolated-mode lease
- THEN the existing format-1 archive preserves committed Buddy history and truthful media coverage, excludes device configuration and credentials, and an empty history produces no archive.

#### Scenario: Preparing an isolated backup that includes portable preferences
- WHEN an ordinary isolated backup contains committed Buddy history and a valid saved configuration capture
- THEN one versioned completion marker binds the verified data-only archive and the allowlisted portable artifact, with raw declaration presence preserved.

#### Scenario: Restoring backup data and portable preferences
- WHEN the operator selects a verified isolated backup for explicit maintenance on a destination tablet
- THEN each destination operation uses the matching verified component, and restoring Buddy data leaves the saved configuration alone until the operator separately confirms portable import.

### Requirement: File/OS management status and protected restore
Versioned file/OS contracts SHALL expose mode/identities, committed/applied revisions, generation, successful-sync time, pending/offline/auth/contention/replacement/recovery state and media coverage. Selected backup restore SHALL be an explicit validated hardwired maintenance transaction with rollback and new local actor identity; no Buddy service API SHALL be introduced.

#### Scenario: Corrupt or incompatible restore
- WHEN a selected backup is interrupted, corrupt or has unsupported schema
- THEN existing local state remains active, the restore reports its specific incomplete/incompatible status, and neither credentials nor native source data are replaced.

#### Scenario: Provider unavailable during offline edits
- WHEN internet/auth is unavailable
- THEN local interaction continues with visible pending work pinned to its accepted base; later contention adopts the committed winner rather than auto-rebasing stale edits.

### Requirement: Qualified application visibility
Shared mode SHALL require an explicitly qualified browser/Electron/tablet OAuth application-binding matrix; account equality alone SHALL NOT establish app-data/private-property visibility.

#### Scenario: Unsupported client registration
- WHEN a selected account is used through an unqualified or incompatible OAuth application binding
- THEN shared mode remains disabled or refuses activation, without widening scopes or exposing credentials.

### Requirement: Connected selected worker uses original publication custody
The application SHALL connect actual selected domain producers to its existing worker, original selected-attempt journal, agreed fixed-slot transport and complete receiving activation. It SHALL route modes before credential access and SHALL NOT use legacy manifest publication for explicit shared or local-only mode.

#### Scenario: Original publication loses acknowledgement
- WHEN the real selected producer's prepared original may have committed and the process restarts
- THEN a still-current original retries exact bytes/IDs at that same slot under actual admission, a stale selection observes only, a changed mode/binding admits no old-namespace network work, and missing or invalid evidence never authorizes a successor.

#### Scenario: Own or competing winner is activated
- WHEN complete same-base domain/media evidence validates a winner
- THEN actual domain-gated activation preserves unresolved local intent/evidence, stale work never appends against the new selection, and receipt-before-withdraw recovery retires only that original without resubmitting.

#### Scenario: Passive first join and later pull have no upload candidate
- WHEN the real worker follows an agreed root/catalog/domain slot on a Store with no local outbound attempt
- THEN it observes exact metadata and descriptor bytes read-only with typed absence/invalid results, creates no upload candidate or outgoing intent, and retains Joining/recovery state when initial evidence is unavailable.

#### Scenario: Explicit first-group allocation precedes shared root selection
- WHEN an original CreateGroup control is admitted under the exact current ordinary mode and qualified binding
- THEN allocation alone occurs under OrdinaryModeLease, complete original IDs/body persist before exact conditional shared-mode selection, and root creation requires the current resulting shared lease; a crash or raced choice cannot create another root or silently refresh the precondition.

#### Scenario: Prepared original stops before its first create
- WHEN a worker restarts after durable outbox preparation but before send
- THEN an unchanged original selection/mode/binding can retry the same fixed ID and bytes under actual domain admission; an intervening local edit forces observe-only recovery without a successor or rebase.

#### Scenario: Passive activation precedes checkpoint publication
- WHEN a first-join or passive-pull local activation receipt is durable but checkpoint or health publication is interrupted
- THEN the worker recovers the persisted receiver-local original operation and exact receipt, finishes only its registration/status bookkeeping, and neither activates twice nor fabricates an outbound attempt.

### Requirement: Portable ancestry and local admission identities remain distinct
Receiving SHALL preserve exact portable record/media references and create fresh local selection/admission identity. Local memory registrations SHALL bind receiving-local genesis; foreign transaction hashes and imported receipts SHALL NOT become local publication or effect authority.

#### Scenario: A second Store adopts shared memory and document state
- WHEN an authorized committed portable genesis is validated on another actor/store
- THEN original fact bytes and remote ancestry remain exact, the receiver derives its own strict local registration/selection, and no foreign token, pending intent or model/native receipt grants execution authority.

#### Scenario: Mixed genesis is initialized before local registration
- WHEN reception stops between a staged mixed scope's local Initialize and exact local catalog Registration
- THEN every affected product read/admission/Writer/worker send refuses readiness until the original receipt and mapping match, and recovery resumes that same staged operation without foreign local authority or recursively acquired gates.

#### Scenario: Retained siblings and imported pending history coexist
- WHEN a winner and a retained losing original have sibling revisions for the same record and the winner contains a validated foreign pending pair
- THEN each exact closure is projected separately, imported history grants no local effect or release, and only verified local original Commit lineage supplies the uncertainty fence; ambiguous purported local lineage remains blocked.

#### Scenario: Winner still selects an unresolved local receipt
- WHEN either own or competing winner includes an exact unresolved locally admitted receipt in selected membership
- THEN the worker keeps committed-not-applied status and original evidence without a successor until genuine local proof exists; exclusive-retention settlement is not used to clear the overlap.

### Requirement: Current notebook data has a working selected publication route
The selected worker feature SHALL include a reviewed compatibility stage for current notebook Source3, NotebookPlan and NotebookStage data and its actual selected producer. It SHALL preserve original envelope/media identities, semantic source/plan/stage closure, fresh local activation and older-reader refusal rather than relabeling unsupported format4 as synchronized.

#### Scenario: Notebook publication races winner adoption
- WHEN a current multi-stage notebook producer and worker encounter a replacement winner
- THEN each stage's accepted base/generation is checked at its real publication or model handoff, stale results remain historical or unknown without replay, and complete winning records/media activate atomically with local unresolved evidence retained.

#### Scenario: Required notebook source media is unavailable
- WHEN canonical archive media needed to validate Source3 and plan/stage semantics is absent or intentionally omitted
- THEN the candidate remains unapplied/incomplete and cannot be reported as a complete domain-valid winner; optional media omission remains separately visible and local evidence is preserved.

#### Scenario: Notebook publication outlives its original phase
- WHEN a selected notebook commit passes phase prechecks but cancellation, a stage or original cutoff, or original read-allowance exhaustion occurs while waiting or staging publication
- THEN the existing guarded commit checks that same allowance and pure cancellation/deadline predicate under the publication mutex and before the durable marker, refusing any new stage or draft authority
- AND no time window, read reservation, model permit or original operation is replaced to continue the attempt.

#### Scenario: Crash during selected notebook preparation
- WHEN the compatibility operation stops around generation/marker/contract/CURRENT/capability publication
- THEN recovery exposes the old complete ordinary generation or the complete new supported generation, retains original bytes and intent, and an older reader refuses the new unsupported format without repair.

#### Scenario: Notebook live validation matches reopen and original preparation recovers
- WHEN selected notebook publication/adoption or a crash around CURRENT and capabilities occurs
- THEN live writer/adopter enforce the same source/plan/stage semantics as recovery, actual model handoff and result commit retain current admission, and only the exact actor/source/target-bound preparation under existing-only custody can reconcile stale capabilities.


### Requirement: Shared portable declarations have a real selected producer and consumer
Shared mode SHALL adjudicate one portable-configuration record under the group-stable global key SHA-256 of UTF-8 `urn:remarkable-buddies:global-record:v1:portable-configuration`, with record UUIDv5 under the group UUID and the same name. Format5 SHALL be the explicit selected namespace/schema boundary. Values SHALL use the delivered strict V1 portable allowlist and raw present-declaration merge; decoded defaults, credentials, paths, model/runtime/native bindings and omitted declarations SHALL NOT become durable shared settings.

#### Scenario: Explicit edit and passive adoption
- WHEN an explicit conditional shared-preference Edit or a validated passive winner is processed
- THEN the existing selected Store/Worker/original outbox or ReceiveRequest supplies the sole publication/adoption path, no local Config file is rewritten, equal raw results create no receipt, and join/mode choice alone never seeds a preference record.

#### Scenario: Strict original bytes and sparse values
- WHEN a portable envelope contains duplicate nested payload members, unsupported null, unknown or excluded fields
- THEN strict decoding of its original ObjectRef bytes refuses it before generic JSON materialization; valid sparse objects and supported explicit null retain the delivered merge semantics and exact text.

#### Scenario: Effective request changes while work is in flight
- WHEN the selected preference head or established absence changes after a request captured its admitted raw and typed local configuration
- THEN one ordered preference/document/memory gate set revalidates the original pins at actual handoff and result publication; stale work refuses, original-only recovery stays readable, and the next request uses the validated in-memory overlay with local excluded values preserved.

#### Scenario: Local saved settings are not effective shared management
- WHEN the existing local Manager/import maintenance displays or edits the saved file
- THEN it retains its delivered local contract and cannot claim effective shared-group preference management; mode-aware shared view/edit remains separate integration work.

### Requirement: Shared preferences have guarded effective management
The Manager SHALL expose shared preference Inspect/Edit/Status through the same guarded private host behavior in browser and Electron. The real versioned Buddy one-shot command SHALL establish selected readiness, exact mode/group/binding/Store/selection or qualified-absence pins and the raw local configuration identity used for the effective projection. Only a successful authoritative Inspect SHALL enable a deliberately confirmed sparse V1 Edit. Saved mode hints, source-only fixtures and saved-file inspection SHALL NOT supply that authority.

For first absence only, Buddy MAY reuse its already-qualified fixed-slot adapter for a bounded GET-only refresh of Drive data under current mode/binding/Store custody, with qualification before credentials. It SHALL revalidate exact root identity, a complete accepted catalog, expected global key/owner, Store generation, epoch and raw local Config pin under existing gates and one original deadline/read budget. The Manager transports SHALL NOT issue provider requests or introduce another engine. This exception SHALL NOT allocate IDs, write Drive data, create OAuth grants/resources, change mode/Config/service state, or move publication/adoption from the existing Worker. Existing separately qualified credential refresh retains its original bounded authorization contract.

#### Scenario: First absence needs complete current evidence
- WHEN no local preference selection is available and first absence is requested
- THEN only a verified bootstrap and complete accepted catalog where the exact global key is absent can establish an editable absent guard; an exact-ID 404 alone, missing/partial/invalid/unavailable bootstrap, stale pins, or a known mapping not yet received remain Joining/unavailable without a guard or empty seed.

#### Scenario: First Edit re-admits absence
- WHEN an Edit presents an original absent Inspect guard
- THEN Buddy establishes current qualified absence again before conditional local publication; the saved guard grants no live permit, the GET provides no reservation or upstream success, and a later competing registration is adjudicated through the existing catalog/fixed-slot path without rebase of losing user content.

#### Scenario: Established selected work remains offline-capable
- WHEN an established selected Inspect/Edit or an original Status runs without a provider connection
- THEN exact current local domain/configuration pins or local original transaction/result custody remain the applicable admission evidence, with no unconditional network prerequisite introduced by first-absence refresh.

#### Scenario: Effective inspection changes before Edit
- WHEN a selected head, established absence, local fallback configuration, mode or connection changes after inspection
- THEN the original guard refuses stale Edit, field origins remain distinguishable, and any new edit requires fresh inspection and confirmation rather than rebase or automatic retry.

#### Scenario: Equal effective values have different declarations
- WHEN an explicit sparse shared declaration yields today's same effective value as local fallback or a default
- THEN omission, supported null and explicit-default declaration semantics remain distinct, and only an unchanged resulting portable declaration artifact is no-change without a fabricated receipt; effective-value equality alone cannot suppress the edit.

#### Scenario: Original Status after possible dispatch
- WHEN Edit output is lost or canceled after possible dispatch
- THEN the host retains the original operation/guard/patch digest and unknown disposition without private patch text, and Status proves correspondence from exact existing transaction and result custody or remains unknown; no fresh Edit, alternate ordinary Status or second operation index is used.

#### Scenario: Shared private presentation is removed
- **WHEN** navigation, submission, reinspection, expiry or clearing removes the shared prompt editor or revealed value
- **THEN** Manager clears the actual private input and revealed nodes before detaching them, reduces late hidden results without restoring an editor, and keeps pending or uncertain originals reachable without retry or treating a blank form as saved intent.

#### Scenario: Shared command meets a resident Store owner
- WHEN existing-only command acquisition encounters the resident process's exclusive Store lock or an older Buddy lacks the selector
- THEN both host paths report busy or unsupported truthfully without stopping the service, using a saved-file fallback or pretending effective shared values are available.

#### Scenario: Inspection is a snapshot rather than running activation
- WHEN Manager displays effective fields or a local pending/upstream applied/replaced disposition
- THEN explicit private text disclosure and bounded opaque-reference lifecycle preserve uncertainty, and the report identifies the next admitted request's projection without claiming that an already-running request consumed it.

### Requirement: Confirmed handwriting uses independent exact correction scopes
Shared confirmed handwriting SHALL use one fixed-slot chain per correction, typed owner HandwritingCorrection(profile, correction), existing Handwriting1 record identity/mutation semantics, and key SHA-256 of UTF-8 `urn:remarkable-buddies:global-record:v1:handwriting:{record_uuid}` using its canonical lowercase hyphenated UUID. Only an explicitly confirmed conditional typed operation in admitted format5 SharedGroup SHALL create or update this scope. Join, mode change, imported history and source/native document availability SHALL NOT confirm, reprofile or silently promote ordinary corrections.

#### Scenario: Confirm, update, forget and rollback
- WHEN a typed confirmed mutation targets an agreed genesis absence or current expected head
- THEN it uses existing mode lease, ordered catalog/correction gates and original Store receipt; a first Confirm alone creates genesis, Update preserves immutable original/sample/source linkage, Forget appends a known-key tombstone, and rollback is a fresh confirmed CAS Update without slot rewind or physical sample purge.

#### Scenario: Local operation UUID is reused across producers
- WHEN competing selected producers reuse one local operation with changed correction, profile, scope or request content
- THEN bounded complete local transaction evidence and the actual Store publication mutex atomically reject the conflicting publication across applicable producers without a shadow database; identical original replay remains historical, and imported envelope operations are not treated as local publication receipts.

#### Scenario: Competing correction winner and exact sample closure
- WHEN the existing Worker validates and adopts a same-key handwriting winner
- THEN strict original envelope/payload bytes, deterministic revisions/parents, one selected head, immutable original and bounded verified PNG/source provenance remain exact; each retained branch is validated separately, local required evidence/media survives one atomic activation, and the original passive receipt resumes after interruption without outbound intent or fresh confirmation.

#### Scenario: Omitted and missing samples differ
- WHEN a selected correction declares policy omission or promises included sample bytes
- THEN omission may activate verified metadata with incomplete-media status and no usable example, while missing/corrupt promised bytes prevent usable activation; unrelated cached bytes cannot override selected coverage, no sample is substituted/resampled, and source/retained evidence remains protected.

### Requirement: Shared handwriting reaches only a compatible admitted recognition consumer
Recognition SHALL use the explicitly selected local profile and a validated catalog/current correction inventory. Catalog/absence and exact example/head/media pins SHALL participate in the same ordered document/memory/preference admission set at actual recognition handoff and result publication. Stored corrections SHALL remain historical data and SHALL NOT authorize native output or import a foreign live capability.

#### Scenario: Bounded selected examples
- WHEN a compatible admitted shared recognition consumer captures confirmed context
- THEN it uses exact Included verified samples, target-hash exclusion, bounded confirmed-recency-v1 ordering, at most 16 candidates and 3 examples and the existing request/PNG budgets; explicitly requested stale/missing examples refuse, automatic selection reports incompleteness truthfully, and unavailable/incomplete with no usable sample never becomes complete-empty.

#### Scenario: Receiving interfaces remain unavailable
- WHEN the compatible Reader analysis/verification and typed Writer normalization interfaces from the separately owned receiving work are not delivered
- THEN domain transfer does not claim an actual recognition consumer, text-only Writer or archived normalized notebook processing does not masquerade as recognition, and null-original abstention/native ingress and held fidelity/device gates remain explicitly unfinished.

### Requirement: Manager inspects isolated backup revisions without tablet contact
Manager SHALL reuse the existing authenticated provider boundary and ordinary isolated V1 publisher format for disconnected backup inspection. Only a qualified current read binding may enumerate the publisher namespace. Complete bounded metadata and predecessor validation SHALL distinguish qualified empty from unavailable, corrupt or incomplete listings. Explicit selection SHALL retain the exact verified marker bytes, digest and binding under a bounded opaque host handle; it SHALL NOT imply a verified archive, restore eligibility or current native-page authority.

#### Scenario: Namespace visibility is not established
- WHEN Manager is signed in but the actual registration/grant cannot prove visibility of the tablet publisher's root, properties, markers and objects
- THEN backup inspection remains unqualified or unavailable rather than claiming empty backups or borrowing authority from the tablet's provisioning report.

#### Scenario: Selected marker remains the user's historical choice
- WHEN Manager verifies a revision's exact raw marker and a later revision appears
- THEN the selection remains tied to its original marker and observed ancestry until expiry or invalidation; Manager does not select by timestamps, silently advance the choice or claim its unverified archive/media are complete.

#### Scenario: Inspection loses its authority or complete listing
- WHEN cancellation, deadline, grant replacement, repeated pagination, ambiguous ancestry or changed selected metadata prevents complete validation
- THEN no partial view grants a usable selection and no provider write, automatic retry, tablet operation or restore follows.

### Requirement: Selected download reuses the complete isolated package validator
Manager SHALL reconstruct only the explicitly selected ordinary V1 closure under its original current protected authority, bounded transfer and private staging ownership. Byte hashes and an inventory alone SHALL NOT grant package verification; the existing Buddy isolated package oracle must accept the exact staged marker and closure before a verified handoff. Download SHALL NOT perform restore, import preferences or activate native/runtime state.

For a private stage-backed restore, Manager SHALL permit checked destination deletion only before a reader is submitted or after the original authenticated Prepare or Apply terminal report is strictly validated. Missing reader completion SHALL retain cleanup uncertainty without deleting the stage. Write-outcome reconciliation SHALL NOT substitute for reader completion.

#### Scenario: Selected download loses custody or exceeds its operational allowance
- WHEN the original selection expires, authority changes, a stream is corrupt or incomplete, staging identity changes, or the original byte/disk/call/deadline allowance is exhausted
- THEN no verified package is exposed, original reads stop, and only proven owned staging is retired; no replacement grant, later revision, path reuse or automatic retry is used.

#### Scenario: Download cancellation precedes its start acknowledgement
- WHEN the user starts download for the current selected operation and cancels before the start reply arrives
- THEN the same original operation owns cancellation, its deadline is not renewed, reads and verifier work join before exact owned staging is retired, and any reduced cleanup warning remains associated only with that operation; a late reply or old cancellation cannot replace or affect a successor.

#### Scenario: The download cancellation reply is lost
- WHEN the current view cancels a download and its transport rejects or cannot validate the joined cancellation reply
- THEN cleanup remains unconfirmed in that view without changing a later successor; neither host returns the awaited result after the original caller or document loses authority.

#### Scenario: A verified package intentionally omits media
- WHEN the existing complete package oracle accepts the original selected marker and closure with media intentionally omitted
- THEN the UI reports a verified package with omitted media separately from an interrupted or unverified download, validates the summary against the original selected digest, and receives no staging path, restore authority or replacement selection.

#### Scenario: Either Manager host exits with backup work outstanding
- WHEN desktop or packaged browser-helper shutdown begins while an inspection predecessor, protected guard, provider read, verifier or private restore destination is still closing
- THEN one shared owner closes admission and waits for the original pending work and checked staging release before shutdown completes, including when another owner fails; repeated shutdown joins the same drain and unconfirmed cleanup remains in the existing close/error report. Abort notification alone is not completion.

#### Scenario: A trusted restore handoff reads the verified local source
- WHEN the original handoff reads a member of its frozen verified inventory
- THEN the existing staging broker checks original file custody and streams bounded bytes under the original deadline and signal, verifies exact length and digest through EOF, refuses changed or additional members and use after retirement, and joins file access before staging release. This capability does not establish a remote destination or prove remote Prepare completion after a lost connection.

#### Scenario: A compatible complete package verifier is unavailable
- WHEN the selected bytes are reconstructed but no qualified existing Buddy oracle runner can validate them
- THEN Manager reports unavailable or reconstruction-only evidence and does not offer the bytes as a verified restore input or silently introduce another semantic validator.

#### Scenario: A verified backup enters the existing restore preview
- WHEN a trusted host consumer explicitly hands off the exact verified selection to the existing ordinary restore owner for the captured wired target
- THEN one original maintenance admission covers bounded transfer and Prepare, the returned archive digest must match the original data manifest, and preview is accepted only after complete source handoff and destination custody checks; paths and producer intents remain private and no Apply is dispatched.

#### Scenario: Cancellation outlives a restore handoff timeout
- WHEN transfer or Prepare is still closing after the original handoff deadline or cancellation
- THEN the host joins that work before releasing its stages, preserves uncertain cleanup, and refuses stale preview; a later explicit Confirm requires the original ready intent and still-owned destination, while uncertain Apply Status retains its original reconciliation packet.

#### Scenario: A submitted restore reader loses its terminal report
- WHEN the original stage-backed Prepare or Apply has no strictly validated authenticated terminal report because of cancellation, timeout, local child exit, missing remote exit status, malformed output or lost target identity
- THEN the host withholds destination release and reports cleanup uncertainty; repeated close and a later original Status do not convert that uncertainty into deletion authority.

#### Scenario: Apply finishes reading with an unknown write outcome
- WHEN the original authenticated Apply returns a strictly validated terminal report whose write outcome remains unknown
- THEN the owner may attempt checked release of that exact destination while preserving the unknown write outcome and original Status packet; it does not retry Apply or claim restoration.

#### Scenario: External cancellation races private restore retirement
- WHEN an external observer operation attempts to revoke the maintenance lane while a private restore command or checked retirement is still joining
- THEN the existing joined admission prevents a competing owner until that local work settles, without treating local settlement as proof of remote reader completion.

#### Scenario: The host oracle is delivered as a Manager dependency
- WHEN a supported Manager host can verify the pinned normal Buddy command in its private installed resources
- THEN the host uses only the fixed offline inspect-isolated command with its original source, target and byte identity, bounded I/O and joined cancellation; it does not obtain code from a provider package, runtime download, renderer input or tablet release archive.

#### Scenario: Platform or distribution qualification is missing
- WHEN the executable is absent, changed, wrong-platform or unqualified for the actual browser-helper or Electron distribution
- THEN verification remains unavailable; a working Linux source command, static browser ZIP or successful package build alone cannot claim a qualified Windows or installed-host path.

#### Scenario: The packaged Manager starts its browser helper
- WHEN the user explicitly launches the existing packaged executable with `--browser-helper`
- THEN the existing fixed-loopback helper serves its packaged browser UI without a desktop window, resolves host resources only from the installed package, and awaits owned shutdown; the mode does not activate an unqualified oracle or grant source-only helper authority.

### Requirement: Buddy receives isolated restore inputs with exact cleanup ownership

The normal Buddy archive CLI SHALL receive a bounded isolated V1 backup into a
private configuration-derived staging directory, verify it using the existing
package oracle and return a receipt bound to the original boot and exact tree.
It SHALL use the [destination command contract](../../manager-isolated-backup-download.md#buddy-destination-staging-command)
for framing, limits and descriptor custody. It SHALL NOT restore data, apply
preferences, start runtime or register a production Manager adapter.

#### Scenario: A complete original upload becomes a restore input
- WHEN one admitted upload satisfies the fixed framing, deadline, free-space, identity and existing package checks
- THEN Buddy returns only that stage's bounded receipt, and later check or release requires its original boot, parent, exact members and custody commitment.

#### Scenario: An upload fails while the command still owns its partial files
- WHEN framing, integrity or validation fails before receipt handoff and the command can still prove exact ownership
- THEN it attempts bounded descriptor-owned removal of its own partial output; failed or uncertain cleanup is reported, and unrelated, replaced or unexpected entries remain untouched.

#### Scenario: The upload acknowledgement is lost
- WHEN Manager cannot validate the original terminal receive reply
- THEN the preallocated stage ID stays tied to that consumed operation and its cleanup warning, with no automatic adoption, retry or deletion from a matched name alone.

#### Scenario: A staged tree or supported execution boundary changes
- WHEN the original boot, parent, directory membership or member identity changes, or the platform lacks the required descriptor and deadline boundary
- THEN the command refuses success without claiming cleanup or granting restore authority.


### Requirement: Manager streams verified restore input through its existing wired owner

The private Manager destination adapter SHALL stream the original sealed
isolated-package inventory through the existing observed child and joined
maintenance owner, using the [Manager streaming contract](../../manager-isolated-backup-download.md#manager-streaming-adapter).
It SHALL intersect source and restore cancellation and deadlines, retain bounded
buffering and accept only original authenticated terminal evidence. It SHALL
preserve the existing reader-completion guard and sticky cleanup uncertainty.
Source or peer tests SHALL NOT enable production registration without installed
qualification.

#### Scenario: The original verified inventory is uploaded
- WHEN one current source handoff and target admit the private destination adapter
- THEN only the fixed framed inventory reaches the original fixed Buddy selector, complete joined transfer and exact receipt checks precede Prepare, and no payload path, arbitrary command or Apply authority reaches the renderer.

#### Scenario: Cancellation interrupts a buffered or stalled write
- WHEN the original source or restore attempt expires or is cancelled while its source read, pipe writer or SSH child is pending
- THEN those same owners settle before retirement or successor dispatch, no read or close renews the original deadline, and missing trustworthy terminal evidence retains the preallocated stage identity and cleanup warning without retry.

#### Scenario: Destination release occurs after the original preview call
- WHEN disposal, drop or expiry requests the stage handle's one-shot release after its original joined call has ended
- THEN release requires an idle bounded joined maintenance lease and the original still-current target and receipt; a competing owner or unresolved Prepare/Apply reader leaves cleanup unconfirmed and is never cancelled to obtain cleanup access.

### Requirement: Manager previews verified backup preferences in both companions

Browser and Electron Manager SHALL offer a deliberate preferences preview for the exact selected and verified backup on the original admitted wired destination. The shared portable owner SHALL publish a preview only after the one-shot source handoff and checked staging retirement. It SHALL accept Apply only through the existing explicit Confirm for that still-ready original. A possibly dispatched Apply SHALL retain its original portable Status route and reference.

#### Scenario: The operator reviews saved preferences from a verified backup
- WHEN the same verified download and wired connection and boot remain current and the user chooses Review backup preferences
- THEN both companions use the exact original selected pair, show the reduced preview in the existing preferences panel and allow only explicit Confirm of that prepared reference. No-change has no Confirm.

#### Scenario: Task navigation transfers a verified preview to its consumer
- **WHEN** the operator deliberately opens a preference or data preview from Cloud backups
- **THEN** Manager selects the corresponding existing consumer workflow before preparation, preserves the exact source and original deadline, and requires separate confirmation; leaving that consumer invalidates an unused or late preview without replaying an original write.

#### Scenario: The original preview is cancelled while Prepare or retirement settles
- WHEN the original caller, selection, target or view is invalidated while the host holds the joined Prepare
- THEN the host fences result delivery, joins the original work and checked retirement, and reports any unconfirmed cleanup against that operation while denying stale preview and automatic retry.

#### Scenario: A cancelled Ready competes with a successor or Confirm
- WHEN a late cancellation or failed delivery names an older backup attempt
- THEN only that attempt's exact still-ready editor may be discarded. A newer editor keeps custody and an Apply that may have dispatched remains reconcilable only through its existing original Status.

#### Scenario: A shipped host starts without qualified namespace or staging inputs
- WHEN either companion uses its default production startup with those inputs absent
- THEN no verified preferences preview is available and the host dispatches no portable maintenance from the backup path.

### Requirement: Manager previews verified backup data in the existing Ordinary Restore flow

Both companions SHALL offer a deliberate data-only restore preview for the exact verified backup and admitted existing wired target through the [closed preview bridge](../../manager-isolated-backup-download.md#manager-data-restore-preview-from-a-verified-backup). Data and preferences previews SHALL share one attempt owner and one consumable verified download. The ordinary owner SHALL retain the private archive path and stage receipt. The existing explicit Confirm and original Status SHALL remain the Apply and reconciliation routes.

#### Scenario: The operator previews the original verified data
- WHEN the current document, exact verified backup selection and admitted connection and boot match a deliberate data preview
- THEN Manager takes only that verified download under the joined maintenance owner, joins source retirement, and delivers a checked data-only Ready in its existing Ordinary Restore panel without a renderer filesystem path or Apply.

#### Scenario: Two preview actions compete for source custody
- WHEN preferences or data preview is refused Busy while the other action or a maintenance operation holds custody
- THEN retry permission requires refusal before consumption, no cleanup uncertainty and the same still-eligible original download. A consumed download cannot supply either a rival preview or automatic retry.

#### Scenario: Cancellation races an original preview or Confirm
- WHEN cancellation, stale authority or failed delivery occurs during a data preview or an outstanding pre-Apply check
- THEN only the original joined work and exact still-ready editor retire, the original cleanup uncertainty remains visible, and a possible Apply and its original Status reference survive independently of the backup preview.

#### Scenario: A default or unqualified destination is requested
- WHEN trusted source or destination admission is absent, or the requested target is not an admitted existing wired store
- THEN the bridge returns no Ready and dispatches no unqualified restore path. Source, host fixture and packaged evidence leaves provider, installed, and clean or replacement target qualification open.


### Requirement: Manager creates the first target-local saved configuration explicitly

Both companions SHALL expose the same deliberate first-configuration action on
an admitted compatible installed and quiescent wired target as part of the
[clean or replacement workflow](../../manager-isolated-backup-download.md#first-saved-configuration-on-a-clean-or-replacement-target).
On Linux, the fixed Buddy command SHALL validate its own target-local defaults
and use atomic no-replace publication only when the file is absent. The new
selectors SHALL refuse before filesystem access on non-Linux. Review and
current Check SHALL be read-only. Store initialization, backup preview and Apply SHALL
each retain their existing explicit actions.

#### Scenario: A clean target has no saved configuration

- WHEN a reviewed and confirmed request still matches the installed target, connection and boot and the fixed configuration can safely be created
- THEN Buddy publishes only its validated target-local default configuration and verifies readback before reporting success. Store initialization, service activation, provider access, mode or group choice, preferences import, and restore require separate actions.

#### Scenario: The fixed configuration exists or target authority is uncertain

- WHEN the file exists, another creator wins, the path or parent is unsafe, or required installed/target authority is absent or stale
- THEN the action preserves existing bytes and refuses or reports the verified existing file. A safe valid file is reported independently of the absent-or-empty Store roots required for creation. The action does not stage a backup, replace invalid content or infer a clean target from missing metadata.

#### Scenario: A Create response is lost

- WHEN the original Create may have dispatched and no complete original outcome is admitted
- THEN both companions retain the original as unconfirmed within the host lifetime and do not replay it. A separate read-only Check reports current configuration availability without changing the retained outcome. Only a fresh deliberate setup action can proceed from verified current prerequisites.

#### Scenario: Setup presentation is unmounted
- **WHEN** the operator leaves Tablet / Setup while configuration is missing, blocked, pending or uncertain
- **THEN** application-owned current and original state survives navigation, missing or blocked state does not become valid setup, and pending or uncertain work remains reachable without retry.

### Requirement: Manager package observation preserves release compatibility
The existing bounded Manager ZIP observer SHALL verify embedded native oracle metadata and executable bytes without extraction or execution. Native packages SHALL agree on the embedded Buddy source record, and present oracles SHALL have complete platform-specific membership, modes, sizes and hashes. Runtime observation SHALL validate the downloaded release's internal consistency rather than require its dependency to match the older installed Manager pin. The fixed quarantine response SHALL NOT grant installation eligibility.

#### Scenario: An older Manager downloads a newer dependency
- WHEN an otherwise authenticated Manager release contains a different valid Buddy pin with consistent native provenance and executable bytes
- THEN bounded runtime observation accepts that dependency consistency without consulting the installed old pin or executing the new command; existing release identity and digest checks still apply.

#### Scenario: Legacy package or mandatory version-1 dependency
- WHEN both native oracles are absent from a Manager release earlier than 1.0.0
- THEN legacy quarantine remains available; any present oracle requires complete matching-source native pairs, and Manager 1.0.0 or later requires both pairs. Static browser output contains no native oracle.

#### Scenario: Shipping candidate differs from its reviewed inputs
- WHEN shipping CI observes a candidate at any version
- THEN it additionally requires both native pairs to match the candidate checkout pin and Build's original retained executable/provenance, while preserving the same three ZIPs, no-execution observation and premature-1.0 hold.

#### Scenario: Native tests consume a shipping dependency
- WHEN Build has retained the normal executable before compiling test-only targets
- THEN the existing native Integration jobs test that exact packaged executable using retained native test inputs, check its original version and bytes, and leave both the command and release ZIPs unchanged; no Integration rebuild or replacement grants shipping qualification.

### Requirement: Manager completes Drive authorization without user developer setup
Both companions SHALL begin normal Drive setup in Manager using an approved
maintainer-owned desktop registration and Google's system-browser consent.
Each user SHALL authorize their own account. The private tablet authorization
purpose SHALL reuse the existing OAuth implementation, preserve the host grant,
and retain only a distinct, verified, short-lived tablet grant for one private
handoff. Tokens SHALL NOT enter renderer messages or public status. The
[connected delivery contract](../../manager-tablet-drive-authorization.md)
SHALL keep authorization, verified USB installation and completed backup distinct.

#### Scenario: A separate tablet grant is accepted
- WHEN the new grant has the expected client, exact application-data scope, original account and distinct refresh token and the original protected custody remains current
- THEN Manager retains it privately until its bounded expiry and exposes only a reduced state, account label and opaque reference; the original host grant is unchanged.

#### Scenario: Pending authorization loses its owner
- WHEN cancellation, another authentication operation, expiry, disposal or protected registration/grant drift invalidates the pending authorization
- THEN no stale callback or handoff can recover its credential, and no automatic tablet write or provider retry follows.

#### Scenario: A private handoff is consumed
- WHEN the trusted host workflow takes the exact current reference for a canonical nonzero collection UUID
- THEN it receives the existing Buddy V1 record once with expiry converted to UNIX seconds; a second take returns no secret. This helper alone does not establish target authority or installed backup readiness.

#### Scenario: Tablet connection is confirmed
- WHEN the selected connection, boot, configured Store, mode token, original credential slot and private account custody still match the reviewed setup
- THEN the shared host persists its token-free original operation before dispatching the fixed stdin-only credential writer once. Creation requires absence; replacement and removal require the exact original revision, metadata and binding. Buddy serializes publication with Store and mode ownership and reports success only after private atomic publication and checked readback.

#### Scenario: A credential write response is lost across Manager restart
- WHEN a dispatched credential change has no admitted response and the Manager restarts
- THEN both companions recover the original readback request from the existing protected store and offer Check without replaying Apply. Desired-state observation proves the current file state, not who wrote it; changed custody stays unresolved. Only verified resolution and a successful protected compare-and-swap retire the original.

#### Scenario: An isolated tablet reconnects after credential removal
- WHEN the credential slot is absent but an isolated backup mode remains selected
- THEN setup uses the verified collection and binding retained atomically with the earlier resolution. Missing or mismatched provenance requires recovery before consent, never a guessed collection or implicit mode change. Protected capacity reserves a binding slot for every unresolved target before any write.

#### Scenario: A prepared connection loses its owner
- WHEN a matching preview detects connection loss, account supersession, protected-record drift, expiry or cancellation
- THEN it erases its prepared input and permanently retires that reference. Restoring the previous observation cannot make it confirmable again, and a late response cannot release another maintenance owner or restore a private view.
