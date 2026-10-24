## ADDED Requirements

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

### Requirement: Experimental native-backed acquisition hands off owned bytes
A separately selected native-backed experimental producer SHALL acquire one exact RGB32 portrait plane through one held process memory handle between fresh native tuple/header and process/map checks. Only a complete bound frame with producer exit zero SHALL be accepted for pure native/overview PNG conversion. The converter SHALL NOT reopen process memory or infer native authority from conversion alone. Failed, short, extra, stale or mismatched framing SHALL publish no accepted image.

#### Scenario: Producer closes successfully
- **WHEN** exact selected nonce/process/boot, supported layout, both native tuples/headers, full plane and terminal framing agree and the producer exits zero
- **THEN** both PNG views derive from those same owned bytes, preserving sampled lifetime/coherence limits

#### Scenario: Closing evidence or frame is incomplete
- **WHEN** producer exit, framing, selected identity, tuple/header equality, layout or exact byte length fails
- **THEN** conversion/admission refuses without using prior cached pixels or an alternate allocation

### Requirement: Scoped native capture closes every depended-on range
The selected experimental scoped producer SHALL freeze bounded dependencies from initial native tuple/header validation for every actual memory read and every validated object, code, GOT, vtable, slot, global, BSS anchor, header, full allocation and pixel interval. Each of the same three map checkpoints SHALL parse a fresh bounded sorted non-overlapping table and require unique single-VMA coverage of every dependency. Required mapping permissions, device, inode, file offset, path and boundaries SHALL remain exact, except a baseline private `rw-p` anonymous `[heap]` with zero device/inode/offset MAY keep its exact lower boundary and monotonically extend its upper boundary while retaining its entire original extent and every dependency. Each newly added heap interval from the preceding accepted upper boundary to the new upper boundary SHALL be disjoint from every other preceding parsed VMA, refusing absorption of a previously mapped neighbor even if that neighbor disappears. A decrease against either initial or preceding accepted checkpoint, lower-bound change, split, lost coverage, changed attributes or ambiguous interval SHALL refuse.

The producer SHALL retain exact complete map-row sets, including observed absence, for the selected executable, Qt native backends and selected mapped runtime provider paths and aliases. Later range checks and closing ELF/inode provenance validation SHALL use the fresh validated table. Post-freeze reads or validations outside frozen dependencies SHALL refuse. Disjoint map differences MAY be admitted only after the complete fresh parser passes bounds, order, overlap and checked interval arithmetic. This closure SHALL NOT add process-memory or map reads, plane retries, address-selection alternatives, or lifetime/atomicity claims.

#### Scenario: Containing heap extends without changing required coverage
- **WHEN** the same verified private heap grows only at its upper boundary, monotonically, with all attributes, original extent and required intervals preserved, and all other closure checks pass
- **THEN** that boundary change alone does not refuse the scoped producer

#### Scenario: Required mapping or provider changes
- **WHEN** a required mapping loses coverage, changes an unadmitted boundary or attribute, becomes split or ambiguous, or a selected provider map-row set changes
- **THEN** the producer refuses with no accepted frame, navigation or creation

#### Scenario: Unrelated mapping changes
- **WHEN** disjoint rows change while the complete fresh map parser and every frozen dependency/provider closure pass
- **THEN** whole-process map text inequality alone does not refuse the scoped producer

### Requirement: Consumer binds scoped producer authority
The host SHALL select the reviewed scoped closure version through exact source/artifact bindings and accept only producer exit zero, empty stderr and the existing complete bound envelope after all producer closing checks. Public conversion SHALL remain pure and infer no native authority. Bounded wrapper map snapshots SHALL remain contextual evidence, not an independent whole-process equality gate under the scoped contract. All existing frame/hash/converter/receipt/image, provider-hash, identity, deadline, idle, visual, recovery and no-input-on-failure gates SHALL remain enforced.

#### Scenario: Producer refuses scoped closure
- **WHEN** the selected producer returns a failure, partial output or diagnostic stderr
- **THEN** conversion, navigation and creation remain unadmitted, and the attempt remains spent even if provisional tuples match


### Requirement: Visual readiness observations remain bounded and failure-terminal
The experimental host MAY perform at most three distinct successful ready captures within the original fixed ready deadline, each with an exclusive claim and complete identity, waiting/window/expiry, released-input and hash evidence. The first complete ready observation SHALL freeze nonce, boot, PID/start, root inode, original window and waiting expiry even if its pixels do not match; later observations SHALL retain that binding. Every observation SHALL be recorded and pass host admission/idle checks before a further request. Exact approved Library pixels SHALL remain required before the single ordinary opening gesture. Ready attempt prefixes SHALL be limited to host-ready-000..002 and opening attempts to host-open-000..004, with counts including failed attempts. A complete nonmatching image, without an inferred loading/modal classifier, SHALL remain unready evidence; any acquisition, conversion, mapping, identity, input, hash, transport or partial-response failure SHALL terminate rather than retry. At most five opening captures plus trigger/result SHALL preserve ten captures total. No output reuse, fixed-delay readiness assumption or deadline renewal is permitted.

#### Scenario: Loading becomes the Library under the fixed deadline
- **WHEN** one complete bounded ready image is loading and a later distinct complete observation matches the Library with all unchanged admission gates
- **THEN** only the matching fresh observation may admit the single ordinary opening gesture

#### Scenario: Fault or readiness cap is reached
- **WHEN** any observation fails a required gate or the fixed time/count allowance ends without the approved Library
- **THEN** the host admits no opening or creation and preserves spent evidence for independent recovery

### Requirement: Capture response and hash verification preserve existing bounds
The host SHALL bound response completion by both a maximum of 20 seconds and conservatively computed remaining fixed stage time using fresh remote uptime and a host monotonic anchor established before the query. Unknown or exhausted time SHALL refuse. Complete remote closing identity/expiry and host admission checks SHALL remain mandatory; partial transport output SHALL never be accepted or replayed. Exact before/after native/provider hash checks MAY be batched only through the independently bootstrapped reviewed bounded launcher and verified hash tool, with complete bounded ordered expected path/digest comparison and no omitted checkpoint or input bytes.

#### Scenario: Batched hash output is incomplete or wrong
- **WHEN** a batch has nonzero status, missing/duplicate/reordered/changed path or digest, malformed bytes or exceeded output/time bound
- **THEN** capture refuses before navigation or creation even if pixels match

### Requirement: Snapshot preparation preserves pins and brackets sidecar identity
The experimental snapshot consumer MAY batch the existing exact three encoder/provider and six helper path hashes through the independently bootstrapped existing three-second launcher. All original file identity checks SHALL remain and the complete exact ordered nine-line output SHALL match the expected paths and digests with zero exit and empty stderr. Each distinct snapshot SHALL own exclusive private stdout/stderr records bounded to 2048 bytes each. The two native/provider hash checkpoints SHALL remain unchanged. Non-snapshot action preludes SHALL retain their current checks. Additional evidence SHALL remain within the existing ten-snapshot storage allowance.

The initial live content/metadata hashes, copies and copied-byte hashes SHALL precede the complete released-input observation and plane read. Fresh live content/metadata closing hashes SHALL follow the plane and equal both the initial and copied digests. Immutable-file closing checks and final identity/window/expiry admission SHALL remain after capture. Every prefix SHALL use fresh sidecar evidence. This interval SHALL NOT establish atomicity, render readiness or native lifetime authority.

#### Scenario: Prelude batch or bracketed sidecar changes
- **WHEN** bootstrap, exclusive output, exact ordered hash output, exit/stderr/cap, copied sidecar identity or fresh live closing sidecar identity fails
- **THEN** the observation refuses terminally without navigation, creation, cached evidence or replay

#### Scenario: Snapshot preparation completes
- **WHEN** every same-pin prelude batch and initial/copied/closing sidecar equality passes within the unchanged stage deadline
- **THEN** only the complete capture may proceed to existing identity, idle and exact visual admission; preparation does not itself prove Library readiness

### Requirement: Explicit production timing variant preserves fixed authority
A separately selected production v2 SHALL bind candidate-relative ready45/open75/trigger90/result115/stop125/candidate130, start reserve315, absolute360 and recovery185. Original SDK setup95 SHALL anchor once to constructor BOOTTIME; acceptance before original expiry SHALL grant exactly one independent five-second access interval. Legacy40 and observation-only configurations SHALL retain their existing semantics. Purpose/profile/source/artifact mismatches SHALL refuse.

Publication SHALL require full12 seconds remaining in both trigger and original SDK setup intervals at RPC entry after all query/staging costs, and final commit SHALL independently require candidate remaining40, absolute remaining225 and the complete remaining candidate interval plus185. Action caps SHALL remain ready3/GO3/publication12; original setup/contact leases SHALL never renew. Complete query/transport/decode/retention costs SHALL consume fixed stage bounds. Result115 SHALL cover all asynchronous acceptance/access/poll/capture costs together; stop125 SHALL retain independent actor130 recovery. Partial, late or uncertain actions SHALL never replay. Selected production negative closure predicates SHALL refuse regular files, directories and dangling symlinks explicitly.

#### Scenario: Narrow volatile Library bar differs
- **WHEN** an otherwise exact approved768x1024 Library differs only within half-open battery charge-bar rectangle(735,30,737,36) under explicitly selected v2
- **THEN** the comparison reports masked_match separately from whole_image_exact, retains raw pixels/full differences and grants no exemption to any other pixel or source/footer/result predicate

#### Scenario: Late publication or result work
- **WHEN** fresh admission lacks the full publication reservation, original expiry/reserves fail, or any response/decode/retention crosses its fixed bound
- **THEN** the operation refuses without lease renewal or action replay and independent recovery remains available

### Requirement: V2 ordinary opening tap requires coordinate-complete evidence

The explicit v2 library tap SHALL use exactly one preselected canonical library_tap_variant, primary-1641396 or alternate-2011360, bound equally in selection/profile/preparation receipt. Missing, unknown or conflicting variants SHALL refuse without a default or transport action. Each variant SHALL map to its exact explicit command and fixed native point and require stable fully released fresh setup/post-GO/post-intent seed observations with both slot0 axes different from that point before the sole DOWN write. The first DOWN SYN frame SHALL include exact tracking ID and both selected axes to earn successful tap evidence. Missing axes SHALL preserve conditional exact-owned release/recovery but SHALL NOT grant success, automatic switching or replay. Legacy and close routes SHALL retain their existing contracts. Strict policy SHALL derive from the v2 command context, not coordinates shared with legacy. Exact source/artifact bindings and all fixed input, timing, recovery and visual/source gates SHALL remain mandatory. The owning tap-coordinate-contract.md and forward wrapper-boundary-contract.md specify scope and fault controls; kernel echo does not acknowledge application delivery or opening.

#### Scenario: Cached axis or incomplete first frame refuses successful tap
- **WHEN** either cached slot0 axis equals the selected v2 point, the seed drifts, or the first DOWN SYN frame lacks either exact coordinate
- **THEN** no successful tap is admitted, no action is replayed and conditional exact-owned release and independent recovery remain available

### Requirement: Exact v2 publisher arguments cross the bounded launcher

The selected launcher SHALL retain legacy eight publisher arguments and admit nine only with the exact final open-document-insertion-v2 token. It SHALL preserve the original same-PID execution and three-second own alarm, all other argument grammars and their existing alarms. Unknown, missing or extra purpose/arguments and relative publisher paths SHALL refuse before child execution. Exact source/artifact pins and executed real rendered-wrapper controls SHALL qualify this seam before fresh selection; direct publisher tests alone SHALL NOT establish wrapper compatibility. No launcher retry, fork, shell or timing renewal is permitted.

#### Scenario: V2 arguments reach selected child while an unknown ninth argument refuses
- **WHEN** the exact selected v2 rendered invocation crosses the reviewed launcher, or its ninth argument is replaced by an unknown value
- **THEN** the valid invocation preserves all arguments, PID and original alarm and the invalid invocation refuses before child execution without replay

### Requirement: Known pending Library never grants source authority
Explicit production v2 MAY classify a complete pre-footer opening observation as UNREADY only when every pixel matches the approved Library without an exclusion, exact seven-page/current-source0 metadata and both raw sidecar hashes match the accepted pre-tap Library baseline, and both observations contain exact canonical-empty raw LastOpen bytes. NormalizedNone SHALL NOT substitute for raw-byte equality. Existing capture/provenance/identity/original SDK-unarmed/expiry/fixed OPEN75/count/decode/retention gates SHALL remain mandatory. The baseline SHALL bind at accepted Library, not loading.

#### Scenario: Ordinary opening is still at Library
- **WHEN** a complete v2 observation before any footer satisfies every narrowly defined pending-Library condition
- **THEN** it is retained as UNREADY and consumes one existing MAX5 opening attempt, allowing only another fresh bounded read-only observation without tap/GO replay, count/time renewal, footer/body acceptance or creation permission

#### Scenario: Pending Library cannot be admitted
- **WHEN** any condition is unknown, malformed or mismatching, the original count/deadline is exhausted, or Library returns after a footer
- **THEN** the attempt refuses terminally and preserves recovery; strict selected-document/footer context and a later distinct loaded-body frame remain required before any creation publication

### Requirement: Visual timing diagnostic has no insertion authority
A selected `open-document-readiness-observation-v1` purpose SHALL use the unchanged original SDK configuration and reviewed capture path through a distinct diagnostic entry point. Opening, GO and creation-arm publication SHALL refuse this purpose before any state change or transport. A diagnostic image SHALL NOT satisfy production ready20 or fall through to insertion. At most three distinct attempted full-idle observations SHALL use fresh diagnostic prefixes and remain within existing read/memory/storage caps.

The fixed diagnostic cutoff SHALL be the minimum of candidate-start plus40 seconds, original waiting expiry, original actor observation end and original absolute deadline minus185 seconds, floored for integer shell gates. All fresh complete response/admission and original capture phase margins SHALL fit strictly before that cutoff. Both diagnostics.json and callback.json SHALL be absent before each frame and at closing; original closing/restoration/stop markers and all capture provenance checks SHALL remain mandatory. Any failed or uncertain operation SHALL be terminal. Exact Library pixels, count/cutoff exhaustion or fault SHALL cause immediate guarded stop with unchanged independent recovery.

#### Scenario: Diagnostic observes Library
- **WHEN** a complete provenance-valid diagnostic image exactly matches the approved Library pixels within its original fixed diagnostic interval
- **THEN** the host reports the actual observation and candidate-relative recorded phase/completion times, requests stop and grants no opening or creation permission

#### Scenario: Diagnostic cannot complete safely
- **WHEN** identity, original expiry, terminal markers, full idle, hash/map/frame/receipt, phase bounds, complete transport or diagnostic cutoff fails
- **THEN** no further capture or mutation is admitted, failed output is preserved without replay, and independent recovery remains available

### Requirement: Exploratory relative movement preserves fixed path and conditional ownership
A separately selected development-only relative gesture SHALL reuse the existing fixed-height SDK swipe and one tagged direct writer child under the ownership/context/deadline contract in relative-gesture-contract.md. Every event batch including final UP SHALL check scoped ownership. The original strict Library tap lane SHALL remain unchanged. Initial unchanged Y SHALL be admitted only from an exact freshly revalidated seed equal to transformed y512 and reported as seed-carried evidence; initial tag/X SHALL still require first-SYN echo. Raw progression and per-step durable intent SHALL bound conditional recovery. Normal writes SHALL expire at original GO+1500ms, recovery at GO+2500ms and all response work at GO+5000ms; no renewal is permitted. Recovery SHALL inject UP only after proven writer death and positive exact-contact evidence. UI destination SHALL be verified independently before any further movement.

#### Scenario: Start is refused or writer cannot be fenced
- **WHEN** start context fails or the direct writer cannot be confirmed dead within the original recovery cutoff
- **THEN** no unauthorized UP or replay occurs and unresolved ownership is retained

#### Scenario: Fixed-height Y is suppressed
- **WHEN** first DOWN has exact fresh tag/X and Y is absent but the bound stable released seed already equals the exact transformed y512
- **THEN** evidence reports seed-carried Y without claiming GUI delivery, and only independent fresh page/pixel observation can qualify navigation

#### Scenario: Saved selection and pixels disagree
- **WHEN** fresh current-page evidence and rendered pixels disagree after a movement
- **THEN** the attempt ends without automatic corrective movement, restart qualification or direct native page opening

For an explicitly sealed development navigation_policy=stop-at-declared-neighbor-v1, after positively observed owned DOWN the exact intended neighbor in either field of either fully valid existing context sample SHALL terminally stop normal emission. Parent or typed worker terminal detection SHALL grant no further MOVE or normal UP. Only confirmed exact-child death and existing positively owned bounded conditional release may yield released-after-target-observation-ui-unverified with trajectory_complete=false. Both context samples, inventory/session/input and retained prefix SHALL remain validated; unknown overrides target evidence and forbids release. Source-only raw drift SHALL not become an expected transition. Independent exact destination/order/pixels remain required; completed trajectory or synchronous in-motion content/metadata updates SHALL not be required for this selected outcome. Missing/conflicting policy, lost terminal evidence or expired release SHALL not qualify. Prior freezes and failed trials SHALL retain their original semantics.

The helper's original GO+1500/2500/5000 limits SHALL bound normal input, recovery and helper response/evidence. The development operator's separate one-shot post observation SHALL retain its existing20-second transport bound starting at post invocation; it SHALL NOT be described as a GO+5000 destination deadline or new motion authority. No additional GO-anchored post-admission gate currently exists. Future same-candidate insertion SHALL retain its original stricter candidate-relative admission/capture limits through separately assessed integration.

#### Scenario: Owned navigation begins before both page files agree
- **WHEN** both existing samples remain fully valid within the sealed source/neighbor pair and a neighbor field is observed after positive owned DOWN
- **THEN** normal emission terminates, the exact writer is fenced, only positively owned conditional release is admitted, and destination remains independently unverified

#### Scenario: Target evidence is accompanied by unknown ownership
- **WHEN** either sample or a subsequent release guard identifies an unknown page, changed document/order/session or uncertain/foreign input
- **THEN** target evidence does not override the sticky failure, no uncertain UP or expected-release qualification is granted, and the selection is not replayed

### Requirement: Fresh eight-page trials preserve the successful inserted page
The explicit preserved-eight-after-9005 selector SHALL bind the exact approved eight-page order, matching SDK configuration/profile/receipt and28 protected paths under preserved-eight-fixture-contract.md. Existing Legacy behavior SHALL remain unchanged. Only the two document sidecars SHALL be mutable; the26 immutable records SHALL include the preserved inserted page. Hash launcher r5 SHALL accept at most26 exact absolute paths under its unchanged own alarm3, and reject27 before execution. Fresh nine-page result and actual UI SHALL be reconciled independently; callback alone SHALL NOT acknowledge rendering.

#### Scenario: Preserved page or selector binding changes
- **WHEN** the existing inserted page, exact order/path set, inventory selector or SDK/header/profile/receipt binding differs
- **THEN** the fresh trial refuses before input/publication without rolling back or deleting the successful page

#### Scenario: Hash count exceeds the reviewed seam
- **WHEN** a hash invocation supplies27 paths or an invalid absolute path
- **THEN** the selected launcher refuses before child execution and does not renew the action budget

### Requirement: Explicit Source5 stable source observation remains bounded operator evidence
New SOURCE5 selections SHALL explicitly bind source_witness_variant through selection, receipt, profile, coordinator bindings and report. The only accepted values SHALL be source5-stable-body-idle-v1 and source5-footer-then-body-v1 under source5-stable-source-witness-contract.md. Missing, unknown, conflicting or drifting SOURCE5 values and selector-on-legacy inventory SHALL refuse before transport/input; legacy fieldless behavior SHALL remain unchanged. The stable variant SHALL require one exact source BODY open observation and a distinct later full2000ms released-idle trigger BODY observation, same candidate/waiting/window, exact source context, and full raw Library-to-source1-to-source2 sidecar equality. It SHALL retain actual capture identifiers, PNG hashes, completed times and footer-match booleans, with source_authority=operator-conjunction and native_current_page_authority=false. No failed-footer fallback, renewed deadline, quota refund or spent-trial credit SHALL occur.

#### Scenario: Stable source and idle witness agree within original bounds
- **WHEN** two distinct source captures satisfy all selected BODY, identity, raw-context, preservation and full-idle checks within unchanged deadlines and quotas
- **THEN** the original once-only creation publication may proceed while the report distinguishes host display inference from SDK document/map/template guards and atomic native current-page authority

#### Scenario: Exact sidecars or second witness disagree
- **WHEN** either source differs from the approved Library baseline raw sidecars, later BODY/context changes, completed time does not advance, or the second full-idle observation is missing
- **THEN** no creation permission is published and the original guarded stop/recovery remains required

#### Scenario: Minimum source captures cannot fit before opening
- **WHEN** the sticky shared ledger cannot fit both remaining source witnesses and all3 protected postcreation captures
- **THEN** the stable selection refuses before ordinary open input without increasing or refunding any quota
