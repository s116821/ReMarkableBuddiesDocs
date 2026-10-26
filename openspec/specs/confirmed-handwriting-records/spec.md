# Confirmed handwriting records

## Purpose

Define explicit local confirmed sample/text retention, truthful readback and invalidation. Detailed version-one [design](../../changes/archive/2026-10-26-retain-confirmed-handwriting-corrections/design.md), [transport](../../changes/archive/2026-10-26-retain-confirmed-handwriting-corrections/contract.md), [report schema](../../changes/archive/2026-10-26-retain-confirmed-handwriting-corrections/report-schema.md) and [literal identity vectors](../../changes/archive/2026-10-26-retain-confirmed-handwriting-corrections/identity-vectors.json) pin exact fields and bounds.

Source basis for these requirements: [implemented source a9d01cd](https://github.com/s116821/ReMarkableBuddies/tree/a9d01cdce62bc67916ce398f4ac4432ce811988d/src/handwriting), [passing current-head CI](https://github.com/s116821/ReMarkableBuddies/actions/runs/40269256006) and [independent source/evidence acceptance](https://github.com/s116821/ReMarkableBuddies/pull/104#pullrequestreview-5650161916). Stored caller assertions do not establish recognition improvement, native integration or sync authority.

## Requirements

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
Reads SHALL validate required retained causal closure and known-key tombstones;
unrecognized/orphan history SHALL NOT masquerade as confirmed correction deletion.
Updates SHALL require CAS and explicit new confirmation; forget SHALL tombstone
only the selected logical key while retaining historical bytes/references.
Unknown domain shapes SHALL be preserved/refused rather than reinterpreted.
An explicit non-mutating operation-status path SHALL inspect accepted history
without staging/committing. Absence SHALL mean unknown, never rollback or dispatch
permission. A later deliberately invoked mutation SHALL be distinguished from
read-only reconciliation and pass exact replay/CAS without automatic resubmission.

#### Scenario: Replay, conflict and sample replacement
- **WHEN** an operation replays across restart, heads conflict, or an update substitutes the original sample/text/source linkage
- **THEN** identical replay is historical, conflicts do not choose a timestamp winner, and changed immutable facts require a new correction identity without rewriting old records.

#### Scenario: Forget and backup closure
- **WHEN** an explicit current-head forget completes and the whole owned Store is backed up/restored
- **THEN** active query excludes that key while exact history, tombstone, conflicts and all retained sample bytes survive without deleting another correction/profile.

#### Scenario: Uncertain commit and absent status
- **WHEN** a commit acknowledgment is uncertain and explicit status does or does not find the requested accepted operation
- **THEN** status performs no staging/commit, reports retained success versus unknown absence accurately, and never infers rollback or an automatic mutation grant from missing history.

### Requirement: Bounded readback and local ownership report honest scope
Query/inspect SHALL use bounded current snapshots with explicit profile and complete
encoded output budgets, deterministic ordering and truthful partial/conflict/media
availability. Required missing bytes SHALL prevent complete usable-sample claims.
Ordinary local mode and legacy-data leases SHALL span actual command output;
the live local domain SHALL exclude both already-active and newly admitted legacy
publishers until output ownership is released, without claiming permanent sync policy.
Unsupported selected/sync/native paths SHALL refuse without implicit activation.
Routine logs SHALL redact content and images, while explicit reports remain bounded.
Metadata traversal SHALL retain a single4096-envelope/8 MiB causal snapshot bound
for query and refuse incomplete/excess closure. Output subset
selection SHALL precede at most16 sample verifications/8 MiB compressed media and
the declared sequential pixel budget per command. Omitted samples SHALL remain
not-examined rather than acquire invented availability from metadata alone.
Reports SHALL follow the exact fact/head/sample states, diagnostics, fixed failure
codes and command/status/null/history/mutation-outcome matrix in report-schema.md.

#### Scenario: Query budget or missing data
- **WHEN** matches exceed requested output bounds, heads conflict or required media/commits are unavailable
- **THEN** bounded diagnostics distinguish omitted/partial/unavailable facts from complete-empty success without truncated text or fabricated recognition confidence.

#### Scenario: Ownership and failed output
- **WHEN** another owner holds the Store, an unsupported selected mode is configured, or stdout fails after a mutation
- **THEN** ownership/refusal remains enforced through actual completion and mutation uncertainty is not relabeled rollback or followed by an automatic retry/second report.

#### Scenario: Large matching corpus
- **WHEN** many metadata matches exceed the requested result/output budget
- **THEN** no more than the bounded selected subset is image-verified, omitted availability remains not-examined, and partial diagnostics do not claim every retained sample is usable.

#### Scenario: Exact report variants
- **WHEN** command results include unsupported/conflicted heads, missing/not-examined samples, empty status or query-budget refusal
- **THEN** strict output matches the pinned public fields, nullability and outcome matrix without guessed availability, accepted-history claims or invented transaction IDs.

#### Scenario: Existing or newly started legacy publisher
- **WHEN** a legacy publisher already owns the Store or attempts admission while a local correction report is live
- **THEN** the conflicting lifetime refuses through actual output completion, and releasing the report releases that local exclusion without starting any publisher.

### Requirement: Stored corrections do not imply recognition improvement
The implementation SHALL keep typed correction retention separate from recognition
providers, automatic Reader/Writer hooks, subject memory, configured preferences,
training artifacts and native/sync authority. Qualification SHALL use actual
Store/CLI/backup mechanisms and preserve failed results; semantic improvement and
full handwriting integration SHALL require their own representative evidence.

#### Scenario: Synthetic storage qualification
- **WHEN** a scripted image/text pair passes retention and replay tests
- **THEN** evidence establishes those mechanisms only and does not claim trained state, better handwriting recognition, real pen input or whole capability completion.
