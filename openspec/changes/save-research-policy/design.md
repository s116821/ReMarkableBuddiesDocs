## Context
The research stage defaults to Required and admits Disabled separately from
per-request NoInternet. Config lacks that declaration. Existing memory/model/basic
editors use checked_document, Ordered encoding, Custody and the same guarded
Store::replace_config_document publication/readback; that machinery remains owner.
Main owns the producer; SCRAPPY owns separately reviewed companion consumers.

## Decisions
Add optional root `research_policy: Option<ResearchPolicy>` to Config, reusing the
existing enum. Default None and skip serialization when None preserve existing
default/absent Config encodings. Omitted or explicit null resolves to Required;
explicit required/disabled preserves its declaration. Whole-file strict parsing
still rejects duplicates, unknown fields, invalid enum/type/schema and size.
An old binary may refuse a new declared field; do not silently rewrite/migrate it.

A pure `Config::research_policy_snapshot()` validates values without declared-root
I/O and returns an immutable typed value exposing policy(). None resolves to
Required. It performs no file/environment/credential/Store/provider lookup and
does not attest disk bytes or runtime state. Capturing another snapshot observes
a later Config value; an existing snapshot stays unchanged. Feed policy() directly
into the existing ResearchInput; do not change with_research or request directives.

A dedicated producer uses contract.md and the existing checked-document/custody/
conditional writer. It edits only the root declaration. No-op preserves raw bytes;
a change uses Ordered JSON while retaining unrelated values and presence. Inspect,
prepare and status never open Store or probe declared roots. Apply revalidates the
same original file/path/patch/target and existing Store/mode custody; no initialize,
repair, stop/restart, new ledger/writer or implicit retry. Hold custody until the
consuming report write completes/fails; keep prefix-output uncertainty honest.

The existing broad inspection v1 wire stays byte/shape compatible: its 25-field
allowlist and six unsupported-view entries remain unchanged. Its research-policy
entry means this broad view does not expose the setting; the dedicated producer
does. Existing basic/model/memory/personalization editors must preserve the new
declaration. No Manager parser/UI/private reference or transport deadline changes.

Main adds only an early explicit maintenance CLI route, mutually exclusive with
existing operations. Unsupported file inputs never become staging workarounds.
Ordinary startup, gesture/Reader lifetime, prompts and native effects stay intact.

## Verification
Exercise strict Config defaults/null/enum/duplicates, default encoding preservation,
typed snapshot immutability and unchanged old inspection output. Use real temporary
existing Store/config plus actual CLI inspect/prepare/apply/status for set/clear,
no-op, foreign path/base/patch/target, Busy/mode changes, output-prefix failure and
unknown publication/status semantics. Reuse existing fault hooks; no new test-only
publication engine. Verify unrelated fields/origins/roots and other editors remain.

Save/reload actual temporary configuration and pass its typed policy snapshot into
the actual research stage over real frozen request/history/source/memory frames.
Use a synthetic Provider to prove Required attempts/refuses honestly, Disabled and
NoInternet make zero calls with distinct reasons, NoInternet dominates both saved
policies, and prior request/history/encoded bytes remain exact. No credentials,
network/model/tablet or live research are contacted. These tests qualify saved
configuration/local composition only, not automatic runtime consumption.

## Delivery
Prepare linked Docs/Source PRs; freeze exact pairs, inspect feedback and complete
the full verify/sync/archive/final review/Docs-first workflow. Actual merge/main CI
and new publication remain external observations, pending until actually observed.
