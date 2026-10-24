# Design

## Current mechanisms and ownership

`RequestSource` already expresses explicit NoDocument or Original with origin turn,
source record and complete IndexKey. The receiver validates a coherent ordinary
snapshot and queries the supplied local Provider. RequestEvidence preserves an
exact historical frame per operation; multiple operations for one request are
intentional and do not identify an active choice or model consumption.

BindingReceipt records a page claim, not a document-source registry. Retained
Reader original-source accessors concern synthetic placement observations. Writer
owns supplied normalized-text selections. Neither is changed or copied here.

## Additive API

Add `conversation::resolution` with `SourceDirective`:

- `Explicit(RequestSource)` deliberately sets or clears the source.
- `Inherit { request_turn, operation: Option<Uuid>, expected: Option<IndexKey> }`
  declares the prior request and a specific evidence operation to carry forward.

Add `Ledger::resolve_request_source(conversation, request_turn, directive)` returning
an ordinary `RequestSource` or a typed `SourceResolutionRefusal` through the
existing Result convention. No serialization or persisted record is introduced.

An omitted operation refuses with AnchorRequired even if only one selection
exists. This is an unresolved caller declaration, not evidence that the ledger
found multiple candidates. Named operations resolve independently even when other
operations for the same request disagree. Never scan for a latest timestamp,
smallest ID, successful-looking acknowledgment or current Buddy page.

## Admission order and semantics

Validate a non-nil conversation and current interpreted Reader user request using
ordinary non-retained inspection. Explicit directives reuse original-association
validation; explicit NoDocument remains valid regardless of earlier choices.

Inheritance requires a non-nil prior request/operation, a validated committed fact
from existing bounded request_evidence readback, and a prior interpreted Reader
request strictly earlier than the current request in the same conversation. A
missing, foreign, deleted, conflicted, unsupported or corrupt dependency refuses;
no historical retained winner is promoted into the current conversation.

For prior NoDocument, expected must be absent and output is NoDocument. For prior
Original, require a newly caller-supplied complete expected key, derive only the
origin turn/source ID from the validated historical frame, and reuse current
ordinary original-association validation. Require the current source record's
content to equal that preserved in the named historical frame; changed content
refuses. This does not assert identical current revision identity: an identical
content successor may resolve, and later receiving/publication still admits its
own snapshot. Historical immutable identity remains preserved in the original
evidence fact. Never copy its saved expected key as a freshness witness.

The fresh supplied key may differ from the historical key when the same document
has been independently reindexed. The resolver checks complete key shape and
document identity, not source freshness. A stale but structurally valid key can
resolve; the existing Provider/receiver must reject a mismatched current index.
Do not claim provenance of independent acquisition can be mechanically proven.

## Snapshot and bounds

Read validated historical evidence, then inspect one current ordinary conversation
snapshot and validate the target, prior turn and source against it. There are no
Provider/tokenizer callbacks. Resolution is read-only historical data, not a lock
or preparation spanning a later receiving call. Changes after resolution are
rechecked by existing receiving and durable-preparation admission. Preserve their
APIs/schema and never silently requery or publish here.

Reuse existing metadata/reference bounds and original-source encoding cap. Do not
add unbounded enumeration of evidence operations. Error Display text contains no
user request, source text, raw provider error, private path or record body.

## Verification and lifecycle

Use public real temporary Store/Index fixtures, following the shared simulator
checklist. Cover explicit original/no-source changes, inherited original/no-source,
two disagreeing operations for one prior request, missing anchor, wrong/future/same
request, foreign/missing/corrupt facts, invalid keys, changed source content,
historical-key replacement, stale Provider refusal after resolution, restart and
unchanged Store heads. Resolution must make zero Provider calls and zero writes.
Preserve original receiving and evidence regressions and normal quality checks.

No model/native behavior changes; live model or tablet evidence would not qualify
this data adapter. Obtain independent precode review before Source implementation,
then exact-revision paired review/CI, own canonical sync/archive and normal
Docs-first/Rust-second squash delivery. Broader routing, default research and
automatic active-source policy remain open.
