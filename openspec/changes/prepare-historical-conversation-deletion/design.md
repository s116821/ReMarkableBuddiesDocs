# Design and source basis

## Current facts
Source baseline053c31499988c132bcf2342424aeb6aadba221a9, Docs baseline
f3c7e7c3f1a3d6f2cb0526f10ae96e9d5859357d. Current Ledger::delete checks full
root/binding heads and publishes their tombstones plus a receipt; its retry returns
historical facts without revival. Existing tests cover retained/shared media.
Store::open_existing retains the OS lease and runs recover: committed metadata and
required media are read/hash-validated into an in-memory index; no repair, staging
cleanup, chmod or disk-index publication is performed by that recovery loop.
It currently does not impose a whole-store aggregate read budget. Root schema1
alone does not establish that all descendants are ordinary or settled.

Source files: src/conversation/{mod,types}.rs, tests/conversation.rs,
src/storage/{mod,maintenance,conditional,inspection}.rs and sync/mode.rs.
Canonical inputs: historical-conversation-ledger, shared-storage,
storage-existing-maintenance and owned-data-inspection. Current project tracking
requires selective cleanup, inactive-unit confirmation, writer exclusion and
retention of original/source material. Proposed API/budgets are design decisions,
not implemented behavior or native evidence.

## Admission and privacy
Use a new isolated maintenance module and additive existing-only bounded Store
admission. Preserve legacy APIs/recovery behavior and all existing closed wires.
The new admission acquires existing store.lock once; under that lease validate
known ownership/ordinary-generation headers and perform conservative metadata
budget checks BEFORE existing recovery. Never construct an empty-index ordinary
Store for preview. Reject selected-format/feature/history and unknown root entries;
never activate or migrate a generation. The new recovery path must enforce one cumulative512MiB content/65536-reference
budget across repeated hashing/record rereads/dependency passes and receipt work;
unique inventory length alone is insufficient. Existing legacy recovery stays
unchanged. New admission validates only admitted committed objects within both
inventory and cumulative work bounds, with no unbudgeted fallback. Temporary
stage files count toward inventory bounds but remain unread and untouched.
No credential resolver or credential payload read follows; only existing known
ownership marker validation required by Store admission is permitted.

A fixed read-only systemctl show observation provides service admission. Neither
Config enable flags, LocalOnly, PID files nor acquiring the Store lease alone is
called proof of inactivity. The unit can change after observation; the retained
Store lease excludes cooperating runtime access across that race. Reobserve the
unit under custody before preparation output or apply publication. Never stop,
start, reload, disable, reset or repair a unit. Non-Linux refuses before input or
OS/filesystem access. No actual tablet or real service is contacted in this work.

## Logical transaction and exact retry
Build a deterministic original-bound transaction containing root tombstone,
optional binding tombstone and a schema-one conversation receipt. Reuse existing
Store atomic publication/recovery, historical payload types and stable operation
receipt identity. Add a private narrowly scoped multi-record conditional publisher;
do not change Ledger::delete semantics or selected/native paths. One Store mutex
spans exact generation, original target history/root/binding, receipt absence and
publication. An ordinary mode lease pins absent/explicit LocalOnly and excludes
workers. No source/media/export-association record is tombstoned or unlinked.

The receipt fingerprint binds the COMPLETE original intent digest, not merely the
conversation UUID. Exact original retry recognizes that transaction BEFORE fresh-live eligibility;
later target revisions never become a current-history-equality precondition for
the old acknowledgment. Retained original root/binding bytes still must match.
Exact original retry observes the same deterministic transaction;
changed-content reuse refuses. Historical receipt acknowledgment and current root
state remain distinct. A later conflict/revival does not erase the original receipt
or authorize another write. After publication is attempted, any unverified outcome
is unknown; never retry, roll back, compensate or automatically prepare again.
Only explicit status of the original intent can resolve historical publication.

## Eligibility and costs
Validate the complete relevant supported history/heads and ordinary Ledger view,
not a guessed payload subset. Reject conflicts, unavailable commits, invalid
domain records, schema2, selected/intent/settlement facts and pending or uncertain
current turns/exports. Preserve all historical revisions and media, even after
deletion. This does not implement physical garbage collection or sync deletion.
Normal settled history includes Interpreted user requests paired by exact exchange
with one later terminal assistant. The contract states required completion/outcome
facts, ancestry and ambiguity refusals; existing user history is never rewritten.
Immutable outcome facts are not automatically current uncertainty.
Before prepare/first publication reserve final and partial transaction inventory,
target history and prospective recovery-work headroom. Exact deterministic orphan
objects after interruption permit bounded original status only, never a new apply.
Whole-store conservative budget refusal may reject a small target in a large
store; do not return a partial view or quietly increase limits.

## Verification limits
Pure fixtures with an injected typed service observer prove eligibility,
transaction/readback/refusal and failure behavior. The injected observer exists
only in test/internal dependency seams and cannot be selected through public CLI,
Config, environment or a request. Executed actual Linux CLI controls stop before
the production observer, at selector/parser/missing-Config refusals. Controlled
synthetic subprocesses separately exercise the observer runner; no actual systemd
unit is queried. Windows tests prove unsupported and parser boundaries only. New modeled cases are storage/OS
fixtures; there is no gesture/page simulator behavior to invent.

Read-only OS interface reference: [systemctl official manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#show%20%5BPATTERN%E2%80%A6%7CJOB%E2%80%A6%5D).
The manual documents machine-parsable show/properties; exact acceptance and bounds
below are our conservative proposed contract, not a claim of device qualification.
