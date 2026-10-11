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
