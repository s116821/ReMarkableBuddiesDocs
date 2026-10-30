# document-scoped-buddy-sync

## Purpose

Define the implemented domain-opaque selected-storage APIs and their fail-closed custody boundaries. These APIs do not enable a shared worker, verify a provider binding, restore a selected store, or grant native authority. The unfinished end-to-end change remains active.

## Requirements

### Requirement: Original selection publication replay
The storage layer SHALL preserve bounded durable publication evidence tied to the
original scope, parent selection and request. Only evidence reachable from the
accepted current selection SHALL authorize replay. Replay SHALL return the original
publication identity and SHALL NOT append to a replacement winner or silently
refresh the caller's authority. Exhausted history bounds SHALL refuse further
publication instead of discarding replay evidence. Complete selected snapshot reads
SHALL validate reachable accepted history and required historical closures before
returning a snapshot/live token, including corruption introduced after Store open.

#### Scenario: Lost acknowledgement followed by replacement
- WHEN a guarded commit is accepted, its acknowledgement is lost, and a replacement is activated before retry
- THEN retry with the original identity returns the original receipt, the replacement is unchanged, and the old token cannot authorize another mutation.

#### Scenario: Unaccepted staging remains orphaned
- WHEN a process dies after staging objects or prior metadata but before selection publication
- THEN reopening retains the prior complete selection and does not treat staged objects or unreachable history as accepted publication evidence.

#### Scenario: Incompatible maintenance cannot discard selection metadata
- WHEN backup, restore or generation migration lacks an implemented selected-metadata portability policy
- THEN it refuses without publishing a complete backup or changing the active generation.


#### Scenario: Required lineage becomes unavailable after open
- WHEN accepted parent metadata or a required historical record/media object is removed or corrupted while the Store remains open
- THEN a complete selected snapshot refuses without returning a live token or changing CURRENT/membership; reopen also refuses, while restoring the exact required bytes permits the same selection again.

### Requirement: Retained-only opaque settlement publication
Historical settlement storage SHALL link to an accepted original publication and
an exact intent reference in retained membership. It SHALL atomically extend
retained facts/evidence without changing winner references or adding an active
append. Required prior evidence SHALL remain reachable. Storage SHALL NOT infer
backend verification or enqueue a new shared document edit from that publication.

#### Scenario: Late settlement after replacement
- WHEN a domain-validated late fact is published for an exact retained intent
- THEN the current winner references are unchanged, original evidence and new historical facts reopen together, and stale/foreign/orphan intent requests refuse.

#### Scenario: Retained settlement replay
- WHEN acknowledgement is lost and the same settlement is retried after another replacement
- THEN the original settlement publication is returned without changing the replacement or admitting an effect.

### Requirement: Verified portable selection archive custody
Selected export SHALL preserve original reachable selection transaction/history,
winner and retained evidence/media plus unrelated owned committed scopes in a bounded
versioned archive. Offline inspection SHALL validate exact bytes and closure without
minting a live token or activating imported membership. Configuration SHALL remain
excluded until a portable allowlist exists.

#### Scenario: Historical selected archive inspection
- WHEN a compatible complete selected archive is inspected offline
- THEN original references/history/retained media remain verifiable and counts/media completeness are reported without native/group/admission authority.

#### Scenario: Domain validation of archived winning membership
- WHEN a domain adapter requests one historical scope from a valid format2 archive
- THEN it receives the exact original head and ordered winner/retained references with pinned included media, without a live token or destination Store mutation.

#### Scenario: Invalid archive or absent scope during domain inspection
- WHEN the requested scope or bound is invalid, the archive format is incompatible, or any required archive history/object is corrupt
- THEN inspection refuses even if the requested winner alone is readable; only an absent scope in a completely valid format2 archive returns absence.

#### Scenario: Incompatible or interrupted selected export
- WHEN required history/objects are corrupt, unsupported, missing or cannot be staged
- THEN no complete marker is published and current source selection and unrelated data remain unchanged.

### Requirement: Original predecessor evidence without live authority
Historical selection lookup SHALL resolve the immediate hash-linked predecessor of
an exact accepted original operation and validate original and parent closures.
It SHALL return historical transaction evidence only, without minting a live token
or changing current membership. Corrupt, missing or foreign history SHALL refuse.

#### Scenario: Original parent after replacement
- WHEN the accepted original operation is queried after later selection replacement or process restart
- THEN its original immediate predecessor is returned without substituting the current head or refreshing admission.

#### Scenario: Invalid original predecessor closure
- WHEN an original or parent link, scope, generation, identity or required object cannot be verified
- THEN lookup refuses without changing current selection or unrelated data.

### Requirement: Cumulative selected receiving read budget
A budgeted selected read SHALL charge caller-owned cumulative aggregate,
transaction/reference, metadata-read and media-verification limits before content
I/O across all requested snapshots and accepted history. Exhaustion SHALL refuse
without a partial authoritative snapshot, preserve complete lineage validation
and poison the request budget. The existing selected-read API SHALL remain usable.

#### Scenario: Catalogue and aggregate reads share a budget
- WHEN several individually valid selected snapshots together exceed a receiving request's budget
- THEN the first unaffordable read refuses before its content I/O and the domain caller discards the incomplete receiving result.

#### Scenario: Historical or media work exhausts the budget
- WHEN old accepted closures, repeated reads, oversized files or included-media verification exhaust a shared limit
- THEN validation cannot return a complete snapshot or skip history/media to fit the limit; source selection remains unchanged.

#### Scenario: Catalogue ancestry without unbudgeted receipt reads
- WHEN a domain validates append-only selected membership and exact Initialize/genesis identity from a budgeted snapshot
- THEN already verified accepted metadata and original raw-byte digests are available without additional file reads, historical live tokens or promoting retained registrations.

#### Scenario: Immutable domain identity from already charged historical custody
- WHEN a new selected winner re-roots an existing record UUID and drops the original claim chain from its current closure
- THEN each accepted transaction exposes its already verified selected envelopes paired in original ObjectRef order without extra I/O, allowing domain-owned immutable identity validation without treating historical or retained records as current authority.

### Requirement: Durable pinned selected publication intent
A prepared local selected outbox intent SHALL pin the original actor, scope,
Store/aggregate generation, accepted base, complete opaque selection and fixed
provider slot/immutable descriptor. Preparation and current checks SHALL refuse
stale or incompatible pins and corrupt required objects. Replay SHALL recover
only the original intent without rebase, slot allocation or live authority.

#### Scenario: Restart and original-operation replay
- WHEN a prepared intent is retried after restart, withdrawal or selection replacement
- THEN identical operation/request recovers its original custody state, while changed payload refuses and current readiness never substitutes a newer selection.

#### Scenario: Binding and selection isolation
- WHEN token, actor, generation or group/account/application binding differs from the prepared intent
- THEN current preparation refuses without changing unrelated scopes, media or pending intent; no slot or native operation is attempted.

#### Scenario: Withdrawal without remote inference
- WHEN the local owner explicitly withdraws a prepared attempt
- THEN its original intent remains inspectable but withdrawn, with no remote acceptance, deletion, publication permission or automatic retry claimed.

#### Scenario: Incomplete outbox atomic-write staging after interruption
- WHEN an exact UUID regular staging residue remains before preparation or alongside pending/withdrawn intent
- THEN lease-held reopen cleanup removes that uncommitted residue, preserves the original journal and current data, and continues refusing unsupported foreign entries without broadening deletion rules.

### Requirement: Explicit mode binding and publisher lifetime isolation
Local mode transitions SHALL pin current actor/epoch and refuse active publisher
leases. Explicit local-only, isolated-backup and shared-group choices SHALL keep
device/actor/group/backup identities distinct and preserve prior namespaces without
automatic join, import or deletion. Mode metadata SHALL not grant verified provider
or native authority. Old queued intent SHALL not rebind across mode epochs.

#### Scenario: Stop publisher before a mode change
- WHEN an old legacy publisher or explicit mode lease is still alive
- THEN mode transition refuses, and after that owner stops the current-token transition may atomically select the new mode without changing selections or media.

#### Scenario: Leave and return or change provider binding
- WHEN the installation re-enters isolated backup or shared mode after leaving or changing its binding/root
- THEN isolated identity is fresh and old shared intents remain original custody but are not current work under the new epoch.

#### Scenario: Mode metadata is not bootstrap proof
- WHEN a caller chooses a group/root ID or opens a mode lease
- THEN no cloud slot/native operation occurs and verified bootstrap, supported account/app binding and actual domain admission remain separately required.

### Requirement: Read-only original slot observation
Uncertain or stale prepared-slot reconciliation SHALL support exact-ID read-only
observation with prepared account/application and group/scope integrity checks.
It SHALL not create, allocate, update, delete or choose a successor, and provider
evidence SHALL not become domain/native authority.

#### Scenario: Observe occupied original slot without another create
- WHEN a caller observes its prepared original slot after uncertain acknowledgement
- THEN strict same/different immutable pointer evidence is returned using read operations only, without republishing its candidate.

#### Scenario: Missing or incompatible original slot
- WHEN the slot or referenced descriptor is absent, removed, malformed, corrupt or outside the prepared binding
- THEN observation refuses and never infers freedom or authorizes a successor/rebase.

### Requirement: Persisted isolated backup identity continuity
The system SHALL refuse persisted mode history that changes backup identity during consecutive same-binding isolated choices or reuses a historical identity after leaving isolated mode or changing binding.

#### Scenario: Re-entry identity is corrupted on disk
- **WHEN** saved history substitutes an old backup UUID for a later re-entry
- **THEN** snapshot, publisher lease and original-operation replay refuse before current admission

#### Scenario: Contiguous same-binding identity is corrupted on disk
- **WHEN** saved consecutive isolated choices for the same binding contain different backup UUIDs
- **THEN** mode history load refuses while valid identity-preserving histories still reopen

### Requirement: Bounded historical outbox enumeration
Recovery callers SHALL be able to enumerate the complete bounded local selected-intent journal under one Store lock using original operation identity and strict actor/fingerprint/filename validation. Enumeration SHALL return historical custody only, not current selection, provider acknowledgement or permission to send/apply.

#### Scenario: Restart with stale or withdrawn intents
- **WHEN** stored intents span scopes, withdrawals or departed mode/selection epochs
- **THEN** enumeration returns original entries in deterministic operation UUID order without rewriting state or silently granting current authority.

#### Scenario: Corrupt or foreign journal entry
- **WHEN** any entry violates the existing journal validation or capacity limits
- **THEN** the entire enumeration refuses without returning a partial inventory or altering source bytes.
