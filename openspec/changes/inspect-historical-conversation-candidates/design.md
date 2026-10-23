# Design and source basis

## Verified baseline and scope inference
Actual Buddy main66d46ee5b1e3d145bf56ef5be991d5a5b70698ff/tree
0105c5aab26e14779b23d4a6ae32cbe4b068fb06 and Docs main
017955736a59be781e79888ccc4518615533cbcf are the starting points.
The maintenance route and Ledger::inspect both require one conversation UUID.
OwnedDataReport exposes aggregate namespace/file/reference accounting and declares
logical_liveness_evaluated=false; it contains no conversation-ID collection.
These are current source/contract facts, not an observed installed-UI failure.
The selection need is inferred from the selective owned-data requirement.

Source basis: src/main.rs, conversation/{mod,types,cleanup}.rs,
conversation_maintenance{.rs,/engine.rs,/service.rs}, storage/{inspection,
conversation_cleanup,maintenance}.rs; canonical historical-conversation-ledger,
owned-data-inspection and prepared-conversation-deletion requirements.

## Separate wire and retained safety controls
Use a new parameterless route/report, not another value in the released deletion
Operation or Status enums. The caller has no path/filter/input override or nonce.
Preserve every existing CLI default, conflict outcome, selector and frozen vector.
Reuse the existing fixed observer, Config/Store/mode checks and bounded recovery
where they fit. Add isolated internal helpers or carefully factor private admission
without changing old branch order, reports or publication semantics. Focused old
producer regressions must cover any shared refactor. No public injection seam.

This inventory reads and decodes owned persisted payloads; it is not metadata-only.
Existing Store initialization/recovery fallback is forbidden. The same bounded
existing-only Session retains its original Store lease, ordinary mode guard,
header facts and sticky cumulative budget through final output or failure.
No transaction Plan, nonce reservation or publication headroom is required for a
read-only collection. Actual filesystem/read-work caps remain unchanged.

## Root classification and completeness
Scan all retained Conversation-namespace envelopes under one Store mutex. Require
ordinary schema one, original supported typed value decoding and envelope/payload
identity agreement; unknown/schema-two/admitted/settlement history refuses the
whole inventory. Other namespaces are not a second root-discovery mechanism,
although normal bounded recovery still validates all owned envelope/media bytes.

Collect IDs with any retained typed Root value. For those IDs, reject retained
value-type reuse as another record kind and reject ambiguous/missing current head
sets. A singleton current Root value is a candidate; a singleton current tombstone
is excluded. A non-Root current value under a known root ID is conflict, not silent
absence. Deleted-only history can therefore yield a complete empty candidate list.
Do not emit a partial list on conflict, unsupported history or more than sixteen
current candidates. Sort unique canonical UUID strings lexically and report the
exact list length. Root presence is not descendant eligibility: a structurally valid
root with pending/conflicted turns may still be listed; fresh existing inspect/
prepare decides whether that explicitly selected target is eligible.

## Cost and custody
Keep the released whole-generation inventory and cumulative512MiB/65536-visit
limits. Charge before each new record/head/reference visit and before each typed
payload reread/deserialize, using already-admitted object length rather than an
unmetered serialization to discover its size. Never reset work per root or use
unbudgeted Ledger/Store recovery. Typed classification is bounded by the same
admitted current-generation files. Retained root count may exceed sixteen when
the current non-tombstoned candidate count does not; traversal is still metered.

Classify one consistent in-memory index while holding its mutex, then retain the
existing OS/mode leases and original file facts. Bracket the final fixed observer
with Config/header/named-lock/owned-file checks, clearing candidate fields if
custody changes. After fully safe admission, even discovery refusals retain custody
through response/failure. Early admission refusals expose no candidate state.
These guards exclude cooperating writers; they do not certify malicious external
filesystem modification or real device/power-loss behavior.

## Evidence and remaining gates
Use only typed observer and controlled subprocess fixtures; the fixed production
systemctl observer is never invoked by this lane. Actual CLI cases stop before it,
at unsupported/conflicting invocation or missing Config. Exercise true empty,
deleted, mixed history, deterministic order,16/17 boundary, root conflicts/type
reuse/schema/corruption, work exhaustion, output loss and custody races. Preserve
all bytes/modes/mtime where inspected, stage files and original documents.
Current source/fixture/build evidence is distinct from real-unit, tablet, provider,
native/runtime and Manager qualification. Independent precode and implementation
review, exact-current CI and the complete paired lifecycle remain required.
