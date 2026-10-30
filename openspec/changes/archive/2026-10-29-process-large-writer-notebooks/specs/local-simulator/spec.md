## MODIFIED Requirements

### Requirement: Shared workflow execution
The Reader simulator SHALL retain the real device-facing interface and production
Reader orchestration, parsing/verification, classification and recovery policies.
Writer host scenarios SHALL run the production joined Writer/export flow and
Ledger with declared normalized text and a scripted destination. Deterministic
scenarios SHALL use scripted LLMEngine replies with no credentials or network
calls. Explicit live Reader scenarios SHALL retain the configured provider path.
Separate loopback HTTP integration tests SHALL remain distinct from scripted
simulation and live account/native evidence.

Notebook host scenarios SHALL run the production planner, stage runner, typed
Ledger/media and guarded exporter with scripted model/destination behavior. They
SHALL NOT replace production calls with hand-built successful status reports.

#### Scenario: Accepted question
- **WHEN** proposal and independent transcription agree and the successor is blank
- **THEN** the production workflow writes one header and the exact Q&A block to the successor while preserving the source.

#### Scenario: Declined or disagreeing question
- **WHEN** a proposal is NONE or independent reading disagrees
- **THEN** the source receives no feedback ink, successor navigation or answer text; the matching non-ink diagnostic is recorded.

#### Scenario: Writer create and refined update
- **WHEN** a scripted Writer host scenario generates/exports, reopens and deliberately refines/re-exports one correlation
- **THEN** the production flow retains exact drafts/source history, creates then updates the same scripted destination identity and records actual stage/poll counts without claiming tablet output.


#### Scenario: Larger notebook generation and refinement
- **WHEN** a bounded declared normalized asset exceeds inline limits and is processed/refined across restart
- **THEN** production paths retain complete source/range/stage facts, enforce actual call budgets and update the same scripted note without a native-transition claim.

#### Scenario: Stage or media fault
- **WHEN** a declared stage loses acknowledgment, is canceled/stale/invalid or loses required media
- **THEN** actual admission/cancellation rules stop subsequent calls/writes and report truthful partial/uncertain state without automatic replay.
### Requirement: Structured reproducible scenarios
Reader scenarios SHALL preserve their existing page, iteration, gesture, reply,
fault and expected-result contract. Writer host scenarios SHALL declare bounded
normalized source/selection, steps, scripted replies, restart and phase-indexed
cancellation/state/destination faults. Unknown/duplicate fields, unsupported
modes and invalid values SHALL fail before execution. Relative assets/output
SHALL resolve from the scenario location; mode dispatch SHALL use strict schemas
without silently accepting Reader fields as Writer instructions.

Writer notebook scenarios SHALL resolve declared source assets relative to the
scenario, validate at most 8 MiB per asset and 32 MiB total before execution, and
keep the existing Writer scenario-JSON limit separate from Reader admissibility.
Reader SHALL retain its current larger valid inputs. Unknown/duplicate fields,
unsupported native modes and invalid work/call/asset budgets SHALL refuse before
Store/model/device effects. Original fixture files SHALL remain unmodified.
Each new asset SHALL declare its raw SHA-256 and follow the same regular-file,
opened-handle, bounded-read, strict JSON and path-sanitization contract as notebook
generation; special files and changed/unsupported bindings SHALL refuse.
Relative notebook assets SHALL resolve against the scenario file's directory,
not the build machine's source checkout. Complete validated observed buffers
SHALL freeze before fixture Store creation; production preparation SHALL consume
those buffers without reopening mutable transport paths. The sum of declared
raw notebook asset bytes SHALL be at most 8 MiB per scenario.

#### Scenario: Bounded gesture input
- **WHEN** a short contact precedes a stationary two-second corner hold
- **THEN** the shared timer ignores the short contact and triggers on the valid hold without movement.

#### Scenario: Exhausted gestures
- **WHEN** a scenario has no valid remaining trigger
- **THEN** execution records a bounded error instead of waiting forever.

#### Scenario: Writer phase faults
- **WHEN** replay, acknowledgment loss, cancellation or selected-state change is injected at a declared joined-flow phase
- **THEN** actual production admission/dispatch rules determine the result and assertions verify exact forbidden model/destination/write counts without sleeps as success.


#### Scenario: Asset and admission bounds
- **WHEN** a Writer asset/total budget is exceeded or a valid Reader history is larger than 1 MiB
- **THEN** the Writer request refuses before execution while the original valid Reader admission remains supported, without sharing the new Writer cap globally.

#### Scenario: Asset substitution or special file
- **WHEN** an asset is a FIFO/symlink/reparse path, changes opened-file binding or does not match its expected raw hash
- **THEN** the scenario refuses before Store/model/destination effects with a fixed sanitized error, without a blocking special-file read or fallback to newer path content.

#### Scenario: Relocated maintained fixture
- **WHEN** a scenario and its declared relative notebook asset are copied outside the build checkout
- **THEN** the actual application resolves and freezes the asset beside that scenario, retaining its exact raw hash and complete coverage.
### Requirement: Inspectable results and meaningful assertions
Reader scenarios SHALL preserve page PNGs and JSON reports of exact rendered
text, marks, active page, model calls, errors and timestamped operations. Writer
host scenarios SHALL save exact draft/export content, source preservation,
ordered phase/destination traces, call/write counts and assertion failures,
without invented tablet PNGs or native output. Expected mismatches SHALL fail
after artifacts are saved. Existing Reader exact/text_contains assertions SHALL
remain supported, and execution labels SHALL distinguish scripted simulation,
loopback transport and explicit live-provider observations.

Notebook reports SHALL expose actual source/media digests, selected unit/range
coverage, planned/invoked calls, stage outcomes, fixed error codes, bounded final
content and actual destination/write observations. They SHALL distinguish
processed coverage from semantic quality, invoked model cost from zero writes,
and failed recording from local zero-invocation/no-send observations. Reports
SHALL be saved before assertion failures and SHALL NOT fabricate tablet PNGs.
An explicit `retain_store_fixture` option MAY retain a closed test-owned data
directory beneath a new `store-fixture` directory in the declared scenario
output. It SHALL default off, refuse existing/symlink destinations, exclude
credential/cache roots, and bound the copy at 8192 regular files/64 MiB with
relative-path/hash evidence. This diagnostic fixture SHALL NOT claim backup
restore compatibility, native authority or fresh model/export admission.
Unused scripted replies and unreached declared phase faults SHALL fail assertions.

#### Scenario: Fresh empty host fixture
- **WHEN** a scripted scenario performs only a restart and explicitly retains its Store fixture
- **THEN** it saves the actual closed ordinary Store and newly created conversation with zero model/destination calls, without creating a fake model result or native binding.

#### Scenario: Failed assertion
- **WHEN** expected text, page, operation counts or error behavior differs
- **THEN** the process exits unsuccessfully and the report identifies the mismatch.

#### Scenario: Writer report is not rendered output
- **WHEN** a Writer host scenario succeeds
- **THEN** its report exposes the actual production draft/export state and no fabricated navigation, page drawing, tool/menu operation or native-completion claim.


#### Scenario: Partial-stage report
- **WHEN** two model stages were invoked before cancellation or storage failure prevents continuation
- **THEN** actual recorded/uncertain stages and zero later calls/writes remain inspectable rather than being labeled no cost, complete generation or native success.
