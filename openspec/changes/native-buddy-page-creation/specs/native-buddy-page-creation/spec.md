## ADDED Requirements

### Requirement: Conditional supervised session activation
If XOVI is selected after comparison with robust native/direct alternatives, the Buddy product SHALL ship a tiny independent Supervisor and normal runtime as separate processes in the same repository, release artifact and Manager installation. It SHALL keep cold boot stock with no XOVI injection, manage the vetted payload internally, gate activation by exact compatibility, and restrict hooks to necessary semantic capabilities. The earlier categorical production exclusion SHALL NOT disqualify this candidate; selection still requires safety, maintainability and native evidence. SDK-owned adapter contracts remain in ReMarkableOpenSDK's OpenSpec.

#### Scenario: Cold boot and first supported gesture
- **WHEN** a tablet boots and receives its first recognized Buddy gesture of a supported kind
- **THEN** it remains stock until compatibility-gated session activation is required; activation permits at most a brief one-time restart/rebind, and subsequent gestures use the ready runtime without per-conversation restart.

#### Scenario: Triggering action crosses activation
- **WHEN** activation replaces the native session before continuing the triggering intent
- **THEN** the action reacquires and validates current source, cancellation and fresh handles; stale capture, lease or pending native operation is not replayed across restart.

#### Scenario: Incompatible or unhealthy session
- **WHEN** compatibility is unknown, readiness/heartbeat times out or rapid crash/restart loops occur
- **THEN** activation refuses or bounded automatic rollback restores stock while the independent Supervisor remains available for UI-independent recovery and preserves documents/data.

#### Scenario: Management and reboot recovery
- **WHEN** Manager disables, updates or uninstalls the selected components, or the tablet cold reboots
- **THEN** Manager owns the complete lifecycle without a user-managed XOVI or separate SDK prerequisite, recovery does not rely on modified UI, and reboot returns to the non-XOVI baseline without a persistent injection crash loop.

#### Scenario: Narrow stock experience
- **WHEN** extension capabilities become available
- **THEN** Buddy uses narrow semantic hooks and does not replace the tablet shell or broadly customize stock UI merely because hooks permit it.

### Requirement: Qualified automatic native successor creation
The system SHALL provide qualified automatic native writable Buddy-page creation immediately after the exact source, preserving native identity/content in supported notebooks and open annotated PDFs. Qt/XOVI MAY be selected through evidence; a library or notebook-only demonstration SHALL NOT establish PDF support. Source: REM25; qualification Q0-Q3.

#### Scenario: New conversation in open PDF
- **WHEN** capability and exact source ownership are verified
- **THEN** exactly one native writable successor is created without menu automation or per-request restart, preserving original PDF bytes, prior IDs/order/mappings, annotations and unknown metadata.

#### Scenario: Unsupported capability
- **WHEN** firmware, ABI, native schema, module or owner cannot be verified
- **THEN** automatic mutation is refused with an honest unsupported result.

### Requirement: Exact binding and non-destructive reuse
Acquisition SHALL use stable conversation/document/page IDs and native session/revision guards, with REM37 as canonical binding/history owner. Source: REM25/37/38; Q4-Q7.

#### Scenario: Existing scrolled or edited page
- **WHEN** the conversation has a verified target
- **THEN** that page is reused without duplicate creation or clearing edits even with invisible header.

#### Scenario: Moved or ambiguous binding
- **WHEN** binding location changes or identity is missing/ambiguous
- **THEN** a moved exact page is resolved without silent reordering using a qualified route, while uncertainty requires reconciliation without render authorization.

#### Scenario: Blank start or refinement
- **WHEN** blank-start or Writer refinement requests acquisition
- **THEN** the same contract applies, refinement retains its conversation, and blank-start fabricates no question or model call.

### Requirement: Durable correlated acquisition and recovery
The system SHALL serialize mutations and track operation identity/native outcome/binding commit using shared storage. Completion SHALL require exact target/order/persistence observation, not transport reply or elapsed delay. Native effect journals SHALL remain device-local and SHALL NOT replay through restored or synced records. Source: REM25/36/37 coordination; Q4-Q5.

#### Scenario: Lost reply after insertion
- **WHEN** insertion may have committed before timeout/crash
- **THEN** retry reconciles the same operation against unambiguous native identity; uncertainty remains ReconcileRequired without another insertion.

#### Scenario: Cancellation or user activity
- **WHEN** cancellation, external editing/navigation or session replacement invalidates ownership
- **THEN** no late rendering occurs and uncertain/user-edited pages are preserved rather than deleted or globally undone.

#### Scenario: Restored logical conversation
- **WHEN** a conversation binding is restored or synced
- **THEN** its native association is revalidated on this device and no native creation or pending operation is replayed automatically.

### Requirement: Evidence-backed fallback and safe manual preparation
Automatic creation SHALL remain required until exhaustive investigation and real tests of credible alternatives show no elegant reliable route, with independent outcome review. The manual blank-successor fallback SHALL be documented and exercised without overwriting unrelated or unknown content. Source: REM25 latest clarification; A-F/Q6.

#### Scenario: Untested candidate remains
- **WHEN** a credible route remains untested, unavailable to a contributor or only failed its first prototype
- **THEN** outcome acceptance remains incomplete; elapsed effort and search misses do not establish impossibility.

#### Scenario: Prepared successor
- **WHEN** exact successor identity and full native blankness including hidden/off-screen content are verified
- **THEN** it may be safely adopted without a model; unrelated nonblank, legacy-unbound or unknown content is preserved/refused.

### Requirement: Minimal versioned extension lifecycle
Any selected extension SHALL have pinned provenance, license notices, minimal dependencies, exact compatibility and supported activation/disable/rollback/removal consumed by REM41. It SHALL be internal device integration without a Buddy admin service. Source: REM25/41; Q8.

#### Scenario: Inactive or incompatible extension
- **WHEN** activation fails or reboot/ABI changes remove capability
- **THEN** actual unavailability is reported, documents/data are preserved and supported stock/reactivation instructions are available; file presence is not activation proof.

#### Scenario: Public installation/removal
- **WHEN** Manager or a manual contributor manages accepted components
- **THEN** integrity/compatibility/preservation checks apply, unrelated extensions remain, and no firmware/account/sync/general remote-command service is introduced.

### Requirement: Evidence-qualified delivery
The system SHALL preserve simulator regressions for native findings and qualify the selected outcome on disposable notebooks/annotated PDFs through preservation, persistence, idempotency, cancellation and rollback. Source: REM25 acceptance; Q0-Q10.

#### Scenario: Offline contributor checks
- **WHEN** fixtures/simulation run without authorized hardware
- **THEN** results are labeled accordingly and native maintainer gates remain open without making private tools contribution prerequisites.

#### Scenario: Integrated release
- **WHEN** the selected outcome is proposed for1.0
- **THEN** REM35 verifies downstream native integration and scope limits; unpaired offline RM2 tests do not establish cloud-sync/Paper Pro support.

### Requirement: Host-owned lifecycle fault experiment
Before a supervised candidate advances to device activation, Buddy SHALL exercise an original isolated host lifecycle harness with fake processes and owned temporary configuration. It SHALL demonstrate independently observed recovery after Supervisor failure, reject stale generation/nonce/process messages, preserve unrelated configuration, and report recovery failure honestly. It SHALL permit harmless Supervisor autostart only when boot remains stock and stale session activation cannot cross a boot. Host success SHALL NOT qualify tablet behavior or authorize activation.

#### Scenario: Supervisor or protection fails
- **WHEN** the Supervisor dies during activation or rollback, or the recovery guard dies after Ready
- **THEN** independent recovery restores exact stock state or the harness reports failed/unprotected operation; deadlines alone cannot establish recovery, and no further activation is automatically attempted.

#### Scenario: Stale messages or interrupted management
- **WHEN** old readiness/heartbeat messages arrive or update/uninstall leaves partial transaction files
- **THEN** old messages cannot establish readiness or renew protection, baseline and unrelated files are preserved, and only owned transaction artifacts are removed.

#### Scenario: Simulated cold boot
- **WHEN** both protection processes are lost and a new simulated boot reconstructs state
- **THEN** it begins stock without injection regardless of leftover payload/session files and requires a new authorized trigger before activation.
