## ADDED Requirements

### Requirement: Resident historical source capture
Buddy SHALL route source capture through the existing resident request, input,
health and runtime checks under resident-capture-integration.md. It SHALL retain
the original deadline and expected source, accept only SDK-validated historical
image evidence and grant no page observation or write authority from that result.
Capture SHALL neither journal a mutation nor resolve a prior uncertain effect.
Original v1/v2 mutation frames and digests SHALL remain unchanged when live
transport advances to revision 3; mutation-journal bounds SHALL remain unchanged.

#### Scenario: Capture exceeds an ordinary control frame
- **WHEN** an admitted source capture returns a valid bounded image larger than 64 KiB
- **THEN** the consumer delivers historical image evidence only after final input, health and runtime admission

#### Scenario: Capture is canceled while awaiting pixels
- **WHEN** input cancels or the original deadline expires during capture
- **THEN** the request retires without image delivery or automatic retry, preserves the resident child and retains prior uncertain effects

#### Scenario: Capture source or image is inconsistent
- **WHEN** a correlated response changes the expected source or has invalid image bytes
- **THEN** the consumer reports integrity failure and withholds the capture

### Requirement: Development bootstrap handoff uses distinct input admissions
The standalone observation-only controller SHALL require valid quiet input before
its single Buddy-stop submission. After submission it MAY end that admission,
wait for the original service's terminal and empty-group proof, then establish a
fresh read-only observation admission under the original deadline. It SHALL record
both boundaries and disclose the uncovered handoff interval. It SHALL NOT claim
request or source continuity across that interval, reset a failed admission, or
exclude devices by name. Fresh seeded contacts or observer failure SHALL refuse.
The new guard SHALL remain active through stock shutdown, observer launch and
completion. Installed Session input continuity SHALL remain unchanged.

Same-incarnation terminal snapshots with an original populated group SHALL remain
pending under the existing deadline, never stopped. Identity, policy, group and
cleared-state validation SHALL remain mandatory. Recovery SHALL require fresh quiet
input before a new Buddy-start submission; independently verified restoration
afterward SHALL be recorded as historical service evidence without requiring the
pre-start input inventory to survive or granting input authority.

#### Scenario: Buddy shutdown removes its input device
- **WHEN** the diagnostic has admitted one Buddy stop and is awaiting terminal proof
- **THEN** it records the ended handoff admission, grants no observation authority during the interval, and creates its fresh admission only after the original service and group are proved stopped

#### Scenario: Fresh observation admission sees a held contact
- **WHEN** the new observer's seeded state is not quiet or its inventory cannot be validated
- **THEN** the diagnostic refuses before stock stop without retrying admission or claiming a quiet handoff interval

#### Scenario: Service termination precedes group teardown
- **WHEN** a valid original terminal service snapshot brackets a still-populated original group
- **THEN** shutdown remains pending until a fresh valid empty-group bracket or the original deadline, while changed policy or identity still refuses

#### Scenario: Restored Buddy creates its keyboard
- **WHEN** recovery has submitted the sole admitted start and independently verifies Buddy running
- **THEN** it may record historical restoration without reusing pre-start input authority or submitting another start

### Requirement: Resident caller progress
Buddy SHALL service caller cancellation and main-thread health during resident
socket startup and request waits using the original deadline. Progress failure
SHALL preserve original pending-effect uncertainty and Store reservations;
only explicit predispatch proof SHALL permit known-not-dispatched recording.
Startup failure after spawn SHALL retain evidence and stop only the owned child.
For an established session, ordinary request cancellation, timeout or idle
connection retirement SHALL preserve the resident process. Reconnection SHALL
retain its verified activation, use fresh connection identities, preserve
original uncertainty and never replay an effect. Health or session integrity
failure SHALL still enter independent recovery.
Installed Session operations SHALL obtain input progress from an owned Linux
observer guard. Cancellation SHALL remain sticky for that request, while later
observer errors SHALL still be treated as integrity loss. Postactivation input
descriptor renewal SHALL overlap old and new observation without reusing a stale
page/process guard or resetting cancellation.

#### Scenario: Cancel while the resident endpoint is starting
- **WHEN** installed progress fails before socket readiness or handshake completion
- **THEN** startup fails under the unchanged deadline, the owned child is stopped and reaped, and retained evidence does not claim native cancellation or recovery

#### Scenario: Cancel an already dispatched effect
- **WHEN** input or health progress fails while awaiting insertion or selection
- **THEN** the original attempt remains uncertain across Store restart and no retry is inferred from the closed connection

#### Scenario: Idle connection closes between conversations
- **WHEN** the endpoint retires an idle connection while the verified resident process remains healthy
- **THEN** the next admitted connection uses fresh identities with the same resident process and retained evidence, without restarting stock or replaying a prior request

#### Scenario: Input changes during an authority check
- **WHEN** a request's service or runtime authority check takes time and input cancels during that check
- **THEN** fresh input admission refuses the request before effect reservation or dispatch

#### Scenario: Request expires during outcome publication
- **WHEN** cancellation, the original deadline, or input-observer failure occurs while a valid reply is being durably recorded
- **THEN** final admission refuses reply delivery, preserves the actual recorded historical outcome without replay, and treats observer failure as a session integrity failure

#### Scenario: Caller deadline differs from failed service observation
- **WHEN** a bounded service read fails during request progress
- **THEN** only an explicitly typed caller deadline with successful owned-command cleanup may retire the request ordinarily; internal read timeout, integrity failure, or an unreaped command remains fatal

#### Scenario: Input quiets after canceling a request
- **WHEN** an owned observer reports activity or an unfinished contact and later reports quiet input
- **THEN** the same request remains canceled, and a subsequent observer error still becomes integrity loss

#### Scenario: Input changes while descriptors are renewed after activation
- **WHEN** fresh input descriptors are constructed before retiring the old observer
- **THEN** old and new observations both participate in final admission, activity on either refuses continuation, and any renewal failure invalidates the guard without retry

### Requirement: Durable resident insertion attempt reservation
The resident SDK consumer SHALL durably reserve the exact original insertion frame/digest and conversation before request bytes, using the existing Store ownership/serialization boundary. A reservation SHALL reject reused operations and replacement attempts for unresolved or observed conversations, survive restart and generation changes, and retain uncertain outcomes for read-only reconciliation of the original target. Only a durably recorded known-no-effect outcome SHALL permit a new caller-selected operation; no automatic retry is supplied. Historical replies SHALL NOT grant binding, rendering or native persistence authority. Malformed or incomplete journal state SHALL refuse without resetting it. Detailed consumer obligations are in resident-client-integration.md.

#### Scenario: Response is lost after request admission
- **WHEN** an insertion loses its authenticated connection after pending admission
- **THEN** the original conversation/operation/source/target reservation remains, and neither reconnect nor a fresh operation/target can automatically authorize another insertion for that conversation

#### Scenario: Journal cannot be made durable
- **WHEN** reservation persistence or validation fails before request admission
- **THEN** no insertion bytes are sent, existing evidence is preserved, and any uncertain publication remains conservatively reserved

#### Scenario: Historical insertion response is stored
- **WHEN** the SDK returns an attributed insertion observation and the consumer records it
- **THEN** it remains historical correspondence without native persistence, current selection, qualified page binding or render authority

#### Scenario: SDK protocol upgrades with retained attempts
- **WHEN** the consumer moves from v1 to v2 with prior insertion attempts
- **THEN** original canonical frame/digest fields, consumed operations and unresolved reservations survive unchanged; responses require the original digest and matching revision, and live requests use v3 without replaying historical effects

### Requirement: Durable resident target-selection attempts
Selection SHALL reserve its exact original effect frame/digest before pending
admission or bytes, using the same Store-owned bounded journal and consumed-operation
namespace as insertion. Unknown outcomes SHALL block later effects for that
conversation. Observed insertion/selection SHALL allow only fresh selection of the
same document/target, not another insertion or different-target fallback. A known
refusal SHALL NOT erase an earlier target restriction. Historical selection SHALL
remain separate from binding, capture, writing and native settlement authority.
Detailed transition and schema obligations are in resident-selection-integration.md.

#### Scenario: Selection response is lost
- **WHEN** a selection request loses its response after admission
- **THEN** its original operation/source/target remains reserved, later insertion and selection refuse, and only typed read-only reconciliation is available without clearing the reservation

#### Scenario: Created or reused Buddy needs selection
- **WHEN** an earlier insertion or selection was observed for a conversation
- **THEN** a new operation may select only that same document/target under fresh expected facts; a refusal of that new selection does not remove the earlier restriction

#### Scenario: Selection journal is upgraded
- **WHEN** a successful write upgrades the legacy insertion-only journal to format 2
- **THEN** original frame/digest/outcome fields and consumed operation IDs are retained, and readers that do not support the new format refuse it

#### Scenario: Outcome publication reports failure after storing a valid reply
- **WHEN** a publication error is reported and the journal is later reopened
- **THEN** the actual validated stored outcome governs fresh-operation admission: an observed result restricts selection to its original document/target, Reserved or Indeterminate blocks both effects, and every later effect requires a successful synchronized whole-journal reservation write before bytes; the original operation is never replayed

### Requirement: Stored association input remains historical in SDK acquisition decisions
The existing SDK acquisition decision seam SHALL consume the real historical Ledger through a read-only lookup under historical-binding-projection-contract.md. A saved match SHALL map only to historical evidence, and missing/failed/conflicted/tombstoned stored data SHALL remain unresolved rather than the model's affirmative Missing or RelevantModelAssociation input. Existing complete Synthetic observation/receipt guards SHALL precede lookup. This increment SHALL leave installed Reader behavior unchanged and grant no reuse, insertion, adoption, binding or rendering permission.

#### Scenario: Matching saved association is supplied to current-first assessment
- **WHEN** the guarded SDK decision consults a matching historical Ledger association
- **THEN** it remains unresolved as a current-effect decision, without unnecessary successor inspection, Store writes or SDK effects

#### Scenario: Positive recognition accompanies uncertain stored data
- **WHEN** positive ordinary or non-Buddy model recognition accompanies missing, failed, conflicted or tombstoned stored inspection
- **THEN** it cannot erase that uncertainty to produce a reuse candidate or insertion plan through this lookup

### Requirement: Buddy-page recognition and reuse precede automatic insertion
The automatic product workflow SHALL identify and reuse the relevant current Buddy page or its relevant immediate successor before creating another page, under buddy-page-reuse-contract.md. It SHALL reuse the existing REM-37 document/page-to-conversation Store binding with current native identity/order and device qualification, not invent a separate registry. Unknown or stale associations SHALL fall back to recognition; missing binding or uncertain recognition SHALL NOT imply a non-Buddy page or authorize duplicate creation. Legacy header-only candidates SHALL require qualified acquisition/adoption rather than a silently trusted claim. Lower-level SDK insertion tests SHALL NOT establish this product requirement.

#### Scenario: Current or adjacent Buddy page is already relevant
- **WHEN** qualified association and current state or recognition establish the relevant Buddy page is current or immediately follows the original source
- **THEN** the workflow reuses that page and creates no duplicate; a verified current-page binding avoids unnecessary successor inspection

#### Scenario: Association is unknown or stale
- **WHEN** a binding is missing, conflicted, stale or inconsistent with current native identity/order, or a legacy candidate is unbound
- **THEN** the workflow falls back to recognition and qualified adoption as applicable, preserving content; unresolved recognition grants no insertion authority

#### Scenario: Visual inspection discovers a non-Buddy neighbor
- **WHEN** an ordinary guarded successor inspection positively identifies the existing neighbor as a non-Buddy page
- **THEN** after fresh source/session/order revalidation the workflow inserts between the ORIGINAL source and that same neighbor, preserving both and all saved ink regardless of the displayed inspection page

#### Scenario: Placement changes during inspection
- **WHEN** the original source, immediate neighbor, document/session or ordered inventory changes before insertion publication
- **THEN** the planned insertion refuses without relocating its anchor, creating a duplicate or replaying an effect

#### Scenario: Recognized Buddy candidate has an unresolved association
- **WHEN** recognition identifies a Buddy candidate but its relevance or existing conversation association is conflicting or unresolved
- **THEN** acquisition resolves/reuses/adopts that candidate or safely refuses; being unbound or not yet established as relevant SHALL NOT cause insertion beside it

### Requirement: Local SDK acquisition planning preserves reuse and original placement without effect authority
The experimental local consumer SHALL assess a relevant current Buddy candidate before successor inspection, consume supplied read-only association projections and observation-bound recognition, and retain missing/stale/imported/conflicting ownership as unresolved evidence rather than permission to duplicate a page. It SHALL preserve the ORIGINAL source and exact order through an SDK-created successor navigation receipt, with complete opaque current/receipt observation equality. Only positive ordinary source and confirmed non-Buddy successor, or exact synthetic end, SHALL yield an explicitly synthetic placement plan after the original source. This seam SHALL allocate no target, dispatch no SDK creation/navigation, mutate no Store/binding, construct no NativeCommitted or renderer permission, and leave installed Reader behavior unchanged under buddy-acquisition-decision-contract.md.

#### Scenario: Relevant current association is supplied
- **WHEN** the complete fresh synthetic current observation and exact page/conversation association agree
- **THEN** the model returns a reuse candidate with only current lookup and no successor inspection or creation

#### Scenario: Association or recognition remains uncertain
- **WHEN** binding is missing/historical/conflicted or recognition is blank, unavailable, unknown or mismatched
- **THEN** no insertion plan is produced from that uncertainty, and an unbound Buddy candidate requires separately qualified adoption

#### Scenario: Confirmed ordinary successor is displayed after inspection
- **WHEN** SDK successor evidence matches the original source, exact immediate neighbor/order and fresh completed observation, and positive non-Buddy recognition has no contradictory claim
- **THEN** the model retains an after-original/before-neighbor plan without retargeting creation to the inspected successor or dispatching the stale original source guard

### Requirement: Synthetic return matching does not refresh logical claims or effect authority
The local placement model SHALL retain either uninspected end or the actual validated successor completion. Its pure continuity matcher SHALL require explicit Synthetic origins, exact original order/adjacency and SDK-created Previous receipt source matching that retained completion, target matching original source and supplied source matching returned completion. End plans SHALL require no receipt and unchanged full original observation still at end. Results SHALL remain point-in-time SyntheticSourceContinuity under buddy-source-continuity-contract.md, not proof of collection freshness, logical association/recognition refresh, native qualification or creation/render/binding permission. No effects, allocation, SDK private-field reconstruction or CreationRequest conversion SHALL be added.

#### Scenario: Supported synthetic return preserves the original anchor
- **WHEN** the Previous receipt closes from the retained inspected successor to the exact original page/order and the supplied completed observation agrees
- **THEN** the matcher returns source continuity while retaining historical original placement and conveying no effect permission

#### Scenario: Return or end evidence is wrong or stale
- **WHEN** receipt is missing/unexpected/foreign, direction or target differs, order/adjacency changes, or opaque completion/current evidence disagrees
- **THEN** matching refuses without navigation, creation, target allocation or fallback to a stale original source

#### Scenario: Logical claims change independently of SDK state
- **WHEN** Store-like association or recognition changes while supplied SDK continuity remains equal
- **THEN** a continuity result does not validate those claims or authorize an insertion, and future effectful use still requires separate current logical and SDK guards

### Requirement: Legacy classification is not positive non-Buddy or relevant ownership evidence
The pure synthetic consumer bridge SHALL exhaustively map ExistingQA to LegacyBuddy, Blank to Blank and Invalid to Unknown under buddy-legacy-recognition-bridge-contract.md, with explicit Synthetic observation/full context/conversation binding and valid order. It SHALL NOT produce RelevantBuddy, OrdinarySource or ConfirmedNonBuddy, claim the supplied enum's capture provenance or grant reuse/insertion/adoption/binding/render permission. The classifier and installed Reader SHALL remain unchanged.

#### Scenario: Unbound legacy header match
- **WHEN** ExistingQA is supplied with a matching synthetic observation and missing association
- **THEN** the current or successor model requires separately qualified adoption and creates no insertion plan

#### Scenario: Blank or invalid page classification
- **WHEN** Blank or Invalid is supplied with missing association evidence
- **THEN** the model remains unresolved rather than infer Buddy absence or duplicate creation eligibility

#### Scenario: Supplied classification belongs to another context
- **WHEN** opaque observation, logical page or desired conversation witness differs from the decision's expected context
- **THEN** existing witness guards refuse, and matching fields alone still do not establish actual capture/current-device provenance

### Requirement: Owned resident runtime startup
The Linux resident runtime owner SHALL verify supplied approved artifact bytes, publish one fresh synchronized SDK admission, retain its directly launched child and authenticated connection, and preserve diagnostics under resident-runtime-integration.md. It SHALL use one absolute startup deadline and at most one handshake, close and stop only its owned child on failure/shutdown, retain effect uncertainty, and make no native capability claim from protocol readiness. Stock-service handoff, lazy activation, health/recovery and installed Reader qualification SHALL remain required before production use.

#### Scenario: Owned endpoint becomes ready
- **WHEN** the exact launched child consumes the original admission and completes its single authenticated handshake within the startup deadline
- **THEN** the owner retains that child, process incarnation, directory and connection together; readiness establishes only the protocol connection and grants no page-writing authority

#### Scenario: Startup fails or runtime closes
- **WHEN** artifacts/admission/process identity fail, the child exits, the deadline expires, or the caller shuts down the owner
- **THEN** the connection closes, only the owned child is stopped within a bounded recovery attempt, original uncertainty and admission/diagnostic files remain, and no launch, handshake or native effect is automatically retried

### Requirement: Independent bounded stock restoration
Installed native activation and recovery SHALL share one fixed boot-scoped occupied lease path. A versioned lease SHALL bind a distinct release-approved recovery-profile digest as well as the native profile and adapter identities. The recovery helper SHALL verify its own actual PID1 oneshot process, invocation, executable and populated service group, the unchanged protected installation/profile, and the original terminal Buddy service/group before restoring stock under resident-supervisor-integration.md. Missing, malformed, duplicate, stale or changed evidence SHALL refuse without resetting the activation lease. An unqualified profile SHALL NOT be synthesized from live observations or shipped as approved configuration.

Restoration SHALL issue at most one fixed nonblocking stock start with job-mode=fail per helper attempt, only after zero stock process fields, no job and actual group emptiness are bracketed with unchanged service state. Already active or starting stock SHALL be observed without a new command. Unknown command outcome SHALL retain possible queued-job effects without automatic retry. Success SHALL require stable actual stock process incarnation, executable bytes/argv, group membership/population, loaded policy and no pending job, followed by renewed original Buddy/helper/lease admission within the original deadline. Recovery SHALL NOT kill/restart stock or imply visual readiness or document persistence.

#### Scenario: Conflicting shutdown job arrives
- **WHEN** a conflicting PID1 stop job arrives after the pre-start sample
- **THEN** job-mode=fail refuses replacement, the helper retains the consumed lease and reports failure or uncertainty without a second command

#### Scenario: Installed Buddy recovery trigger can replace pending jobs
- **WHEN** approved or loaded Buddy OnSuccessJobMode or OnFailureJobMode is absent, duplicated or differs from fail
- **THEN** installed admission refuses before stock stop or native launch; trigger targets alone do not grant recovery eligibility
- **AND** unchanged vendor stock modes remain pinned without unit rewriting, and matching Buddy trigger modes alone do not qualify system shutdown behavior

#### Scenario: Recovery starts during original stock shutdown
- **WHEN** an approved stock service is deactivating in a known stop/final substate with the lease's original invocation and last-main PID
- **THEN** recovery waits within its original 120-second deadline, retaining the nonzero systemd start timestamp, and may issue its first start only after that identity is retained or completely cleared in inactive/dead, no process/job remains and the stock group is empty

#### Scenario: Startup uncertainty precedes shutdown
- **WHEN** the helper has already requested a start or observed startup or an unknown pending job before a later shutdown/terminal sample
- **THEN** it never resets the no-retry restriction or issues another start, and partial/changed shutdown identity or deadline expiry also refuses

#### Scenario: Recovery timeout policy differs
- **WHEN** loaded or approved helper TimeoutStartUSec, Buddy WatchdogUSec or stock TimeoutStopUSec differs from the supported 130-second, 120-second and 90-second values
- **THEN** installed admission refuses; matching these values alone does not qualify actual shutdown/startup timing

#### Scenario: Exclusive recovery command on a boot without a recorded activation
- **WHEN** the exclusive recovery command observes only the final activation record absent beneath the unchanged existing protected fixed directory
- **THEN** it returns NoRecordedActivation without configuration, Store, provider, device or service startup, without changing the directory or claiming stock readiness
- **AND** missing parents, any occupied invalid record, symlinks or observation errors remain failures; no outcome resets the activation latch

#### Scenario: Recovery command mixed with ordinary application options
- **WHEN** recovery is requested with another application or maintenance option
- **THEN** argument validation rejects the combination before either operation runs; recovery accepts no arbitrary unit or path override

#### Scenario: Recovery is invoked again after an uncertain start
- **WHEN** the original immutable lease remains valid and stock is already active or starting
- **THEN** the helper verifies or observes stock without another start, and reports success only after the complete stable process/service checks

#### Scenario: Installation or process changes during restoration
- **WHEN** the bound profile, loaded policy, artifact, original Buddy terminal evidence, helper context, or restored stock identity changes
- **THEN** restoration does not report success and neither resets the activation latch nor repeats a native effect

### Requirement: Installed resident session owns stock handoff
The installed caller SHALL compose the protected recovery installation, fixed boot lease, actual Buddy/helper/stock service contexts and resident runtime under resident-supervisor-integration.md. It SHALL arm fatal main-thread health ownership before exclusive lease publication can leave occupied state, issue at most one fixed nonblocking stock stop with job-mode=fail, and launch only after stable original stock termination and recursive group emptiness or qualified deletion. The entire activation SHALL use one at-most-60-second deadline. The session SHALL retain its lease, artifact pins and child, verify child membership before exposing its connection, and permanently fail the actual ordinary runtime on any post-publication failure or session drop. Neither publication, service health, handshake nor caller callback success SHALL establish current page identity or native mutation authority. Product admission and fresh source/cancellation reacquisition remain required.

#### Scenario: Lease publication fails after creating occupied state
- **WHEN** exclusive publication or its closing checks fail without returning a lease
- **THEN** the already-armed health guard forces ordinary runtime exit, leaves the occupied record and diagnostics intact, and issues no stop retry

#### Scenario: Resident session ends while ordinary Buddy remains alive
- **WHEN** the session drops or its validated connection becomes unavailable
- **THEN** its actual health owner fails permanently and the ordinary runtime exits for independent recovery; the session never starts stock from its destructor

#### Scenario: Stock changes during the takeover wait
- **WHEN** a new stock incarnation, changed loaded policy, replaced group or incomplete terminal evidence is observed
- **THEN** the session does not launch or expose native work and any consumed activation remains fatal to the ordinary runtime

#### Scenario: Reloaded terminal dependency lists change textual order
- **WHEN** independently qualified terminal observations differ only in the order of their After or Conflicts dependency lists
- **THEN** the stable-state check accepts the equivalent duplicate-free lists while retaining the original raw evidence and requiring every other sampled field to match exactly
- **AND** missing, added or duplicated dependencies, changed watchdog/runtime state, pending jobs, identity changes or failed original-group proof still refuse admission

### Requirement: Main-thread service health
The installed ordinary Buddy runtime SHALL emit service readiness only after initialization and watchdog notifications only from actual main-thread progress under resident-supervisor-integration.md. Idle input polling, including the ordinary touch fallback, and active request-progress checks SHALL drive those notifications; no independent indefinite keep-alive thread SHALL be introduced. Notification I/O SHALL be nonblocking and errors, owner mismatch or expiration SHALL permanently fail that instance and reach service exit. Existing operation deadlines and input/cancellation semantics SHALL remain unchanged. Service readiness SHALL NOT grant native activation, page identity or write authority.

#### Scenario: Main loop stalls after reporting readiness
- **WHEN** successful progress callbacks stop for the watchdog window
- **THEN** no background worker emits watchdog messages, and a late callback cannot renew the expired health instance

#### Scenario: Idle input continues without a user gesture
- **WHEN** the real main-thread input loop successfully polls without a gesture
- **THEN** it may send a due bounded watchdog notification without manufacturing input, resetting the contact reducer or changing the existing observation deadline

#### Scenario: Notification endpoint fails
- **WHEN** a notification cannot be sent immediately or is attempted by a different process/thread
- **THEN** health failure remains latched and the ordinary runtime exits without retrying notification or reporting native readiness

### Requirement: Explicit developer capture setup
The development-only native capture experiment SHALL follow resident-capture-setup.md. Both controller and observer SHALL end launch input admission before publishing setup-ready, bind setup completion to the original candidate and resident incarnation, and acquire quiet fresh input guards exactly once before one CaptureSource request. Original deadlines, runtime/service checks, whole-source preservation and independent stock-first recovery SHALL remain active. Setup completion SHALL NOT establish Reader identity or installed product readiness.

#### Scenario: Setup completes for a different incarnation
- **WHEN** the setup completion record is stale, replaced, partial or bound to a different candidate, observer or resident process
- **THEN** the experiment aborts without capture, guard renewal, retry or effect replay and independent recovery remains responsible for stock restoration

#### Scenario: Input continues after setup
- **WHEN** either newly acquired input guard observes contact, cancellation or an input error
- **THEN** capture is refused and that guard is never reset or reacquired to make the attempt pass

#### Scenario: Deliberate setup changes protected source bytes
- **WHEN** source inventory differs from the candidate's preservation contract
- **THEN** preservation fails without a directory exemption or success claim, and stock restoration still precedes the decision whether Buddy may resume

#### Scenario: Explicit opening activity allowance
- **WHEN** a version-2 candidate supplies original manifest-bound content/metadata bytes and durable matching setup-ready and ended-admission evidence exists
- **THEN** actor completion and recovery may accept only the typed opening activity changes specified in resident-capture-setup.md, while retaining sampled bytes and checking their inventory correspondence and file pins
- **AND** all protected JSON fields, exact numeric tokens, page order and other file/directory inventory remain unchanged; activity metadata never proves the displayed page

#### Scenario: Missing or invalid setup history
- **WHEN** the opening allowance is requested but setup-ready is absent or its durable history is mismatched, partial or replaced
- **THEN** missing setup-ready leaves byte-exact preservation in force, invalid history refuses the allowance, and recovery restores stock before deciding whether Buddy may resume

## MODIFIED Requirements

### Requirement: Successor navigation and identity heuristic
After agreement, the automatic native acquisition path SHALL first resolve current Buddy-page reuse under buddy-page-reuse-contract.md. A relevant current Buddy page SHALL be reused without a successor navigation attempt. Otherwise the path SHALL retain the ORIGINAL source identity/order, resolve its immediate successor, reuse a qualified relevant Buddy successor, or insert after that original source and before a positively identified non-Buddy successor after fresh placement revalidation. A verified end of document SHALL allow qualified creation after the original source once current-page reuse is ruled out. Unknown recognition/association SHALL not authorize creation. Verified RM2 navigation SHALL use ordered native identity and fresh settled pixels under the reader-responsiveness contract.

The explicitly authorized legacy/manual fallback SHALL retain its one-successor visual heuristic for unsupported layouts and its separately documented REM-25 fallback limits; it SHALL not be represented as the automatic path. Masked screenshot similarity at least0.999 SHALL still identify unchanged pages. Neither failure nor refusal SHALL draw source feedback.

#### Scenario: Automatic end of document
- **WHEN** qualified current-page assessment rules out reuse and verified native order has no successor after the original source
- **THEN** the automatic path may create after that source under the native creation/identity/preservation gates; a callback alone does not establish a usable target

#### Scenario: Legacy fallback has no successor
- **WHEN** the selected legacy/manual fallback has no known successor or its next-page attempt leaves the screenshot sufficiently similar to the source
- **THEN** no answer is written and a non-ink NoSuccessor diagnostic is recorded without creating a page or swiping backward

#### Scenario: Physical gesture and completion
- **WHEN** navigation requires a swipe
- **THEN** ordinary product gesture timing remains15 steps at10ms after50ms initial contact; verified-layout completion uses correlated state, while unsupported layouts retain documented legacy waits without verified-layout claims

### Requirement: Invalid successor recovery
In the automatic path, a positively identified non-Buddy successor SHALL be preserved and may permit qualified insertion between the ORIGINAL source and that neighbor after current source/session/order revalidation. An unknown/uncertain successor or recognized Buddy candidate with unresolved association SHALL grant no insertion permission. If restoring the original displayed source is required, recovery SHALL check source identity before navigation, attempt at most one previous-page swipe and verify once; any failure SHALL stop without retry or relocating the insertion anchor.

In the explicitly selected legacy/manual fallback, an Invalid successor SHALL retain the existing source precheck and bounded return behavior: if already on the saved source at similarity0.999, do not navigate; otherwise attempt at most one previous-page swipe and verify once, with no retry after failed verification or input/capture error. The caller SHALL record a non-ink typed failure after recovery or recovery failure, with no source-page display mutation. Legacy Invalid classification alone SHALL not authorize automatic insertion. Source: src/workflow/navigation.rs and the planned automatic acquisition contract.

#### Scenario: Automatic inspection finds an ordinary neighbor
- **WHEN** the inspected successor is positively non-Buddy and original source/session/order remain qualified immediately before publication
- **THEN** the automatic path may insert before that preserved neighbor under the native contract instead of treating it solely as a legacy InvalidSuccessor failure

#### Scenario: First return fails
- **WHEN** the single previous-page swipe does not restore source similarity
- **THEN** recovery reports Unconfirmed and the caller records Device without another swipe or insertion

#### Scenario: Already on the source
- **WHEN** recovery's initial check matches the saved source, including a forward attempt that did not leave it
- **THEN** recovery reports AlreadySource with no previous-page swipe
- **AND** the legacy forward no-movement guard records NoSuccessor without invoking reverse recovery at end of document

#### Scenario: Successful return
- **WHEN** the source is initially absent and the single previous-page swipe restores it
- **THEN** recovery reports Returned after one precheck, one swipe and one postcheck; an automatic insertion still requires its separate qualified acquisition and placement checks

#### Scenario: Navigation or capture error
- **WHEN** a source-identity check or the previous-page operation returns an error
- **THEN** recovery propagates that error and performs no further navigation or insertion; the render-error handler records Device without feedback input
