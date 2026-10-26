## ADDED Requirements

### Requirement: Explicit confirmed samples remain distinct from inference
The component SHALL offer an explicitly invoked offline typed correction provider
and one-shot transport, retaining exact bounded sample PNG bytes, original text,
confirmed replacement and asserted provenance in the existing Handwriting domain.
Only explicit caller confirmation SHALL create/update a correction. The transport
SHALL validate strict bounded JSON/base64/image data before admission, preserve
Unicode text and distinguish caller-asserted source links from verified ownership.
No canceled/uncertain model output, refinement or export SHALL imply confirmation.

#### Scenario: Confirmed Unicode correction
- **WHEN** a caller explicitly confirms a valid bounded sample/text pair and later reopens the Store
- **THEN** the exact original bytes, texts and asserted provenance remain readable without recapture, model training or fabricated native authority.

#### Scenario: Unconfirmed or malformed input
- **WHEN** confirmation is absent, data is malformed/duplicated/oversized or image decoding exceeds admitted format/dimension/pixel bounds
- **THEN** the command refuses before correction admission without model/device startup, path fallback or a learned-example claim.

### Requirement: Typed correction identity and invalidation preserve history
The domain SHALL use exact Handwriting1 discriminator/identity/media validation,
explicit profile/key/operation and expected heads, deterministic replay and
immutable original sample/linkage. Changed-content operation reuse SHALL refuse.
Updates SHALL require CAS and explicit new confirmation; forget SHALL tombstone
only the selected logical key while retaining historical bytes/references.
Unknown domain shapes SHALL be preserved/refused rather than reinterpreted.

#### Scenario: Replay, conflict and sample replacement
- **WHEN** an operation replays across restart, heads conflict, or an update substitutes the original sample/text/source linkage
- **THEN** identical replay is historical, conflicts do not choose a timestamp winner, and changed immutable facts require a new correction identity without rewriting old records.

#### Scenario: Forget and backup closure
- **WHEN** an explicit current-head forget completes and the whole owned Store is backed up/restored
- **THEN** active query excludes that key while exact history, tombstone, conflicts and all retained sample bytes survive without deleting another correction/profile.

### Requirement: Bounded readback and local ownership report honest scope
Query/inspect SHALL use bounded current snapshots with explicit profile and complete
encoded output budgets, deterministic ordering and truthful partial/conflict/media
availability. Required missing bytes SHALL prevent complete usable-sample claims.
Ordinary local mode and legacy-data leases SHALL span actual command output;
unsupported selected/sync/native paths SHALL refuse without implicit activation.
Routine logs SHALL redact content and images, while explicit reports remain bounded.

#### Scenario: Query budget or missing data
- **WHEN** matches exceed requested output bounds, heads conflict or required media/commits are unavailable
- **THEN** bounded diagnostics distinguish omitted/partial/unavailable facts from complete-empty success without truncated text or fabricated recognition confidence.

#### Scenario: Ownership and failed output
- **WHEN** another owner holds the Store, an unsupported selected mode is configured, or stdout fails after a mutation
- **THEN** ownership/refusal remains enforced through actual completion and mutation uncertainty is not relabeled rollback or followed by an automatic retry/second report.

### Requirement: Stored corrections do not imply recognition improvement
The implementation SHALL keep typed correction retention separate from recognition
providers, automatic Reader/Writer hooks, subject memory, configured preferences,
training artifacts and native/sync authority. Qualification SHALL use actual
Store/CLI/backup mechanisms and preserve failed results; semantic improvement and
full handwriting integration SHALL require their own representative evidence.

#### Scenario: Synthetic storage qualification
- **WHEN** a scripted image/text pair passes retention and replay tests
- **THEN** evidence establishes those mechanisms only and does not claim trained state, better handwriting recognition, real pen input or whole capability completion.
