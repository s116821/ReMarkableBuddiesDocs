## ADDED Requirements

### Requirement: Explicit fixed-service stop with qualified lifecycle admission
Both companions SHALL require a separately reviewed, explicitly confirmed stop of only the fixed Buddy service on the original verified wired connection and boot. The host SHALL revalidate the original invocation, supported loaded unit/package/runtime identity and source-backed supported-profile predicate and independently accepted shutdown qualification before submission. Unknown or changed native ownership or unsupported stop policy SHALL refuse without mutation. No arbitrary command/unit/PID, start/restart, force-kill fallback, recovery, provider or native page operation SHALL follow.

#### Scenario: Supported original service is deliberately stopped
- **WHEN** the original unexpired review still matches a qualified current service lifecycle and the user confirms
- **THEN** the host submits only one fixed stop request and independently reads bounded current OS state without claiming native restoration or flush durability.

#### Scenario: Native owner or loaded unit cannot be qualified
- **WHEN** the service's invocation, package/unit policy or ordinary/resident source-backed evidence or shutdown qualification is absent, changed or unqualified
- **THEN** Stop is unavailable before dispatch; no signal, stop job, unit repair or alternate recovery is attempted.

### Requirement: Delivered resident package records remain closed and source bound
Resident Stop admission SHALL use only the independently qualified PACKAGE/Profile6/Lease3 contract defined in package-record-contract.md. The host SHALL bind fixed package paths, all twelve protected artifacts, the original nested rm-sync ServiceBaseline1, current companion identity/group observations, both fixed vendor policy projections and every private fact in the original sample digest. Historical LEGACY schemas, missing or contradictory companion records, observed-policy enrollment and unqualified build tuples SHALL refuse. Both production qualification registries SHALL remain empty during this proposed source reconciliation. The public protocol and unit-scoped Stop intent SHALL remain unchanged.

#### Scenario: Complete package shape has no production qualification
- **WHEN** a synthetic or observed package has matching Profile6/Lease3 and companion facts but its exact build/unit/policy/platform tuple has not passed the independent enablement gate
- **THEN** Stop remains unavailable with zero submissions; matching versions, hashes or a successful development experiment cannot enroll it.

#### Scenario: A proposed tuple weakens the companion watchdog invariant
- **WHEN** the original baseline or current rm-sync WatchdogUSec differs from zero, including when a proposed tuple agrees with that nonzero value
- **THEN** resident Stop admission refuses independently of tuple matching, preserving the fixed vendor-source invariant.

#### Scenario: Companion or package evidence differs from the original review
- **WHEN** an original companion record, fixed artifact, loaded policy, incarnation, group/context, package path or canonical private sample differs or cannot be observed within bounds
- **THEN** review or confirmation refuses before dispatch without dropping fields, translating legacy records, repairing an installation or granting native recovery authority.

### Requirement: Historical stop outcome remains separate from current service state
Possible submission without an admitted complete result SHALL remain unknown. Later inactive state SHALL NOT settle historical uncertainty, establish native restoration or automatically continue maintenance. Stop waiting SHALL cancel only its original local transport wait and SHALL NOT cancel or reverse a remote systemd job. Eight possible-submission and thirty-two-invocation/fence limits SHALL refuse without eviction; a connection's unknown history SHALL block another stop within host lifetime even after reboot.

#### Scenario: Stop reply is lost and later service is inactive
- **WHEN** a stop may have been submitted but its original result is unavailable and a separate read later observes inactive
- **THEN** both companions show current inactive state separately while preserving the unconfirmed original and offering no automatic retry or readiness claim.

#### Scenario: Old cancellation arrives after a newer operation
- **WHEN** a stale timer, cancellation or finalizer executes after its original ownership ended
- **THEN** it cannot signal the remote service, release another owner's guard or restore a late view.

### Requirement: Closed shared host boundaries preserve maintenance and native ownership
Both actual factories SHALL enforce strict bounded action-specific requests/results, current and retained identity relationships, shared maintenance ownership, observation quiescence and renderer generation fences. Only reduced OS status and opaque original references SHALL reach the renderer. Private unit/process/path/runtime/lease/provenance details SHALL remain privileged. Existing maintenance and native owners SHALL retain independent guards; OS stop success SHALL NOT be promoted to a general quiescence or native-restoration grant.

#### Scenario: Another maintenance operation owns the host
- **WHEN** Stop review or confirmation encounters an active owner
- **THEN** Busy performs no competing dispatch, invalidation or cancellation, preserving earlier uncertainty in every capability.

#### Scenario: Malformed or contradictory public reply
- **WHEN** a result contradicts its action, selected original connection/boot, allowed current observation or retained history
- **THEN** both host bridges and the shared controller refuse the complete result without clearing a possibly submitted original or leaking private metadata.

### Requirement: Reciprocal notebook archive maintenance ownership
The Stop controls SHALL share the existing maintenance owner with notebook archive controls. Either lane SHALL refuse conflicting active work without side effects and invalidate the other lane's idle review before new work. Retained lookup SHALL neither dispatch nor invalidate an unrelated review, and each lane SHALL preserve the other's uncertain history. Production native qualification registries SHALL remain empty until their separate native qualification is complete.

#### Scenario: Notebook and Stop contend
- **WHEN** either lane owns an invocation or replaces the other lane's idle review
- **THEN** both host factories and the actual shared UI preserve Busy exclusion, exact draft clearing and current owner/epoch cancellation without granting native Stop qualification.

### Requirement: Positive typed Stop-hook evidence

The fixed-service sampler SHALL obtain ExecStop and ExecStopPost through explicit
bounded Properties.Get calls using the installed standard client, an admitted
systemd unique owner and the verified loaded object for an already-allowed unit.
It SHALL use the normal fixed system-bus route and explicit reply, no-auto-start,
noninteractive-authorization and method-timeout flags. Ordinary OS socket
activation and ephemeral clients may occur; no zero-infrastructure-effects or
installed-source-attestation guarantee is implied.

The private service DTO SHALL separate the remaining strict textual fields from
two closed typed hook observations. Only two complete positively typed empty
arrays with valid currentness brackets SHALL satisfy the empty-hook predicate.
Omitted text, missing observations, nonempty arrays, malformed or incomplete
replies, drift, failed status or bounds SHALL refuse without substituting empty
strings or retrying through another candidate profile. Every command in a
nonempty array SHALL be validated before classification. Raw hook commands,
arguments, errors, private bus identifiers and response hashes SHALL NOT enter
retained facts or logs.

Every new read SHALL share the original product deadline, caps and observation
scope. Repeated samples SHALL read hooks afresh, and matching samples SHALL NOT
be treated as atomic configuration/invocation custody. The private sample digest
SHALL include reduced typed evidence, with matching Python/JavaScript encoding.
Public requests/results, the fixed Stop command, pre-submission qualification and
post-submission uncertainty semantics SHALL remain unchanged. Both production
qualification registries SHALL remain empty until separate target, lifecycle and
recovery qualification; historical metadata alone SHALL NOT enable Stop.

#### Scenario: Text omission and positively typed emptiness
- **WHEN** the remaining textual projection is complete and both current hook replies are complete typed empty arrays under matching original context
- **THEN** only the private hook evidence predicate is satisfied; no textual value is invented and no production tuple or Stop authority is created.

#### Scenario: Missing, nonempty or unverified hook observation
- **WHEN** either hook is absent, nonempty, malformed, incomplete, stale or outside its bounds, including a malformed later array member
- **THEN** admission refuses without raw value disclosure, default emptiness, alternate route, profile-loop retry or Stop submission.

#### Scenario: Currentness or deadline changes
- **WHEN** bus, owner, reported PID1, loaded unit, boot, client identity, repeated sample or original deadline no longer matches
- **THEN** the original typed query group stops and cannot be resumed or reused to authorize another operation.

#### Scenario: Complete typed evidence without shutdown qualification
- **WHEN** source fixtures or an actual metadata observation satisfy the typed hook predicate but production shutdown qualification is absent
- **THEN** Stop remains disabled and actual native cancellation/recovery acceptance remains unfinished.
