# tablet-io

## Purpose

Describe the implemented tablet io contracts, initially baselined from v0.1.4. Known gaps are explicit and require a later change delta to alter.
## Requirements
### Requirement: Device selection
The system SHALL detect RM2 from reMarkable2 1.0 and Paper Pro from ferrari 1.0 in /etc/hwrevision; other values SHALL select Unknown with legacy RM2 defaults in device implementations. Source: src/device/mod.rs; src/device/{screenshot,touch,pen}.rs.

#### Scenario: Linux input selection
- **WHEN** RM2 is detected
- **THEN** pen input uses /dev/input/event1 and touch uses /dev/input/event2.
- **AND** Paper Pro instead selects event2 for pen and event3 for touch.

### Requirement: Screenshot layout and ambiguity handling
RM2 SHALL select four-byte BGRA for IMG_VERSION major/minor at least 3.24 and the legacy two-byte layout otherwise. Missing or malformed RM2 version fields SHALL error. Capture SHALL read xochitl process memory and reject missing or ambiguous modern RM2 allocations. Source: src/device/screenshot.rs rm2_uses_bgra/find_rm2_bgra_allocation/take_screenshot.

#### Scenario: Modern RM2 allocation
- **WHEN** modern RM2 capture searches anonymous writable mappings
- **THEN** it searches page-aligned addresses where the complete allocation fits, requires exactly one matching 32-bit mmap allocation header for 1404 by 1872 by four bytes, and reads pixels after the eight-byte header.

#### Scenario: Merged memory mappings after restart
- **WHEN** a valid framebuffer allocation is inside a merged anonymous mapping rather than at its start
- **THEN** discovery finds its validated header without a fixed address or historical-offset fallback.
- **AND** missing, malformed, truncated and multiple matching allocations are not accepted as a unique framebuffer.

#### Scenario: Native detail and overview
- **WHEN** modern RM2 pixels are encoded
- **THEN** neutral-preserving luminance from the BGR channels supplies full-range grayscale in portrait 1404 by 1872 without legacy rotation, retaining text contrast in colored highlights.
- **AND** the API provides a 768 by 1024 overview plus three overlapping full-width native-detail strips.

#### Scenario: Legacy and Paper Pro branches
- **WHEN** another implemented capture branch is selected
- **THEN** legacy RM2 uses its existing conversion/rotation/flip and Paper Pro uses its existing four-byte 1632 by 2154 path.
- **AND** presence of these paths does not establish hardware compatibility for every firmware.

#### Scenario: Colored highlighter pixels
- **WHEN** modern RM2 native pixels contain a yellow highlight over printed text
- **THEN** grayscale conversion uses (77R+150G+29B+128)>>8, preserving neutral values exactly and keeping yellow background lighter than black text.

### Requirement: Corner hold trigger
The shared history-capable input path SHALL recognize one stationary contact in the configured 68-pixel corner region of the virtual 768 by 1024 screen after a continuous two-second hold and full release. The legacy fallback SHALL retain its slot-zero two-second trigger. Both paths SHALL evaluate complete input frames and support stationary holds without new position events. Reader admission SHALL use guarded conditional overlay dismissal instead of an unconditional tap. Source: src/device/interaction.rs; src/device/native_history.rs; src/device/touch.rs; src/device/trigger_dismiss.rs.

#### Scenario: Stationary hold
- **WHEN** a valid single contact stays in the selected corner for two seconds and releases
- **THEN** the shared path recognizes Reader once without requiring movement; a positively absent overlay receives no tap, a qualified known panel receives one guarded outside-panel tap, and unknown or failed dismissal stops admission.

#### Scenario: Contact ends or exits
- **WHEN** contact ends before two seconds or its complete frame leaves the trigger region
- **THEN** the hold is canceled and a later valid hold starts fresh.

#### Scenario: Legacy fallback
- **WHEN** the shared native history observer is unavailable
- **THEN** the existing slot-zero polling trigger remains available at its two-second threshold, without native history ownership; this does not bypass conditional dismissal checks.

### Requirement: Coordinate and output assumptions
Input and workflow operations SHALL use virtual portrait coordinates 768 by 1024 with device-specific transformations; RM2 touch Y is inverted and Paper Pro touch is directly scaled. Pen and keyboard output SHALL use Linux input injection, not direct native document edits. Source: src/device/touch.rs virtual_to_input; src/device/pen.rs; src/device/keyboard.rs.

#### Scenario: Body text output
- **WHEN** a Q&A is written
- **THEN** the keyboard selects body style with Ctrl+3 and emits supported character key events, including the special caret handling in string_to_keypresses.

#### Scenario: Coverage boundary
- **WHEN** assessing compatibility
- **THEN** the recorded RM2 3.28.0.172 portrait evidence is distinguished from untested human gestures, other orientations, reboot behavior and Paper Pro hardware; non-Linux stubs are not a faithful simulator.

### Requirement: Deterministic hold timing
Hold timing SHALL be isolated from Linux polling so contact loss, leaving/reentering, stationary timeout and release ordering can be tested without device access. The two-second threshold SHALL remain unchanged. Source: src/device/touch.rs; src/device/interaction.rs.

#### Scenario: Interrupted hold
- **WHEN** contact exits the zone or ends before timeout
- **THEN** its elapsed time is discarded and the next valid hold starts fresh.

#### Scenario: No movement required
- **WHEN** a valid contact remains stationary until the threshold
- **THEN** no new position event is required for qualification; the shared path emits Reader on full release, while the legacy timer retains threshold activation.

### Requirement: History interaction events
While awaiting the next Reader action, tablet input SHALL recognize stationary four-contact holds of two seconds as undo and two-contact holds of two seconds as redo. Recognition SHALL use complete contact frames and stable tracking identities, emit once per hold, and require complete release before another action. The existing single-contact corner hold SHALL still initiate Reader. Departure or editing events SHALL invalidate history ownership without concurrent device input. Source: src/device/touch.rs event reducer and src/device/backend.rs idle interaction boundary.

#### Scenario: Four-contact hold
- **WHEN** four stable contacts remain stationary for two seconds
- **THEN** one undo event is emitted; transitional two-contact formation does not emit redo.

#### Scenario: Two-contact hold
- **WHEN** two stable contacts remain stationary for two seconds
- **THEN** one redo event is emitted without an additional conflicting native edit.

#### Scenario: Short or interrupted gesture
- **WHEN** a contact releases, moves, changes tracking identity or changes count before the threshold
- **THEN** no undo/redo event is emitted from the incomplete hold.

#### Scenario: Held contact and rearm
- **WHEN** a qualifying hold continues beyond two seconds
- **THEN** it does not repeat until all contacts have been released and a new qualifying hold begins.

#### Scenario: No history
- **WHEN** an undo/redo gesture occurs without a valid corresponding history state
- **THEN** Reader performs no text mutation and no model request.

#### Scenario: Corner release opens native menu
- **WHEN** a single contact qualifies for Reader and is subsequently released
- **THEN** the shared input path emits Reader once after release, so menu dismissal follows the native release action; no capture begins while the trigger is still held.

#### Scenario: History observer unavailable
- **WHEN** the native history observer cannot initialize
- **THEN** history is discarded and disabled for the process, while the ordinary Reader trigger remains available without a restart loop.

### Requirement: Equivalent direct capture pixels
Screenshot normalization SHALL preserve exact decoded pixels, dimensions, orientation, luminance and nearest-neighbor overview sampling for every implemented format while avoiding unnecessary PNG encode/decode work. Status observation MAY consume a fresh image directly without serializing native/overviewPNG. Discovery ambiguity, invalid-length and owner/session checks SHALL remain enforced, and frames SHALL NOT be reused across mutation boundaries. Source: REM9; src/device/screenshot.rs and backend.rs.

#### Scenario: Direct status image
- **WHEN** fresh status pixels replace the prior serialization path
- **THEN** exact normalized pixels match the prior codec pipeline and identity is checked around that observation before any dependent input.

#### Scenario: Format equivalence
- **WHEN** modern RM2BGRA, legacy RM2 or PaperProRGBA is processed
- **THEN** exact legacy conversion/rotation/flip, colored luminance and alpha/nearest sampling are preserved; software equivalence does not claim native PaperPro timing validation.

### Requirement: Preserve the selected drawing tool
Automatic drawing SHALL preserve the user's selected pen, slot, color and width.
It SHALL NOT simulate menu presses to select or inspect drawing tools. A future
selection mechanism requires evidence of a robust supported direct interface.
Normal status and failure ink SHALL be retired entirely. Legacy diagnostic-only
marks SHALL be suppressed before input when fresh
non-mutating observations cannot establish a visible, bounded, safely erasable
current tool. Saved preferences alone SHALL NOT establish actual tool state.
Normal Q&A SHALL remain available when optional feedback is suppressed.

#### Scenario: Supported current pen
- **WHEN** the current pen is positively recognized and its full supported width range fits the verified blank footprint and cleanup envelope
- **THEN** normal Reader emits no feedback ink; explicitly invoked historical diagnostic marks, if retained, use that pen and slot with zero tool-selection presses and all ownership/journal/neighbor-ink checks enforced.

#### Scenario: Unknown or unsuitable current tool
- **WHEN** the toolbar is unknown, the tool is destructive, or visibility/maximum footprint/cleanup coverage is unproven
- **THEN** optional ink is suppressed without opening menus or changing settings; Q&A continues and the missing visual feedback is reported honestly.

#### Scenario: Unsafe cleanup or external change
- **WHEN** owner, content, input activity, controls or cleanup postconditions change after owned ink begins
- **THEN** further mutation fails closed and recovery evidence is retained; the implementation never broadens erasure to hide the failure.

#### Scenario: Uncalibrated notes toolbar
- **WHEN** a notes/blank page toolbar or other layout differs from the calibrated PDF annotation toolbar
- **THEN** optional ink is suppressed before journal creation or drawing, without changing tools or blocking core Q&A; the reduced feedback coverage is explicit.

#### Scenario: Trigger release does not navigate menus
- **WHEN** a Reader trigger qualifies
- **THEN** the workflow must not navigate menus; the proposed removal of the automatic bottom-center tap requires native trigger/overlay verification. A necessary verified non-menu tap remains allowed, and subsequent operations retain their ownership checks.

#### Scenario: Known trigger overlay needs an outside dismissal
- **WHEN** a released Reader trigger leaves the positively qualified overflow panel visible
- **THEN** one guarded tap outside every menu item may dismiss it, followed by fresh unchanged-owner/tool/native-content and panel-absence verification; no menu item is selected.

#### Scenario: Missing or unknown trigger overlay
- **WHEN** the trigger overlay is positively absent or its layout cannot be qualified
- **THEN** absence emits no dismissal input, while unknown layout fails closed; no guessed or repeated tap occurs.

#### Scenario: Discovery candidate vanishes during trigger observation
- **WHEN** a trigger observation fails with the typed verified-unmapped discovery-header EIO
- **THEN** at most one complete fresh read-only retry is allowed within500ms and the overall5s dismissal deadline, with the same retained input observer and unchanged pinned owner/session/native bytes; all other errors or guard changes refuse, and no tap is repeated.

### Requirement: Experimental capture has exact process provenance
The experimental RM2 capture path SHALL bind an explicit boot ID, PID and process start identity and SHALL refuse identity changes, changed headers, or violations of its selected required-mapping closure before accepting pixels. It SHALL NOT rediscover a different process by name after binding. Unrelated process mapping changes alone SHALL NOT invalidate a separately reviewed scoped closure.

#### Scenario: Bound process is replaced
- **WHEN** the PID start identity or boot differs at any capture boundary
- **THEN** capture refuses and publishes no image or cached output

### Requirement: Ambiguous allocation discovery preserves bounded evidence
RM2 allocation discovery SHALL retain bounded selected-identity, map and matched raw-header evidence. Without separately qualified native backing attribution, zero or multiple heuristic matches SHALL refuse capture. Malformed evidence or scan-cap exhaustion SHALL always refuse capture; no ordering, cached address or image resemblance SHALL select a match.

#### Scenario: Two allocations have the expected header
- **WHEN** two matching allocation headers are discovered
- **THEN** bounded match evidence is retained and no pixels are accepted without separately qualified native backing attribution

#### Scenario: Discovery reaches a bound
- **WHEN** the maps, scan or evidence cap is exceeded
- **THEN** discovery is explicitly incomplete and refuses rather than treating a partial scan as unique

### Requirement: Selected resident source handoff owns released input and session
An explicitly selected installed resident source route SHALL follow
resident-source-handoff.md. Source-only selection activates on the first
qualified release. The pinned installed native output profile can activate
once at service startup under the recovery policy. Either route SHALL use
qualified release without legacy dismissal or Touch fallback, one retained
Session, guarded post-activation Observe/CaptureSource, and one original
request deadline. Selected failure SHALL NOT downgrade to legacy capture
or retry effects. Historical facts and images SHALL NOT grant native output
or blank-start authority.

#### Scenario: A held contact is returned by the old trigger fallback
- **WHEN** a selected route lacks its own released/quiescent observer handoff
- **THEN** no Session factory, native request, dismissal input or provider call occurs

#### Scenario: A later distinct released request follows completed capture
- **WHEN** the retained Session remains valid and fresh input/installed admission succeeds
- **THEN** the same native child is reused with one explicitly selected reconnect, rather than another activation or replay of the old request

### Requirement: Resident polling separates pulses from fresh admission boundaries
Read-only resident source and visual routes SHALL follow resident-admission-progress.md. Internal command and mailbox polling SHALL use cheap deadline/input/health/lease/file/known-child/group pulses without recursively launching PID1 or broker observations. Fresh complete service/broker boundaries SHALL gate native request dispatch and reply/delivery, and marker acceptance/admission. PID1 batching SHALL preserve existing complete Snapshot, policy, incarnation, job and group bracket predicates and output bounds. A CLOSED read-only enum/dispatcher SHALL expose no generic action or mutable-connection escape; existing effectful/Reconcile and unresolved-journal guards SHALL remain unchanged. Real Session full delivery admission SHALL run after stored readback/encoding/payload assembly and before clearing the original acquisition deadline. Cheap retained Reader/companion, lease, file and group checks SHALL also run during provider progress and actual idle polling; ownership loss SHALL poison the health owner and refuse subsequent work. No cached success, budget increase or weaker effectful/recovery admission SHALL replace these checks.

#### Scenario: Broker response needs many pipe polls
- **WHEN** one bounded read-only broker query requires additional internal pipe polls
- **THEN** cancellation and identity pulses continue under the original deadline without multiplying full service/broker subprocess observations or authorizing stale dispatch/delivery

#### Scenario: A marker arrives after a service or owner changed
- **WHEN** a mailbox marker or native reply arrives after a required service, broker or known ownership identity changed
- **THEN** its current full boundary refuses onward admission/delivery without retry, fallback, deadline renewal or effect authority

#### Scenario: A retained native child dies during provider work or idle wait
- **WHEN** the owned Reader or companion loses its admitted live identity while a provider request or actual idle Reader poll runs
- **THEN** the cheap real Session pulse poisons the health owner and refuses later delivery/new requests without healthy-watchdog continuation, PID1/broker poll amplification, restart or replay

#### Scenario: Full delivery admission fails after payload preparation
- **WHEN** stored readback, encoding or model-payload construction is followed by changed service/broker ownership or original acquisition expiry
- **THEN** the real Session full boundary refuses the first provider admission before the original deadline is discharged, even if input and health checks alone succeed

### Requirement: Native output persistence is verified independently

Qualification SHALL distinguish rendered ink from saved native output. A fresh
stock Reader instance SHALL reopen the intended saved target and corroborate
its visible content while the original page order, annotations and document
bytes are independently compared. The ordinary user close action MAY serve
as a qualification boundary. The runtime SHALL NOT require a developer
close or reopen command after each answer.

#### Scenario: Rendering succeeds before stock restoration

- **WHEN** the resident Reader displays output on the intended page
- **THEN** the output is credited as persisted only after saved target data and fresh stock reopen agree
- **AND** the original source and neighboring page assets remain unchanged
