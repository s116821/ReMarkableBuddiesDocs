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
