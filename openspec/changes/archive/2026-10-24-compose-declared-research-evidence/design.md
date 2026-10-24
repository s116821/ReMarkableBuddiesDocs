# Ordinary declared research boundary

## Placement and preserved ownership

Add `conversation::receiving::memory::research` and
`FrozenSourceMemoryContext::with_research(input, CombinedBudget, counter)` returning
an owned `FrozenResearchContext`. The module is a child of the existing memory
composition module so it can serialize the existing private frame without public
field exposure or a parallel context model. Add only that child declaration to the
old module; preserve its existing source/memory composition and durable schemas.

The result owns the original FrozenSourceMemoryContext, exposes it by shared
reference, and retains its exact encoded_json/count/request/history/source/memory
objects unchanged. A transient schema1 research wrapper nests the same existing
CombinedFrame and adds an explicitly untrusted research report. Its existing
source-only/source+memory/evidence APIs remain valid. The new object cannot become
a prepared durable request-evidence write or selected/native/model admission.
No Ledger/source/memory query, Store write or configuration lookup occurs here.

Current source/memory frames are ordinary historical observations, not a joint
currentness lease. Keep REM-39 exact request/history and the preset/personalization
separation. No fake turn, summary, instruction or rewritten question is inserted.
Research policy is a supplied typed value, not a new persisted configuration or
provider registry; REM-42/Manager ownership and installed policy resolution stay
separate. Source acquisition, native identity and existing held work stay held.

## Policy and Provider contract

`ResearchPolicy` defaults to Required; its other value is Disabled.
`ResearchDirective` defaults to UsePolicy; its other value is NoInternet.
`ResearchInput` carries policy/directive, optional borrowed Provider and options.
Options carry explicit positive now_ms,1..4max_queries,1..8max_sources and
256..16384max_evidence_bytes. No wall-clock lookup is made.

Resolve NoInternet first: status Disabled/reason RequestNoInternet, zero provider
calls even if a provider or invalid research options were supplied. Otherwise
Disabled policy gives Disabled/reason ConfiguredDisabled, also zero calls. Offline
options are unused and no dispatch identity/query/evidence is fabricated. Both
paths still validate the complete output budget and final encoding/counter.
This API does not parse natural-language opt-outs: the caller must supply an
authoritative explicit directive. Future request/config resolution must preserve
that requirement; absence of a provider is never an offline choice.

Required validates options and complete byte preflight before one Provider call.
Missing provider, callback error or Unavailable status returns typed unavailable;
there is no retry, offline fallback, dropped research or empty-success substitution.
The synchronous callback has no new timeout/cancellation/network implementation;
the caller's acquisition/runtime contract remains separate.

A borrowed ResearchRequest gives the Provider the entire immutable frozen context,
its options and a generated ResearchIdentity: conversation UUID, request-turn UUID,
SHA256 of exact source/memory encoded_json and explicit observed_ms. The Provider
can read exact request/history/source/memory through existing accessors; no 2048-byte
question truncation or context summary is substituted. The already-qualified
context bounds remain applicable, including larger NoDocument requests with memory
disabled. Claimed search-query strings in a result are separate untrusted data:
they never replace the user's question/history. Future actual query construction
and network privacy/authorization are not qualified by this callback seam.

Provider returns an owned typed ResearchResult with matching identity, status,
optional bounded diagnostic enum, evidence basis, claimed queries and citations.
EvidenceBasis is Synthetic or ProviderAsserted; neither means source-verified,
performed network research or effect admission. Fixtures must use Synthetic and
state that provenance. The output report always labels data
`provider-asserted-unverified` and retains its explicit basis.

## Result admission and bounds

Check identity exactly before result encoding: wrong context, turn, conversation
or observation time refuses. Recognized statuses are CompleteEmpty, Complete,
Partial and Unavailable; the report additionally has Disabled for skipped policy.
CompleteEmpty has zero sources/no diagnostic; Complete has at least one source/no
diagnostic; Partial has a diagnostic (BudgetLimited, SourceUnavailable or
ProviderFailure) and may have zero sources. Every admitted called-provider result
has1..max_queries distinct nonblank query strings and at most max_sources sources.
Unavailable refuses the whole composition regardless of other payload; it never
becomes empty or partial. An unrecognized/contradictory typed shape refuses.

Each claimed query is<=2048UTF8 bytes, no NUL/disallowed controls; whitespace is
retained, not trimmed for output. Each citation has nonblank title<=512bytes,
nonblank excerpt<=4096bytes, URL<=2048bytes and optional positive published_ms not
after observed_ms. Text permits ordinary CR/LF/tab but no other controls. Use the
existing pinned reqwest::Url reexport to validate absolute HTTPS with host and no
username/password/fragment; do not fetch URLs, resolve hosts or inspect credentials.
Reject duplicate parsed canonical URLs rather than silently merging or discarding
excerpts; preserve accepted original strings. Query duplicates use exact bytes.
These syntax/time constraints do not verify truth, source ownership, safety,
publication time, excerpt accuracy or actual external search execution.

Validate vector counts and individual lengths before cloning/walking/encoding
returned data. Bounded report serialization, including identity, status, diagnostic,
queries, citations, basis/authority labels and JSON escaping, must fit
max_evidence_bytes or refuse without partial text. Caller-provided Provider data
is already allocated; these checks do not bound callback acquisition/allocation.
No global RAM/CPU/deadline, HTTP/SSRF policy or source-verification claim is added.

Reuse CombinedBudget:512..524288 complete encoded bytes and positive token limit.
Before Required query, serialize the complete outer wrapper with research:null as
a byte lower-bound preflight, including prior source/memory frame and new labels.
It proves no token lower bound. Serialize the final complete wrapper with the
admitted/disabled report, then invoke the supplied counter exactly once. Do not
sum component counts or assume tokenization is monotonic. Zero/error count or
exhaustion refuses without dropping research or shortening request/history.
Typed errors have canned displays without provider errors, URLs, questions,
excerpts, credentials or filesystem paths.

## Historical compatibility and verification

No new persistent schema, Store mutation, source IndexKey/cache identity or model
request is produced. A callback may reenter/mutate local Store data while the
captured context remains immutable; hold no Store/currentness locks here and do
not upgrade old source/memory assertions afterward. Research report provenance is
an additional declared observation, not an atomic Store snapshot or native lease.

Use actual temporary Store/Index/LocalMemory contexts and authored synthetic
Providers to verify default-required/no-provider refusal, explicit no-internet
dominance/zero calls, configured-disabled distinction, exact callback context and
unchanged prior bytes, nonempty/empty/partial/unavailable outcomes, foreign identity,
malformed/duplicate/oversized URL/query/text/time shapes, complete evidence/wrapper
escaping limits, exact byte/token boundaries and nonmonotonic counter controls.
Verify64KiB NoDocument requests are not truncated, reentrant callback mutation and
sanitized errors, no retries and no new source/memory queries/Store writes. Preserve
existing source/memory/durable-evidence and selected-refusal controls. These fixtures
do not deliver a live search backend, validate real source truth or qualify an
answering model/installed Reader; those remain explicit later gates.

Review exact precode before source edits. Qualify the exact successor with affected
integration, full default library, strict all-target/all-feature lint, default
library check, fmt/diff, central guidance/strict and current hosted CI. Preserve
failures, obtain independent implementation acceptance, sync/archive only this
increment, then final paired review, normal Docs-first delivery and separately
observed actual-main/new publication. Broader research/runtime/MVP stays unfinished.
