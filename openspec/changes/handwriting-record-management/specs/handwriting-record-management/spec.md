## ADDED Requirements

### Requirement: Explicit bounded saved-correction inspection
Both browser and Electron companions SHALL offer the same explicit-profile bounded saved handwriting correction query and exact-key inspection through the delivered fixed one-shot producer. They SHALL display exact supported requested text and caller-asserted provenance with truthful head/media/partial diagnostics, without claiming recognition efficacy, native source verification, image display or whole-corpus completeness from a subset.

#### Scenario: Supported results and incomplete empty search
- **WHEN** the user searches a profile and the producer returns supported usable values or a partial empty subset
- **THEN** both companions render escaped exact content and diagnostics, and a withheld/omitted/unavailable subset is never presented as a complete empty corpus.

#### Scenario: Unsupported, conflicted or unverifiable record
- **WHEN** exact-key inspection observes unsupported/conflicting heads, unavailable samples or malformed/new-version output
- **THEN** the companion shows bounded truthful inspection/refusal and offers no removal authority from that observation.

### Requirement: Separate exact-record confirmation and retained tombstones
Removing a saved correction from active use SHALL require a fresh complete single-head supported inspection, host-captured immutable expected revision and a separate deliberate confirmation naming its exact content/consequence. Confirmation SHALL dispatch the original tombstone request at most once and SHALL explain retained historical text/samples and backups without promising physical erasure or recognition changes.

#### Scenario: Captured correction is deliberately removed
- **WHEN** a current prepared single-head correction is separately confirmed within its lifetime
- **THEN** only its captured CAS tombstone may dispatch once, and exact validated commit/historical acknowledgment is labeled as an observed operation rather than permanent current-state authority.

#### Scenario: Record changes or output is lost
- **WHEN** expected heads become stale, or output is lost/corrupt/cancelled after possible dispatch
- **THEN** a proved CAS refusal is distinguished from unknown effect, and no automatic retry/new-head/operation replacement or active-query inference is permitted.

### Requirement: Original-operation status and guarded private lifetime
Status checks SHALL use only finite host-custodied original key/operation on the verified original target and SHALL remain non-mutating. Original disposition and later historical status SHALL remain distinct. Shared ownership, immutable response context, cancellation fencing and content clearing SHALL apply consistently across actual browser/Electron and observation paths.

#### Scenario: Historical acceptance or absent status
- **WHEN** an original uncertain removal is checked and the producer finds its exact retained tombstone or no accepted history
- **THEN** the former is historical operation evidence and the latter remains unknown; neither grants mutation replay or asserts the current active head.

#### Scenario: Expiry, capacity or identity invalidation
- **WHEN** private custody expires, bounded capacity is exhausted, or refresh/disconnect/peer/Stop/page lifetime invalidates the flow
- **THEN** private drafts/content and prepared authority clear, no deadline renews or original evicts silently, and late output cannot repopulate content or dispatch.

#### Scenario: Maintenance owner is occupied or a stale cancel arrives
- **WHEN** another admitted maintenance owner holds I/O or cancellation names an older action
- **THEN** Busy preserves that owner before hooks/I/O, and only the exact captured action can be fenced/cancelled while every existing directed owner relationship remains enforced.
