# Selected Reader researched answers from an original PDF

Proposed design for the active [document-scoped Buddy sync change](proposal.md).
The baselines are Buddy `520d89e5b47d2646f6bd87fd87a989778f1db9d1` and Docs
`18cdf3a12bf89c6b17fff7f6d91fe88ef1c8e4ab`. Review this design with the paired
implementation before enabling the installed route.

## Installed entry and explicit research intent

Extend `reader_runtime::run_installed_selected` and
`workflow::selected_resident_reader::run`. Use an optional, local-only
`reader.researched_pdf` block in the existing trusted Config to admit this
route for the configured, already registered document. Validate the typed
block in `reader_runtime::Configuration`. Its fields are the required
`no_internet_corner` and optional `research_model`. Without that block the
existing selected workflow continues. With it, an unavailable source or
required research stage ends the request through the existing finalizer.
Preserve ordinary Ledger APIs, selected Writer routing, and the default
refusal when installed source or health admission is absent.

Parse both corners with `TriggerCorner::from_string` and reject an unknown
value or the same parsed corner, including aliases such as `LL` and
`lower-left`. In `device/{interaction,input_observer,request_input}.rs`,
enable the second corner only in the installed selected Reader idle observer.
Both corners require the same stationary single-contact hold, complete
release, and overlapping quiet-observer checks. Mixed contacts or crossings
refuse a Reader release. The ordinary corner keeps its existing armed
regional Writer priority and refusal on unknown slot state. Otherwise it
supplies `UsePolicy`. The second corner supplies `NoInternet` for Reader
only and leaves any Writer slot untouched. The resident owner sees the
same Reader gesture. Re-admit the effective configuration after each release
and refuse any change to the observer's corner mapping or opt-in block.

Freeze the typed directive with the release. `NoInternet` dominates effective
policy throughout the Attempt. Model output, inferred intent and later
configuration cannot turn research back on. Keep the interpreted question
and history byte-exact. The second corner disables external web/tool research.
Recognition, verification and answering still use the configured model service.
The ordinary corner does not interpret free-form handwritten internet
instructions. Delivering that form of opt-out requires an explicit intent
admission with agreement and ambiguity controls before web egress. Its
acceptance must demonstrate a handwritten denial blocks the research call
while the exact transcription remains intact. Until then, the installed
entry documents the second corner as the proposed per-release opt-out.
Installed researched-route activation remains gated on accepting and implementing
handwritten intent admission, including ambiguous intent refusal. The original-PDF
producer and its offline composition can be implemented independently; neither
that producer nor the proposed second corner closes this activation gate.

## Produce and pin the original source

Initial support is the existing bounded text-bearing PDF profile and a
captured original page of that PDF. The current resident capture supplies
document UUID, page UUID, order and pixels. Buddy's
`workflow/resident_output/development.rs::recognizes_ordinary_page` demonstrates the
native PDF and page-table inputs. The installed input owner still needs a
read-only producer for these inputs. Add it beside `ResidentSourceOwner`
with a parser in `device/native_page.rs` that can consume the held directory's
bytes and the existing SDK facts. Reuse the native ordering and redirect
validation. The development output recognizer remains outside this route.

- Open the installation's Xochitl data root
  `/home/root/.local/share/remarkable/xochitl` through held directory
  descriptors. Use only the canonical, nonnil document UUID from the
  exact SDK observation and the matching selected registration. Open
  that UUID's `.content` and `.pdf` by basename relative to the held
  directory. Reuse the protected regular-file checks and stable descriptor
  identity from the existing bounded readers. Reject links, untrusted
  owners/permissions, ambiguous JSON or page maps, absent files, path or
  inode replacement, and unstable reads. Bound the content table at 1 MiB
  and original PDF at the existing 16 MiB input cap.
- After SDK Observe and before CaptureSource, read both files through held
  descriptors. Validate PDF type, exact ordered active page UUIDs against
  the observation, unique in-range original redirects, and an original
  redirect for the selected page. After the matching capture, reread both
  files and require the same original byte digests and identities. Both
  full passes run outside selected gates, with observed input ownership and
  the original acquisition deadline. Freeze directory/file identities,
  owner/mode/link count/length, nanosecond change and modification times,
  table and PDF SHA-256, original page count and redirect. Retain only
  the first accepted PDF bytes for processing.
- Before Prepare, credential resolution, each owned submission and each
  Interpret or Generate CAS, check the held descriptors and reopen the
  installed root path through no-follow directory descriptors. Verify the
  directory and both named entries still match the frozen identities and
  metadata. Repeat the short check under the ordered admission gates just
  before the action. No source content read or PDF parsing runs under those gates.
  A failed or changed check ends the request without taking another
  snapshot. The full passes establish original bytes around the capture.
  Later metadata checks detect observable replacement or change. Xochitl
  does not share the gates, so the boundary cannot prove uninterrupted
  freshness or exclude changes between observations or beneath filesystem
  timestamp resolution. The image remains historical evidence.
- This entry starts the fresh root currently produced by
  `ResidentPrepared::new`. Existing interpreted request/history assembly
  stays reusable for resumed turns. Selecting an existing conversation and
  inheriting its exact prior source are separate work and require an
  explicit prior-turn origin. A note page, unknown source, changed source,
  or unsupported PDF refuses before new model submission. True
  no-document input requires its own explicit admission.

### Owned PDF processing

The PDF parser and index builder run synchronously and have no cancellation
hook. On Linux, run both in one owned child of the installed Reader binary.
Add a private worker dispatch in `main.rs` before ordinary argument/config
startup. Spawn the exact running executable through `/proc/self/exe` and reuse
the bounded child observation and cancel/reap pattern in
`conversation_maintenance/service.rs` and `workflow/resident_runtime.rs`.
Accept only the exact internal worker invocation and its protocol version.
The worker receives an empty environment, bounded IPC on stdin/stdout and
stderr directed to null. Keep other descriptors close-on-exec.
It receives PDF bytes, never a source path, credential, Store, native handle
or inherited request authority. It spawns no children. Apply Linux
`RLIMIT_AS` of 256 MiB and `RLIMIT_CPU` of 20 seconds soft / 21 seconds hard
before processing. Refuse if the limits cannot be installed. These proposed
limits are part of the offline verification, alongside the parser's existing
format and input bounds.

- Use a versioned, typed frame with a fixed-width little-endian length on
  stdin/stdout. Reject excessive lengths before allocation.
  Admit one PDF frame of at most 16 MiB plus a fixed header with request and
  document IDs, input byte count and SHA-256, expected page count and
  extractor revision. The child checks exact length/digest and reuses
  `retrieval::pdf::normalize` and `Index::build`. It returns a ready frame
  containing its complete key and the canonical serialized units used to
  compute that key, plus its actual PDF page count. Cap the frame at 9 MiB.
  The parent hashes those exact unit bytes as they arrive, then discards
  them. It derives the expected complete `IndexKey`
  from that hash, its own admitted UUID/PDF digest, PDF format and declared
  extractor revision. Require equality with the built key and agreement
  on the native original page count. No cache identity enters the proof.
- The same child retains the index in memory. After a fresh Interpret, the
  existing assembler invokes the request's one-shot retrieval provider.
  Send one query frame of at most 4 KiB with the same request/key, exact
  question and admitted passage/neighbor limits. Use the existing
  `Index::query`. Require one response with the matching request/key and
  at most the existing 16 KiB encoded passage limit plus a fixed header,
  then EOF and exit zero. The parent uses the existing result validator and
  original one-based PDF locators. Valid zero matches stay source-bound.
  Extra frames, bad lengths/identities, trailing bytes or wrong exit refuse.
- The parent services nonblocking pipes and observes child exit with short,
  deadline-clamped polls. It waits for the ready frame within the original
  acquisition interval. The child consumes the same request's remaining
  lifetime and between-call allowance for the single query. Recheck input
  ownership while waiting and cancel on any refused stage, timeout, shutdown
  or unwind. Close both pipes, kill only the owned unreaped child if still
  running, and retain ownership until exit is observed and reaped. A child
  that cannot be reaped is a runtime failure with no new release or draft.
  Reserve the deadlines for accepting work and cancellation. They do not
  guarantee Linux can reap a stuck process by a fixed instant. No worker or
  pipe reader is detached.

## Freeze the context and admit dispatch

Use the freshly acknowledged Interpret token in
`Orchestrator::run_prepared`, immediately after `interpret_source_target`.
Before research or final answer work, use the existing selected read budget and
`SelectedDomainProjection::inspect` to verify exact acknowledged root, user,
and capture objects. Take the original interpreted turn, its admitted source
and the eligible model history strictly before that turn from the same
snapshot. First installed turns have empty prior history. Preserve the
established history eligibility, chronology, media reporting and byte limits.
Factor internal data assembly below `Ledger::assemble_request_context` so
the selected receiver passes its already-admitted records and media view.
Retain ordinary public types, formats and refusal of selected memory.
Evaluate any enabled memory once through `Attempt::query_memory`. Keep the
original view for joined gates, including observed empty. Reuse the bounded
memory report, research and citation logic with a crate-private admitted
selected input. Supply effective personalization as an explicit bounded
answer prompt part, separate from the exact frozen evidence JSON. Count the
complete descriptors and label the initial UTF-8 byte counter as a
conservative request-size bound, without a model tokenizer claim.

Use `ReaderPreferences::config()` for effective research policy and preserve
the explicit directive. Before reading any credential, admit the exact
Config, document pin, route, selected memory provider compatibility, and
model/endpoint configuration. For required research, the local block
selects `research_model` explicitly. Admit only the initial exact pair
`gpt-5.6-terra` and `https://api.openai.com/v1/responses`, which has
[retained standalone web-search evidence](../archive/2026-10-25-acquire-openai-web-research/tasks.md).
Reject a missing or different research profile before reading the secret.
This allowlist describes the initial search profile. Answering uses the
configured Chat Completions model independently, including an admitted
`gpt-6.1-terra` setting. The standalone search evidence establishes no
installed composition or answering-model capability. Use the existing
protected model credential reference and reader, after admitting its
destination. For this opt-in route use the admitted OpenAI Chat Completions
origin for the configured recognition/verification/answer model. Require
that origin and a protected reference before reading the secret. Do not
derive Responses eligibility from an arbitrary Chat Completions URL or
use environment or CLI credential overrides in this opt-in route. Split
non-secret selection from credential resolution in `config.rs` and
`selected_resident_reader.rs`; use only the resolved request-local secret.
Tests inject a loopback transport in the existing in-process fixture.
Disabled and per-release NoInternet produce their existing distinct zero-web
reports and skip research transport and search-profile admission. Read the
protected credential once for the admitted answer model and permit research
to borrow it only when its required profile was admitted. Required with
unavailable or invalid search evidence yields no answer. Keep summaries and
citations labeled by their actual provenance.

Use four ordered one-use stages in `reader_attempt/selected.rs`.
Analysis and independent verification use the same acknowledged images and
retain their existing prompts and checks. Interpret must be freshly
acknowledged before research. Use the research adapter and final answer
consumer in place of legacy enrichment, then publish one draft. Disabled
or NoInternet marks research skipped, giving three submissions. The
analysis proposal can never be published as the researched answer.

- Keep the existing 420-second deadline from genuine release. Use up to
  90 seconds through the first handoff, at most 67 seconds per provider
  stage, and the existing 60 seconds total for between-call and final
  publication/readback. Clamp each worker to the original remaining time.
  An unused stage never extends a deadline or permits a replacement call.
- Reserve source and selected reads from one request allowance before
  admission. Allow two full source passes outside gates, with a combined
  34 MiB cap for successful source bytes. Use the admitted file lengths
  to size reads and one one-byte EOF probe per file. Charge every read
  call, including short reads and EOF. A full pass allows 512 PDF reads,
  32 table reads and two EOF probes, for at most 1,092 calls across both
  passes. A nonempty probe refuses. Extra calls exhaust the reservation.
  Reserve two metadata samples per full pass and two per
  action at Prepare, credential resolution, four submissions and two
  publication CASes. Each sample allows at most 64 actual path,
  descriptor and stat operations. This is 1,280 metadata work items
  across the request, allocated to the acquisition, submission and
  result partitions. Reserve separate IPC byte and work bounds before
  spawning, using the declared frame caps and at most 2,048 nonblocking
  read/write attempts, including EOF and any short calls. Poll readiness before attempting I/O and use
  bounded 32 KiB chunks. Progress may observe input and current selection
  without rereading source content. Reserve the existing bounded memory
  query once, allow a full joined proof for each of the four submission
  slots, and keep progress separate.
  Use the existing 333 ms selected progress cadence over the full
  parent lifetime, with boundary checks charged to their stage. Give
  guarded web transport this cadence instead of its ordinary 50 ms
  callback. Exhaustion or cancellation joins the worker and ends the
  original request.
- Factor the private answer execution seam below `answer::answer` and the
  web worker submission seam below `OpenAIWebResearch`. Use the existing
  owned model handoff pattern for both. Take ordered document, catalog,
  preference and applicable memory/handwriting gates, revalidate the exact
  selection, source pin, input ownership and deadline, then allow the one
  submission. Release gates before the worker waits. Verify again at the
  next actual handoff and at Generated CAS. Join the same memory result
  for research, answering and generation. A provider progress callback
  cannot mint a submission, refresh input or renew the reservation.

## Generated publication and verification

Keep the strict captured-citation validator in `receiving/answer.rs`.
Append a bounded reference list to the existing Generated text in order of
first marker occurrence. Source cites original PDF page and document identity,
memory cites the exact fact record/revision, and research
cites the validated title and HTTPS locator with its evidence label.
Clarifications have no citations. Bound the complete text and refuse
overflow. The existing selected Generate CAS and receipt bind the exact
text, accepted token, user/root references and operation. Freeze them once
and recover only the original acknowledgment after uncertainty. Recovery
must avoid acquisition, reads of current source or preferences for
authorization, resubmission and additional Generated or native effects.
A stale or canceled request retains its last acknowledged state.

Extend the actual resident receiver fixture in
`storage/sync/selected/tests.rs` and the existing guarded HTTP and historical
receiving fixtures. Exercise the real source producer against a temporary
Xochitl-shaped directory, including a nonzero original redirect, changed
same-UUID bytes, reordered or ambiguous pages, changed links/inodes, limits
and exact-key zero matches. Exercise the same-binary child and framed
transport under stalled parse/query, memory or CPU exhaustion, invalid
digest/key/frame/EOF and abrupt exit. Assert cancellation observes child
exit and reaps it before another request. Use two candidate PDFs to prove only the
captured document is queried. Assert unchanged request/history, exact
outbound stage order, payloads and citation locators, and one durable
Generated draft. Cover equivalent-corner rejection, crossing, Writer
arbitration and both release directives, effective Disabled,
required-but-unavailable, pure and mixed selected memory including empty,
precredential refusal, drift before a handoff or CAS, withheld responses,
budget/cadence exhaustion, and lost acknowledgment without replay.
Retain ordinary no-document, selected-memory refusal, and ordinary
three-stage controls. Assert zero ordinary or native output mutations.

Fixture and hosted CI evidence qualify source composition and loopback
transport. Installed RM2 evidence separately qualifies the actual file
custody, gesture and original-page observation. Live model/provider evidence
separately qualifies the explicit Responses model and useful citation
behavior. Source implementation and CI can proceed with the existing
offline fixtures.
